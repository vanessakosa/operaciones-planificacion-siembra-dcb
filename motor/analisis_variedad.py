#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analisis preliminar de rentabilidad por variedad.

    python3 motor/analisis_variedad.py

Junta las cuatro piezas que hasta hoy vivian separadas: la VENTANA de cosecha de
cada grupo, lo que el registro anoto, lo que se vendio, y el rol que cumple en
los bouquets. Y con eso hace la primera aproximacion a rentabilidad por variedad.

LA VENTANA ES LO QUE HACE COMPARABLE AL RESTO
---------------------------------------------
Vanessa 2026-09-11: "hay algunos que se empezaron a registrar despues de que
aperturo la ventana de cosecha y otros que todavia no se ha cerrado esa
ventana". Sin corregir eso, el numero de tallos de un grupo no dice nada:

    TRUNCADA  su cosecha arranco ANTES del 2026-05-31, que es cuando empieza el
              registro. Le faltan tallos reales que nunca se anotaron, asi que
              su produccion sale SUBESTIMADA y su $/tallo INFLADO.
    ABIERTA   seguia cosechando el dia del corte. Va a producir mas, asi que
              tambien sale subestimada — pero por el otro extremo.
    COMPLETA  el registro vio la ventana entera. Es el unico caso en que el
              total se puede leer literal.

EL INGRESO YA NO SE DERIVA DEL CATALOGO: SALE DE LA PLATA QUE ENTRO
-------------------------------------------------------------------
Hasta hoy el ingreso por grupo se estimaba repartiendo el precio de lista del
catalogo. Con ventas_puntos.csv hay algo mejor: $293.887.084 de venta REAL con
su valor cobrado, descuentos incluidos. Este script reparte ese valor entre los
grupos segun cuantos tallos DCB pone cada uno en el producto vendido.

El follaje comprado no recibe ingreso: no es produccion de la finca. Es un COSTO
que todavia no se resta — por eso esto es INGRESO, no margen.

LO QUE ESTE ANALISIS TODAVIA NO PUEDE DECIR
-------------------------------------------
Si una variedad da PERDIDA. Falta el costo, y sigue faltando por la misma razon
de siempre: la fila de tallos vendidos de DCB_Modelo_Costos. Lo que si dice es
cuanto INGRESO genera cada variedad por metro cuadrado y por semana de cama, que
es la mitad del eje que el proyecto persigue.
"""

import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerebro as C
import ficha_variedad as F
import ocupacion as O

REGISTRO_ABRE = datetime.date(2026, 5, 31)


def ventana_por_grupo(grupos):
    """Cuando abrio y cerro la ventana de cosecha de cada grupo.

    El inicio sale de campo_siembras (272 de 302 filas lo tienen) y se compara
    contra el dia en que arranca el registro. El fin sale del registro mismo.
    """
    ciclos = C.cargar_ciclos()
    ordenados = sorted(grupos, key=lambda g: -len(g))
    abre = {}
    for v in O.ventanas_de_siembra(ciclos):
        if not v["inicio"]:
            continue
        g = next((x for x in ordenados
                  if any(a in C.norm(v["nombre"]) for a in C.alias_grupo(x))), None)
        if g and (g not in abre or v["inicio"] < abre[g]):
            abre[g] = v["inicio"]
    return abre


def ingreso_real_por_grupo(grupos):
    """Reparte el valor COBRADO de cada venta entre los grupos que la componen.

    El reparto es por tallos DCB: si un producto lleva 10 tallos propios y 4 son
    de Statice, a Statice le toca el 40% de lo que se cobro por ese producto. El
    follaje comprado no recibe nada — no es produccion de la finca.
    """
    ventas = C._leer_opcional("ventas_puntos.csv")
    productos, _ = C.cargar_recetas()
    por_nombre, por_grupo = C.cargar_paleta()
    recetas = {C.norm(p["producto"]): p for p in productos}
    ordenados = sorted(grupos, key=lambda g: -len(g))

    ingreso, tallos = {}, {}
    total_repartido = total_sin = 0.0
    for v in ventas:
        cant = C.num((v.get("cantidad") or "").strip()) or 0.0
        valor = C.num((v.get("valor_cobrado") or "").strip()) or 0.0
        if not cant:
            continue
        p = recetas.get(C.norm(C.receta_de_producto(
            v.get("producto") or "", {k: k for k in recetas})))
        if p is None:
            total_sin += valor
            continue
        reparto = {}
        for it in p["ingredientes"]:
            if (it.get("origen") or "").lower().startswith("compr"):
                continue
            n = it.get("cant_max") or it.get("cant_min") or 0.0
            if not n:
                continue
            res = C.resolver(it["ingrediente"], por_nombre, por_grupo)
            if res["tipo"] in ("SUSTITUCION", "NO_FLOR"):
                continue
            texto = C.norm(it["ingrediente"])
            g = next((x for x in ordenados
                      if any(a in texto for a in C.alias_grupo(x))), None)
            if g:
                reparto[g] = reparto.get(g, 0.0) + n
        tot = sum(reparto.values())
        if not tot:
            total_sin += valor
            continue
        total_repartido += valor
        for g, n in reparto.items():
            ingreso[g] = ingreso.get(g, 0.0) + valor * (n / tot)
            tallos[g] = tallos.get(g, 0.0) + n * cant
    return ingreso, tallos, total_repartido, total_sin


def rol_en_bouquets(grupos):
    """En cuantos productos del catalogo entra cada grupo, y con que peso."""
    productos, _ = C.cargar_recetas()
    por_nombre, por_grupo = C.cargar_paleta()
    ordenados = sorted(grupos, key=lambda g: -len(g))
    prods, sustituible = {}, {}
    for p in productos:
        vistos = set()
        for it in p["ingredientes"]:
            if (it.get("origen") or "").lower().startswith("compr"):
                continue
            texto = C.norm(it["ingrediente"])
            res = C.resolver(it["ingrediente"], por_nombre, por_grupo)
            g = next((x for x in ordenados
                      if any(a in texto for a in C.alias_grupo(x))), None)
            if not g or g in vistos:
                continue
            vistos.add(g)
            prods[g] = prods.get(g, 0) + 1
            if res["tipo"] == "SUSTITUCION":
                sustituible[g] = sustituible.get(g, 0) + 1
    return prods, sustituible


def main():
    roles = C.cargar_roles()
    ofe = C.oferta_registrada()
    dem = C.demanda_catalogo()
    ciclos = C.cargar_ciclos()
    grupos = sorted(set(roles) | set(dem["demanda"]) | set(ofe["tallos"]))
    corte = ofe["corte"]
    corte_d = corte if hasattr(corte, "year") else datetime.date.fromisoformat(str(corte))

    abre = ventana_por_grupo(grupos)
    ing, ven_tallos, repartido, sin_repartir = ingreso_real_por_grupo(grupos)
    prods, sust = rol_en_bouquets(grupos)
    areas, _ = F.area_por_grupo(grupos)

    print("=" * 118)
    print("ANALISIS PRELIMINAR DE RENTABILIDAD POR VARIEDAD")
    print("=" * 118)
    print()
    print("  Registro de cosecha: %s a %s" % (REGISTRO_ABRE, corte))
    print("  Ingreso repartido  : $%s de $%s de venta registrada" % (
        "{:,.0f}".format(repartido).replace(",", "."),
        "{:,.0f}".format(repartido + sin_repartir).replace(",", ".")))
    print()
    print("  VENTANA — lo que hace comparable (o no) a cada grupo:")
    print("    TRUNCADA  empezo a cosechar ANTES del %s -> produccion SUBESTIMADA" % REGISTRO_ABRE)
    print("    ABIERTA   seguia cosechando el %s -> va a producir mas" % corte)
    print("    COMPLETA  el registro vio la ventana entera -> se puede leer literal")
    print()

    filas = []
    for g in grupos:
        cos = ofe["tallos"].get(g, 0)
        if not cos:
            continue
        a = abre.get(g)
        ultima = ofe["ultima"].get(g)
        estado = []
        if a and a < REGISTRO_ABRE:
            estado.append("TRUNCADA")
        if ultima and ultima >= corte_d - datetime.timedelta(days=7):
            estado.append("ABIERTA")
        if not estado:
            estado = ["COMPLETA"]
        cic = ciclos.get(C.norm(g)) or {}
        campo = cic.get("sem_a_campo_max") or cic.get("sem_a_campo_min")
        vent = cic.get("ventana_max") or cic.get("ventana_min")
        sem = (campo + vent) if (campo and vent) else None
        area = areas.get(g)
        i = ing.get(g, 0.0)
        filas.append({
            "g": g, "rol": (roles.get(g, {}) or {}).get("rol", "") or "SIN_ROL",
            "cos": cos, "ven": ven_tallos.get(g, 0.0), "ing": i,
            "por_tallo": i / cos if cos else None,
            "area": area, "sem": sem,
            "ing_m2_sem": (i / (area * sem)) if (area and sem) else None,
            "estado": "+".join(estado),
            "prods": prods.get(g, 0), "sust": sust.get(g, 0),
        })

    filas.sort(key=lambda f: -(f["ing"] or 0))
    print("%-19s %-6s %8s %8s %13s %9s %7s %5s %10s %5s %s" % (
        "GRUPO", "ROL", "COSECHO", "VENDIO", "INGRESO", "$/TALLO",
        "AREA", "SEM", "$/m2/SEM", "PROD", "VENTANA"))
    print("-" * 118)
    for f in filas:
        print("%-19s %-6s %8s %8s %13s %9s %7s %5s %10s %5d %s" % (
            f["g"][:19], f["rol"][:6],
            "{:,.0f}".format(f["cos"]).replace(",", "."),
            "{:,.0f}".format(f["ven"]).replace(",", ".") if f["ven"] else "--",
            "$" + "{:,.0f}".format(f["ing"]).replace(",", ".") if f["ing"] else "--",
            "{:,.0f}".format(f["por_tallo"]).replace(",", ".") if f["por_tallo"] else "--",
            ("%.0f" % f["area"]) if f["area"] else "--",
            ("%.0f" % f["sem"]) if f["sem"] else "--",
            "{:,.0f}".format(f["ing_m2_sem"]).replace(",", ".") if f["ing_m2_sem"] else "--",
            f["prods"], f["estado"]))

    print()
    print("=" * 118)
    print("COMO LEERLO")
    print("=" * 118)
    print()
    comp = [f for f in filas if f["estado"] == "COMPLETA" and f["ing_m2_sem"]]
    inc = [f for f in filas if f["estado"] != "COMPLETA"]
    print("  Grupos con ventana COMPLETA: %d de %d. Solo esos se pueden comparar" % (
        len([f for f in filas if f["estado"] == "COMPLETA"]), len(filas)))
    print("  entre si sin corregir nada.")
    if comp:
        comp.sort(key=lambda f: -f["ing_m2_sem"])
        print()
        print("  Ordenados por INGRESO por m2 por semana de cama, solo los COMPLETA:")
        for f in comp:
            print("    %-19s $%s/m2/sem   %s en %d productos" % (
                f["g"][:19],
                "{:,.0f}".format(f["ing_m2_sem"]).replace(",", "."),
                f["rol"], f["prods"]))
    print()
    print("  Los %d con ventana TRUNCADA o ABIERTA salen SUBESTIMADOS: su ingreso" % len(inc))
    print("  por m2 es un piso, no una medida. Truncada = le faltan tallos de antes")
    print("  del registro; abierta = todavia va a producir.")
    print()
    print("  $/TALLO es el ingreso REAL cobrado repartido entre los tallos que el")
    print("  grupo aporto, no un precio de lista. Incluye descuentos.")
    print()
    print("  PROD es en cuantos productos del catalogo entra. Un grupo que entra en")
    print("  muchos productos es una dependencia: si falla, arrastra el surtido.")
    dep = sorted(filas, key=lambda f: -f["prods"])[:5]
    print("    los mas usados: %s" % ", ".join(
        "%s (%d)" % (f["g"], f["prods"]) for f in dep))
    s = [f for f in filas if f["sust"]]
    if s:
        print()
        print("  SUSTITUIBLE — estos entran en recetas donde pueden ser reemplazados,")
        print("  asi que su demanda NO es cautiva:")
        for f in sorted(s, key=lambda x: -x["sust"]):
            print("    %-19s sustituible en %d de %d productos" % (
                f["g"][:19], f["sust"], f["prods"]))
    print()
    print("  ESTO ES INGRESO, NO MARGEN. No lleva costo de semilla, insumo, mano de")
    print("  obra, follaje comprado ni el PINTADO (ver 10-postcosecha/03-el-flujo-del-seco.md).")
    print("  Lo desbloquea la fila 'Tallos vendidos en el mes' de DCB_Modelo_Costos.")
    print()


if __name__ == "__main__":
    main()
