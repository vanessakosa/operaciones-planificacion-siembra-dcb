# Proyección semana 38 — Amor y Amistad

> Corte 2026-09-03 (semana ISO 36). **Segunda versión**, corregida con el dictado
> de Vanessa del mismo día. Anclada en `registro_tallos.csv` (ritmo real medido,
> semanas 29–32) y en tallos/planta **medidos** donde existen.

---

## La respuesta

**Entre 1.600 y 3.400 tallos con lo que está confirmado — centro ~2.400.**
(Tercera pasada: el Ammi del 6ext se cayó — *"no se ven tallos formados"*.)

Contra un ritmo real de **6.526 tallos/semana** en las semanas 29–32, la semana
del pico comercial llega a **menos de la mitad**.

### Qué cambió respecto a la primera versión

La primera versión daba 2.600–4.600 con centro en 3.600, y **apoyaba el número en
dos pilares que no existen**:

| | v1 decía | Realidad | Efecto |
|---|---|---|---|
| **Boca de Dragón** | 800–1.100 — *"el pilar de la semana"* | Opus Fresh 3A y Appleblossom arrancaron en la **36**, no en la 37. Con ventana de 2–3 semanas, la 38 los agarra en la cola | **−800** |
| **Campanula** | 200–400 | Igual: empieza la 36, pico la 37. *"En la 38 no va a quedar casi nada"* | **−250** |

El error de raíz fue el mismo en los dos casos: **tomé la semana de inicio
registrada en CAMPO como si fuera observación, cuando era proyección.** Los dos
lotes decían "inicio 37" en la hoja y en el campo arrancaron en la 36. Cuando el
dato de campo y la hoja se contradicen, manda el campo — está en la jerarquía de
verdad del proyecto y no lo apliqué.

---

## Grupo por grupo — versión corregida

| Grupo | Real s29–32 | Sem 38 | Base del número |
|---|---|---|---|
| **Gomphrena** | 79 | **550–900** | 🟢 **El nuevo pilar.** Carmine Inv5 (1.728 pl, inicio registrado en la 38), Salmon 4B (730 pl) y Pink 4A, las tres *"terminando de madurarse"*. Calculado con **1,14 tallos/planta medidos** en Quis Carmine, no con el teórico de 3 |
| **Carthamus Zanzibar** | — | **SIN_DATO** | 🟡 4A, 1.900 plantas, **inicio de cosecha registrado en la semana 38** — la hoja y el campo coinciden. Pero `ciclos_variedad.csv` **no tiene tallos/planta** para Carthamus. Si diera 1 tallo/planta serían ~475/semana; si diera 2, el doble. **Es la carta más grande que queda y no se puede cuantificar** |
| Resto (Matricaria · Ammobium · Amaranto · Strawflower) | ~820 | 300–500 | Sin reporte de campo; decaimiento del promedio |
| **Statice** | 1.299 | **250–500** | Quedan tres camas pequeñas. El blanco ya salió, Forever Happy arrancó en la 27 y se agota, Forever Silver 3C entra con **tallos cortos** |
| **Ammi** | 290 | **100–250** | ⬇️ Solo el de **3EXT**, que empieza la 37. El **6ext no llega**: la hoja le pone inicio en la 38 pero en campo *"no se ven tallos formados"* |
| Dusty Miller | 84 | 150–300 | *"Todavía hay bastante"* |
| **Celosia** | 1.065 | **50–200** | 🔴 Toda la Shimmer (3A, Mini, 3B) cierra **esta semana**. Solo *"algunos centrales"* de las de otoño — que llegan tarde, ver abajo |
| Trachelium | 15 | 100–250 | Mini agotado; el 5 con tallos torcidos; otra cama en formación |
| Lisianthus | 999 | 100–200 | *"Insignificante"* |
| Green Ball | 439 | 100–200 | La 4B cerró alrededor de la 36 |
| **Boca de Dragón** | 1.049 | **0** | ⬇️ Opus Fresh arrancó en la 36; **Appleblossom (4B y 3C) termina ciclo en la 37**. No queda nada para la 38 |
| **Campanula** | 2 | **0–100** | ⬇️ Pico en la 37 |
| Zinnia · Girasol · Colitas de conejo | 424 | **0** | Zinnia en cero desde la 32; girasol con tallos delgados; conejo cierra la 37 |

---

## Las celosias de otoño llegan tarde para el pico — pico real: semanas 41 a 43

Esto responde lo que preguntaste. Sembradas en la **semana 27**, en una cama del
4A y una del 3A. Con las medidas de `capacidad_bloques.csv`:

| | Huecos × líneas | Sitios |
|---|---|---|
| 1 cama Inv 4A | 112 × 8 | 896 |
| 1 cama Inv 3A | 198 × 8 | 1.584 |
| | **Tope de cama** | **2.480** |

Corriendo el ciclo desde la semana 27:

| Si son… | Cosecha | Techo de tallos | Con realización 0,24 |
|---|---|---|---|
| **Cristata** (14 sem, ventana 3, 1 t/planta) | **sem 41–43** | 2.480 | ~198/semana |
| **Plumosa** (14 sem, ventana 4, 4 t/planta) | **sem 41–44** | 9.920 | ~595/semana |

**Su producción máxima cae en las semanas 41 a 43, no en la 38.** Para el pico
solo alcanzan *"algunos centrales"*, tal como dijiste — y eso es adelanto sobre
el ciclo, coherente con el problema de luz que ya adelantó al lisianthus y a la
cristata.

🔴 **No está registrado si Autumn Blaze y Sangría son cristata o plumosa, y la
diferencia son 4× los tallos** (2.480 contra 9.920). Es el dato más barato de
conseguir de toda esta proyección y el que más mueve el número de octubre.

---

## Las dos incógnitas que deciden si son 2.400 o 3.200

**1. Carthamus Zanzibar no tiene tallos/planta en ningún CSV.** Es el único lote
grande cuyo inicio de cosecha cae exactamente en la semana 38, con 1.900 plantas
y confirmación de campo (*"en formación de botones, va a estar perfecto para esa
época"*). Es, con diferencia, la carta más grande que le queda al pico — y el
repositorio no puede decir cuántos tallos son.

→ **Contar tallos por planta en una muestra esta semana.** Es media hora de
trabajo y es la diferencia entre planear el pico a ciegas o con número.

**2. Autumn Blaze y Sangría no están registradas.** Cero filas en CAMPO. No
tienen semana de siembra, ni bloque, ni cantidad, ni nombre homologado — así que
ni entran en esta proyección ni van a aparecer en el calendario de Erica.

---

## Lo que esto significa

**El pico no se sostiene con lo que hay, y ya no se puede sembrar** — nada
plantado hoy llega antes de la semana 45. Y la composición cambió por completo:

> El bouquet de Amor y Amistad hay que rediseñarlo alrededor de **Gomphrena y
> Carthamus**, no de Boca de Dragón, Celosia ni Lisianthus.

Gomphrena es flor de bola y Carthamus es textura espinosa: **entre las dos no hay
una sola flor de foco**. Esa es la conversación de bouquet que toca esta semana,
y es un problema de estructura, no de volumen.

Las tres palancas que quedan sobre la semana 38, todas de manejo:

1. **Rediseñar la receta** alrededor de Gomphrena + Carthamus, resolviendo la
   falta de foco.
2. **Medir el Carthamus ya**, para saber si son 400 o 900 tallos.
3. **Decidir si se compra tallo de fuera**, que es la única palanca que actúa
   sobre la 38 en el plazo que queda.

---

## Cuánta confianza tiene esto

**Baja en el total, alta en la dirección.** Lo que sostiene el número:

- Gomphrena se calculó con **tallos/planta medidos en campo** (1,14 en Quis
  Carmine), no con el teórico. Es la línea más sólida.
- Boca de Dragón y Campanula caen por **observación directa de Vanessa**, que
  gana sobre la hoja.
- Carthamus y las celosias nuevas son **SIN_DATO declarado**, no estimación
  disfrazada.

Lo que sigue sin resolver y afecta a esto: 33.399 plantas sin fila en
`ciclos_variedad.csv` (casi todas celosia), cero mortalidad medida, y
`calidad_tallo.csv` vacío justo cuando hay cuatro observaciones de tallo corto o
delgado en una sola sesión.
