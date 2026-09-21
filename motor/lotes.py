#!/usr/bin/env python3
"""Imputacion de eventos a siembras por (bloque x semana).

LA IDEA CENTRAL, y la unica que hay que entender para usar todo esto:

    una bomba se aplica a un BLOQUE en una SEMANA
    una cosecha ocupa un BLOQUE durante un RANGO DE SEMANAS
    -> el cruce es (bloque x semana), y de ahi sale todo lo demas

Un evento (bomba, labor, fertirriego) en el bloque B la semana W se le carga a
TODA siembra que ocupaba B esa semana, prorrateado por area. Si el area no se
conoce, se reparte en partes iguales y el resultado sale marcado APROX — nunca
se inventa un numero y se presenta como medido.

Vanessa 2026-09-11: *"si tu sabes que en semana 37 yo aplique esta bomba, y en
semana 37 esta sembrado este numero de variedades, yo se que este numero de
variedades lo recibieron... eso se lo va sumando la ficha."*
"""
import csv, os, re, unicodedata, collections

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RAIZ, "07-datos")


def norm(s):
    s = unicodedata.normalize("NFKD", (s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def leer(nombre):
    ruta = os.path.join(DATOS, nombre)
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]


# ---------------------------------------------------------------- bloques
def alias_bloques():
    """El registro escribe el mismo bloque de 45 formas. Esto las colapsa.

    La tabla canonica es `area_camas.csv`, que ya trae `alias_registro`.
    """
    canon = {}
    for r in leer("area_camas.csv"):
        a = (r.get("alias_registro") or "").strip()
        if a:
            canon[norm(a)] = a
    return canon


def bloques_de(texto):
    """'Mini 3C Y 3B' -> ['Mini', '3C', '3B'].  Devuelve [] si no reconoce nada."""
    canon = alias_bloques()
    t = norm(texto)
    if not t or t == "sin dato":
        return []
    # El registro escribe el exterior en los dos ordenes: 'Ext 5' y '5 EXT'.
    # Sin esto '6 EXT' pierde contra el alias '6' y el lote del exterior se
    # imputa ADENTRO del invernadero — una bomba mal atribuida en dos fichas.
    t = re.sub(r"\b(\d+ ?[abc]?) ?ext\b", lambda m: "ext " + m.group(1).strip(), t)
    # los alias largos primero, para que 'Ext 3B' gane sobre '3B'
    hallados, usados = [], []
    for k in sorted(canon, key=len, reverse=True):
        if re.search(r"\b%s\b" % re.escape(k), t) and not any(k in u for u in usados):
            hallados.append(canon[k])
            usados.append(k)
    return hallados


def _semanas(desde, hasta, tope):
    try:
        d = int(float(desde))
    except (TypeError, ValueError):
        return set()
    try:
        h = int(float(hasta))
    except (TypeError, ValueError):
        h = tope          # ventana ABIERTA: ocupa hasta hoy
    return set(range(d, h + 1))


# ---------------------------------------------------------------- ocupacion
def ocupacion(tope_semana=53):
    """{(bloque, semana): [ {siembra, area_m2 o None}, ... ] }

    DOS fuentes, en este orden:

    1. La PROGRAMACION (`campo_siembras.csv`, Estado = Activa). Es la base: un
       lote ocupa sus bloques desde la semana de trasplante hasta que cierra la
       ventana. Son ~130 lotes y se mantienen solos al refrescar la hoja CAMPO.
    2. `ocupacion_lote.csv` ENCIMA, como correccion. Es el archivo curado a mano
       y es el unico que trae `area_m2`, asi que cuando una siembra esta en los
       dos gana este: sin area el reparto va en partes iguales y sale APROX.

    Antes solo existia (2), con UNA cosecha cargada. Toda bomba registrada caia
    en `NO SE PUDO IMPUTAR`. Vanessa 2026-09-21: *"si no esta leyendo el archivo
    de programacion... es un error"*.
    """
    idx = collections.defaultdict(list)
    vistos = set()

    # (1) la programacion. Import diferido: etapa.py importa este modulo.
    import etapa as E
    for lo in E.lotes_activos():
        if not lo["bloques"] or lo["sem_siembra"] is None:
            continue
        nombre = lo["homologado"] or lo["variedad"]
        siembra = "%s %s-S%s" % (nombre, "2026", lo["sem_siembra"])
        for b in lo["bloques"]:
            for w in _semanas(lo["sem_siembra"], lo["sem_cosecha_fin"], tope_semana):
                idx[(norm(b), w)].append({"siembra": siembra, "area": None})
            vistos.add((norm(b), norm(siembra)))

    # (2) el archivo curado encima — trae area y gana sobre la programacion
    for r in leer("ocupacion_lote.csv"):
        bloque = (r.get("bloque") or "").strip()
        if not bloque:
            continue
        try:
            area = float(r.get("area_m2") or "")
        except ValueError:
            area = None
        for w in _semanas(r.get("sem_desde"), r.get("sem_hasta"), tope_semana):
            idx[(norm(bloque), w)].append({"siembra": r["siembra"], "area": area})
    return idx


def reparto(bloque, semana, idx):
    """Que fraccion del evento le toca a cada siembra. Suma 1,0.

    Devuelve [(siembra, fraccion, exacto)] — `exacto` es False cuando el area
    no se conoce y hubo que repartir en partes iguales.
    """
    ocup = idx.get((norm(bloque), semana), [])
    if not ocup:
        return []
    areas = [o["area"] for o in ocup]
    if all(a is not None for a in areas) and sum(areas) > 0:
        tot = sum(areas)
        return [(o["siembra"], o["area"] / tot, True) for o in ocup]
    n = len(ocup)
    return [(o["siembra"], 1.0 / n, n == 1) for o in ocup]


# ---------------------------------------------------------------- eventos
def eventos(siembra=None, tope_semana=53):
    """Todo lo que le paso a una siembra, imputado por (bloque x semana).

    Devuelve filas con `fraccion` y `exacto`, mas las que no se pudieron
    imputar (`bloque` vacio o SIN_DATO), que se devuelven aparte porque son
    trabajo pendiente, no ruido.
    """
    idx = ocupacion(tope_semana)
    imputados, huerfanos = [], []
    fuentes = [
        ("BOMBA", "aplicaciones_lote.csv", "bomba_id"),
        ("LABOR", "labores_lote.csv", "labor"),
        ("FERTIRRIEGO", "fertirriego_lote.csv", "formula"),
    ]
    for tipo, archivo, campo in fuentes:
        for r in leer(archivo):
            que = (r.get(campo) or "").strip()
            sem = (r.get("semana_iso") or "").strip()
            blos = bloques_de(r.get("bloque") or "")
            semanas = []
            for parte in re.findall(r"\d+", sem):
                semanas.append(int(parte))
            if len(semanas) == 2:                    # '10-14' es un rango
                semanas = list(range(semanas[0], semanas[1] + 1))
            if not blos or not semanas:
                huerfanos.append(dict(tipo=tipo, que=que, fila=r,
                                      falta="bloque" if not blos else "semana"))
                continue
            # Aplicacion dirigida a camas puntuales: NO se reparte al bloque.
            # Un drench a 1 cama de 3B no lo recibieron los 11 lotes del bloque.
            # Mientras la ocupacion no baje a nivel CAMA, atribuirlo seria
            # inventar: sale como pendiente, con el motivo escrito.
            if (r.get("camas") or "").strip():
                huerfanos.append(dict(tipo=tipo, que=que, fila=r,
                                      falta="alcance de CAMA (%s) — la ocupacion solo llega a BLOQUE"
                                            % r["camas"].strip()))
                continue
            tocado = False
            for b in blos:
                for w in semanas:
                    for coh, frac, exacto in reparto(b, w, idx):
                        if siembra and norm(siembra) not in norm(coh):
                            continue
                        tocado = True
                        imputados.append(dict(tipo=tipo, que=que, siembra=coh, bloque=b,
                                              semana=w, fraccion=frac / len(blos),
                                              exacto=exacto, fila=r))
            if not tocado and not siembra:
                huerfanos.append(dict(tipo=tipo, que=que, fila=r,
                                      falta="no hay siembra ocupando ese bloque esa semana"))
    return imputados, huerfanos


def receta_bomba(bomba_id):
    return [r for r in leer("bombas_catalogo.csv")
            if norm(r.get("bomba_id")) == norm(bomba_id)]


def rotacion(desde_semana, hasta_semana):
    """La tabla que exige la regla APLICACIONES antes de recomendar nada."""
    out = collections.defaultdict(list)
    for r in leer("aplicaciones_lote.csv"):
        try:
            w = int(float(r.get("semana_iso") or ""))
        except ValueError:
            continue
        if desde_semana <= w <= hasta_semana:
            out[w].append(r)
    return out
