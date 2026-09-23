"""La hoja de bombas del operario, siempre con el mismo diseno.

    python3 motor/hoja_bomba.py 39      # lee 05-programacion/hojas-operario/bombas/semana-39.csv

Vanessa 2026-09-23: *"cada vez que generamos este PDF me lo haces distinto"*. Por
eso el diseno vive AQUI, no en cada sesion: la semana solo cambia el CSV de
entrada (que hoja, que bomba, que dia, a que hora, quien).

Reglas del diseno (no se negocian sesion a sesion):
  - Una hoja por pagina. Titulo grande en negrita: PREFLORACION · FLORACION,
    DESARROLLO · VEGETATIVO, REFUERZOS.
  - Dia sugerido, hora y operario.
  - Los productos en lista, EN ORDEN DE MEZCLA, con la cantidad para 25 L.
    Nada de dosis, camas, bloques ni explicaciones: el operario ya sabe
    distinguir las etapas.
  - REFUERZOS junta en una sola hoja todas las filas con ese titulo, una
    seccion por subtitulo (Matricaria, Statice...).

Las cantidades salen de bombas_catalogo.csv (receta vigente a la fecha de la
hoja) y el orden de 07-datos/orden_mezcla.csv. Un producto sin paso de mezcla
detiene la hoja: no se adivina donde va en el tanque.
"""
import sys, os, csv, datetime, subprocess, glob, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lotes as L

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(RAIZ, "05-programacion", "hojas-operario", "bombas")
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

CSS = """
  @page{size:letter;margin:16mm 16mm}
  *{box-sizing:border-box}
  body{margin:0;color:#1A1A1A;background:#fff;
       font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}
  .hoja{page-break-after:always;min-height:240mm}
  .hoja:last-child{page-break-after:auto}
  .marca{font-size:10pt;letter-spacing:.2em;text-transform:uppercase;color:#555;
         margin:0 0 18mm;border-bottom:1px solid #D0C8B8;padding-bottom:3mm}
  h1{font-size:34pt;font-weight:800;line-height:1.1;margin:0 0 8mm}
  .cuando{font-size:18pt;font-weight:700;margin:0 0 2mm}
  .quien{font-size:14pt;color:#555;margin:0 0 12mm}
  h2{font-size:20pt;font-weight:800;margin:10mm 0 3mm;padding-top:4mm;border-top:2px solid #1A1A1A}
  .en{font-size:13pt;color:#555;margin:0 0 3mm}
  table{width:100%;border-collapse:collapse;font-size:17pt}
  td{padding:3.2mm 0;border-bottom:1px solid #D0C8B8}
  td.n{width:12mm;font-weight:800;color:#555}
  td.p{font-weight:700}
  td.c{text-align:right;font-weight:800;white-space:nowrap}
"""


def num(v):
    s = ("%g" % float(v)).replace(".", ",")
    return s


def receta(bomba_id, fecha):
    orden = {}
    for r in L.leer("orden_mezcla.csv"):
        orden[r["producto"].strip()] = int(r["paso"])
    items = []
    for i, r in enumerate(L.leer("bombas_catalogo.csv")):
        if r["bomba_id"] != bomba_id:
            continue
        desde, hasta = r["vigencia_desde"].strip(), r["vigencia_hasta"].strip()
        if (desde and desde > fecha) or (hasta and hasta <= fecha):
            continue
        prod = r["producto"].strip()
        if prod not in orden:
            raise SystemExit("%s (bomba %s) no tiene paso en orden_mezcla.csv. "
                             "Agregalo antes de imprimir la hoja." % (prod, bomba_id))
        items.append((orden[prod], i, prod, r["dosis_25L"], r["unidad"]))
    if not items:
        raise SystemExit("La bomba %s no tiene receta vigente al %s." % (bomba_id, fecha))
    return [(p, "%s %s" % (num(d), u)) for _, _, p, d, u in sorted(items)]


def lista(items):
    filas = "".join('<tr><td class="n">%d</td><td class="p">%s</td><td class="c">%s</td></tr>'
                    % (k, html.escape(p), html.escape(c)) for k, (p, c) in enumerate(items, 1))
    return '<p class="en">En 25 litros, en este orden:</p><table>%s</table>' % filas


def generar(semana):
    ruta = os.path.join(DIR, "semana-%d.csv" % semana)
    with open(ruta, encoding="utf-8") as f:
        filas = sorted(csv.DictReader(f), key=lambda r: int(r["orden"]))
    hojas, por_titulo = [], {}
    for r in filas:
        t = r["titulo"].strip()
        if t not in por_titulo:
            por_titulo[t] = {"r": r, "secciones": []}
            hojas.append(por_titulo[t])
        por_titulo[t]["secciones"].append(r)
    cuerpo = []
    for h in hojas:
        r = h["r"]
        d = datetime.date.fromisoformat(r["fecha"])
        partes = ['<div class="hoja">',
                  '<p class="marca">Dreams Can Bloom · Bombas · Semana %d</p>' % semana,
                  "<h1>%s</h1>" % html.escape(r["titulo"]),
                  '<p class="cuando">%s %s · %s</p>' % (DIAS[d.weekday()], d.strftime("%d/%m"),
                                                        html.escape(r["hora"])),
                  '<p class="quien">%s</p>' % html.escape(r["operario"])]
        for s in h["secciones"]:
            if s["subtitulo"].strip():
                partes.append("<h2>%s</h2>" % html.escape(s["subtitulo"]))
            partes.append(lista(receta(s["bomba_id"], s["fecha"])))
        partes.append("</div>")
        cuerpo.append("".join(partes))
    doc = ("<!doctype html><meta charset='utf-8'><title>Bombas semana %d</title>"
           "<style>%s</style>%s" % (semana, CSS, "".join(cuerpo)))
    out_html = os.path.join(DIR, "semana-%d.html" % semana)
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(doc)
    pdf = os.path.join(RAIZ, "05-programacion", "hojas-operario", "pdf",
                       "DCB-Bombas-Semana-%d.pdf" % semana)
    chrome = (glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome") or ["chromium"])[0]
    subprocess.run([chrome, "--headless", "--no-sandbox", "--no-pdf-header-footer",
                    "--print-to-pdf=" + pdf, out_html],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print("Hoja: %s\nPDF:  %s  (%d hojas)" % (out_html, pdf, len(hojas)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    generar(int(sys.argv[1]))
