# Dreams Can Bloom — Cerebro de Operaciones

**Este repositorio es el estratega del cultivo.** Decide **qué sembrar, cuánto,
dónde, cuándo y con qué manejo** para que el tallo salga con calidad, el bouquet
salga bien combinado y con color gobernado, el punto de venta muestre la mezcla
de color que se decidió, y la finca gane más por metro cuadrado.

**Empieza por [`CLAUDE.md`](CLAUDE.md)** — instrucciones maestras y reglas no
negociables.

## Arranque rápido

```bash
python3 motor/cerebro.py matriz      # cuánto se puede decidir hoy con datos reales
python3 motor/cerebro.py auditar     # diagnóstico completo del catálogo
python3 motor/cerebro.py valor       # ingreso por tallo propio
python3 motor/cerebro.py sembrar motor/demanda_ejemplo.csv
```

Sin dependencias: Python 3 y librería estándar.

## El objetivo tiene tres piernas, y la tercera es la más grande

1. **Color deliberado en el punto de venta** — que la exhibición muestre la
   mezcla que se decidió, no la que resultó. → [`12-punto-de-venta/`](12-punto-de-venta/)
2. **Combinación y color correctos dentro del bouquet** — seis roles en rango,
   dominante gobernada, cultivar fijado. → [`11-bouquets/`](11-bouquets/)
3. **Todas las decisiones del medio** — la eficiencia y optimización de cada
   decisión y cada producto para lograr un tallo de calidad. Es una matriz de
   once variables y es donde se gana la rentabilidad.
   → [`13-optimizacion/02-matriz-de-decision.md`](13-optimizacion/02-matriz-de-decision.md)

## La cadena

```
punto de venta -> receta de producto -> tallos por variedad y semana
              -> semana de siembra
              -> BLOQUE Y CAMA segun microclima, agua, suelo e historia de plagas
              -> capacidad de camas -> manejo -> cosecha
```

Se recorre **de derecha a izquierda para ejecutar** y de izquierda a derecha
para decidir. La demanda de color manda sobre la siembra — pero **el dónde y el
cómo los manda la matriz de campo.**

## La matriz de decisión

Sembrar bien no es saber la fecha. Es cruzar once variables:

| | Variable | Estado hoy |
|---|---|---|
| 1 | Demanda de color y producto | 74 % — 83 tallos piden grupo, no cultivar |
| 2 | Ciclo, ventana, tallos/planta | 70 % — faltan 10 grupos |
| 3 | **Microclima medido por bloque** | **0 % — solo cualitativo** |
| 4 | Presión y uniformidad de riego | 39 % — la limitante dominante |
| 5 | Suelo por zona | 78 % |
| 6 | Histórico de plagas y hongos | 69 % — semana ambigua |
| 7 | **Clima semanal** | **0 %** |
| 8 | Rendimiento normalizado | 21 % — falta el divisor de plantas |
| 9 | **Calidad de tallo (longitud)** | **0 % — no se mide en ninguna parte** |
| 10 | Capacidad de camas | 72 % — faltan 5 bloques |
| 11 | **Costos** | **0 % — bloquea el margen** |

`python3 motor/cerebro.py matriz` mide esto. Qué falta y en qué orden:
[`08-roadmap/02-informacion-que-falta.md`](08-roadmap/02-informacion-que-falta.md)

**La unidad correcta de eficiencia es margen por m² por semana de cama
ocupada** — no tallos por planta. El tiempo de cama es el recurso escaso y hoy
no se cobra en ninguna cuenta.

## Estructura

| Carpeta | Contenido |
|---|---|
| `00-contexto/` … `09-procedimientos/` | Base operativa de campo (espejo de Drive) |
| `10-postcosecha/` | Sala, hidratación, vida en vaso |
| `11-bouquets/` | Estructura (6 roles) y color del bouquet |
| `12-punto-de-venta/` | Distribución de color en exhibición |
| `13-optimizacion/` | Cómo optimizar productos y procesos |
| `07-datos/` | Datos vivos en CSV |
| `motor/` | Motor de planificación |
| `.claude/skills/` | Skills que se activan solas según el tema |

## Los hallazgos hasta hoy

1. **83 tallos DCB del catálogo (26 %) no tienen cultivar definido en la
   receta.** La receta dice "Zinnia", que son 6 colores distintos. El color del
   punto de venta hoy no lo decide la receta: lo decide lo que haya en la sala.
   → [`11-bouquets/02-color-del-bouquet.md`](11-bouquets/02-color-del-bouquet.md)

2. **La calidad del tallo no se mide en ninguna parte del repositorio.** No hay
   un solo registro de longitud. El sistema optimiza cantidad porque es lo único
   que puede ver, y la calidad es la mitad del objetivo declarado.

3. **El microclima está descrito en adjetivos, no en números.** "Caliente",
   "fresco", "humedad nocturna alta". La botrytis no responde a adjetivos:
   responde a horas de HR sobre ~85 % entre 15 y 25 °C. Sin umbral no hay
   predicción. → [`13-optimizacion/02-matriz-de-decision.md`](13-optimizacion/02-matriz-de-decision.md)

4. **29 eventos de plagas y hongos estaban enterrados en texto libre** dentro de
   los COMENTARIOS de `campo_siembras.csv`. Ya extraídos a
   `07-datos/incidencia_fitosanitaria.csv`. Al ordenarlos aparecieron patrones que
   nadie había podido ver: botrytis en Statice por **ventana temporal** (semana
   16–21 de cosecha, independiente de variedad), mosca blanca en Matricaria por
   **inóculo de suelo** en 3C e Inv 5, y once cultivares de lisianthus con
   fusarium donde **uno resistió** — una diferencia varietal que vale plata.

5. **Brecha de 5.8x en ingreso por tallo propio.** `Paquete gomphrenas
   frambuesa` pide 26 tallos y se vende a $45.000; `Gomphrenas (paquete
   grande)` pide los mismos 26 más 4 de Ruscus y se vende a $90.000.
   → [`13-optimizacion/01-como-optimizar.md`](13-optimizacion/01-como-optimizar.md)

6. **Un argumento de rendimiento que no se sostenía.** Se iba a sacar la
   Campanula Champion Lavender por rendir 0.64 tallos/planta contra 0.92 de la
   blanca. Normalizado por días de ventana, la lavanda rinde 4 % **más**. El 0.64
   medía nueve días menos de cosecha registrada.
   → [`04-variedades/03-campanula-champion-lavender.md`](04-variedades/03-campanula-champion-lavender.md)

La estructura de los bouquets, en cambio, está bien: los cinco arreglos
compuestos tienen los seis roles dentro de rango. Y los 13 grupos del catálogo
ya son planificables — el bloqueo de ciclos quedó cerrado.

## Alcance

Este proyecto cubre **solo `Drive / DCB Claude / 07_Operaciones`**. Los datos
de venta y rotación (`03_Ventas`) están fuera de alcance: la mezcla objetivo de
color del punto de venta está creada como propuesta sin validar, a la espera de
esos datos.

---
*Dreams Can Bloom · Green Candle Capital S.A.S*
