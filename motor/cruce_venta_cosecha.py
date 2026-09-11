#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cruce venta contra cosecha, tallo por tallo, con su margen de error.

    python3 motor/cruce_venta_cosecha.py

Contesta la pregunta que abrio la mesa de variedad: de lo que el campo dio,
cuanto salio por la puerta. Pero la respuesta NO es una resta limpia, y este
script existe sobre todo para decir por que.

LAS DOS VENTANAS NO SON LA MISMA, y esa es la correccion mas grande
-------------------------------------------------------------------
El registro de cosecha corta el 2026-08-27 y la venta llega al 2026-09-10. Son
DOS SEMANAS de venta sin cosecha que le corresponda. Comparar los totales
crudos le da a cada grupo un exceso de venta que no es real: es calendario.
Asi que el cruce recorta la venta a la ventana de la cosecha, y muestra aparte
lo que queda fuera.

CUATRO FUENTES DE ERROR, todas medidas y ninguna corregida a mano
-----------------------------------------------------------------
1. RECETAS QUE FALTAN. La venta se registra por producto; para bajarla a
   tallos hace falta la receta. Lo no cubierto se reporta por grupo, no se
   reparte.

2. COSECHA NO ANOTADA. Vanessa 2026-09-11: "puede haber algo que se coseche y
   no entro al registro". No hay forma de medirlo desde adentro — lo que si se
   puede es señalar donde el sintoma aparece: un grupo que vende mas de lo que
   figura cosechado esta acusando el hueco.

3. LO QUE SE SECA NO SE SEPARA. Vanessa: "no se esta separando las cosas que se
   van a secar, porque casi siempre lo que se va a secar es como sobrante de
   sala". La columna 'Tallos secos' de registro_tallos.csv esta VACIA — 0 de
   83.315 tallos. Como el seco sale de sobrante de sala, ya se conto como
   fresco al cortar: no hay doble conteo, pero SI hay cosecha que nunca se
   vendio fresca y no se puede distinguir de la que si.

4. TRES CULTIVOS PENDIENTES DE SUBIR (Vanessa 2026-09-11): Craspedia, Scabiosa
   Estrella y Dianthus, "los que empezamos a cosechar". Sus filas de cosecha
   suben mañana, asi que hoy su cruce no significa nada y sale marcado.

Ninguna de las cuatro se "arregla" inventando un factor. Se reportan.
"""

import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerebro as C
import ficha_variedad as F

# Cultivos cuya cosecha todavia no esta en el registro (Vanessa 2026-09-11).
PENDIENTES_DE_SUBIR = ("Craspedia", "Scabiosa", "Dianthus")


def venta_por_grupo_hasta(corte, grupos):
    """Tallos vendidos por grupo, contando solo la venta HASTA `corte`.

    Recorta a la ventana de la cosecha. Devuelve ademas lo que quedo fuera por
    ser posterior, que es informacion y no descarte.
    """
    ventas = C._leer_opcional("ventas_puntos.csv")
    productos, _ = C.cargar_recetas()
    por_nombre, por_grupo = C.cargar_paleta()
    recetas = {C.norm(p["producto"]): p for p in productos}
    ordenados = sorted(grupos, key=lambda g: -len(g))

    corte_iso = corte.isoformat() if hasattr(corte, "isoformat") else str(corte)
    dentro, fuera, sin_receta = {}, {}, {}
    u_dentro = u_fuera = u_sin = 0.0
    for v in ventas:
        cant = C.num((v.get("cantidad") or "").strip()) or 0.0
        if not cant:
            continue
        fecha = (v.get("fecha") or "").strip()
        posterior = bool(fecha and fecha > corte_iso)
        nombre = v.get("producto") or ""
        p = recetas.get(C.norm(C.receta_de_producto(nombre, {k: k for k in recetas})))
        if p is None:
            p = recetas.get(C.norm(v.get("producto_receta") or ""))
        if p is None:
            sin_receta[nombre] = sin_receta.get(nombre, 0.0) + cant
            u_sin += cant
            continue
        if posterior:
            u_fuera += cant
        else:
            u_dentro += cant
        destino = fuera if posterior else dentro
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
                destino[g] = destino.get(g, 0.0) + n * cant
    return dentro, fuera, sin_receta, u_dentro, u_fuera, u_sin


def main():
    roles = C.cargar_roles()
    ofe = C.oferta_registrada()
    dem = C.demanda_catalogo()
    grupos = sorted(set(roles) | set(dem["demanda"]) | set(ofe["tallos"]))
    corte = ofe["corte"]

    dentro, fuera, sin_receta, u_dentro, u_fuera, u_sin = \
        venta_por_grupo_hasta(corte, grupos)
    invis = F.venta_invisible(grupos, sin_receta)

    print("=" * 104)
    print("CRUCE VENTA CONTRA COSECHA — tallo por tallo")
    print("=" * 104)
    print()
    print("  Cosecha registrada hasta  : %s" % corte)
    print("  Venta recortada a esa misma fecha, para comparar lo comparable.")
    print("  Unidades vendidas DENTRO de la ventana : %6.0f" % u_dentro)
    print("  Unidades vendidas DESPUES del corte    : %6.0f  (no entran al cruce)"
          % u_fuera)
    print("  Unidades sin receta                    : %6.0f" % u_sin)
    print()
    print("%-20s %9s %9s %10s %7s  %s" % (
        "GRUPO", "COSECHO", "VENDIO", "DIFERENCIA", "%VTA", "LECTURA"))
    print("-" * 104)

    filas = []
    for g in grupos:
        cos = ofe["tallos"].get(g, 0)
        ven = dentro.get(g, 0.0)
        if not cos and not ven:
            continue
        filas.append((g, cos, ven))
    filas.sort(key=lambda x: -(x[1] or 0))

    for g, cos, ven in filas:
        pend = any(p.lower() in g.lower() for p in PENDIENTES_DE_SUBIR)
        pct = (100 * ven / cos) if cos else None
        iv = invis.get(g)
        if pend:
            lec = "COSECHA PENDIENTE DE SUBIR — el cruce no significa nada hoy"
        elif not cos:
            lec = "vende y no figura cosechado"
        elif pct is None:
            lec = ""
        elif pct > 110:
            lec = "VENDE MAS DE LO COSECHADO -> falta registro de cosecha"
        elif pct < 40:
            lec = "sobra cosecha, o le faltan recetas"
        else:
            lec = "en equilibrio"
        if iv:
            lec += "  [+%.0f unid sin receta]" % iv["unidades"]
        print("%-20s %9s %9s %10s %7s  %s" % (
            g[:20],
            "{:,.0f}".format(cos).replace(",", ".") if cos else "--",
            "{:,.0f}".format(ven).replace(",", ".") if ven else "--",
            ("{:+,.0f}".format(cos - ven).replace(",", ".")) if (cos and ven) else "--",
            ("%.0f%%" % pct) if pct is not None else "--",
            lec))

    tc = sum(c for _, c, _ in filas)
    tv = sum(v for _, _, v in filas)
    print("-" * 104)
    print("%-20s %9s %9s %10s %7s" % (
        "TOTAL",
        "{:,.0f}".format(tc).replace(",", "."),
        "{:,.0f}".format(tv).replace(",", "."),
        "{:+,.0f}".format(tc - tv).replace(",", "."),
        "%.0f%%" % (100 * tv / tc) if tc else "--"))

    print()
    print("=" * 104)
    print("EL MARGEN DE ERROR — cuatro fuentes, ninguna corregida a mano")
    print("=" * 104)
    print()
    print("  1. RECETAS QUE FALTAN — %.0f unidades (%.0f%% de la venta) sin bajar a tallos."
          % (u_sin, 100 * u_sin / (u_dentro + u_fuera + u_sin)))
    if invis:
        print("     Golpea sobre todo a: %s" % ", ".join(
            "%s (%.0f u)" % (g, d["unidades"])
            for g, d in sorted(invis.items(), key=lambda kv: -kv[1]["unidades"])[:5]))
    print()
    print("  2. COSECHA NO ANOTADA — Vanessa: \"puede haber algo que se coseche y no")
    print("     entro al registro\". No se puede medir desde adentro. El sintoma es")
    print("     un grupo que vende mas de lo que figura cosechado:")
    altos = [(g, c, v) for g, c, v in filas
             if c and v and 100 * v / c > 110
             and not any(p.lower() in g.lower() for p in PENDIENTES_DE_SUBIR)]
    for g, c, v in sorted(altos, key=lambda x: -(x[2] / x[1])):
        print("       %-20s cosecho %6.0f, vendio %6.0f  -> faltan al menos %.0f tallos"
              % (g[:20], c, v, v - c))
    print()
    print("  3. LO QUE SE SECA NO SE SEPARA — la columna 'Tallos secos' esta VACIA")
    print("     (0 de %s tallos). Vanessa: \"casi siempre lo que se va a secar es"
          % "{:,.0f}".format(tc).replace(",", "."))
    print("     como sobrante de sala\". Como sale de sobrante, ya se conto como")
    print("     fresco: NO hay doble conteo. Pero si hay cosecha que nunca se vendio")
    print("     fresca y hoy no se distingue de la que si — parte de la 'diferencia")
    print("     positiva' de arriba es secado, no sobrante perdido.")
    print()
    print("  4. TRES CULTIVOS PENDIENTES DE SUBIR (Vanessa 2026-09-11): %s."
          % ", ".join(PENDIENTES_DE_SUBIR))
    print("     Su cosecha entra mañana. Hoy salen marcados y su cruce no significa nada.")
    print()
    print("  Y una quinta que no es error sino calendario: %.0f unidades se vendieron"
          % u_fuera)
    print("  despues del %s y quedaron fuera del cruce. Cuando entre la cosecha" % corte)
    print("  de esas dos semanas, el cruce se vuelve a correr y cambia.")
    print()


if __name__ == "__main__":
    main()
