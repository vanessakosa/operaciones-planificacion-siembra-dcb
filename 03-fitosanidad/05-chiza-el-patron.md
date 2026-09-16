# Chiza (gallina ciega) — el patrón, y la pregunta que lo ordena

> Dictado por Vanessa el 2026-09-16, cerrando la sesión del drench. Este documento existe
> porque ella hizo la pregunta correcta: **¿por qué las bocas de dragón, y por qué en tres
> bloques distintos a la vez?**

## Los cuatro eventos que hay registrados

| Cuándo | Bloque | Variedad | Desenlace |
|---|---|---|---|
| Anterior (fecha SIN_DATO) | **3A** | **Dianthus** | Emergencia. **Controlada** con drench — el motivo por el que se compró el Deep Green |
| Anterior (fecha SIN_DATO) | **3A** | **Statice** | SIN_DATO |
| 2026-09-16 | **3B** | Boca de dragón | En manejo |
| 2026-09-16 | **4A** · **4B** | Boca de dragón | En manejo |

**Vanessa: *"ellas tienen como épocas, ciclos."*** Es la observación que hay que medir: si la
chiza aparece en ventanas del año, el manejo deja de ser reactivo y pasa a ser calendario.
**Falta la fecha de los dos eventos de 3A** — sin eso no se puede ver el ciclo.

## La pregunta: ¿están seleccionando las bocas de dragón?

Parece que sí: tres bloques distintos, una sola variedad. Pero los datos de
`campo_siembras.csv` dicen otra cosa, y son dos argumentos.

### 1. La boca de dragón es el 20 % de todas las siembras de la finca

**60 de 302 siembras**, repartidas en **13 bloques distintos.** Es la variedad más sembrada y
la que está presente en más sitios al mismo tiempo:

| Bloque | Siembras de boca de dragón | Sobre el total del bloque |
|---|---|---|
| **4A** | 14 | de 35 — **40 %** |
| 3A | 13 | de 35 |
| **3B** | 7 | de 29 — 24 % |
| **4B** | 4 | de 14 — 29 % |

Si una plaga de suelo aparece en tres bloques a la vez, **la variedad con más probabilidad de
estar en los tres es justamente la boca de dragón.** Eso es sesgo de exposición, no preferencia.

### 2. Y el argumento que lo cierra: en 3A la chiza NO fue a las bocas de dragón

**3A tiene 13 siembras de boca de dragón registradas** — casi tantas como 4A. Y sin embargo,
cuando hubo chiza en 3A, fue al **Dianthus** y al **Statice**.

> **Si hubiera preferencia por la boca de dragón, en 3A habría ido a ella.** No fue.

## Lo que queda como hipótesis, en orden de fuerza

| # | Hipótesis | Cómo se verifica |
|---|---|---|
| 1 | **No seleccionan variedad: coinciden con lo que está tierno.** La larva L3 —el estadio que más come— cae en una ventana del año, y arrasa con la raíz nueva que encuentre. Boca de dragón en 3B/4A/4B ahora, Dianthus y Statice en 3A entonces | **Fecha de trasplante de las camas afectadas.** Si las tres son de la misma ventana, se sostiene |
| 2 | **La postura sigue a la preparación de cama.** La hembra pone donde hay materia orgánica fresca y cobertura. Camas preparadas en la misma tanda de bokashi = mismas camas atacadas | Cruzar las camas afectadas contra la fecha de preparación |
| 3 | **Preferencia real de hospedero** | Es la que los datos **no** respaldan hoy, por el caso de 3A |

## El experimento que está en el campo ahora mismo, y es gratis

> **¿Qué más hay sembrado en 3B, 4A y 4B en este momento, y está sano?**

Es la observación que decide entre las tres hipótesis, y no cuesta nada:

- Si hay **otra variedad en la cama de al lado, intacta** → sí hay selección, y la hipótesis 3
  vuelve a la mesa.
- Si lo demás de esos bloques es **más viejo, con raíz ya leñosa** → es la hipótesis 1: no
  eligieron, encontraron.
- Si lo demás está **igual de afectado y no se había notado** → no es un problema de bocas de
  dragón: es un problema de los tres bloques.

## Lo que falta para cerrar todo esto

1. **Fecha (año y época) de los dos eventos de 3A.** Es lo que convierte *"tienen ciclos"* en un
   calendario de manejo.
2. **Fecha de trasplante de las camas afectadas hoy.** Decide la hipótesis 1.
3. **Qué hay sano al lado**, de la pregunta de arriba.
4. **Dosis y resultado del control de 3A** — funcionó, y no está escrito con qué números.
5. **Conteo de la trampa de luz**, semana a semana. Es la única forma de medir presión con el
   ground cover puesto, y lo que confirmaría o tumbaría lo de los ciclos.

## Manejo vigente

Ver `07-datos/decisiones_manejo.csv` (2026-09-16) y la hoja
`05-programacion/hojas-operario/drench-chiza.html`.

**Deep Green 1 cc/L en tanques de 200 L, por fertirriego, con la cama llevada a capacidad de
campo antes.** Dosis dictada por Vanessa: 0,7 cc/L normal, **1 cc/L en incidencia alta**.
Operario: Tilio.
