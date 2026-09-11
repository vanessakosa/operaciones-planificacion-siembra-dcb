# La arquitectura de la ficha por cosecha

**Vanessa, 2026-09-11**, pidiendo lo que sigue después del caso Lisianthus:

> *"La idea es que lo podamos tener de cada variedad en cada cosecha. Que yo
> pueda decir: en esta época del año la cosecha fue mucho más productiva; la
> cosecha fue productiva pero no se vendió; la demanda fue alta. Que empecemos a
> contrastar entre campánulas: la campánula lavanda no fue así, tuvimos que
> hacerle muchas más aplicaciones, la campánula rosa ganó."*

> *"Necesito un lugar donde viva esa información, donde yo pueda abrir una nueva
> conversación, decir 'diseñá la bomba semanal según lo que está sucediendo', y
> eso se guarde. Si tú sabes que en semana 37 apliqué esta bomba, y en semana 37
> está sembrado este número de variedades, yo sé que ese número de variedades la
> recibieron. **Eso se lo va sumando la ficha.**"*

## La idea, que es una sola

```
    una bomba se aplica a un BLOQUE en una SEMANA
    una cosecha ocupa un BLOQUE durante un RANGO DE SEMANAS
                           ↓
               el cruce es (bloque × semana)
```

Todo lo demás sale de ahí. No hay que anotar a qué variedad se le aplicó cada
cosa: **se deduce de dónde estaba sembrada esa semana.** El operario registra lo
que hace por bloque, que es como trabaja de todos modos, y la ficha de cada
cosecha se arma sola.

Esa deducción vive en `motor/lotes.py`, y es la única pieza conceptual nueva.

## Las piezas

| Archivo | Qué es | Grano |
|---|---|---|
| `07-datos/ciclos_observados.csv` | **quién es** la cohorte y **cómo le fue** | 1 por cosecha |
| **`07-datos/ocupacion_lote.csv`** | **dónde y cuándo estuvo — LA LLAVE** | 1 por cosecha × bloque |
| `07-datos/bombas_catalogo.csv` | la receta de cada bomba, con vigencia | 1 por bomba × producto |
| `07-datos/aplicaciones_lote.csv` | **evento**: qué bomba, qué bloque, qué semana | 1 por aplicación |
| `07-datos/fertirriego_lote.csv` | evento, misma forma | 1 por fertirriego |
| `07-datos/labores_lote.csv` | evento, misma forma + días y jornal | 1 por labor |
| `07-datos/infraestructura_lote.csv` | dotación: mallas, luz, plástico | 1 por cosecha × elemento |
| `07-datos/inputs_cohorte.csv` | lo dictado que no es evento fechado | 1 por cosecha × insumo |
| `07-datos/costos_productos.csv` | **el precio. Hoy vacío: es el bloqueo** | 1 por producto |

Los tres archivos de **evento** tienen la misma forma a propósito —
`fecha · semana_iso · bloque · qué · cuánto` — para que el motor los impute con
el mismo código. Agregar una cuarta categoría (riego, poda, cosecha por lote) es
copiar el patrón, no tocar el motor.

## Cómo reparte cuando hay varias cosechas en un bloque

Un evento en el bloque B la semana W se le carga a **toda** cohorte que ocupaba B
esa semana, **prorrateado por área**. Si el área no se conoce, se reparte en
partes iguales y el resultado sale marcado **`APROX`**.

> **Nunca se inventa un número y se presenta como medido.** `APROX` en la ficha
> significa «esto es un reparto, no una medición», y la forma de quitarlo es
> llenar `area_m2` en `ocupacion_lote.csv`.

Y cuando un evento **no se puede imputar** —porque no dice el bloque, o porque
ninguna cohorte estaba ahí— no se descarta en silencio: sale en la ficha bajo
**`NO SE PUDO IMPUTAR`** con el motivo. Es trabajo pendiente, no ruido.

El primer caso real es la bomba del 2026-07-03: su columna `Destino` dice
`idem`, así que no se le puede sumar a nadie. Ese es exactamente el motivo por
el que `aplicaciones_lote.csv` existe aparte del historial de Drive.

## La sesión semanal de bombas

```bash
python3 motor/bomba.py semana 37     # PRIMERO, siempre
python3 motor/bomba.py catalogo      # las bombas y sus dosis por tanque de 25 L
python3 motor/bomba.py registrar 2026-09-12 37 "3B,3C" CHOQUE-BO 4 Wilson "oidio en lisianthus"
```

**`semana` es la regla APLICACIONES hecha comando.** Imprime tres cosas antes de
que nadie proponga una mezcla:

1. La rotación de las últimas 4 semanas — contra qué hay que rotar.
2. **Qué cosechas hay en cada bloque esa semana** — a quién le va a caer.
3. La incidencia fitosanitaria conocida de esos bloques.

Si no hay registro de las semanas anteriores, lo dice y se niega a hablar de
rotación. No hay forma de saltárselo «de memoria».

`registrar` valida contra el catálogo y contra los bloques reales de
`area_camas.csv`, y **al terminar dice a qué cosechas se les acaba de sumar.**
Si no se le suma a ninguna, avisa — normalmente significa que falta la fila en
`ocupacion_lote.csv`.

## El problema del nombre del bloque

El registro escribe el mismo bloque de **45 formas distintas** («3B», «3b»,
«Inv 3B», «Mini 3C Y 3B», «3AB», «5?»…). Sin resolver eso el cruce no existe.

La tabla canónica es **`area_camas.csv`**, que ya traía la columna
`alias_registro`. `lotes.bloques_de()` la usa para colapsar cualquier escritura a
los 15 bloques reales, y reconoce varios en un mismo texto: `"Mini 3C Y 3B"` →
`['Mini', '3C', '3B']`. Los alias largos ganan sobre los cortos, para que
`Ext 3B` no se confunda con `3B`.

## Qué se puede contestar hoy y qué falta

La ficha ya imputa. Lo que le falta para contestar la pregunta de Vanessa
—*¿dónde se nos está fugando el dinero?*— es **precio**, no estructura:

| Para contestar | Falta |
|---|---|
| ¿cuánto costó la fitosanidad de esta cosecha? | `costos_productos.csv` — **vacío, 0 filas** |
| ¿cuánto costó la mano de obra? | confirmar el jornal (~$100.000) con David |
| ¿cuánto costó la luz? | no existe registro de horas de luz ni de consumo en el repo |
| ¿cuántas líneas de malla? | no está por lote en ninguna parte |
| ¿cómo se reparte el área entre bloques? | `area_m2` de `ocupacion_lote.csv` |

**Ninguno de esos cinco es un problema de diseño: son cinco columnas por llenar.**
La arquitectura no cambia cuando lleguen.

## El orden para seguir

1. **Llenar `ocupacion_lote.csv` con las cohortes vivas.** Es lo que hace que
   toda aplicación futura se impute sola. Sin esto lo demás no sirve.
2. **Empezar a registrar las bombas con bloque**, con `bomba.py registrar`. A
   partir de la primera semana registrada, la ficha empieza a sumar sola.
3. **Precio por producto** en `costos_productos.csv`.
4. Recorrer variedad por variedad con `ficha_completa.py`.
5. Recién entonces, el análisis de programación: dónde invertir más y dónde se
   está fugando la plata. **Ese es el destino, y es el paso 5, no el 1.**
