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
    python3 motor/cerebro.py rendimiento [grupo]
    python3 motor/cerebro.py m2 [grupo]
    python3 motor/cerebro.py prorratear [grupo]
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

# Geometria de cama. La malla de siembra es de 0,15 m en las DOS direcciones
# (Vanessa 2026-08-13: "cada hueco tiene cero quince en esa malla"), asi que:
#
#     largo de la cama = huecos x 0,15      ancho = lineas x 0,15
#     sitios por m2    = 1 / 0,15^2 = 44,44
#
# Verificado contra el campo: Inv 4A son 112 huecos x 8 lineas = 896 sitios,
# que es el numero que Vanessa escribio en el comentario de esa cama.
#
# De ahi sale la densidad real, que NO es la de la malla sino la de la
# DISTANCIA DE SIEMBRA de cada cultivo:
#
#     plantas por m2 = 1 / (0,15 x distancia_de_siembra_en_metros)
#
# Una sola formula cubre los tres casos de la finca sin excepciones:
#   15 cm  -> 1 planta por hueco        -> 44,44 pl/m2
#    7,5 cm-> 2 plantas por hueco       -> 88,89 pl/m2
#   30 cm  -> 1 planta cada dos huecos  -> 22,22 pl/m2
MALLA_M = 0.15

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


def _leer_semanas_siembra():
    """Semana ISO de trasplante por fila de campo_siembras.csv, con el ano
    inferido por secuencia.

    Vanessa 2026-08-14: "Fecha a siembra a campo esta vacio porque deje de
    usarla, ahora trabajo solo con las semanas... la columna que sigue es la
    semana que se trasplanto... eso lo hago porque a veces puede pasar que en
    esa semana se sembro en dos dias distintos, y proyectamos todo por
    semana. Ese dato si esta en todo." Confirmado: 294 de 302 filas la tienen
    (97%), contra 37% de 'Fecha siembra campo'.

    Es la columna "Semana" que aparece justo despues de "Fecha siembra
    campo". El archivo tiene DOS columnas llamadas "Semana" (la otra es la
    semana de INICIO DE COSECHA, mas adelante) y csv.DictReader colapsa
    encabezados duplicados quedandose solo con la ultima -- asi que
    _leer_csv() nunca pudo ver esta columna. Por eso se lee aparte, por
    POSICION (columna 7), no por nombre.

    El archivo no trae el ano, solo el numero de semana ISO (1-52), y las
    302 filas son un log CRONOLOGICO que arranca en la semana 31 de 2025
    (confirmado cruzando contra la fecha exacta de esa misma fila, de las
    pocas que todavia la traen) y llega hasta 2026. El ano se infiere por
    SECUENCIA: una caida grande en el numero de semana (mas de
    UMBRAL_CRUCE_ANIO) es el cruce de diciembre a enero, no un error de
    tipeo. Un salto chico (1-2 semanas) es jitter normal del dictado y no
    dispara cambio de ano -- se observaron 9 de esos en las filas que se
    pueden verificar contra fecha exacta, ninguno mayor a 1 semana.

    Devuelve una lista alineada 1 a 1 con _leer_csv("campo_siembras.csv"):
    [(semana:int|None, anio:int|None), ...]
    """
    ANIO_INICIAL = 2025
    UMBRAL_CRUCE_ANIO = 26
    ruta = os.path.join(DATOS, "campo_siembras.csv")
    with open(ruta, newline="", encoding="utf-8") as fh:
        filas = list(csv.reader(fh))[1:]
    resultado = []
    anio = ANIO_INICIAL
    anterior = None
    for r in filas:
        txt = (r[7] if len(r) > 7 else "").strip()
        if not txt.isdigit():
            resultado.append((None, None))
            continue
        semana = int(txt)
        if anterior is not None and (anterior - semana) > UMBRAL_CRUCE_ANIO:
            anio += 1
        anterior = semana
        resultado.append((semana, anio))
    return resultado


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
        # Una variedad retirada del cultivo sigue en la paleta como memoria
        # historica, pero NO es una opcion de color disponible.
        reg["retirada"] = reg["notas"].startswith("RETIRADA")
        for clave in (reg["nombre_completo"], "%s %s" % (reg["grupo"], reg["variedad"]), reg["variedad"]):
            por_nombre.setdefault(norm(clave), reg)
        if not reg["retirada"]:
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
            "perenne": (fila.get("perenne") or "").strip().lower() == "si",
            "fuente": fila["fuente"].strip(),
            "notas": fila["notas"].strip(),
        }
    return ciclos


def cargar_subtipos():
    """Cultivar -> subtipo agronomico, cuando el grupo es un paraguas.

    Celosia es el caso: el REGISTRO escribe grupo "Celosia", pero cristata va
    a 7,5 cm con 1 tallo/planta y plumosa a 15 cm con 4. Sin resolver el
    subtipo, el area de la cama sale con el doble o la mitad del error.
    Vive en CSV y no en el codigo porque es dato de campo, no una regla.
    """
    ruta = os.path.join(DATOS, "subtipos.csv")
    if not os.path.exists(ruta):
        return []
    with open(ruta, newline="", encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))
    return [f for f in filas
            if (f.get("subtipo") or "").strip()
            and f["subtipo"].strip() != "SIN_CONFIRMAR"]


def parametros_de(grupo, variedad, ciclos, subtipos=()):
    """Fila de ciclos_variedad.csv que le corresponde a un lote del REGISTRO.

    Devuelve (fila, nivel). nivel dice de donde salio el match, para que
    quien lea la tabla sepa cuanto creerle:

      SUBTIPO  el cultivar esta en subtipos.csv (Shimmer -> Celosia plumosa)
      EXACTO   el nombre del grupo de ciclos aparece en "grupo + variedad"
      GRUPO    varias filas del grupo aplican y COINCIDEN en el parametro
      -        ninguna, o varias que se contradicen -> SIN_DATO honesto

    El nivel GRUPO es el que salva a Boca de Dragon: el registro escribe
    "Monaco Orange", que no esta en ciclos_variedad, pero TODAS las filas de
    boca de dragon dicen 7,5 cm — asi que el dato no depende del cultivar.
    Si se contradijeran, no se elige una: se reporta SIN_DATO.
    """
    alias = alias_grupo(grupo)
    clave = norm("%s %s" % (grupo, variedad))
    claves = {clave} | {norm("%s %s" % (a, variedad)) for a in alias}

    # 1. subtipo declarado para ese cultivar
    v = norm(variedad)
    for s in subtipos:
        if not any(a in norm(s["grupo"]) or norm(s["grupo"]) in a for a in alias):
            continue
        cu = norm(s["cultivar"])
        if cu and cu in v:
            fila = ciclos.get(norm(s["subtipo"]))
            if fila:
                return fila, "SUBTIPO"

    # 2. match exacto por nombre de grupo de ciclos_variedad
    mejor, largo = None, 0
    for k, fila in ciclos.items():
        if not k:
            continue
        if any(k in c for c in claves) and len(k) > largo:
            mejor, largo = fila, len(k)
    if mejor:
        return mejor, "EXACTO"

    # 3. consenso entre todas las filas del grupo
    candidatas = [f for k, f in ciclos.items()
                  if k and any(a in k or k in a for a in alias)]
    if candidatas:
        return candidatas, "GRUPO"
    return None, "-"


def valor_parametro(res, nivel, campo):
    """Extrae un parametro de lo que devolvio parametros_de().

    En nivel GRUPO hay varias filas: solo se devuelve el valor si TODAS las
    que lo tienen lleno coinciden. Un promedio entre 7,5 y 15 seria un numero
    que no existe en ninguna cama.
    """
    if not res:
        return None, "-"
    if nivel != "GRUPO":
        return res.get(campo), nivel
    valores = {f.get(campo) for f in res if f.get(campo)}
    if len(valores) == 1:
        return valores.pop(), "GRUPO"
    return None, "AMBIGUO"


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


class _CategoriaVenta(object):
    """Que categorias de formulas_productos_bouquets.csv son producto de venta.

    El archivo mezcla el catalogo comercial con un bloque de productos
    fitosanitarios que tiene otro esquema. Se separan por categoria.
    """

    PREFIJOS = ("bouquet", "maxi bouquet", "centro de mesa", "paquete",
                "yugo", "arreglo", "ramo")

    def match(self, categoria):
        return norm(categoria).startswith(self.PREFIJOS)


CATEGORIA_VENTA = _CategoriaVenta()


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
            # Un producto de venta se reconoce por su CATEGORIA, no por como
            # este redactada la cabecera.
            #
            # La version anterior exigia la frase "flores DCB" en la columna
            # Ingrediente. Funcionaba hasta que se cargaron Dream Land y My
            # Love con una cabecera descriptiva ("BASE DE TALLOS — ..."), y
            # el motor los TIRO A LA BASURA etiquetados como fitosanitarios.
            # El catalogo decia 30 productos y el motor veia 28, sin avisar.
            #
            # Es lista blanca a proposito: una categoria nueva se reporta como
            # desconocida en vez de desaparecer en silencio.
            if not CATEGORIA_VENTA.match(categoria):
                descartadas.append({
                    "fila": prod,
                    "motivo": "categoria '%s' no es de venta" % (categoria or "(vacia)"),
                })
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

    total_libre = total_dcb = 0.0
    incoherentes = []
    for p in productos:
        a = analizar_producto(p, por_nombre, por_grupo)
        total_libre += a["tallos_color_libre"]
        total_dcb += a["tallos_dcb"]
        alertas = len(a["diagnostico"]) + sum(
            1 for e in a["estructura"] if e["estado"] in ("bajo", "alto"))
        for d in a["diagnostico"]:
            if "pero ningun ingrediente" in d:
                incoherentes.append((p["producto"], d))
        print("%-38s %6.0f %6.0f%% %7.0f%% %s"
              % (p["producto"][:38], a["total_tallos"], 100 * a["pct_color_libre"],
                 100 * a["neutro_pct"], "!" * alertas))

    # Esto salia solo al abrir el producto uno por uno, asi que en la tabla se
    # veia como un "!" mas entre otros. Un producto que no contiene lo que su
    # nombre promete es un problema de otra categoria: el cliente lo pide por
    # el nombre. Va aparte y va primero.
    if incoherentes:
        print("\n" + "-" * 78)
        print("EL NOMBRE NO CORRESPONDE AL CONTENIDO (%d)" % len(incoherentes))
        for nombre, d in incoherentes:
            print("  ! %-36s %s" % (nombre[:36], d))
        print("  Revisar la receta en formulas_productos_bouquets.csv antes de")
        print("  usarla para planificar: el motor va a sembrar lo que dice la")
        print("  receta, no lo que dice el nombre.")

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


def _fecha_siembra_estim(fila, semana_info):
    """Fecha de siembra estimada para una fila de campo_siembras.csv.

    Fuente principal: el LUNES de la semana ISO de trasplante (columna
    "Semana" junto a "Fecha siembra campo" -- ver _leer_semanas_siembra).
    Vanessa 2026-08-14 la confirmo como la que usa de verdad hoy: "deje de
    usar la fecha exacta, ahora trabajo solo con las semanas... a veces se
    sembro en dos dias distintos [de la misma semana] y proyectamos todo por
    semana." Aproxima el dia real por hasta 6 dias, pero es 97% de las filas
    contra 37% de la fecha exacta -- que se usa solo como respaldo cuando la
    semana falta, para las pocas filas viejas que todavia la traen.

    semana_info es la tupla (semana, anio) de esa misma fila, ya alineada por
    posicion -- ver _leer_semanas_siembra().
    """
    semana, anio = semana_info
    if semana and anio:
        try:
            return datetime.date.fromisocalendar(anio, semana, 1)
        except ValueError:
            pass
    fecha_txt = (fila.get("Fecha siembra campo") or "").strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_txt):
        return datetime.date.fromisoformat(fecha_txt)
    return None


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
    semanas_siembra = _leer_semanas_siembra()
    n = len(filas)
    llenas = lambda k: sum(1 for f in filas if (f.get(k) or "").strip())

    print("=" * 74)
    print("CICLOS OBSERVADOS EN CAMPO — %d siembras registradas" % n)
    print("=" * 74)
    print("\nCALIDAD DEL DATO (leer esto antes de creer cualquier promedio)")
    for k in ("Fecha siembra campo", "Inicio cosecha", "Fin de cosecha"):
        c = llenas(k)
        print("  %-22s %3d llenas  %5.0f%%" % (k, c, 100.0 * c / n if n else 0))
    con_semana = sum(1 for sem, anio in semanas_siembra if sem and anio)
    print("  %-22s %3d llenas  %5.0f%%  <- fuente real hoy (Vanessa 2026-08-14:"
          % ("Semana de siembra", con_semana, 100.0 * con_semana / n if n else 0))
    print("  %-22s %25s     \"deje de usar la fecha exacta, ahora trabajo solo" % ("", ""))
    print("  %-22s %25s     con las semanas\")" % ("", ""))

    tri = sum(1 for f in filas
              if (f.get("Fecha siembra campo") or "").strip()
              and (f.get("Inicio cosecha") or "").strip()
              and (f.get("Fin de cosecha") or "").strip())
    print("  filas con las TRES fechas %3d           <- la VENTANA solo sale de aqui" % tri)

    # El ciclo (trasplante -> inicio de cosecha) ya no depende de la fecha
    # exacta: se calcula con la fecha ESTIMADA de la semana de trasplante
    # (lunes de esa semana ISO), que es la fuente que Vanessa usa de verdad.
    # La fecha exacta, cuando esta, sigue sirviendo de respaldo.
    obs = []
    for f, semana_info in zip(filas, semanas_siembra):
        fecha_est = _fecha_siembra_estim(f, semana_info)
        if not fecha_est:
            continue
        c = ciclo_observado(fecha_est.isoformat(), f.get("Inicio cosecha"))
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


def _fecha_de_semana_relativa(ancla, semana_iso):
    """Fecha de una semana ISO sin año, ubicada en o despues de `ancla`.

    cierres_lote.csv guarda EN QUE SEMANA se cerro una cama (extraida de los
    comentarios de campo), pero sin año. Se ancla a la fecha de siembra de esa
    misma siembra -- que ya tiene año resuelto -- y se toma el primer año
    (el de la siembra, o el siguiente si cruza diciembre) que deja la semana
    de cierre en o despues de la siembra. Se usa el DOMINGO de esa semana (el
    ultimo dia), no el lunes: el cierre es un limite superior, "hasta aca
    produjo", y conviene el extremo mas generoso.
    """
    if not (ancla and semana_iso):
        return None
    for anio in (ancla.year, ancla.year + 1):
        try:
            candidata = datetime.date.fromisocalendar(anio, int(semana_iso), 7)
        except ValueError:
            continue
        if candidata >= ancla:
            return candidata
    return None


def _ventana_estimada(grupo, var_texto, fecha_siembra, ciclos, subtipos,
                       bloque=None, cierres=None):
    """Ventana de cosecha ESTIMADA de UNA siembra puntual.

    Existe para poder responder la pregunta de Vanessa: "¿siempre cruzas con
    la ventana de siembra?" — con esto, cuando el mismo cultivar se sembro dos
    veces en el mismo bloque, se puede saber cual de las dos siembras estaba
    activa en la fecha de un corte, en vez de sumarlas a ciegas.

    El inicio SIEMPRE sale de ciclos_variedad.csv — semanas de siembra a
    campo, contadas desde la fecha real de siembra. Nunca se inventa un
    numero que no este ahi:

      * si la siembra no tiene fecha registrada, no hay ventana -> (None, None)
      * si el ciclo no tiene NINGUN dato de semanas a campo, tampoco -> (None, None)

    El FIN tiene dos fuentes, y la de campo manda sobre la estimada:

      1. Vanessa 2026-08-14: "los fines de cosecha estan en las notas, en los
         comentarios" -- ya extraidos a cierres_lote.csv (semana_cierre). Si
         existe un cierre documentado para este lote, ESE es el fin real, no
         una estimacion por ciclo.
      2. Si no hay cierre documentado, se estima con la ventana de cosecha
         del ciclo (duracion). Si tampoco hay eso, la ventana queda ABIERTA
         hacia adelante (fin=None) — sigue produciendo indefinidamente en vez
         de cerrarse con un numero inventado.
    """
    if not fecha_siembra:
        return None, None
    res, nivel = parametros_de(grupo, var_texto, ciclos, subtipos or ())
    ini_sem, _ = valor_parametro(res, nivel, "sem_a_campo_min")
    fin_sem, _ = valor_parametro(res, nivel, "sem_a_campo_max")
    vmin, _ = valor_parametro(res, nivel, "ventana_min")
    vmax, _ = valor_parametro(res, nivel, "ventana_max")
    ini_sem = ini_sem or fin_sem
    fin_sem = fin_sem or ini_sem
    if not ini_sem:
        return None, None
    ini = fecha_siembra + datetime.timedelta(weeks=float(ini_sem))
    dur = vmax or vmin
    fin = (fecha_siembra + datetime.timedelta(weeks=float(fin_sem) + float(dur))) if dur else None

    if bloque and cierres:
        cie = buscar_cierre(grupo, var_texto, bloque, cierres)
        sem_cierre = num((cie or {}).get("semana_cierre") or "")
        if sem_cierre:
            fin_real = _fecha_de_semana_relativa(fecha_siembra, sem_cierre)
            if fin_real:
                fin = fin_real
    return ini, fin


def _solapa(ini, fin, fecha_min, fecha_max):
    """True si el corte [fecha_min, fecha_max] cae dentro de [ini, fin].

    fin=None es una ventana ABIERTA hacia adelante (ver _ventana_estimada):
    sigue produciendo indefinidamente porque no hay dato para cerrarla, asi
    que solapa con cualquier corte posterior a ini.
    """
    if fecha_max < ini:
        return False
    if fin is not None and fecha_min > fin:
        return False
    return True


def _plantas_del_lote(grupo, variedad, bloque, plantas,
                       fecha_min=None, fecha_max=None, ciclos=None, subtipos=None,
                       cierres=None):
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

    UNA SOLA siembra coincidiendo no tiene ambiguedad. Pero cuando el MISMO
    cultivar (o, en un corte "Mix", cualquier cultivar del bloque) se sembro
    mas de una vez, sumar sus plantas a ciegas es un error real y ya
    documentado: Snapdragon Potomac Appleblossom se sembro en 3B el
    2025-11-20 (2.880 plantas) y otra vez sin fecha (3.014 plantas) — antes
    esta funcion sumaba 5.894 sin importar cual de las dos produjo el corte.

    Con fecha_min/fecha_max/ciclos SI se puede resolver, pero no siempre:
    hace falta que CADA siembra candidata tenga fecha de siembra propia y un
    ciclo con el que estimar su ventana. Si falta cualquiera de esas dos
    cosas para alguna candidata, o si dos candidatas solapan la misma fecha,
    queda AMBIGUO — se sigue sumando (para no perder tallos) pero marcado,
    nunca en silencio.

    Devuelve (plantas, siembras_sin_conteo, nivel_multi):
      nivel_multi es None si hubo 0 o 1 siembra candidata (sin ambiguedad),
      "VENTANA" si hubo varias y se aislo una sola por fecha, o
      "AMBIGUO(n)" si hubo varias y no se pudieron separar.
    """
    alias = alias_grupo(grupo)
    v = norm(variedad)
    generica = v in ("", "mix", "sin variedad")
    candidatos = []
    for (hom, var, blo), entradas in plantas.items():
        if blo not in bloques_de(bloque):
            continue
        if not any(a in var for a in alias):
            continue
        if not generica and not (v in hom or (hom and hom in v) or v in var):
            continue
        for e in entradas:
            candidatos.append({"n": e["n"], "tiene": e["tiene"], "fecha": e["fecha"],
                               "hom": hom, "var": var, "blo": blo})

    con_conteo = [c for c in candidatos if c["tiene"]]
    faltan = sum(1 for c in candidatos if not c["tiene"])
    if not con_conteo:
        return None, faltan, None
    if len(con_conteo) == 1:
        return con_conteo[0]["n"], faltan, None

    # Mas de una siembra coincide. Intentar aislar la que estaba activa.
    if fecha_min and fecha_max and ciclos is not None:
        for c in con_conteo:
            c["ini"], c["fin"] = _ventana_estimada(grupo, c["var"], c["fecha"], ciclos, subtipos,
                                                    bloque=c["blo"], cierres=cierres)
        con_ventana = [c for c in con_conteo if c["ini"]]
        if len(con_ventana) == len(con_conteo):
            solapan = [c for c in con_ventana if _solapa(c["ini"], c["fin"], fecha_min, fecha_max)]
            if len(solapan) == 1:
                return solapan[0]["n"], faltan, "VENTANA"

    total = sum(c["n"] for c in con_conteo)
    return total, faltan, "AMBIGUO(%d siembras)" % len(con_conteo)


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


def construir_lotes(grupo=None):
    """Cruza CAMPO (plantas trasplantadas) con REGISTRO (tallos cosechados).

    Es el puente del que cuelgan 'rendimiento' y 'm2', y esta afuera de los
    dos a proposito: cuando el cruce estaba duplicado, arreglar una grafia de
    bloque en un comando dejaba el otro dando un numero distinto para el
    mismo lote. Es exactamente lo que sigue pasando con 'matriz', que todavia
    tiene su propio cruce y por eso reporta 20% donde este reporta 57%.

    Devuelve (lotes, plantas, corte_registro, sin_variedad, inicio_registro).
    """
    siembras = _leer_csv("campo_siembras.csv")
    cosecha = _leer_csv("registro_tallos.csv")

    # Plantas trasplantadas. Se guarda tambien la columna Variedad de CAMPO
    # porque es la unica que trae el GRUPO: los homologados son "Monaco
    # Orange" u "Opus Fresh", que no dicen a que grupo pertenecen. Sin eso el
    # cruce exigia que el grupo apareciera en el homologado y fallaba en el
    # 90% de los lotes.
    # Cada siembra se guarda como una entrada INDIVIDUAL, no sumada de entrada,
    # y con su propia fecha. Antes se sumaba aqui mismo -- plantas[(hom, var,
    # blo, True)] += n -- y esa suma ya no se podia deshacer mas adelante: dos
    # siembras del mismo cultivar en el mismo bloque, en fechas distintas,
    # quedaban indistinguibles para siempre. Es un caso real y no raro:
    # Snapdragon Potomac Appleblossom se sembro en 3B el 2025-11-20 (2.880
    # plantas) y otra vez sin fecha (3.014 plantas) -- sumadas dan las 5.894
    # plantas que hoy reclama el corte "Mix" de esa cama, sin saber cual de
    # las dos produjo el tallo. _plantas_del_lote() es quien ahora decide,
    # lote por lote, si puede separarlas por fecha o si hay que dejarlo
    # marcado como ambiguo.
    # La fecha de siembra ya casi no se llena (Vanessa 2026-08-14: "deje de
    # usarla, ahora trabajo solo con las semanas"). La fuente principal es la
    # semana ISO de trasplante -- 97% llena contra 37% de la fecha exacta --
    # y de ahi se toma el lunes de esa semana como estimador. Es aproximado
    # (la siembra real cae en algun dia de esa semana, a veces en dos dias
    # distintos segun ella misma explica) pero alcanza sobrado para construir
    # una ventana de varias SEMANAS de ciclo. La fecha exacta, cuando esta,
    # sirve de respaldo para las pocas filas viejas sin semana.
    semanas_siembra = _leer_semanas_siembra()
    plantas = defaultdict(list)
    for s, semana_info in zip(siembras, semanas_siembra):
        hom = norm(s.get("Nombre Homologados") or "")
        var = norm(s.get("Variedad") or "")
        n = num((s.get("Cantidad Trasplantada") or "").strip())
        fecha_siembra = _fecha_siembra_estim(s, semana_info)
        if not (hom or var):
            continue
        # Una siembra SIN cantidad trasplantada se registra igual, marcada.
        # Si no, su cosecha se divide entre las plantas de las otras camas y
        # el tallos/planta sale inflado: en Zinnia 4B hay 4 siembras y solo 1
        # tiene conteo, asi que el resultado salia 4 veces mas alto.
        if not n:
            for blo in bloques_de(s.get("Bloque sembrado") or ""):
                plantas[(hom, var, blo)].append({"n": 0.0, "tiene": False, "fecha": fecha_siembra})
            continue
        for blo in bloques_de(s.get("Bloque sembrado") or ""):
            plantas[(hom, var, blo)].append({"n": n, "tiene": True, "fecha": fecha_siembra})

    # cosecha por (grupo, variedad, bloque)
    lotes = defaultdict(lambda: {"tallos": 0.0, "fechas": [],
                                 "grafias": defaultdict(int)})
    # El corte del REGISTRO se mide sobre todas las filas, no sobre las del
    # filtro: una ventana esta abierta si sigue produciendo hasta donde llega
    # el registro completo. Medido contra el maximo del grupo, un lote que
    # dejo de producir en julio se marcaria ABIERTA solo porque es el ultimo
    # de su grupo, aunque el registro siga tres semanas mas.
    corte_registro = ""
    inicio_registro = ""
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
        inicio_registro = min(inicio_registro or f, f)
        if grupo and norm(grupo) not in norm(g):
            continue
        # La clave usa el bloque NORMALIZADO: "Inv 4C" e "Inv4c" son la misma
        # cama y antes salian como dos lotes, cada uno reclamando el total de
        # plantas de la cama. Eso partia la cosecha en dos y subestimaba el
        # tallos/planta de ambos.
        #
        # La VARIEDAD tambien se normaliza, por la misma razon y con el mismo
        # efecto: "Opus Fresh" y "opus fresh" son la misma planta, y salian
        # como dos lotes de 790 y 38 tallos. Se guarda aparte la grafia mas
        # frecuente para mostrarla — normalizar la clave no debe cambiar como
        # se ve el nombre en la tabla.
        t = num(c.get("Tallos frescos") or "")
        clave_b = "+".join(sorted(bloques_de(b))) or norm_bloque(b)
        clave_v = norm(v)
        d = lotes[(g, clave_v, clave_b)]
        d["tallos"] += t or 0
        d["fechas"].append(f)
        d["grafias"][v] += 1

    # Se reemplaza la clave normalizada por la grafia mas usada en el REGISTRO.
    salida = {}
    for (g, cv, cb), d in lotes.items():
        nombre = max(d["grafias"].items(), key=lambda kv: (kv[1], kv[0]))[0]
        salida[(g, nombre, cb)] = d
    return salida, plantas, corte_registro, sin_variedad, inicio_registro


def ventana_del_lote(fechas):
    """(inicio, fin, dias, fechas_sospechosas) de un lote.

    Hay errores de tipeo de ano en el registro (fechas de 2025 dentro de un
    lote de 2026). Se detectan como puntos alejados de la mediana y se
    REPORTAN, no se corrigen en silencio.
    """
    import datetime as dt
    fs = sorted(fechas)
    ds = [dt.date.fromisoformat(x) for x in fs]
    mediana = ds[len(ds) // 2]
    sanas = [x for x in ds if abs((x - mediana).days) <= 60]
    raras = [x.isoformat() for x in ds if abs((x - mediana).days) > 60]
    a, z = min(sanas), max(sanas)
    return a, z, (z - a).days + 1, raras


def cmd_m2(grupo=None):
    """Tallos por metro cuadrado — el denominador que pidio Vanessa.

    Por que m2 y no tallos/planta:

      * Un perenne no tiene denominador de plantas. Dahlia se propaga por
        division, asi que el conteo deriva; el AREA no. Este comando es el
        unico que puede medir a Dahlia y a Esparrago.
      * El eje del proyecto es margen por m2 por SEMANA de cama ocupada.
        Tallos/planta no se puede convertir a plata sin saber cuanta cama
        costo. Tallos/m2/semana si.
      * Dos variedades con el mismo tallos/planta rinden distinto si una va a
        7,5 cm y la otra a 30. Statice da 8 tallos por planta pero ocupa
        cuatro veces mas cama que un lisianthus.

    El area NO se mide en campo: se deriva de plantas x distancia de siembra.
    Por eso cada fila dice de donde salio la distancia (columna FTE).
    """
    lotes, plantas, corte, sin_variedad, arranque = construir_lotes(grupo)
    if not lotes:
        raise SystemExit("Sin datos de cosecha para '%s'." % (grupo or "el filtro"))

    ciclos = cargar_ciclos()
    subtipos = cargar_subtipos()
    cierres = cargar_cierres()

    print("TALLOS POR METRO CUADRADO DE CAMA OCUPADA")
    print("El registro de cosecha corta el %s." % corte)
    print()
    print("El area no se mide en campo, se DERIVA:")
    print("    plantas/m2 = 1 / (0,15 x distancia de siembra)")
    print("    area_m2    = plantas trasplantadas / plantas por m2")
    print("La malla es de 0,15 m (Vanessa 2026-08-13). La columna FTE dice de")
    print("donde salio la distancia de cada fila.")
    print()
    print("%-13s %-19s %-7s %7s %5s %6s %7s %7s %6s %9s" % (
        "GRUPO", "VARIEDAD", "BLOQUE", "PLANTAS", "DIST", "M2",
        "TALLOS", "T/M2", "SEM", "T/M2/SEM"))
    print("-" * 96)

    filas, sin_dist, notas = [], [], []
    total_m2 = total_tallos = 0.0
    for (g, v, b), d in sorted(lotes.items(), key=lambda kv: (kv[0][0], -kv[1]["tallos"])):
        ini, fin, dias, raras = ventana_del_lote(d["fechas"])
        semanas = dias / 7.0
        pl, sin_conteo, nivel_multi = _plantas_del_lote(g, v, b, plantas, ini, fin, ciclos, subtipos, cierres)
        res, nivel = parametros_de(g, v, ciclos, subtipos)
        dist, fte = valor_parametro(res, nivel, "distancia_cm")
        vmin, _ = valor_parametro(res, nivel, "ventana_min")

        marcas = []
        if d["fechas"] and max(d["fechas"]) == corte:
            marcas.append("ABIERTA")
        # El registro empieza el 2026-05-31, con lotes ya en plena cosecha. Un
        # lote que arranca ahi NO empezo ahi: le falta el tramo anterior.
        if arranque and ini.isoformat() <= arranque:
            marcas.append("ARRANCA EN EL CORTE")
        # Una ventana registrada mas corta que la ventana MINIMA documentada
        # del grupo no es una ventana: es un pedazo de ventana. Y miente en
        # las dos direcciones a la vez, que es lo peligroso — el total sale
        # corto y el ritmo sale largo, porque el pedazo registrado suele ser
        # el pico.
        fragmento = bool(vmin) and semanas < float(vmin)
        if fragmento:
            marcas.append("FRAGMENTO %.1f de %g sem" % (semanas, float(vmin)))
        if pl and sin_conteo:
            marcas.append("DENOM INCOMPLETO")
        if nivel_multi == "VENTANA":
            marcas.append("multi-siembra: resuelta por fecha")
        elif nivel_multi:
            marcas.append(nivel_multi)
        cie = buscar_cierre(g, v, b, cierres)
        motivo = (cie or {}).get("motivo", "")
        if motivo in CIERRE_AJENO:
            marcas.append("CIERRE AJENO: " + motivo)
        elif motivo == CIERRE_TARDIO:
            marcas.append("PASADO DE PUNTO")
        if raras:
            marcas.append("fechas raras")

        if not (pl and dist):
            falta = []
            if not pl:
                falta.append("plantas")
            if not dist:
                falta.append("distancia (%s)" % ("ambigua" if fte == "AMBIGUO" else "sin dato"))
            sin_dist.append((g, v, b, d["tallos"], ", ".join(falta)))
            continue

        dens = 1.0 / (MALLA_M * (dist / 100.0))
        area = pl / dens
        tm2 = d["tallos"] / area
        tm2s = tm2 / semanas if semanas else None
        total_m2 += area
        total_tallos += d["tallos"]

        # El ritmo de un fragmento no se imprime. Es la unica columna de todo
        # el motor que se puede leer al reves de la realidad, y ya paso: en la
        # primera corrida Amaranto Emerald Tails salio primero del bloque 3A
        # con 48 t/m2/sem — que eran 380 tallos en DOS DIAS de pico.
        celda_ritmo = "        -" if fragmento else "%9.2f" % (tm2s or 0)
        print("%-13s %-19s %-7s %7.0f %5s %6.1f %7.0f %7.1f %6.1f %s %s %s" % (
            g[:13], v[:19], b[:7], pl, ("%g" % dist), area, d["tallos"],
            tm2, semanas, celda_ritmo, fte[:3],
            " ".join("[%s]" % m for m in marcas)))
        filas.append((g, v, b, area, d["tallos"], tm2, tm2s, semanas, marcas,
                      fte, fragmento))

    if total_m2:
        print("-" * 96)
        print("%-13s %-19s %-7s %7s %5s %6.1f %7.0f %7.1f" % (
            "TOTAL", "%d lotes medidos" % len(filas), "", "", "", total_m2,
            total_tallos, total_tallos / total_m2))

    print()
    print("FTE = de donde salio la distancia de siembra:")
    print("  EXA  ciclos_variedad.csv nombra ese cultivo exacto")
    print("  SUB  el cultivar se resolvio por subtipos.csv (Shimmer -> plumosa)")
    print("  GRU  el cultivar no esta, pero TODAS las filas del grupo coinciden")
    print("       en la distancia — asi que el dato no depende del cultivar")

    if sin_dist:
        sin_dist.sort(key=lambda x: -x[3])
        perdidos = sum(x[3] for x in sin_dist)
        print()
        print("%d lote(s) SIN TALLOS/M2 — %.0f tallos, el %.0f%% de lo cosechado"
              % (len(sin_dist), perdidos, 100 * perdidos / (perdidos + total_tallos)))
        print("Esto NO es un cero: es que falta el denominador. Que falta en cada uno:")
        for g, v, b, t, falta in sin_dist[:20]:
            print("  %-13s %-19s %-7s %6.0f tallos   falta %s" % (g[:13], v[:19], b[:7], t, falta))
        if len(sin_dist) > 20:
            print("  ... y %d mas" % (len(sin_dist) - 20))

    # Comparacion dentro del mismo bloque: misma agua, misma luz, mismo suelo.
    por_b = defaultdict(list)
    excluidos = 0
    for g, v, b, area, t, tm2, tm2s, sem, marcas, fte, frag in filas:
        # Un fragmento no entra al ranking. Si entra, gana — porque su ritmo
        # esta medido sobre el pico y no sobre la ventana.
        if frag:
            excluidos += 1
            continue
        if tm2s:
            por_b[b].append((g, v, tm2, tm2s, sem, marcas))
    hay = False
    for b, l in sorted(por_b.items()):
        if len(l) < 2:
            continue
        if not hay:
            print("\nQUIEN RINDE MAS POR CAMA — dentro del mismo bloque")
            print("(mismo riego, misma luz, mismo suelo: aqui la comparacion es limpia)")
            if excluidos:
                print("%d lote(s) quedaron fuera por ventana FRAGMENTO — su ritmo esta"
                      % excluidos)
                print("medido sobre un pedazo, casi siempre el pico, asi que ganarian")
                print("el ranking sin haber rendido mas.")
            hay = True
        l.sort(key=lambda x: -x[3])
        print("\n  Bloque %s — ordenado por tallos/m2/semana:" % b)
        for g, v, tm2, tm2s, sem, marcas in l:
            print("    %-13s %-19s %6.2f t/m2/sem   (%6.1f t/m2 en %.1f sem)%s"
                  % (g[:13], v[:19], tm2s, tm2, sem,
                     "  " + " ".join("[%s]" % m for m in marcas) if marcas else ""))

    print()
    print("COMO LEER ESTA TABLA")
    print("  T/M2      cuanto produjo esa cama en toda su ventana. Es el numero")
    print("            que se compara con el costo de ocupar la cama.")
    print("  T/M2/SEM  el ritmo. Sirve para comparar un cultivo de ventana larga")
    print("            con uno de ventana corta, que es lo que T/M2 no deja ver.")
    print("  [ABIERTA] la ventana seguia produciendo al cierre del registro:")
    print("            su T/M2 esta TRUNCADO, va a subir.")
    print("  [DENOM INCOMPLETO] hay siembras sin conteo en esa cama, asi que el")
    print("            area sale mas chica de lo real y el T/M2 sale INFLADO.")
    print("  [CIERRE AJENO] la cama se cerro por espacio, demanda o sanidad —")
    print("            no porque la planta dejara de producir. SUBESTIMA.")
    print("  [FRAGMENTO] la ventana registrada es mas corta que la ventana MINIMA")
    print("            documentada del grupo. Miente en las dos direcciones: el")
    print("            T/M2 sale corto y el ritmo sale largo. Por eso el ritmo no")
    print("            se imprime y el lote no entra al ranking.")
    print("  [ARRANCA EN EL CORTE] su primera cosecha es del %s, el primer dia" % (arranque or "?"))
    print("            del registro. Ese lote ya venia cosechando desde antes.")


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

    lotes, plantas, corte_registro, sin_variedad, _ = construir_lotes(grupo)

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
    subtipos = cargar_subtipos()
    cierres = cargar_cierres()
    hubo_perenne = False
    cerrados_ajenos, cerrados_tarde = [], []
    denom_incompleto = 0
    ambiguos = 0
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
        pl, sin_conteo, nivel_multi = _plantas_del_lote(g, v, b, plantas, a, z, ciclos_perenne, subtipos, cierres)
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
        if nivel_multi == "VENTANA":
            marca = ("multi-siembra: resuelta por fecha " + marca).strip()
        elif nivel_multi:
            marca = ("%s %s" % (nivel_multi, marca)).strip()
            ambiguos += 1
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

    if ambiguos:
        print()
        print("%d lote(s) MULTI-SIEMBRA: el mismo cultivar (o, en un corte Mix," % ambiguos)
        print("cualquier cultivar del bloque) se sembro mas de una vez en esa cama.")
        print("Cuando las dos siembras tienen fecha y ciclo conocido, esta funcion")
        print("aisla cual estaba activa en la fecha del corte (marca 'resuelta por")
        print("fecha'). Cuando no puede — falta una fecha, o las dos ventanas")
        print("estimadas se solapan — queda AMBIGUO: se sigue sumando para no perder")
        print("tallos, pero el numero de plantas puede estar mezclando dos siembras")
        print("que no produjeron al mismo tiempo.")

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


def tasas_limpias():
    """Tasa de corte (tallos/planta/dia) medida SOLO en lotes limpios.

    "Limpio" quiere decir: cultivar identificado (no Mix), denominador de
    plantas completo, sin multi-siembra ambigua, ventana igual o mayor a la
    minima documentada del grupo (no FRAGMENTO), y sin cierre ajeno. Son las
    mismas condiciones que 'm2' usa para su ranking "sin ninguna marca".

    Es la base del prorrateo de "Mix": Vanessa pidio prorratear por tasa de
    corte conocida, no por cantidad de plantas a secas — dos cultivares con
    la misma cantidad de plantas activas no cortan igual.

    Devuelve (tasas_cultivar, tasas_grupo):
      tasas_cultivar: {(grupo_norm, cultivar_norm): tallos/planta/dia}
      tasas_grupo:    {grupo_norm: tallos/planta/dia} — promedio de TODO el
                      grupo, para cuando el cultivar activo no tiene lotes
                      limpios propios con los que medirse.
    """
    lotes, plantas, _, _, _ = construir_lotes()
    ciclos = cargar_ciclos()
    subtipos = cargar_subtipos()
    cierres = cargar_cierres()

    num_c, den_c = defaultdict(float), defaultdict(float)
    num_g, den_g = defaultdict(float), defaultdict(float)
    for (g, v, b), d in lotes.items():
        vn = norm(v)
        if vn in ("", "mix", "sin variedad") or es_perenne(g, ciclos):
            continue
        ini, fin, dias, raras = ventana_del_lote(d["fechas"])
        if raras:
            continue
        pl, sin_conteo, nivel_multi = _plantas_del_lote(g, v, b, plantas, ini, fin, ciclos, subtipos, cierres)
        if not pl or sin_conteo or (nivel_multi and nivel_multi != "VENTANA"):
            continue
        res, nivel = parametros_de(g, v, ciclos, subtipos)
        vmin, _ = valor_parametro(res, nivel, "ventana_min")
        if vmin and (dias / 7.0) < float(vmin):
            continue
        cie = buscar_cierre(g, v, b, cierres)
        if (cie or {}).get("motivo", "") in CIERRE_AJENO:
            continue
        num_c[(norm(g), vn)] += d["tallos"]
        den_c[(norm(g), vn)] += pl * dias
        num_g[norm(g)] += d["tallos"]
        den_g[norm(g)] += pl * dias

    tasas_c = {k: num_c[k] / den_c[k] for k in num_c if den_c[k]}
    tasas_g = {k: num_g[k] / den_g[k] for k in num_g if den_g[k]}
    return tasas_c, tasas_g


def siembras_activas(grupo, bloque_clave, fecha, plantas, ciclos, subtipos, cierres=None):
    """Cultivares con ventana de cosecha ESTIMADA activa en esa fecha y bloque.

    bloque_clave puede nombrar mas de una cama ("3a+3b+3c" — la clave que usa
    un lote de REGISTRO cuando el corte se hizo sobre varias camas a la vez).

    El fin de la ventana usa el cierre real de cierres_lote.csv cuando existe
    (ver _ventana_estimada) — es mas preciso que estimarlo por ciclo.

    Un cultivar sin fecha de siembra, o cuyo ciclo no tiene ningun dato de
    semanas a campo, NO ENTRA a la lista — no se puede saber si estaba activo,
    y afirmar que si seria inventar el dato. Devuelve {cultivar: plantas}.
    """
    beds = set(bloque_clave.split("+"))
    alias = alias_grupo(grupo)
    activos = defaultdict(float)
    for (hom, var, blo), entradas in plantas.items():
        if blo not in beds or not any(a in var for a in alias):
            continue
        for e in entradas:
            if not e["tiene"]:
                continue
            ini, fin = _ventana_estimada(grupo, var, e["fecha"], ciclos, subtipos,
                                          bloque=blo, cierres=cierres)
            if not ini or not (ini <= fecha and (fin is None or fecha <= fin)):
                continue
            activos[hom or var] += e["n"]
    return dict(activos)


def siembras_del_bloque(grupo, bloque_clave, plantas):
    """Todos los cultivares alguna vez sembrados de este grupo en esta cama,
    SIN filtrar por fecha ni ventana.

    Respaldo de Vanessa 2026-08-14 para cuando 'siembras_activas' no puede
    aislar quien estaba activo: "si no existe [ventana] para prorratear, se
    divide entre las variedades sembradas de esa especie". Es un reparto por
    PARTES IGUALES, mas grueso que el de tasa de corte — se usa solo cuando
    el metodo mejor no tiene con que trabajar. Devuelve un set de cultivares.
    """
    beds = set(bloque_clave.split("+"))
    alias = alias_grupo(grupo)
    cultivares = set()
    for (hom, var, blo), entradas in plantas.items():
        if blo not in beds or not any(a in var for a in alias):
            continue
        if any(e["tiene"] for e in entradas):
            cultivares.add(hom or var)
    return cultivares


def cmd_prorratear(grupo=None):
    """Prorratea los cortes 'Mix' entre los cultivares activos esa fecha.

    Vanessa 2026-08-13: "prorratea como el 2" — por tasa de corte conocida
    (tallos/planta/dia medida en lotes limpios), no por partes iguales ni por
    cantidad de plantas a secas, porque dos cultivares con las mismas plantas
    activas no cortan igual. Ese es el metodo PRINCIPAL.

    Vanessa 2026-08-14 agrego el respaldo para cuando el principal no
    alcanza: "si no existe [ventana/tasa] para prorratear, se divide entre
    las variedades sembradas de esa especie" — partes iguales. Se aplica en
    dos escalones, del mas al menos preciso:

      1. TASA — el metodo principal. Cultivares con ventana activa esa
         fecha (fecha de siembra + ciclo, y el cierre real de
         cierres_lote.csv cuando existe), ponderados por su tasa de corte.
      2. PARTES IGUALES ENTRE ACTIVAS — hay cultivares con ventana activa,
         pero ninguno tiene tasa medible (es el caso de Statice, Lisianthus,
         Zinnia y Strawflower: 0-6% de trazabilidad, no hay lotes limpios de
         los que medir una tasa). Se reparte igual entre esos cultivares.
      3. PARTES IGUALES ENTRE TODAS LAS SEMBRADAS DE LA CAMA — ni siquiera se
         pudo saber quien estaba activo esa fecha (falta la fecha de siembra
         de todos los candidatos, o su ventana estimada no cubre el corte).
         Se reparte igual entre TODO lo que CAMPO registra como sembrado de
         ese grupo en esa cama, sin filtrar por fecha. Es el escalon mas
         grueso: puede incluir una siembra que ya no estaba activa si CAMPO
         no trae con que descartarla.

    Solo si NINGUNA de las tres tiene con que trabajar —el grupo nunca se
    sembro en esa cama segun CAMPO— el corte queda SIN PRORRATEAR.

    Es una ESTIMACION, nunca un dato de cosecha real — regla 1 del CLAUDE.md.
    No se reescribe registro_tallos.csv: el resultado se guarda aparte en
    07-datos/mix_prorrateado.csv, marcado como derivado y con el metodo usado
    en cada fila, para que nadie lo confunda con un corte que alguien
    realmente conto en campo — y para que un reparto por partes iguales no
    se confunda con uno pesado por tasa real.

    Un corte "Mix" repartido en MAS DE UNA CAMA a la vez no se separa aqui
    (se cuenta y se reporta aparte): no hay como saber cuanto le toco a cada
    cama, y ese es un problema distinto al de que cultivar.
    """
    lotes, plantas, _, _, _ = construir_lotes()
    ciclos = cargar_ciclos()
    subtipos = cargar_subtipos()
    cierres = cargar_cierres()
    tasas_c, tasas_g = tasas_limpias()

    cosecha = _leer_csv("registro_tallos.csv")
    mix_por_dia = defaultdict(float)
    multi_cama = 0
    for c in cosecha:
        g = (c.get("Grupo") or "").strip()
        v = (c.get("Variedad / Serie") or "").strip()
        b = (c.get("Bloque") or "").strip()
        f = (c.get("Fecha") or "").strip()
        if not (g and b) or not re.match(r"^\d{4}-\d{2}-\d{2}$", f):
            continue
        if norm(v) not in ("", "mix", "sin variedad"):
            continue
        if grupo and norm(grupo) not in norm(g):
            continue
        camas = bloques_de(b)
        if len(camas) != 1:
            multi_cama += 1
            continue
        t = num(c.get("Tallos frescos") or "") or 0
        if t:
            mix_por_dia[(g, next(iter(camas)), f)] += t

    resultados, sin_prorratear = [], []
    for (g, blo, f), tallos_mix in mix_por_dia.items():
        fecha = datetime.date.fromisoformat(f)
        por_cultivar = siembras_activas(g, blo, fecha, plantas, ciclos, subtipos, cierres)
        metodo = "tasa"

        pesos = {}
        if por_cultivar:
            for cultivar, n in por_cultivar.items():
                tasa, fte = tasas_c.get((norm(g), cultivar)), "propia"
                if tasa is None:
                    tasa, fte = tasas_g.get(norm(g)), "de grupo"
                if tasa:
                    pesos[cultivar] = (n * tasa, tasa, fte)
            # Escalon 2: hay activas, pero ninguna tiene tasa medible.
            if not pesos:
                metodo = "partes iguales entre activas (sin tasa)"
                pesos = {cv: (1.0, None, "sin tasa") for cv in por_cultivar}
        else:
            # Escalon 3: no se pudo saber quien estaba activo. Se reparte
            # entre todo lo que CAMPO registra sembrado en esa cama.
            todas = siembras_del_bloque(g, blo, plantas)
            if todas:
                metodo = "partes iguales entre sembradas (sin ventana)"
                pesos = {cv: (1.0, None, "sin ventana") for cv in todas}

        total_peso = sum(p for p, _, _ in pesos.values())
        if not total_peso:
            sin_prorratear.append((g, blo, f, tallos_mix,
                                    "ninguna siembra de este grupo registrada en esa cama"))
            continue
        for cultivar, (peso, tasa, fte) in pesos.items():
            resultados.append({
                "fecha": f, "grupo": g, "bloque": blo,
                "tallos_mix_originales": "%.0f" % tallos_mix,
                "cultivar_estimado": cultivar,
                "metodo": metodo,
                "plantas_activas": "%.0f" % por_cultivar[cultivar] if cultivar in por_cultivar else "",
                "tasa_usada": "%.5f" % tasa if tasa else "",
                "fuente_tasa": fte,
                "pct_asignado": "%.4f" % (peso / total_peso),
                "tallos_estimados": "%.1f" % (tallos_mix * peso / total_peso),
            })

    ruta = os.path.join(DATOS, "mix_prorrateado.csv")
    campos = ["fecha", "grupo", "bloque", "tallos_mix_originales", "cultivar_estimado",
              "metodo", "plantas_activas", "tasa_usada", "fuente_tasa", "pct_asignado",
              "tallos_estimados"]
    with open(ruta, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(sorted(resultados, key=lambda r: (r["grupo"], r["fecha"])))

    total_mix = sum(mix_por_dia.values())
    total_prorrateado = sum(float(r["tallos_estimados"]) for r in resultados)
    print("PRORRATEO DE CORTES 'MIX'")
    print("ESTIMACION, no dato de cosecha real. Guardado en 07-datos/mix_prorrateado.csv")
    print("con el METODO de cada fila — no todos pesan igual de fuerte:")
    print("  tasa                                     -> el mas confiable")
    print("  partes iguales entre activas (sin tasa)   -> se sabe quien, no cuanto corta")
    print("  partes iguales entre sembradas (sin ventana) -> el mas grueso")
    print()
    print("Tallos 'Mix' totales%s: %.0f" % (" de %s" % grupo if grupo else "", total_mix))
    print("Prorrateados          : %.0f  (%.0f%%)" % (
        total_prorrateado, 100 * total_prorrateado / total_mix if total_mix else 0))
    print("Sin prorratear         : %.0f  (%.0f%%)" % (
        total_mix - total_prorrateado, 100 * (1 - total_prorrateado / total_mix) if total_mix else 0))
    if multi_cama:
        print("Cortes 'Mix' en MAS DE UNA CAMA a la vez (no se reparten aqui): %d filas"
              % multi_cama)

    if resultados:
        por_metodo = defaultdict(float)
        for r in resultados:
            por_metodo[r["metodo"]] += float(r["tallos_estimados"])
        print("\nProrrateados, por metodo:")
        for m, t in sorted(por_metodo.items(), key=lambda kv: -kv[1]):
            print("  %8.0f tallos: %s" % (t, m))

        por_gc = defaultdict(float)
        for r in resultados:
            por_gc[(r["grupo"], r["cultivar_estimado"])] += float(r["tallos_estimados"])
        print("\nTallos estimados por cultivar (suma de todas las fechas prorrateadas):")
        for (g, cv), t in sorted(por_gc.items(), key=lambda kv: (kv[0][0], -kv[1])):
            print("  %-16s %-22s %8.0f tallos" % (g[:16], cv[:22], t))

    if sin_prorratear:
        motivos = defaultdict(float)
        for g, blo, f, t, motivo in sin_prorratear:
            motivos[motivo] += t
        print("\nSIN PRORRATEAR — por que:")
        for motivo, t in sorted(motivos.items(), key=lambda kv: -kv[1]):
            print("  %8.0f tallos: %s" % (t, motivo))


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

    _escalera_de_valor(productos, por_nombre, por_grupo)


def _escalera_de_valor(productos, por_nombre, por_grupo):
    """Contrasta la escalera declarada con la que muestran los precios.

    Vanessa la enuncio el 2026-08-13: "Los bouquets suelen tener de todas las
    formas para tener armonia. Pero tambien hacemos paquetes mixtos, que
    pueden tener solo lineales por ejemplo pero en mezcla de colores o
    variedades. Esas son de menos valor que un bouquet, pero de mayor valor
    que el paquete solido de una sola variedad y nos hace unicos."

    Se mide en dos unidades a proposito, porque dan respuestas distintas:
    por UNIDAD (lo que paga el cliente) y por TALLO (lo que cuesta la cama).
    """
    ESCALONES = [
        ("1 PAQUETE SOLIDO", lambda c: c == "paquete"),
        ("2 PAQUETE MIXTO", lambda c: c == "paquete mixto"),
        ("3 BOUQUET / ARREGLO",
         lambda c: c.startswith(("bouquet", "maxi bouquet", "centro de mesa"))),
    ]
    grupos = defaultdict(list)
    for p in productos:
        if not p["precio"]:
            continue
        a = analizar_producto(p, por_nombre, por_grupo)
        if not a["total_tallos"]:
            continue
        c = norm(p["categoria"])
        for etiqueta, prueba in ESCALONES:
            if prueba(c):
                grupos[etiqueta].append((p["producto"], a["precio"], a["total_tallos"]))
                break

    if len(grupos) < 2:
        return

    def mediana(xs):
        xs = sorted(xs)
        return xs[len(xs) // 2]

    print("\n\nESCALERA DE VALOR — paquete solido < paquete mixto < bouquet")
    print("%-22s %3s %12s %12s" % ("ESCALON", "N", "$/UNIDAD", "$/TALLO"))
    print("-" * 54)
    resumen = []
    for etiqueta, _ in ESCALONES:
        l = grupos.get(etiqueta)
        if not l:
            continue
        mu = mediana([pr for _, pr, _ in l])
        mt = mediana([pr / t for _, pr, t in l])
        resumen.append((etiqueta, mu, mt))
        print("%-22s %3d %12s %12s" % (
            etiqueta, len(l),
            "{:,.0f}".format(mu).replace(",", "."),
            "{:,.0f}".format(mt).replace(",", ".")))
    print("(medianas, no promedios: con 5 a 12 productos por escalon un solo")
    print(" precio atipico mueve el promedio y no mueve la mediana)")

    if len(resumen) == 3:
        u = [r[1] for r in resumen]
        t = [r[2] for r in resumen]
        sube_u = u[0] < u[1] < u[2]
        sube_t = t[0] < t[1] < t[2]
        print()
        print("  Por UNIDAD la escalera %s: %s" % (
            "SE CUMPLE" if sube_u else "NO se cumple",
            " -> ".join("{:,.0f}".format(x).replace(",", ".") for x in u)))
        print("  Por TALLO  la escalera %s: %s" % (
            "SE CUMPLE" if sube_t else "NO se cumple",
            " -> ".join("{:,.0f}".format(x).replace(",", ".") for x in t)))
        if sube_u and not sube_t:
            print()
            print("  Los dos juntos dicen una sola cosa: el escalon se esta cobrando")
            print("  en TALLOS, no en precio. Un paquete mixto vale mas porque lleva")
            print("  mas flor, no porque la mezcla se cobre. Si mezclar es lo que")
            print("  hace unico al producto, hoy esa diferencia se esta regalando —")
            print("  y ademas cuesta mas cama, porque son mas tallos propios.")
    print("\n  OJO: esto es PRECIO DE LISTA, no lo que se vende. Cual combinacion")
    print("  rota mejor no se puede responder todavia: no existe archivo de")
    print("  ventas. Lo que hay son las combinaciones que Vanessa nombro, en")
    print("  07-datos/combinaciones_venta.csv.")


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
    elif cmd == "rendimiento":
        cmd_rendimiento(argv[2] if len(argv) > 2 else None)
    elif cmd == "m2":
        cmd_m2(argv[2] if len(argv) > 2 else None)
    elif cmd == "prorratear":
        cmd_prorratear(argv[2] if len(argv) > 2 else None)
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
