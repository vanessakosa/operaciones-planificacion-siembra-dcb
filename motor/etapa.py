#!/usr/bin/env python3
"""Etapa fenologica de cada lote ACTIVO, derivada de la programacion.

Vanessa 2026-09-21: *"si no esta leyendo el archivo de programacion donde
aparece todo lo que no ha cerrado su ciclo de ventana, donde aparecen todos los
comentarios, es un error... ahi podria saber entonces la etapa fenologica en la
que esta cada cosa. Eso tiene que suceder ANTES de hacerme una sugerencia de
bomba."*

Antes de este archivo el motor buscaba la ocupacion en `ocupacion_lote.csv`, que
tiene UNA sola cosecha cargada a mano. La programacion, en cambio, ya trae las
tres cosas que hacen falta y las trae para 130 lotes:

    columna 16 `Estado`   -> Activa = no ha cerrado su ventana
    columna  7 `Semana`   -> semana de TRASPLANTE
    columna 10 `Semana`   -> semana de INICIO DE COSECHA

La etapa no hay que registrarla: se deriva. Y con ella la bomba que toca.

OJO — las dos columnas de semana se leen POR POSICION, no por nombre. El archivo
tiene DOS encabezados llamados `Semana` y `csv.DictReader` colapsa los repetidos
quedandose con el ultimo. Es el mismo bug que `ocupacion.py` documenta.
"""
import csv, os, sys, collections, datetime
import lotes as L

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RAIZ, "07-datos")

# indices de columna en campo_siembras.csv (POR POSICION — ver docstring)
I_VARIEDAD, I_SEM_SIEMBRA, I_BLOQUE = 2, 7, 8
I_SEM_COSECHA, I_FIN_COSECHA, I_COMENTARIOS = 10, 11, 12
I_HOMOLOGADO, I_ESTADO = 13, 16

# Los cortes de etapa. Se cambian aca, en un solo lugar.
SEM_VEGETATIVO = 6      # < 6 semanas en campo = vegetativo (regla del catalogo de bombas)
SEM_PREFLORACION = 3    # a <= 3 semanas de abrir cosecha = prefloracion

ETAPA_BOMBA = {
    "VEGETATIVO":   "VEG",
    "DESARROLLO":   "VEG",
    "PREFLORACION": "PREFLOR",
    "COSECHA":      "PREFLOR",
    "SIN_DATO":     None,
}


def semana_actual():
    return datetime.date.today().isocalendar()[1]


def _int(v):
    try:
        return int(float(str(v).strip()))
    except (ValueError, TypeError):
        return None


def etapa_de(sem_siembra, sem_cosecha, sem_actual):
    """(etapa, semanas_en_campo, confianza).

    El ano no esta en el archivo. Se infiere por secuencia: si la semana de
    inicio de cosecha es MENOR que la de siembra, la cosecha cae el ano
    siguiente y hay que sumarle 52. Mismo criterio para la semana en campo.
    """
    if sem_siembra is None:
        return "SIN_DATO", None, "NULA"
    en_campo = sem_actual - sem_siembra
    if en_campo < 0:
        en_campo += 52
    if sem_cosecha is None:
        # sin ventana declarada solo se puede separar vegetativo de lo demas
        etapa = "VEGETATIVO" if en_campo < SEM_VEGETATIVO else "DESARROLLO"
        return etapa, en_campo, "BAJA"
    cosecha = sem_cosecha + (52 if sem_cosecha < sem_siembra else 0)
    actual = sem_actual + (52 if sem_actual < sem_siembra else 0)
    faltan = cosecha - actual
    if faltan <= 0:
        etapa = "COSECHA"
    elif faltan <= SEM_PREFLORACION:
        etapa = "PREFLORACION"
    elif en_campo < SEM_VEGETATIVO:
        etapa = "VEGETATIVO"
    else:
        etapa = "DESARROLLO"
    return etapa, en_campo, "ALTA"


def lotes_activos(sem_actual=None, incluir_sin_estado=False):
    """Un dict por lote activo, ya con su etapa y sus bloques canonicos."""
    sem_actual = sem_actual or semana_actual()
    ruta = os.path.join(DATOS, "campo_siembras.csv")
    with open(ruta, encoding="utf-8") as f:
        filas = list(csv.reader(f))[1:]
    out = []
    for r in filas:
        r = (r + [""] * 21)[:21]
        estado = r[I_ESTADO].strip()
        if estado.lower() == "cerrada":
            continue
        if not estado and not incluir_sin_estado:
            continue
        if not r[I_VARIEDAD].strip():
            continue
        s, c = _int(r[I_SEM_SIEMBRA]), _int(r[I_SEM_COSECHA])
        fin = _int(r[I_FIN_COSECHA])
        etapa, en_campo, conf = etapa_de(s, c, sem_actual)
        out.append({
            "variedad": r[I_VARIEDAD].strip(),
            "homologado": r[I_HOMOLOGADO].strip(),
            "bloque_txt": r[I_BLOQUE].strip(),
            "bloques": L.bloques_de(r[I_BLOQUE]) or [],
            "sem_siembra": s, "sem_cosecha": c, "sem_cosecha_fin": fin,
            "en_campo": en_campo, "etapa": etapa, "confianza": conf,
            "estado": estado or "(sin estado)",
            "comentarios": r[I_COMENTARIOS].strip(),
        })
    return out


def por_bloque(sem_actual=None, incluir_sin_estado=False):
    """{bloque: [lote, ...]} — un lote en 2 bloques aparece en los dos."""
    d = collections.defaultdict(list)
    for lo in lotes_activos(sem_actual, incluir_sin_estado):
        for b in (lo["bloques"] or ["SIN_BLOQUE"]):
            d[b].append(lo)
    return d


def imprimir(sem_actual=None, incluir_sin_estado=False):
    sem = sem_actual or semana_actual()
    lot = lotes_activos(sem, incluir_sin_estado)
    d = por_bloque(sem, incluir_sin_estado)
    print("=" * 92)
    print(f"ETAPA FENOLOGICA POR BLOQUE — SEMANA {sem}   ({len(lot)} lotes sin cerrar ventana)")
    print("=" * 92)
    for b in sorted(d, key=lambda x: (x == "SIN_BLOQUE", x)):
        sub = d[b]
        cuenta = collections.Counter(x["etapa"] for x in sub)
        resumen = " · ".join(f"{k} {v}" for k, v in sorted(cuenta.items()))
        print(f"\n{b}   ({len(sub)} lotes: {resumen})")
        print("-" * 92)
        for x in sorted(sub, key=lambda y: (y["etapa"], -(y["en_campo"] or 0))):
            enc = f"{x['en_campo']}s" if x["en_campo"] is not None else "?"
            marca = "" if x["confianza"] == "ALTA" else f"  [{x['confianza']}]"
            print(f"   {x['etapa']:13} {enc:>4} en campo  {x['variedad'][:40]:40}{marca}")
            if x["comentarios"]:
                print(f"                 · {x['comentarios'][:150]}")
    # lo que la programacion NO pudo ubicar
    huerf = [x for x in lot if not x["bloques"]]
    if huerf:
        print(f"\n{'=' * 92}\nSIN BLOQUE RECONOCIBLE ({len(huerf)}) — no se les puede imputar ninguna bomba")
        print("-" * 92)
        for x in huerf:
            print(f"   {x['variedad'][:44]:44} bloque escrito: {x['bloque_txt']!r}")


if __name__ == "__main__":
    sem = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None
    imprimir(sem, incluir_sin_estado="--todos" in sys.argv)
