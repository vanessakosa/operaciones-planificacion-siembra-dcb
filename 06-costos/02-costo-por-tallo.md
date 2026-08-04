# Costo por tallo

## Los dos componentes

### 1. Costo agrícola (BR) — varía por especie

Se calcula en `Calculo_por_tallo.xlsx`, columna BY. Depende de:
costo de semilla · densidad de siembra · ciclo del cultivo · rendimiento por m².

**Los cuatro insumos vienen de este repositorio:**
- Densidad → `07-datos/variedades_parametros_siembra.csv` y `capacidad_bloques.csv`
- Ciclo → `07-datos/variedades_bitacora.csv` (ciclo real, no el teórico)
- Rendimiento/m² → hoja RENDIMIENTO... **que está vacía** (ver `05-programacion/02-registro-de-tallos.md`)
- Costo de semilla → `07-datos/finca_entregas_plantulas.csv` y facturas de proveedor

### 2. Los tres parámetros variables — cambian cada mes con volumen real

| Parámetro | Valor sept. 2025 | Fórmula | Fuente |
|---|---|---|---|
| Poscosecha / tallo | $800 COP | (nómina + insumos) ÷ tallos procesados | Nómina + Registro Gastos 2E |
| Overhead / tallo | $224 COP | Overhead mensual ÷ tallos vendidos | Registro Gastos 3C |
| Logístico / tallo | $305 COP | Costo LABAN ÷ (tallos × 93%) | Registro Gastos 2F |

⚠️ **Estos tres valores están basados en septiembre 2025 (25.142 tallos). Son la referencia
más vieja del sistema.** El modelo nuevo los recalcula mes a mes con datos reales.
Cualquier análisis de rentabilidad que los use hoy tiene ese sesgo — declararlo.

Suma de los tres: **$1.329 COP/tallo de costo no agrícola.** Ese número por sí solo explica por
qué el análisis de rentabilidad por variedad importa tanto: si el costo fijo por tallo es
$1.329, una variedad de bajo rendimiento por m² no se salva bajando el costo agrícola.

## Lo que bloquea el análisis de rentabilidad hoy

Tres cadenas rotas, en orden de impacto:

1. **CONSOLIDADO y RENDIMIENTO vacías** → no hay tallos/m² real por lote → no hay costo agrícola real
2. **`costos_productos.csv` vacío** → no hay costo por aplicación → el componente 2B (insumos
   cultivo) no se puede atribuir por variedad ni por bloque
3. **Los 3 parámetros congelados en sept 2025** → el denominador está desactualizado

Arreglar (1) y (2) es lo que convierte este repositorio en un sistema de decisión y no solo
de documentación.

## Precios de venta de referencia

`07-datos/formulas_productos_bouquets.csv` tiene la composición y el precio de los productos
terminados (ej. Cosecha Grande $125.000 = 11 flores DCB + 4 follaje comprado).

Esto permite cerrar el círculo: **cuántos tallos de qué variedad entran en cada bouquet, a qué
costo, contra qué precio de venta.** Es el puente entre lo agrícola y lo comercial, y es donde
se ve si una variedad "bonita" pero de bajo rendimiento se justifica por su rol en el bouquet.
