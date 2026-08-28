#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Importa DCB_Registro_Tallos desde el XLSX de Drive a los CSV de 07-datos/.

    python3 motor/importar_tallos.py ruta/al/DCB_Registro_Tallos.xlsx

POR QUE ESTE SCRIPT EXISTE
--------------------------
Bajar la hoja de Drive como *texto interpretado* trunca los datos sin avisar:
la pestana REGISTRO tiene 598 filas con datos y la lectura en texto devolvio
solo 251 (se cortaba el 23/06 cuando la hoja llega al 31/07). Un truncamiento
silencioso es peor que un error, porque el calendario se recalcula con menos
cosecha y nadie se entera.

La unica via confiable es descargar el XLSX binario y parsearlo. Este script
lo hace con libreria estandar (zipfile + XML), igual que el resto del motor:
no hay nada que instalar.

Escribe las 6 pestanas a 07-datos/ y reporta cuantas filas salieron de cada
una. Es idempotente: correrlo dos veces sobre el mismo XLSX da el mismo
resultado.

CORRECCIONES DE FECHA
---------------------
La hoja de Drive tiene fechas malas que Vanessa confirmo el 2026-08-12. Se
corrigen aqui, de forma explicita y auditable, NO en silencio. La hoja de
Drive sigue teniendo los valores originales: si se arreglan alla, estas reglas
simplemente dejan de encontrar coincidencias y no hacen nada.
"""

import csv
import datetime
import os
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NSR = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RAIZ, "07-datos")

# Excel cuenta los dias desde esta fecha (con el bug historico del 1900)
EPOCA = datetime.date(1899, 12, 30)

# Ventana de fechas plausibles para el cultivo. Cualquier cosa afuera es un
# error de captura y debe reportarse, no importarse callado.
FECHA_MIN = datetime.date(2025, 1, 1)
FECHA_MAX = datetime.date(2027, 12, 31)

# --- Correcciones confirmadas por Vanessa el 2026-08-12 -------------------
#
# 1) Ano 2056 en lugar de 2026 (33 filas del 06 al 08 de julio). Error de
#    tipeo: las filas vecinas son de julio 2026 y los conteos son coherentes.
CORRIGE_ANO = {2056: 2026}

# 2) Una fila suelta con 2026-09-19 entre filas del 18 y 19 de junio. Es la
#    misma variedad, bloque y cantidad que la cosecha del 18/06, un dia
#    despues: corresponde al 19/06. Se identifica por su contenido, no por su
#    numero de fila, para que siga funcionando si la hoja se reordena.
CORRIGE_FILA = [
    {
        "de": "2026-09-19",
        "a": "2026-06-19",
        "si": {"Grupo": "Amaranto", "Variedad / Serie": "Love Lies Bleeding",
               "Bloque": "Inv 3A"},
        "motivo": "fila entre 18 y 19 de junio; mismo lote que el 18/06",
    },
    # 3) Un 2025-06-17 en medio de la corrida diaria de Ammobium en Inv 3A,
    #    que va del 08/06 al 26/06 de 2026 sin huecos. Ano mal tecleado.
    #    NO se generaliza el ano 2025 -> 2026: la hoja podria traer historia
    #    legitima de 2025 mas adelante. Solo esta fila.
    {
        "de": "2025-06-17",
        "a": "2026-06-17",
        "si": {"Grupo": "Ammobium", "Variedad / Serie": "Ammobium Alatum",
               "Bloque": "Inv 3A"},
        "motivo": "fila dentro de la corrida diaria de junio 2026",
    },
]

# 4) Mes mal tecleado: 64 filas del 6 al 12 de septiembre de 2026 que en
#    realidad son de agosto (confirmado por Vanessa el 2026-08-13). Con el mes
#    corregido la corrida queda continua y los dos unicos dias sin cosecha son
#    los dos sabados, 01 y 08 de agosto.
#
#    EL CANDADO: la regla solo se aplica si la fecha TODAVIA NO HA OCURRIDO.
#    Una cosecha no se registra en el futuro, asi que una fecha futura es por
#    definicion un error de captura. Cuando septiembre llegue de verdad, la
#    regla deja de dispararse sola y los registros legitimos de septiembre
#    pasan intactos. Por eso no hace falta acordarse de quitarla.
CORRIGE_MES_SI_FUTURA = {(2026, 9): 8}

# Pestana -> (archivo destino, fila del encabezado, formato de fecha)
#   iso  = 2026-07-31   (lo que exige el motor para registro_tallos.csv)
#   dmy  = 31/07/2026   (formato que ya traia resumen_tallos_dia.csv)
PESTANAS = [
    ("REGISTRO",     "registro_tallos.csv",        1, "iso"),
    ("LISTAS",       "listas_desplegables.csv",    1, None),
    ("RESUMEN",      "resumen_tallos_dia.csv",     1, "dmy"),
    # CONSOLIDADO NO se espeja: se RECALCULA desde REGISTRO. Ver
    # consolidar_desde_registro() para el por que.
    ("CONSOLIDADO",  None,                         4, "iso"),
    ("RENDIMIENTO",  "rendimiento_costo_lote.csv", 4, "iso"),
    ("HOMOLOGACION", "homologacion_registro.csv",  1, None),
]


# --------------------------------------------------------------------------
# Lectura del XLSX
# --------------------------------------------------------------------------

def _col(ref):
    """'BC12' -> indice 0-based de la columna."""
    letras = re.match(r"[A-Z]+", ref).group()
    n = 0
    for ch in letras:
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def _cadenas(z):
    if "xl/sharedStrings.xml" not in z.namelist():
        return []
    raiz = ET.fromstring(z.read("xl/sharedStrings.xml"))
    return ["".join(t.text or "" for t in si.iter(NS + "t"))
            for si in raiz.findall(NS + "si")]


def _pestanas(z):
    """[(nombre, ruta interna)] en el orden del libro."""
    rels = {r.get("Id"): r.get("Target")
            for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    libro = ET.fromstring(z.read("xl/workbook.xml"))
    salida = []
    for hoja in libro.find(NS + "sheets"):
        destino = rels[hoja.get(NSR + "id")].lstrip("/")
        if not destino.startswith("xl/"):
            destino = "xl/" + destino
        salida.append((hoja.get("name"), destino))
    return salida


def _filas(z, ruta, cadenas):
    """Devuelve [(numero_de_fila, [celdas...])] con las columnas densas."""
    hoja = ET.fromstring(z.read(ruta))
    salida = []
    for fila in hoja.iter(NS + "row"):
        celdas = {}
        for c in fila.findall(NS + "c"):
            tipo = c.get("t")
            v = c.find(NS + "v")
            inline = c.find(NS + "is")
            if tipo == "s" and v is not None:
                valor = cadenas[int(v.text)]
            elif tipo == "inlineStr" and inline is not None:
                valor = "".join(t.text or "" for t in inline.iter(NS + "t"))
            elif v is not None:
                valor = v.text
            else:
                valor = ""
            celdas[_col(c.get("r"))] = valor if valor is not None else ""
        ancho = (max(celdas) + 1) if celdas else 0
        salida.append((int(fila.get("r")),
                       [celdas.get(i, "") for i in range(ancho)]))
    return salida


# --------------------------------------------------------------------------
# Normalizacion
# --------------------------------------------------------------------------

def _limpiar_numero(valor):
    """'73.0' -> '73'. Deja intacto lo que no sea numero."""
    if not isinstance(valor, str) or not valor:
        return valor
    try:
        f = float(valor)
    except ValueError:
        return valor
    return str(int(f)) if f.is_integer() else valor


def _a_fecha(valor):
    """Serial de Excel o texto dd/mm/aaaa -> date. None si no es fecha."""
    if not valor:
        return None
    if re.match(r"^\d+(\.\d+)?$", str(valor)):
        try:
            return EPOCA + datetime.timedelta(days=int(float(valor)))
        except (ValueError, OverflowError):
            return None
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", str(valor).strip())
    if m:
        d, mes, a = (int(x) for x in m.groups())
        try:
            return datetime.date(a, mes, d)
        except ValueError:
            return None
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", str(valor).strip())
    if m:
        try:
            return datetime.date(*(int(x) for x in m.groups()))
        except ValueError:
            return None
    return None


def _formatear(fecha, formato):
    if formato == "dmy":
        return fecha.strftime("%d/%m/%Y")
    return fecha.isoformat()


def _corregir(fecha, registro, informe, hoy=None):
    """Aplica las correcciones confirmadas. Devuelve la fecha buena."""
    if hoy is None:
        hoy = datetime.date.today()

    if fecha.year in CORRIGE_ANO:
        nueva = fecha.replace(year=CORRIGE_ANO[fecha.year])
        informe.append((fecha.isoformat(), nueva.isoformat(),
                        "ano %d -> %d" % (fecha.year, nueva.year)))
        return nueva

    # Mes mal tecleado, solo si la fecha aun no ocurrio (ver CORRIGE_MES_SI_FUTURA)
    mes_nuevo = CORRIGE_MES_SI_FUTURA.get((fecha.year, fecha.month))
    if mes_nuevo is not None and fecha > hoy:
        nueva = fecha.replace(month=mes_nuevo)
        informe.append((fecha.isoformat(), nueva.isoformat(),
                        "mes %02d -> %02d (fecha futura)" % (fecha.month, mes_nuevo)))
        return nueva
    for regla in CORRIGE_FILA:
        if fecha.isoformat() != regla["de"]:
            continue
        if all((registro.get(k) or "").strip() == v
               for k, v in regla["si"].items()):
            nueva = datetime.date.fromisoformat(regla["a"])
            informe.append((regla["de"], regla["a"], regla["motivo"]))
            return nueva
    return fecha


# --------------------------------------------------------------------------
# Exportacion
# --------------------------------------------------------------------------

def exportar(z, cadenas, nombre, ruta_hoja, destino, fila_encabezado, fmt):
    filas = _filas(z, ruta_hoja, cadenas)
    por_numero = {n: c for n, c in filas}

    encabezado = por_numero.get(fila_encabezado, [])
    while encabezado and not (encabezado[-1] or "").strip():
        encabezado.pop()
    if not encabezado:
        return None

    # Columnas de fecha: por nombre de encabezado
    col_fecha = [i for i, h in enumerate(encabezado)
                 if re.search(r"fecha|cosecha", (h or ""), re.I)]
    indice = {h: i for i, h in enumerate(encabezado)}

    hoy = datetime.date.today()
    cuerpo, correcciones, sospechosas, futuras = [], [], [], []
    for numero, celdas in filas:
        if numero <= fila_encabezado:
            continue
        celdas = list(celdas) + [""] * (len(encabezado) - len(celdas))
        if not any((c or "").strip() for c in celdas):
            continue

        registro = {h: celdas[i] for h, i in indice.items()
                    if i < len(celdas)}
        for i in col_fecha:
            if i >= len(celdas):
                continue
            fecha = _a_fecha(celdas[i])
            if fecha is None:
                continue
            buena = _corregir(fecha, registro, correcciones, hoy)
            if not (FECHA_MIN <= buena <= FECHA_MAX):
                sospechosas.append((numero, buena.isoformat()))
                continue
            # Una cosecha no se registra en el futuro. Se importa igual —
            # perder el dato es peor — pero se reporta para que se revise.
            if buena > hoy:
                futuras.append((numero, buena.isoformat()))
            celdas[i] = _formatear(buena, fmt)

        cuerpo.append([_limpiar_numero(c) if i not in col_fecha else c
                       for i, c in enumerate(celdas[:len(encabezado)])])

    with open(os.path.join(DATOS, destino), "w", newline="",
              encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(encabezado)
        w.writerows(cuerpo)

    return {"filas": len(cuerpo), "destino": destino,
            "correcciones": correcciones, "sospechosas": sospechosas,
            "futuras": futuras}


def _sumar_columna(z, cadenas, ruta_hoja, fila_encabezado, columna):
    """Suma una columna numerica de una pestana, sin escribir nada.

    Sirve para CONTRASTAR la pestana CONSOLIDADO de Drive contra el recalculo
    propio, sin espejarla. Un #REF! o un texto no suman — es lo correcto: son
    justamente las celdas rotas que se quieren detectar.
    """
    filas = _filas(z, ruta_hoja, cadenas)
    por_numero = {n: c for n, c in filas}
    encabezado = por_numero.get(fila_encabezado, [])
    try:
        idx = [i for i, h in enumerate(encabezado)
               if (h or "").strip() == columna][0]
    except IndexError:
        return None
    total = 0.0
    for numero, celdas in filas:
        if numero <= fila_encabezado or idx >= len(celdas):
            continue
        try:
            total += float((celdas[idx] or "0").replace(",", "") or 0)
        except ValueError:
            pass
    return total


def _norm(texto):
    """Minusculas, sin acentos, sin espacios ni puntuacion. Para comparar."""
    t = (texto or "").strip().lower()
    for a, b in (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
                 ("ñ", "n")):
        t = t.replace(a, b)
    return re.sub(r"[\s.\-_/]+", "", t)


def consolidar_desde_registro():
    """Recalcula consolidado_lotes.csv desde registro_tallos.csv.

    POR QUE NO SE ESPEJA LA PESTANA
    -------------------------------
    La pestana CONSOLIDADO de Drive esta MAL CALCULADA y el error es grande:
    reportaba 76.963 tallos contra 69.122 reales, 7.841 de mas (11%). Dos
    causas, las dos verificadas fila por fila el 2026-08-28:

      1. CUENTA DOS VECES lo que solo difiere en mayusculas. 'Inv4a' e
         'inv4a' entran al pivote como camas distintas, y 'Opus Fresh' y
         'opus fresh' como variedades distintas. Las filas duplicadas traen
         las MISMAS fechas y el MISMO numero de registros — es la misma
         cosecha contada dos veces. Son 11 casos, +8.041 tallos. El peor:
         Statice Mix en Inv4c, +1.587.

      2. TIENE FORMULAS ROTAS. Seis filas con #REF!, todas de cortes de
         agosto de grupos que se registran sin variedad (Colitas de conejo,
         Dahlias, Esparrago, Matricaria, Campanula). En Colitas de conejo
         ademas PIERDE un corte: el REGISTRO tiene dos de 200 tallos y
         CONSOLIDADO reporta 200.

    Espejar una pestana rota propaga el error a todo el motor sin que se vea.
    Recalcular desde REGISTRO —que es el dato crudo, escrito a mano, y la
    fuente de verdad— cuesta veinte lineas y elimina las dos causas de raiz.

    El agrupado normaliza mayusculas y espacios en Grupo, Variedad y Bloque,
    pero MUESTRA la grafia mas frecuente de cada uno: normalizar la clave no
    debe cambiar como se lee el nombre.
    """
    origen = os.path.join(DATOS, "registro_tallos.csv")
    if not os.path.exists(origen):
        return None
    with open(origen, newline="", encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))

    lotes = {}
    for r in filas:
        g = (r.get("Grupo") or "").strip()
        v = (r.get("Variedad / Serie") or "").strip()
        b = (r.get("Bloque") or "").strip()
        f = (r.get("Fecha") or "").strip()
        if not g or _norm(g) == "seleccionargrupo":
            continue
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", f):
            continue
        clave = (_norm(g), _norm(v), _norm(b))
        d = lotes.setdefault(clave, {
            "frescos": 0.0, "secos": 0.0, "n": 0, "fechas": [],
            "gg": {}, "gv": {}, "gb": {},
        })
        for col, campo in (("Tallos frescos", "frescos"), ("Tallos secos", "secos")):
            try:
                d[campo] += float((r.get(col) or "0").replace(",", "") or 0)
            except ValueError:
                pass
        d["n"] += 1
        d["fechas"].append(f)
        for txt, bolsa in ((g, "gg"), (v, "gv"), (b, "gb")):
            d[bolsa][txt] = d[bolsa].get(txt, 0) + 1

    def frecuente(bolsa):
        return max(bolsa.items(), key=lambda kv: (kv[1], kv[0]))[0] if bolsa else ""

    salida = []
    for d in lotes.values():
        salida.append([
            frecuente(d["gg"]), frecuente(d["gv"]), frecuente(d["gb"]),
            "%g" % d["frescos"], "%g" % d["secos"],
            "%g" % (d["frescos"] + d["secos"]), d["n"],
            min(d["fechas"]), max(d["fechas"]),
        ])
    salida.sort(key=lambda x: (x[0], -float(x[5]), x[2]))

    destino = os.path.join(DATOS, "consolidado_lotes.csv")
    with open(destino, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Grupo", "Variedad / Serie", "Bloque", "Tallos frescos",
                    "Tallos secos", "Total tallos", "# Registros",
                    "Primera cosecha", "Última cosecha"])
        w.writerows(salida)
    return {"lotes": len(salida),
            "frescos": sum(float(x[3]) for x in salida)}


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__.strip().split("\n\n")[1].strip())
    xlsx = sys.argv[1]
    if not os.path.exists(xlsx):
        raise SystemExit("No existe el archivo: %s" % xlsx)

    z = zipfile.ZipFile(xlsx)
    cadenas = _cadenas(z)
    disponibles = dict(_pestanas(z))

    print("Importando %s" % os.path.basename(xlsx))
    print("-" * 66)

    total_corr, total_sosp, total_fut = [], [], []
    frescos_drive = None
    for nombre, destino, fila_enc, fmt in PESTANAS:
        if nombre not in disponibles:
            print("  %-14s FALTA en el libro — se deja el CSV como estaba"
                  % nombre)
            continue
        # CONSOLIDADO de Drive se lee solo para COMPARAR, no se escribe.
        if destino is None:
            frescos_drive = _sumar_columna(z, cadenas, disponibles[nombre],
                                           fila_enc, "Tallos frescos")
            print("  %-14s     (no se espeja — se recalcula desde REGISTRO)"
                  % nombre)
            continue
        r = exportar(z, cadenas, nombre, disponibles[nombre],
                     destino, fila_enc, fmt)
        if r is None:
            print("  %-14s sin encabezado en la fila %d — omitida"
                  % (nombre, fila_enc))
            continue
        print("  %-14s %4d filas  ->  07-datos/%s"
              % (nombre, r["filas"], r["destino"]))
        total_corr.extend(r["correcciones"])
        total_sosp.extend((nombre,) + s for s in r["sospechosas"])
        total_fut.extend((nombre,) + s for s in r["futuras"])

    cons = consolidar_desde_registro()
    if cons:
        print("  %-14s %4d lotes  ->  07-datos/consolidado_lotes.csv  (RECALCULADO)"
              % ("consolidado", cons["lotes"]))
        if frescos_drive is not None:
            delta = frescos_drive - cons["frescos"]
            print("-" * 66)
            print("CONSOLIDADO — recalculado contra la pestana de Drive:")
            print("  REGISTRO (fuente de verdad)  %9.0f tallos frescos"
                  % cons["frescos"])
            print("  pestana CONSOLIDADO de Drive %9.0f" % frescos_drive)
            if abs(delta) >= 1:
                print("  DIFERENCIA                   %9.0f  (%.1f%%)"
                      % (delta, 100.0 * delta / cons["frescos"] if cons["frescos"] else 0))
                print("  La pestana de Drive esta mal: cuenta dos veces lo que solo")
                print("  difiere en mayusculas ('Inv4a' vs 'inv4a', 'Opus Fresh' vs")
                print("  'opus fresh') y tiene formulas rotas con #REF!. Se usa el")
                print("  recalculo. Conviene arreglar la formula en Drive igual.")
            else:
                print("  Coinciden. La pestana de Drive ya no necesita arreglo.")

    if total_corr:
        print("-" * 66)
        print("Correcciones de fecha aplicadas: %d" % len(total_corr))
        vistos = {}
        for de, a, motivo in total_corr:
            vistos.setdefault((de[:7], a[:7], motivo), 0)
            vistos[(de[:7], a[:7], motivo)] += 1
        for (de, a, motivo), n in sorted(vistos.items()):
            print("  %-9s -> %-9s  %3d filas   (%s)" % (de, a, n, motivo))

    if total_fut:
        print("-" * 66)
        print("REVISAR — %d fechas posteriores a hoy (%s). Se importaron, pero"
              % (len(total_fut), datetime.date.today().isoformat()))
        print("una cosecha no se registra en el futuro: son error de captura.")
        for hoja, numero, fecha in total_fut[:15]:
            print("  %s fila %s: %s" % (hoja, numero, fecha))
        if len(total_fut) > 15:
            print("  ... y %d mas" % (len(total_fut) - 15))

    if total_sosp:
        print("-" * 66)
        print("REVISAR — fechas fuera de rango que NO se importaron:")
        for hoja, numero, fecha in total_sosp:
            print("  %s fila %s: %s" % (hoja, numero, fecha))

    print("-" * 66)
    print("Listo. Correr 'python3 motor/cerebro.py matriz' para ver el efecto.")


if __name__ == "__main__":
    main()
