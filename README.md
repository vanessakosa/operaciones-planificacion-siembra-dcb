# Dreams Can Bloom — Cerebro de Operaciones

De la semilla al punto de venta. Este repositorio decide **cuándo sembrar,
cuánto sembrar, cómo sembrar**, en qué bouquet termina cada tallo, y con qué
distribución de color llega al punto de venta.

**Empieza por [`CLAUDE.md`](CLAUDE.md)** — instrucciones maestras y reglas no
negociables.

## Arranque rápido

```bash
python3 motor/cerebro.py auditar     # diagnóstico completo del catálogo
python3 motor/cerebro.py valor       # ingreso por tallo propio
python3 motor/cerebro.py sembrar motor/demanda_ejemplo.csv
```

Sin dependencias: Python 3 y librería estándar.

## La cadena

```
punto de venta -> receta de producto -> tallos por variedad y semana
              -> semana de siembra -> capacidad de camas -> manejo -> cosecha
```

Se recorre **de derecha a izquierda para ejecutar** y de izquierda a derecha
para decidir. La demanda de color manda sobre la siembra.

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

## Los tres hallazgos de la primera auditoría

1. **24 % de los tallos DCB del catálogo no tienen cultivar definido en la
   receta** (83 de 345). La receta dice "Zinnia", que son 6 colores distintos.
   El color del punto de venta hoy no lo decide la receta: lo decide lo que haya
   en la sala. → [`11-bouquets/02-color-del-bouquet.md`](11-bouquets/02-color-del-bouquet.md)

2. **4 grupos en uso activo no tienen ciclo registrado**: Girasol (el focal
   principal), Green Ball (en 8 de 24 productos), Amaranto y Ammobium. El motor
   se niega a inventarlos, así que no son planificables.

3. **Brecha de 5.8x en ingreso por tallo propio.** `Paquete gomphrenas
   frambuesa` pide 26 tallos y se vende a $45.000; `Gomphrenas (paquete
   grande)` pide los mismos 26 más 4 de Ruscus y se vende a $90.000.
   → [`13-optimizacion/01-como-optimizar.md`](13-optimizacion/01-como-optimizar.md)

La estructura de los bouquets, en cambio, está bien: los cinco arreglos
compuestos tienen los seis roles dentro de rango.

## Alcance

Este proyecto cubre **solo `Drive / DCB Claude / 07_Operaciones`**. Los datos
de venta y rotación (`03_Ventas`) están fuera de alcance: la mezcla objetivo de
color del punto de venta está creada como propuesta sin validar, a la espera de
esos datos.

---
*Dreams Can Bloom · Green Candle Capital S.A.S*
