#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Captura de cosecha dictada, cuando Drive todavia no esta actualizado.

    python3 motor/dictar_tallos.py estado     # hasta que fecha llega el registro
    python3 motor/dictar_tallos.py validar    # revisa lo dictado, no escribe nada
    python3 motor/dictar_tallos.py aplicar    # mezcla lo dictado en registro_tallos.csv
    python3 motor/dictar_tallos.py pegar      # bloque TSV para pegar en la hoja de Drive
    python3 motor/dictar_tallos.py vaciar     # cierra la sala de espera cuando Drive ya lo trae

POR QUE ESTE SCRIPT EXISTE
--------------------------
`importar_tallos.py` reescribe `registro_tallos.csv` COMPLETO desde el XLSX de
Drive (modo "w"). Cualquier fila que se escriba a mano en ese CSV desaparece en
la siguiente importacion, sin aviso.

Asi que lo dictado no vive ahi: vive en `07-datos/registro_tallos_dictado.csv`,
que es un archivo aparte y sobrevive a la importacion. Este script lo valida y
lo mezcla. El orden de trabajo es siempre el mismo:

    1. Vanessa dicta       -> se escriben filas en registro_tallos_dictado.csv
    2. validar             -> se revisan grupo, fecha, bloque y duplicados
    3. aplicar             -> registro_tallos.csv queda completo para el motor
    4. pegar               -> el bloque se pega en la hoja de Drive
    5. cuando Drive ya lo tiene, importar_tallos.py + aplicar (no duplica:
       las filas que ya llegaron por Drive se detectan y se saltan)

DRIVE SIGUE SIENDO LA FUENTE DE VERDAD. Este archivo es una sala de espera, no
un segundo registro paralelo: el paso 4 no es opcional.

REGLA QUE NO SE NEGOCIA
-----------------------
No se inventa una sola cifra. Todo lo que entra aqui salio del dictado de
Vanessa, y la columna `dictado_el` guarda la fecha en que lo dijo. Si un dato
falta (bloque, cantidad, grupo), la fila se marca ERROR y `aplicar` se niega a
correr hasta que se pregunte y se complete.
"""

import csv
import datetime
import difflib
import os
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RAIZ, "07-datos")

REGISTRO = os.path.join(DATOS, "registro_tallos.csv")
DICTADO = os.path.join(DATOS, "registro_tallos_dictado.csv")
LISTAS = os.path.join(DATOS, "listas_desplegables.csv")

# Columnas de la hoja REGISTRO de Drive, en su orden exacto. La columna 9 va
# vacia en la hoja original y se respeta para no desalinear el espejado.
CAB_REGISTRO = ["Fecha", "Grupo", "Variedad / Serie", "Tallos frescos",
                "Tallos secos", "Bloque", "¿Cierre cama?", "Notas", "",
                "CLAVE_LOTE (auto)"]

# Las 8 columnas que Vanessa dicta, mas la trazabilidad del dictado.
CAB_DICTADO = ["Fecha", "Grupo", "Variedad / Serie", "Tallos frescos",
               "Tallos secos", "Bloque", "¿Cierre cama?", "Notas",
               "dictado_el"]


def norm(s):
    """Minusculas sin acentos, para comparar 'Boca de Dragon' con 'Dragón'."""
    s = unicodedata.normalize("NFKD", (s or "").strip().lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def _leer(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, newline="", encoding="utf-8") as fh:
        return list(csv.reader(fh))


def _fecha(txt):
    txt = (txt or "").strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d/%m/%y"):
        try:
            return datetime.datetime.strptime(txt, fmt).date()
        except ValueError:
            continue
    return None


def _entero(txt):
    txt = (txt or "").strip().replace(".", "").replace(",", "")
    if not txt:
        return 0
    try:
        return int(float(txt))
    except ValueError:
        return None


def grupos_validos():
    """Grupo -> lista de variedades del desplegable de la hoja LISTAS."""
    filas = _leer(LISTAS)
    salida = {}
    for f in filas[1:]:
        if not f or not f[0].strip():
            continue
        salida[f[0].strip()] = [v.strip() for v in f[1:] if v.strip()]
    return salida


def filas_registro():
    """Filas de datos de registro_tallos.csv (sin encabezado ni fila de ayuda)."""
    filas = _leer(REGISTRO)
    if not filas:
        return [], []
    cabeza = filas[:2]          # encabezado + fila de instrucciones de la hoja
    cuerpo = [f for f in filas[2:] if any(c.strip() for c in f)]
    return cabeza, cuerpo


def bloques_conocidos(cuerpo):
    return {norm(f[5]) for f in cuerpo if len(f) > 5 and f[5].strip()}


def variedades_vistas(cuerpo):
    """(grupo, variedad) que ya se cosecharon de verdad.

    El desplegable de la hoja LISTAS dice 'Mix' para casi todo, pero el campo
    registra 'Forever Happy' o 'Enda Rose'. El dato real le gana al
    desplegable: si esa combinacion ya se cosecho, no se avisa nada.
    """
    return {(norm(f[1]), norm(f[2])) for f in cuerpo
            if len(f) > 2 and f[1].strip() and f[2].strip()}


def clave_lote(grupo, variedad, bloque):
    return "%s|%s|%s" % (grupo.strip(), variedad.strip(), bloque.strip())


def huella(fecha, grupo, variedad, bloque, frescos, secos):
    """Identidad de una cosecha, para no duplicar lo que ya entro por Drive."""
    return (fecha, norm(grupo), norm(variedad), norm(bloque), frescos, secos)


# --------------------------------------------------------------------------
# estado
# --------------------------------------------------------------------------

def cmd_estado():
    _, cuerpo = filas_registro()
    fechas = sorted(f for f in (_fecha(r[0]) for r in cuerpo) if f)
    if not fechas:
        print("registro_tallos.csv no tiene una sola fecha valida.")
        return
    hoy = datetime.date.today()
    ultima = fechas[-1]
    print("REGISTRO DE TALLOS")
    print("  filas          : %d" % len(cuerpo))
    print("  primera cosecha: %s (semana ISO %02d)"
          % (fechas[0], fechas[0].isocalendar()[1]))
    print("  ultima cosecha : %s (semana ISO %02d)"
          % (ultima, ultima.isocalendar()[1]))
    hueco = (hoy - ultima).days
    print("  hoy            : %s" % hoy)
    print("  sin registrar  : %d dias" % hueco)
    if hueco > 0:
        semanas = sorted({(ultima + datetime.timedelta(days=i)).isocalendar()[1]
                          for i in range(1, hueco + 1)})
        print("  semanas ISO en el hueco: %s"
              % ", ".join(str(s) for s in semanas))

    pend = _leer(DICTADO)
    pend = [f for f in pend[1:] if any(c.strip() for c in f)] if pend else []
    print("\nSALA DE ESPERA (registro_tallos_dictado.csv)")
    if not pend:
        print("  vacia — nada dictado pendiente de aplicar")
    else:
        fp = sorted(f for f in (_fecha(r[0]) for r in pend) if f)
        tot = sum(_entero(r[3]) or 0 for r in pend)
        print("  %d filas dictadas, %s -> %s, %d tallos frescos"
              % (len(pend), fp[0] if fp else "?", fp[-1] if fp else "?", tot))


# --------------------------------------------------------------------------
# validar
# --------------------------------------------------------------------------

def revisar():
    """Devuelve (filas_ok, incidencias). Cada incidencia es (nivel, fila, texto)."""
    crudas = _leer(DICTADO)
    if not crudas:
        return [], [("ERROR", 0, "No existe %s" % DICTADO)]

    cab = [c.strip() for c in crudas[0]]
    if [norm(c) for c in cab] != [norm(c) for c in CAB_DICTADO]:
        return [], [("ERROR", 1, "El encabezado no coincide. Esperado: %s"
                     % ", ".join(CAB_DICTADO))]

    _, cuerpo = filas_registro()
    ya = {huella(_fecha(f[0]), f[1], f[2] if len(f) > 2 else "",
                 f[5] if len(f) > 5 else "",
                 _entero(f[3] if len(f) > 3 else ""),
                 _entero(f[4] if len(f) > 4 else ""))
          for f in cuerpo}
    validos = grupos_validos()
    bloques = bloques_conocidos(cuerpo)
    combos = variedades_vistas(cuerpo)
    mapa_grupo = {norm(g): g for g in validos}
    hoy = datetime.date.today()

    ok, inc, vistas = [], [], set()
    for n, f in enumerate(crudas[1:], start=2):
        if not any(c.strip() for c in f):
            continue
        f = (f + [""] * len(CAB_DICTADO))[:len(CAB_DICTADO)]
        fecha_txt, grupo, variedad, frescos_txt, secos_txt, bloque, cierre, notas, dicho = \
            [c.strip() for c in f]

        fecha = _fecha(fecha_txt)
        if fecha is None:
            inc.append(("ERROR", n, "fecha ilegible: %r" % fecha_txt))
            continue
        if fecha > hoy:
            inc.append(("ERROR", n, "fecha futura (%s). Una cosecha no se "
                                    "registra antes de cortarla" % fecha))
            continue

        if not grupo:
            inc.append(("ERROR", n, "sin grupo"))
            continue
        if norm(grupo) not in mapa_grupo:
            cerca = difflib.get_close_matches(norm(grupo), list(mapa_grupo), 1, 0.6)
            pista = (" ¿quisiste decir %r?" % mapa_grupo[cerca[0]]) if cerca else ""
            inc.append(("ERROR", n, "grupo %r no esta en listas_desplegables.csv.%s"
                        % (grupo, pista)))
            continue
        grupo = mapa_grupo[norm(grupo)]        # se escribe con el nombre oficial

        opciones = validos[grupo]
        if not variedad:
            inc.append(("AVISO", n, "%s sin variedad — CLAVE_LOTE quedara "
                                    "'%s||%s'" % (grupo, grupo, bloque)))
        elif (norm(grupo), norm(variedad)) in combos:
            pass                               # ya se cosecho asi antes
        elif opciones and norm(variedad) not in {norm(o) for o in opciones}:
            inc.append(("AVISO", n, "variedad %r no esta en el desplegable de "
                                    "%s (%s)" % (variedad, grupo,
                                                 ", ".join(opciones))))

        frescos = _entero(frescos_txt)
        secos = _entero(secos_txt)
        if frescos is None or secos is None:
            inc.append(("ERROR", n, "cantidad no numerica: frescos=%r secos=%r"
                        % (frescos_txt, secos_txt)))
            continue
        if frescos == 0 and secos == 0:
            inc.append(("ERROR", n, "fila sin tallos (frescos y secos en 0)"))
            continue

        if not bloque:
            inc.append(("ERROR", n, "sin bloque — sin bloque el dato no cruza "
                                    "con microclima ni con capacidad"))
            continue
        if norm(bloque) not in bloques:
            inc.append(("AVISO", n, "bloque %r no aparece antes en el registro"
                        % bloque))

        if not dicho:
            inc.append(("AVISO", n, "sin dictado_el — se pierde la trazabilidad "
                                    "de cuando se dijo"))

        h = huella(fecha, grupo, variedad, bloque, frescos, secos)
        if h in ya:
            inc.append(("SALTA", n, "ya esta en registro_tallos.csv "
                                    "(%s %s %s)" % (fecha, grupo, bloque)))
            continue
        if h in vistas:
            inc.append(("SALTA", n, "repetida dentro del propio dictado"))
            continue
        vistas.add(h)

        ok.append({"fecha": fecha, "grupo": grupo, "variedad": variedad,
                   "frescos": frescos, "secos": secos, "bloque": bloque,
                   "cierre": cierre, "notas": notas, "dictado_el": dicho,
                   "linea": n})
    return ok, inc


def cmd_validar():
    ok, inc = revisar()
    errores = [i for i in inc if i[0] == "ERROR"]
    for nivel, linea, texto in inc:
        print("  [%s] linea %s: %s" % (nivel, linea, texto))
    if inc:
        print()
    print("%d filas listas para aplicar, %d errores, %d avisos, %d saltadas"
          % (len(ok), len(errores),
             len([i for i in inc if i[0] == "AVISO"]),
             len([i for i in inc if i[0] == "SALTA"])))
    if ok:
        print("\n%-12s %-16s %-18s %6s %6s %-10s" %
              ("FECHA", "GRUPO", "VARIEDAD", "FRESC", "SECOS", "BLOQUE"))
        for r in ok:
            print("%-12s %-16s %-18s %6d %6d %-10s"
                  % (r["fecha"], r["grupo"][:16], r["variedad"][:18],
                     r["frescos"], r["secos"], r["bloque"][:10]))
        print("\ntotal dictado: %d frescos, %d secos"
              % (sum(r["frescos"] for r in ok), sum(r["secos"] for r in ok)))
    return 1 if errores else 0


# --------------------------------------------------------------------------
# aplicar
# --------------------------------------------------------------------------

def cmd_aplicar():
    ok, inc = revisar()
    errores = [i for i in inc if i[0] == "ERROR"]
    if errores:
        print("NO se aplico nada. Hay %d errores que hay que resolver "
              "preguntando, no adivinando:" % len(errores))
        for _, linea, texto in errores:
            print("  linea %s: %s" % (linea, texto))
        return 1
    if not ok:
        print("Nada nuevo que aplicar (todo lo dictado ya esta en el registro).")
        return 0

    cabeza, cuerpo = filas_registro()
    nuevas = []
    for r in ok:
        fila = [r["fecha"].isoformat(), r["grupo"], r["variedad"],
                str(r["frescos"]), str(r["secos"]) if r["secos"] else "",
                r["bloque"], r["cierre"], r["notas"], "",
                clave_lote(r["grupo"], r["variedad"], r["bloque"])]
        nuevas.append(fila)

    todas = cuerpo + nuevas
    todas.sort(key=lambda f: (_fecha(f[0]) or datetime.date.min))

    with open(REGISTRO, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        for f in cabeza:
            w.writerow(f)
        w.writerows(todas)

    ult = max(_fecha(f[0]) for f in todas if _fecha(f[0]))
    print("Aplicadas %d filas nuevas a registro_tallos.csv (%d -> %d filas)."
          % (len(nuevas), len(cuerpo), len(todas)))
    print("El registro ahora llega al %s." % ult)
    for nivel, linea, texto in inc:
        if nivel != "ERROR":
            print("  [%s] linea %s: %s" % (nivel, linea, texto))
    print("\nOJO — dos cosas que esto NO hace:")
    print("  1. consolidado_lotes.csv y resumen_tallos_dia.csv se calculan en")
    print("     Drive; siguen sin estas filas hasta que Drive se actualice.")
    print("  2. Drive es la fuente de verdad. Corre 'pegar' y sube el bloque a")
    print("     la hoja REGISTRO, o la proxima importacion borra esto.")
    return 0


# --------------------------------------------------------------------------
# pegar
# --------------------------------------------------------------------------

def cmd_pegar():
    """Bloque para la hoja de Drive.

    Imprime la sala de espera COMPLETA, no solo lo que 'aplicar' considero
    nuevo: despues de aplicar, esas filas ya estan en el CSV local pero
    siguen faltando en Drive, que es lo que este comando resuelve.
    """
    _, inc = revisar()
    if [i for i in inc if i[0] == "ERROR"]:
        print("Hay errores. Corre 'validar' primero.")
        return 1
    crudas = _leer(DICTADO)
    filas = [f for f in crudas[1:] if any(c.strip() for c in f)] if crudas else []
    if not filas:
        print("Nada dictado que pegar.")
        return 0
    print("Columnas A-H de la hoja REGISTRO. Copiar y pegar en la primera fila")
    print("vacia. La columna I (CLAVE_LOTE) se calcula sola en la hoja.\n")
    for f in filas:
        f = (f + [""] * 9)[:9]
        fecha = _fecha(f[0])
        print("\t".join([fecha.strftime("%d/%m/%Y") if fecha else f[0]]
                        + [c.strip() for c in f[1:8]]))
    repes = [i for i in inc if i[0] == "SALTA"]
    if repes:
        print("\nREVISAR ANTES DE PEGAR — estas filas ya existian en el "
              "registro:")
        for _, linea, texto in repes:
            print("  linea %s: %s" % (linea, texto))
    print("\nCuando Drive ya tenga estas filas: correr importar_tallos.py con "
          "el XLSX\nnuevo y despues 'vaciar' para cerrar la sala de espera.")
    return 0


def cmd_vaciar():
    """Cierra la sala de espera una vez que Drive ya trae las filas.

    No borra nada a ciegas: exige que cada fila dictada este ya en
    registro_tallos.csv, y guarda copia en el historico antes de vaciar.
    """
    crudas = _leer(DICTADO)
    filas = [f for f in crudas[1:] if any(c.strip() for c in f)] if crudas else []
    if not filas:
        print("La sala de espera ya esta vacia.")
        return 0

    _, cuerpo = filas_registro()
    ya = {huella(_fecha(f[0]), f[1], f[2] if len(f) > 2 else "",
                 f[5] if len(f) > 5 else "",
                 _entero(f[3] if len(f) > 3 else ""),
                 _entero(f[4] if len(f) > 4 else ""))
          for f in cuerpo}
    faltan = []
    for n, f in enumerate(filas, start=2):
        f = (f + [""] * len(CAB_DICTADO))[:len(CAB_DICTADO)]
        h = huella(_fecha(f[0]), f[1], f[2], f[5],
                   _entero(f[3]), _entero(f[4]))
        if h not in ya:
            faltan.append((n, f))
    if faltan:
        print("NO se vacio nada. %d filas dictadas todavia no aparecen en "
              "registro_tallos.csv:" % len(faltan))
        for n, f in faltan:
            print("  linea %s: %s %s %s" % (n, f[0], f[1], f[5]))
        return 1

    historico = os.path.join(DATOS, "registro_tallos_dictado_historico.csv")
    existe = os.path.exists(historico)
    with open(historico, "a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if not existe:
            w.writerow(CAB_DICTADO + ["cerrado_el"])
        hoy = datetime.date.today().isoformat()
        for f in filas:
            w.writerow((f + [""] * len(CAB_DICTADO))[:len(CAB_DICTADO)] + [hoy])
    with open(DICTADO, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerow(CAB_DICTADO)
    print("Sala de espera cerrada: %d filas archivadas en %s."
          % (len(filas), os.path.basename(historico)))
    return 0


def main():
    cmds = {"estado": cmd_estado, "validar": cmd_validar,
            "aplicar": cmd_aplicar, "pegar": cmd_pegar, "vaciar": cmd_vaciar}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        raise SystemExit(__doc__.strip().split("\n\n")[1].rstrip())
    salida = cmds[sys.argv[1]]()
    sys.exit(salida or 0)


if __name__ == "__main__":
    main()
