# Cómo optimizar productos y procesos

## Los tres ejes

Toda decisión de DCB se evalúa desde tres ejes (heredado de `CLAUDE.md`):

1. **Calidad del tallo** — largo, grosor, sanidad, vida en vaso.
2. **Rentabilidad** — ingreso por tallo y por cama.
3. **Uso eficiente de recursos** — cama, agua, insumo, mano de obra.

Un cambio que mejora uno y empeora otro no es una mejora: es un intercambio, y
hay que nombrarlo como tal.

## Qué se puede optimizar hoy, con los datos que existen

### 1. Valor por tallo propio

```bash
python3 motor/cerebro.py valor
```

**Brecha actual: 5.8x** entre el mejor y el peor producto.

| | Producto | $/tallo propio |
|---|---|---|
| Mejor | Dream Big | $10.000 |
| Peor | Paquete gomphrenas frambuesa | $1.731 |

`Paquete gomphrenas frambuesa` pide **26 tallos de Gomphrena Quis Carmine** y se
vende a $45.000. `Gomphrenas (paquete grande)` pide 26 tallos (20 Carmine + 6
Sequin) más 4 de Ruscus y se vende a $90.000 — el doble de precio por
prácticamente el mismo tallo propio. Uno de los dos precios está mal puesto.

**Esto es una pregunta, no una conclusión:** puede que el paquete frambuesa sea
deliberadamente un producto de entrada. Pero si no lo es, es la corrección de
precio más rentable disponible y no cuesta nada implementarla.

### 2. Apalancamiento en follaje comprado

17 de 24 productos usan **0 % de follaje comprado**. El follaje comprado
(Ruscus, Eucalyptus, Silver Dollar, Helecho) aporta volumen y marco visual sin
consumir cama propia. Los cinco arreglos compuestos lo usan entre 27 % y 35 %;
los paquetes no lo usan casi nunca.

Los paquetes de un solo tipo de flor con 0 % follaje son los que **más cama
consumen por peso de venta**. Agregar 3-4 tallos de Ruscus a un paquete sube el
volumen percibido a costo de compra, no de cama.

### 3. Gobernanza de color

24 % de los tallos DCB sin cultivar definido. Cerrar esto no cuesta insumo ni
cama: es reescribir recetas. Y es prerrequisito de todo lo demás — sin color
gobernado, la distribución en punto de venta no es controlable. Ver
`11-bouquets/02-color-del-bouquet.md`.

### 4. Ventanas de cosecha y escalonamiento

`07-datos/ciclos_variedad.csv`, columna `ventana_sem_max`:

- **Ventana corta (1-3 semanas)** — Campanula, Larkspur, Boca de Dragón,
  Zinnia, Matricaria, Celosia cristata, Nigela. Entregan todo de golpe.
  Requieren siembras escalonadas para dar continuidad.
- **Ventana larga (6-16 semanas)** — Statice, Limonium, Trachelium, Anémona,
  Strawflower, Daucus. Una siembra cubre muchas semanas.

Statice: **ventana de 8 semanas y 8 tallos por planta**. Es la variedad más
eficiente del catálogo en cama por tallo, y aparece en 9 de 24 productos. Bien
usada.

Las de ventana corta que aparecen en muchos productos son el riesgo de
continuidad: Campanula y Boca de Dragón tienen ventana de 2 semanas y están en
6 y 5 productos respectivamente.

## Qué NO se puede optimizar todavía — y qué lo desbloquea

| Falta | Bloquea | Qué se necesita |
|---|---|---|
| `costos_productos.csv` vacío | Margen real por producto, costo por aplicación | Precio por presentación de ~35 insumos |
| Ciclo de Girasol, Green Ball, Amaranto, Ammobium | Planificar 4 grupos en uso activo | Dato de ciclo y tallos/planta de Vanessa |
| 5 bloques sin medir (Ext 3B, Inv 2, Mini, Inv 4C, Inv 6) | Capacidad real de campo | Medición con cinta métrica |
| `CONSOLIDADO` y `RENDIMIENTO` sin fórmulas | Rentabilidad por variedad | Reconstruir en `DCB_Registro_Tallos` |
| Datos de venta y rotación (`03_Ventas`) | Mezcla objetivo de punto de venta validada | Traer del Drive o dictar |

Los cuatro grupos sin ciclo son el bloqueo más barato de levantar y el de mayor
efecto inmediato: **Girasol es el focal principal del catálogo y Green Ball
aparece en 8 de 24 productos.** Sin su ciclo, el motor no puede decir cuándo
sembrarlos, y son justamente los que sostienen la estructura de los bouquets.

## El orden correcto de ataque

1. **Ciclo de Girasol, Green Ball, Amaranto, Ammobium** — desbloquea la
   planificación de 4 grupos activos. Costo: una conversación.
2. **Confirmar Statice Forever Happy** — está en 9 productos con color inferido.
   Costo: mirar una flor.
3. **Fijar color en las recetas** — de `Zinnia, 3` a `Zinnia [ROSA_FUERTE], 3`.
   Costo: decisión comercial producto por producto.
4. **Revisar el precio del paquete frambuesa** — o confirmar que es intencional.
5. **Limpiar `formulas_productos_bouquets.csv`** — sacar las 11 filas
   fitosanitarias y el florero de la lista de ingredientes.
6. **Medir los 5 bloques faltantes** — desbloquea el chequeo real de capacidad.
7. **Llenar `costos_productos.csv`** — desbloquea todo el análisis de margen.

Los pasos 1 a 5 no cuestan dinero ni insumo. Son decisiones y limpieza de
datos, y desbloquean más que cualquier cambio agronómico.
