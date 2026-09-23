"""El cerebro de productos: una ficha por producto, no recetas armadas.

    python3 motor/productos.py                  # que falta por producto: ficha, dosis, precio
    python3 motor/productos.py ficha Equifun    # todo lo que se sabe de un producto
    python3 motor/productos.py comparar Mn      # productos que comparten ingrediente, por costo

Vanessa 2026-09-23: *"no deberian estar las formulas prehechas, sino la
informacion de cada producto, de forma que cada semana podamos hacer una
formulacion muy personalizada"*. Y: *"van a entrar productos nuevos... que
podamos razonar si de verdad este producto es mejor en costo-beneficio que este
otro que tiene lo mismo"*.

Tres tablas en 07-datos/:
  productos.csv              una fila por producto: que es, dosis de etiqueta,
                             restricciones, estado de la ficha, stock y PRECIO
  producto_ingredientes.csv  formato largo: producto x ingrediente x concentracion.
                             Una mezcla de 4 microorganismos son 4 filas. Es lo que
                             permite comparar por unidad de activo y no por frasco.
  compatibilidad.csv         reglas por CLASE (hongo vivo x fungicida) y por producto

Regla 3 de CLAUDE.md hecha codigo: `ficha_estado` distinto de CONFIRMADA sale
marcado, y `comparar` no da veredicto de costo-beneficio si falta la ficha o el
precio de alguno de los dos — dice cual falta.
"""
import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lotes as L

ORDEN_FICHA = {"CONFIRMADA": 0, "PARCIAL": 1, "LISTADA_SIN_DATOS": 2, "SIN_FICHA": 3}


def num(v):
    try:
        return float(str(v).replace(",", "."))
    except (TypeError, ValueError):
        return None


def cargar():
    return {r["producto"]: r for r in L.leer("productos.csv")}


def costo_unidad(r):
    """$ por cc o por g, si hay precio y presentacion."""
    p, q = num(r.get("precio_cop")), num(r.get("presentacion"))
    return p / q if p and q else None


def costo_bomba(r):
    cu, d = costo_unidad(r), num(r.get("dosis_max_25L")) or num(r.get("dosis_min_25L"))
    return cu * d if cu and d else None


def cmd_estado():
    P = cargar()
    print("ESTADO DEL CEREBRO DE PRODUCTOS — %d productos\n" % len(P))
    cuenta = {}
    for r in P.values():
        cuenta[r["ficha_estado"]] = cuenta.get(r["ficha_estado"], 0) + 1
    for k in sorted(cuenta, key=lambda k: ORDEN_FICHA.get(k, 9)):
        print("   %-18s %3d" % (k, cuenta[k]))
    con_precio = sum(1 for r in P.values() if num(r["precio_cop"]))
    print("   %-18s %3d de %d\n" % ("con precio", con_precio, len(P)))
    print("%-26s %-12s %-18s %-10s %-8s %s" % ("PRODUCTO", "CATEGORIA", "FICHA", "DOSIS 25L", "PRECIO", "FALTA"))
    print("-" * 110)
    for r in sorted(P.values(), key=lambda r: (ORDEN_FICHA.get(r["ficha_estado"], 9), r["categoria"], r["producto"])):
        falta = []
        if r["ficha_estado"] != "CONFIRMADA":
            falta.append("ficha")
        if not (r["dosis_min_25L"] or r["dosis_max_25L"]) and "cama" not in r["unidad"]:
            falta.append("dosis")
        elif r["dosis_fuente"] == "HISTORIAL":
            falta.append("dosis de etiqueta")
        if not num(r["precio_cop"]):
            falta.append("precio")
        if not r["stock"]:
            falta.append("stock")
        d = r["dosis_max_25L"] or r["dosis_min_25L"]
        print("%-26s %-12s %-18s %-10s %-8s %s" % (
            r["producto"][:26], r["categoria"][:12], r["ficha_estado"],
            ("%s %s" % (d, r["unidad"])) if d else "-", "si" if num(r["precio_cop"]) else "-",
            ", ".join(falta)))


def cmd_ficha(nombre):
    P = cargar()
    hit = [p for p in P if nombre.lower() in p.lower()]
    if not hit:
        raise SystemExit("No hay producto que contenga %r." % nombre)
    for p in hit:
        r = P[p]
        print("=" * 70)
        print(p)
        print("=" * 70)
        for k, v in r.items():
            if v and k != "producto":
                print("  %-20s %s" % (k, v))
        for i in L.leer("producto_ingredientes.csv"):
            if i["producto"] == p:
                print("  %-20s %s  %s %s  [%s]" % ("ingrediente", i["ingrediente"],
                      i["concentracion"], i["unidad"], i["fuente"]))
        for c in L.leer("compatibilidad.csv"):
            if c["sujeto"] in (p, r["organismo_vivo"], r["categoria"]) or c["con"] in (p, r["categoria"]):
                print("  %-20s %s %s %s  [%s]" % ("compatibilidad", c["sujeto"], c["regla"], c["con"], c["confianza"]))
        cb = costo_bomba(r)
        print("  %-20s %s" % ("costo por bomba 25L", "$%s" % format(round(cb), ",") if cb else "SIN PRECIO"))


def cmd_comparar(ingrediente):
    P = cargar()
    filas = [i for i in L.leer("producto_ingredientes.csv") if ingrediente.lower() in i["ingrediente"].lower()]
    if not filas:
        raise SystemExit("Ningun producto registra %r como ingrediente en producto_ingredientes.csv." % ingrediente)
    print("PRODUCTOS CON %s\n" % ingrediente.upper())
    print("%-18s %-14s %-16s %-12s %-12s %-14s %s" % ("PRODUCTO", "CONC.", "UNIDAD", "DOSIS 25L", "$/BOMBA", "$/1e9 UNID.", "PARA DECIDIR FALTA"))
    print("-" * 115)
    for i in filas:
        r = P.get(i["producto"], {})
        falta = []
        if r.get("ficha_estado") != "CONFIRMADA":
            falta.append("ficha")
        if "NO ficha" in i["fuente"]:
            falta.append("concentracion de ficha")
        conc, d = num(i["concentracion"]), num(r.get("dosis_max_25L")) or num(r.get("dosis_min_25L"))
        cb, cu = costo_bomba(r), costo_unidad(r)
        if not cu:
            falta.append("precio")
        if not d:
            falta.append("dosis por 25L")
        activo = "-"
        if cu and conc and "%" not in i["unidad"]:
            activo = "$%s" % format(round(cu / conc * 1e9), ",")
        elif cu and conc:
            activo = "$%s/g act." % format(round(cu / (conc / 100.0)), ",")
        print("%-18s %-14s %-16s %-12s %-12s %-14s %s" % (
            i["producto"][:18], i["concentracion"], i["unidad"][:16],
            ("%g %s" % (d, r.get("unidad", ""))) if d else "-",
            "$%s" % format(round(cb), ",") if cb else "-", activo, ", ".join(falta) or "OK"))
    print("\nEl costo por unidad de activo solo compara productos con la MISMA unidad de concentracion.")
    print("Costo-beneficio no es solo precio: pesan tambien los otros ingredientes de la mezcla,")
    print("el intervalo entre aplicaciones y la evidencia de eficacia. Eso lo razona la sesion.")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        cmd_estado()
    elif a[0] == "ficha" and len(a) > 1:
        cmd_ficha(" ".join(a[1:]))
    elif a[0] == "comparar" and len(a) > 1:
        cmd_comparar(" ".join(a[1:]))
    else:
        raise SystemExit(__doc__)
