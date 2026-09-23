"""El formulador: arma y revisa la bomba de la semana desde el cerebro de productos.

    python3 motor/formular.py candidatos            # por componente: que hay, dosis de ficha, costo
    python3 motor/formular.py revisar S40-PREFLOR   # chequea una bomba de bombas_catalogo.csv

Vanessa 2026-09-23: *"que cada semana podamos hacer una formulacion muy
personalizada... una combinacion lo mas completa posible, ya que solamente
podemos hacer una a la semana"*. El criterio agronomico esta en
03-fitosanidad/06-criterio-de-formulacion.md. Este script NO elige productos: eso
se razona en la sesion con Vanessa. Lo que hace es que ninguna bomba salga sin
pasar por los chequeos que hasta ahora dependian de la memoria:

  1. los cuatro componentes (nutricional, bioestimulante, fungicida, insecticida)
  2. ficha confirmada (regla 3 de CLAUDE.md)
  3. dosis dentro del rango de la ficha; marca las que vienen por hectarea
  4. via foliar en la ficha (Naturmix-L es solo fertirriego)
  5. compatibilidad por producto y por clase (compatibilidad.csv)
  6. hora: productos de manana y de tarde en el mismo tanque
  7. vida util: vivos que piden nevera
  8. rotacion: producto repetido de la bomba de la semana anterior
  9. gramos de cada micronutriente por bomba, sumados entre productos
 10. costo por bomba (con precio viejo marcado)

Una bomba nueva se escribe en bombas_catalogo.csv con su propio bomba_id y su
vigencia_desde; asi queda el historial de lo que se formulo cada semana.
"""
import sys, os, csv, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lotes as L

COMPONENTES = ["NUTRICIONAL", "BIOESTIMULANTE", "FUNGICIDA", "INSECTICIDA"]
ELEMENTOS = ["Zn", "Mn", "Cu", "Fe", "B", "Mo", "CaO"]


def num(v):
    try:
        return float(str(v).replace(",", "."))
    except (TypeError, ValueError):
        return None


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def cargar():
    return {r["producto"]: r for r in L.leer("productos.csv")}


def buscar(P, nombre):
    """El nombre en bombas_catalogo puede traer parentesis o alias."""
    if nombre in P:
        return P[nombre]
    n = norm(re.sub(r"\(.*?\)", "", nombre))
    for p in P:
        if norm(p) == n or norm(p).startswith(n) or n.startswith(norm(p)):
            return P[p]
    return None


def costo_bomba(p, dosis):
    pr, q = num(p.get("precio_cop")), num(p.get("presentacion"))
    return pr / q * dosis if pr and q and dosis else None


def cmd_candidatos():
    P = cargar()
    print("CANDIDATOS POR COMPONENTE — dosis de ficha por bomba de 25 L\n")
    for comp in COMPONENTES + ["COADYUVANTE"]:
        print("== %s" % comp)
        filas = [p for p in P.values() if p["categoria"] == comp]
        filas.sort(key=lambda p: (p["ficha_estado"] != "CONFIRMADA", p["producto"]))
        for p in filas:
            lo, hi = p["dosis_min_25L"], p["dosis_max_25L"]
            dosis = ("%s-%s %s" % (lo, hi, p["unidad"])) if lo and lo != hi else (
                ("%s %s" % (lo, p["unidad"])) if lo else "POR_HA/SIN_DATO")
            cb = costo_bomba(p, num(hi) or num(lo))
            alerta = []
            if p["ficha_estado"] != "CONFIRMADA":
                alerta.append(p["ficha_estado"])
            if "FERTIRRIEGO" in p["via"].upper() and "FOLIAR" not in p["via"].upper():
                alerta.append("NO FOLIAR")
            if "NO VIABLE" in p.get("conservacion", ""):
                alerta.append("NO VIABLE")
            if p["organismo_vivo"] not in ("NO", "", "SIN_DATO"):
                alerta.append("VIVO:" + p["organismo_vivo"])
            print("   %-24s %-20s %-10s %s" % (p["producto"][:24], dosis,
                  ("$%s" % format(round(cb), ",")) if cb else "-", " · ".join(alerta)))
        print()


def cmd_revisar(bomba_id, fecha=None):
    P = cargar()
    receta = [r for r in L.leer("bombas_catalogo.csv") if r["bomba_id"] == bomba_id
              and not r["vigencia_hasta"].strip()]
    if not receta:
        raise SystemExit("No hay receta vigente para %r en bombas_catalogo.csv." % bomba_id)
    compat = L.leer("compatibilidad.csv")
    ingred = L.leer("producto_ingredientes.csv")
    alertas, items = [], []
    print("REVISION DE LA BOMBA %s — %s\n" % (bomba_id, receta[0]["nombre"]))
    print("%-26s %-12s %-10s %-9s %s" % ("PRODUCTO", "COMPONENTE", "DOSIS", "$/BOMBA", "FICHA"))
    print("-" * 80)
    total = 0.0
    for r in receta:
        p = buscar(P, r["producto"])
        d = num(r["dosis_25L"])
        if not p:
            alertas.append("NO EN CEREBRO: %s no esta en productos.csv" % r["producto"])
            print("%-26s %s" % (r["producto"][:26], "?? no esta en productos.csv"))
            continue
        items.append((p, d))
        cb = costo_bomba(p, d)
        total += cb or 0
        viejo = " (precio 2023)" if cb and p["precio_fecha"].startswith("2023") else ""
        print("%-26s %-12s %-10s %-9s %s" % (p["producto"][:26], p["categoria"][:12],
              "%s %s" % (r["dosis_25L"], r["unidad"]),
              ("$%s" % format(round(cb), ",")) if cb else "-", p["ficha_estado"] + viejo))
        # 2 ficha
        if p["ficha_estado"] != "CONFIRMADA":
            alertas.append("FICHA: %s esta %s (regla 3)" % (p["producto"], p["ficha_estado"]))
        # 3 dosis
        lo, hi = num(p["dosis_min_25L"]), num(p["dosis_max_25L"])
        if d and lo and hi:
            if d < lo:
                alertas.append("DOSIS BAJA: %s a %g, la ficha pide %g-%g" % (p["producto"], d, lo, hi))
            elif d > hi:
                alertas.append("DOSIS ALTA: %s a %g, la ficha pide %g-%g" % (p["producto"], d, lo, hi))
        elif "ha" in p["dosis_fuente"].lower():
            alertas.append("POR_HA: %s viene por hectarea (%s) -- falta L de caldo por ha"
                           % (p["producto"], p["dosis_fuente"]))
        # 4 via
        if "FERTIRRIEGO" in p["via"].upper() and "FOLIAR" not in p["via"].upper():
            alertas.append("VIA: %s esta registrado solo para fertirriego" % p["producto"])
        # 7 vida util
        if "NO VIABLE" in p.get("conservacion", ""):
            alertas.append("VIABILIDAD: %s -- %s" % (p["producto"], p["conservacion"]))
    print("-" * 80)
    print("%-26s %-12s %-10s $%s" % ("TOTAL", "", "", format(round(total), ",")))

    # 1 componentes
    tiene = {p["categoria"] for p, _ in items}
    if "REF" in bomba_id.upper():
        # Un refuerzo va dirigido a un blanco, pero nunca solo (Vanessa 2026-09-23:
        # "si ya el operario se va a poner la bomba, deberia ser una bomba mas completa")
        if not tiene & {"NUTRICIONAL", "BIOESTIMULANTE"}:
            alertas.append("COMPONENTE: el refuerzo no lleva nada nutricional ni bioestimulante")
    else:
        for c in COMPONENTES:
            if c not in tiene:
                alertas.append("COMPONENTE: falta %s" % c)
    # 5 compatibilidad
    nombres = {p["producto"] for p, _ in items}
    cats = {p["categoria"] for p, _ in items}
    vivos = [p for p, _ in items if p["organismo_vivo"] not in ("NO", "", "SIN_DATO")]
    for c in compat:
        s, con, regla = c["sujeto"], c["con"], c["regla"]
        if s in nombres and regla in ("PREFERIBLEMENTE_SOLO",) and len(items) > 1:
            alertas.append("COMPAT: %s -- %s (%s)" % (s, regla, c["notas"] or c["fuente"]))
        if s in nombres and regla in ("NO_MEZCLAR", "CONSULTAR") and (con in cats or con in nombres):
            alertas.append("COMPAT: %s %s %s (%s)" % (s, regla, con, c["fuente"]))
    for v in vivos:
        ok_ficha = any(c["sujeto"] == v["producto"] and c["regla"].startswith("COMPATIBLE")
                       for c in compat)
        fung = [p["producto"] for p, _ in items if p["categoria"] == "FUNGICIDA" and p is not v]
        if fung and not ok_ficha:
            alertas.append("COMPAT: %s (vivo) con fungicida %s -- prueba de jarra o separar"
                           % (v["producto"], ", ".join(fung)))
    # 6 hora
    manana = [p["producto"] for p, _ in items if "MANANA" in p["ventana_uv"].upper()]
    tarde = [p["producto"] for p, _ in items if "TARDE" in p["ventana_uv"].upper()]
    if manana and tarde:
        alertas.append("HORA: %s piden manana y %s piden tarde" % (", ".join(manana), ", ".join(tarde)))
    # 8 rotacion
    # Contra lo APLICADO (aplicaciones_lote.csv), no contra lo formulado: una bomba
    # que se formulo y no se aplico no cuenta para la rotacion.
    desde = receta[0]["vigencia_desde"]
    aplicadas = [a for a in L.leer("aplicaciones_lote.csv")
                 if a["fecha"] < desde and "NO_APLICADA" not in (a.get("notas") or "")]
    if aplicadas:
        ultima = max(a["fecha"] for a in aplicadas)
        ids = {a["bomba_id"] for a in aplicadas if a["fecha"] == ultima}
        cat = L.leer("bombas_catalogo.csv")
        previos = set()
        for r in cat:
            if r["bomba_id"] in ids and r["vigencia_desde"] <= ultima and \
                    (not r["vigencia_hasta"] or r["vigencia_hasta"] > ultima):
                q = buscar(P, r["producto"])
                if q:
                    previos.add(q["producto"])
        rep = previos & nombres - {"Neofat"}
        if rep:
            alertas.append("ROTACION: repite de la aplicacion del %s: %s" % (ultima, ", ".join(sorted(rep))))
    # 9 micronutrientes
    gramos = {}
    for p, d in items:
        for i in ingred:
            if i["producto"] != p["producto"] or not d:
                continue
            c, u = num(i["concentracion"]), i["unidad"].lower()
            if c is None or i["ingrediente"] not in ELEMENTOS:
                continue
            if u.startswith("g/l"):
                g = d / 1000.0 * c
            elif "%" in u:
                g = d * c / 100.0
            else:
                continue
            gramos.setdefault(i["ingrediente"], []).append((p["producto"], g))
    if gramos:
        print("\nMICRONUTRIENTES POR BOMBA DE 25 L")
        for e in ELEMENTOS:
            if e in gramos:
                tot = sum(g for _, g in gramos[e])
                print("   %-4s %6.2f g  (%s ppm)   %s" % (e, tot, format(tot / 25 * 1000, ".0f"),
                      " + ".join("%s %.2f" % (n, g) for n, g in gramos[e])))
    print("\nALERTAS (%d)" % len(alertas))
    for a in alertas:
        print("   - " + a)
    if not alertas:
        print("   ninguna")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["candidatos"]:
        cmd_candidatos()
    elif a[:1] == ["revisar"] and len(a) > 1:
        cmd_revisar(a[1])
    else:
        raise SystemExit(__doc__)
