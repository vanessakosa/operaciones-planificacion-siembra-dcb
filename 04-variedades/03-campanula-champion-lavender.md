# Campanula Champion Lavender — resolución del conflicto

```bash
python3 motor/cerebro.py rendimiento Campanula
```

## El conflicto

Dos fuentes del repositorio se contradecían:

| Fuente | Dice |
|---|---|
| `decisiones_manejo.csv` (2026-07-07) | **SACAR** del cultivo definitivamente. Rindió 0.64 tallos/planta contra 0.92 de la blanca en el mismo bloque. Flor sin comprador se marchitó por polinizadores. |
| `variedades_bitacora.csv` (CAMBIOS SEM24) | **MANTENER** en zona correcta. Segundo ciclo con tallos cortos en 3B por estrés hídrico crónico. 3A con riego consistente da tallos excelentes. *"Variedad viable — problema es zona, no variedad."* |

## Veredicto: el argumento de rendimiento no se sostiene

El 0.64 vs 0.92 es reproducible desde los datos crudos. Lo que no se sostiene es
la conclusión que se sacó de él, porque **las dos ventanas de cosecha no llevaban
el mismo tiempo transcurrido.**

Inv 3B — misma cama, misma agua, misma luz, mismo suelo:

| Variedad | Plantas | Tallos | Días de ventana | Tallos/planta | **Tallos/planta/día** |
|---|---|---|---|---|---|
| Champion White | 1.370 | 1.267 | 27 | 0.92 | **0.0343** |
| Champion Lavender | 1.918 | 1.231 | **18** ⚠ abierta | 0.64 | **0.0357** |

**Normalizado por día, la lavanda rinde 4 % MÁS que la blanca.** El 0.64 no mide
peor productividad: mide nueve días menos de cosecha registrada.

Y la ventana de la lavanda estaba **abierta** cuando el registro se cortó
(último corte 2026-07-03, que es el último día del archivo). La blanca ya había
cerrado el 2026-06-30. Si la lavanda hubiera corrido los mismos 27 días al mismo
ritmo, habría llegado a ~0.96 tallos/planta — por encima de la blanca.

### Por qué importa el modo de error

Es el mismo error que `09-procedimientos/C-cierre-de-lote.md` ya advierte para
los lotes sacrificados: *un lote interrumpido parece de bajo rendimiento cuando
en realidad fue interrumpido.* Aquí la interrupción no fue un sacrificio, fue el
corte del registro — pero el sesgo es idéntico.

Por eso quedó codificado en `motor/cerebro.py` → `rendimiento`, que normaliza por
ventana y marca con `<- ABIERTA` los lotes cuyo último corte coincide con el
final del archivo. Cualquier comparación futura entre variedades pasa por ahí.

## Lo que cada fuente tenía bien

- **La bitácora tiene razón en que la variedad es viable.** Los números la
  respaldan, aunque no por el motivo que ella da: la lavanda iguala a la blanca
  *dentro de 3B*, o sea incluso bajo el estrés hídrico.
- **La bitácora tiene razón en la regla de zona**, pero esa regla no es sobre la
  lavanda: es sobre 3B. `01-invernaderos.md` documenta doble limitante en 3B
  (suelo degradado + presión de agua insuficiente) y la regla dice *campánula NO
  en 3B hasta resolver la bomba*. **Eso aplica igual a la blanca y a la rosada.**
- **`decisiones_manejo.csv` tiene razón en que hay un problema**, pero el
  problema no es rendimiento. Son las otras dos cosas que ese mismo registro
  menciona y que nadie cuantificó: **tallo corto** (calidad) y **flor sin
  comprador marchitada por polinizadores** (demanda + daño). Ninguna de las dos
  se mide en tallos por planta.

## Recomendación

**No sacar la variedad. Sacar la campánula de 3B — toda, no solo la lavanda —
hasta que se resuelva la bomba de presión.**

El ensayo que zanja la pregunta de zona ya está en el suelo: **2.192 plantas de
Champion Lavender en 3A, cosecha proyectada agosto** (`campo_siembras.csv`).
Todavía no ha producido un solo registro de cosecha. Cuando lo haga, correr
`rendimiento Campanula` y comparar 3A contra 3B da la respuesta limpia.

## Lo que sigue siendo decisión de Vanessa

El rendimiento ya no es argumento. Quedan dos preguntas que los datos no
responden:

1. **¿El tallo corto en 3B descalifica la lavanda comercialmente?** El repositorio
   no registra longitud de tallo en ninguna parte. Si esa es la razón real para
   sacarla, hay que empezar a medirla — hoy no es un dato, es una impresión.
2. **¿Hay comprador para el lavanda?** `decisiones_manejo.csv` dice que la flor se
   marchitó sin comprador. Eso es un problema de demanda, no de campo, y la
   bitácora lo contradice: *"Vende muy bien"*. Esa contradicción sí es tuya.

## Hallazgo lateral: Champion Pink

En la misma cama de 3B, la rosada rinde **0.0755 tallos/planta/día — 2,2 veces
más que la blanca y la lavanda.**

| Variedad | Plantas | Tallos/planta/día |
|---|---|---|
| Champion Pink | 200 | 0.0755 |
| Champion Lavender | 1.918 | 0.0357 |
| Champion White | 1.370 | 0.0343 |

Con 200 plantas la muestra es chica y no da para concluir. Pero la bitácora dice
que *"clientes y wedding planners la prefieren sobre el blanco para bouquets"*.
Si además rinde el doble por planta, **la pregunta interesante no es si sacar la
lavanda: es por qué la rosada tiene 200 plantas y la lavanda 1.918.**

Vale sembrar rosada en volumen comparable y medirlo con `rendimiento`.

## Error de datos detectado

Tres lotes de campánula de 3B tienen un corte fechado **2025-06-17** dentro de
una cosecha que ocurre toda en junio de 2026. Es un error de año en el registro.
El motor los excluye del cálculo de ventana y los reporta, pero **hay que
corregirlos en la fuente** (`DCB_Registro_Tallos`, hoja REGISTRO).
