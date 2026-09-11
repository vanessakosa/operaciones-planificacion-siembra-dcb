# La interfaz con el repositorio `Campo`

Vanessa compartió el `CLAUDE.md` de **`Campo`** el 2026-09-11: el repositorio que
lleva las planillas de Drive a Postgres. No compite con éste — **lo contiene por
debajo.** Pero hay tres choques concretos que conviene resolver antes de que los
dos sigan creciendo por separado.

## La división es limpia y está escrita en los dos lados

`Campo` se define por lo que **no** hace:

> *"Tampoco es un repo que decide el modelo de costos —eso viene de finanzas— ni
> que diseña el sistema de siembra."*

Y este repositorio se define por lo que **sí**:

> *"Este repositorio es el estratega del cultivo… el sistema que decide cómo
> sembrar este cultivo de manera eficiente."*

| | `Campo` | Este repositorio |
|---|---|---|
| Qué hace | el **puente**: Drive → Postgres confiable | el **estratega**: qué, cuánto, dónde y cómo sembrar |
| Salida | tres números calculados, no estimados | la decisión de siembra |
| Grano | la **cama** | hoy el **bloque** |
| Almacén | Postgres con restricciones | CSV + Python de librería estándar |

**`Campo` es la versión industrial de la capa de datos que aquí se improvisó en
CSV.** Los dos llegaron por caminos distintos a la misma arquitectura de eventos
con procedencia; eso es una buena señal, no una duplicación.

## Los tres choques

### 1. La unidad mínima: `Campo` dice CAMA, nosotros imputamos por BLOQUE

`Campo` no lo deja abierto:

> **Cama** — La unidad física de siembra. **La unidad mínima de todo.**

`motor/lotes.py` imputa por `bloque × semana`. Es exactamente la pregunta que
este repositorio le iba a hacer a David —*¿alcanza bloque, o hay que bajar a
cama?*— y **su propia especificación ya la contestó.**

El repositorio le da la razón sin haberlo buscado. Los patrones que más valen
aquí son **intra-bloque**, no entre bloques:

- Larkspur y gomphrena van en las camas **inferiores** de 3A; el dianthus fracasó
  en las **superiores**. Mismo bloque, resultado opuesto.
- Lisianthus en 3C es «la cama más problemática del bloque por humedad nocturna».

Imputar por bloque promedia justo la diferencia que se quiere medir.

**Qué hacer:** `ocupacion_lote.csv` ya tiene una columna `camas` vacía y
`area_camas.csv` ya sabe cuántas camas tiene cada bloque. El cambio es de datos,
no de motor: `lotes.reparto()` funciona igual con cama que con bloque. **Lo caro
no es el código: es que el operario registre la cama y no el bloque.** Esa es la
conversación con campo, y `Campo` la va a tener de todos modos.

### 2. «Tallo» sin apellido: `Campo` tiene razón y nos duele exactamente donde dice

> *"«Tallo» sin apellido no significa nada… la diferencia entre los dos **es** la
> merma, que es uno de los tres números."*

`registro_tallos.csv` tiene `Tallos frescos` y `Tallos secos` — que es un eje de
**destino**, no de **calidad**. No existe `tallo calificado` en ninguna parte del
repositorio, y `calidad_tallo.csv` está vacío.

Por eso los **2.231 tallos sin explicar** de la cohorte de Lisianthus (32 % de la
cosecha) no se pueden repartir: pueden ser seco de sacada de cama, descarte por
oidio, o venta posterior al corte del registro. **El vocabulario de `Campo`
nombra el hueco con precisión: nos falta la clasificación.**

Y hay una segunda ambigüedad que `Campo` también anticipa: los tallos de la
sacada de cama **nadie los cuenta**, porque quien los sube es el preparador de
cama, no el cortador. En el vocabulario de `Campo` eso es cosecha no registrada,
y su regla 7 diría: marcarla, no estimarla.

### 3. Insert-only: aquí se reescribe en sitio, y ya nos costó

`Campo`, reglas 5 y 9:

> *"Nada se corrige con `UPDATE`… Las proyecciones se insertan, nunca se
> actualizan."*

Aquí `importar_tallos.py` **reescribe `registro_tallos.csv` completo** en cada
corrida. Ya obligó a un parche: las filas dictadas por Vanessa no se pueden
escribir ahí porque el importador las borraría sin avisar, así que viven en un
archivo aparte.

Y el caso más caro ya está documentado: **las recetas no tienen fecha de
vigencia.** `formulas_productos_bouquets.csv` guarda una sola versión —la de
hoy— y el cruce la aplica hacia atrás a cinco meses de venta. Eso ya inventó 255
tallos de Scabiosa que jamás salieron. La regla 9 de `Campo` es exactamente el
arreglo: cada versión es una fila nueva con su fecha, y la anterior queda
apuntando a la que la reemplazó.

## Donde los dos coinciden sin haberlo acordado

| Principio | `Campo` | Aquí |
|---|---|---|
| El origen no se toca | regla 1 | Drive es la fuente; los CSV son espejo |
| Lo que no se sabe se marca, no se inventa | regla 7 | `SIN_DATO` · `APROX` · el motor se niega a estimar |
| Nada se descarta en silencio | regla 10 | `NO SE PUDO IMPUTAR`, con el motivo |
| Procedencia por fila | `raw` con archivo/pestaña/fila | columna `fuente` en cada CSV |
| La labor siempre lleva ciclo | regla 6 | `labores_lote.csv` lo **deriva** del cruce |

Esa última fila es una diferencia de método que vale discutir: `Campo` quiere el
ciclo **anotado en origen**; aquí se **deduce** de dónde estaba sembrado. Deducir
es más barato para el operario y más frágil: si la ocupación está mal, la labor
se le carga a la cosecha equivocada. Las dos son defendibles; la que no es
defendible es no tener ninguna.

## La crítica que hay que aceptar

> *"No dejar reglas sólo en un prompt. Si una regla importa de verdad, además de
> escribirla hay que hacerla cumplir en código. Una regla escrita se incumple sin
> que nadie se entere; una restricción en la base no."*

Es una crítica legítima a este repositorio. Una parte grande de lo que lo
gobierna vive en `CLAUDE.md` —las ocho reglas no negociables, la jerarquía de
verdad, las advertencias sobre cómo leer cada número— y **sólo algunas están
forzadas en código**. Las que sí lo están (el motor reporta `SIN_DATO` y se
niega a estimar; `bomba.py semana` exige la rotación antes de recomendar;
`dictar_tallos.py` rechaza fechas futuras y filas sin bloque) son precisamente
las que nunca se han incumplido.

**El camino no es mover este repositorio a Postgres.** Es que las reglas que de
verdad importan bajen a `Campo` como restricciones de base, y que aquí quede la
estrategia — que es lo que un prompt sí sabe hacer.

## La pregunta que hay que llevarle a David

No es «¿cama o bloque?» —eso ya lo contestó su especificación—. Es:

> **¿Este repositorio lee de Postgres cuando `Campo` esté listo, o siguen los dos
> con sus propios espejos de Drive?**

Si lee de Postgres, los seis archivos de la ficha por cosecha dejan de ser
almacén y pasan a ser **vistas**: `ocupacion_lote` es la tabla de ciclos de
`Campo`, `aplicaciones_lote` son sus aplicaciones, `labores_lote` su labor. El
motor de imputación de `lotes.py` sigue valiendo igual — pasa a ser una consulta.

Si siguen separados, hay que decidir cuál manda cuando los dos tengan el mismo
número distinto, y eso es peor que elegir ahora.
