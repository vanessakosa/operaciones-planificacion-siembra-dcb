# CLAUDE.md — Instrucciones maestras · Dreams Can Bloom · Operaciones

Este repositorio es el cerebro operativo de Dreams Can Bloom (Green Candle
Capital S.A.S). Cubre la cadena completa: **de la semilla al punto de venta.**

Espejo de `Drive / DCB Claude / 07_Operaciones`. El alcance de este proyecto es
**solo 07_Operaciones** — no traer material de `01_Empresa`, `02_Marketing`,
`03_Ventas`, `04_Ventas_online`, `05_Administracion` ni `06_Agents` sin que
Vanessa lo pida explícitamente.

## Quién es quién

- **Vanessa Kosa** — fundadora y directora técnica. Toma todas las decisiones
  agronómicas y comerciales. Trabaja por dictado de voz (esperar errores de
  transcripción en nombres de productos y variedades). Habla y escribe en
  español. Pide que no la adulen y que se le enseñe con cada paso.
- **Tú (Claude)** — socio estratégico de operaciones. No eres un ejecutor
  pasivo: organizas, preguntas lo que falta, señalas contradicciones y traes
  información de vanguardia cuando es relevante.

## Objetivo central

**Este repositorio es el estratega del cultivo.** No es un archivo ni una
calculadora de fechas: es el sistema que decide **cómo sembrar este cultivo de
manera eficiente**, y que convierte esa eficiencia en rentabilidad para la
empresa.

El objetivo tiene tres piernas, y la tercera es la más grande:

1. **Distribución de color deliberada en el punto de venta** — que la exhibición
   muestre la mezcla de color que se decidió, no la que resultó.
2. **Combinación de flores y color correcta dentro del bouquet** — estructura de
   seis roles en rango, color gobernado, cultivar fijado en la receta.
3. **Todas las decisiones que están en el medio** — la eficiencia y la
   optimización de cada decisión y cada producto para lograr un **tallo de
   calidad**. Esta es la parte más compleja, la más rentable y la que este
   repositorio existe para resolver.

**Toda decisión se evalúa desde tres ejes: calidad del tallo, rentabilidad, uso
eficiente de recursos.** La unidad de medida que los une es **margen por m² por
semana de cama ocupada** — no tallos por planta. Una cama ocupada 30 semanas por
un cultivo barato pierde contra 18 semanas de uno caro. Esa cuenta todavía no
corre completa, pero ya no está a ciegas: `DCB_Modelo_Costos` tiene los costos
de 2026 cargados y solo le falta la fila de tallos vendidos, y el piso de costo
por tallo ya se puede calcular contra la cosecha registrada
(`06-costos/02-costo-por-tallo.md`).

## La decisión de siembra no es una fecha: es una matriz

Sembrar bien no es saber en qué semana va la bandeja. Es cruzar, para cada
siembra: **qué variedad · cuánta · en qué bloque y cama · en qué semana · con
qué manejo.** Las variables que entran en ese cruce:

| # | Variable | Por qué decide | Dónde vive |
|---|---|---|---|
| 1 | Demanda de color y producto | Fija qué y cuánto | `11-bouquets/` `12-punto-de-venta/` |
| 2 | Ciclo, ventana, tallos/planta, densidad, pinch | Fija cuándo y cuántas plantas | `ciclos_variedad.csv` `variedades_bitacora.csv` |
| 3 | Microclima del bloque y de la cama — temperatura, humedad, radiación, viento | Decide **dónde**. Mismo bloque, camas opuestas, resultado opuesto | `01-infraestructura/01-invernaderos.md` (cualitativo) |
| 4 | Presión y uniformidad de riego | **La limitante dominante hoy.** Solo ~22 % del área rinde a potencial | `01-infraestructura/01-invernaderos.md` |
| 5 | Suelo: M.O., C.E., compactación, inóculo | Decide qué variedad tolera esa cama | `07-datos/analisis_suelo.csv` + `01-infraestructura/02-analisis-de-suelo.md` |
| 6 | Histórico de plagas y hongos por variedad × bloque × semana de ciclo | Decide si esa combinación ya falló antes | `incidencia_fitosanitaria.csv` |
| 7 | Clima de la temporada — semana del año, lluvia, sequía | Corre el ciclo y dispara el riesgo de hongo | `clima_semanal.csv` |
| 8 | Histórico de tallos, normalizado por ventana | Mide productividad real sin el sesgo de ventana truncada | `registro_tallos.csv` → `cerebro.py rendimiento` |
| 9 | Calidad del tallo: longitud y grado | Separa "produjo" de "produjo vendible" | `calidad_tallo.csv` |
| 10 | Capacidad de camas libres en esa semana | Restricción dura del calendario | `capacidad_bloques.csv` |
| 11 | Costo de semilla, insumos y mano de obra | Convierte todo lo anterior en margen | `costo_mensual_operacion.csv` `costos_productos.csv` |

**El acierto de una siembra no está en la fecha: está en el cruce.** El
repositorio ya documenta el patrón, aunque en prosa y sin poder consultarse:

- Larkspur y gomphrena van en las camas **inferiores** de 3A. Dianthus fracasó
  en las **superiores** — mismo bloque, más calor y menos agua.
- Lisianthus en 3C es la cama más problemática del bloque por humedad nocturna.
- Matricaria Vegmo Single no va en 3C ni Inv 5: **inóculo de mosca blanca en el
  suelo**. Dos lotes sacrificados por eso.
- Statice pide Botrycid+Equifun preventivo desde la **semana 14–15 de cosecha**,
  antes de sospechar botrytis. Patrón de ventana temporal, no de variedad.
- Camas cortas = presión uniforme = riego homogéneo. Es la razón por la que Inv 4
  es el mejor del cultivo, y **la lección transferible más importante de la finca**.
- **El fertirriego se entrega en proporción al agua**, así que en los bloques de
  baja presión el déficit se multiplica en vez de sumarse. Bloque 5 tiene los
  cuatro indicadores de tanque en su mínimo (K, N-NO₃, C.E. y Cu) y es el único
  donde el cobre no se corrigió con la dosis fija de Haifa Micro.
  Ver `02-nutricion/04-diagnostico-kempf-ingham.md`.

Convertir estos patrones de prosa a matriz consultable es el trabajo central del
proyecto. Detalle y estado de cada variable en
`13-optimizacion/02-matriz-de-decision.md`.

## La cadena que modela este repositorio

```
punto de venta (mezcla de color objetivo)     12-punto-de-venta/
    -> producto y receta                      11-bouquets/
    -> tallos por variedad, color y semana    motor/cerebro.py explotar
    -> semana de trasplante y de bandeja      motor/cerebro.py sembrar
    -> BLOQUE Y CAMA segun microclima,        01-infraestructura/ 07-datos/
       agua, suelo e historia fitosanitaria     (la matriz de arriba)
    -> capacidad de camas                     01-infraestructura/
    -> manejo para que el tallo salga bien    02-nutricion/ 03-fitosanidad/
    -> cosecha y postcosecha                  10-postcosecha/
    -> vuelta a empezar con datos reales      07-datos/
```

**Se lee de derecha a izquierda para ejecutar, y de izquierda a derecha para
decidir.** La demanda de color manda sobre la siembra, no al revés — pero el
**dónde y el cómo** los manda la matriz de campo, y ahí es donde se gana o se
pierde la rentabilidad.

## Reglas no negociables

1. **Nunca inventar datos de cosecha, ciclos ni rendimientos.** Solo lo que está
   en `07-datos/variedades_bitacora.csv`, en el resto de los CSV, o lo que
   Vanessa confirma explícitamente. Si un dato no existe, decirlo y pedirlo. Un
   ciclo inventado corrompe todo el calendario de Erica. El motor respeta esto:
   reporta `SIN_DATO` y se niega a estimar.
2. **Regla APLICACIONES:** nunca recomendar una bomba sin leer primero
   `07-datos/aplicaciones_historial.csv` actualizado. Antes de cualquier
   recomendación, mostrar la tabla de rotación de las últimas 3–4 semanas. Esto
   aplica incluso si Vanessa dice "hazlo de memoria".
3. **Ningún producto entra a formulación sin ficha técnica confirmada.** Si
   falta, se marca `SIN FICHA — NO USAR EN FORMULACIÓN`.
4. **Cambios semanales:** cuando Vanessa dicta el brain dump, organizar los
   cambios en una tabla y esperar validación antes de escribir en los archivos.
   Excepción: cambios obvios e inequívocos (cerrar una cama, corregir un color)
   se aplican directo y se reportan.
5. **Nombre homologado obligatorio.** Toda siembra nueva en CAMPO necesita
   columna N llena con el nombre exacto de la BITÁCORA. Sin eso, no aparece en
   el calendario de Erica. Si el nombre homologado no existe todavía, PAUSAR y
   proponer uno — no improvisar.
6. **Nunca dar a Erica datos históricos de cosecha en crudo** — solo estimados
   a futuro.
7. **Identidad visual obligatoria** en cualquier documento o PDF generado. Para
   PDFs de operarios: solo cantidades, cero explicaciones.
8. **Nunca asignar un color a una variedad por deducción del nombre y
   presentarlo como dato.** `paleta_color.csv` tiene columna `confianza_color`;
   lo marcado `baja` se confirma en campo antes de decidir sobre él.

## Jerarquía de verdad (si dos fuentes se contradicen)

1. Lo que Vanessa dice en la sesión actual
2. Los CSV de `07-datos/` (datos de campo reales)
3. Los markdown de este repositorio
4. Conocimiento general de floricultura

**Los datos de campo reales siempre le ganan a las proyecciones del Excel.** Se
han observado ciclos reales corriendo hasta 4 semanas por delante de lo
proyectado.

Para ciclo y ventana de cosecha del calendario de clientes, la fuente primaria
es **VARIEDADES_BITACORA**. `07-datos/ciclos_variedad.csv` es referencia
agronómica de manejo y se usa para planificación interna de siembra.

## Mapa del repositorio

| Carpeta | Contenido |
|---|---|
| `00-contexto/` | Empresa, equipo, reglas operativas, identidad visual |
| `01-infraestructura/` | Invernaderos bloque por bloque, análisis de suelo, No-Dig |
| `02-nutricion/` | Fertirriego, bokashi, biochar, supermagro, drenches |
| `03-fitosanidad/` | Reglas, rotación, inventario, estructura de bombas |
| `04-variedades/` | Comportamiento agronómico por variedad, notas de campo |
| `05-programacion/` | Sistema de previsión de cosecha, esquemas, Apps Script |
| `06-costos/` | Modelo de costos, costo por tallo, nómina |
| `07-datos/` | **Datos vivos en CSV** — exportados de los Excel maestros |
| `08-roadmap/` | Lo que falta construir y la visión de automatización |
| `09-procedimientos/` | Los 19 procedimientos de cómo se opera DCB |
| `10-postcosecha/` | Sala, hidratación, vida en vaso |
| `11-bouquets/` | **Estructura y color del bouquet** |
| `12-punto-de-venta/` | **Distribución de color en exhibición** |
| `13-optimizacion/` | **Cómo optimizar productos y procesos** |
| `motor/` | El motor de planificación en Python |
| `.claude/skills/` | Skills operativas (fitosanidad, variedades, programación, bouquets, marketing) |

## El motor

Python 3, solo librería estándar. Todo se ejecuta desde la raíz del repo.

```bash
python3 motor/cerebro.py matriz                 # cuánto de la matriz de decisión está cubierto
python3 motor/cerebro.py productos              # las 24 recetas del catálogo
python3 motor/cerebro.py auditar                # estructura + color de todo el catálogo
python3 motor/cerebro.py bouquet "Cosecha Grande"   # un producto en detalle
python3 motor/cerebro.py valor                  # ingreso por tallo propio
python3 motor/cerebro.py ciclos                 # ciclo y ventana por grupo
python3 motor/cerebro.py cartera                # demanda del catalogo contra cosecha real
python3 motor/cerebro.py cartera Gomphrena      # ficha de un grupo para decidir sobre el
python3 motor/cerebro.py rendimiento Campanula  # tallos/planta/día normalizado por ventana
python3 motor/cerebro.py explotar motor/demanda_ejemplo.csv   # demanda -> tallos
python3 motor/cerebro.py sembrar  motor/demanda_ejemplo.csv   # demanda -> siembra

python3 motor/importar_tallos.py registro.xlsx  # Drive -> los CSV de 07-datos/
python3 motor/dictar_tallos.py estado           # hasta que fecha llega el registro de cosecha
python3 motor/dictar_tallos.py validar          # revisa la cosecha dictada, sin escribir
python3 motor/dictar_tallos.py aplicar          # la mezcla en registro_tallos.csv
python3 motor/dictar_tallos.py pegar            # bloque TSV para subirla a la hoja de Drive

python3 motor/ficha_variedad.py                 # que dato hay por grupo, y cual falta
python3 motor/ocupacion.py                      # ingreso por m2 por semana de cama
python3 motor/ocupacion.py camas                # area de cada cama de la finca
python3 motor/calibrar_rendimiento.py           # lo teorico del ciclo contra lo que dio el campo
python3 motor/importar_ventas.py Punto=hoja.txt # hojas de punto de venta -> ventas_puntos.csv
python3 motor/cruce_venta_cosecha.py            # lo cosechado contra lo vendido, con su margen de error
python3 motor/analisis_variedad.py              # rentabilidad preliminar por variedad: ventana + venta + rol
python3 motor/ficha_completa.py Lisianthus      # la mesa de variedad por variedad: 11 secciones fijas
```

**Cuando Drive va atrasado y Vanessa dicta la cosecha:** las filas dictadas
NO se escriben en `registro_tallos.csv` — `importar_tallos.py` lo reescribe
completo y las borraría sin avisar. Van a `07-datos/registro_tallos_dictado.csv`
y entran con `dictar_tallos.py aplicar`, que valida grupo contra el desplegable,
rechaza fechas futuras y filas sin bloque, y salta lo que ya está registrado.
Drive sigue siendo la fuente de verdad: `pegar` produce el bloque para subirlo.
Detalle en `05-programacion/02-registro-de-tallos.md`.

**Para refrescar el registro de cosecha:** bajar
`DCB_Registro_Tallos_v7_ORGANIZADO` de Drive **como XLSX binario** y pasarlo por
`importar_tallos.py`. Leerlo como texto interpretado **trunca sin avisar** — el
2026-08-12 devolvió 251 filas de 598. El importador espeja las 6 pestañas,
corrige 3 errores de fecha confirmados y reporta cada corrección. Detalle en
`07-datos/FUENTES.md`.

**La cartera tiene niveles, no es una sola lista** (Vanessa 2026-09-10). 23
grupos clasificados en `07-datos/roles_cartera.csv`:

| Nivel | Quiénes | Regla |
|---|---|---|
| `BASE` | Statice · Celosia · Strawflower · Amaranto · Campánula · Boca de Dragón · Ammobium ↔ Matricaria | Siempre debe haber; un hueco es una falla |
| `BASE_ENCAJE` | Ammi ↔ Trachelium | El encaje es un **rol**, no una especie |
| `FOCAL` | Lisianthus · Zinnia · Girasol · Dahlias | Siempre una principal; el rol no queda vacío |
| `FOLLAJE` | Dusty Miller · Espárrago | El follaje propio **desplaza compra** de Ruscus: es costo evitado |
| `TOQUE` | Gomphrena · Green Ball · Larkspur · Colitas · Craspedia · Scabiosa · Amaranto Velvet/Cocoa | Rota **a propósito**, poca cantidad, en Inv 2 |
| `TOQUE_ENSAYO` | Cynoglossum | Con criterio de salida: si falla, se saca la cama |

**Juzgar un TOQUE por volumen es un error de categoría** — mide como fracaso lo
que es una decisión. Y el rol puede ser **por subtipo**: Celosia tiene una regla
distinta para plumosa, cristata y spicata, y Dusty Miller una por cultivar.

El archivo guarda además **cadencia de siembra** (Amaranto y Celosia spicata cada
3 semanas, Cristata mensual), **alternancia** (Ammobium ↔ Matricaria, Ammi ↔
Trachelium), **ventana de eventos** (Zinnia en agosto·diciembre·marzo, Cristata
en épocas de calor) y **anti-solapamiento** (Green Ball y Dusty Miller: dos camas
en cosecha al tiempo es pérdida). Detalle y citas en
`13-optimizacion/03-estrategia-de-surtido.md`.

`cartera` es la mesa de la sesión de cartera: cruza lo que el catálogo pide con
lo que el campo dio, grupo por grupo, y marca FALTA · SOBRA · COSECHA SIN RECETA
· señales de calidad/venta. La demanda es una **canasta no ponderada** (una
unidad de cada producto) porque el volumen de venta por producto vive en
`03_Ventas`, fuera del alcance — es el peso en el catálogo, no en la caja. No
ordena por margen: `costos_productos.csv` sigue vacío.

**El area de cama NO hay que medirla: es una constante** (2026-09-10). La finca
tiene una sola geometria — huecos cada 15 cm, 8 lineas, 1,20 m de ancho — que da
**0,18 m² por hueco**, y cierra contra toda el area ya documentada: Inv 4
completo 677,3 m² (doc: 677) e Inv 5 411,8 m² (doc: 412). Asi que el area de un
lote se deriva:

```
area m² = plantas trasplantadas × 0,15 × (distancia_cm / 100)
```

La malla es de 0,15 m **fijo en una direccion**; la distancia de siembra manda
solo en la otra. Sembrar mas denso mete mas plantas en la MISMA cama, no en menos
cama — por eso la distancia entra una sola vez, no al cuadrado. Es la formula
que corre en `motor/ocupacion.py`. Detalle en `07-datos/area_camas.csv` (21
camas).

**El eje ingreso/m²/semana YA CORRE** (2026-09-10). Se creia bloqueado por
falta de la columna `Fecha siembra campo` — llena en 112 de 302 filas, el 14 %
de las plantas. No estaba bloqueado: **esa columna se dejo de usar.** Vanessa
2026-08-14: *"deje de usarla, ahora trabajo solo con las semanas... la columna
que sigue es la semana que se trasplanto."* La columna `Semana` de trasplante
esta llena en **294 de 302 filas — el 95 % de las plantas.**

No se veia por una razon mecanica: `campo_siembras.csv` tiene **dos columnas
llamadas `Semana`** (trasplante e inicio de cosecha), y `csv.DictReader`
colapsa encabezados repetidos quedandose con la ultima. Asi que `_leer_csv()`
nunca pudo ver la de siembra. **Se leen por POSICION, no por nombre** (idx 7 y
10). El ano no esta en el archivo: se infiere por secuencia — las 302 filas son
un log cronologico y una caida grande en el numero de semana es el cruce de
diciembre a enero. Verificado contra las 111 filas que aun traen fecha exacta:
coinciden las 111.

`ocupacion.py` recorta el area a la ventana de cosecha **propia de cada grupo**
—el denominador tiene que cubrir el mismo periodo que el numerador— y trae su
propia validacion: el `tallos/planta` implicito se acerca al documentado en 11
grupos de 15. **Sigue siendo INGRESO, no margen:** falta la fila de tallos
vendidos del modelo de costos.

**Dos advertencias que no hay que perder de vista.** El orden es **sensible al
largo del registro**: al entrar las semanas 33-35, Lisianthus paso de
$78.474/m²/sem a $17.749 y de primero a cuarto. Un cultivo de ocupacion larga
y ventana corta de cosecha es el mas expuesto. Y `sem_a_campo` de
`ciclos_variedad.csv` **se cuenta desde el TRASPLANTE**, no desde la semilla —
lo fija `cerebro.plan_siembra` (`sem_campo = sem_cosecha - sem_a_campo`, y solo
despues resta la germinacion para llegar a la bandeja). Por eso las semanas de
cama son `sem_a_campo + ventana` y la germinacion no entra.

## Las cuatro preguntas de la mesa de variedad

Vanessa 2026-09-10, sobre para que sirve esta mesa: *"vamos a evaluar variedad
por variedad. Si nos esta dando la rentabilidad, segun el registro de tallos,
que estamos esperando si se esta vendiendo, si esta aportando y ver cuales son
los huecos de siembras y los sobrantes para ajustar la programacion."*

Son **cuatro** preguntas con salud de datos muy distinta.
`python3 motor/ficha_variedad.py` audita grupo por grupo cual se puede
contestar:

| # | Pregunta | Hoy | Qué la desbloquea |
|---|---|---|---|
| 3 | **APORTA** — ¿lo pide el catálogo? | **23 de 24** | ya está: catálogo + `roles_cartera.csv` |
| 4 | **AJUSTE** — ¿huecos y sobrantes? | **16 de 24** | ya está: demanda vs cosecha + ciclo |
| 1 | **RENTA** — ¿da rentabilidad? | **0 de 24** | falta UNA cosa: el **costo** |
| 2 | **VENTA** — ¿se está vendiendo? | **0 de 24** | **le falta el esqueleto entero** |

**La pregunta 1 ya corre a medias:** `ocupacion.py` da INGRESO por m² por semana
con el área recortada a la ventana. Lo que no se puede es restarle el costo, y
por eso no dice si algo da pérdida. La desbloquean los doce números de `Tallos
vendidos en el mes` en `DCB_Modelo_Costos`.

**La pregunta 2 ya corre desde el 2026-09-11 — 18 de 24 grupos.** La venta **no
vive en este repositorio**: las cuatro columnas de venta de `campo_siembras.csv`
están en 0 de 302 y **no son la fuente.** Vive en Drive, en **una hoja por punto
de venta**, en la cuenta de servicio `poscdreamscanbloom@gmail.com` (Vanessa
2026-09-11: *"debes mirar a través de la cuenta de servicios las hojas de venta
de cada uno de los puntos"*).

```bash
python3 motor/importar_ventas.py Jardines=jardines.txt "San Lucas=san_lucas.txt" ...
```

Se espejan a **`07-datos/ventas_puntos.csv`**: 3.789 ventas, 4.510 unidades,
121 productos, del 2026-04-21 al 2026-09-10.

El estado de cada punto vive en **`07-datos/puntos_venta.csv`**, y el importador
lo lee: sin él, un punto **cerrado** se confunde con uno que dejó de anotar, y
son cosas opuestas.

| Punto | Estado | Ventas | Unidades | Desde | Hasta |
|---|---|---|---|---|---|
| Jardines | ACTIVO | 1.169 | 1.285 | 17/06 | 10/09 |
| Online | ACTIVO | 870 | 1.311 | 07/05 | 28/08 |
| San Lucas | ACTIVO | 532 | 579 | 18/06 | 10/09 |
| Tesoro | ACTIVO | 410 | 443 | 19/06 | 10/09 |
| Del Este | ACTIVO | 391 | 431 | 28/07 | 10/09 |
| Viva Envigado | **CERRADO** | 416 | 460 | 21/04 | 21/05 |
| Lemont | **CERRADO** | 1 | 1 | 07/08 | 07/08 |
| **Especia** | **ACTIVO, SIN HOJA** | — | — | ~01/09 | — |

**Viva Envigado y Lemont están cerrados** (Vanessa 2026-09-11: *"ya no estamos en
Viva Envigado, y en Lemont tampoco"*). Sus ventas son históricas y completas —
**no son un hueco de registro.** La única venta de Lemont es real: el punto duró
muy poco.

**Falta `Especia`**, que arrancó la semana del 01/09 (ISO 36). **No tiene hoja de
venta visible en Drive** — no aparece por título, ni entre las hojas creadas
desde el 20/08, ni en la cuenta `poscdreamscanbloom`. Hay que pedirla o que la
compartan; mientras tanto ese punto no entra a `ventas_puntos.csv`.

**Cómo está armada cada hoja** — una pestaña `CONFIG_PRECIOS` y después **una
pestaña por día**, cada una con tres bloques: la venta fila a fila, los totales,
y un `INVENTARIO` que trae `Reposicion` y `Salida`. El bloque de inventario
también empieza con `Producto`, así que sin cortarlo sus filas se leen como
ventas. Viva Envigado y Online traen además tablas dinámicas, abonos y entregas.
`importar_ventas.py` exige la firma completa de la tabla diaria y descarta —sin
rellenar— toda fila sin fecha.

**EL LÍMITE AHORA ES EL CATÁLOGO, no el dato de venta.** La venta se registra por
**PRODUCTO**, y sin receta no se puede bajar de producto a tallos. La mesa de
trabajo es **`11-bouquets/recetas_por_hacer.csv`**, ordenada por unidades
vendidas:

| Tipo | Prod | Unid | Qué hay que hacer |
|---|---|---|---|
| PAQUETE | 42 | 1.154 | un número cada uno: tallos por paquete |
| BOUQUET | 21 | 770 | receta completa |
| MIXTO | 14 | 358 | el reparto entre 2-3 variedades |
| EVENTO | 13 | 231 | ya prellenadas: el conteo está en el nombre |
| NO_FLOR | 6 | 55 | sobres, boutonnieres, floreros |

**Avance: 5 de 96 productos, 448 unidades (17 %)** — dictadas por Vanessa el
2026-09-11 y escritas en `formulas_productos_bouquets.csv`. Cobertura de la
venta: **43 % → 54 %** de las unidades.

**UN NOMBRE DISTINTO NO SIEMPRE ES UN PRODUCTO DISTINTO.** Vanessa 2026-09-11:
*"Cristata y Gomphrenas, y Cristata Pop son lo mismo, tienen la misma cantidad
de tallos, sólo que son dos colores diferentes. A veces le pongo nombres
diferentes **para yo saber si algún color se vendió más que otro**."*

Eso cambia cómo se lee la lista de 121 productos: **no son 121 recetas.** Varios
son **el mismo ramo en dos colores**, con nombre distinto a propósito, y esa
duplicación es un **instrumento de medición de color en punto de venta** — la
pierna 1 del objetivo de este repositorio. Los dos primeros documentados
comparten estructura (5 cristata + 15 gomphrena) y cambian sólo el color:

| Producto | Cristata | Gomphrena | Precio |
|---|---|---|---|
| `Bouquet cristata pop` | Verda Green (VERDE) | frambuesa — Quis Carmine/Red | $85.000 |
| `Cristata y gomphenas` | Enda Rose (CORAL) | Quis Carmine (FUCSIA) | $65.000 |

*(Mismo contenido y $20.000 de diferencia: pendiente de confirmar si es precio
real o uno quedó desactualizado.)*

**Antes de dar un producto por "sin receta", hay que preguntarse si es variante
de color de otro que ya la tiene.**

**Gomphrena son DOS productos, no uno** (Vanessa 2026-09-11): la **pequeña de
racimo** (Quis Carmine, Quis Red → "fresa", "frambuesa") va a **25 tallos + 3
Ruscus**, y la **grande con laterales** (salmón, blancas, rose) va a **5-6
tallos**, *"un tallo con laterales completo"*. La equivalencia la dio ella:
*"cinco tallos de la grande, más o menos el mismo volumen"* que veinticinco de
la pequeña — **5×**. El catálogo ya lo corroboraba sin que nadie lo notara:
`Gomphrenas blancas (paquete)` tenía 4 tallos a $45.000 y `Gomphrenas (paquete
grande)` 26 a $90.000.

**Qué es un `Event planner`** (Vanessa 2026-09-11): *"básicamente tienen un
quince por ciento de descuento, se hacen en papelería más básica, y no suelen
tener follaje"*. La cuenta cierra exacta — $45.000 × 0,85 = **$38.250**, que es
el precio de todos los `Event` del archivo. **No llevan menos tallos: llevan lo
mismo sin follaje.**

**Dos recetas son variables A PROPÓSITO, y eso no es un dato faltante: es como
funciona el producto.** Vanessa sobre la Edición Especial: *"todo depende de lo
que esté en cosecha"*. Su acompañante rota entre **Ammi, Trachelium, Celosia
plumosa y Green Ball, 3-5 tallos** — *"dependiendo lo grandes que son"*. Se
escriben como `SUSTITUCIÓN`, que `cerebro.py` ya maneja sin sumar el ingrediente
a las dos variedades a la vez. Lo mismo el *"Strawflower o Helipterum"* de la
Cristata Plus.

> **El `%VTA` de `ficha_variedad.py` NO se lee literal, y el caso que lo prueba
> vale recordarlo.** Antes de escribir estas cinco recetas, Lisianthus figuraba
> con **1 %** (76 tallos vendidos contra 6.926 cosechados) porque *Edición
> Especial Lisianthus* —189 unidades, de lo más vendido del cultivo— no tenía
> receta. Con la receta escrita pasó a **28 % (1.912 tallos)**. Ese 1 % medía el
> catálogo, no la venta, y **arrancar el cultivo por leerlo mal habría sido el
> error más caro posible.** El motor imprime la tabla de venta invisible por
> grupo antes del veredicto; a Lisianthus todavía le quedan 151 unidades ahí.
>
> Y al revés: un `%VTA` **sobre 100** no es un milagro, es un hueco del registro
> de cosecha. Larkspur figura vendiendo más de lo cosechado porque su ventana
> registrada son dos días.

> **LAS RECETAS CAMBIAN EN EL TIEMPO, Y EL MOTOR NO LO MODELA.** Es la
> advertencia más importante sobre la cobertura del 82 %.
> `formulas_productos_bouquets.csv` guarda **una sola versión de cada receta —
> la de hoy** — y el cruce la aplica hacia atrás a cinco meses de venta.
>
> El caso que lo destapó: Vanessa 2026-09-11, *"comenzamos a colectarle
> Escabiosa Estrella solamente a esta semana. Todos los que eran con colitas de
> conejo anteriores **no** tenían Escabiosa Estrella"*. La receta de hoy de
> `Dusty miller con colitas de conejo` lleva 3 scabiosa; aplicada a las 85
> unidades vendidas desde junio, inventaba **255 tallos que nunca salieron** —
> y hacía aparecer a Scabiosa, que no tiene un solo tallo cosechado registrado,
> como si vendiera.
>
> **Mientras no haya fecha de vigencia por receta, un ingrediente agregado
> hace poco se deja con la cantidad VACÍA** (el motor salta los ingredientes
> sin cantidad) y la fecha de arranque va en las notas. Es preferible
> subestimar a inventar demanda que jamás existió, porque esa demanda
> inventada termina en una cama sembrada.
>
> La hoja de cada punto de venta ya tiene el concepto: `CONFIG_PRECIOS` trae
> una columna `FECHA INICIO` por producto. Al archivo de recetas le falta.

Las **13 señales cualitativas** de `07-datos/desajuste_demanda.csv` siguen
valiendo: dicen **por qué** sobró o faltó, que el número no dice — *"no tengo a
quien vendérselo"* (Boca de Dragón 4A), *"las usamos todas en MADRES y se
quedaron cortas"*.

*(`07-datos/tallos_despachados.csv` sigue vacío y es otra cosa: el despacho de
poscosecha al punto. En Drive existe **`Despacho poscosecha a puntos de venta`**,
sin espejar, con datos hasta el 2026-05-14.)*

## El seco son DOS corrientes, y sólo una está en el registro

Vanessa 2026-09-11. Explica por qué el cruce venta/cosecha no cierra y de dónde
sale la línea `forever`. Detalle en **`10-postcosecha/03-el-flujo-del-seco.md`**.

| Corriente | Origen | ¿En el registro? |
|---|---|---|
| **Sobrante de sala** | *"el lunes y el martes, con lo que se cosechó sobre todo el viernes y sobró, se suele colgar para secar"* | **SÍ** — ya se contó como fresco al cortar |
| **Sacada de cama** | *"los tallos enanos, lo que sobra… se suele cortar para secar, pero de eso no hay registro"* | **NO, en absoluto** |

La primera **no es doble conteo**: es el mismo tallo cambiando de destino. Parte
de los +36.512 tallos de diferencia del cruce es esto, no pérdida.

La segunda es **producción adicional que el registro nunca vio** — la finca
produce más que los 83.200 tallos. No se cuenta porque **el que sube ese
material es el preparador de cama, no el cortador** (*"normalmente no es el que
cuenta, y lo sube muy crudo"*), y después *"la persona que cuelga lo maquilla y
de ahí saca lo que está bueno"* — dos mermas en serie, ninguna medida.

**La salida no es contar en el origen: es derivarlo de la venta.** `Bouquet
forever Dream` es el producto de esa corriente, así que
`unidades vendidas × receta = tallos secos consumidos` da un piso real, sacado
de una venta que sí se registra. Hoy la línea forever son **186 unidades y
$19.725.000 sin una sola receta** — son las tres que faltan.

**Larkspur corrobora la lectura:** `secado_variedad.csv` ya dice que seca `SI`
con rol `LINEA`, y es el grupo que más vende por encima de lo cosechado (243
contra 879). Se vende seco, y el seco viene de sacada de cama, que no se
registra. El cruce no está fallando: está encontrando esto.

## El ciclo no es un número: es una serie por cohorte

Vanessa 2026-09-11, corrigiendo una lectura mía. Yo reporté que el ciclo de
Lisianthus **estaba mal** (15 semanas reales contra 19-23 documentadas). No
estaba mal:

> *"La documentación que hay de los ciclos de lisianthus, el cerebro, es por
> **siembras pasadas**, no es por literatura imaginada. Pero esta tuvimos un
> resultado diferente… **cada cosecha tiene que ser personalizada**, porque puede
> comportarse diferente."*

`ciclos_variedad.csv` es el **consolidado histórico** y no se toca: sigue siendo
la referencia de planificación. Lo que faltaba es dónde guardar la cohorte que se
comportó distinto — **`07-datos/ciclos_observados.csv`**, una fila por COSECHA con
su ventana observada, su rendimiento real, su incidencia y su procedencia. Con
suficientes cohortes dirá si el consolidado hay que mover, y **con qué
dispersión**, que es lo que hoy no se sabe.

Protocolo completo en **`04-variedades/protocolo-por-variedad.md`**; la ficha de
once secciones la produce `motor/ficha_completa.py <variedad>`.

**El caso Lisianthus está escrito en `04-variedades/lisianthus-el-caso.md`** — el
sustento para la discusión de portafolio que Vanessa tiene con David. Resumen:
los 20 productos que lo llevan tienen **ticket 1,5× mayor** ($87.442 contra
$58.654) y mueven el **29 % del ingreso** siendo el 17 % del catálogo. Su costo
de reemplazo comprado es bajo ($2,4M), así que el argumento de peso no es el
tallo: es la **vida en vaso** — *"los bouquets permanecen bonitos, así le cambie
una boca de dragón o una campánula varios días"* — y ése es **el único dato que
no está medido**: `vida_en_vaso.csv` tiene una sola fila y no es Lisianthus.

`matriz` es el tablero de control del proyecto: mide qué porcentaje de cada una
de las 11 variables de decisión está cubierto con datos reales. **Empieza cada
sesión de estrategia corriéndolo.**

Las reglas de estructura y color viven en constantes al inicio de
`motor/cerebro.py` (`RANGO_ESTRUCTURA`, `DOMINANTE_MIN`,
`MAX_FAMILIAS_CROMATICAS`, `NEUTRO_MIN`, `NEUTROS`). Se cambian ahí, en un solo
lugar, no repartidas por el código.

## Para retomar la sesión del 2026-09-10

Tres documentos, en este orden — cada uno continúa al anterior:

1. **`08-roadmap/03-donde-quedamos.md`** — la sesión de **cartera** (mañana): las
   tres cosas que cambiaron el marco, los 8 pendientes de Vanessa ordenados por
   desbloqueo. **Leerlo antes de retomar cartera o siembra.**
2. **`08-roadmap/04-donde-quedamos-rentabilidad.md`** — la sesión de
   **rentabilidad** (tarde): las dos preguntas con salud de datos opuesta, y el
   mapa de las ramas sueltas.
3. **`08-roadmap/05-donde-quedamos-ocupacion.md`** — **el más reciente** (noche):
   el eje ingreso/m²/semana ya corre, por qué el bloqueo que reportaba el doc 04
   no existía, el registro al 27/08, y la decisión de arquitectura que quedó
   abierta con `cerebro.py m2`. **Empezar por acá si el tema es ocupación,
   margen o rentabilidad.**

## Cómo arranca cada sesión

Vanessa hace un brain dump de la semana en campo. El flujo es:

1. Leer `07-datos/` para el estado actual (siembras, aplicaciones, tallos).
2. Organizar lo dictado en categorías: camas cerradas · ventanas modificadas ·
   siembras nuevas · problemas fitosanitarios · observaciones de variedad.
3. Preguntar solo lo que falta para poder escribir (bloque, semana, cantidad,
   nombre homologado).
4. Aplicar los cambios y reportar qué cambió.
5. Promover a regla cualquier observación que se repita (misma variedad + misma
   zona + mismo comportamiento, 2 veces o más) → `04-variedades/notas-campo.md`.

*"El campo enseña solo si lo documentamos bien."*

## Estado: los bloqueos que resolver primero

Ordenados por relación esfuerzo/desbloqueo. Correr `cerebro.py matriz` para el
estado medido. Detalle en `13-optimizacion/01-como-optimizar.md` y la lista
completa de datos pendientes en `08-roadmap/02-informacion-que-falta.md`.

**Nivel 0 — archivos que ya existen y solo hay que compartir:**

0. **`DCB_Fitosanidad_Maestro.xlsx`** (8 hojas), **`DCB_Modelo_Costos.xlsx`**,
   **`Calculo_por_tallo.xlsx`**, `aplicaciones_historial` actualizado y el
   **`PROGRAMACION_2026` v8**. No hay que generar el dato: hay que traerlo.
   Desbloquean fitosanidad y margen completos. **Pedirlos antes que nada.**

**Para poder decidir DÓNDE sembrar (la pierna que falta):**

1. **Medir temperatura y humedad por bloque** — hoy el microclima es cualitativo
   ("caliente", "fresco", "húmedo nocturno"). Sin números no se puede cruzar con
   el riesgo de hongo ni con la velocidad de ciclo. → `microclima_bloques.csv`
2. **Registrar el clima semanal de la finca** — lluvia, temperatura mínima y
   máxima por semana ISO. Es la variable que corre los ciclos y dispara la
   botrytis. → `clima_semanal.csv`
3. **Estructurar el histórico fitosanitario** — 24 eventos de fusarium, botrytis,
   mosca blanca, mildeo, oidio y roya están enterrados en texto libre dentro de
   los COMENTARIOS de `campo_siembras.csv`. Extraídos ya a
   `incidencia_fitosanitaria.csv`; faltan las semanas de ciclo y la severidad.
4. **Empezar a medir longitud de tallo** — la calidad no se registra en ninguna
   parte del repositorio. Es la diferencia entre "produjo" y "produjo vendible".
   → `calidad_tallo.csv`

**Para poder cerrar la nutrición (abierto 2026-09-02):**

4b. **Litros de tanque aplicados por m² por bloque** — sin esto no se puede pasar
    de "gramos por tanque" a "kg por m² por año", que es la unidad en la que se
    decide el fertirriego. Es también lo que confirma por qué el cobre de Bloque 5
    no respondió a la dosis fija de Haifa Micro.
4c. **Análisis del Bokashi terminado** (abono orgánico, Natural Control) — es la
    fuente de potasio no contabilizada del sistema: equinaza + ceniza + melaza +
    king grass, aplicada a 1–2 kg/m², 2–3 veces al año, sobre un suelo con
    saturación de K de 24–30 %. Sin este dato el balance de nutrientes no cierra.
4d. **Ficha técnica de Haifa Micro Hydroponic (% de Cu)** y precios actualizados
    de Haifa — mesa de trabajo en `02-nutricion/05-comparativo-casas-comerciales.md`.
4e. **N-NH₄ y análisis de savia** — el N-NH₄ vino vacío en los tres informes de
    agosto; sin la relación nitrato:amonio el diagnóstico de Fase 1 (Kempf) es
    parcial. La savia es lo que verifica si el mineral llegó a la planta.
4f. **Análisis de suelo de Inv 1** — los tres informes de agosto son Bloque 3, 4
    y 5. Inv 1 tiene las rosas de jardín injertadas de ~7 años, el cultivo de
    **mayor ticket** de la finca, y **no tiene una sola variable de suelo medida.**

**Para poder decidir CUÁNTO y a QUÉ PRECIO:**

5. **Cargar `Tallos vendidos en el mes` en `DCB_Modelo_Costos`** — el modelo de
   costo por tallo **ya está construido y con los costos de 2026 cargados**
   (verificado en Drive el 2026-09-10). Su único campo manual es esa fila, y
   está en 0 en los doce meses, así que todo sale en $0. Doce números
   desbloquean el costo por tallo real del año. Piso ya calculable con cosecha
   como denominador: **$1.379/tallo en junio, $869 en julio**. Ver
   `06-costos/02-costo-por-tallo.md`.
   *(`costos_productos.csv` es otra cosa: una lista de precios de insumos para
   el costo por aplicación. Sigue vacía, pero no es el bloqueo del margen.)*
6. **Fijar el cultivar en las recetas** — 24 % de los tallos DCB del catálogo
   no lo tienen. Es la causa raíz de la inconsistencia de color en punto de venta.
7. **Confirmar el color de Statice Forever Happy** — está en 9 de 24 productos
   con color inferido (confianza baja).
8. **Medir Ext 3B, Inv 2, Mini, Inv 4C, Inv 6** — sin esto la capacidad real
   de campo está subestimada.
9. **Limpiar `formulas_productos_bouquets.csv`** — 11 filas de productos
   fitosanitarios contaminan el archivo de recetas.
10. **Llenar `RENDIMIENTO`** en `DCB_Registro_Tallos` — la pestaña existe con sus
    columnas (área m², costo semilla, costo insumos) pero está **vacía en la
    fuente**, no es un problema de espejado. Es el mismo bloqueo que el #5.

*Cerrado:* ciclo de Girasol, Green Ball, Amaranto y Ammobium — los 13 grupos del
catálogo ya son planificables. **Registro de tallos reexportado** (2026-08-12):
596 filas hasta el 31/07 contra 361 que había, y `consolidado_lotes.csv` pasó de
vacío a 141 lotes — `CONSOLIDADO` sí se calculaba solo en Drive, solo faltaba
espejarlo.

## Si abres este repo desde otra cuenta o máquina

Con `git pull` viaja casi todo: este `CLAUDE.md`, las skills de `.claude/skills/`,
los CSV de `07-datos/` y el motor. El motor es Python 3 con librería estándar, no
hay nada que instalar. **La procedencia de cada dato viaja también** — la columna
`fuente` dice si un número salió de un CSV, de un documento o de una confirmación
explícita de Vanessa.

Tres cosas que **no** viajan:

1. **El acceso a Google Drive.** Está atado a la cuenta, no al repo. Los cuatro
   Excel maestros de la tabla de abajo están aquí solo como IDs; sin el conector
   de Drive autorizado sobre `DCB Claude / 07_Operaciones`, esos IDs no se pueden
   abrir. Traer los archivos del Nivel 0 de
   `08-roadmap/02-informacion-que-falta.md` requiere Drive.
2. **`motor/espejar.py`.** Lee los resultados de descarga desde los transcripts de
   sesión en `~/.claude/projects/`. Desde otra cuenta esos transcripts no existen,
   así que el script no encuentra nada que espejar. No está roto: se quedó sin
   fuente.
3. **Permiso de escritura en GitHub** sobre
   `vanessakosa/operaciones-planificacion-siembra-dcb`.

Para arrancar una sesión desde cero:

```bash
git pull
python3 motor/cerebro.py matriz     # estado medido de las 11 variables
python3 motor/cerebro.py auditar    # estado del catálogo
```

## Archivos maestros que viven en Drive y NO están en el repo

Son demasiado grandes para espejar como texto. Se consultan en Drive por ID:

| Archivo | ID de Drive |
|---|---|
| `PROGRAMACION_2026_v8_ACTUALIZADO.xlsx` (17 MB) | `1NaGlBEY5j-e-rLx_7NvdIWWPWCiGxv0x` |
| `Stock Productos Agro DCB.xlsx` | `1lqk28pyr6Fd00U1nuPmwH9_hfVL8yZE4` |
| `DCB_Calculadora_Bouquets.xlsx` | `14eKUYrRhmseyqrHXxDFt2Siq97E71yVN` |
| `DCB_Registro_Tallos_v7_ORGANIZADO` | `14OP0GgkNmV1ty8Jz0hmASEts64ptI3y9L0i2FYsedHc` |

El archivo maestro activo de programación es siempre el `PROGRAMACION_2026` en
su versión más reciente — **verificar la versión antes de tomar los CSV de
`07-datos/` como definitivos.**
