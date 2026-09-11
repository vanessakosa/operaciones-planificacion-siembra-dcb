#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ficha de completitud por grupo: que se puede decidir hoy de cada uno.

    python3 motor/ficha_variedad.py            # la tabla completa
    python3 motor/ficha_variedad.py faltantes  # solo lo que hay que traer

POR QUE ESTE SCRIPT EXISTE
--------------------------
Vanessa 2026-09-10, sobre para que sirve esta mesa: "vamos a evaluar variedad
por variedad. Si nos esta dando la rentabilidad, segun el registro de tallos,
que estamos esperando si se esta vendiendo, si esta aportando y ver cuales son
los huecos de siembras y los sobrantes para ajustar la programacion."

Son CUATRO preguntas, no una, y tienen salud de datos muy distinta. Este script
no las contesta: audita, grupo por grupo, cual se puede contestar hoy y con que.

    1. RENTA   da rentabilidad?        tallos x precio - costo, por m2 y semana
    2. VENTA   se esta vendiendo?      lo cosechado contra lo que salio
    3. APORTA  esta aportando?         lo pide el catalogo, y en que rol
    4. AJUSTE  huecos y sobrantes?     para mover la programacion

La regla es no rellenar con supuestos. Un margen inventado manda a arrancar una
cama que estaba dando plata, y un "se vende bien" sin dato manda a sembrar mas
de lo que nadie pidio. Lo que falta se marca FALTA y se pide.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerebro as C


def plantas_por_grupo(grupos):
    """Cantidad trasplantada, sumada por grupo, desde campo_siembras."""
    tot, lotes, con_dato = {}, {}, {}
    ordenados = sorted(grupos, key=lambda g: -len(g))
    for fila in C._leer_csv("campo_siembras.csv"):
        nombre = " ".join([(fila.get("Nombre Homologados") or ""),
                           (fila.get("Variedad") or "")])
        # Por ALIAS, no por el nombre del grupo: CAMPO escribe "Snapdragon" en
        # ingles y el grupo se llama "Boca de Dragón". Sin esto, el grupo de
        # mas volumen del cultivo salia con cero plantas. Ver
        # ocupacion.emparejar_grupo, que documenta el caso completo.
        n = C.norm(nombre)
        g = next((x for x in ordenados
                  if any(a in n for a in C.alias_grupo(x))), None)
        if not g:
            continue
        lotes[g] = lotes.get(g, 0) + 1
        p = C.num((fila.get("Cantidad Trasplantada") or "").strip())
        if p:
            tot[g] = tot.get(g, 0) + p
            con_dato[g] = con_dato.get(g, 0) + 1
    return tot, lotes, con_dato


def ingreso_por_grupo():
    """Ingreso atribuible a cada grupo, repartiendo el precio del producto
    entre sus tallos DCB. Es ingreso, no margen: no hay costo que restar.

    Se resuelve ingrediente por ingrediente, igual que demanda_catalogo(): un
    ingrediente SUSTITUIBLE ("Trachelium o Ammi") NO se suma a ninguno de los
    dos, porque sumarlo a ambos inflaria los dos.
    """
    por_nombre, por_grupo = C.cargar_paleta()
    productos, _ = C.cargar_recetas()
    ing, tallos = {}, {}
    for p in productos:
        a = C.analizar_producto(p, por_nombre, por_grupo)
        if not a["tallos_dcb"] or not a["precio"]:
            continue
        unit = a["precio"] / a["tallos_dcb"]
        for it in p["ingredientes"]:
            if (it["origen"] or "").lower().startswith("compr"):
                continue
            cant = it["cant_max"] or it["cant_min"] or 0.0
            if not cant:
                continue
            res = C.resolver(it["ingrediente"], por_nombre, por_grupo)
            if res["tipo"] in ("SUSTITUCION", "NO_FLOR"):
                continue
            g = None
            if res["tipo"] == "EXACTA" and res["reg"]:
                g = res["reg"].get("grupo")
            elif res.get("grupo"):
                g = res["grupo"]
            if not g:
                continue
            ing[g] = ing.get(g, 0) + unit * cant
            tallos[g] = tallos.get(g, 0) + cant
    return {g: ing[g] / tallos[g] for g in ing if tallos.get(g)}


def _por_grupo_desde(archivo, grupos, campo_variedad="variedad"):
    """Agrupa las filas de un CSV de senales por grupo de cartera.

    Los archivos de senales (desajuste_demanda, picos_cosecha) nombran la
    VARIEDAD como la escribio campo — "Snapdragon Monaco Dark Pink" — no el
    grupo. Se emparejan por alias, igual que las plantas: sin eso las nueve
    filas de Snapdragon no llegan a Boca de Dragón.
    """
    ordenados = sorted(grupos, key=lambda g: -len(g))
    salida = {}
    for f in C._leer_opcional(archivo):
        v = f.get(campo_variedad) or ""
        n = C.norm(v)
        g = next((x for x in ordenados
                  if any(a in n for a in C.alias_grupo(x))), None)
        if not g:
            continue
        salida.setdefault(g, []).append(f)
    return salida


def venta_cuantitativa():
    """Cuantos tallos VENDIDOS hay registrados, por grupo.

    Existe para dejar constancia de que la pregunta 2 no tiene numerador. En
    campo_siembras.csv hay cuatro columnas para esto y las cuatro estan vacias:

        idx14  Tallos vendidos                    0 de 302
        idx18  Ventas WIX                         0 de 302
        idx19  Utilidad                           0 de 302
        idx20  Ventas por tallos calculados MG    0 de 302

    Asi que "se esta vendiendo" hoy solo se puede responder con las senales
    cualitativas que quedaron en los COMENTARIOS, ya extraidas a
    desajuste_demanda.csv. El esqueleto de la columna esta; el dato no.
    """
    cols = ("Tallos vendidos", "Ventas WIX", "Utilidad",
            "Ventas por tallos calculados MG")
    tot = {c: 0 for c in cols}
    for f in C._leer_csv("campo_siembras.csv"):
        for c in cols:
            if (f.get(c) or "").strip():
                tot[c] += 1
    # El archivo propio del despacho, que es el que deberia mandar cuando se
    # empiece a llenar: una fila por variedad y semana, del lado de la SALIDA.
    # Se cuenta aparte para que la pregunta 2 pase a SI sola en cuanto tenga
    # filas, sin que haya que volver a tocar este script.
    desp = [f for f in C._leer_opcional("tallos_despachados.csv")
            if (f.get("tallos_despachados") or "").strip()]
    tot["tallos_despachados.csv (filas)"] = len(desp)
    return tot


def area_por_grupo(grupos):
    """Area en m2 recortada a la ventana del registro, por grupo.

    Se delega en ocupacion.py, que es donde vive el recorte por ventana. El
    import es tardio a proposito: ocupacion importa este modulo, y a nivel de
    modulo seria una importacion circular.
    """
    try:
        import ocupacion as O
    except Exception:
        return {}, {}
    ciclos = C.cargar_ciclos()
    ofe = C.oferta_registrada()
    ventana_de = {g: (ofe["primera"][g], ofe["ultima"][g])
                  for g in ofe["primera"] if g in ofe["ultima"]}
    en_vent, _, _ = O.plantas_en_ventana(grupos, ciclos, ventana_de)
    areas = {}
    for g, pl in en_vent.items():
        dist = (ciclos.get(C.norm(g)) or {}).get("distancia_cm")
        if dist and pl:
            areas[g] = pl * O.MALLA_M * (dist / 100.0)
    return areas, en_vent


def venta_por_grupo(grupos):
    """Tallos VENDIDOS por grupo, bajando de producto a variedad por receta.

    La venta se registra por PRODUCTO ("Cosecha Grande", "Bocas de dragon"), no
    por tallo. Para llegar a la variedad hay que explotar cada producto vendido
    con su receta, igual que hace `cerebro.py explotar` con la demanda.

    Devuelve (tallos_por_grupo, unidades_con_receta, unidades_totales,
    productos_sin_receta) — las tres ultimas para poder decir CUANTA de la venta
    quedo fuera del cruce, que es la mitad del diagnostico.
    """
    ventas = C._leer_opcional("ventas_puntos.csv")
    if not ventas:
        return {}, 0.0, 0.0, {}
    productos, _ = C.cargar_recetas()
    por_nombre, por_grupo = C.cargar_paleta()
    recetas = {C.norm(p["producto"]): p for p in productos}
    ordenados = sorted(grupos, key=lambda g: -len(g))

    tallos, con, tot, sin = {}, 0.0, 0.0, {}
    for v in ventas:
        cant = C.num((v.get("cantidad") or "").strip()) or 0.0
        if not cant:
            continue
        tot += cant
        nom = C.norm(v.get("producto_receta") or "")
        p = recetas.get(nom)
        if not p:
            sin[v.get("producto") or "?"] = sin.get(v.get("producto") or "?", 0.0) + cant
            continue
        con += cant
        for it in p["ingredientes"]:
            if (it.get("origen") or "").lower().startswith("compr"):
                continue
            n = it.get("cant_max") or it.get("cant_min") or 0.0
            if not n:
                continue
            res = C.resolver(it["ingrediente"], por_nombre, por_grupo)
            if res["tipo"] in ("SUSTITUCION", "NO_FLOR"):
                continue
            texto = C.norm(it["ingrediente"])
            g = next((x for x in ordenados
                      if any(a in texto for a in C.alias_grupo(x))), None)
            if g:
                tallos[g] = tallos.get(g, 0.0) + n * cant
    return tallos, con, tot, sin


def venta_invisible(grupos, sin_receta):
    """Unidades vendidas de productos SIN receta cuyo nombre nombra al grupo.

    Es la salvaguarda mas importante de esta tabla. El %VTA sale de explotar
    los productos vendidos con su receta, y hoy solo 25 de 121 productos
    vendidos tienen una. Un grupo cuyos productos estrella no estan recetados
    aparece vendiendo casi nada — y la conclusion natural, arrancarlo, seria
    exactamente la equivocada.

    El caso que obliga a esto: Lisianthus figura con 76 tallos vendidos contra
    6.926 cosechados, un 1%. Pero "Edicion Especial Lisianthus" vendio 189
    unidades sin receta y es de lo mas vendido del cultivo. Ese 1% mide el
    catalogo, no la venta.

    No convierte a tallos: sin receta no se sabe cuantos tallos lleva cada
    unidad. Cuenta UNIDADES, que es lo unico que se puede afirmar.
    """
    ordenados = sorted(grupos, key=lambda g: -len(g))
    inv = {}
    for prod, cant in sin_receta.items():
        n = C.norm(prod)
        for g in ordenados:
            if any(a in n for a in C.alias_grupo(g)):
                inv.setdefault(g, {"unidades": 0.0, "productos": []})
                inv[g]["unidades"] += cant
                inv[g]["productos"].append((prod, cant))
                break
    return inv


def main(argv):
    solo_faltantes = len(argv) > 1 and argv[1].startswith("falt")

    roles = C.cargar_roles()
    dem = C.demanda_catalogo()
    ofe = C.oferta_registrada()
    ciclos = C.cargar_ciclos()

    grupos = sorted(set(roles) | set(dem["demanda"]) | set(ofe["tallos"]))
    plantas, lotes, lotes_con_planta = plantas_por_grupo(grupos)
    try:
        ingreso = ingreso_por_grupo()
    except Exception:
        ingreso = {}
    areas, en_vent = area_por_grupo(grupos)
    desaj = _por_grupo_desde("desajuste_demanda.csv", grupos)
    picos = _por_grupo_desde("picos_cosecha.csv", grupos)
    vq = venta_cuantitativa()
    vend, uni_con, uni_tot, sin_receta = venta_por_grupo(grupos)
    invis = venta_invisible(grupos, sin_receta)
    vts2 = C._leer_opcional("ventas_puntos.csv")
    nprod = len({v.get("producto") for v in vts2})
    hay_venta_cuant = bool(vend)

    print("=" * 100)
    print("FICHA POR GRUPO — cual de las cuatro preguntas se puede contestar")
    print("=" * 100)
    print()
    print("  1 RENTA   da rentabilidad?     tallos x precio - costo, por m2 y por semana")
    print("  2 VENTA   se esta vendiendo?   lo cosechado contra lo que salio")
    print("  3 APORTA  esta aportando?      lo pide el catalogo, y en que rol")
    print("  4 AJUSTE  huecos y sobrantes?  para mover la programacion")
    print()
    print("  SI = se puede decidir   ~ = solo cualitativo, sin numero   NO = falta el dato")
    print()
    print("%-19s %-6s %7s %7s %5s %8s %7s  %-5s %-5s %-6s %-6s  %s" % (
        "GRUPO", "ROL", "COSECHO", "VENDIDO", "%VTA", "AREA m2", "PLANTAS",
        "RENTA", "VENTA", "APORTA", "AJUSTE", "QUE LE FALTA"))
    print("-" * 110)

    faltan = {"costo": [], "venta": [], "ciclo": [], "planta": [],
              "precio": [], "calidad": [], "area": [], "distancia": []}
    cuenta = {"renta": 0, "venta": 0, "aporta": 0, "ajuste": 0}

    for g in grupos:
        rol = (roles.get(g, {}) or {}).get("rol", "") or "SIN_ROL"
        d = dem["demanda"].get(g, 0)
        o = ofe["tallos"].get(g, 0)
        cic = ciclos.get(C.norm(g)) or {}
        tiene_ciclo = bool(cic.get("sem_a_campo_min"))
        tiene_dist = bool(cic.get("distancia_cm"))
        pl = plantas.get(g, 0)
        area = areas.get(g)
        val = ingreso.get(g)

        # 1 RENTA — el costo no existe para ningun grupo, asi que ninguno llega
        # a SI. Lo que ya se puede es el INGRESO por m2 por semana, que es media
        # respuesta: ordena, pero no dice si da perdida.
        tiene_costo = False
        if val and area and tiene_ciclo:
            renta = "~"          # ingreso/m2/sem si; margen no
        elif o:
            renta = "NO"
        else:
            renta = "NO"

        # 2 VENTA — sin tallos vendidos no hay numerador. Queda la senal
        # cualitativa de los COMENTARIOS, que para varios grupos es explicita
        # ("no tengo a quien venderselo").
        sen_venta = [f for f in desaj.get(g, [])
                     if (f.get("tipo") or "") in ("sobra", "falta", "calidad_venta")]
        vt = vend.get(g)
        if vt:
            venta = "SI"
        elif sen_venta:
            venta = "~"
        else:
            venta = "NO"

        # 3 APORTA — el catalogo lo pide, o tiene rol asignado. Es la pregunta
        # mas sana de las cuatro: se contesta con lo que ya esta en el repo.
        aporta = "SI" if (d or rol != "SIN_ROL") else "NO"

        # 4 AJUSTE — para mover la programacion hacen falta las dos puntas:
        # saber si sobra o falta (demanda contra cosecha) y saber cuando
        # sembrar (ciclo). Con senal de campo o pico, mejor.
        if (d or o) and tiene_ciclo:
            ajuste = "SI"
        elif d or o:
            ajuste = "~"
        else:
            ajuste = "NO"

        for k, v in (("renta", renta), ("venta", venta),
                     ("aporta", aporta), ("ajuste", ajuste)):
            if v == "SI":
                cuenta[k] += 1

        f = []
        iv = invis.get(g)
        if iv:
            f.append("OJO %.0f unid sin receta" % iv["unidades"])
        if not tiene_costo:
            f.append("costo"); faltan["costo"].append(g)
        if not hay_venta_cuant:
            faltan["venta"].append(g)
            if not sen_venta:
                f.append("venta")
        if not tiene_ciclo:
            f.append("ciclo"); faltan["ciclo"].append(g)
        if not tiene_dist:
            f.append("distancia"); faltan["distancia"].append(g)
        if not pl:
            f.append("plantas"); faltan["planta"].append(g)
        if not val:
            f.append("precio"); faltan["precio"].append(g)
        if not area:
            faltan["area"].append(g)
        faltan["calidad"].append(g)

        if solo_faltantes and not f:
            continue

        print("%-19s %-6s %7.0f %7s %5s %8s %7s  %-5s %-5s %-6s %-6s  %s" % (
            g[:19], rol[:6], o,
            ("{:,.0f}".format(vt).replace(",", ".") if vt else "--"),
            ("%.0f%%" % (100 * vt / o)) if (vt and o) else "--",
            ("%.1f" % area) if area else "--",
            ("{:,.0f}".format(pl).replace(",", ".") if pl else "--"),
            renta, venta, aporta, ajuste, ", ".join(f) or "nada"))

    if invis:
        vts = C._leer_opcional("ventas_puntos.csv")
        print()
        print("!" * 110)
        print("EL %VTA NO SE PUEDE LEER LITERAL — la venta se registra por PRODUCTO,")
        print("y solo %d de %d productos vendidos tienen receta (%.0f%% de las unidades)."
              % (len({v.get("producto_receta") for v in vts if v.get("producto_receta")}),
                 len({v.get("producto") for v in vts}),
                 100 * uni_con / uni_tot if uni_tot else 0))
        print("Un grupo cuyos productos estrella no estan recetados aparece vendiendo")
        print("casi nada. Arrancarlo por eso seria el error mas caro posible.")
        print()
        print("  %-19s %8s  %s" % ("GRUPO", "UNID", "vendidas bajo productos SIN receta"))
        print("  " + "-" * 104)
        for g in sorted(invis, key=lambda x: -invis[x]["unidades"]):
            d = invis[g]
            top = sorted(d["productos"], key=lambda x: -x[1])[:3]
            print("  %-19s %8.0f  %s" % (
                g[:19], d["unidades"],
                " | ".join("%s (%.0f)" % (p[:32], c) for p, c in top)))
        print()
        print("  Y al reves: un %VTA SOBRE 100 no es un milagro, es un hueco del")
        print("  REGISTRO DE COSECHA. Larkspur figura vendiendo mas de lo cosechado")
        print("  porque su ventana registrada son dos dias.")
        print("!" * 110)
        print()
    n = len(grupos)
    print()
    print("=" * 100)
    print("VEREDICTO POR PREGUNTA")
    print("=" * 100)
    print()
    print("  3 APORTA  — SE PUEDE en %d de %d grupos." % (cuenta["aporta"], n))
    print("     Es la mas sana: sale del catalogo y de roles_cartera.csv, que ya estan.")
    print("     `cerebro.py cartera` la contesta grupo por grupo.")
    print()
    print("  4 AJUSTE  — SE PUEDE en %d de %d grupos." % (cuenta["ajuste"], n))
    print("     Demanda contra cosecha da el balance, y el ciclo da cuando sembrar.")
    print("     Ya hay 13 senales de campo extraidas en desajuste_demanda.csv y")
    print("     %d picos de cosecha en picos_cosecha.csv." % sum(len(v) for v in picos.values()))
    print("     ADVERTENCIA: el registro corta el %s, asi que un grupo puede" % ofe["corte"])
    print("     verse corto solo porque su cosecha todavia no esta anotada.")
    print()
    print("  1 RENTA   — SE PUEDE en %d de %d grupos. Falta UNA cosa: el COSTO."
          % (cuenta["renta"], n))
    print("     Ya corre la mitad: `ocupacion.py` da INGRESO por m2 por semana de")
    print("     cama, con el area recortada a la ventana del registro. Lo que no")
    print("     se puede es restarle el costo, y por eso no dice si algo da perdida.")
    print("     Lo desbloquea la fila 'Tallos vendidos en el mes' de DCB_Modelo_Costos:")
    print("     doce numeros, unico campo manual, en 0 en los doce meses. El modelo")
    print("     ya tiene los costos de 2026 cargados.")
    print()
    print("  2 VENTA   — SE PUEDE en %d de %d grupos, y desde el 2026-09-11."
          % (cuenta["venta"], n))
    print("     La venta NO vive en este repositorio: vive en Drive, en una hoja")
    print("     por PUNTO DE VENTA, en la cuenta poscdreamscanbloom. Espejadas a")
    print("     07-datos/ventas_puntos.csv con motor/importar_ventas.py:")
    print("     %d ventas, %.0f unidades, %d productos." % (len(vts2), uni_tot, nprod))
    print()
    print("     Las cuatro columnas de venta de campo_siembras.csv siguen vacias")
    print("     y NO son la fuente — la fuente son las hojas de punto:")
    for c, k in vq.items():
        if c.endswith("(filas)"):
            print("       %-34s %3d filas" % (c, k))
        else:
            print("       %-34s %3d de 302" % (c, k))
    print()
    print("     EL LIMITE AHORA ES OTRO, y es el catalogo: la venta se registra")
    print("     por PRODUCTO y solo el %.0f%% de las unidades tiene receta, asi que"
          % (100 * uni_con / uni_tot if uni_tot else 0))
    print("     el resto no se puede bajar a tallos. Ver la advertencia de arriba.")
    print()
    print("     Las 13 senales cualitativas de desajuste_demanda.csv siguen")
    print("     valiendo: dicen POR QUE sobro o falto, que el numero no dice.")
    con_senal = sorted((g for g in grupos if desaj.get(g)),
                       key=lambda g: -len(desaj[g]))
    for g in con_senal:
        tipos = {}
        for fila in desaj[g]:
            t = fila.get("tipo") or "?"
            tipos[t] = tipos.get(t, 0) + 1
        print("       %-19s %s" % (g[:19], ", ".join(
            "%s x%d" % (t, k) for t, k in sorted(tipos.items()))))
    print()
    print("=" * 100)
    print("LO QUE FALTA DEL ESQUELETO, ORDENADO POR LO QUE DESBLOQUEA")
    print("=" * 100)
    print()
    print("  1. TALLOS DESPACHADOS por variedad y semana — NO EXISTE EL ARCHIVO.")
    print("     Es la pregunta 2 entera. Sin esto, 'se esta vendiendo' se contesta")
    print("     de memoria. El registro de cosecha ya tiene la forma exacta que")
    print("     haria falta (fecha, grupo, variedad, cantidad): seria su gemelo")
    print("     del lado de la salida. Es tambien lo que convierte el sobrante de")
    print("     'sobra' en un numero en vez de una impresion.")
    print()
    print("  2. 'Tallos vendidos en el mes' en DCB_Modelo_Costos — doce numeros.")
    print("     Es la pregunta 1. Ya esta todo lo demas.")
    print()
    print("  3. calidad_tallo.csv — VACIO (0 filas, 16 columnas).")
    print("     El esqueleto esta, el dato no. Separa 'produjo' de 'produjo")
    print("     vendible': un grupo con mucho volumen y descarte alto se ve")
    print("     rentable y no lo es. Afecta a las preguntas 1 y 2 a la vez.")
    print()
    print("  4. distancia de siembra de %d grupos — bloquea su area, y con ella"
          % len(faltan["distancia"]))
    print("     su ocupacion: %s%s" % (", ".join(faltan["distancia"][:8]),
                                  " ... y %d mas" % (len(faltan["distancia"]) - 8)
                                  if len(faltan["distancia"]) > 8 else ""))
    print("     El caso mas caro es Celosia: su distancia depende del subtipo")
    print("     (cristata 7,5 cm, plumosa 15) y el grupo no tiene una sola.")
    print()
    print("  5. precio por tallo de %d grupos — sin el no entran al eje de plata:"
          % len(faltan["precio"]))
    print("     %s%s" % (", ".join(faltan["precio"][:8]),
                       " ... y %d mas" % (len(faltan["precio"]) - 8)
                       if len(faltan["precio"]) > 8 else ""))
    print()
    print("  Lo que SI esta y sirve hoy:")
    print("    * cosecha real de %d grupos, hasta el %s" % (
        len(ofe["tallos"]), ofe["corte"]))
    print("    * area recortada a la ventana de %d grupos" % len(areas))
    print("    * ingreso por tallo propio de %d grupos" % len(ingreso))
    print("    * ciclo y ventana de %d grupos" % sum(
        1 for g in grupos if (ciclos.get(C.norm(g)) or {}).get("sem_a_campo_min")))
    print("    * plantas trasplantadas de %d grupos (%d lotes con el dato)" % (
        len(plantas), sum(lotes_con_planta.values())))
    print("    * rol de cartera, cadencia y alternancia de %d grupos" % len(roles))
    print()


if __name__ == "__main__":
    main(sys.argv)
