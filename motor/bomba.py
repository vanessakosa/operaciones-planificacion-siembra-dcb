#!/usr/bin/env python3
"""La sesion semanal de bombas: ver antes de decidir, y dejar registro al aplicar.

    python3 motor/bomba.py semana 37        # la mesa para disenar la bomba de la semana
    python3 motor/bomba.py catalogo         # las bombas y sus dosis
    python3 motor/bomba.py registrar 2026-09-12 37 "3B,3C" CHOQUE-BO 4 Wilson "oidio en lisianthus"
    python3 motor/bomba.py registrar 2026-09-12 37 "3B,3C" CHOQUE-BO PENDIENTE Wilson "oidio en lisianthus"
    python3 motor/bomba.py tanques 2026-09-12 "3B,3C" CHOQUE-BO 4    # completa el PENDIENTE de arriba

`semana` es OBLIGATORIO antes de recomendar nada — es la regla APLICACIONES de
CLAUDE.md hecha comando: muestra la rotacion de las ultimas 4 semanas y que hay
sembrado en cada bloque, para que la bomba se disene sobre lo que hay, no de
memoria.

`registrar` escribe en `07-datos/aplicaciones_lote.csv` con el BLOQUE, que es lo
que permite que la aplicacion se le sume despues a la ficha de cada cosecha.
Sin bloque la fila queda huerfana y no le suma a nadie.

Vegetativo y Prefloracion cambian de semana a semana segun lo que se vaya
cosechando, y Vanessa no sabe cuantos tanques se gastaron hasta que le
pregunta al operario — a veces dias despues. Por eso `tanques` NO es
obligatorio en `registrar`: se puede pasar `PENDIENTE` y la fila queda con
tanques/litros vacios (SIN romper la imputacion, que solo necesita bloque y
semana). `tanques` completa esa fila despues, cuando el dato llegue.
"""
import sys, os, csv, io, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lotes as L
import etapa as E

ANCHO = 92


def _siembras_por_bloque(semana):
    """Que hay en cada bloque esta semana, y en que etapa fenologica.

    Sale de la PROGRAMACION (campo_siembras.csv, columna Estado = Activa), no de
    ocupacion_lote.csv. Vanessa 2026-09-21: *"si no esta leyendo el archivo de
    programacion donde aparece todo lo que no ha cerrado su ciclo de ventana...
    es un error"*. La etapa se deriva, no se registra — ver motor/etapa.py.
    """
    return E.por_bloque(semana)


def cmd_semana(semana):
    print("=" * ANCHO)
    print("MESA DE BOMBA — SEMANA %d" % semana)
    print("=" * ANCHO)

    print("\n1. ROTACION DE LAS ULTIMAS 4 SEMANAS  (regla APLICACIONES: mirar antes de decidir)")
    print("-" * ANCHO)
    rot = L.rotacion(semana - 4, semana - 1)
    if not rot:
        print("   SIN REGISTRO en las semanas %d a %d." % (semana - 4, semana - 1))
        print("   NO se puede recomendar rotacion: no hay contra que rotar.")
        print("   aplicaciones_lote.csv esta vacio o no cubre este periodo.")
    else:
        for w in sorted(rot):
            for r in rot[w]:
                print("   sem %-3s %-12s %-14s %s" % (
                    w, r.get("bomba_id", ""), r.get("bloque", "") or "SIN BLOQUE",
                    r.get("motivo", "")[:40]))

    print("\n2. QUE HAY EN CADA BLOQUE, Y EN QUE ETAPA  (a quien le va a caer la bomba)")
    print("-" * ANCHO)
    porb = _siembras_por_bloque(semana)
    if not porb:
        print("   La programacion no tiene ningun lote Activa. Refrescar campo_siembras.csv.")
    else:
        for b in sorted(porb, key=lambda x: (x == "SIN_BLOQUE", x)):
            cuenta = collections.Counter(x["etapa"] for x in porb[b])
            resumen = " · ".join("%s %d" % (k, v) for k, v in sorted(cuenta.items()))
            bomba = sorted({E.ETAPA_BOMBA.get(x["etapa"]) for x in porb[b]} - {None})
            print("   %-10s %-42s -> %s" % (b, resumen, "+".join(bomba) or "SIN_DATO"))
        print("\n   Detalle lote por lote, con los comentarios de campo:")
        print("     python3 motor/etapa.py %d" % semana)

    print("\n3. SIEMBRAS QUE LA PROGRAMACION TODAVIA NO VE")
    print("-" * ANCHO)
    lot = E.lotes_activos(semana)
    ult = max((x["sem_siembra"] for x in lot if x["sem_siembra"]), default=None)
    veg = [x for x in lot if x["etapa"] == "VEGETATIVO"]
    if ult is not None and ult < semana - 1:
        print("   La siembra mas reciente registrada es de la semana %d." % ult)
        print("   Faltan las ultimas %d semanas de siembra -> todo lo VEGETATIVO" % (semana - ult))
        print("   es invisible aca (%d lotes en vegetativo hoy)." % len(veg))
        print("   Refrescar la hoja CAMPO antes de confiar en la bomba de desarrollo.")
    else:
        print("   La programacion esta al dia.")

    print("\n4. INCIDENCIA CONOCIDA EN ESOS BLOQUES")
    print("-" * ANCHO)
    hubo = False
    for r in L.leer("incidencia_fitosanitaria.csv"):
        blo = " ".join(str(v) for k, v in r.items() if "bloque" in L.norm(k))
        if any(b.lower() in blo.lower() for b in porb):
            hubo = True
            campos = [v for v in list(r.values())[:5] if v]
            print("   " + " · ".join(str(c)[:34] for c in campos))
    if not hubo:
        print("   Sin eventos registrados para estos bloques.")

    print("\n" + "-" * ANCHO)
    print("Con esto ya se puede disenar la bomba. Para dejarla registrada:")
    print('  python3 motor/bomba.py registrar <fecha> %d "<bloques>" <bomba_id> '
          '<tanques> <operario> "<motivo>"' % semana)


def cmd_catalogo():
    filas = L.leer("bombas_catalogo.csv")
    por = collections.OrderedDict()
    for r in filas:
        por.setdefault(r["bomba_id"], []).append(r)
    for bid, ings in por.items():
        print("\n%-12s %s  (%s)" % (bid, ings[0]["nombre"], ings[0]["objetivo"]))
        for i in ings:
            print("     %-28s %6s %s" % (i["producto"][:28], i["dosis_25L"], i["unidad"]))
    print("\nDosis por tanque de 25 L. Una aspersion completa de Lisianthus son 4 tanques.")


def cmd_registrar(argv):
    if len(argv) < 6:
        raise SystemExit(
            'Uso: registrar <fecha> <semana> "<bloques>" <bomba_id> <tanques> '
            '[operario] ["motivo"]')
    # --camas "3 camas" marca una aplicacion DIRIGIDA: no se reparte al bloque
    camas = ""
    if "--camas" in argv:
        i = argv.index("--camas")
        camas = argv[i + 1] if len(argv) > i + 1 else ""
        argv = argv[:i] + argv[i + 2:]
    fecha, semana, bloques, bomba_id, tanques = argv[:5]
    operario = argv[5] if len(argv) > 5 else ""
    motivo = argv[6] if len(argv) > 6 else ""

    if not L.receta_bomba(bomba_id):
        raise SystemExit("La bomba %r no esta en bombas_catalogo.csv. "
                         "Agregala ahi primero, con sus dosis." % bomba_id)
    reconocidos = L.bloques_de(bloques)
    if not reconocidos:
        raise SystemExit("No reconozco ningun bloque en %r. Los validos salen de "
                         "area_camas.csv: %s" % (bloques, ", ".join(sorted(
                             set(L.alias_bloques().values())))))
    pendiente = tanques.strip().upper() in ("PENDIENTE", "SIN_DATO", "?")
    if pendiente:
        litros = None
    else:
        try:
            litros = float(tanques) * 25
        except ValueError:
            raise SystemExit("tanques tiene que ser un numero, o 'PENDIENTE' si "
                             "el operario todavia no reporta cuanto gasto.")

    ruta = os.path.join(L.DATOS, "aplicaciones_lote.csv")
    with open(ruta, encoding="utf-8") as f:
        cols = next(csv.reader(f))
    fila = dict.fromkeys(cols, "")
    fila.update(fecha=fecha, semana_iso=semana, anio=fecha[:4], bloque=",".join(reconocidos),
                bomba_id=bomba_id, tanques="" if pendiente else tanques,
                litros="" if pendiente else "%g" % litros,
                operario=operario, motivo=motivo, fuente="motor/bomba.py registrar")
    if "camas" in fila:
        fila["camas"] = camas
    with io.open(ruta, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=cols).writerow(fila)

    if pendiente:
        print("Registrada: sem %s · %s · %s · TANQUES PENDIENTE · %s" % (
            semana, ",".join(reconocidos), bomba_id, operario or "sin operario"))
        print("Cuando el operario reporte cuanto gasto:")
        print('  python3 motor/bomba.py tanques %s "%s" %s <tanques>' % (
            fecha, ",".join(reconocidos), bomba_id))
    else:
        print("Registrada: sem %s · %s · %s · %s tanques (%g L) · %s" % (
            semana, ",".join(reconocidos), bomba_id, tanques, litros, operario or "sin operario"))
    idx = L.ocupacion(tope_semana=int(semana))
    tocadas = set()
    for b in reconocidos:
        for coh, frac, exacto in L.reparto(b, int(semana), idx):
            tocadas.add((coh, exacto))
    if tocadas:
        print("Se le suma a:")
        for coh, exacto in sorted(tocadas):
            print("   %s%s" % (coh, "" if exacto else "   (reparto APROX: falta el area)"))
    else:
        print("OJO: ninguna siembra tiene ocupacion registrada en esos bloques esa semana,")
        print("asi que esta aplicacion no le suma a ninguna ficha. Revisa ocupacion_lote.csv.")


def cmd_tanques(argv):
    if len(argv) < 4:
        raise SystemExit('Uso: tanques <fecha> "<bloques>" <bomba_id> <tanques>')
    fecha, bloques, bomba_id, tanques = argv[:4]
    reconocidos = ",".join(L.bloques_de(bloques)) or bloques
    try:
        litros = float(tanques) * 25
    except ValueError:
        raise SystemExit("tanques tiene que ser un numero.")

    ruta = os.path.join(L.DATOS, "aplicaciones_lote.csv")
    with open(ruta, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    cols = list(filas[0].keys()) if filas else []
    candidatas = [f for f in filas
                  if f.get("fecha") == fecha and f.get("bloque") == reconocidos
                  and f.get("bomba_id") == bomba_id and not (f.get("tanques") or "").strip()]
    if not candidatas:
        raise SystemExit("No encontre una fila SIN tanques con fecha=%s bloque=%s bomba=%s. "
                         "Revisa con 'python3 motor/bomba.py rotacion' o el CSV directo." % (
                             fecha, reconocidos, bomba_id))
    if len(candidatas) > 1:
        raise SystemExit("Hay %d filas pendientes iguales (misma fecha/bloque/bomba) — "
                         "edita el CSV a mano para no ambiguar cual es cual." % len(candidatas))
    candidatas[0]["tanques"] = tanques
    candidatas[0]["litros"] = "%g" % litros
    with io.open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(filas)
    print("Actualizado: %s · %s · %s -> %s tanques (%g L)" % (
        fecha, reconocidos, bomba_id, tanques, litros))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    cmd = argv[1]
    if cmd == "semana":
        cmd_semana(int(argv[2]) if len(argv) > 2 else 37)
    elif cmd == "catalogo":
        cmd_catalogo()
    elif cmd == "registrar":
        cmd_registrar(argv[2:])
    elif cmd == "tanques":
        cmd_tanques(argv[2:])
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
