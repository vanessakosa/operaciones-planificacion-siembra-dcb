# A10 — Cierre de lote

## Las tres formas de cierre

Una cama no termina de una sola forma. El tipo de cierre determina si el lote
entra al cálculo de rendimiento o solo al análisis de fracasos.

| Motivo | Cuándo | ¿Entra al promedio de rendimiento? |
|---|---|---|
| **Normal** | Se agotó la ventana de cosecha | ✅ Sí |
| **Sacrificio-espacio** | Se saca antes de tiempo por prioridad de siembra | ❌ No — se excluye del promedio |
| **Sacrificio-calidad** | Ya no da tallo vendible (quebradizo, nano) | ❌ No |
| **Sacrificio-enfermedad** | Se saca para evitar contagio al bloque | ❌ No — y se marca en historial de enfermedad de la cama |

**Por qué importa:** un lote sacrificado en semana 8 tiene pocos tallos. Si entra
al promedio sin el motivo, esa variedad parece de bajo rendimiento cuando en
realidad fue interrumpida. Es el mismo problema que se resolvió descartando
los valores atípicos de Matricaria Snowball (37 y 42 semanas).

## La herramienta de decisión de sacrificio

Para el caso más común — sacrificio por espacio — el sistema muestra:

```
Ejemplo:
─────────────────────────────────────────────
Gomphrena 3A-08 — Lote #127
Tallos cosechados:   312  (87% del proyectado)
Semanas restantes:   1.5
Calidad actual:      señal amarilla
─────────────────────────────────────────────
Campanula 3A-08 — siembra programada sem 31
  Si entra sem 31 → cosecha sem 43
  Si entra sem 33 → cosecha sem 45
  Sem 45 ya cubierta por otra fuente

→ RECOMENDACIÓN: sacar la Gomphrena esta semana.
  El 13% restante (~46 tallos, ~$92.000) no justifica
  desplazar 2 semanas la Campanula.
```

**El % de retorno capturado** es el número que quita la culpa emocional.
La cama ya cumplió. No es sacrificarla — es cerrarla.

## Señales de deterioro (escala de calidad visual)

| Señal | Qué significa | Acción |
|---|---|---|
| 🟢 Normal | Ventana activa, producción constante | No tocar salvo costo de oportunidad alto |
| 🟡 Menor densidad floral | Fin natural de ventana | Evaluar con % de retorno |
| 🔴 Quebradizas (bocas de dragón) | Problema en poscosecha, merma en pedido | Sacar — no hay ganancia neta |
| 🔴 Se quedaron en nanas | Cama sin capacidad de recuperar tamaño | Sacar |
| ⛔ Superenfermas | Inoculando el bloque | **Sacar urgente** — el costo es la cama de al lado |

**Las camas ⛔ no son candidatas a "esperar una semana más".** El costo no son
los tallos que se pierden — es el inóculo que están distribuyendo.

## Jerarquía cuando hay conflicto de espacio

1. ¿Hay siembra con **fecha inamovible** (compromiso de venta, bandeja al límite)? → la programada gana
2. ¿La cama tiene **señal ⛔ o 🔴**? → saca ya, sin importar el % de retorno
3. ¿La cama capturó **más del 80% del retorno proyectado**? → la decisión es económica, no emocional
4. ¿La cama está en pico y la siguiente puede esperar una semana? → quedarse vale

## Los campos del cierre

| Campo | Tipo | Lo llena |
|---|---|---|
| Motivo de cierre | Normal / Sacrificio-espacio / Sacrificio-calidad / Sacrificio-enfermedad | Vanessa |
| % retorno capturado al cierre | Automático (REGISTRO ÷ proyectado) | Code |
| Semanas de ventana real | Automático | Code |
| Calidad visual al cierre | 🟢 / 🟡 / 🔴 / ⛔ + texto corto | Vanessa |
| ¿Repite en este bloque? | Sí / Sí con ajuste / No | Vanessa |
| Causa si no repite | Texto corto | Vanessa |
| Prescripción de suelo | Generado desde A11 | Code con validación de Vanessa |

## El criterio de repetir en el bloque

Lo que se evalúa en el cierre normal:
1. **Calidad de los tallos** — escala ★ 1–5, misma de la BITÁCORA
2. **Resiliencia en esa cama** — aguantó bien / justo / no aguantó las condiciones del bloque
3. **Las condiciones del bloque** (luz, agua, suelo) no cambian — están en el perfil fijo de la cama

**La unidad de aprendizaje es variedad × bloque, no variedad sola.**
La misma variedad puede dar ★★★★ en Inv 4 y ★★ en 3B.
Eso es una decisión de programación distinta a "esta variedad es buena o mala".

## La rotación como restricción

Vanessa siempre rota — nunca repite la misma variedad seguida en la misma cama.
Entonces el sistema no pregunta "¿repito?", sino:
**¿Qué rota bien después de esto, y cuándo puedo volver a esta variedad en este bloque?**

Restricciones de rotación conocidas y codificadas:
- Lisianthus en Inv 4 → intercalar marigold, gomphrena o matricaria (biosupresión Fusarium)
- Cama con historial 1+ año de lisianthus → preparación diferenciada obligatoria (A11)
- Cama con señal ⛔ por enfermedad → no sembrar variedad susceptible al mismo patógeno sin la prescripción de A11
