# Protocolo por variedad — el ciclo no es un número, es una serie

> Vanessa 2026-09-11: *"la idea es que trabajemos juntos y que exista un
> protocolo por variedad, y en base a eso vayamos ajustándolo con cada ciclo…
> cada cosecha tiene que ser personalizada, porque puede comportarse
> diferente."*

## La corrección que originó este documento

Al analizar Lisianthus reporté que el ciclo documentado **estaba mal**: 15
semanas reales a cosecha contra 19-23 en `ciclos_variedad.csv`, y ventana de 10
semanas contra 4-6.

Vanessa corrigió la lectura:

> *"La documentación que hay de los ciclos de lisianthus, el cerebro, es por
> **siembras pasadas**, no es por literatura imaginada. Pero esta tuvimos, fíjate,
> un resultado diferente."*

**No estaba mal: estaba midiendo otra cosecha.** `ciclos_variedad.csv` es el
consolidado histórico. Esta siembra se comportó distinto, y eso no es un error
que corregir sino **un dato nuevo que guardar al lado del anterior**.

La consecuencia es de diseño: un solo número por variedad no puede representar
algo que cambia de siembra en siembra. Hace falta **una fila por cosecha**.

## Cómo se guarda

**`07-datos/ciclos_observados.csv`** — una fila por SIEMBRA, no por variedad:

| Campo | Qué guarda |
|---|---|
| `siembra` | identificador: grupo + semana de siembra + bloque |
| `semillas_enviadas` · `plantulas_entregadas` · `pct_germinacion` | el tramo del **plantulador** |
| `plantas_viables` · `sem_conteo_viables` | el tramo de **campo**: cuántas seguían vivas, y en qué semana se contaron |
| `plantas_trasplantadas_registro` | lo que dice `campo_siembras.csv` — **se guarda para poder contrastarlo, no porque sea el dato bueno** |
| `sem_inicio_cosecha` · `sem_pico` · `sem_fin_primera` | la ventana **observada**, no la proyectada |
| `tallos_primera` · `tallos_planta_obs` | lo que rindió de verdad |
| `segunda_floracion` | `EN CURSO` · `SI` · `NO` · proporción respecto de la primera |
| `incidencia` | qué le pasó — oidio, fusarium, botrytis |
| `confianza` · `fuente` | de dónde salió cada número |

`ciclos_variedad.csv` **no se toca**: sigue siendo la referencia de
planificación. `ciclos_observados.csv` es la serie histórica que, con suficientes
siembras, dirá si el consolidado hay que moverlo — y con qué dispersión, que es
lo que hoy no se sabe.

### La merma son dos tramos, no uno

La primera siembra lo dejó claro: entre la semilla y la planta que produce hay
**dos pérdidas independientes con dueños distintos**, y promediarlas en un solo
número de «merma» las hace invisibles.

| Tramo | Quién lo controla | Dónde está el dato |
|---|---|---|
| semilla → plántula entregada | el plantulador (Andrés) | `07-datos/germinacion_andres.csv` |
| plántula → planta viva en cama | el manejo de la finca | conteo de campo, hoy solo existe para Lisianthus |

En Lisianthus cada tramo se llevó ~4.900 plantas por separado. Arreglar uno no
arregla el otro, y la conversación para corregirlos es con personas distintas.

**`plantas_trasplantadas` de `campo_siembras.csv` no sirve como input.** Registra
la primera entrega cuando el plantulador entrega por tandas, y las tandas
siguientes entran como filas sueltas sin cultivar. El input bueno es
`plantulas_entregadas` de la hoja de Andrés.

## Las once secciones de la ficha

`python3 motor/ficha_completa.py <variedad>` produce siempre las mismas once, de
modo que dos variedades se comparen sin tener que recordar qué se miró en cada
una: siembra · ventana documentada contra real · cosecha semana a semana · pico ·
coincidencia · venta · reparto por tipo de producto · merma · inputs · decisiones
de manejo · lo que falta para cerrar el margen.

## El protocolo de revisión, ciclo a ciclo

1. **Al sembrar** — anotar semillas enviadas, plántulas recibidas y
   trasplantadas. La merma de plantulación es el primer costo y hoy no se mide.
2. **Al abrir la ventana** — anotar la semana real de primera cosecha, no la
   proyectada.
3. **Durante** — registrar incidencia y trabajo cultural, que es lo que explica
   la diferencia contra el consolidado.
4. **Al cerrar** — semana de fin, tallos totales, tallos/planta observados. **Hoy
   0 de 21 siembras de Lisianthus tienen fin de cosecha anotado**, y por eso
   ninguna ventana se puede cerrar.
5. **Recálculo** — comparar la siembra contra `ciclos_variedad.csv` y contra las
   siembras anteriores. Si el patrón se repite dos veces, se promueve a regla
   (`04-variedades/notas-campo.md`).

## Lo que este protocolo todavía no puede capturar

- **Por cultivar.** El registro de cosecha anota `Mix`: 19 cultivares de
  Lisianthus sembrados, uno solo en el registro. Vanessa tiene la lectura
  cualitativa de cuáles rindieron; falta pasarla a dato.
- **Vida en vaso.** `vida_en_vaso.csv` tiene una sola fila (Boca de Dragón). Es
  el argumento central a favor de Lisianthus y no está medido.
- **Inputs por lote.** Sólo se puede atribuir fitosanidad, y con 16 filas en
  `aplicaciones_historial.csv` no cubre un ciclo.
