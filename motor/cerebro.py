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
    python3 motor/cerebro.py matriz
    python3 motor/cerebro.py productos
    python3 motor/cerebro.py auditar
    python3 motor/cerebro.py bouquet "Cosecha Grande"
    python3 motor/cerebro.py ciclos
    python3 motor/cerebro.py cartera [grupo]
    python3 motor/cerebro.py rendimiento [grupo]
    python3 motor/cerebro.py explotar demanda.csv
    python3 motor/cerebro.py sembrar demanda.csv
"""

from __future__ import annotations

import csv
import datetime
import os
import re
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
    "BLANCO", "MARFIL", "CREMA", "PLATA", "BEIGE",
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
            # El subtipo es la unidad de manejo cuando el grupo es un
            # paraguas: en Celosia, cristata va a 7,5 cm y 1 tallo/planta y
            # plumosa a 15 cm y 4. La receta pide el SUBTIPO y el cultivar es
            # el que este en cosecha (Vanessa 2026-09-10).
            "subtipo": (fila.get("subtipo") or "").strip(),
        }
        # Una variedad retirada del cultivo sigue en la paleta como memoria
        # historica, pero NO es una opcion de color disponible.
        reg["retirada"] = reg["notas"].startswith("RETIRADA")
        for clave in (reg["nombre_completo"], "%s %s" % (reg["grupo"], reg["variedad"]), reg["variedad"]):
            por_nombre.setdefault(norm(clave), reg)
        if not reg["retirada"]:
            por_grupo[reg["grupo"]].append(reg)
    return por_nombre, dict(por_grupo)


def por_subtipo(por_grupo):
    """(grupo, subtipo) -> cultivares de ese subtipo, no retirados."""
    salida = defaultdict(list)
    for grupo, regs in por_grupo.items():
        for reg in regs:
            if reg.get("subtipo"):
                salida[(grupo, reg["subtipo"])].append(reg)
    return dict(salida)


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
            "perenne": (fila.get("perenne") or "").strip().lower() == "si",
            "fuente": fila["fuente"].strip(),
            "notas": fila["notas"].strip(),
            # El subtipo es la unidad de manejo cuando el grupo es un
            # paraguas: en Celosia, cristata va a 7,5 cm y 1 tallo/planta y
            # plumosa a 15 cm y 4. La receta pide el SUBTIPO y el cultivar es
            # el que este en cosecha (Vanessa 2026-09-10).
            "subtipo": (fila.get("subtipo") or "").strip(),
        }
    return ciclos


def es_perenne(grupo, ciclos=None):
    """Un cultivo perenne no se normaliza por planta.

    Se propaga por division — de Dahlia se sacan hijos — asi que el numero de
    plantas deriva con el tiempo y no sirve de denominador. El denominador
    correcto es el AREA, que es ademas la unidad del eje central del proyecto:
    margen por m2 por semana de cama ocupada.
    """
    if ciclos is None:
        ciclos = cargar_ciclos()
    g = norm(grupo)
    for clave, fila in ciclos.items():
        if clave and (clave in g or g in clave) and fila.get("perenne"):
            return True
    return False


# Motivos de cierre que NO significan "la planta dejo de producir".
# Extraidos de los COMENTARIOS de CAMPO — ver 13-optimizacion/04-...
# Solo 4 de 36 lotes cerraron por agotamiento real: si la ventana se mide como
# primer corte -> ultimo corte sin mirar esto, no mide la variedad sino una
# decision de Vanessa, y subestima a la variedad.
CIERRE_AJENO = {
    "espacio":         "se necesitaba la cama",
    "rotacion":        "esperando salir otro lote",
    "demanda":         "cortado para un pico comercial",
    "sanitario":       "sacrificado por plaga u hongo",
    "calidad":         "sacado por deformidad o vida en florero",
    "perdida_total":   "perdida total",
    "perdida_parcial": "perdida parcial",
    "temprano":        "cortado antes de tiempo — hubiese aguantado mas",
}

# 'tardio' se trata aparte: la cama NO se interrumpio, se paso de punto. No
# subestima a la variedad — al reves, los ultimos tallos bajaron de calidad.
# Meterlo en el mismo saco seria otra columna que miente.
CIERRE_TARDIO = "tardio"


def cargar_cierres():
    """Motivo de cierre por lote, extraido de los COMENTARIOS de CAMPO."""
    ruta = os.path.join(DATOS, "cierres_lote.csv")
    if not os.path.exists(ruta):
        return []
    with open(ruta, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def buscar_cierre(grupo, variedad, bloque, cierres):
    """Cruza un lote de REGISTRO con su fila de cierre.

    El cruce es difuso a proposito: cierres_lote.csv guarda el nombre como se
    escribio en CAMPO ("Celosias Indian Summer") mientras REGISTRO lo parte en
    grupo y variedad ("Celosia" + "Indian Summer"). Se exige que el grupo Y la
    variedad aparezcan en el nombre del cierre, y que el bloque case por
    prefijo — "3A bajas" cuenta como "3A".
    """
    g, v, b = norm(grupo), norm(variedad), norm_bloque(bloque)
    if not (g and b):
        return None
    for fila in cierres:
        nombre = norm(fila.get("variedad", ""))
        if g not in nombre:
            continue
        if v and v not in nombre:
            continue
        cb = norm_bloque(fila.get("bloque", ""))
        if not cb or not (cb.startswith(b) or b.startswith(cb)):
            continue
        return fila
    return None


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
    # La receta escribe "Dahlia", el registro de cosecha "Dahlias".
    "dahlia": ("GRUPO", "Dahlias"),
    # La receta escribe "Trachelium", la paleta el grupo "Trachellium".
    "trachelium": ("GRUPO", "Trachellium"),
    # "cabeza grande" y "cabeza pequena" son GRADO, no cultivares distintos
    # (Vanessa 2026-09-10). El grado es un atributo de calidad del tallo, no de
    # variedad: la receta lo pide y hoy no se mide en ninguna parte — es el
    # primer caso de uso real de calidad_tallo.csv, que esta vacio.
    "lisianthus cabeza grande": ("GRUPO", "Lisianthus"),
    "lisianthus cabeza pequena": ("GRUPO", "Lisianthus"),
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
      tipo: EXACTA | GRUPO | GRUPO_PARCIAL | SUBTIPO | SUSTITUCION |
            FOLLAJE | NO_FLOR | DESCONOCIDA
      reg:  registro de paleta si la resolucion es exacta
      opciones: variedades candidatas si el color queda abierto
    """
    clave = norm(ingrediente)

    # "Trachelium o Ammi" — la receta declara dos grupos intercambiables.
    # Vanessa 2026-08-13: "SUSTITUCION: el que haya". No es un ingrediente sin
    # resolver: es una receta que a proposito no se compromete. Se resuelve a
    # los dos grupos y el que suma la demanda decide que hacer con eso.
    if re.search(r"\bo\b", clave):
        partes = [p.strip() for p in re.split(r"\bo\b", clave) if p.strip()]
        if len(partes) > 1:
            grupos = []
            for parte in partes:
                g = next((gr for gr in por_grupo if norm(gr) == parte), None)
                # La receta escribe "Trachelium" y la paleta "Trachellium".
                # ALIAS es el lugar donde viven esas diferencias de escritura.
                if not g and parte in ALIAS:
                    modo, valor = ALIAS[parte]
                    if modo != "EXACTA" and valor in por_grupo:
                        g = valor
                if g:
                    grupos.append(g)
            if len(grupos) == len(partes):
                return {"tipo": "SUSTITUCION", "reg": None,
                        "opciones": [r for g in grupos for r in por_grupo[g]],
                        "grupos": grupos}

    # "Celosia plumosa" — grupo paraguas + subtipo. El cultivar queda abierto
    # a proposito: es el que este en cosecha esa semana.
    subs = por_subtipo(por_grupo)
    for (grupo, subtipo), regs in subs.items():
        if clave == norm("%s %s" % (grupo, subtipo)):
            return {"tipo": "SUBTIPO", "reg": None, "opciones": regs,
                    "grupo": grupo, "subtipo": subtipo}
    # "Celosia Dreams (spicata)" — nombra cultivar Y subtipo. norm() ya quito
    # el parentesis, asi que lo que queda es "celosia dreams spicata".
    for (grupo, subtipo), regs in subs.items():
        if clave.startswith(norm(grupo)) and clave.endswith(norm(subtipo)):
            return {"tipo": "SUBTIPO", "reg": None, "opciones": regs,
                    "grupo": grupo, "subtipo": subtipo}

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
    # Abierto POR DISENO: la receta fija el subtipo y el cultivar es el que
    # este en cosecha (Celosia, Vanessa 2026-09-10). Sigue siendo color
    # libre — cristata tiene hoy VERDE y CORAL en cosecha simultanea — pero
    # no es un descuido que haya que cerrar, y meterlo en el mismo saco que
    # un ingrediente sin definir hace que el numero mienta.
    tallos_abierto_diseno = 0.0
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
        elif res["tipo"] == "SUBTIPO":
            opciones = res["opciones"]
            if opciones:
                por_macro[opciones[0]["macro_rol"]] += cant
            por_familia["COLOR_LIBRE"] += cant
            tallos_color_libre += cant
            tallos_abierto_diseno += cant
            colores = sorted({o["familia_color"] for o in opciones
                              if o["familia_color"] not in ("MIX", "SIN_DATO")})
            incidencias.append(
                "'%s' fija el SUBTIPO y deja el cultivar abierto A PROPOSITO: "
                "%d tallos son el cultivar que este en cosecha. Color abierto "
                "entre %d familia(s): %s"
                % (ing["ingrediente"], cant, len(colores),
                   ", ".join(colores[:6]) or "sin datos")
            )
        elif res["tipo"] == "SUSTITUCION":
            opciones = res["opciones"]
            if opciones:
                por_macro[opciones[0]["macro_rol"]] += cant
            por_familia["COLOR_LIBRE"] += cant
            tallos_color_libre += cant
            incidencias.append(
                "'%s' es SUSTITUIBLE entre %s: %d tallos sin grupo fijado"
                % (ing["ingrediente"], " o ".join(res["grupos"]), cant)
            )
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
        "tallos_abierto_diseno": tallos_abierto_diseno,
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
            elif res["tipo"] in ("GRUPO", "GRUPO_PARCIAL", "SUBTIPO"):
                # SUBTIPO cae aqui a proposito: el grupo esta fijado y el
                # color queda abierto entre los cultivares de ese subtipo.
                tallos[(d["semana"], res.get("grupo", "?"), "COLOR_LIBRE")] += need
            elif res["tipo"] == "SUSTITUCION":
                # No hay un grupo al que cargarle el tallo: la receta acepta
                # cualquiera de los dos. Se reporta como sustitucion en vez de
                # elegir uno, que seria inventar la siembra.
                tallos[(d["semana"], "SUSTITUIBLE:%s" % " o ".join(res["grupos"]),
                        "COLOR_LIBRE")] += need
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
        if not c or c["sem_a_campo_max"] is None:
            sin_datos.append({"semana_cosecha": sem_cosecha, "grupo": grupo, "tallos": n_tallos,
                              "motivo": "SIN CICLO — no se puede fechar la siembra"})
            continue
        # Con ciclo pero sin tallos/planta se puede fechar la siembra aunque no
        # se pueda convertir tallos a plantas. La fecha ya es accionable.
        plantas = (n_tallos / c["tallos_planta"]) if c["tallos_planta"] else None
        if plantas is None:
            sin_datos.append({"semana_cosecha": sem_cosecha, "grupo": grupo, "tallos": n_tallos,
                              "motivo": "falta tallos/planta — fecha SI calculable, cantidad NO"})
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

    total_libre = total_dcb = total_diseno = 0.0
    for p in productos:
        a = analizar_producto(p, por_nombre, por_grupo)
        total_libre += a["tallos_color_libre"]
        total_diseno += a["tallos_abierto_diseno"]
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
    if total_diseno:
        print()
        print("De esos, %.0f tallos estan abiertos POR DISENO: la receta fija el"
              % total_diseno)
        print("subtipo de Celosia y el cultivar es el que este en cosecha esa")
        print("semana (Vanessa 2026-09-10). No son un descuido por cerrar.")
        print("Descontandolos, el descubierto real es %.0f%% (%.0f de %.0f)."
              % (100 * (total_libre - total_diseno) / total_dcb if total_dcb else 0,
                 total_libre - total_diseno, total_dcb))

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
        print("%-6s %-20s %8.0f %8s %7s %7s %6s" % (
            p["semana_cosecha"], p["grupo"][:20], p["tallos"],
            "%.0f" % p["plantas"] if p["plantas"] is not None else "?",
            p["semana_trasplante"],
            p["semana_siembra_bandeja"] if p["semana_siembra_bandeja"] is not None else "?",
            p["ventana_sem"] if p["ventana_sem"] is not None else "?"))

    total_plantas = sum(p["plantas"] for p in plan if p["plantas"] is not None)
    sitios, pendientes = sitios_disponibles(capacidad)
    print("\nCAPACIDAD")
    print("  plantas requeridas por el plan : %8.0f" % total_plantas)
    print("  sitios medidos (1 planta/hueco): %8.0f" % sitios)
    print("  ocupacion                      : %8.1f%%" % (100 * total_plantas / sitios if sitios else 0))
    if pendientes:
        print("  bloques SIN medir (no suman)   : %s" % ", ".join(pendientes))

    if sin_datos:
        print("\nDATOS FALTANTES (regla: no se inventa)")
        for s in sin_datos:
            print("  ! sem %-4s %-20s %7.0f tallos — %s"
                  % (s["semana_cosecha"], s["grupo"][:20], s["tallos"], s["motivo"]))
    if faltantes:
        print("\nPRODUCTOS SIN RECETA: %s" % ", ".join(faltantes))


# Antioquia tiene regimen bimodal: dos temporadas de lluvia y dos secas.
MESES_LLUVIA = {3, 4, 5, 9, 10, 11}

MES_NOMBRE = {
    "ENERO": 1, "FEBRERO": 2, "MARZO": 3, "ABRIL": 4, "MAYO": 5, "JUNIO": 6,
    "JULIO": 7, "AGOSTO": 8, "SEPTIEMBRE": 9, "OCTUBRE": 10, "NOVIEMBRE": 11,
    "DICIEMBRE": 12, "ENE": 1, "FEB": 2, "MAR": 3, "ABR": 4, "AGO": 8,
    "SEP": 9, "JUN": 6, "JUL": 7, "OCT": 10, "NOV": 11, "DIC": 12,
}


def _meses_de(texto):
    """CAMPO registra el inicio de cosecha como nombre de mes, no como fecha."""
    import re
    return [MES_NOMBRE[w] for w in re.findall(r"[A-ZÁÉÍÓÚ]+", (texto or "").upper())
            if w in MES_NOMBRE]


def ciclo_observado(fecha_siembra, texto_cosecha):
    """Ciclo trasplante -> inicio de cosecha, como RANGO.

    Devuelve (fecha_siembra, sem_min, sem_max) o None.

    El rango NO es opcional: como la cosecha se anota por mes y no por fecha,
    cualquier valor puntual seria falsa precision. sem_min asume cosecha el dia
    1 del mes; sem_max asume el ultimo dia.
    """
    import datetime as dt
    try:
        s = dt.date.fromisoformat((fecha_siembra or "").strip())
    except ValueError:
        return None
    meses = _meses_de(texto_cosecha)
    if not meses:
        return None
    lo = hi = None
    for m in meses:
        anio = s.year if m >= s.month else s.year + 1
        ini = dt.date(anio, m, 1)
        fin = dt.date(anio + (m == 12), 1 if m == 12 else m + 1, 1) - dt.timedelta(days=1)
        a, b = (ini - s).days / 7.0, (fin - s).days / 7.0
        lo = a if lo is None else min(lo, a)
        hi = b if hi is None else max(hi, b)
    if lo is None or hi <= 0:
        return None
    return (s, max(lo, 0.0), hi)


def cmd_ciclos():
    """Deriva ciclos reales de 07-datos/campo_siembras.csv (hoja CAMPO).

    Reporta primero la calidad del dato: sin eso, cualquier promedio enganaria.
    """
    filas = _leer_csv("campo_siembras.csv")
    n = len(filas)
    llenas = lambda k: sum(1 for f in filas if (f.get(k) or "").strip())

    print("=" * 74)
    print("CICLOS OBSERVADOS EN CAMPO — %d siembras registradas" % n)
    print("=" * 74)
    print("\nCALIDAD DEL DATO (leer esto antes de creer cualquier promedio)")
    for k in ("Fecha siembra campo", "Inicio cosecha", "Fin de cosecha"):
        c = llenas(k)
        print("  %-22s %3d llenas  %5.0f%%" % (k, c, 100.0 * c / n if n else 0))

    tri = sum(1 for f in filas
              if (f.get("Fecha siembra campo") or "").strip()
              and (f.get("Inicio cosecha") or "").strip()
              and (f.get("Fin de cosecha") or "").strip())
    print("  filas con las TRES fechas %3d           <- la VENTANA solo sale de aqui" % tri)

    obs = []
    for f in filas:
        c = ciclo_observado(f.get("Fecha siembra campo"), f.get("Inicio cosecha"))
        if c:
            obs.append((f, c[0], c[1], c[2]))
    print("\n  ciclo calculable en %d de %d filas (%.0f%%)" % (len(obs), n, 100.0 * len(obs) / n if n else 0))

    meses_cubiertos = sorted({s.month for _, s, _, _ in obs})
    print("  meses del anio con siembras fechadas: %s" % (meses_cubiertos or "ninguno"))
    if len(meses_cubiertos) < 12:
        print("  ADVERTENCIA: faltan %d meses. No hay base para predecir en esos meses."
              % (12 - len(meses_cubiertos)))

    # Por grupo homologado
    por_grupo = defaultdict(list)
    for f, s, lo, hi in obs:
        clave = ((f.get("Nombre Homologados") or "").strip()
                 or (f.get("Variedad") or "").strip() or "?")
        por_grupo[clave].append((s.month, lo, hi))

    print("\nCICLO POR NOMBRE HOMOLOGADO (rango, no valor puntual)")
    print("%-32s %4s %10s %10s" % ("HOMOLOGADO", "N", "PISO", "TECHO"))
    print("-" * 60)
    for k, v in sorted(por_grupo.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(v) < 2:
            continue
        print("%-32s %4d %8.1f s %8.1f s" % (
            k[:32], len(v), sum(x[1] for x in v) / len(v), sum(x[2] for x in v) / len(v)))

    # Temporada
    secas = [(lo + hi) / 2 for _, s, lo, hi in obs if s.month not in MESES_LLUVIA]
    lluvias = [(lo + hi) / 2 for _, s, lo, hi in obs if s.month in MESES_LLUVIA]
    print("\nEFECTO DE TEMPORADA (Antioquia bimodal: lluvia mar-may y sep-nov)")
    if secas:
        print("  SECA    n=%-3d ciclo medio %.1f sem" % (len(secas), sum(secas) / len(secas)))
    if lluvias:
        print("  LLUVIA  n=%-3d ciclo medio %.1f sem" % (len(lluvias), sum(lluvias) / len(lluvias)))
    if secas and lluvias:
        dif = abs(sum(secas) / len(secas) - sum(lluvias) / len(lluvias))
        ruido = sum(hi - lo for _, _, lo, hi in obs) / len(obs)
        print("  diferencia observada : %.1f sem" % dif)
        print("  ruido de medicion    : %.1f sem  (por anotar la cosecha por mes)" % ruido)
        if dif < ruido:
            print("\n  >> El efecto de temporada (%.1f sem) es MENOR que el ruido de" % dif)
            print("     medicion (%.1f sem). Con este dato NO se puede afirmar que la" % ruido)
            print("     temporada mueva el ciclo. Para poder afirmarlo hace falta")
            print("     anotar 'Inicio cosecha' y 'Fin de cosecha' como FECHA.")


# El mismo grupo se llama distinto en cada archivo. REGISTRO usa el nombre en
# espanol y CAMPO el comercial. Sin esto, el grupo mas grande del cultivo —60
# siembras de Snapdragon— no cruza con sus 6.221 tallos cosechados.
SINONIMOS_GRUPO = {
    "boca de dragon": "snapdragon",
    "colitas de conejo": "bunny tails",   # confirmado por Vanessa 2026-08-13
}

# Palabras que describen la cama pero no la identifican: "CAMAS BAJAS 3A" es
# el bloque 3A.
_RUIDO_BLOQUE = ("camas", "cama", "bajas", "baja", "altas", "alta", "del",
                 "de", "la", "el", "y")


def alias_grupo(grupo):
    """Devuelve todas las formas conocidas de nombrar un grupo."""
    g = norm(grupo)
    formas = {g}
    for a, b in SINONIMOS_GRUPO.items():
        if g == a or a in g:
            formas.add(b)
        if g == b or b in g:
            formas.add(a)
    return {f for f in formas if f}


def bloques_de(texto):
    """Codigos de cama que aparecen en un texto libre.

    CAMPO escribe "CAMAS BAJAS 3A", "Gomphrenas 3B", "5 y 3C" o "3A+3B+4A".
    Devuelve el conjunto de camas mencionadas — varias si el texto nombra
    varias, que es informacion honesta: ese lote ocupa mas de una.
    """
    t = norm(texto)
    for r in _RUIDO_BLOQUE:
        t = re.sub(r"\b%s\b" % r, " ", t)
    partes = re.split(r"[+,/]| y |\s+", t)
    salida = set()
    for p in partes:
        b = norm_bloque(p)
        # Solo lo que tiene forma de cama. Sin este filtro entraban "inv" del
        # propio prefijo, el nombre del cultivo en "Gomphrenas 3B", y el "1"
        # de "5+ 1 del 4A", que es un conteo de camas y no un bloque.
        if b and re.match(r"^(ext)?\d[a-c]?$|^mini$|^ext$", b):
            salida.add(b)
    return salida


def _plantas_del_lote(grupo, variedad, bloque, plantas):
    """Cuantas plantas se trasplantaron en el lote que produjo estos tallos.

    Cruza REGISTRO (grupo + variedad + bloque) con CAMPO (Variedad + Nombre
    Homologado + Bloque sembrado). Tres cosas lo hacen dificil y las tres
    estan resueltas aqui:

      * el grupo se llama distinto en cada archivo (ver SINONIMOS_GRUPO)
      * el bloque tiene 46 grafias y a veces viene con prosa alrededor
      * la variedad del registro es la serie ("Monaco Orange") y en CAMPO
        aparece dentro del nombre completo ("Snapdragon Monaco Orange")

    "Mix" y las variedades vacias NO identifican un cultivar, asi que para
    ellas basta grupo + bloque. Es deliberado: devolver el total del bloque es
    correcto cuando el corte fue efectivamente mezclado.
    """
    alias = alias_grupo(grupo)
    v = norm(variedad)
    generica = v in ("", "mix", "sin variedad")
    total = 0.0
    faltan = 0
    for (hom, var, blo, tiene), n in plantas.items():
        if blo not in bloques_de(bloque):
            continue
        if not any(a in var for a in alias):
            continue
        if not generica and not (v in hom or (hom and hom in v) or v in var):
            continue
        if tiene:
            total += n
        else:
            faltan += 1
    if not total:
        return None, 0
    return total, faltan


def norm_bloque(texto):
    """Unifica las 46 grafias distintas de bloque que hay entre los archivos.

    CAMPO escribe "3B" y REGISTRO "Inv 3B", pero ademas conviven "Inv3b",
    "inv3b" y "3b". La version anterior solo quitaba el prefijo CUANDO HABIA
    ESPACIO, asi que "Inv 5" quedaba en "5" y "Inv5" en "inv5" — dos claves
    distintas para la misma cama, y el cruce con las plantas fallaba en
    silencio en la mayoria de los lotes.

    El exterior se conserva SEPARADO del invernadero a proposito: "ext 3B" es
    una cama al aire libre y "Inv 3B" esta bajo plastico. Son microclimas
    opuestos — mezclarlos inventaria un lote que no existe.
    """
    t = norm(texto).replace(" ", "")
    if not t:
        return ""
    # exterior, venga como prefijo ("ext3b", "exterior") o sufijo ("3ext")
    for pref in ("exterior", "ext"):
        if t.startswith(pref):
            return "ext" + t[len(pref):]
    for suf in ("exterior", "ext"):
        if t.endswith(suf) and len(t) > len(suf):
            return "ext" + t[:-len(suf)]
    # invernadero
    for pref in ("invernadero", "inv"):
        if t.startswith(pref) and len(t) > len(pref):
            return t[len(pref):]
    return t


def cmd_rendimiento(grupo=None):
    """Rendimiento real por variedad y bloque, NORMALIZADO por ventana.

    Por que normaliza: comparar tallos/planta entre dos variedades cuyas
    ventanas de cosecha llevan distinto tiempo transcurrido produce una
    conclusion falsa. Es el mismo error que C-cierre-de-lote.md advierte para
    los lotes sacrificados: un lote interrumpido parece de bajo rendimiento
    cuando en realidad fue interrumpido.

    El caso que motivo este comando: Campanula Champion Lavender parecia
    rendir 0.64 t/planta contra 0.92 de la blanca en la MISMA cama. Pero la
    lavanda llevaba 18 dias de ventana y la blanca 27. Por planta por dia son
    iguales.
    """
    import datetime as dt
    import re

    siembras = _leer_csv("campo_siembras.csv")
    cosecha = _leer_csv("registro_tallos.csv")

    # Plantas trasplantadas. Se guarda tambien la columna Variedad de CAMPO
    # porque es la unica que trae el GRUPO: los homologados son "Monaco
    # Orange" u "Opus Fresh", que no dicen a que grupo pertenecen. Sin eso el
    # cruce exigia que el grupo apareciera en el homologado y fallaba en el
    # 90% de los lotes.
    plantas = defaultdict(float)
    for s in siembras:
        hom = norm(s.get("Nombre Homologados") or "")
        var = norm(s.get("Variedad") or "")
        n = num((s.get("Cantidad Trasplantada") or "").strip())
        if not (hom or var):
            continue
        # Una siembra SIN cantidad trasplantada se registra igual, marcada.
        # Si no, su cosecha se divide entre las plantas de las otras camas y
        # el tallos/planta sale inflado: en Zinnia 4B hay 4 siembras y solo 1
        # tiene conteo, asi que el resultado salia 4 veces mas alto.
        if not n:
            for blo in bloques_de(s.get("Bloque sembrado") or ""):
                plantas[(hom, var, blo, False)] += 0
            continue
        for blo in bloques_de(s.get("Bloque sembrado") or ""):
            plantas[(hom, var, blo, True)] += n

    # cosecha por (grupo, variedad, bloque)
    lotes = defaultdict(lambda: {"tallos": 0.0, "fechas": []})
    # El corte del REGISTRO se mide sobre todas las filas, no sobre las del
    # filtro: una ventana esta abierta si sigue produciendo hasta donde llega
    # el registro completo. Medido contra el maximo del grupo, un lote que
    # dejo de producir en julio se marcaria ABIERTA solo porque es el ultimo
    # de su grupo, aunque el registro siga tres semanas mas.
    corte_registro = ""
    sin_variedad = 0
    for c in cosecha:
        g = (c.get("Grupo") or "").strip()
        v = (c.get("Variedad / Serie") or "").strip()
        b = (c.get("Bloque") or "").strip()
        f = (c.get("Fecha") or "").strip()
        # Antes se exigia tambien la variedad, y eso descartaba en silencio
        # cultivos enteros: Esparrago, Dahlias y Colitas de conejo se registran
        # sin serie, asi que sus 530 tallos no aparecian en ningun reporte.
        # Un lote sin variedad es un lote igual; se etiqueta y se ve.
        if not (g and b) or not re.match(r"^\d{4}-\d{2}-\d{2}$", f):
            continue
        if not v:
            v = "(sin variedad)"
            sin_variedad += 1
        corte_registro = max(corte_registro, f)
        if grupo and norm(grupo) not in norm(g):
            continue
        # La clave usa el bloque NORMALIZADO: "Inv 4C" e "Inv4c" son la misma
        # cama y antes salian como dos lotes, cada uno reclamando el total de
        # plantas de la cama. Eso partia la cosecha en dos y subestimaba el
        # tallos/planta de ambos.
        t = num(c.get("Tallos frescos") or "")
        clave_b = "+".join(sorted(bloques_de(b))) or norm_bloque(b)
        d = lotes[(g, v, clave_b)]
        d["tallos"] += t or 0
        d["fechas"].append(f)

    if not lotes:
        raise SystemExit("Sin datos de cosecha para '%s'." % (grupo or "el filtro"))

    corte = corte_registro
    ultima_filtro = max(f for d in lotes.values() for f in d["fechas"])
    print("RENDIMIENTO REAL NORMALIZADO POR VENTANA")
    print("El registro de cosecha corta el %s — las ventanas abiertas en esa" % corte)
    print("fecha estan TRUNCADAS, no cerradas.")
    if ultima_filtro != corte:
        print("La ultima cosecha registrada de este filtro es del %s, o sea que"
              % ultima_filtro)
        print("ningun lote de aqui sigue abierto al cierre del registro.")
    print()
    print("%-14s %-20s %-8s %7s %8s %6s %9s %12s" % (
        "GRUPO", "VARIEDAD", "BLOQUE", "PLANTAS", "TALLOS", "DIAS", "T/PLANTA", "T/PLANTA/DIA"))
    print("-" * 94)

    filas, sospechosas = [], []
    ciclos_perenne = cargar_ciclos()
    cierres = cargar_cierres()
    hubo_perenne = False
    cerrados_ajenos, cerrados_tarde = [], []
    denom_incompleto = 0
    for (g, v, b), d in sorted(lotes.items(), key=lambda kv: (kv[0][0], -kv[1]["tallos"])):
        fs = sorted(d["fechas"])
        # Hay errores de tipeo de ano en el registro (fechas de 2025 dentro de
        # un lote de 2026). Se detectan como puntos alejados de la mediana y se
        # REPORTAN, no se corrigen en silencio.
        ds = [dt.date.fromisoformat(x) for x in fs]
        mediana = ds[len(ds) // 2]
        sanas = [x for x in ds if abs((x - mediana).days) <= 60]
        raras = [x.isoformat() for x in ds if abs((x - mediana).days) > 60]
        if raras:
            sospechosas.append((g, v, b, raras))
        a, z = min(sanas), max(sanas)
        dias = (z - a).days + 1
        # El homologado es "<Grupo> <Color>" (ej. "Campanula Lavender") y la
        # variedad del registro es "<Serie> <Color>" (ej. "Champion Lavender").
        # El puente es el color, que es la ultima palabra de ambos.
        pl, sin_conteo = _plantas_del_lote(g, v, b, plantas)
        # Un perenne NO se normaliza por planta: se propaga por division y el
        # numero de plantas deriva. Mostrar "?" ahi confundiria "no se" con
        # "no aplica", que es justo el error que hace sacar conclusiones falsas.
        perenne = es_perenne(g, ciclos_perenne)
        if perenne:
            pl = None
        tp = (d["tallos"] / pl) if pl else None
        tpd = (tp / dias) if tp else None
        abierta = fs[-1] == corte
        marca = "<- ABIERTA" if abierta else ""
        if perenne:
            marca = ("PERENNE: normalizar por m2 " + marca).strip()
            hubo_perenne = True

        # Una ventana cerrada por espacio, demanda o sanidad NO mide a la
        # variedad. Si no se marca, este lote parece de bajo rendimiento
        # cuando en realidad fue interrumpido.
        if pl and sin_conteo:
            marca = ("DENOMINADOR INCOMPLETO: %d siembra(s) sin conteo %s"
                     % (sin_conteo, marca)).strip()
            denom_incompleto += 1
        cie = buscar_cierre(g, v, b, cierres)
        motivo = (cie or {}).get("motivo", "")
        if motivo in CIERRE_AJENO:
            marca = ("CIERRE AJENO: %s %s" % (motivo, marca)).strip()
            cerrados_ajenos.append((g, v, b, motivo, cie.get("evidencia_literal", "")))
        elif motivo == CIERRE_TARDIO:
            marca = ("PASADO DE PUNTO %s" % marca).strip()
            cerrados_tarde.append((g, v, b, cie.get("evidencia_literal", "")))
        print("%-14s %-20s %-8s %7s %8.0f %6d %9s %12s %s" % (
            g[:14], v[:20], b[:8],
            "%.0f" % pl if pl else ("n/a" if perenne else "?"), d["tallos"], dias,
            "%.2f" % tp if tp else ("n/a" if perenne else "?"),
            "%.4f" % tpd if tpd else ("n/a" if perenne else "?"),
            marca))
        if tpd:
            filas.append((g, v, b, tpd, tp, dias, abierta))

    if denom_incompleto:
        print()
        print("%d lote(s) con DENOMINADOR INCOMPLETO: en esa cama hay siembras sin" % denom_incompleto)
        print("cantidad trasplantada, asi que la cosecha se divide entre menos plantas")
        print("de las que hubo. Ese tallos/planta es un TECHO, no una medicion — y")
        print("este error INFLA, al reves que la ventana truncada.")

    if cerrados_ajenos:
        print()
        print("%d lote(s) con CIERRE AJENO — la cama se cerro por una razon que no" % len(cerrados_ajenos))
        print("es la planta, asi que su ventana esta INTERRUMPIDA, no terminada. El")
        print("tallos/planta de estas filas SUBESTIMA a la variedad:")
        for g, v, b, motivo, ev in cerrados_ajenos:
            print("  %s %s (%s) — %s" % (g, v, b, CIERRE_AJENO[motivo]))
            if ev:
                print("      \"%s\"" % ev[:88])
        print("  (%d de %d cierres conocidos cruzaron con un lote cosechado; el resto"
              % (len(cerrados_ajenos) + len(cerrados_tarde), len(cierres)))
        print("   es de lotes anteriores al rango del registro de tallos)")

    if cerrados_tarde:
        print()
        print("%d lote(s) PASADOS DE PUNTO. Aqui la ventana no se interrumpio: se"
              % len(cerrados_tarde))
        print("estiro de mas, asi que el tallos/planta NO esta subestimado — pero los")
        print("ultimos tallos entraron con menos calidad:")
        for g, v, b, ev in cerrados_tarde:
            print("  %s %s (%s)" % (g, v, b))
            if ev:
                print("      \"%s\"" % ev[:88])

    if sin_variedad:
        print()
        print("%d registros no traen variedad y salen como (sin variedad)." % sin_variedad)
        print("Antes se descartaban en silencio. Sin la serie no se pueden comparar")
        print("cultivares entre si — conviene llenarla en REGISTRO.")

    if hubo_perenne:
        print()
        print("n/a NO es un dato faltante. Un perenne se propaga por division —")
        print("de Dahlia se sacan hijos — asi que el numero de plantas deriva y no")
        print("sirve de denominador. Hay que medir AREA (m2) y comparar tallos/m2,")
        print("que es ademas la unidad del eje del proyecto: margen por m2 por")
        print("semana de cama ocupada. Falta el area en rendimiento_costo_lote.csv.")

    # comparaciones dentro del mismo grupo y bloque
    por_gb = defaultdict(list)
    for g, v, b, tpd, tp, dias, ab in filas:
        por_gb[(g, b)].append((v, tpd, tp, dias, ab))
    hay = False
    for (g, b), l in sorted(por_gb.items()):
        if len(l) < 2:
            continue
        if not hay:
            print("\nCOMPARACION DENTRO DEL MISMO BLOQUE (misma agua, misma luz, mismo suelo)")
            hay = True
        l.sort(key=lambda x: -x[1])
        mejor = l[0]
        print("\n  %s en %s — ordenado por tallos/planta/dia:" % (g, b))
        for v, tpd, tp, dias, ab in l:
            dif = 100 * (tpd / mejor[1] - 1)
            print("    %-22s %.4f t/pl/dia  (%.2f t/pl en %d dias) %+6.1f%%%s"
                  % (v[:22], tpd, tp, dias, dif, "  ventana ABIERTA" if ab else ""))
        dias_distintos = len({x[3] for x in l}) > 1
        if dias_distintos:
            print("    OJO: las ventanas llevan distinto tiempo. Comparar t/planta")
            print("         a secas sobreestima a la que lleva mas dias.")

    if sospechosas:
        print("\nFECHAS SOSPECHOSAS EXCLUIDAS DEL CALCULO DE VENTANA")
        print("(probable error de ano en el registro — corregir en la fuente)")
        for g, v, b, raras in sospechosas:
            print("  %s / %s / %s: %s" % (g, v, b, ", ".join(raras)))


def cmd_valor():
    """Valor por tallo propio — palanca de optimizacion disponible HOY.

    No requiere costos_productos.csv (que esta vacio). Mide cuanto ingreso
    genera cada tallo DCB y cuanto del volumen se apalanca en follaje comprado.
    """
    por_nombre, por_grupo = cargar_paleta()
    productos, _ = cargar_recetas()

    filas = []
    for p in productos:
        a = analizar_producto(p, por_nombre, por_grupo)
        if not a["tallos_dcb"] or not a["precio"]:
            continue
        comprado = a["total_tallos"] - a["tallos_dcb"]
        filas.append({
            "producto": p["producto"],
            "precio": a["precio"],
            "tallos_dcb": a["tallos_dcb"],
            "comprado": comprado,
            "pct_comprado": comprado / a["total_tallos"] if a["total_tallos"] else 0.0,
            "por_tallo": a["precio"] / a["tallos_dcb"],
        })

    filas.sort(key=lambda f: -f["por_tallo"])
    print("VALOR POR TALLO PROPIO — ordenado de mayor a menor\n")
    print("%-38s %9s %7s %8s %8s" % ("PRODUCTO", "$/TALLO", "T.DCB", "COMPRADO", "%COMPR"))
    print("-" * 76)
    for f in filas:
        print("%-38s %9s %7.0f %8.0f %7.0f%%" % (
            f["producto"][:38],
            "{:,.0f}".format(f["por_tallo"]).replace(",", "."),
            f["tallos_dcb"], f["comprado"], 100 * f["pct_comprado"]))

    mejor, peor = filas[0], filas[-1]
    print("\nLECTURA")
    print("  mejor : %-34s $%s por tallo propio"
          % (mejor["producto"][:34], "{:,.0f}".format(mejor["por_tallo"]).replace(",", ".")))
    print("  peor  : %-34s $%s por tallo propio"
          % (peor["producto"][:34], "{:,.0f}".format(peor["por_tallo"]).replace(",", ".")))
    print("  brecha: %.1fx" % (mejor["por_tallo"] / peor["por_tallo"]))
    print("\n  El follaje comprado apalanca volumen sin gastar cama. Los productos")
    print("  con 0% comprado se sostienen solo con tallo propio: son los que mas")
    print("  cama consumen por peso de venta.")
    print("\n  NOTA: esto es ingreso por tallo, NO margen. El margen requiere")
    print("  costos_productos.csv, que hoy esta vacio (bloqueo #2 del roadmap).")


# --------------------------------------------------------------------------
# La matriz de decision: que tan lejos esta el motor de poder decidir DONDE
# --------------------------------------------------------------------------

def _leer_opcional(nombre):
    """Como _leer_csv pero devuelve [] si el archivo no existe todavia.

    La matriz mide huecos, asi que un archivo ausente es un resultado valido
    (cobertura 0), no un error que aborte el reporte.
    """
    ruta = os.path.join(DATOS, nombre)
    if not os.path.exists(ruta):
        return []
    with open(ruta, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


VACIO = ("", "SIN_DATO", "-", "?", "N/A", "PENDIENTE")


def _lleno(valor):
    return (valor or "").strip().upper() not in [v.upper() for v in VACIO]


def _es_numero(valor):
    try:
        float((valor or "").strip().replace(",", "."))
        return True
    except ValueError:
        return False


def cobertura_matriz():
    """Devuelve una lista de dicts, uno por variable de decision.

    cubierto/total son conteos reales sobre los CSV. Ninguna variable se da
    por buena sin contarla: si el archivo no existe, la cobertura es 0.
    """
    filas = []

    def add(n, nombre, cubierto, total, unidad, desbloquea, nota=""):
        filas.append({
            "n": n, "nombre": nombre, "cub": cubierto, "tot": total,
            "unidad": unidad, "desbloquea": desbloquea, "nota": nota,
        })

    # 1 — Demanda: el cultivar fijado en la receta es lo que hace consultable
    #     la demanda de color. Sin cultivar, la receta no pide un color.
    recetas = _leer_opcional("formulas_productos_bouquets.csv")
    por_nombre, por_grupo = cargar_paleta()
    dcb = fijos = 0
    for fila in recetas:
        if norm(fila.get("Origen", "")) != "dcb":
            continue
        cant = num(fila.get("Cantidad", ""))
        if cant is None:
            continue
        dcb += cant
        res = resolver(fila.get("Ingrediente", ""), por_nombre, por_grupo)
        if res["tipo"] in ("EXACTA", "FOLLAJE", "NO_FLOR"):
            fijos += cant
    add(1, "Demanda de color y producto", fijos, dcb, "tallos DCB con cultivar fijado",
        "que la receta pida un color y no un grupo",
        "objetivo_color_pdv.csv esta como PROPUESTA SIN VALIDAR (faltan datos de 03_Ventas)")

    # 2 — Ciclo, ventana, tallos/planta
    ciclos = _leer_opcional("ciclos_variedad.csv")
    completos = sum(1 for f in ciclos if _lleno(f.get("sem_a_campo_min"))
                    and _lleno(f.get("ventana_sem_min")) and _lleno(f.get("tallos_planta")))
    add(2, "Ciclo, ventana y tallos/planta", completos, len(ciclos), "grupos",
        "fechar la siembra hacia atras desde la demanda")

    # 3 — Microclima MEDIDO (no cualitativo): temperatura y humedad numericas
    micro = _leer_opcional("microclima_bloques.csv")
    medidos = sum(1 for f in micro if _es_numero(f.get("temp_min_c"))
                  and _es_numero(f.get("hum_rel_max_pct")))
    add(3, "Microclima medido por bloque", medidos, len(micro), "zonas con T y HR numericas",
        "cruzar zona con riesgo de hongo y velocidad de ciclo",
        "hay %d zonas descritas en cualitativo (ALTA/MEDIA/BAJA)" % len(micro))

    # 4 — Presion y uniformidad de riego
    riego = sum(1 for f in micro if _lleno(f.get("presion_agua")) and _lleno(f.get("uniformidad_riego")))
    add(4, "Presion y uniformidad de riego", riego, len(micro), "zonas con presion y uniformidad",
        "explicar por que solo ~22% del area rinde a potencial")

    # 5 — Suelo por zona
    suelo = sum(1 for f in micro if _lleno(f.get("suelo_estado")))
    add(5, "Estado de suelo por zona", suelo, len(micro), "zonas con suelo caracterizado",
        "decidir que variedad tolera esa cama")

    # 6 — Historia fitosanitaria: existir no basta, hay que poder cruzarla por
    #     semana de ciclo. Un evento con la semana ambigua no predice nada.
    inc = _leer_opcional("incidencia_fitosanitaria.csv")
    fechables = sum(1 for f in inc if (f.get("tipo_semana", "").strip().upper() in ("ISO", "CAMPO"))
                    and _lleno(f.get("momento_reportado")))
    add(6, "Historico de plagas y hongos", fechables, len(inc), "eventos con semana resuelta",
        "predecir en que semana del ciclo aparece el problema",
        "extraidos de texto libre; la semana reportada es ambigua entre ISO y semana de campo")

    # 7 — Clima semanal contra las semanas que si tienen cosecha registrada
    clima = _leer_opcional("clima_semanal.csv")
    reg = _leer_opcional("registro_tallos.csv")
    sem_cosecha = set()
    for f in reg:
        fecha = (f.get("Fecha") or "").strip()[:10]
        try:
            sem_cosecha.add(datetime.date.fromisoformat(fecha).isocalendar()[1])
        except ValueError:
            continue
    sem_clima = set()
    for f in clima:
        if _es_numero(f.get("semana_iso")):
            sem_clima.add(int(float(f["semana_iso"])))
    add(7, "Clima semanal de la finca", len(sem_clima & sem_cosecha), len(sem_cosecha) or 1,
        "semanas ISO con cosecha y clima",
        "separar el efecto de temporada del efecto de variedad")

    # 8 — Rendimiento: un lote cuenta si tiene tallos Y plantas para dividir
    campo = _leer_opcional("campo_siembras.csv")
    plantas = {}
    for f in campo:
        clave = (norm(f.get("Nombre Homologados", "")), norm_bloque(f.get("Bloque sembrado", "")))
        if clave[0] and _es_numero(f.get("Cantidad Trasplantada")):
            plantas[clave] = True
    lotes, con_plantas = set(), set()
    for f in reg:
        clave = (norm(f.get("Variedad / Serie", "")), norm_bloque(f.get("Bloque", "")))
        if not clave[0]:
            continue
        lotes.add(clave)
        if clave in plantas:
            con_plantas.add(clave)
    add(8, "Rendimiento normalizado por ventana", len(con_plantas), len(lotes) or 1,
        "lotes con tallos Y numero de plantas",
        "comparar variedades sin el sesgo de ventana truncada")

    # 9 — Calidad de tallo
    cal = _leer_opcional("calidad_tallo.csv")
    add(9, "Calidad de tallo (longitud, grado)", len(cal), len(lotes) or 1, "lotes medidos",
        "separar 'produjo' de 'produjo vendible'",
        "hoy la longitud de tallo NO se mide en ninguna parte del repositorio")

    # 10 — Capacidad de camas
    cap = _leer_opcional("capacidad_bloques.csv")
    medidas = sum(1 for f in cap if _es_numero(f.get("Huecos (largo)")))
    add(10, "Capacidad de camas", medidas, len(cap), "bloques medidos",
        "saber si la siembra cabe en la semana que se necesita")

    # 11 — Costos
    cos = _leer_opcional("costos_productos.csv")
    add(11, "Costo de semilla, insumos y mano de obra", len(cos), 1, "filas de costo",
        "margen por m2 por semana — el eje que une los otros tres")

    return filas


# --------------------------------------------------------------------------
# Cartera de variedades: que se queda, que se va, de que falta y de que sobra
# --------------------------------------------------------------------------

def demanda_catalogo():
    """Tallos DCB que pide el catalogo, por grupo.

    CANASTA NO PONDERADA: asume una unidad de cada producto. El volumen de
    venta por producto vive en 03_Ventas, fuera del alcance de este proyecto,
    y ponderar a ojo seria inventar demanda. Asi que este numero dice
    "cuanto pesa el grupo en el CATALOGO", no "cuanto pesa en la CAJA".
    Es un proxy, y como proxy se reporta.

    Devuelve (demanda, en_productos, pendientes, n_productos):
      pendientes = ingredientes DCB que la paleta no resuelve. NO se suman a
      ningun grupo: se listan con su grupo candidato para que Vanessa decida.
      Meterlos por deduccion del nombre violaria la regla 8.
    """
    productos, _ = cargar_recetas()
    por_nombre, por_grupo = cargar_paleta()
    grupos = sorted(por_grupo, key=lambda g: -len(g))

    demanda = defaultdict(float)
    en_productos = defaultdict(set)
    por_subtipo_dem = defaultdict(float)
    sustituciones = defaultdict(lambda: {"cant": 0.0, "prods": set()})
    pendientes = []

    for prod in productos:
        for ing in prod["ingredientes"]:
            if (ing["origen"] or "").lower().startswith("compr"):
                continue
            cant = ing["cant_max"] or ing["cant_min"] or 0.0
            res = resolver(ing["ingrediente"], por_nombre, por_grupo)

            # Ingrediente sustituible ("Trachelium o Ammi"). NO se suma a
            # ningun grupo: inflaria los dos. Se cuenta una vez en su propio
            # cajon y se reporta aparte.
            if res["tipo"] == "SUSTITUCION":
                clave = " o ".join(res["grupos"])
                sustituciones[clave]["cant"] += cant
                sustituciones[clave]["prods"].add(prod["producto"])
                continue

            grupo = None
            if res["tipo"] == "EXACTA" and res["reg"]:
                grupo = res["reg"].get("grupo")
            elif res.get("grupo"):
                grupo = res["grupo"]
            if res["tipo"] == "SUBTIPO":
                por_subtipo_dem[(res["grupo"], res["subtipo"])] += cant
            if grupo:
                demanda[grupo] += cant
                en_productos[grupo].add(prod["producto"])
                continue
            if res["tipo"] == "NO_FLOR":
                continue
            # Sin vinculo. Se busca un grupo candidato por prefijo, y se
            # reporta como candidato — no se cuenta como demanda.
            clave = norm(ing["ingrediente"])
            candidato = next((g for g in grupos if clave.startswith(norm(g))), None)
            pendientes.append({
                "ingrediente": ing["ingrediente"],
                "producto": prod["producto"],
                "cantidad": cant,
                "candidato": candidato,
            })
    return {"demanda": demanda, "en_productos": en_productos,
            "pendientes": pendientes, "n_productos": len(productos),
            "subtipos": por_subtipo_dem, "sustituciones": sustituciones}


def cargar_roles():
    """Rol de cada grupo en la cartera. Dictado por Vanessa el 2026-09-10.

    LA PREMISA QUE FALTABA: no todo se siembra todo el tiempo, y los grupos NO
    compiten entre si en una sola lista. Hay tres niveles con reglas distintas:

      BASE / BASE_ENCAJE  siempre debe haber. Un hueco es una falla.
      FOCAL               siempre debe haber UNA flor principal. El rol no
                          puede quedar vacio, pero se llena con la que sea.
      TOQUE               rota A PROPOSITO, poca cantidad, en Inv 2. El poco
                          volumen NO es un fracaso: es el diseno. Lo que
                          genera venta es que la gente no lo haya visto en un
                          rato.

    Comparar un TOQUE contra la demanda del catalogo por volumen es un error de
    categoria: mediria como fracaso lo que es una decision.
    """
    roles = {}
    for fila in _leer_opcional("roles_cartera.csv"):
        g = (fila.get("grupo") or "").strip()
        if g:
            # Un grupo puede tener varias filas: Celosia tiene una regla por
            # subtipo y Dusty Miller una por cultivar. Se guarda la lista y el
            # rol del grupo es el de su primera fila.
            roles.setdefault(g, {
                "rol": (fila.get("rol_cartera") or "").strip(),
                "alterna_con": (fila.get("alterna_con") or "").strip(),
                "area": (fila.get("area_objetivo") or "").strip(),
                "cadencia": (fila.get("cadencia_siembra") or "").strip(),
                "ventana": (fila.get("ventana_objetivo") or "").strip(),
                "destino": (fila.get("destino") or "").strip(),
                "no_solapar": (fila.get("no_solapar") or "").strip() == "SI",
                "regla": (fila.get("regla") or "").strip(),
                "notas": (fila.get("notas") or "").strip(),
                "filas": [],
            })
            roles[g]["filas"].append({
                "subtipo": (fila.get("subtipo_o_cultivar") or "").strip(),
                "rol": (fila.get("rol_cartera") or "").strip(),
                "cadencia": (fila.get("cadencia_siembra") or "").strip(),
                "ventana": (fila.get("ventana_objetivo") or "").strip(),
                "regla": (fila.get("regla") or "").strip(),
                "destino": (fila.get("destino") or "").strip(),
                "notas": (fila.get("notas") or "").strip(),
            })
    return roles


ORDEN_ROL = ["BASE", "BASE_ENCAJE", "FOCAL", "FOLLAJE", "TOQUE",
             "TOQUE_ENSAYO", "SIN_CLASIFICAR"]

LEE_ROL = {
    "BASE": "siempre debe haber — un hueco es una falla",
    "BASE_ENCAJE": "el rol es ENCAJE; Ammi y Trachelium se sustituyen entre si",
    "FOCAL": "siempre una flor principal; el rol no puede quedar vacio",
    "TOQUE": "rota a proposito, poca cantidad, Inv 2 — el poco volumen es el diseno",
    "FOLLAJE": "el follaje propio desplaza compra de Ruscus — es costo evitado",
    "TOQUE_ENSAYO": "en prueba; si no funciona, se saca la cama",
    "SIN_CLASIFICAR": "Vanessa todavia no le asigno rol — PREGUNTAR antes de juzgarlo",
}


def oferta_registrada():
    """Tallos cosechados por grupo, con corte y semanas del registro."""
    oferta = defaultdict(float)
    semanas = defaultdict(set)
    ultima, primera = {}, {}
    por_semana = defaultdict(lambda: defaultdict(float))
    for fila in _leer_csv("registro_tallos.csv"):
        fecha = (fila.get("Fecha") or "").strip()
        try:
            d = datetime.date.fromisoformat(fecha)
        except ValueError:
            continue
        grupo = (fila.get("Grupo") or "").strip()
        if not grupo:
            continue
        tallos = num((fila.get("Tallos frescos") or "").strip())
        seco = num((fila.get("Tallos secos") or "").strip())
        total = (tallos or 0) + (seco or 0)
        oferta[grupo] += total
        iso = d.isocalendar()[1]
        semanas[grupo].add(iso)
        por_semana[grupo][iso] += total
        primera[grupo] = min(primera.get(grupo, d), d)
        ultima[grupo] = max(ultima.get(grupo, d), d)
    corte = max(ultima.values()) if ultima else None
    return {"tallos": oferta, "semanas": semanas, "primera": primera,
            "ultima": ultima, "por_semana": por_semana, "corte": corte}


def _senales_campo():
    """Lo que el campo ya dijo en prosa, indexado por grupo."""
    idx = defaultdict(lambda: defaultdict(list))

    def grupo_de(nombre, grupos):
        n = norm(nombre)
        return next((g for g in grupos if norm(g) in n), None)

    grupos = sorted({(f.get("Grupo") or "").strip()
                     for f in _leer_csv("registro_tallos.csv")
                     if (f.get("Grupo") or "").strip()}, key=lambda g: -len(g))

    for fila in cargar_cierres():
        g = grupo_de(fila.get("variedad", ""), grupos)
        if g:
            idx[g]["cierres"].append(fila)
    for fila in _leer_opcional("desajuste_demanda.csv"):
        g = grupo_de(fila.get("variedad", ""), grupos)
        if g:
            # Los tipos vienen del barrido de COMENTARIOS: sobra, falta y
            # calidad_venta (despetalado, pudricion, devoluciones). No se
            # normalizan a mano: si aparece uno nuevo, entra igual.
            idx[g][(fila.get("tipo") or "otro").strip()].append(fila)
    for fila in _leer_opcional("picos_cosecha.csv"):
        g = grupo_de(fila.get("variedad", ""), grupos)
        if g:
            idx[g]["picos"].append(fila)
    return idx


def _etiqueta_balance(pct_dem, pct_ofe, dem, ofe):
    """Traduce la brecha a una etiqueta. La etiqueta es evidencia, no orden."""
    if dem and not ofe:
        return "EN RECETA, SIN COSECHA", -100.0
    if ofe and not dem:
        return "COSECHA SIN RECETA", 100.0
    if not dem and not ofe:
        return "SIN DATO", 0.0
    pp = pct_ofe - pct_dem
    if pp <= -5:
        return "FALTA", pp
    if pp >= 5:
        return "SOBRA", pp
    return "en equilibrio", pp


def cmd_cartera(grupo=None):
    """Demanda del catalogo contra cosecha real, grupo por grupo.

    Es la mesa de trabajo de la sesion de cartera: que se queda, que se va,
    de que hay que sembrar mas y de que menos. No decide sola — pone la
    evidencia y marca en que se apoya y en que no.
    """
    cat = demanda_catalogo()
    demanda, en_prod = cat["demanda"], cat["en_productos"]
    pendientes, n_prod = cat["pendientes"], cat["n_productos"]
    ofe = oferta_registrada()
    senales = _senales_campo()
    ciclos = cargar_ciclos()

    if grupo:
        return _cartera_detalle(grupo, demanda, en_prod, ofe, senales, ciclos,
                                n_prod, cat["subtipos"])

    tot_dem = sum(demanda.values()) or 1.0
    tot_ofe = sum(ofe["tallos"].values()) or 1.0
    hoy = datetime.date.today()
    corte = ofe["corte"]

    # TRUNCAMIENTO POR LA IZQUIERDA. El registro de cosecha arranca en una
    # semana concreta, y todo lo que produjo ANTES no esta en el. Un grupo
    # cuyo pico documentado cayo antes de esa semana aparece con una oferta
    # ridicula que no mide a la variedad: mide cuando empezo a llevarse el
    # registro. Larkspur es el caso extremo — pico en la semana 21, registro
    # desde la 22, y 243 tallos anotados de 4.788 plantas.
    inicio = min(ofe["primera"].values()) if ofe["primera"] else None
    sem_inicio = inicio.isocalendar()[1] if inicio else 0
    truncados = {}
    for g, s_g in senales.items():
        pruebas = []
        for f in s_g.get("picos", []):
            try:
                sp = int((f.get("sem_pico") or "").strip())
            except ValueError:
                continue
            if sp < sem_inicio:
                pruebas.append("pico sem %d" % sp)
        for f in s_g.get("cierres", []):
            try:
                sc = int((f.get("semana_cierre") or "").strip())
            except ValueError:
                continue
            if sc < sem_inicio:
                pruebas.append("cerro sem %d por %s" % (sc, f.get("motivo") or "?"))
        if pruebas:
            truncados[g] = pruebas

    print("=" * 78)
    print("CARTERA DE VARIEDADES — que se queda, que se va, de que falta")
    print("=" * 78)
    print()
    if corte:
        atraso = (hoy - corte).days
        print("Registro de cosecha: %s -> %s. Hoy es %s: %d dias sin registrar."
              % (min(ofe["primera"].values()), corte, hoy, atraso))
        if atraso > 7:
            faltan = sorted({(corte + datetime.timedelta(days=i)).isocalendar()[1]
                             for i in range(1, atraso + 1)})
            print("ADVERTENCIA: faltan las semanas ISO %s. Todo lote abierto al"
                  % ", ".join(str(s) for s in faltan))
            print("%s sale SUBESTIMADO, y la columna OFERTA con el." % corte)
            print("Lo que se decida hoy sobre produccion es provisional hasta")
            print("cerrar ese hueco.")
    if truncados:
        print()
        print("ADVERTENCIA 2 — el registro tampoco cubre el principio del ano.")
        print("Arranca en la semana ISO %d, y estos %d grupos tienen picos o"
              % (sem_inicio, len(truncados)))
        print("cierres DOCUMENTADOS antes de esa semana. Su columna OFERTA no")
        print("mide a la variedad: mide desde cuando se lleva el registro.")
        for g in sorted(truncados):
            print("  %-18s %s" % (g[:18], "; ".join(truncados[g][:3])))
        print()
        print("Con las dos advertencias juntas: la tabla es una FOTO DE 12")
        print("SEMANAS (ISO %d a %d), no un veredicto del ano. FALTA y SOBRA se"
              % (sem_inicio, corte.isocalendar()[1] if corte else 0))
        print("leen dentro de esa ventana y de ninguna manera fuera de ella.")
    print()
    print("DEMANDA = canasta NO ponderada: una unidad de cada uno de los %d"
          % n_prod)
    print("productos del catalogo. El volumen real de venta por producto vive")
    print("en 03_Ventas, fuera del alcance. Es un proxy del peso en el")
    print("CATALOGO, no del peso en la CAJA.")
    print()

    filas = []
    for g in set(list(demanda) + list(ofe["tallos"])):
        dem = demanda.get(g, 0.0)
        of = ofe["tallos"].get(g, 0.0)
        pct_dem = 100 * dem / tot_dem
        pct_ofe = 100 * of / tot_ofe
        etiqueta, pp = _etiqueta_balance(pct_dem, pct_ofe, dem, of)
        # Un grupo que solo aparece como parte de un ingrediente sustituible
        # NO esta fuera del catalogo: esta dentro, sin cantidad propia.
        if etiqueta == "COSECHA SIN RECETA" and any(
                g in clave.split(" o ") for clave in cat["sustituciones"]):
            etiqueta = "SOLO SUSTITUIBLE"
        filas.append({"grupo": g, "dem": dem, "prods": len(en_prod.get(g, ())),
                      "pct_dem": pct_dem, "ofe": of, "pct_ofe": pct_ofe,
                      "sem": len(ofe["semanas"].get(g, ())),
                      "ultima": ofe["ultima"].get(g),
                      "etiqueta": etiqueta, "pp": pp})
    roles = cargar_roles()
    for f in filas:
        r = roles.get(f["grupo"], {})
        f["rol"] = r.get("rol") or "SIN_CLASIFICAR"
        f["area"] = r.get("area") or ""
        # Un TOQUE no se juzga por volumen. Sustituir el veredicto evita el
        # error de categoria de medirlo contra la demanda del catalogo.
        if f["rol"].startswith("TOQUE"):
            if f["etiqueta"] in ("FALTA", "SOBRA", "COSECHA SIN RECETA",
                                 "EN RECETA, SIN COSECHA"):
                f["etiqueta"] = "rotativo (volumen no aplica)"
    filas.sort(key=lambda f: (ORDEN_ROL.index(f["rol"]) if f["rol"] in ORDEN_ROL
                              else 99, -f["pct_dem"], -f["pct_ofe"]))

    rol_actual = None
    for f in filas:
        if f["rol"] != rol_actual:
            rol_actual = f["rol"]
            print()
            print("%s — %s" % (rol_actual, LEE_ROL.get(rol_actual, "")))
            print("%-18s %6s %5s %6s %8s %6s %4s %-11s %s"
                  % ("GRUPO", "PIDE", "PROD", "%DEM", "COSECHO", "%OFE", "SEM",
                     "ULTIMA", "BALANCE"))
            print("-" * 78)
        print("%-18s %6s %5s %5.1f%% %8.0f %5.1f%% %4d %-11s %s"
              % (f["grupo"][:18],
                 "%.0f" % f["dem"] if f["dem"] else "—",
                 "%d/%d" % (f["prods"], n_prod) if f["prods"] else "—",
                 f["pct_dem"], f["ofe"], f["pct_ofe"], f["sem"],
                 f["ultima"] or "—",
                 (f["etiqueta"] + (" <TRUNCADO" if f["grupo"] in truncados
                                   else ""))))
    print()

    for titulo, cond in (
            ("FALTA — el catalogo lo pide mas de lo que el campo lo da",
             lambda f: f["etiqueta"] in ("FALTA", "EN RECETA, SIN COSECHA")),
            ("SOBRA — el campo lo da mas de lo que el catalogo lo pide",
             lambda f: f["etiqueta"] == "SOBRA"),
            ("COSECHA SIN RECETA — produce y ninguna receta lo nombra",
             lambda f: f["etiqueta"] == "COSECHA SIN RECETA"),
            ("SOLO SUSTITUIBLE — en el catalogo, pero sin cantidad propia",
             lambda f: f["etiqueta"] == "SOLO SUSTITUIBLE")):
        elegidas = [f for f in filas if cond(f)]
        if not elegidas:
            continue
        print(titulo)
        for f in sorted(elegidas, key=lambda x: x["pp"]):
            extra = []
            s = senales.get(f["grupo"], {})
            if s.get("sobra"):
                extra.append("campo dijo SOBRA sem %s"
                             % "/".join(x.get("semana", "?") for x in s["sobra"][:3]))
            if s.get("falta"):
                extra.append("campo dijo FALTA sem %s"
                             % "/".join(x.get("semana", "?") for x in s["falta"][:3]))
            if s.get("calidad_venta"):
                extra.append("PROBLEMA DE VENTA/CALIDAD (%d)"
                             % len(s["calidad_venta"]))
            motivos = {x.get("motivo") for x in s.get("cierres", ()) if x.get("motivo")}
            if motivos:
                extra.append("cierres: %s" % ", ".join(sorted(motivos)))
            if f["ultima"] and corte and (corte - f["ultima"]).days > 21:
                extra.append("sin cosecha desde %s" % f["ultima"])
            if f["grupo"] in truncados:
                extra.append("OJO: %s — produjo antes del registro"
                             % truncados[f["grupo"]][0])
            print("  %-18s %+6.1f pp   %s"
                  % (f["grupo"][:18], f["pp"] if abs(f["pp"]) < 100 else 0,
                     " | ".join(extra) or "sin senales de campo registradas"))
        print()

    # Un grupo con rol asignado y CERO tallos registrados no es un grupo que no
    # produjo: es un grupo que nadie anoto. Los toques son justo los que se
    # escapan, porque no estan en el desplegable de la hoja LISTAS.
    grupos_lista = {norm(f["GRUPO"]) for f in _leer_csv("listas_desplegables.csv")
                    if (f.get("GRUPO") or "").strip()}
    invisibles = [(g, r) for g, r in sorted(roles.items())
                  if not ofe["tallos"].get(g)]
    if invisibles:
        print("CON ROL ASIGNADO Y SIN UN SOLO TALLO REGISTRADO (%d)"
              % len(invisibles))
        print("No es que no hayan producido: es que nadie los anoto. Y el motivo")
        print("suele ser el desplegable — un grupo que no esta en la hoja LISTAS")
        print("no se puede elegir, asi que no se registra:")
        for g, r in invisibles:
            en_lista = "en LISTAS" if norm(g) in grupos_lista else "NO esta en LISTAS"
            print("  %-20s %-14s %s" % (g[:20], r["rol"], en_lista))
        print()

    if cat["subtipos"]:
        print("DEMANDA POR SUBTIPO — donde el grupo es un paraguas")
        print("La receta pide el SUBTIPO y el cultivar es el que este en")
        print("cosecha esa semana (Vanessa 2026-09-10). Cada subtipo tiene su")
        print("propia densidad y sus propios tallos por planta, asi que la")
        print("siembra se decide por subtipo, no por grupo:")
        for (g, st), cant in sorted(cat["subtipos"].items(), key=lambda kv: -kv[1]):
            print("  %-12s %-10s %5.0f tallos por canasta" % (g, st, cant))
        print()

    if cat["sustituciones"]:
        print("INGREDIENTES SUSTITUIBLES — la receta no se compromete")
        print("No se suman a ningun grupo: sumarlos a los dos inflaria los dos.")
        for clave, d in sorted(cat["sustituciones"].items(), key=lambda kv: -kv[1]["cant"]):
            print("  %-24s %5.0f tallos en %d producto(s)"
                  % (clave, d["cant"], len(d["prods"])))
        print()

    con_calidad = [f for f in filas if senales.get(f["grupo"], {}).get("calidad_venta")]
    if con_calidad:
        print("SENALES DE CALIDAD O DE VENTA — candidatos a salir aunque el")
        print("balance de volumen se vea bien. Un tallo que se despetala en el")
        print("carrito o que vuelve devuelto no es produccion, es costo.")
        for f in con_calidad:
            for x in senales[f["grupo"]]["calidad_venta"]:
                print("  %-18s %-9s \"%s\""
                      % (f["grupo"][:18], x.get("bloque") or "?",
                         (x.get("evidencia_literal") or "")[:60]))
        print()

    grupos_lista = {norm(f["GRUPO"]) for f in _leer_csv("listas_desplegables.csv")
                    if (f.get("GRUPO") or "").strip()}
    huerfanos = [f["grupo"] for f in filas
                 if f["ofe"] and norm(f["grupo"]) not in grupos_lista]
    if huerfanos:
        print("GRUPOS QUE COSECHAN Y NO ESTAN EN EL DESPLEGABLE (%d)"
              % len(huerfanos))
        print("Diana los escribio a mano en REGISTRO. Mientras no esten en la")
        print("hoja LISTAS no hay desplegable que los proteja del error de")
        print("tipeo, y cada variante nueva se vuelve un grupo distinto:")
        for g in huerfanos:
            print("  %-20s %6.0f tallos" % (g, next(f["ofe"] for f in filas if f["grupo"] == g)))
        print()

    if pendientes:
        print("INGREDIENTES DE RECETA SIN VINCULO A LA PALETA (%d)"
              % len(pendientes))
        print("Estos tallos NO estan contados en la columna PIDE. La receta los")
        print("nombra, el campo los cosecha, y paleta_color.csv no los tiene:")
        print("por eso el grupo aparece como COSECHA SIN RECETA. Se resuelve")
        print("agregando la fila a paleta_color.csv — con color CONFIRMADO en")
        print("campo, no deducido del nombre (regla 8).")
        agrup = defaultdict(lambda: {"cant": 0.0, "prods": set(), "cand": None})
        for p in pendientes:
            k = p["ingrediente"]
            agrup[k]["cant"] += p["cantidad"]
            agrup[k]["prods"].add(p["producto"])
            agrup[k]["cand"] = p["candidato"]
        for ing, d in sorted(agrup.items(), key=lambda kv: -kv[1]["cant"]):
            print("  %-28s %5.0f tallos en %d producto(s)  candidato: %s"
                  % (ing[:28], d["cant"], len(d["prods"]),
                     d["cand"] or "NINGUNO — preguntar"))
        print()

    print("LO QUE ESTE COMANDO NO PUEDE DECIDIR")
    print("  margen         costos_productos.csv esta vacio. Sin costo no hay")
    print("                 margen por m2 por semana, que es el eje que")
    print("                 ordena de verdad la cartera. FALTA y SOBRA de")
    print("                 arriba son de VOLUMEN, no de plata.")
    print("  calidad        calidad_tallo.csv esta vacio: no se separa")
    print("                 'produjo' de 'produjo vendible'.")
    print("  ocupacion      falta area por lote para pasar de tallos a")
    print("                 tallos por m2 por semana de cama ocupada.")
    print("  venta real     la canasta no esta ponderada por volumen de venta.")
    print()
    print("Detalle de un grupo:  python3 motor/cerebro.py cartera Gomphrena")
    return 0


def _cartera_detalle(grupo, demanda, en_prod, ofe, senales, ciclos, n_prod,
                     subtipos=None):
    """Ficha de un grupo para decidir sobre el: se queda, se va, mas o menos."""
    clave = norm(grupo)
    reales = [g for g in set(list(demanda) + list(ofe["tallos"]))
              if clave in norm(g) or norm(g) in clave]
    if not reales:
        print("No hay ni demanda ni cosecha registrada para %r." % grupo)
        print("Grupos con dato: %s"
              % ", ".join(sorted(set(list(demanda) + list(ofe["tallos"])))))
        return 1

    for g in sorted(reales):
        print("=" * 78)
        print("CARTERA — %s" % g.upper())
        print("=" * 78)
        dem = demanda.get(g, 0.0)
        of = ofe["tallos"].get(g, 0.0)
        print()
        print("EN EL CATALOGO")
        if dem:
            print("  pide %.0f tallos por canasta, en %d de %d productos:"
                  % (dem, len(en_prod.get(g, ())), n_prod))
            for p in sorted(en_prod.get(g, ())):
                print("    - %s" % p)
        else:
            print("  ninguna receta lo nombra con un vinculo resuelto a la")
            print("  paleta. Correr 'cartera' sin argumento para ver si es un")
            print("  ingrediente sin vinculo o una ausencia real.")
            for (sg, st), cant in sorted((subtipos or {}).items()):
                if sg == g:
                    print("    subtipo %s: %.0f tallos" % (st, cant))
        print()
        print("EN EL CAMPO")
        if of:
            semanas = sorted(ofe["por_semana"][g])
            print("  %.0f tallos entre %s y %s, en %d semanas ISO"
                  % (of, ofe["primera"][g], ofe["ultima"][g], len(semanas)))
            pico = max(ofe["por_semana"][g].items(), key=lambda kv: kv[1])
            print("  pico registrado: semana %d con %.0f tallos" % pico)
            ancho = max(ofe["por_semana"][g].values()) or 1
            for s in semanas:
                v = ofe["por_semana"][g][s]
                print("    sem %2d %-30s %6.0f"
                      % (s, "#" * int(30 * v / ancho), v))
        else:
            print("  sin un solo tallo en registro_tallos.csv")
        print()

        rol = cargar_roles().get(g)
        if rol:
            print("ROL EN LA CARTERA — %s" % rol["rol"])
            for f in rol["filas"]:
                etiqueta = f["subtipo"] or "(todo el grupo)"
                print("  %-18s %s" % (etiqueta, f["regla"] or "sin regla escrita"))
                if f["cadencia"] or f["ventana"]:
                    print("  %-18s cadencia: %s | ventana: %s"
                          % ("", f["cadencia"] or "SIN_DATO", f["ventana"] or "SIN_DATO"))
            if rol["alterna_con"]:
                print("  alterna con: %s" % rol["alterna_con"])
            if rol["no_solapar"]:
                print("  OJO: no solapar dos camas en cosecha")
            print()

        c = next((f for k, f in ciclos.items() if k and (k in norm(g) or norm(g) in k)), None)
        print("CICLO (ciclos_variedad.csv — referencia agronomica interna)")
        if c:
            print("  germinacion %s sem | a campo %s-%s sem | ventana %s-%s sem"
                  % (c["sem_germinacion"] or "SIN_DATO",
                     c["sem_a_campo_min"] or "SIN_DATO", c["sem_a_campo_max"] or "?",
                     c["ventana_min"] or "SIN_DATO", c["ventana_max"] or "?"))
            print("  distancia %s cm | tallos/planta %s | %s"
                  % (c["distancia_cm"] or "SIN_DATO",
                     c["tallos_planta"] or "SIN_DATO",
                     "PERENNE" if c["perenne"] else "anual"))
            if c["notas"]:
                print("  nota: %s" % c["notas"])
        else:
            print("  SIN_DATO — no hay fila para este grupo")
        print()

        s = senales.get(g, {})
        print("LO QUE EL CAMPO YA DIJO")
        vacio = True
        for etiqueta, filas in (("SOBRO", s.get("sobra", [])),
                                ("FALTO", s.get("falta", [])),
                                ("CALIDAD/VENTA", s.get("calidad_venta", []))):
            for f in filas:
                vacio = False
                print("  %s sem %s (%s): \"%s\""
                      % (etiqueta, f.get("semana") or "?", f.get("bloque") or "?",
                         (f.get("evidencia_literal") or "")[:80]))
        for f in s.get("picos", []):
            vacio = False
            print("  PICO sem %s, inicio sem %s (%s)"
                  % (f.get("sem_pico") or "?", f.get("sem_inicio") or "?",
                     f.get("bloque") or "?"))
        for f in s.get("cierres", []):
            vacio = False
            print("  CIERRE sem %s por %s (%s): \"%s\""
                  % (f.get("semana_cierre") or "?", f.get("motivo") or "?",
                     f.get("bloque") or "?",
                     (f.get("evidencia_literal") or "")[:70]))
        if vacio:
            print("  nada registrado en cierres_lote, picos_cosecha ni")
            print("  desajuste_demanda")
        print()
    return 0


def cmd_matriz():
    filas = cobertura_matriz()
    print("\n" + "=" * 78)
    print("LA MATRIZ DE DECISION — cuanto se puede decidir hoy con datos reales")
    print("=" * 78)
    print("\nCada variable entra en la decision de QUE sembrar, CUANTA, DONDE, CUANDO")
    print("y CON QUE MANEJO. Una variable en SIN_DATO no se estima: bloquea.\n")

    listas = 0
    for f in filas:
        pct = (f["cub"] / f["tot"]) if f["tot"] else 0.0
        if pct >= 0.999:
            estado, listas = "LISTA  ", listas + 1
        elif pct > 0:
            estado = "PARCIAL"
        else:
            estado = "SIN_DATO"
        print("%2d. %-38s %s %s %5.0f%%  (%s/%s %s)" % (
            f["n"], f["nombre"][:38], barra(pct, 14), estado, pct * 100,
            f["cub"], f["tot"], f["unidad"]))
        print("     desbloquea: %s" % f["desbloquea"])
        if f["nota"]:
            print("     nota: %s" % f["nota"])
        print("")

    print("-" * 78)
    print("%d de %d variables listas para decidir." % (listas, len(filas)))
    print("\n  Las tres piernas del objetivo:")
    print("    punto de venta  -> variable 1")
    print("    bouquet         -> variables 1 y 2")
    print("    EL MEDIO        -> variables 3 a 11  <- aqui esta el trabajo")
    print("\n  Detalle y como llenar cada hueco: 08-roadmap/02-informacion-que-falta.md")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd = argv[1]
    if cmd == "matriz":
        cmd_matriz()
    elif cmd == "productos":
        cmd_productos()
    elif cmd == "auditar":
        cmd_auditar()
    elif cmd == "valor":
        cmd_valor()
    elif cmd == "ciclos":
        cmd_ciclos()
    elif cmd == "cartera":
        cmd_cartera(argv[2] if len(argv) > 2 else None)
    elif cmd == "rendimiento":
        cmd_rendimiento(argv[2] if len(argv) > 2 else None)
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
