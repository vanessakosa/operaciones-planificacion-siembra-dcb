#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ficha de completitud por grupo: que se puede decidir hoy de cada uno.

    python3 motor/ficha_variedad.py            # la tabla completa
    python3 motor/ficha_variedad.py faltantes  # solo que hay que traer

POR QUE ESTE SCRIPT EXISTE
--------------------------
`cerebro.py cartera` ya dice si un grupo SOBRA o FALTA en VOLUMEN. Lo que no
dice es si ese grupo es RENTABLE, y no lo dice porque el dato no existe.

Este script no estima el margen que falta: audita, campo por campo y grupo por
grupo, cual de las dos preguntas se puede contestar hoy y cual no.

    pregunta A — sobra o falta en la programacion  -> volumen
    pregunta B — es rentable                       -> plata

A se contesta con demanda y oferta, que estan. B necesita area, costo y precio
de venta por lote. Se marca FALTA y no se rellena con supuestos: un margen
inventado manda a arrancar una cama que estaba dando plata.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerebro as C


def plantas_por_grupo(grupos):
    """Cantidad trasplantada, sumada por grupo, desde campo_siembras."""
    tot, lotes, con_dato = {}, {}, {}
    ordenados = sorted(grupos, key=lambda g: -len(g))
    for fila in C._leer_csv("campo_siembras.csv"):
        nombre = " ".join([(fila.get("Nombre Homologados") or ""),
                           (fila.get("Variedad") or "")])
        n = C.norm(nombre)
        g = next((x for x in ordenados if C.norm(x) in n), None)
        if not g:
            continue
        lotes[g] = lotes.get(g, 0) + 1
        p = C.num((fila.get("Cantidad Trasplantada") or "").strip())
        if p:
            tot[g] = tot.get(g, 0) + p
            con_dato[g] = con_dato.get(g, 0) + 1
    return tot, lotes, con_dato


def ingreso_por_grupo():
    """Ingreso atribuible a cada grupo, repartiendo el precio del producto
    entre sus tallos DCB. Es ingreso, no margen: no hay costo que restar.

    Se resuelve ingrediente por ingrediente, igual que demanda_catalogo(): un
    ingrediente SUSTITUIBLE ("Trachelium o Ammi") NO se suma a ninguno de los
    dos, porque sumarlo a ambos inflaria los dos.
    """
    por_nombre, por_grupo = C.cargar_paleta()
    productos, _ = C.cargar_recetas()
    ing, tallos = {}, {}
    for p in productos:
        a = C.analizar_producto(p, por_nombre, por_grupo)
        if not a["tallos_dcb"] or not a["precio"]:
            continue
        unit = a["precio"] / a["tallos_dcb"]
        for it in p["ingredientes"]:
            if (it["origen"] or "").lower().startswith("compr"):
                continue
            cant = it["cant_max"] or it["cant_min"] or 0.0
            if not cant:
                continue
            res = C.resolver(it["ingrediente"], por_nombre, por_grupo)
            if res["tipo"] in ("SUSTITUCION", "NO_FLOR"):
                continue
            g = None
            if res["tipo"] == "EXACTA" and res["reg"]:
                g = res["reg"].get("grupo")
            elif res.get("grupo"):
                g = res["grupo"]
            if not g:
                continue
            ing[g] = ing.get(g, 0) + unit * cant
            tallos[g] = tallos.get(g, 0) + cant
    return {g: ing[g] / tallos[g] for g in ing if tallos.get(g)}


def main(argv):
    solo_faltantes = len(argv) > 1 and argv[1].startswith("falt")

    roles = C.cargar_roles()
    dem = C.demanda_catalogo()
    ofe = C.oferta_registrada()
    ciclos = C.cargar_ciclos()

    grupos = sorted(set(roles) | set(dem["demanda"]) | set(ofe["tallos"]))
    plantas, lotes, lotes_con_planta = plantas_por_grupo(grupos)
    try:
        ingreso = ingreso_por_grupo()
    except Exception:
        ingreso = {}

    def marca(ok):
        return "si" if ok else "--"

    print("=" * 92)
    print("FICHA POR GRUPO — que dato hay para decidir, y cual falta")
    print("=" * 92)
    print()
    print("A = se puede decidir SOBRA/FALTA (volumen)   B = se puede decidir RENTABLE (plata)")
    print()
    print("%-20s %-6s %6s %7s %8s %4s %4s %6s %7s %5s %s" % (
        "GRUPO", "ROL", "DEM", "COSECHO", "$/TALLO",
        "CIC", "T/P", "PLANTAS", "AREA_M2", "COSTO", "A/B"))
    print("-" * 92)

    faltan = {"area": [], "costo": [], "ciclo": [], "planta": [],
              "precio": [], "calidad": []}

    for g in grupos:
        rol = (roles.get(g, {}) or {}).get("rol", "") or "SIN_ROL"
        d = dem["demanda"].get(g, 0)
        o = ofe["tallos"].get(g, 0)
        cic = ciclos.get(C.norm(g)) or {}
        tiene_ciclo = bool(cic.get("sem_a_campo_min"))
        tp = cic.get("tallos_planta")
        tiene_tp = bool(tp)
        pl = plantas.get(g, 0)
        val = ingreso.get(g)

        # AREA y COSTO no existen para ningun grupo: los archivos estan vacios.
        tiene_area = False
        tiene_costo = False

        puede_a = bool(d or o)
        puede_b = tiene_area and tiene_costo and bool(val)

        if not tiene_area:
            faltan["area"].append(g)
        if not tiene_costo:
            faltan["costo"].append(g)
        if not tiene_ciclo:
            faltan["ciclo"].append(g)
        if not pl:
            faltan["planta"].append(g)
        if not val:
            faltan["precio"].append(g)
        faltan["calidad"].append(g)

        if solo_faltantes and puede_b:
            continue

        print("%-20s %-6s %6.0f %7.0f %8s %4s %4s %6s %7s %5s %s/%s" % (
            g[:20], rol[:6], d, o,
            ("{:,.0f}".format(val).replace(",", ".") if val else "--"),
            marca(tiene_ciclo), marca(tiene_tp),
            ("{:,.0f}".format(pl).replace(",", ".") if pl else "--"),
            "FALTA", "FALTA",
            "si" if puede_a else "--", "si" if puede_b else "NO"))

    n = len(grupos)
    print()
    print("=" * 92)
    print("VEREDICTO")
    print("=" * 92)
    print()
    print("  Pregunta A — sobra / falta en la programacion")
    print("    SE PUEDE HOY para %d de %d grupos. Es lo que ya hace `cerebro.py cartera`," % (
        sum(1 for g in grupos if dem["demanda"].get(g) or ofe["tallos"].get(g)), n))
    print("    con la advertencia de la ventana truncada (semanas ISO 33-37 sin registrar).")
    print()
    print("  Pregunta B — cual variedad es rentable")
    print("    NO SE PUEDE PARA NINGUNO DE LOS %d GRUPOS. Faltan tres piezas," % n)
    print("    y las tres son de archivo, no de calculo:")
    print()
    print("      1. AREA m2 por lote        -> rendimiento_costo_lote.csv esta VACIO")
    print("         Sin area no hay tallos/m2, y sin eso no hay margen por m2 por")
    print("         semana de cama ocupada, que es el eje que ordena la cartera.")
    print()
    print("      2. COSTO por lote          -> costos_productos.csv esta VACIO")
    print("         costo_mensual_operacion.csv SI tiene la nomina y el overhead de")
    print("         8 meses, pero es costo de finca, no repartido por variedad.")
    print()
    print("      3. TALLOS VENDIDOS         -> en 0 en los 12 meses del modelo")
    print("         Es el UNICO campo manual del modelo de costos. Mientras siga en")
    print("         cero, el costo por tallo sale $0 y todo margen calculado es falso.")
    print()
    print("  Lo que SI se tiene y sirve de inmediato:")
    print("    * ingreso por tallo propio de %d grupos (de las recetas y el precio)" % len(ingreso))
    print("    * ciclo y ventana de %d grupos" % sum(
        1 for g in grupos if (ciclos.get(C.norm(g)) or {}).get("sem_a_campo_min")))
    print("    * plantas trasplantadas de %d grupos (%d lotes con el dato)" % (
        len(plantas), sum(lotes_con_planta.values())))
    print()
    print("  Con eso alcanza para ordenar por INGRESO por tallo y por ocupacion")
    print("  aproximada. NO alcanza para decir 'esta variedad da perdida'.")
    print()


if __name__ == "__main__":
    main(sys.argv)
