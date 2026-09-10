# Notas de Campo Acumuladas

Registro cronológico de observaciones de campo reportadas por Vanessa. Formato: fecha, variedad, zona, observación.

**Regla de promoción automática:** si la misma variedad + misma zona + mismo tipo de comportamiento aparece reportada dos o más veces en este log, se promueve automáticamente a `reglas_agronomicas.md` como regla establecida — sin esperar confirmación explícita de Vanessa. Un patrón repetido en campo ya es una regla. Al promoverla, anotar aquí la fecha de promoción y dejar la entrada original como historial.

Si una observación nueva contradice una regla ya establecida (no la repite, la contradice), esa sí requiere pausar y preguntar antes de tocar la regla existente.

---

## 2026-09-10 — LA PREMISA QUE FALTABA: la cartera tiene niveles

Vanessa corrigió el marco entero del análisis: *"Yo no siembro todo, todo el
tiempo."* Tres niveles con reglas distintas, en
`07-datos/roles_cartera.csv` y explicados en
`13-optimizacion/03-estrategia-de-surtido.md`:

- **BASE** — Boca de Dragón, Campánula, un encaje (Ammi **o** Trachelium).
  Siempre debe haber; un hueco es una falla.
- **FOCAL** — siempre una flor principal: Lisianthus preferido, o Dianthus,
  Marigold, Zinnia. El rol no puede quedar vacío.
- **TOQUE** — rota **a propósito**, poca cantidad, **en Inv 2**, para no quitarle
  área productiva a Inv 3. Hoy: colitas de conejo y craspedia. Sigue larkspur.
  En ensayo: cynoglossum.

**El motivo del toque es de demanda, no de oferta:** *"que no haya una cosecha
siempre de lo mismo, para que cuando las personas vayan al carrito se antojen
porque tienen rato que no lo ven. Eso es lo que genera que la gente esté
constantemente comprando."*

Dos cosas que esto corrige de lo que dije antes:

1. **"Trachelium o Ammi" no es una receta indecisa.** Es el rol de encaje con la
   especie abierta a propósito. Yo lo había reportado como un ingrediente que la
   receta no se comprometía a fijar.
2. **El `SOBRA` de Lisianthus no es un exceso a recortar.** Es la focal del
   catálogo cumpliendo su función, con un ciclo de 19–23 semanas que no se
   improvisa.

Y el caso que enseñó la regla: **Larkspur son 4.788 plantas en 3A** — un toque
sembrado a escala de producción en el mejor bloque. Los toques de hoy están todos
en Bloque 2 y son de 338 a 870 plantas.

### El hallazgo inmediato

**Craspedia, Scabiosa Estrella y Cynoglossum tienen cosecha abierta desde agosto
y CERO tallos en `registro_tallos.csv`.** Y ninguno de los tres está en la hoja
LISTAS, así que no aparecen en el desplegable de Grupo — un grupo que no se puede
elegir es un grupo que no se registra.

O sea que **la pierna de la estrategia que genera la recompra es la única que no
se está midiendo.**

## 2026-09-10 — DECISIÓN: Larkspur se queda, como cultivo de SECO, con Light Blue

Vanessa confirmó las tres cosas que faltaban:

> *"Larkspur es un ingrediente más en nuestros arreglos secos, sí. El Light Blue
> se seca mejor. No lo hemos vuelto a sembrar."*

**Eso resuelve la contradicción.** El despetalado en el carrito era un fracaso de
**flor fresca**, y el canal real de larkspur es **seco** — donde el despetalado
importa mucho menos. El lote de 3A se sacó en la semana 24 *para secar*, no por
agotamiento: era la cosecha yendo a su destino correcto, no un fracaso.

**Se queda `Light Blue`.** Seca mejor y es el **único azul verdadero del
catálogo** (`paleta_color.csv`: AZUL_CLARO). Registrado en
`07-datos/secado_variedad.csv`.

`Misty Lavender` queda **pendiente de decidir**: si el canal es seco y Light Blue
seca mejor, sembrar las dos compite por la misma cama sin aportar surtido —
LAVANDA ya lo dan las Snapdragon Cannes Lavender. No se retira sin que Vanessa lo
diga.

### El problema urgente que esto destapa

**No hay larkspur sembrado.** Y el ciclo no perdona: germinación 6 semanas + 12 a
cosecha. Sembrando bandeja hoy (semana 37), el **primer corte cae el 14 de enero
de 2027** — después de Navidad.

Y diciembre es justo cuando importa: el `calendario_comercial_colombia.csv` dice
que **el fuerte en dinero de diciembre son las coronas y guirnaldas**, alto ticket
por unidad. El larkspur seco es ingrediente de eso.

**Así que lo único que puede cubrir diciembre es el larkspur que ya está seco en
bodega, del lote de la semana 24 — y nadie sabe cuánto hay.** No existía ningún
archivo de inventario de material seco: se creó
`07-datos/inventario_seco.csv` (solo encabezado) para poder anotarlo. Es un activo
del negocio que hoy no se cuenta, y es el mismo caso de las colitas de conejo,
cuyo excedente también va a coronas.

Aparte: **4 productos del catálogo dependen de larkspur fresco.**
`Larkspur (paquete solo)` a $65.000 es **100 % larkspur** — no se puede armar.
`Larkspur combinado` ($55.000) y `Paquete amaranto velvet y larkspur` ($62.000)
son 67 %. `Centro de mesa pequeño` ($145.000) es 19 %.

### Dahlias — homologados aprobados

Vanessa aprobó los tres nombres, uno por origen: **`Dahlia Ball`** (esquejes
comprados a Ball), **`Dahlia Mix DCB`** (propias por división) y
**`Dahlia Italiana`** (las regaladas, a sembrar la sem 37). Las filas hay que
crearlas en VARIEDADES_BITACORA **en Drive** y llenar la columna N de los dos
lotes que ya están en CAMPO — ver acciones 10 a 12 de
`05-programacion/06-plan-semanal.md`.

## 2026-09-10 — CORRECCIÓN: Larkspur no produjo poco, el registro empezó tarde

**Lo que se dijo mal en esta sesión:** que Larkspur era el caso más claro de
"se va" porque dio **243 tallos en toda la corrida**, siendo el 11 % del
catálogo. Eso está **equivocado**, y el propio comentario de campo lo desmiente:

> *"Ya cosechando en semana 20, medio balde diario. Cosecha extraordinaria en
> semana 21 y 22, sacando un balde diario, sacamos las plantas en sem 24 para
> secar, las ventas no fueron tan buenas, se despetalaban en el carrito."*

**4.788 plantas en 3A**, cosecha empezando en la semana 20 y pico en la 21 y 22
— y `registro_tallos.csv` arranca el 2026-05-31, que es la **semana 22**. El pico
de Larkspur ocurrió casi todo **antes de que existiera el registro**. Los 243
tallos no miden a la variedad: miden desde cuándo se anota.

Y el lote no se cerró por agotamiento: *"sacamos las plantas en sem 24 **para
secar**"*. Larkspur tiene destino en seco, igual que las colitas de conejo.

**El problema real de Larkspur no es producción, es poscosecha:** se despetala en
el carrito. Esa es la variable que decide si se queda, y no aparece en ninguna
columna de la cartera porque `calidad_tallo.csv` y `vida_en_vaso.csv` están casi
vacíos.

### El patrón general, que es lo importante

No es un caso aislado. **Nueve grupos tienen picos o cierres documentados antes
de la semana 22**, o sea antes del registro: Gomphrena (picos en la 9 y la 21),
Celosia (pico 15), Green Ball (16), Matricaria (15), Strawflower (21), Statice,
Ammobium, Zinnia y Larkspur.

Sumado a las cuatro semanas que faltan al final, **la tabla de cartera es una
foto de 12 semanas (ISO 22 a 33), no un veredicto del año.** `cerebro.py cartera`
ahora lo advierte y marca los grupos afectados con `<TRUNCADO`, para que la
lectura no se vuelva a hacer mal.

## 2026-09-10 — respuestas al cierre de la sesión de cartera

**Colitas de conejo · color BEIGE confirmado**
Vanessa lo confirmó en campo. Entró a `paleta_color.csv` como BEIGE, confianza
alta, y **BEIGE se agregó al conjunto de NEUTROS** del motor: Lagurus es textura
neutra, así que cuenta para el mínimo de neutro del bouquet y no como surtido de
color. El bouquet se llama **"Dusty con colitas"** y lleva 7 — no existe en el
catálogo todavía, ver `11-bouquets/03-recetas-pendientes.md`.

**Espárrago · Bloque 2 · ciclo 15 semanas ESTIMADO**
Vanessa: *"el ciclo calcúlalo con la ventana de inicio de cosecha, pero calculo
como 15 semanas."* Se registró como **estimado por ella, no medido**, porque no
hay fila de siembra en `campo_siembras.csv` contra la que verificar. Con ciclo 15
y primer corte el 2026-08-10 (sem 33), la siembra caería cerca de la semana 18 —
por confirmar. ~30 plantas aproximadas.

**Dahlias · "Ball" es el PROVEEDOR, no la forma**
Se resolvió la ambigüedad del dictado anterior: cuando Vanessa dijo *"rojas de
bol"* se refería a que ese bloque se compró como esquejes a **Ball**, el
proveedor que ya aparece en `campo_siembras.csv` (lote de 696 plantas, sembrado
el 2025-11-11 en bloque 2). No son dalias de forma "bola". Corregido en la nota
de `paleta_color.csv`.

**Lisianthus · "cabeza grande" y "cabeza pequeña" son GRADO, no cultivares**
Vanessa: *"es grado, no es cultivar distinto."* Las dos recetas que los piden
resuelven ahora al grupo Lisianthus. **Y esto destapa algo:** el catálogo ya pide
un grado de tallo que **no se mide en ninguna parte** — `calidad_tallo.csv` está
vacío. Es el primer caso de uso concreto de ese archivo: no es una mejora
teórica, hay dos recetas que dependen de él.

## 2026-09-10 — sesión de cartera (dictado de Vanessa)

**Celosia cristata · en cosecha ahora · Enda Rose es el segundo color**
Vanessa: *"Celosia Cristata Enda Rose es otro color que estamos cosechando en
este momento."* Hasta hoy la paleta solo tenía `Cristata Verda Green` (VERDE).
El color de Enda Rose **no se dedujo del nombre**: `campo_siembras.csv` fila 272
lo registra como *"Rosado coral"*. Entró a `paleta_color.csv` como CORAL,
confianza alta, citando esa fuente.

**Celosia · REGLA NUEVA · la receta fija el subtipo, no el cultivar**
Vanessa: *"cada vez que una receta pida Celosia Plumosa va a ser una de ellas,
la que esté en cosecha en ese momento."* O sea que el cultivar abierto en las
recetas de Celosia **no es un dato que falte: es el diseño.** La unidad que la
receta fija es el subtipo (cristata · plumosa · spicata), y eso es coherente con
que en 3A y MINI las plumosas van intercaladas en la misma cama. Consecuencia
práctica: para Celosia, el bloqueo #6 del `CLAUDE.md` ("fijar el cultivar en las
recetas") **no aplica** — lo que hay que fijar es el subtipo, y ya está fijado.

**Dahlias · colección mixta, tres orígenes distintos, sin conteo**
Vanessa: colección mixta de todos los colores, **sin segmentar por color**. Tres
orígenes que conviene mantener separados en el registro:
1. **Esquejes comprados** — blancas, rosadas y rojas de bola. *"Florece como al
   mismo tiempo"*: es el bloque que da un pico concentrado.
2. **Mixtas propias** — propagadas por división, hijos guardados de años previos.
3. **Italianas regaladas** — a sembrar esta semana (sem 37).

*"Está un poco desordenado todavía"* — **no hay cantidad de plantas.** Sin
denominador no hay tallos/planta ni tallos/m². Dahlia es además perenne, así que
el denominador correcto es el ÁREA, no las plantas.

**Espárrago · follaje propio de semilla · ENSAYO exitoso**
Vanessa: se sembró **desde semilla** como prueba y *"nos ha ido muy bien"*. La
intención es **sembrar más**. Aproximadamente **30 plantas** (dato aproximado
dictado, pendiente de contar). Zona SIN_DATO — no se registró el bloque.
Es el único follaje propio del catálogo: hoy el follaje se compra (Ruscus), así
que cada tallo de espárrago propio desplaza compra.

**Colitas de conejo (Lagurus ovatus) · en uso comercial real, sin receta escrita**
Vanessa dictó el uso: **7 tallos** en cada uno de dos bouquets "con colitas";
**1–3** en arreglos secos; **1 por yugo**; **1 por boutonnière**; y *"a algunos
bouquets les hemos agregado un tallito"*. El excedente **se guarda seco para
coronas de Navidad** — o sea que no hay sobrante real: hay inventario seco.
Contexto ya documentado: **1.170 plantas en Inv 2**, primera vez bajo
invernadero, cosechando desde sem 32, 400 tallos hasta el 11/08.
**Ninguna receta la nombra todavía** — el uso vive solo en la cabeza de Vanessa.

---

*(Las entradas nuevas se agregan arriba de esta línea, con fecha.)*

