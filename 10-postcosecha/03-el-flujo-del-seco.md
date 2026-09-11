# El flujo del seco — dos corrientes, y sólo una está en el registro

> Dictado de Vanessa, 2026-09-11. Es la explicación de por qué el cruce
> venta/cosecha no cierra, y de dónde sale la línea `forever`.

## El problema, en sus palabras

> *"Normalmente nos queda muy difícil a nivel operativo hacer un corte solo de
> secos. Entonces estamos secando, sobre todo, los sobrantes de sala."*

## Son DOS corrientes distintas, y hay que dejar de tratarlas como una

### Corriente 1 — sobrante de sala · **SÍ está en el registro**

> *"El lunes y el martes, con lo que se cosechó sobre todo el viernes y sobró,
> se suele colgar para secar."*

Ese tallo **se cortó y se contó como fresco** el viernes. Cuando el lunes se
cuelga, no es cosecha nueva: es el mismo tallo cambiando de destino.

**Consecuencia:** no hay doble conteo — el riesgo que había que descartar antes
de cruzar. Pero sí hay cosecha registrada que **nunca se vendió fresca**, y hoy
no se distingue de la que sí. Parte de los **+36.512 tallos** de diferencia del
cruce es esto, no pérdida.

### Corriente 2 — sacada de cama · **NO está en el registro, en absoluto**

> *"Cuando se hace la sacada de la cama con lo que sobra —los tallos enanos, lo
> que sobra— eso se suele cortar para secar, pero de eso no hay registro."*

Este material **nunca se contó**. No infla la diferencia del cruce: es
producción adicional que el registro no ve. **La finca produce más de lo que
dicen los 83.200 tallos.**

Y la cadena explica por qué no se cuenta:

| Paso | Quién | Qué pasa |
|---|---|---|
| 1. Corte | **el que prepara la cama**, no el cortador | *"normalmente no es el que cuenta"* |
| 2. Sube | el mismo | *"lo sube muy crudo"* |
| 3. Cuelga | otra persona | *"lo maquilla y de ahí saca lo que está bueno"* → **segunda merma, tampoco medida** |

Dos pérdidas en serie y ningún conteo en el origen. Pedirle al preparador de
cama que cuente es cambiar el procedimiento de otra persona, y por eso el
problema lleva tiempo sin resolverse.

## La salida: no contar en el origen, derivarlo de la venta

**`Bouquet forever Dream` es el producto de esa corriente.** Y eso lo vuelve el
instrumento de medición que faltaba: si se sabe qué lleva cada forever y cuántos
se vendieron, los tallos secos consumidos salen **hacia atrás**, exactamente
igual que se hizo con todo lo demás en esta sesión.

```
unidades forever vendidas  ×  receta  =  tallos secos consumidos
```

Eso da un **piso** de la corriente 2 — piso, porque no incluye lo que se colgó y
no se vendió todavía. Pero es un número real, sacado de una venta que sí se
registra, en vez de un conteo que operativamente no se puede hacer.

**Escritas el 2026-09-11.** Pero con una salvedad que Vanessa puso de entrada y
que cambia el modelo:

> *"Es muy difícil darte una receta de forever… Yo normalmente trato de que los
> forever tengan un **tamaño**. Tenemos tres tamaños, y ese **volumen** tratamos
> de lograrlo para mantener consistencia, y como los tallos secos suelen ser
> **deshidratados**, a veces se usa un poco más y otras veces menos."*

**El forever se especifica por VOLUMEN, no por conteo.** El operario llena hasta
el tamaño; cuántos tallos entren depende de qué tan deshidratado esté el
material. Por eso las tres recetas se escribieron con **rangos y sustituciones**,
marcadas como composición típica y no como contrato. Es el mismo criterio que se
usó con la Edición Especial, pero por una razón distinta: allá varía **qué hay
en cosecha**, acá varía **cuánto ocupa cada tallo**.

| Producto | Unidades | Precio |
|---|---|---|
| `Bouquet forever Dream pequeño` | 97 | $85.000 |
| `Bouquet forever Dream mediano` | 49 | $120.000 |
| `Bouquet forever Dream grande` | 40 | $140.000 |

La composición crece por tamaño de forma escalonada — statice 5/4/3-4, celosia
3/2-3/1, ammobium 3/3/1, zinnia 3/2/1 — y el grande suma cristata, amaranto
colgante y strawflower que el pequeño no lleva.

## El pintado: un paso de proceso con costo que no está en ningún modelo

> *"A veces le pintamos, por lo menos tres elementos, lo que le da un retroceso
> y un **costo adicional**."*

Es la primera vez que aparece en el repositorio un paso de **transformación con
costo** entre la cosecha y la venta. No es merma ni es insumo de campo: es mano
de obra y material de taller sobre un tallo ya cosechado, y **hoy no está en
`DCB_Modelo_Costos` ni en ninguna parte**.

Importa para el eje de rentabilidad porque va en dirección contraria al resto:
el pintado **sube el costo del tallo después de cortarlo**, así que un forever
pintado no cuesta lo mismo que uno sin pintar aunque lleve los mismos tallos.
Queda anotado en la receta del grande, que es donde Vanessa lo nombró
(matricaria Snowball pintada).

## Larkspur corrobora la lectura

`07-datos/secado_variedad.csv` ya documenta que **Larkspur seca `SI`**, con rol
seco `LINEA` y calidad `BUENA` en Light Blue. Y Larkspur es, por lejos, el grupo
que más vende por encima de lo que figura cosechado:

> cosechó **243** tallos, vendió **879** → faltan al menos **636**

Las dos cosas se explican mutuamente: **Larkspur se vende seco, y el seco viene
sobre todo de sacada de cama, que no se registra.** No es un error del cruce —
es el cruce encontrando exactamente lo que este documento describe.

Espárrago, Trachellium y Amaranto velvet aparecen con el mismo síntoma y valen
la misma revisión.

## Lo que NO se debe hacer

Inventar un porcentaje de merma para "cuadrar" el cruce. Taparía la señal justo
donde es más útil. Las dos mermas de la cadena —la del preparador que sube crudo
y la del que maquilla al colgar— se pueden medir el día que alguien pese o cuente
una sola vez en cada punto. Mientras tanto se nombran y se dejan abiertas.
