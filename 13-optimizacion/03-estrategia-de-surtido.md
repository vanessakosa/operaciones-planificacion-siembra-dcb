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

## Lo que falta para que este documento responda la pregunta completa

1. **El archivo de ventas** (bloqueo ya conocido: producto · semana ·
   vendidos · devueltos) — sin esto, "combina bien" y "se cosechó a tiempo"
   siguen siendo proxies, no la respuesta real de si se vendió.
2. **Cultivar fijado en receta** — mientras las recetas no digan de qué
   color se armó cada bouquet, no hay forma de saber si el punto de venta
   mostró la mezcla que Vanessa decidió o la que resultó de lo que había esa
   semana. Es el objetivo central del CLAUDE.md, no un detalle de este
   documento.
3. **Las 3 filas de afinidad pendientes** arriba.
4. **Una temporada completa de datos** — 11 semanas no alcanzan para hablar
   de "planificación anual" con certeza.
