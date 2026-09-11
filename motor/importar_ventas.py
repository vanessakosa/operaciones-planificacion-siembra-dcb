#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hojas de punto de venta de Drive -> 07-datos/ventas_puntos.csv

    python3 motor/importar_ventas.py Jardines=jardines.txt "San Lucas=san_lucas.txt" ...

DE DONDE SALE
-------------
Las ventas NO viven en este repositorio ni en campo_siembras.csv (sus cuatro
columnas de venta estan en 0 de 302). Viven en Drive, en una hoja por PUNTO DE
VENTA, en la cuenta de servicio poscdreamscanbloom@gmail.com (Vanessa
2026-09-11: "debes mirar a traves de la cuenta de servicios las hojas de venta
de cada uno de los puntos para ver las ventas").

    Jardines · San Lucas · Tesoro · Del Este · Lemont · Viva Envigado · Online

Son demasiado grandes para exportar como XLSX ("File too large for export"), asi
que se bajan con el lector de contenido de Drive, que las devuelve como tablas
markdown, y ese texto es lo que come este script.

LA ESTRUCTURA DE CADA HOJA
--------------------------
Una pestana CONFIG_PRECIOS con la lista de precios, y despues UNA PESTANA POR
DIA. Cada pestana diaria trae TRES bloques, y hay que separarlos:

    1. la venta fila a fila    Fecha | Producto | Precio | Cantidad | ...
    2. los totales del dia     Total Vendido, Total_efectivo, ...
    3. INVENTARIO              Producto | Inventario Inicial | Reposicion | ...

El bloque 3 tambien empieza con 'Producto', asi que sin cortarlo sus filas se
leen como ventas y el nombre del producto cae en la columna de cantidad — por
eso aparecian "productos" llamados 1, 2 y 3. Viva Envigado y Online traen ademas
tablas dinamicas ('SUM de Cantidad'), abonos y entregas. Por eso se exige la
firma COMPLETA de la tabla diaria: fecha + producto + cantidad + (valor a cobrar
o % descuento).

QUE NO HACE
-----------
No inventa. Una fila sin fecha no se puede cruzar contra la semana de cosecha,
asi que se descarta y se reporta — nunca se rellena. Y la venta es por PRODUCTO,
no por tallo: para llegar a la variedad hay que pasar por las recetas, y hoy
solo 25 de 121 productos vendidos tienen uná.
"""
import csv
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerebro as C

def celdas(linea):
    if not linea.startswith('|'):
        return None
    p = linea.split('|')
    return [c.strip().replace('\\', '') for c in p[1:-1]] if len(p) > 2 else None

def num(s):
    s = (s or '').replace('$', '').replace(',', '').replace('%', '').strip()
    if not s or s in ('-', '#REF!', '#N/A', '#VALUE!'):
        return None
    try:
        return float(s)
    except ValueError:
        return None

def fecha(s):
    s = (s or '').strip()
    for f in ('%d/%m/%Y', '%Y-%m-%d', '%d/%m/%y', '%m/%d/%Y'):
        try:
            return datetime.datetime.strptime(s, f).date()
        except ValueError:
            pass
    return None

def parsear(ruta):
    L = open(ruta, encoding='utf-8').read().split('\n')
    filas, hdr, ncol = [], None, 0
    for ln in L:
        c = celdas(ln)
        if not c:
            continue
        low = [x.lower() for x in c]
        # Cada pestana diaria trae TRES bloques: ventas, totales e INVENTARIO.
        # El de inventario empieza con su propio encabezado y tiene 'Producto'
        # en la primera columna, asi que sin este corte sus filas se leian como
        # ventas y el nombre del producto caia en la columna de cantidad — por
        # eso aparecian "productos" llamados 2, 1, 3.
        if 'inventario inicial' in low or (low and low[0] == 'inventario'):
            hdr = None
            continue
        if low and low[0].startswith('total'):
            continue
        # Solo la tabla de venta DIARIA. Viva Envigado y Online traen ademas
        # tablas dinamicas ("SUM de Cantidad"), abonos y entregas, que tienen
        # Fecha y Producto pero no son ventas fila a fila. Se exige la firma
        # completa de la tabla diaria.
        if any('sum de' in x for x in low):
            hdr = None
            continue
        if ('fecha' in low and 'producto' in low and 'cantidad' in low
                and ('valor a cobrar' in low or '% descuento' in low)):
            hdr = {k: low.index(k) for k in
                   ('fecha', 'producto', 'precio', 'cantidad', 'valor a cobrar',
                    'forma de pago', 'observaciones') if k in low}
            continue
        if not hdr:
            continue
        def g(k):
            i = hdr.get(k)
            return c[i] if (i is not None and i < len(c)) else ''
        prod = g('producto')
        cant = num(g('cantidad'))
        f = fecha(g('fecha'))
        # Sin fecha no sirve: no se puede cruzar contra la semana de cosecha.
        # Se descarta y se cuenta aparte, nunca se rellena.
        if not prod or not cant or cant <= 0 or not f:
            continue
        filas.append({
            'fecha': f.isoformat() if f else '',
            'producto': prod,
            'precio': num(g('precio')),
            'cantidad': cant,
            'valor': num(g('valor a cobrar')),
            'pago': g('forma de pago'),
            'obs': g('observaciones'),
        })
    return filas


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    productos, _ = C.cargar_recetas()
    recetas = {C.norm(p["producto"]): p["producto"] for p in productos}

    def receta_de(p):
        n = C.norm(p)
        return recetas.get(n) or next(
            (r for k, r in recetas.items() if k and (k in n or n in k)), "")

    todo = []
    print("%-16s %7s %9s %12s %12s %6s" % (
        "PUNTO", "FILAS", "UNIDADES", "DESDE", "HASTA", "PROD"))
    print("-" * 68)
    for arg in argv[1:]:
        punto, _, ruta = arg.partition("=")
        if not ruta:
            raise SystemExit("Formato: Punto=ruta.txt  (recibido: %r)" % arg)
        fs = parsear(ruta)
        for f in fs:
            f["punto"] = punto
        todo += fs
        ff = sorted(x["fecha"] for x in fs)
        print("%-16s %7d %9.0f %12s %12s %6d" % (
            punto, len(fs), sum(x["cantidad"] for x in fs),
            ff[0] if ff else "--", ff[-1] if ff else "--",
            len({x["producto"] for x in fs})))

    todo.sort(key=lambda x: (x["fecha"], x["punto"], x["producto"]))
    ruta = os.path.join(C.DATOS, "ventas_puntos.csv")
    with open(ruta, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["fecha", "semana_iso", "punto", "producto", "cantidad",
                    "precio_unitario", "valor_cobrado", "forma_pago",
                    "producto_receta", "observaciones", "fuente"])
        for x in todo:
            d = datetime.date.fromisoformat(x["fecha"])
            w.writerow([
                x["fecha"], d.isocalendar()[1], x["punto"], x["producto"],
                "%g" % x["cantidad"],
                "%g" % x["precio"] if x["precio"] is not None else "",
                "%g" % x["valor"] if x["valor"] is not None else "",
                x["pago"], receta_de(x["producto"]), x["obs"],
                "hojas de punto de venta, cuenta poscdreamscanbloom (Drive)"])

    print("-" * 68)
    ff = sorted(x["fecha"] for x in todo)
    print("%-16s %7d %9.0f %12s %12s %6d" % (
        "TOTAL", len(todo), sum(x["cantidad"] for x in todo),
        ff[0], ff[-1], len({x["producto"] for x in todo})))
    con = sum(x["cantidad"] for x in todo if receta_de(x["producto"]))
    tot = sum(x["cantidad"] for x in todo)
    print()
    print("Escrito en 07-datos/ventas_puntos.csv")
    print("Con receta: %.0f de %.0f unidades (%.0f%%). El resto se vende y el"
          % (con, tot, 100 * con / tot))
    print("catalogo no lo nombra, asi que no se puede bajar a tallos.")


if __name__ == "__main__":
    main(sys.argv)
