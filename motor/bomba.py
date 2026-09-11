#!/usr/bin/env python3
"""La sesion semanal de bombas: ver antes de decidir, y dejar registro al aplicar.

    python3 motor/bomba.py semana 37        # la mesa para disenar la bomba de la semana
    python3 motor/bomba.py catalogo         # las bombas y sus dosis
    python3 motor/bomba.py registrar 2026-09-12 37 "3B,3C" CHOQUE-BO 4 Wilson "oidio en lisianthus"

`semana` es OBLIGATORIO antes de recomendar nada — es la regla APLICACIONES de
CLAUDE.md hecha comando: muestra la rotacion de las ultimas 4 semanas y que hay
sembrado en cada bloque, para que la bomba se disene sobre lo que hay, no de
memoria.

`registrar` escribe en `07-datos/aplicaciones_lote.csv` con el BLOQUE, que es lo
que permite que la aplicacion se le sume despues a la ficha de cada cosecha.
Sin bloque la fila queda huerfana y no le suma a nadie.
"""
import sys, os, csv, io, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lotes as L

ANCHO = 92


def _cohortes_por_bloque(semana):
    idx = L.ocupacion(tope_semana=semana)
    out = collections.defaultdict(list)
    for r in L.leer("ocupacion_lote.csv"):
        for b in L.bloques_de(r.get("bloque") or ""):
            for coh, frac, exacto in L.reparto(b, semana, idx):
                if coh not in out[b]:
                    out[b].append(coh)
    return out


def cmd_semana(semana):
    print("=" * ANCHO)
    print("MESA DE BOMBA — SEMANA %d" % semana)
    print("=" * ANCHO)

    print("\n1. ROTACION DE LAS ULTIMAS 4 SEMANAS  (regla APLICACIONES: mirar antes de decidir)")
    print("-" * ANCHO)
    rot = L.rotacion(semana - 4, semana - 1)
    if not rot:
        print("   SIN REGISTRO en las semanas %d a %d." % (semana - 4, semana - 1))
        print("   NO se puede recomendar rotacion: no hay contra que rotar.")
        print("   aplicaciones_lote.csv esta vacio o no cubre este periodo.")
    else:
        for w in sorted(rot):
            for r in rot[w]:
                print("   sem %-3s %-12s %-14s %s" % (
                    w, r.get("bomba_id", ""), r.get("bloque", "") or "SIN BLOQUE",
                    r.get("motivo", "")[:40]))

    print("\n2. QUE HAY SEMBRADO ESTA SEMANA  (a quien le va a caer la bomba)")
    print("-" * ANCHO)
    porb = _cohortes_por_bloque(semana)
    if not porb:
        print("   Ninguna cohorte con ocupacion registrada en la semana %d." % semana)
        print("   Llenar 07-datos/ocupacion_lote.csv — sin eso nada se puede imputar.")
    else:
        for b in sorted(porb):
            for c in porb[b]:
                print("   %-10s %s" % (b, c))

    print("\n3. INCIDENCIA CONOCIDA EN ESOS BLOQUES")
    print("-" * ANCHO)
    hubo = False
    for r in L.leer("incidencia_fitosanitaria.csv"):
        blo = " ".join(str(v) for k, v in r.items() if "bloque" in L.norm(k))
        if any(b.lower() in blo.lower() for b in porb):
            hubo = True
            campos = [v for v in list(r.values())[:5] if v]
            print("   " + " · ".join(str(c)[:34] for c in campos))
    if not hubo:
        print("   Sin eventos registrados para estos bloques.")

    print("\n" + "-" * ANCHO)
    print("Con esto ya se puede disenar la bomba. Para dejarla registrada:")
    print('  python3 motor/bomba.py registrar <fecha> %d "<bloques>" <bomba_id> '
          '<tanques> <operario> "<motivo>"' % semana)


def cmd_catalogo():
    filas = L.leer("bombas_catalogo.csv")
    por = collections.OrderedDict()
    for r in filas:
        por.setdefault(r["bomba_id"], []).append(r)
    for bid, ings in por.items():
        print("\n%-12s %s  (%s)" % (bid, ings[0]["nombre"], ings[0]["objetivo"]))
        for i in ings:
            print("     %-28s %6s %s" % (i["producto"][:28], i["dosis_25L"], i["unidad"]))
    print("\nDosis por tanque de 25 L. Una aspersion completa de Lisianthus son 4 tanques.")


def cmd_registrar(argv):
    if len(argv) < 6:
        raise SystemExit(
            'Uso: registrar <fecha> <semana> "<bloques>" <bomba_id> <tanques> '
            '[operario] ["motivo"]')
    fecha, semana, bloques, bomba_id, tanques = argv[:5]
    operario = argv[5] if len(argv) > 5 else ""
    motivo = argv[6] if len(argv) > 6 else ""

    if not L.receta_bomba(bomba_id):
        raise SystemExit("La bomba %r no esta en bombas_catalogo.csv. "
                         "Agregala ahi primero, con sus dosis." % bomba_id)
    reconocidos = L.bloques_de(bloques)
    if not reconocidos:
        raise SystemExit("No reconozco ningun bloque en %r. Los validos salen de "
                         "area_camas.csv: %s" % (bloques, ", ".join(sorted(
                             set(L.alias_bloques().values())))))
    try:
        litros = float(tanques) * 25
    except ValueError:
        raise SystemExit("tanques tiene que ser un numero.")

    ruta = os.path.join(L.DATOS, "aplicaciones_lote.csv")
    with open(ruta, encoding="utf-8") as f:
        cols = next(csv.reader(f))
    fila = dict.fromkeys(cols, "")
    fila.update(fecha=fecha, semana_iso=semana, anio=fecha[:4], bloque=",".join(reconocidos),
                bomba_id=bomba_id, tanques=tanques, litros="%g" % litros,
                operario=operario, motivo=motivo, fuente="motor/bomba.py registrar")
    with io.open(ruta, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=cols).writerow(fila)

    print("Registrada: sem %s · %s · %s · %s tanques (%g L) · %s" % (
        semana, ",".join(reconocidos), bomba_id, tanques, litros, operario or "sin operario"))
    idx = L.ocupacion(tope_semana=int(semana))
    tocadas = set()
    for b in reconocidos:
        for coh, frac, exacto in L.reparto(b, int(semana), idx):
            tocadas.add((coh, exacto))
    if tocadas:
        print("Se le suma a:")
        for coh, exacto in sorted(tocadas):
            print("   %s%s" % (coh, "" if exacto else "   (reparto APROX: falta el area)"))
    else:
        print("OJO: ninguna cohorte tiene ocupacion registrada en esos bloques esa semana,")
        print("asi que esta aplicacion no le suma a ninguna ficha. Revisa ocupacion_lote.csv.")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    cmd = argv[1]
    if cmd == "semana":
        cmd_semana(int(argv[2]) if len(argv) > 2 else 37)
    elif cmd == "catalogo":
        cmd_catalogo()
    elif cmd == "registrar":
        cmd_registrar(argv[2:])
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
