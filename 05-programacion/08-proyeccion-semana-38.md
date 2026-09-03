# Proyección semana 38 — Amor y Amistad

> Corte 2026-09-03 (semana ISO 36). Construida sobre `registro_tallos.csv`
> (ritmo real medido, semanas 29–32) corregido lote por lote con el brain dump
> de campo de Vanessa del 2026-09-03.
> **Es una estimación con rango, no una cifra.** El método está abajo para que
> se pueda discutir cada línea.

---

## La respuesta

**Entre 2.600 y 4.600 tallos, con centro en ~3.600.**

El ritmo real de las semanas 29 a 32 fue **6.526 tallos/semana** de promedio.
La semana 38 llega a **poco más de la mitad de eso** — y es la semana del pico
comercial de Amor y Amistad.

Dos métodos independientes coinciden, lo cual da cierta confianza:

| Método | Semana 38 |
|---|---|
| `cerebro.py huecos` (ciclo teórico × factor de realización 0,24) | 3.904 |
| Suma grupo por grupo sobre el ritmo real + reporte de campo | 2.600–4.600 |

Coinciden **en el total pero no en la composición**, y la diferencia importa:
el motor pone Trachelium (978) y Dusty Miller (954) como los dos primeros, y eso
no se sostiene contra lo medido —Trachelium nunca ha pasado de 60 tallos en una
semana y Dusty Miller promedia 84—. El motor los infla porque
`ciclos_variedad.csv` les asigna 6 y 8 tallos por planta. **La coincidencia del
total es en parte casualidad.**

---

## Grupo por grupo

| Grupo | Real prom. s29–32 | Sem 38 | Por qué |
|---|---|---|---|
| **Boca de Dragón** | 1.049 | **800–1.100** | Opus Fresh 3A y Opus Appleblossom, ambos con inicio registrado en la 37 y ventana de 2–3 semanas → la 38 les cae en pleno centro. **Es el pilar de la semana.** |
| **Statice** | 1.299 | **300–600** | Forever Happy (3A+3B+4A) arrancó en la 27 y con ventana de 4–8 semanas se está agotando. El blanco ya se sacó. Forever Silver 3C arranca pero con tallos cortos |
| **Gomphrena** | 79 | **300–500** | El único grupo que va **hacia arriba**. Carmine 5 con inicio registrado en la 38, Salmon Pastel 4B y Quis Pink 2 desde la 37, y Vanessa arranca a cosechar carmines hoy |
| **Campanula** | 2 | **200–400** | La 4C (rosado + blanco, 3.014 pl) florece la 36 y se cosecha la 37; la 38 la agarra ya de bajada |
| **Ammi** | 290 | **150–300** | Ammi Majus 6ext con inicio en la 38 |
| **Dusty Miller** | 84 | **150–300** | *"Todavía hay bastante"*. Por encima de su promedio, pero lejos de los 954 del motor |
| **Trachelium** | 15 | **100–250** | Mini agotado, el 5 con tallos torcidos, otra cama en formación. Nunca ha superado 60/semana |
| **Celosia** | 1.065 | **100–300** | 🔴 **El derrumbe.** Ver abajo |
| **Lisianthus** | 999 | **100–200** | *"Insignificante… máximo ponerle un lisianthus a los bouquets más grandes"* |
| **Green Ball** | 439 | **100–200** | La 4B arrancó en la 33 con ventana de 3 semanas → cierra alrededor de la 36 |
| Matricaria · Ammobium · Amaranto · Strawflower · resto | ~820 | **300–500** | Sin reporte de campo esta sesión; se asume decaimiento del promedio |
| Zinnia | 374 | **0** | Ya en cero desde la semana 32 |
| Girasol | — | **0** | Media cama en 4B, tallos demasiado delgados, hay que dejar madurar |
| Colitas de conejo | 50 | **0** | Cierran en la 37 |

---

## Lo que de verdad rompe la semana 38: la celosia

Celosia venía aportando **1.065 tallos/semana** — el segundo grupo del cultivo.
Para la semana 38 se queda en 100–300, y el brain dump explica exactamente por
qué, cama por cama:

- Las del **3A (serie Floret + Shimmer)** ya están pasadas → salen en la 36.
- Las **Floret rojas y las últimas rosadas** se acaban en la 37.
- Las **cristata del 3A y del 4A alta** — sembradas apuntando a Amor y Amistad,
  con `AMOR` escrito en la columna `Inicio cosecha` — **adelantaron el ciclo por
  el problema de luz** y terminan al final de la 37.
- Queda **una sola cama de cristata en pie** a ver si resiste.
- Las **"de otoño" (rojas y moradas, 3A baja + bloque 4)** darían solo *"algunos
  centrales"* en la 38.

**El respaldo de Amor y Amistad falló por la misma causa que el titular.** El
lisianthus se adelantó por luz, la celosia entró como plan B, y la celosia se
adelantó por luz también. No quedó tercer plan.

---

## Lo que esto significa para el pico

**No alcanza, y ya no se puede sembrar para arreglarlo** — nada plantado hoy
llega antes de la semana 45. Las palancas que quedan para la 38 son tres, y
las tres son de manejo, no de siembra:

1. **Rediseñar el bouquet alrededor de lo que sí va a haber**, que es Boca de
   Dragón y Gomphrena, no Celosia ni Lisianthus. Es trabajo de `cerebro.py
   auditar` y de la skill de bouquets, y hay que hacerlo esta semana, no la
   entrante.
2. **Estirar lo que se pueda estirar.** `cierres_lote.csv` documenta cuatro
   lotes cerrados históricamente con el motivo `temprano` y el comentario
   *"hubiesen aguantado 1 semana más"*. Esta vez esa semana vale doble.
3. **Decidir ya si se compra tallo de fuera** para el pico. Es la única palanca
   que actúa sobre la semana 38 en el plazo que queda.

---

## Cuánta confianza tiene esto

**Media-baja, y sesgada hacia abajo.** Tres razones, en orden de peso:

1. **33.399 plantas siguen sin fila en `ciclos_variedad.csv`**, y la mayoría son
   celosia. El motor no puede verificar la línea que más pesa en esta
   proyección — la estimación de celosia sale del reporte de campo, no del
   modelo.
2. **Cero mortalidad medida.** `mortalidad_siembras.csv` sigue con
   `pct_mortalidad` vacía. El factor de realización de 0,24 mezcla mortalidad,
   descarte de calidad y optimismo de tallos/planta sin poder separarlos.
3. **Los rangos por grupo son juicio anclado en el promedio medido**, no salida
   de modelo. Están escritos línea por línea arriba justamente para que se
   puedan discutir uno por uno.

Lo que **sí** es sólido: la dirección y el orden de magnitud. La semana 38 llega
a poco más de la mitad del ritmo reciente, y el hueco lo abre la celosia.
