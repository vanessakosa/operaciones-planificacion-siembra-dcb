#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ocupacion de cama: de tallos a tallos por m2 por semana.

    python3 motor/ocupacion.py           # la tabla por grupo
    python3 motor/ocupacion.py camas     # el area de cada cama de la finca

DE DONDE SALE EL AREA
---------------------
La finca tiene una sola geometria de cama: huecos cada 15 cm, 8 lineas, 1,20 m
de ancho. Eso da 0,18 m2 por hueco, y la constante cierra contra TODA el area
ya documentada:

    Inv 4 completo   28x112 + 225 + 212 + 190 huecos -> 677,3 m2   (doc: 677)
    Inv 5            13 camas x 176 huecos           -> 411,8 m2   (doc: 412)

Asi que el area de un lote NO hay que medirla en campo: se deriva de las
plantas que se trasplantaron y de la distancia de siembra de esa variedad.

    area ocupada m2 = plantas x 0,15 x (distancia_cm / 100)

La malla es de 0,15 m FIJO en una direccion; la distancia de siembra manda solo
en la otra. Sembrar mas denso mete mas plantas en la MISMA cama, no en menos
cama — por eso la distancia entra una sola vez y no al cuadrado.

    a 15 cm : 1.584 plantas en una cama de Inv 3A -> 35,64 m2  = el area real
    a 7,5 cm: 3.168 plantas en ESA MISMA cama     -> 35,64 m2  = el area real

Elevar la distancia al cuadrado daria 17,82 m2 en el segundo caso, y diria que
el lisianthus ocupa media cama cuando ocupa la cama entera. Es la formula de
`cerebro.py m2` (2026-08-13), verificada contra la malla que confirmo Vanessa:
"cada hueco tiene cero quince en esa malla". Ver 07-datos/area_camas.csv.

QUE ES Y QUE NO ES ESTE NUMERO
------------------------------
Es INGRESO por m2 por semana, no MARGEN. El costo por tallo todavia no esta
repartido por variedad — mientras la fila de tallos vendidos del modelo de
costos siga en cero, restar un costo aqui seria inventar el margen.

Y los tallos vienen del registro, que hoy corta el 2026-08-12. Todo lote
abierto en esa fecha sale SUBESTIMADO, y este numero con el.
"""

import csv
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerebro as C
import ficha_variedad as F


# Este bloque existe para arreglar el sesgo que hacia que esta tabla no se
# pudiera usar: el area salia de plantas ACUMULADAS de todo el historico y los
# tallos de la ventana corta del registro. Dividir uno por otro premiaba a los
# grupos recien sembrados y hundia a los de historico viejo.
#
# El diagnostico anterior decia que faltaba la columna 'Fecha siembra campo'.
# NO falta: esa columna se dejo de usar. Vanessa 2026-08-14: "deje de usarla,
# ahora trabajo solo con las semanas... la columna que sigue es la semana que
# se trasplanto... eso lo hago porque a veces puede pasar que en esa semana se
# sembro en dos dias distintos, y proyectamos todo por semana."
#
# La columna que SI esta llena es 'Semana' (la de trasplante):
#     Fecha siembra campo   112/302 filas   14% de las plantas
#     Semana de trasplante  294/302 filas   95% de las plantas
#
# Y no se veia por una razon mecanica: campo_siembras.csv tiene DOS columnas
# llamadas "Semana" (trasplante y inicio de cosecha), y csv.DictReader colapsa
# encabezados repetidos quedandose con la ultima. Asi que C._leer_csv() nunca
# pudo ver la de siembra. Por eso aqui se leen por POSICION.

MALLA_M = 0.15

COL_FECHA_SIEMBRA = 6    # 'Fecha siembra campo'  — respaldo, 14% de plantas
COL_SEMANA_SIEMBRA = 7   # 'Semana' de trasplante — principal, 95%
COL_MES_COSECHA = 9      # 'Inicio cosecha' en texto de mes
COL_SEMANA_COSECHA = 10  # 'Semana' de inicio de cosecha, ISO
COL_SEMANA_FIN = 11      # 'Fin de cosecha', semana ISO

ANIO_INICIAL = 2025
UMBRAL_CRUCE_ANIO = 26

MESES = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "sept": 9, "octubre": 10,
    "noviembre": 11, "nov": 11, "diciembre": 12, "dic": 12,
    # 'MAYO MADRES' lo confirma en el propio archivo: Madres es mayo. No es
    # deduccion, es una fila que trae las dos cosas escritas juntas.
    "mayo madres": 5,
}


def _filas_crudas():
    """campo_siembras.csv como listas, alineado 1 a 1 con C._leer_csv()."""
    ruta = os.path.join(C.DATOS, "campo_siembras.csv")
    with open(ruta, newline="", encoding="utf-8") as fh:
        return list(csv.reader(fh))[1:]


def _semanas_de_siembra(crudas):
    """Semana ISO de trasplante con el ano inferido por SECUENCIA.

    El archivo trae el numero de semana pero no el ano. Las 302 filas son un
    log cronologico que arranca en la semana 31 de 2025, asi que una caida
    grande en el numero de semana es el cruce de diciembre a enero y no un
    error de tipeo. Un salto de 1-2 semanas es jitter del dictado.

    Verificado contra las 111 filas que todavia traen fecha exacta: las 111
    coinciden en ano y en semana (+-1). Ver 13-optimizacion/06-tallos-por-m2.md.
    """
    salida, anio, anterior = [], ANIO_INICIAL, None
    for r in crudas:
        txt = (r[COL_SEMANA_SIEMBRA] if len(r) > COL_SEMANA_SIEMBRA else "").strip()
        if not txt.isdigit():
            salida.append(None)
            continue
        sem = int(txt)
        if anterior is not None and (anterior - sem) > UMBRAL_CRUCE_ANIO:
            anio += 1
        anterior = sem
        try:
            salida.append(datetime.date.fromisocalendar(anio, sem, 1))
        except ValueError:
            salida.append(None)
    return salida


def _semana_iso_anclada(sem, ancla):
    """Fecha del lunes de una semana ISO sin ano, anclada a una fecha previa.

    La cosecha no puede empezar antes de la siembra, asi que de los dos anos
    posibles se toma el primero que no viole eso.
    """
    if not (sem and ancla):
        return None
    for anio in (ancla.year, ancla.year + 1):
        try:
            f = datetime.date.fromisocalendar(anio, sem, 1)
        except ValueError:
            continue
        if f >= ancla:
            return f
    return None


def _mes_anclado(txt, ancla):
    """Fecha aproximada (dia 15) de un mes en texto, anclado a la siembra.

    Es la fuente mas ruidosa: +-2 semanas. Solo se usa cuando no hay semana
    ISO de cosecha. 'MADRES' y 'AMOR' NO se traducen: son nombres de evento
    comercial, no meses, y deducirlos seria inventar el dato.
    """
    t = C.norm(txt or "").strip()
    if not t:
        return None
    mes = MESES.get(t)
    if mes is None:                       # 'JUN-JUL', 'JULIO/AGOSTO', 'ABRIL?'
        for sep in ("-", "/", " "):
            if sep in t:
                mes = MESES.get(t.split(sep)[0].strip().rstrip("?"))
                if mes:
                    break
    if mes is None:
        mes = MESES.get(t.rstrip("?"))
    if mes is None or not ancla:
        return None
    for anio in (ancla.year, ancla.year + 1):
        f = datetime.date(anio, mes, 15)
        if f >= ancla:
            return f
    return None


def ventanas_de_siembra(ciclos):
    """Ventana de cosecha estimada de cada fila de campo_siembras.csv.

    Devuelve una lista alineada con C._leer_csv("campo_siembras.csv"), cada
    elemento un dict con plantas, inicio y fin de la ventana, y la PROCEDENCIA
    de cada extremo — para que se pueda auditar de donde salio cada fecha en
    vez de tener que creerle a la tabla.

    Prioridad del inicio, de mas firme a mas flojo:
      SEM   semana ISO de inicio de cosecha anotada en campo (32% de plantas)
      MES   el texto de mes, aproximado al dia 15 (+-2 semanas)
      CIC   estimado con ciclos_variedad.csv desde el trasplante

    El fin: la semana ISO de 'Fin de cosecha' si esta; si no, inicio mas la
    ventana del ciclo; si tampoco, queda ABIERTO — sigue produciendo, que es
    lo honesto, en vez de cerrarse con un numero inventado.
    """
    crudas = _filas_crudas()
    siembra = _semanas_de_siembra(crudas)
    dicts = C._leer_csv("campo_siembras.csv")
    salida = []
    for fila, cruda, f_siembra in zip(dicts, crudas, siembra):
        def col(i):
            return (cruda[i] if len(cruda) > i else "").strip()

        # Respaldo para las filas viejas que traen fecha exacta y no semana.
        if not f_siembra and re.match(r"^\d{4}-\d{2}-\d{2}$", col(COL_FECHA_SIEMBRA)):
            f_siembra = datetime.date.fromisoformat(col(COL_FECHA_SIEMBRA))

        plantas = C.num(col(5)) or 0.0
        nombre = " ".join([(fila.get("Nombre Homologados") or ""),
                           (fila.get("Variedad") or "")])

        ini = fin = None
        fte_ini = fte_fin = "--"
        sem_cos = col(COL_SEMANA_COSECHA)
        if sem_cos.isdigit() and f_siembra:
            ini = _semana_iso_anclada(int(sem_cos), f_siembra)
            fte_ini = "SEM"
        if not ini and f_siembra:
            ini = _mes_anclado(col(COL_MES_COSECHA), f_siembra)
            if ini:
                fte_ini = "MES"

        cic = None
        n = C.norm(nombre)
        for clave, c in ciclos.items():
            if clave and clave in n:
                cic = c
                break

        if not ini and f_siembra and cic:
            campo = cic.get("sem_a_campo_min") or cic.get("sem_a_campo_max")
            if campo:
                ini = f_siembra + datetime.timedelta(weeks=float(campo))
                fte_ini = "CIC"

        sem_fin = col(COL_SEMANA_FIN)
        if sem_fin.isdigit() and ini:
            fin = _semana_iso_anclada(int(sem_fin), ini)
            fte_fin = "SEM"
        if not fin and ini and cic:
            vent = cic.get("ventana_max") or cic.get("ventana_min")
            if vent:
                fin = ini + datetime.timedelta(weeks=float(vent))
                fte_fin = "CIC"
        if not fin and ini:
            fte_fin = "ABIERTA"

        salida.append({
            "nombre": nombre, "plantas": plantas, "siembra": f_siembra,
            "inicio": ini, "fin": fin, "fte_ini": fte_ini, "fte_fin": fte_fin,
            "ubicada": bool(f_siembra),
        })
    return salida


def plantas_en_ventana(grupos, ciclos, ventana_de):
    """Plantas por grupo cuya cosecha SOLAPA la ventana registrada del grupo.

    Es el arreglo del sesgo: solo entra al denominador de area la cama que
    estaba efectivamente cosechando en el mismo periodo en que se contaron sus
    tallos. Una siembra de 2025 que ya cerro no ocupa cama en la ventana del
    registro y no debe inflar el area de su grupo.

    La ventana es la PROPIA DE CADA GRUPO (ventana_de[g] = (desde, hasta)), no
    una global. Si se usara la global, un grupo cuyos tallos se registraron
    dos semanas cargaria con el area de camas que produjeron doce — el
    numerador y el denominador tienen que cubrir el mismo periodo.

    Devuelve (en_ventana, acumulado, diag) para poder mostrar las dos y que el
    efecto del recorte quede a la vista.
    """
    ordenados = sorted(grupos, key=lambda g: -len(g))
    en_ventana, acumulado = {}, {}
    diag = {"sin_ubicar": 0.0, "sin_ventana": 0.0, "fuera": 0.0,
            "dentro": 0.0, "fte": {}}
    for v in ventanas_de_siembra(ciclos):
        g = next((x for x in ordenados if C.norm(x) in C.norm(v["nombre"])), None)
        if not g or not v["plantas"]:
            continue
        acumulado[g] = acumulado.get(g, 0.0) + v["plantas"]
        rango = ventana_de.get(g)
        if not rango:
            continue
        desde, hasta = rango
        if not v["ubicada"]:
            diag["sin_ubicar"] += v["plantas"]
            continue
        if not v["inicio"]:
            diag["sin_ventana"] += v["plantas"]
            continue
        # Una ventana sin fin documentado ni estimable sigue abierta: solapa
        # con cualquier corte posterior a su inicio.
        fin = v["fin"] or datetime.date.max
        if v["inicio"] <= hasta and fin >= desde:
            en_ventana[g] = en_ventana.get(g, 0.0) + v["plantas"]
            diag["dentro"] += v["plantas"]
            diag["fte"][v["fte_ini"]] = diag["fte"].get(v["fte_ini"], 0.0) + v["plantas"]
        else:
            diag["fuera"] += v["plantas"]
    return en_ventana, acumulado, diag


def cobertura_ubicacion(ciclos):
    """Cuanta del area sembrada se puede UBICAR EN EL TIEMPO.

    Es la validacion que decide si tallos/m2 se puede comparar entre grupos.
    Antes media la columna equivocada — 'Fecha siembra campo', 14% — y por eso
    la tabla se declaraba inservible teniendo el dato al lado.
    """
    con = sin = 0.0
    for v in ventanas_de_siembra(ciclos):
        if not v["plantas"]:
            continue
        if v["ubicada"]:
            con += v["plantas"]
        else:
            sin += v["plantas"]
    tot = con + sin
    return {"con": con, "sin": sin, "total": tot,
            "pct": (con / tot) if tot else 0.0}


def cargar_camas():
    filas = []
    for f in C._leer_csv("area_camas.csv"):
        f["_area"] = C.num(f.get("area_cama_m2") or "")
        filas.append(f)
    return filas


def cmd_camas():
    filas = cargar_camas()
    print("AREA POR CAMA — geometria de la finca (0,15 m x 8 lineas = 0,18 m2/hueco)\n")
    print("%-16s %7s %6s %10s %6s %12s  %s" % (
        "CAMA", "HUECOS", "LIN", "AREA m2", "CAMAS", "BLOQUE m2", "CONFIANZA"))
    print("-" * 82)
    tot = 0.0
    for f in filas:
        ab = C.num(f.get("area_bloque_m2") or "")
        if ab:
            tot += ab
        print("%-16s %7s %6s %10s %6s %12s  %s" % (
            f["bloque"][:16], f.get("huecos_largo") or "--",
            f.get("lineas") or "--",
            ("%.2f" % f["_area"]) if f["_area"] else "--",
            f.get("n_camas") or "--",
            ("%.2f" % ab) if ab else "--",
            f.get("confianza", "")))
    print("-" * 82)
    print("%-16s %7s %6s %10s %6s %12.2f" % ("SUMA", "", "", "", "", tot))
    print("\n  Solo suma donde n_camas es conocido. Faltan Inv 3A, Inv 3B, Inv 2,")
    print("  Inv 1 y las tres Ext: el area de cama esta, el numero de camas no.")
    conflictos = [f for f in filas if f.get("confianza") == "CONFLICTO"]
    if conflictos:
        print("\n  CONFLICTO ABIERTO:")
        for f in conflictos:
            print("    %s — %s" % (f["bloque"], f.get("notas", "")[:110]))


def main(argv):
    if len(argv) > 1 and argv[1].startswith("cama"):
        return cmd_camas()

    roles = C.cargar_roles()
    dem = C.demanda_catalogo()
    ofe = C.oferta_registrada()
    ciclos = C.cargar_ciclos()
    grupos = sorted(set(roles) | set(dem["demanda"]) | set(ofe["tallos"]))
    ingreso = F.ingreso_por_grupo()

    # La ventana de cada grupo es la que cubre SU registro de cosecha, no una
    # global: el area del denominador tiene que corresponder al mismo periodo
    # en que se contaron los tallos del numerador.
    ventana_de = {g: (ofe["primera"][g], ofe["ultima"][g])
                  for g in ofe["primera"] if g in ofe["ultima"]}
    en_vent, acum, diag = plantas_en_ventana(grupos, ciclos, ventana_de)
    cob = cobertura_ubicacion(ciclos)
    valido = cob["pct"] >= 0.5

    filas, sin_area = [], []
    for g in grupos:
        cic = ciclos.get(C.norm(g)) or {}
        dist = cic.get("distancia_cm")
        pl = en_vent.get(g, 0.0)
        pl_acum = acum.get(g, 0.0)
        tallos = ofe["tallos"].get(g, 0)
        val = ingreso.get(g)
        if not tallos:
            continue
        if not (dist and pl):
            falta = []
            if not dist:
                falta.append("distancia")
            if not pl:
                falta.append("ninguna siembra ubicada solapa su ventana"
                             if pl_acum else "plantas trasplantadas")
            sin_area.append((g, tallos, pl_acum, ", ".join(falta)))
            continue
        area = pl * MALLA_M * (dist / 100.0)
        # Semanas de CAMA ocupada: del trasplante al fin de la ventana. La
        # germinacion es en bandeja y no ocupa cama, asi que no entra —
        # sem_a_campo ya se cuenta desde el trasplante (ver cerebro.plan_siembra,
        # que hace sem_campo = sem_cosecha - sem_a_campo y solo despues resta
        # la germinacion para llegar a la semana de bandeja).
        campo = cic.get("sem_a_campo_max") or cic.get("sem_a_campo_min")
        vent = cic.get("ventana_max") or cic.get("ventana_min")
        semanas = (campo + vent) if (campo and vent) else None
        # Cuantas semanas de cosecha alcanzo a ver el registro para este
        # grupo. Si son muchas menos que su ventana documentada, el numerador
        # es un pedazo y su tallos/m2 SUBESTIMA.
        d0, d1 = ventana_de.get(g, (None, None))
        sem_reg = ((d1 - d0).days / 7.0) if (d0 and d1) else None
        vmin = cic.get("ventana_min") or cic.get("ventana_max")
        fragmento = bool(sem_reg is not None and vmin and sem_reg < float(vmin))
        filas.append({
            "grupo": g,
            "rol": (roles.get(g, {}) or {}).get("rol", "") or "SIN_ROL",
            "plantas": pl, "plantas_acum": pl_acum, "dist": dist, "area": area,
            "tallos": tallos, "tallos_m2": tallos / area if area else 0,
            "semanas": semanas, "val": val, "sem_reg": sem_reg,
            "fragmento": fragmento,
            "ing_m2_sem": (tallos * val) / (area * semanas)
                          if (val and semanas and area) else None,
        })

    filas.sort(key=lambda f: -(f["ing_m2_sem"] or -1))

    print("=" * 100)
    print("OCUPACION DE CAMA — ingreso por m2 por semana")
    print("=" * 100)
    print()
    print("  El area esta RECORTADA a la ventana de cosecha de cada grupo: solo")
    print("  entran las plantas de siembras que estaban cosechando en el mismo")
    print("  periodo en que se contaron sus tallos.")
    print()
    print("    plantas ubicadas en el tiempo : %s de %s  (%.0f%%)" % (
        "{:,.0f}".format(cob["con"]).replace(",", "."),
        "{:,.0f}".format(cob["total"]).replace(",", "."), 100 * cob["pct"]))
    print("    plantas dentro de su ventana  : %s   (las que forman el area)"
          % "{:,.0f}".format(diag["dentro"]).replace(",", "."))
    print("    plantas fuera de su ventana   : %s   (siembras ya cerradas o"
          % "{:,.0f}".format(diag["fuera"]).replace(",", "."))
    print("                                    posteriores al corte)")
    print()
    print("  De donde salio el inicio de cosecha de las que entraron:")
    for fte, etiq in (("SEM", "semana ISO anotada en campo — la mas firme"),
                      ("MES", "texto de mes, aproximado al dia 15 (+-2 sem)"),
                      ("CIC", "estimado con ciclos_variedad.csv")):
        if diag["fte"].get(fte):
            print("    %-4s %8s plantas   %s" % (
                fte, "{:,.0f}".format(diag["fte"][fte]).replace(",", "."), etiq))
    print()
    print("%-18s %-6s %8s %8s %5s %8s %7s %8s %4s %10s" % (
        "GRUPO", "ROL", "PLANTAS", "(ACUM)", "DIST", "AREA m2", "TALLOS",
        "TALLOS/m2", "SEM", "$/m2/SEM"))
    print("-" * 100)
    for f in filas:
        print("%-18s %-6s %8s %8s %4.0fcm %8.1f %7.0f %8.1f %4s %10s%s" % (
            f["grupo"][:18], f["rol"][:6],
            "{:,.0f}".format(f["plantas"]).replace(",", "."),
            "{:,.0f}".format(f["plantas_acum"]).replace(",", "."),
            f["dist"], f["area"], f["tallos"], f["tallos_m2"],
            ("%.0f" % f["semanas"]) if f["semanas"] else "--",
            ("{:,.0f}".format(f["ing_m2_sem"]).replace(",", ".")
             if f["ing_m2_sem"] else "--"),
            "  [FRAGMENTO]" if f["fragmento"] else ""))

    if sin_area:
        print()
        print("SIN AREA — cosechan pero no se les puede calcular ocupacion (%d)"
              % len(sin_area))
        print("No es un cero: es que falta el denominador. Que falta en cada uno:")
        for g, t, pa, falta in sorted(sin_area, key=lambda x: -x[1]):
            print("  %-18s %6.0f tallos   acum %7s pl   falta %s" % (
                g[:18], t, "{:,.0f}".format(pa).replace(",", "."), falta))

    # -----------------------------------------------------------------
    # La prueba del denominador. Si el recorte fuera equivocado, el
    # tallos/planta implicito se iria lejos del documentado. Es la unica
    # validacion interna que tiene esta tabla, asi que se imprime siempre.
    # -----------------------------------------------------------------
    print()
    print("PRUEBA DEL DENOMINADOR — tallos por planta implicito")
    print("Si el area recortada fuera equivocada, este numero se iria lejos del")
    print("documentado en ciclos_variedad.csv. Se muestra el antes y el despues.")
    print()
    print("  %-18s %9s %9s %8s  %s" % (
        "GRUPO", "CON ACUM", "RECORTADO", "DOC", "LECTURA"))
    print("  " + "-" * 88)
    mejoro = empeoro = igual = 0
    for f in sorted(filas, key=lambda x: -x["tallos"]):
        cic = ciclos.get(C.norm(f["grupo"])) or {}
        doc = cic.get("tallos_planta")
        iv = f["tallos"] / f["plantas"] if f["plantas"] else None
        ia = f["tallos"] / f["plantas_acum"] if f["plantas_acum"] else None
        if not (iv and doc):
            continue
        # Un grupo cuyo recorte no quito ninguna planta no "mejoro" ni
        # "empeoro": no se movio. Contarlo como empeorado seria afirmar un
        # efecto que no ocurrio.
        if ia:
            if abs(iv - ia) < 1e-9:
                igual += 1
            elif abs(iv - doc) < abs(ia - doc):
                mejoro += 1
            else:
                empeoro += 1
        if iv > doc * 1.5:
            lec = "sobre el doc: el ciclo subestima tallos/planta"
        elif iv < doc * 0.5:
            lec = "bajo el doc: numerador truncado por el corte"
        else:
            lec = "coherente"
        print("  %-18s %9.2f %9.2f %8g  %s" % (f["grupo"][:18], ia or 0, iv, doc, lec))
    print()
    print("  El recorte acerco al valor documentado en %d grupos, lo alejo en %d,"
          % (mejoro, empeoro))
    print("  y en %d no quito ninguna planta (su area ya estaba toda en ventana)."
          % igual)
    print("  Los que quedan SOBRE el doc son cultivos de corte repetido cuyo")
    print("  tallos/planta en ciclos_variedad.csv esta bajo (Zinnia y Green Ball")
    print("  figuran con 1). Los que quedan BAJO son de ventana larga a los que")
    print("  el registro solo les vio un tramo.")
    print()
    print("=" * 100)
    print("COMO SE LEE")
    print("=" * 100)
    print()
    con = [f for f in filas if f["ing_m2_sem"] and not f["fragmento"]]
    if con and valido:
        mej, peo = con[0], con[-1]
        print("  mejor : %-18s $%s por m2 por semana de cama" % (
            mej["grupo"][:18],
            "{:,.0f}".format(mej["ing_m2_sem"]).replace(",", ".")))
        print("  peor  : %-18s $%s" % (
            peo["grupo"][:18],
            "{:,.0f}".format(peo["ing_m2_sem"]).replace(",", ".")))
        print("  brecha: %.1fx" % (mej["ing_m2_sem"] / peo["ing_m2_sem"]))
        print()
        print("  Los lotes [FRAGMENTO] quedan FUERA de mejor/peor: su registro")
        print("  cubre menos semanas que su ventana documentada, asi que su")
        print("  tallos/m2 esta medido sobre un pedazo.")
    elif not valido:
        print("  Menos de la mitad de las plantas se puede ubicar en el tiempo:")
        print("  no se nombra mejor ni peor.")
    print()
    print("  PLANTAS  las que estaban en cosecha en la ventana del registro.")
    print("  (ACUM)   todas las trasplantadas del historico. La diferencia entre")
    print("           las dos es el sesgo que esta tabla corrige: usar (ACUM)")
    print("           como denominador hundia a los grupos con historico viejo.")
    print()
    print("  Este eje NO es el mismo que $/tallo. Un tallo caro que ocupa la cama")
    print("  40 semanas puede perder contra uno barato que la desocupa en 12.")
    print()
    print("  LO QUE TODAVIA LIMITA ESTA TABLA:")
    print("    1. Es INGRESO, no margen: no lleva costo de semilla, insumo ni")
    print("       mano de obra. Cuando entre la fila de tallos vendidos del")
    print("       modelo de costos, se resta y sale margen de verdad.")
    print("    2. Los tallos cortan el 2026-08-12. Faltan las semanas ISO 33-37,")
    print("       asi que todo lote abierto sale SUBESTIMADO — y con el su")
    print("       $/m2/sem.")
    print("    3. El %.0f%% de las plantas sigue sin semana de trasplante, y el"
          % (100 * (1 - cob["pct"])))
    print("       inicio de cosecha de %s plantas salio del texto de mes,"
          % "{:,.0f}".format(diag["fte"].get("MES", 0)).replace(",", "."))
    print("       que trae +-2 semanas de ruido.")
    print("    4. La distancia es la del GRUPO. Donde el subtipo manda (Celosia:")
    print("       cristata 7,5 cm y plumosa 15 cm) el area sale promediada.")
    print("    5. 'MADRES' y 'AMOR' en la columna de inicio de cosecha son")
    print("       nombres de evento, no meses: no se traducen, se preguntan.")
    print()


if __name__ == "__main__":
    main(sys.argv)
