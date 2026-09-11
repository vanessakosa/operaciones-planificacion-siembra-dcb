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
consolidado histórico. Esta cohorte se comportó distinto, y eso no es un error
que corregir sino **un dato nuevo que guardar al lado del anterior**.

La consecuencia es de diseño: un solo número por variedad no puede representar
algo que cambia de cohorte en cohorte. Hace falta **una fila por cosecha**.

## Cómo se guarda

**`07-datos/ciclos_observados.csv`** — una fila por COHORTE, no por variedad:

| Campo | Qué guarda |
|---|---|
| `cohorte` | identificador: grupo + semana de siembra + bloque |
| `semillas_enviadas` · `plantas_trasplantadas` | el input, y la merma de plantulación entre los dos |
| `sem_inicio_cosecha` · `sem_pico` · `sem_fin_primera` | la ventana **observada**, no la proyectada |
| `tallos_primera` · `tallos_planta_obs` | lo que rindió de verdad |
| `segunda_floracion` | `EN CURSO` · `SI` · `NO` · proporción respecto de la primera |
| `incidencia` | qué le pasó — oidio, fusarium, botrytis |
| `confianza` · `fuente` | de dónde salió cada número |

`ciclos_variedad.csv` **no se toca**: sigue siendo la referencia de
planificación. `ciclos_observados.csv` es la serie histórica que, con suficientes
cohortes, dirá si el consolidado hay que moverlo — y con qué dispersión, que es
lo que hoy no se sabe.

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
5. **Recálculo** — comparar la cohorte contra `ciclos_variedad.csv` y contra las
   cohortes anteriores. Si el patrón se repite dos veces, se promueve a regla
   (`04-variedades/notas-campo.md`).

## Lo que este protocolo todavía no puede capturar

- **Por cultivar.** El registro de cosecha anota `Mix`: 19 cultivares de
  Lisianthus sembrados, uno solo en el registro. Vanessa tiene la lectura
  cualitativa de cuáles rindieron; falta pasarla a dato.
- **Vida en vaso.** `vida_en_vaso.csv` tiene una sola fila (Boca de Dragón). Es
  el argumento central a favor de Lisianthus y no está medido.
- **Inputs por lote.** Sólo se puede atribuir fitosanidad, y con 16 filas en
  `aplicaciones_historial.csv` no cubre un ciclo.
