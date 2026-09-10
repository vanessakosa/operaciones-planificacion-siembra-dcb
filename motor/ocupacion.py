#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ocupacion de cama: de tallos a tallos por m2 por semana.

    python3 motor/ocupacion.py           # la tabla por grupo
    python3 motor/ocupacion.py camas     # el area de cada cama de la finca

DE DONDE SALE EL AREA
---------------------
La finca tiene una sola geometria de cama: huecos cada 15 cm, 8 lineas, 1,20 m
de ancho. Eso da 0,18 m2 por hueco, y la constante cierra contra TODA el area
ya documentada:

    Inv 4 completo   28x112 + 225 + 212 + 190 huecos -> 677,3 m2   (doc: 677)
    Inv 5            13 camas x 176 huecos           -> 411,8 m2   (doc: 412)

Asi que el area de un lote NO hay que medirla en campo: se deriva de las
plantas que se trasplantaron y de la distancia de siembra de esa variedad.

    area ocupada m2 = plantas x (distancia_cm / 100)^2

La formula se verifica sola contra la cama: una cama de Inv 3A son 198 huecos
x 8 lineas = 1.584 plantas, y 1.584 x 0,0225 = 35,64 m2, que es exactamente el
area de esa cama. Ver 07-datos/area_camas.csv.

QUE ES Y QUE NO ES ESTE NUMERO
------------------------------
Es INGRESO por m2 por semana, no MARGEN. El costo por tallo todavia no esta
repartido por variedad — mientras la fila de tallos vendidos del modelo de
costos siga en cero, restar un costo aqui seria inventar el margen.

Y los tallos vienen del registro, que hoy corta el 2026-08-12. Todo lote
abierto en esa fecha sale SUBESTIMADO, y este numero con el.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerebro as C
import ficha_variedad as F


def cobertura_fecha_siembra():
    """Cuanta del area sembrada se puede ubicar en el tiempo.

    Es la validacion que decide si tallos/m2 se puede comparar entre grupos.
    El area sale de las plantas trasplantadas, que son ACUMULADAS de todo el
    historico; los tallos salen del registro, que cubre una ventana corta.
    Dividir uno por otro solo tiene sentido si el area se puede recortar a la
    misma ventana — y eso pide la fecha de siembra del lote.
    """
    con, sin = 0.0, 0.0
    for f in C._leer_csv("campo_siembras.csv"):
        p = C.num((f.get("Cantidad Trasplantada") or "").strip())
        if not p:
            continue
        fs = (f.get("Fecha siembra campo") or "").strip()
        if len(fs) >= 4 and fs[:4].isdigit():
            con += p
        else:
            sin += p
    tot = con + sin
    return {"con": con, "sin": sin, "total": tot,
            "pct": (con / tot) if tot else 0.0}


def cargar_camas():
    filas = []
    for f in C._leer_csv("area_camas.csv"):
        f["_area"] = C.num(f.get("area_cama_m2") or "")
        filas.append(f)
    return filas


def cmd_camas():
    filas = cargar_camas()
    print("AREA POR CAMA — geometria de la finca (0,15 m x 8 lineas = 0,18 m2/hueco)\n")
    print("%-16s %7s %6s %10s %6s %12s  %s" % (
        "CAMA", "HUECOS", "LIN", "AREA m2", "CAMAS", "BLOQUE m2", "CONFIANZA"))
    print("-" * 82)
    tot = 0.0
    for f in filas:
        ab = C.num(f.get("area_bloque_m2") or "")
        if ab:
            tot += ab
        print("%-16s %7s %6s %10s %6s %12s  %s" % (
            f["bloque"][:16], f.get("huecos_largo") or "--",
            f.get("lineas") or "--",
            ("%.2f" % f["_area"]) if f["_area"] else "--",
            f.get("n_camas") or "--",
            ("%.2f" % ab) if ab else "--",
            f.get("confianza", "")))
    print("-" * 82)
    print("%-16s %7s %6s %10s %6s %12.2f" % ("SUMA", "", "", "", "", tot))
    print("\n  Solo suma donde n_camas es conocido. Faltan Inv 3A, Inv 3B, Inv 2,")
    print("  Inv 1 y las tres Ext: el area de cama esta, el numero de camas no.")
    conflictos = [f for f in filas if f.get("confianza") == "CONFLICTO"]
    if conflictos:
        print("\n  CONFLICTO ABIERTO:")
        for f in conflictos:
            print("    %s — %s" % (f["bloque"], f.get("notas", "")[:110]))


def main(argv):
    if len(argv) > 1 and argv[1].startswith("cama"):
        return cmd_camas()

    roles = C.cargar_roles()
    dem = C.demanda_catalogo()
    ofe = C.oferta_registrada()
    ciclos = C.cargar_ciclos()
    grupos = sorted(set(roles) | set(dem["demanda"]) | set(ofe["tallos"]))
    plantas, _, lotes_con = F.plantas_por_grupo(grupos)
    ingreso = F.ingreso_por_grupo()

    filas = []
    for g in grupos:
        cic = ciclos.get(C.norm(g)) or {}
        dist = cic.get("distancia_cm")
        pl = plantas.get(g, 0)
        tallos = ofe["tallos"].get(g, 0)
        val = ingreso.get(g)
        if not (dist and pl and tallos):
            continue
        area = pl * (dist / 100.0) ** 2
        # Semanas de CAMA ocupada: del trasplante al fin de la ventana. La
        # germinacion es en bandeja y no ocupa cama, asi que no entra.
        campo = cic.get("sem_a_campo_max") or cic.get("sem_a_campo_min")
        vent = cic.get("ventana_max") or cic.get("ventana_min")
        semanas = (campo + vent) if (campo and vent) else None
        filas.append({
            "grupo": g,
            "rol": (roles.get(g, {}) or {}).get("rol", "") or "SIN_ROL",
            "plantas": pl, "dist": dist, "area": area,
            "tallos": tallos, "tallos_m2": tallos / area if area else 0,
            "semanas": semanas, "val": val,
            "ing_m2_sem": (tallos * val) / (area * semanas)
                          if (val and semanas and area) else None,
        })

    filas.sort(key=lambda f: -(f["ing_m2_sem"] or -1))

    cob = cobertura_fecha_siembra()
    valido = cob["pct"] >= 0.5

    print("=" * 94)
    print("OCUPACION DE CAMA — ingreso por m2 por semana")
    print("=" * 94)
    print()
    if not valido:
        print("  " + "!" * 88)
        print("  NO USAR ESTA TABLA PARA DECIDIR TODAVIA. La columna $/m2/SEM no es")
        print("  comparable entre grupos, y la razon no es el calculo: es la fuente.")
        print()
        print("    area   -> sale de las plantas trasplantadas, ACUMULADAS de todo el")
        print("              historico de campo_siembras (%s plantas)"
              % "{:,.0f}".format(cob["total"]).replace(",", "."))
        print("    tallos -> salen del registro, que cubre 12 semanas de 2026")
        print()
        print("  Solo el %.0f%% de esas plantas tiene fecha de siembra, asi que el area"
              % (100 * cob["pct"]))
        print("  NO se puede recortar a la ventana del registro. Un grupo con mucho")
        print("  historico viejo sale artificialmente mal, y uno recien sembrado sale")
        print("  artificialmente bien. El orden de abajo esta sesgado por eso.")
        print()
        print("  LO QUE FALTA: 'Fecha siembra campo' en campo_siembras.csv.")
        print("  Es UNA columna, y desbloquea el eje central del proyecto.")
        print("  " + "!" * 88)
        print()
    print("%-18s %-6s %8s %5s %9s %8s %8s %5s %11s" % (
        "GRUPO", "ROL", "PLANTAS", "DIST", "AREA m2", "TALLOS",
        "TALLOS/m2", "SEM", "$/m2/SEM"))
    print("-" * 94)
    for f in filas:
        print("%-18s %-6s %8s %4.0fcm %9.1f %8.0f %8.1f %5s %11s" % (
            f["grupo"][:18], f["rol"][:6],
            "{:,.0f}".format(f["plantas"]).replace(",", "."),
            f["dist"], f["area"], f["tallos"], f["tallos_m2"],
            ("%.0f" % f["semanas"]) if f["semanas"] else "--",
            ("{:,.0f}".format(f["ing_m2_sem"]).replace(",", ".")
             if f["ing_m2_sem"] else "--")))

    print()
    print("=" * 94)
    print("COMO SE LEE")
    print("=" * 94)
    print()
    con = [f for f in filas if f["ing_m2_sem"]]
    if con and valido:
        mej, peo = con[0], con[-1]
        print("  mejor : %-18s $%s por m2 por semana de cama" % (
            mej["grupo"][:18],
            "{:,.0f}".format(mej["ing_m2_sem"]).replace(",", ".")))
        print("  peor  : %-18s $%s" % (
            peo["grupo"][:18],
            "{:,.0f}".format(peo["ing_m2_sem"]).replace(",", ".")))
        print("  brecha: %.1fx" % (mej["ing_m2_sem"] / peo["ing_m2_sem"]))
    print()
    if not valido:
        print("  Sin la fecha de siembra no se nombra mejor ni peor: el orden es")
        print("  producto del sesgo de ventana, no del comportamiento del cultivo.")
        print()
    print("  Este eje NO es el mismo que $/tallo. Un tallo caro que ocupa la cama")
    print("  40 semanas puede perder contra uno barato que la desocupa en 12.")
    print()
    print("  ADVERTENCIAS que cambian el orden de esta tabla:")
    print("    0. AREA ACUMULADA vs TALLOS DE UNA VENTANA — el sesgo dominante.")
    print("       %.0f%% de las plantas sin fecha de siembra. Es lo primero a cerrar."
          % (100 * (1 - cob["pct"])))
    print("    1. Los tallos cortan el 2026-08-12. Faltan las semanas ISO 33-37,")
    print("       asi que todo lote abierto sale SUBESTIMADO — y con el su $/m2/sem.")
    print("    2. Es INGRESO, no margen: no lleva costo de semilla, insumo ni mano")
    print("       de obra. Cuando entre la fila de tallos vendidos del modelo de")
    print("       costos, se resta y sale margen de verdad.")
    print("    3. La distancia es la del GRUPO. Donde el subtipo manda (Celosia:")
    print("       cristata 7,5 cm y plumosa 15 cm) el area sale promediada.")
    print("    4. Solo entran los grupos con plantas trasplantadas Y distancia Y")
    print("       cosecha. %d de %d grupos quedaron fuera por falta de alguno." % (
        len(grupos) - len(filas), len(grupos)))
    print()


if __name__ == "__main__":
    main(sys.argv)
