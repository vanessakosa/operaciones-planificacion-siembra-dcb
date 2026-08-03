#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cerebro operativo DCB — de la siembra al punto de venta.

Cadena que modela este motor:

    punto de venta (mezcla de color objetivo)
        -> demanda de productos por semana
        -> explosion de recetas a tallos por variedad
        -> retroceso por ciclo -> semana de siembra y de germinacion
        -> chequeo de capacidad de camas
        -> brechas (que falta sembrar, que color va a faltar)

Reglas no negociables que respeta este codigo:
  * No inventa ciclos ni rendimientos. Si un dato no esta en los CSV, lo
    reporta como SIN_DATO y NO estima por debajo de la mesa.
  * La fuente primaria de ciclo/ventana para el calendario de Erica es
    VARIEDADES_BITACORA. ciclos_variedad.csv es la referencia agronomica
    de manejo y se usa solo para planificacion interna de siembra.

Uso:
    python3 motor/cerebro.py productos
    python3 motor/cerebro.py auditar
    python3 motor/cerebro.py bouquet "Cosecha Grande"
    python3 motor/cerebro.py explotar demanda.csv
    python3 motor/cerebro.py sembrar demanda.csv
"""

from __future__ import annotations

import csv
import os
import sys
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RAIZ, "07-datos")

# --------------------------------------------------------------------------
# Vocabulario estructural y de color
# --------------------------------------------------------------------------

# Los roles finos de paleta_color.csv se agrupan en macro-roles para poder
# evaluar el equilibrio del bouquet.
MACRO_ROL = {
    "FOCAL": "FOCAL",
    "FOCAL_TEXTURA": "FOCAL",
    "LINEA": "LINEA",
    "LINEA_CASCADA": "LINEA",
    "SECUNDARIA": "SECUNDARIA",
    "RELLENO": "RELLENO",
    "RELLENO_AIREADO": "RELLENO",
    "TEXTURA": "TEXTURA",
    "FOLLAJE": "FOLLAJE",
}

# Familias que NO cuentan como color en la lectura cromatica: son los neutros
# que dan descanso visual y sirven de puente entre familias.
NEUTROS = {
    "BLANCO", "MARFIL", "CREMA", "PLATA",
    "VERDE", "VERDE_GRIS", "VERDE_PLATA", "VERDE_MARRON", "BLANCO_CREMA",
}

# Reglas de estructura DCB — proporcion sobre el total de tallos del arreglo
# (incluye follaje). Ver 11-bouquets/01-estructura-del-bouquet.md
RANGO_ESTRUCTURA = {
    "FOCAL":      (0.10, 0.30),
    "LINEA":      (0.15, 0.30),
    "SECUNDARIA": (0.00, 0.20),
    "RELLENO":    (0.20, 0.45),
    "TEXTURA":    (0.05, 0.20),
    "FOLLAJE":    (0.20, 0.40),
}

# Reglas de color DCB — proporcion sobre los tallos NO neutros.
DOMINANTE_MIN = 0.50
MAX_FAMILIAS_CROMATICAS = 4
NEUTRO_MIN = 0.15  # sobre el total de tallos


# --------------------------------------------------------------------------
# Carga de datos
# --------------------------------------------------------------------------

def _leer_csv(nombre):
    ruta = os.path.join(DATOS, nombre)
    if not os.path.exists(ruta):
        raise SystemExit("Falta el archivo de datos: %s" % ruta)
    with open(ruta, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def cargar_paleta():
    """Devuelve (por_nombre, por_grupo).

    por_nombre: clave normalizada -> registro de la variedad
    por_grupo:  grupo -> lista de registros
    """
    por_nombre, por_grupo = {}, defaultdict(list)
    for fila in _leer_csv("paleta_color.csv"):
        reg = {
            "grupo": fila["grupo"].strip(),
            "variedad": fila["variedad"].strip(),
            "nombre_completo": fila["nombre_completo"].strip(),
            "familia_color": fila["familia_color"].strip(),
            "hex": fila["hex_referencia"].strip(),
            "rol": fila["rol_estructural"].strip(),
            "macro_rol": MACRO_ROL.get(fila["rol_estructural"].strip(), "SIN_ROL"),
            "origen": fila["origen"].strip(),
            "confianza": fila["confianza_color"].strip(),
            "notas": fila["notas"].strip(),
        }
        for clave in (reg["nombre_completo"], "%s %s" % (reg["grupo"], reg["variedad"]), reg["variedad"]):
            por_nombre.setdefault(norm(clave), reg)
        por_grupo[reg["grupo"]].append(reg)
    return por_nombre, dict(por_grupo)


def cargar_ciclos():
    ciclos = {}
    for fila in _leer_csv("ciclos_variedad.csv"):
        ciclos[norm(fila["grupo"])] = {
            "grupo": fila["grupo"].strip(),
            "sem_germinacion": num(fila["sem_germinacion"]),
            "sem_a_campo_min": num(fila["sem_a_campo_min"]),
            "sem_a_campo_max": num(fila["sem_a_campo_max"]),
            "ventana_min": num(fila["ventana_sem_min"]),
            "ventana_max": num(fila["ventana_sem_max"]),
            "distancia_cm": num(fila["distancia_cm"]),
            "tallos_planta": num(fila["tallos_planta"]),
            "fuente": fila["fuente"].strip(),
            "notas": fila["notas"].strip(),
        }
    return ciclos


def cargar_capacidad():
    bloques = []
    for fila in _leer_csv("capacidad_bloques.csv"):
        huecos = num(fila["Huecos (largo)"])
        lineas = num(fila["Líneas"])
        bloques.append({
            "bloque": fila["Bloque"].strip(),
            "huecos": huecos,
            "lineas": lineas,
            "sitios": (huecos * lineas) if (huecos and lineas) else None,
            "camas": num(fila.get("# Camas") or ""),
            "notas": (fila.get("Notas") or "").strip(),
        })
    return bloques


def cargar_recetas():
    """Parsea formulas_productos_bouquets.csv.

    El archivo es jerarquico: una fila de cabecera por producto (con Producto,
    Precio, Categoria) y luego filas de ingrediente con las 3 primeras
    columnas vacias. El archivo TAMBIEN trae contaminacion: al final hay
    filas de productos fitosanitarios con otro esquema. Se descartan y se
    reportan aparte.
    """
    productos, descartadas = [], []
    actual = None
    for fila in _leer_csv("formulas_productos_bouquets.csv"):
        prod = (fila.get("Producto") or "").strip()
        ingr = (fila.get("Ingrediente") or "").strip()
        origen = (fila.get("Origen") or "").strip()
        cant = (fila.get("Cantidad") or "").strip()

        if prod:
            categoria = (fila.get("Categoría") or "").strip()
            # Una cabecera legitima de producto describe la composicion en la
            # columna Ingrediente ("11 flores DCB + 4 follaje comprado").
            # Las filas fitosanitarias traen ahi el fabricante o el i.a.
            if "flores DCB" not in ingr:
                descartadas.append({"fila": prod, "motivo": "esquema fitosanitario, no es un producto de venta"})
                actual = None
                continue
            actual = {
                "producto": prod,
                "precio": num((fila.get("Precio") or "").strip()),
                "categoria": categoria,
                "composicion_declarada": ingr,
                "ingredientes": [],
            }
            productos.append(actual)
            continue

        if actual is None or not ingr:
            continue

        cmin, cmax = rango(cant)
        actual["ingredientes"].append({
            "ingrediente": ingr,
            "cant_min": cmin,
            "cant_max": cmax,
            "origen": origen or "DCB",
            "notas": (fila.get("Notas") or "").strip(),
        })
    return productos, descartadas


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def norm(texto):
    """Normaliza para comparar: minusculas, sin acentos, sin puntuacion."""
    t = (texto or "").lower().strip()
    for a, b in (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ñ", "n")):
        t = t.replace(a, b)
    for ch in "()[].,/-":
        t = t.replace(ch, " ")
    return " ".join(t.split())


def num(valor):
    valor = (valor or "").strip()
    if not valor:
        return None
    try:
        return float(valor) if "." in valor else int(valor)
    except ValueError:
        return None


def rango(texto):
    """'3-5' -> (3,5); '2' -> (2,2); '10-12' -> (10,12)."""
    texto = (texto or "").strip()
    if not texto:
        return (None, None)
    if "-" in texto:
        partes = texto.split("-", 1)
        a, b = num(partes[0]), num(partes[1])
        if a is not None and b is not None:
            return (a, b)
    v = num(texto)
    return (v, v)


# --------------------------------------------------------------------------
# Resolucion de ingrediente -> variedad / color
# --------------------------------------------------------------------------

# Ingredientes que no son flor de campo.
NO_FLOR = {"team wheeler florero", "team wheeler"}

# Alias de ingredientes de receta hacia el vocabulario de la paleta.
ALIAS = {
    "snapdragon boca de dragon": ("GRUPO", "Boca de Dragón"),
    "zinnia": ("GRUPO", "Zinnia"),
    "strawflower": ("GRUPO", "Strawflower"),
    "lisianthus": ("GRUPO", "Lisianthus"),
    "campanula champion pink white": ("GRUPO_PARCIAL", "Campanula"),
    "girasol pro cut": ("GRUPO", "Girasol"),
    "girasol pro cut white": ("EXACTA", "Girasol Pro Cut White Lite"),
    "girasol sin petalos": ("EXACTA", "Girasol Pro Cut (sin pétalos)"),
    "girasol pro cut sin petalos": ("EXACTA", "Girasol Pro Cut (sin pétalos)"),
    "gomphrena sequin": ("EXACTA", "Gomphrena Quis Sequin"),
}


class _Arreglo(object):
    """Un arreglo compuesto se juzga con reglas de estructura y color.
    Un paquete (ramo simple o mixto) se juzga con reglas de coherencia."""

    PREFIJOS = ("bouquet", "centro de mesa")

    def match(self, categoria):
        c = norm(categoria)
        return any(c.startswith(p) for p in self.PREFIJOS)


ARREGLO = _Arreglo()

# Palabra del nombre comercial -> grupo botanico que deberia contener.
PALABRA_GRUPO = {
    "bocas": "Boca de Dragón", "boca": "Boca de Dragón", "snapdragon": "Boca de Dragón",
    "campanula": "Campanula", "campanulas": "Campanula",
    "statice": "Statice", "amaranto": "Amaranto", "girasol": "Girasol",
    "strawflower": "Strawflower", "zinnia": "Zinnia", "zinnias": "Zinnia",
    "gomphrena": "Gomphrena", "gomphrenas": "Gomphrena",
    "ammobium": "Ammobium", "larkspur": "Larkspur", "lisianthus": "Lisianthus",
    "celosia": "Celosia", "ammi": "Ammi", "matricaria": "Matricaria",
    "trachelium": "Trachellium", "limonium": "Limonium",
}


def grupos_de(prod, por_nombre, por_grupo):
    """Grupos botanicos realmente presentes en la receta."""
    presentes = set()
    for ing in prod["ingredientes"]:
        res = resolver(ing["ingrediente"], por_nombre, por_grupo)
        if res["tipo"] in ("EXACTA", "FOLLAJE") and res["reg"]:
            presentes.add(res["reg"]["grupo"])
        elif res.get("grupo"):
            presentes.add(res["grupo"])
    return presentes


def nombre_incoherente(prod, por_nombre, por_grupo):
    """Grupos que el nombre comercial promete y la receta no entrega."""
    presentes = grupos_de(prod, por_nombre, por_grupo)
    prometidos, faltan = set(), []
    for palabra in norm(prod["producto"]).split():
        g = PALABRA_GRUPO.get(palabra)
        if g:
            prometidos.add(g)
    # "green ball" es de dos palabras
    if "green ball" in norm(prod["producto"]):
        prometidos.add("Green Ball")
    for g in sorted(prometidos):
        if g not in presentes:
            faltan.append(g)
    return faltan


def pct_libre_paquete(tallos_color_libre, tallos_dcb):
    return (tallos_color_libre / tallos_dcb) if tallos_dcb else 0.0


def resolver(ingrediente, por_nombre, por_grupo):
    """Clasifica un ingrediente de receta.

    Devuelve dict con:
      tipo: EXACTA | GRUPO | GRUPO_PARCIAL | FOLLAJE | NO_FLOR | DESCONOCIDA
      reg:  registro de paleta si la resolucion es exacta
      opciones: variedades candidatas si el color queda abierto
    """
    clave = norm(ingrediente)

    if clave in NO_FLOR:
        return {"tipo": "NO_FLOR", "reg": None, "opciones": []}

    if clave in ALIAS:
        modo, valor = ALIAS[clave]
        if modo == "EXACTA":
            reg = por_nombre.get(norm(valor))
            if reg:
                return {"tipo": "EXACTA", "reg": reg, "opciones": [reg]}
        else:
            opciones = por_grupo.get(valor, [])
            return {"tipo": modo, "reg": None, "opciones": opciones, "grupo": valor}

    reg = por_nombre.get(clave)
    if reg:
        tipo = "FOLLAJE" if reg["macro_rol"] == "FOLLAJE" and reg["origen"] == "Comprado" else "EXACTA"
        return {"tipo": tipo, "reg": reg, "opciones": [reg]}

    # Nombre que coincide con un grupo entero -> color abierto.
    for grupo, regs in por_grupo.items():
        if norm(grupo) == clave:
            return {"tipo": "GRUPO", "reg": None, "opciones": regs, "grupo": grupo}

    return {"tipo": "DESCONOCIDA", "reg": None, "opciones": []}


# --------------------------------------------------------------------------
# Analisis de un producto: estructura y color
# --------------------------------------------------------------------------

def analizar_producto(prod, por_nombre, por_grupo):
    """Calcula estructura, color y grado de indeterminacion cromatica."""
    por_macro = defaultdict(float)
    por_familia = defaultdict(float)
    total = 0.0
    tallos_dcb = 0.0
    tallos_color_libre = 0.0
    incidencias = []

    for ing in prod["ingredientes"]:
        # Se planifica con el techo del rango: es lo que hay que tener en campo.
        cant = ing["cant_max"] if ing["cant_max"] is not None else 0
        res = resolver(ing["ingrediente"], por_nombre, por_grupo)

        if res["tipo"] == "NO_FLOR":
            incidencias.append("'%s' no es un tallo (es contenedor): excluido del conteo" % ing["ingrediente"])
            continue

        total += cant
        if ing["origen"] == "DCB":
            tallos_dcb += cant

        if res["tipo"] in ("EXACTA", "FOLLAJE"):
            reg = res["reg"]
            por_macro[reg["macro_rol"]] += cant
            por_familia[reg["familia_color"]] += cant
        elif res["tipo"] in ("GRUPO", "GRUPO_PARCIAL"):
            opciones = res["opciones"]
            if opciones:
                por_macro[opciones[0]["macro_rol"]] += cant
            por_familia["COLOR_LIBRE"] += cant
            tallos_color_libre += cant
            colores = sorted({o["familia_color"] for o in opciones if o["familia_color"] not in ("MIX", "SIN_DATO")})
            incidencias.append(
                "'%s' no fija cultivar: %d tallos quedan a criterio de sala (%d colores posibles: %s)"
                % (ing["ingrediente"], cant, len(colores), ", ".join(colores[:6]) or "sin datos")
            )
        else:
            por_familia["DESCONOCIDA"] += cant
            incidencias.append("'%s' no esta en paleta_color.csv — agregarla" % ing["ingrediente"])

    # Un paquete mono o bi-variedad NO se juzga con las reglas de equilibrio de
    # un arreglo: un ramo de 10 larkspur esta bien siendo solo linea.
    es_arreglo = ARREGLO.match(prod["categoria"])

    # Estructura (solo aplica a arreglos)
    estructura = []
    if es_arreglo:
        for rol, (lo, hi) in RANGO_ESTRUCTURA.items():
            pct = (por_macro.get(rol, 0.0) / total) if total else 0.0
            estado = "ok" if lo <= pct <= hi else ("bajo" if pct < lo else "alto")
            estructura.append({"rol": rol, "tallos": por_macro.get(rol, 0.0), "pct": pct,
                               "rango": (lo, hi), "estado": estado})
    else:
        for rol in RANGO_ESTRUCTURA:
            if por_macro.get(rol):
                estructura.append({"rol": rol, "tallos": por_macro[rol],
                                   "pct": por_macro[rol] / total if total else 0.0,
                                   "rango": None, "estado": "na"})

    # Color: solo sobre lo que tiene color determinado
    determinado = {f: n for f, n in por_familia.items()
                   if f not in ("COLOR_LIBRE", "DESCONOCIDA", "MIX", "SIN_DATO")}
    neutro = sum(n for f, n in determinado.items() if f in NEUTROS)
    cromatico = {f: n for f, n in determinado.items() if f not in NEUTROS}
    total_crom = sum(cromatico.values())

    familias_ord = sorted(cromatico.items(), key=lambda kv: -kv[1])
    dominante = familias_ord[0] if familias_ord else None

    diagnostico = []
    if es_arreglo:
        if total_crom:
            if dominante[1] / total_crom < DOMINANTE_MIN:
                diagnostico.append(
                    "sin color dominante claro (el mayor es %s con %.0f%% de lo cromatico; minimo %.0f%%)"
                    % (dominante[0], 100 * dominante[1] / total_crom, 100 * DOMINANTE_MIN))
            if len(cromatico) > MAX_FAMILIAS_CROMATICAS:
                diagnostico.append("demasiadas familias de color: %d (maximo %d)"
                                   % (len(cromatico), MAX_FAMILIAS_CROMATICAS))
        if total and neutro / total < NEUTRO_MIN:
            diagnostico.append("poco neutro: %.0f%% (minimo %.0f%%)"
                               % (100 * neutro / total, 100 * NEUTRO_MIN))
    else:
        # Un paquete se juzga por coherencia: el nombre debe corresponder al
        # contenido, y el color no deberia quedar abierto en un ramo simple.
        for grupo_ausente in nombre_incoherente(prod, por_nombre, por_grupo):
            diagnostico.append(
                "el nombre dice '%s' pero ningun ingrediente es de ese grupo" % grupo_ausente)
        if pct_libre_paquete(tallos_color_libre, tallos_dcb) > 0.5:
            diagnostico.append("mas de la mitad del ramo sin cultivar definido")

    pct_libre = (tallos_color_libre / tallos_dcb) if tallos_dcb else 0.0

    return {
        "producto": prod["producto"],
        "precio": prod["precio"],
        "categoria": prod["categoria"],
        "total_tallos": total,
        "tallos_dcb": tallos_dcb,
        "tallos_color_libre": tallos_color_libre,
        "pct_color_libre": pct_libre,
        "estructura": estructura,
        "familias": familias_ord,
        "neutro_pct": (neutro / total) if total else 0.0,
        "diagnostico": diagnostico,
        "incidencias": incidencias,
    }


# --------------------------------------------------------------------------
# Explosion de demanda -> tallos
# --------------------------------------------------------------------------

def cargar_demanda(ruta):
    """CSV de demanda: semana,producto,unidades"""
    if not os.path.exists(ruta):
        raise SystemExit("No existe el archivo de demanda: %s" % ruta)
    with open(ruta, newline="", encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))
    demanda = []
    for f in filas:
        demanda.append({
            "semana": int(f["semana"]),
            "producto": f["producto"].strip(),
            "unidades": float(f["unidades"]),
        })
    return demanda


def explotar(demanda, productos, por_nombre, por_grupo, merma=0.15):
    """Convierte demanda de producto en demanda de tallos por semana.

    merma: fraccion adicional a sembrar por descarte de calidad y no-cosecha.
    """
    recetas = {norm(p["producto"]): p for p in productos}
    tallos = defaultdict(float)      # (semana, grupo, familia) -> tallos
    faltantes = set()

    for d in demanda:
        prod = recetas.get(norm(d["producto"]))
        if prod is None:
            faltantes.add(d["producto"])
            continue
        for ing in prod["ingredientes"]:
            if ing["origen"] != "DCB":
                continue
            cant = ing["cant_max"] if ing["cant_max"] is not None else 0
            res = resolver(ing["ingrediente"], por_nombre, por_grupo)
            if res["tipo"] == "NO_FLOR":
                continue
            need = cant * d["unidades"] * (1 + merma)
            if res["tipo"] in ("EXACTA", "FOLLAJE"):
                reg = res["reg"]
                tallos[(d["semana"], reg["grupo"], reg["familia_color"])] += need
            elif res["tipo"] in ("GRUPO", "GRUPO_PARCIAL"):
                tallos[(d["semana"], res.get("grupo", "?"), "COLOR_LIBRE")] += need
            else:
                tallos[(d["semana"], "DESCONOCIDA:%s" % ing["ingrediente"], "SIN_DATO")] += need
    return tallos, sorted(faltantes)


def plan_siembra(tallos, ciclos):
    """Retrocede de semana de cosecha a semana de siembra y de germinacion."""
    plan, sin_datos = [], []
    agregado = defaultdict(float)
    for (sem, grupo, familia), n in tallos.items():
        agregado[(sem, grupo)] += n

    for (sem_cosecha, grupo), n_tallos in sorted(agregado.items()):
        c = ciclos.get(norm(grupo))
        if not c or c["sem_a_campo_max"] is None or c["tallos_planta"] is None:
            sin_datos.append({"semana_cosecha": sem_cosecha, "grupo": grupo, "tallos": n_tallos,
                              "motivo": "sin ciclo o sin tallos/planta en ciclos_variedad.csv"})
            continue
        plantas = n_tallos / c["tallos_planta"]
        sem_campo = sem_cosecha - c["sem_a_campo_max"]
        sem_germ = (sem_campo - c["sem_germinacion"]) if c["sem_germinacion"] is not None else None
        plan.append({
            "semana_cosecha": sem_cosecha,
            "grupo": grupo,
            "tallos": n_tallos,
            "plantas": plantas,
            "semana_trasplante": sem_campo,
            "semana_siembra_bandeja": sem_germ,
            "ventana_sem": c["ventana_max"],
            "distancia_cm": c["distancia_cm"],
            "tallos_planta": c["tallos_planta"],
        })
    return plan, sin_datos


def sitios_disponibles(capacidad):
    total = sum(b["sitios"] for b in capacidad if b["sitios"])
    pendientes = [b["bloque"] for b in capacidad if not b["sitios"]]
    return total, pendientes


# --------------------------------------------------------------------------
# Presentacion
# --------------------------------------------------------------------------

def barra(pct, ancho=20):
    lleno = int(round(pct * ancho))
    return "#" * lleno + "." * (ancho - lleno)


def cmd_productos():
    productos, descartadas = cargar_recetas()
    print("PRODUCTOS DE VENTA — %d\n" % len(productos))
    print("%-38s %10s  %-22s %6s" % ("PRODUCTO", "PRECIO", "CATEGORIA", "TALLOS"))
    print("-" * 82)
    for p in productos:
        tallos = sum((i["cant_max"] or 0) for i in p["ingredientes"])
        precio = "{:,.0f}".format(p["precio"]).replace(",", ".") if p["precio"] else "-"
        print("%-38s %10s  %-22s %6.0f" % (p["producto"][:38], precio,
                                           p["categoria"][:22], tallos))
    if descartadas:
        print("\nFILAS DESCARTADAS DE formulas_productos_bouquets.csv (%d):" % len(descartadas))
        for d in descartadas:
            print("  - %-24s %s" % (d["fila"][:24], d["motivo"]))


def cmd_bouquet(nombre):
    por_nombre, por_grupo = cargar_paleta()
    productos, _ = cargar_recetas()
    match = [p for p in productos if norm(nombre) in norm(p["producto"])]
    if not match:
        raise SystemExit("No encontre el producto '%s'. Corre: python3 motor/cerebro.py productos" % nombre)

    for p in match:
        a = analizar_producto(p, por_nombre, por_grupo)
        print("=" * 74)
        print("%s   $%s   %s" % (a["producto"], "{:,.0f}".format(a["precio"] or 0).replace(",", "."), a["categoria"]))
        print("=" * 74)
        print("Tallos totales: %.0f   (DCB: %.0f  ·  comprado: %.0f)"
              % (a["total_tallos"], a["tallos_dcb"], a["total_tallos"] - a["tallos_dcb"]))

        print("\nESTRUCTURA")
        for e in a["estructura"]:
            marca = {"ok": " ", "bajo": "v", "alto": "^", "na": " "}[e["estado"]]
            objetivo = ("objetivo %.0f-%.0f%%" % (100 * e["rango"][0], 100 * e["rango"][1])
                        if e["rango"] else "(paquete: sin regla de equilibrio)")
            print("  %s %-11s %5.1f tallos  %s %5.1f%%   %s"
                  % (marca, e["rol"], e["tallos"], barra(e["pct"]), 100 * e["pct"], objetivo))

        print("\nCOLOR")
        for fam, n in a["familias"]:
            print("  %-20s %5.1f tallos  %s" % (fam, n, barra(n / a["total_tallos"] if a["total_tallos"] else 0)))
        print("  %-20s %5.1f%%" % ("neutro", 100 * a["neutro_pct"]))
        print("  %-20s %5.1f%% de los tallos DCB" % ("color SIN definir", 100 * a["pct_color_libre"]))

        if a["diagnostico"]:
            print("\nDIAGNOSTICO")
            for d in a["diagnostico"]:
                print("  ! %s" % d)
        if a["incidencias"]:
            print("\nINCIDENCIAS")
            for i in a["incidencias"]:
                print("  - %s" % i)
        print()


def cmd_auditar():
    por_nombre, por_grupo = cargar_paleta()
    productos, descartadas = cargar_recetas()
    ciclos = cargar_ciclos()

    print("=" * 78)
    print("AUDITORIA DEL CATALOGO — %d productos" % len(productos))
    print("=" * 78)
    print("\n%-38s %6s %7s %8s %s" % ("PRODUCTO", "TALLOS", "S/COLOR", "NEUTRO", "ALERTAS"))
    print("-" * 78)

    total_libre = total_dcb = 0.0
    for p in productos:
        a = analizar_producto(p, por_nombre, por_grupo)
        total_libre += a["tallos_color_libre"]
        total_dcb += a["tallos_dcb"]
        alertas = len(a["diagnostico"]) + sum(
            1 for e in a["estructura"] if e["estado"] in ("bajo", "alto"))
        print("%-38s %6.0f %6.0f%% %7.0f%% %s"
              % (p["producto"][:38], a["total_tallos"], 100 * a["pct_color_libre"],
                 100 * a["neutro_pct"], "!" * alertas))

    print("\n" + "-" * 78)
    print("GOBERNANZA DE COLOR: %.0f%% de los tallos DCB del catalogo (%.0f de %.0f)"
          % (100 * total_libre / total_dcb if total_dcb else 0, total_libre, total_dcb))
    print("quedan sin cultivar definido en la receta. Ese es el porcentaje del")
    print("color del punto de venta que hoy NO esta gobernado por la receta.")

    # Cobertura de ciclos
    usados = set()
    for p in productos:
        for ing in p["ingredientes"]:
            if ing["origen"] != "DCB":
                continue
            res = resolver(ing["ingrediente"], por_nombre, por_grupo)
            if res["tipo"] in ("EXACTA", "FOLLAJE") and res["reg"]:
                usados.add(res["reg"]["grupo"])
            elif res.get("grupo"):
                usados.add(res["grupo"])

    sin_ciclo = []
    for g in sorted(usados):
        c = ciclos.get(norm(g))
        if not c or c["sem_a_campo_max"] is None:
            sin_ciclo.append(g)

    print("\nGRUPOS EN RECETAS SIN CICLO UTILIZABLE (%d de %d):" % (len(sin_ciclo), len(usados)))
    for g in sin_ciclo:
        print("  ! %s — no se puede calcular fecha de siembra" % g)
    if not sin_ciclo:
        print("  ninguno — todo el catalogo es planificable")

    if descartadas:
        print("\nCALIDAD DE DATOS — filas ajenas en formulas_productos_bouquets.csv: %d" % len(descartadas))


def cmd_explotar(ruta):
    por_nombre, por_grupo = cargar_paleta()
    productos, _ = cargar_recetas()
    demanda = cargar_demanda(ruta)
    tallos, faltantes = explotar(demanda, productos, por_nombre, por_grupo)

    print("DEMANDA DE TALLOS (incluye 15%% de merma)\n")
    print("%-6s %-22s %-22s %8s" % ("SEM", "GRUPO", "FAMILIA COLOR", "TALLOS"))
    print("-" * 62)
    for (sem, grupo, fam), n in sorted(tallos.items()):
        print("%-6s %-22s %-22s %8.0f" % (sem, grupo[:22], fam[:22], n))

    por_sem = defaultdict(float)
    for (sem, _, _), n in tallos.items():
        por_sem[sem] += n
    print("\nTOTAL POR SEMANA")
    for sem in sorted(por_sem):
        print("  sem %-4s %8.0f tallos" % (sem, por_sem[sem]))

    if faltantes:
        print("\nPRODUCTOS PEDIDOS QUE NO ESTAN EN EL CATALOGO:")
        for f in faltantes:
            print("  ! %s" % f)


def cmd_sembrar(ruta):
    por_nombre, por_grupo = cargar_paleta()
    productos, _ = cargar_recetas()
    ciclos = cargar_ciclos()
    capacidad = cargar_capacidad()
    demanda = cargar_demanda(ruta)

    tallos, faltantes = explotar(demanda, productos, por_nombre, por_grupo)
    plan, sin_datos = plan_siembra(tallos, ciclos)

    print("PLAN DE SIEMBRA (retroceso desde la semana de cosecha)\n")
    print("%-6s %-20s %8s %8s %7s %7s %6s" % (
        "COSE.", "GRUPO", "TALLOS", "PLANTAS", "TRASPL", "BANDEJA", "VENT"))
    print("-" * 72)
    for p in plan:
        print("%-6s %-20s %8.0f %8.0f %7s %7s %6s" % (
            p["semana_cosecha"], p["grupo"][:20], p["tallos"], p["plantas"],
            p["semana_trasplante"],
            p["semana_siembra_bandeja"] if p["semana_siembra_bandeja"] is not None else "?",
            p["ventana_sem"] if p["ventana_sem"] is not None else "?"))

    total_plantas = sum(p["plantas"] for p in plan)
    sitios, pendientes = sitios_disponibles(capacidad)
    print("\nCAPACIDAD")
    print("  plantas requeridas por el plan : %8.0f" % total_plantas)
    print("  sitios medidos (1 planta/hueco): %8.0f" % sitios)
    print("  ocupacion                      : %8.1f%%" % (100 * total_plantas / sitios if sitios else 0))
    if pendientes:
        print("  bloques SIN medir (no suman)   : %s" % ", ".join(pendientes))

    if sin_datos:
        print("\nNO PLANIFICABLE — falta dato de ciclo (regla: no se inventa)")
        for s in sin_datos:
            print("  ! sem %-4s %-20s %7.0f tallos — %s"
                  % (s["semana_cosecha"], s["grupo"][:20], s["tallos"], s["motivo"]))
    if faltantes:
        print("\nPRODUCTOS SIN RECETA: %s" % ", ".join(faltantes))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[1]
    if cmd == "productos":
        cmd_productos()
    elif cmd == "auditar":
        cmd_auditar()
    elif cmd == "bouquet":
        if len(argv) < 3:
            raise SystemExit("Uso: python3 motor/cerebro.py bouquet \"Cosecha Grande\"")
        cmd_bouquet(argv[2])
    elif cmd == "explotar":
        if len(argv) < 3:
            raise SystemExit("Uso: python3 motor/cerebro.py explotar demanda.csv")
        cmd_explotar(argv[2])
    elif cmd == "sembrar":
        if len(argv) < 3:
            raise SystemExit("Uso: python3 motor/cerebro.py sembrar demanda.csv")
        cmd_sembrar(argv[2])
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
