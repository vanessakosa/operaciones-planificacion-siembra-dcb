# Estrategia de surtido — color × colección × calendario

> Referenciado desde `07-datos/FUENTES.md` como pendiente de escribir. Arranca
> con Boca de Dragón, la primera variedad cerrada en la revisión una-por-una.
> Se completa variedad por variedad, en el mismo orden de esa revisión.

## Qué mide este documento y qué no

Vanessa pidió cruzar, para cada color de cada variedad: en qué colecciones
puede vender (paquete sólido · paquete mixto · bouquet), qué tan bien
combina, y si el calendario de siembra entrega ese color cuando el mercado
lo pide — para decidir si hay que cambiar cantidades por color o fechas de
entrega.

**Dos piezas de esa pregunta se pueden responder hoy con datos reales. Una
no.**

1. ✅ **Cuándo se cosechó cada color** — `registro_tallos.csv` tiene fecha.
2. ✅ **Cuándo el mercado colombiano empuja o castiga la venta** —
   `calendario_comercial_colombia.csv`, dictado por Vanessa.
3. ❌ **Cuánto se vendió de cada color, en qué colección** — no existe. Ni
   archivo de ventas, ni recipe que fije cultivar. Ver "El bloqueo real" más
   abajo antes de leer las conclusiones de este documento como algo más que
   una hipótesis a validar.

## El bloqueo real: las recetas no saben de qué color es el ramo que arman

Los 9 productos del catálogo que llevan Boca de Dragón la piden como grupo
genérico (`Snapdragon (Boca de Dragón)`), no por cultivar. Eso quiere decir
que **no existe, hoy, un solo registro histórico que diga "este bouquet se
armó con Boca roja"** — cada vez que se armó, el color lo decidió quien tenía
el balde en la mano esa semana, no la receta.

Consecuencia directa para este documento: no se puede evaluar si "el paquete
sólido de Boca vendió mejor en rojo que en lavanda", porque el sistema nunca
distinguió esos dos casos. Lo que sí se puede evaluar es si **la cosecha**
de cada color coincidió con las fechas en que el mercado más lo iba a pedir
— que es la mitad de la pregunta de Vanessa (fechas de entrega), no la mitad
de cantidades vendidas por color (esa necesita el archivo de ventas, bloqueo
ya señalado en `00-contexto/05-donde-vamos.md`).

## Boca de Dragón — cosecha real por color vs. calendario comercial

Ventana de datos: **semana 22 a 32 de 2026 (25 de mayo → 9 de agosto)**. Es
menos de un trimestre — cualquier conclusión de "planificación anual" acá es
provisional hasta tener las 52 semanas.

| Color | Tallos | Semanas activas | Ventana calendario en que cayó |
|---|---|---|---|
| **Rojo** (Cannes Red/Red Delight mezclados, Potomac Crimson) | 3.384 | 23–32 | Empieza en TERRIBLE (jun-jul), termina fuerte en la semana 31 (830 tallos) — ya dentro de **Agosto ALTA / Feria de las Flores** |
| **Albaricoque** (Cannes Light Bronze) | 1.870 | 28–31 | Cae casi entero en Agosto ALTA — la única familia que coincidió bien |
| Naranja (Monaco Orange) | 1.699 | 22–28 | Casi todo dentro de TERRIBLE |
| Rosa medio (Cannes Pink, Opus Pink) | 1.508 | 23–32 | Grueso en TERRIBLE, cola en sem32 (Agosto ALTA) |
| Lavanda (Cannes Lavender + Opus Lavender, mezclados) | 1.390 | 24–29 | Enteramente en TERRIBLE |
| Blanco (Opus Fresh) | 828 | 23–26 | Enteramente en TERRIBLE |
| Rosa fuerte (Monaco Dark Pink) | 552 | 22–31 | Sobre todo en TERRIBLE — y es el color con **desajuste de demanda documentado**: sobró en sem22 pese a "tallos extraordinarios" (`desajuste_demanda.csv`) |
| Rosa claro (Appleblossom, Opus+Potomac) | 310 | 23–32 | Repartido, cola en Agosto ALTA |
| Morado (Potomac Royal) | 30 | 27 | TERRIBLE |

**Lo que se ve, dicho sin adornos:** la mayoría de la cosecha de Boca de
Dragón —blanco, lavanda, naranja, rosa fuerte— quedó concentrada en junio-
julio, que `calendario_comercial_colombia.csv` marca como **el peor período
del año** (vacaciones escolares). Muy poco llegó a agosto, que Vanessa marca
**ALTA** por la Feria de las Flores — con la excepción de Cannes Light
Bronze (albaricoque), que sí aterrizó ahí casi entero, y de Cannes Red, cuyo
pico más grande de toda la temporada (830 tallos) cayó justo en la semana
31, ya dentro de esa ventana alta.

**Pregunta que esto abre, no que esto responde:** ¿el calendario de siembra
se armó pensando en llegar a agosto, o coincidió por accidente con Cannes
Red y Light Bronze? Si la intención real es surtir para Feria de las Flores,
vale la pena mirar si Naranja, Blanco y Lavanda —que llegaron tarde para esa
ventana esta vez— se pueden correr de fecha el próximo ciclo.

## Combinabilidad por color (de `afinidad_color_bocas_dragon.csv`)

De los 9 colores cosechados, **6 tienen fila de afinidad** documentada por
Vanessa (rendimiento en sólido, con qué combina, con qué no). **3 no
—Potomac Appleblossom, Cannes Pink, Monaco Dark Pink— quedaron marcados
`PENDIENTE` en esta sesión** en vez de inventados. Cannes Pink pesa
1.203 tallos y Monaco Dark Pink tiene un desajuste de demanda ya
documentado: son los dos huecos que más urge cerrar antes de intentar
un cruce completo de todos los colores.

## El registro de ventas SÍ existe — corrección a este documento

La primera versión de este documento decía que no existía archivo de ventas.
Estaba mal. Existe, en Drive, carpeta **"Archivos de ventas e inventario"** —
el archivo `Online` tiene el registro real, línea por línea, del canal
online: **91 días de ventas, 7 de mayo al 27 de agosto de 2026**, con fecha,
producto, precio, cantidad y canal de salida. Hay archivos hermanos por punto
físico (Viva Palmas, Tesoro, Euro la Inferior) sin explorar todavía.

**Confirmado por Vanessa (2026-08-27): David se encarga de subir ventas y
devoluciones al repositorio.** No es tarea de esta revisión variedad-por-
variedad armar ese pipeline — lo que sí vale la pena dejar es el método,
probado con casos reales, para cuando ese archivo aterrice:

**Método (dictado por Vanessa): cruzar la fecha en que se subió la venta con
la variedad/color que estaba activo en cosecha ese mismo momento.** Ya
probado arriba con Boca de Dragón semana 27 — funciona, con el límite de que
una semana con varios colores en cosecha simultánea da un conjunto de
candidatos, no un color único.

### Caso real confirmado — el primero de este tipo en el repositorio

Venta del **24/7/2026: "Dream Big blanco"**, $270.000 — mismo precio y mismo
producto que "Dream Big" del catálogo (37 tallos, Boca de Dragón cant. 3–5).
"Blanco" no es un producto aparte: es quien vendió anotando el color de Boca
que realmente llevó ese ramo. Es la primera vez que el repositorio tiene un
dato directo — no inferido — de qué color de Boca se usó en un bouquet
específico. Si esta anotación de color se repite en más ventas del archivo
`Online`, ahí hay una fuente de verdad mejor que el cruce por fecha.

### Dos productos reales que faltaban en el catálogo — agregados

Al revisar el registro de ventas aparecieron dos paquetes mixtos que se
venden con regularidad y no tenían receta: **"Bocas de dragón y plumas"**
(8 ventas registradas) y **"Bocas de dragón y statice"** (3 ventas). Vanessa
confirmó la composición — 6 Boca de dragón + 5 Celosia plumosa, y 6 Boca de
dragón + 5 Statice respectivamente — y quedaron agregadas a
`formulas_productos_bouquets.csv` con el precio observado en las ventas
($50.000 y $45.000).

Un tercer nombre que aparecía, **"Event bocas de dragón 10 tallos"** (15
ventas, la más frecuente de los tres), **no es un producto nuevo** — es
"Bocas de dragón (paquete)" (el mismo de 10 tallos ya en catálogo) vendido
con el 15% de descuento mayorista de eventos. El precio observado es
consistente ($32.300 cada vez) pero **no cuadra con un 15% simple sobre los
$50.000 de catálogo** — $32.300 implica una base de ~$38.000, no $50.000.
Queda anotado como discrepancia sin resolver, no asumida: cuando llegue el
archivo formal de ventas, homologar "Event..." a "Bocas de dragón (paquete)"
con un indicador de canal/descuento, no como SKU aparte.

## Lo que falta para que este documento responda la pregunta completa

1. **El archivo de ventas formal** (bloqueo ya conocido: producto · semana ·
   vendidos · devueltos) — David lo sube. Mientras tanto, "combina bien" y
   "se cosechó a tiempo" siguen siendo proxies, no la respuesta real de si
   se vendió. Cuando llegue, aplicar el método de arriba.
2. **Cultivar fijado en receta** — mientras las recetas no digan de qué
   color se armó cada bouquet, no hay forma de saber si el punto de venta
   mostró la mezcla que Vanessa decidió o la que resultó de lo que había esa
   semana. Es el objetivo central del CLAUDE.md, no un detalle de este
   documento.
3. **Las 3 filas de afinidad pendientes** arriba.
4. **Una temporada completa de datos** — 11 semanas no alcanzan para hablar
   de "planificación anual" con certeza.
