#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ficha completa de una variedad: ciclo, cosecha, venta, merma e inputs.

    python3 motor/ficha_completa.py Lisianthus
    python3 motor/ficha_completa.py            # lista los grupos disponibles

Es la mesa de "variedad por variedad" que pidio Vanessa el 2026-09-11. Once
secciones fijas, siempre las mismas, para que dos variedades se puedan comparar
sin tener que acordarse de que se miro en cada una:

     1  siembra: cuando, cuanto, donde
     2  ventana de cosecha DOCUMENTADA contra la REAL
     3  tallos registrados, semana por semana
     4  el pico productivo
     5  coincidencia entre la ventana esperada y la registrada
     6  venta: tallos y plata
     7  reparto por tipo de producto — bouquet, paquete, evento, otros
     8  merma: lo cosechado que no se vendio
     9  inputs fitosanitarios, cruzados contra la semana de ciclo
    10  decisiones de manejo registradas
    11  lo que falta para cerrar el margen

La regla de siempre: donde no hay dato, lo dice. Ninguna seccion se rellena con
supuestos, porque una ficha que inventa la mitad es peor que una que falta.
"""

import collections
import csv
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerebro as C
import ficha_variedad as F
import ocupacion as O

REGISTRO_ABRE = datetime.date(2026, 5, 31)


def _n(v):
    v = (v or "").strip().replace(".", "").replace(",", "")
    return int(v) if v.isdigit() else 0


def siembras(grupo):
    """Filas de campo_siembras que son de este grupo, con su semana y bloque."""
    crudas = O._filas_crudas()
    fechas = O._semanas_de_siembra(crudas)
    alias = C.alias_grupo(grupo)
    out = []
    for r, f in zip(crudas, fechas):
        def col(i):
            return (r[i] if len(r) > i else "").strip()
        nombre = col(13) + " " + col(2)
        if not any(a in C.norm(nombre) for a in alias):
            continue
        out.append({
            "variedad": col(2), "plantas": C.num(col(5)) or 0.0,
            "sem": col(7), "fecha": f, "bloque": col(8),
            "ini_mes": col(9), "ini_sem": col(10), "fin_sem": col(11),
            "comentario": col(12),
        })
    return out


def cosecha(grupo):
    """Tallos registrados de este grupo por semana ISO, bloque y variedad."""
    sem, blo, var = collections.Counter(), collections.Counter(), collections.Counter()
    for x in C._leer_csv("registro_tallos.csv"):
        if C.norm(x.get("Grupo") or "") != C.norm(grupo):
            continue
        f = (x.get("Fecha") or "").strip()
        if not f or not f[0].isdigit():
            continue
        t = _n(x.get("Tallos frescos")) + _n(x.get("Tallos secos"))
        d = datetime.date.fromisoformat(f)
        sem[d.isocalendar()[1]] += t
        blo[(x.get("Bloque") or "?").strip()] += t
        var[(x.get("Variedad / Serie") or "?").strip()] += t
    return sem, blo, var


def venta(grupo, ventana=None):
    """Tallos e ingreso de este grupo, por producto y por tipo de producto.

    `ventana` es (sem_ini, sem_fin) del registro de cosecha. La venta ANTERIOR
    a sem_ini no puede salir de esta cosecha — o es comprada, o es de un ciclo
    previo — asi que se devuelve aparte y NO se atribuye al grupo. Vanessa
    2026-09-11, sobre MADRES: *"mama de los suenos fue antes de que
    empezaramos a cosechar lisianthus. Esos lisianthus eran comprados.
    Entonces tu tienes que cruzarlo desde que empezamos a cosechar."*
    Es la misma regla que ya rige el area en ocupacion.py: el numerador y el
    denominador tienen que cubrir el mismo periodo.
    """
    productos, _ = C.cargar_recetas()
    por_nombre, por_grupo = C.cargar_paleta()
    recetas = {C.norm(p["producto"]): p for p in productos}
    alias = C.alias_grupo(grupo)
    por_prod = collections.defaultdict(lambda: [0.0, 0.0, 0.0])  # unid, tallos, $
    por_tipo = collections.defaultdict(lambda: [0.0, 0.0])
    previo = collections.defaultdict(lambda: [0.0, 0.0])  # unid, tallos — no es nuestro
    for v in C._leer_opcional("ventas_puntos.csv"):
        cant = C.num((v.get("cantidad") or "").strip()) or 0.0
        valor = C.num((v.get("valor_cobrado") or "").strip()) or 0.0
        if not cant:
            continue
        sem_v = C.num((v.get("semana_iso") or "").strip())
        antes = bool(ventana and sem_v and sem_v < ventana[0])
        p = recetas.get(C.norm(C.receta_de_producto(
            v.get("producto") or "", {k: k for k in recetas})))
        if not p:
            continue
        # cuantos tallos DCB pone este grupo, y cuantos en total
        mios = total = 0.0
        for it in p["ingredientes"]:
            if (it.get("origen") or "").lower().startswith("compr"):
                continue
            n = it.get("cant_max") or it.get("cant_min") or 0.0
            if not n:
                continue
            if C.resolver(it["ingrediente"], por_nombre, por_grupo)["tipo"] == "SUSTITUCION":
                continue
            total += n
            if any(a in C.norm(it["ingrediente"]) for a in alias):
                mios += n
        if not mios:
            continue
        if antes:
            previo[p["producto"]][0] += cant
            previo[p["producto"]][1] += mios * cant
            continue
        cat = (p.get("categoria") or "?").strip() or "?"
        por_prod[p["producto"]][0] += cant
        por_prod[p["producto"]][1] += mios * cant
        por_prod[p["producto"]][2] += valor * (mios / total) if total else 0
        por_tipo[cat][0] += mios * cant
        por_tipo[cat][1] += valor * (mios / total) if total else 0
    return por_prod, por_tipo, previo


def inputs_cohorte(grupo):
    """Lo que consumio esta cohorte, dictado por Vanessa y guardado por cohorte.

    Es la unica via para llenar la seccion 9: la fitosanidad de
    `aplicaciones_historial.csv` no trae el lote, y la preparacion de cama, el
    fertirriego y las labores culturales no tienen registro por lote en ningun
    archivo. Sin esto la seccion 9 solo puede listar lo que falta.
    """
    return [r for r in C._leer_opcional("inputs_cohorte.csv")
            if C.norm(grupo) in C.norm(r.get("cohorte") or "")]


def bombas(grupo):
    """Aplicaciones fitosanitarias cuyo destino nombra a este grupo."""
    alias = C.alias_grupo(grupo)
    out = collections.defaultdict(list)
    for a in C._leer_opcional("aplicaciones_historial.csv"):
        destino = C.norm(a.get("Destino (bloques/criterio)") or "")
        if not any(x in destino for x in alias):
            continue
        out[(a.get("Fecha"), a.get("Sem ISO"), a.get("Bomba / Grupo"),
             a.get("Objetivo"))].append(
            "%s %s (%s)" % (a.get("Producto"), a.get("Dosis/25L o /tanque"),
                            a.get("Función")))
    return out


def main(argv):
    ofe = C.oferta_registrada()
    roles = C.cargar_roles()
    dem = C.demanda_catalogo()
    grupos = sorted(set(roles) | set(dem["demanda"]) | set(ofe["tallos"]))
    if len(argv) < 2:
        print("Grupos disponibles:\n")
        for g in grupos:
            print("   %-22s %s tallos" % (
                g, "{:,.0f}".format(ofe["tallos"].get(g, 0)).replace(",", ".")))
        return
    pedido = " ".join(argv[1:])
    grupo = next((g for g in grupos if C.norm(pedido) in C.norm(g)), None)
    if not grupo:
        raise SystemExit("No encuentro el grupo %r. Corre sin argumentos para ver la lista." % pedido)

    ciclos = C.cargar_ciclos()
    cic = ciclos.get(C.norm(grupo)) or {}
    sb = siembras(grupo)
    sem, blo, var = cosecha(grupo)
    ventana_cos = (min(sem), max(sem)) if sem else None
    por_prod, por_tipo, previo = venta(grupo, ventana_cos)
    ap = bombas(grupo)
    inp = inputs_cohorte(grupo)
    areas, en_vent = F.area_por_grupo(grupos)

    L = "=" * 96
    print(L)
    print("FICHA COMPLETA — %s" % grupo.upper())
    print(L)
    rol = (roles.get(grupo, {}) or {})
    print("  rol de cartera: %s   |   registro de cosecha hasta: %s" % (
        rol.get("rol", "SIN_ROL"), ofe["corte"]))

    # ---- 1. SIEMBRA
    print("\n1. SIEMBRA — cuando, cuanto, donde")
    print("-" * 96)
    if not sb:
        print("   SIN SIEMBRAS registradas en campo_siembras.csv")
    else:
        tot = sum(s["plantas"] for s in sb)
        sin_pl = sum(1 for s in sb if not s["plantas"])
        print("   %-28s %8s %5s %-10s %6s %6s" % (
            "VARIEDAD", "PLANTAS", "SEM", "BLOQUE", "INI", "FIN"))
        for s in sorted(sb, key=lambda x: (x["sem"] or "")):
            print("   %-28s %8s %5s %-10s %6s %6s" % (
                s["variedad"][:28],
                "{:,.0f}".format(s["plantas"]).replace(",", ".") if s["plantas"] else "--",
                s["sem"] or "--", s["bloque"][:10] or "--",
                s["ini_sem"] or s["ini_mes"][:5] or "--", s["fin_sem"] or "--"))
        print("   %-28s %8s   (%d de %d filas SIN cantidad)" % (
            "TOTAL", "{:,.0f}".format(tot).replace(",", "."), sin_pl, len(sb)))

    # ---- 2. VENTANA documentada vs real
    print("\n2. VENTANA DE COSECHA — documentada contra real")
    print("-" * 96)
    doc_campo = cic.get("sem_a_campo_min"), cic.get("sem_a_campo_max")
    doc_vent = cic.get("ventana_min"), cic.get("ventana_max")
    semanas_sb = sorted({int(s["sem"]) for s in sb if (s["sem"] or "").isdigit()})
    if sem and semanas_sb:
        primera_siembra = min(semanas_sb)
        primera_cos, ultima_cos = min(sem), max(sem)
        real_a_cosecha = primera_cos - primera_siembra
        real_ventana = ultima_cos - primera_cos
        print("   ciclos_variedad.csv : a campo %s-%s sem   ventana %s-%s sem" % (
            doc_campo[0] or "?", doc_campo[1] or "?", doc_vent[0] or "?", doc_vent[1] or "?"))
        print("   REAL del registro   : a campo %d sem        ventana %d sem y contando" % (
            real_a_cosecha, real_ventana))
        if doc_campo[1] and real_a_cosecha < doc_campo[1]:
            print("   -> el ciclo REAL corrio %d semanas MAS RAPIDO que lo documentado"
                  % (doc_campo[1] - real_a_cosecha))
        if doc_vent[1] and real_ventana > doc_vent[1]:
            print("   -> la ventana REAL es %.1fx la documentada" % (real_ventana / doc_vent[1]))
        print("   OJO: la primera siembra y la primera cosecha registrada pueden ser de")
        print("   lotes distintos. Esto es una aproximacion de grupo, no de lote.")
    else:
        print("   SIN_DATO suficiente para comparar")

    # ---- 3 y 4. COSECHA y PICO
    print("\n3. COSECHA REGISTRADA — %s tallos" % "{:,.0f}".format(sum(sem.values())).replace(",", "."))
    print("-" * 96)
    if sem:
        mx = max(sem.values())
        for k in sorted(sem):
            barra = "#" * int(20 * sem[k] / mx)
            print("   sem %2d  %7s  %s%s" % (
                k, "{:,.0f}".format(sem[k]).replace(",", "."), barra,
                "   <- PICO" if sem[k] == mx else ""))
        pico = max(sem, key=lambda k: sem[k])
        print("\n4. PICO PRODUCTIVO: semana %d con %s tallos" % (
            pico, "{:,.0f}".format(sem[pico]).replace(",", ".")))
        ult = sorted(sem)[-3:]
        if len(ult) == 3 and sem[ult[0]] > sem[ult[1]] > sem[ult[2]]:
            print("   La cosecha viene CAYENDO las ultimas 3 semanas: %s" % " -> ".join(
                "{:,.0f}".format(sem[k]).replace(",", ".") for k in ult))
        print("\n   por BLOQUE:")
        for k, v in blo.most_common(6):
            print("     %-22s %7s" % (k[:22], "{:,.0f}".format(v).replace(",", ".")))
        if len(blo) > 3:
            print("     OJO: %d formas distintas de escribir el bloque — puede ser el mismo" % len(blo))
        print("\n   por CULTIVAR:")
        for k, v in var.most_common(6):
            print("     %-30s %7s" % (k[:30], "{:,.0f}".format(v).replace(",", ".")))
        if len(var) == 1 and "mix" in C.norm(list(var)[0]):
            print("     TODO registrado como Mix: no se puede saber que cultivar rinde.")
            print("     Campo tiene %d cultivares distintos sembrados de este grupo." % len(
                {s["variedad"] for s in sb}))
    else:
        print("   SIN COSECHA REGISTRADA")

    # ---- 5. COINCIDENCIA
    print("\n5. COINCIDENCIA VENTANA / REGISTRO")
    print("-" * 96)
    estado = []
    if sem:
        prim = ofe["primera"].get(grupo)
        ult = ofe["ultima"].get(grupo)
        if prim and prim <= REGISTRO_ABRE + datetime.timedelta(days=3):
            estado.append("TRUNCADA AL INICIO — la cosecha ya venia antes del %s" % REGISTRO_ABRE)
        corte = ofe["corte"]
        corte_d = corte if hasattr(corte, "year") else datetime.date.fromisoformat(str(corte))
        if ult and ult >= corte_d - datetime.timedelta(days=7):
            estado.append("ABIERTA AL CIERRE — seguia cosechando el dia del corte")
        con_fin = [s for s in sb if s["fin_sem"]]
        print("   siembras con fin de cosecha anotado: %d de %d" % (len(con_fin), len(sb)))
    print("   " + ("\n   ".join(estado) if estado else "ventana COMPLETA — se puede leer literal"))

    # ---- 6 y 7. VENTA
    tv = sum(v[1] for v in por_prod.values())
    ti = sum(v[2] for v in por_prod.values())
    print("\n6. VENTA — %s tallos, $%s de ingreso atribuido" % (
        "{:,.0f}".format(tv).replace(",", "."),
        "{:,.0f}".format(ti).replace(",", ".")))
    print("-" * 96)
    for k, (u, t, i) in sorted(por_prod.items(), key=lambda kv: -kv[1][1])[:12]:
        print("   %-38s %6.0f unid %7s tallos  $%s" % (
            k[:38], u, "{:,.0f}".format(t).replace(",", "."),
            "{:,.0f}".format(i).replace(",", ".")))

    if previo:
        pu = sum(v[0] for v in previo.values())
        pt = sum(v[1] for v in previo.values())
        print("\n   NO ATRIBUIDO — %.0f unidades, %s tallos vendidos ANTES de la semana %d,"
              % (pu, "{:,.0f}".format(pt).replace(",", "."), ventana_cos[0]))
        print("   que es la primera con cosecha registrada. No puede salir de esta cama:")
        print("   o se compro, o viene de un ciclo anterior que no quedo en el registro.")
        for k, (u, t_) in sorted(previo.items(), key=lambda kv: -kv[1][1])[:8]:
            print("     %-38s %6.0f unid %7s tallos" % (
                k[:38], u, "{:,.0f}".format(t_).replace(",", ".")))

    print("\n7. REPARTO POR TIPO DE PRODUCTO")
    print("-" * 96)
    for k, (t, i) in sorted(por_tipo.items(), key=lambda kv: -kv[1][0]):
        print("   %-24s %7s tallos (%2.0f%%)  $%s" % (
            k[:24], "{:,.0f}".format(t).replace(",", "."),
            100 * t / tv if tv else 0, "{:,.0f}".format(i).replace(",", ".")))

    # ---- 8. MERMA
    cos_tot = sum(sem.values())
    print("\n8. MERMA — lo cosechado que no aparece vendido")
    print("-" * 96)
    if cos_tot and tv:
        dif = cos_tot - tv
        print("   cosechado %s  -  vendido %s  =  %s tallos (%.0f%%)" % (
            "{:,.0f}".format(cos_tot).replace(",", "."),
            "{:,.0f}".format(tv).replace(",", "."),
            "{:+,.0f}".format(dif).replace(",", "."),
            100 * dif / cos_tot))
        print("   NO todo eso es perdida. Se reparte entre:")
        print("     - lo que se SECO y se vendio como forever (no se separa en el registro)")
        print("     - lo vendido despues del corte del registro")
        print("     - descarte real por calidad — que NO se mide: calidad_tallo.csv esta vacio")
        if dif < 0:
            print("   NEGATIVO: vende mas de lo cosechado -> falta registro de cosecha")
    else:
        print("   SIN_DATO")

    # ---- 9. INPUTS
    print("\n9. INPUTS — fitosanidad cruzada contra la semana de ciclo")
    print("-" * 96)
    if ap:
        prim_sb = min((int(s["sem"]) for s in sb if (s["sem"] or "").isdigit()), default=None)
        for (fecha, siso, bomba, obj), prods in sorted(ap.items()):
            rel = ""
            if prim_sb and siso and siso.isdigit():
                rel = "  (semana %d del ciclo)" % (int(siso) - prim_sb)
            print("   %s  sem %s  %s / %s%s" % (fecha, siso, bomba, obj, rel))
            for p in prods:
                print("        %s" % p)
    else:
        print("   Ninguna aplicacion de aplicaciones_historial.csv nombra a este grupo.")
        print("   El archivo tiene solo %d filas en total — no cubre el ciclo." % len(
            C._leer_opcional("aplicaciones_historial.csv")))
    print()
    if inp:
        print("   LO QUE CONSUMIO ESTA COHORTE (dictado, una fila por insumo):")
        cat = None
        for r in inp:
            if r["categoria"] != cat:
                cat = r["categoria"]
                print("     %s" % cat.replace("_", " "))
            marca = {"SI": "$", "PARCIAL": "~"}.get(r["costeable"], " ")
            det = " ".join(x for x in (r["cantidad"], r["unidad"]) if x)
            print("      %s %-32s %-13s %s" % (
                marca, r["input"][:32], det[:13], r["frecuencia"][:28]))
        n = sum(1 for r in inp if r["costeable"] == "SI")
        print("     ($ ya tiene precio por m2 · ~ parcial · en blanco falta el precio)")
        print("     %d de %d renglones se pueden costear hoy." % (n, len(inp)))
        print("")

    print("   LO QUE NO SE PUEDE ATRIBUIR A ESTA VARIEDAD, y por que:")
    print("     preparacion de cama   no hay registro por lote (ni horas ni insumo)")
    print("     fertilizacion         falta litros de tanque por m2 por bloque — bloqueo 4b")
    print("     trabajo cultural      solo aparece suelto en COMENTARIOS, sin horas")
    print("     luces                 no existe registro de horas de luz en el repositorio")

    # ---- 10. DECISIONES
    print("\n10. DECISIONES DE MANEJO REGISTRADAS")
    print("-" * 96)
    alias = C.alias_grupo(grupo)
    hay = False
    for d in C._leer_opcional("decisiones_manejo.csv"):
        txt = C.norm((d.get("Decisión") or "") + " " + (d.get("Razón") or ""))
        if any(a in txt for a in alias):
            hay = True
            print("   %s sem %s: %s" % (d.get("Fecha"), d.get("Sem ISO"),
                                        (d.get("Decisión") or "")[:70]))
    coment = [s for s in sb if s["comentario"]]
    if coment:
        hay = True
        print("   De los COMENTARIOS de campo:")
        for s in coment[:6]:
            print("     %-22s %s" % (s["variedad"][:22], s["comentario"][:60]))
    if not hay:
        print("   ninguna")

    # ---- 11. LO QUE FALTA
    print("\n11. PARA CERRAR EL MARGEN DE ESTA VARIEDAD")
    print("-" * 96)
    area = areas.get(grupo)
    campo = cic.get("sem_a_campo_max") or cic.get("sem_a_campo_min")
    vent = cic.get("ventana_max") or cic.get("ventana_min")
    semocup = (campo + vent) if (campo and vent) else None
    if area and semocup and ti:
        print("   area en ventana %.1f m2  |  %d sem de cama  |  $%s/m2/sem de INGRESO" % (
            area, semocup, "{:,.0f}".format(ti / (area * semocup)).replace(",", ".")))
    print("   FALTA: costo de semilla, de insumo y de mano de obra por lote.")
    print("   El modelo de costos existe y tiene 2026 cargado; su unico campo manual")
    print("   —'Tallos vendidos en el mes'— esta en 0 en los doce meses.")
    print("   Y la calidad no se mide: sin calidad_tallo.csv no se separa 'produjo'")
    print("   de 'produjo vendible'.")
    print()


if __name__ == "__main__":
    main(sys.argv)
