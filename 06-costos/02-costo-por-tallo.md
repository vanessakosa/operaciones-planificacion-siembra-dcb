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

## El modelo YA está construido — lo que falta es UNA fila (2026-09-10)

Se leyó `DCB_Modelo_Costos` en Drive (Google Sheet
`1MGX0ISxS_UbeUfgC5gHuPlennqCjAlhYr4uU0GBg0Qw`, modificado el 2026-09-10). La
hoja **"Parámetros mensuales de costo por tallo"** existe, con sus fórmulas
corriendo y los costos reales del año ya cargados mes a mes. El propio archivo lo
dice: *"Los campos en azul se calculan automáticamente desde el Registro Gastos.
Solo ingresar los campos en amarillo."*

**Y el único campo manual es `Tallos vendidos en el mes`, que está en 0 en los
doce meses.** Por eso todos los resultados salen en $0: no falta construir el
modelo ni cargar los costos, falta **el denominador.**

Los costos que ya están cargados (espejados en
`07-datos/costo_mensual_operacion.csv`):

| Concepto | Junio 2026 | Julio 2026 |
|---|---|---|
| Nómina poscosecha + MO campo | $22.988.459 | $10.477.451 |
| Insumos poscosecha + empaque | $2.630.425 | $4.598.774 |
| Logístico LABAN | $5.405.331 | $4.454.676 |
| Overhead admin + seguridad social | $4.391.800 | $3.879.100 |
| **Total** | **$35.416.015** | **$23.410.001** |

Agosto todavía no está cerrado en el modelo: solo tiene $387.000 de logístico,
con nómina y overhead en $0.

### El piso del costo por tallo, que sí se puede calcular hoy

Falta *tallos vendidos*, pero el repositorio tiene **tallos cosechados**. Como
lo vendido nunca es más que lo cosechado, dividir por la cosecha da un **piso**:
el costo real por tallo vendido no puede ser menor que esto.

| Mes | Costo total | Tallos cosechados | **Piso $/tallo** |
|---|---|---|---|
| Junio 2026 | $35.416.015 | 25.691 | **$1.379** |
| Julio 2026 | $23.410.001 | 26.951 | **$869** |

Es un piso, no una estimación: el número verdadero es **mayor**, porque el
denominador correcto es menor y porque esto todavía no incluye semilla ni
insumos de cultivo.

**Contra qué se compara:** `cerebro.py valor` da el ingreso por tallo propio de
cada producto, y va de **$10.000** (Dream Big) a **$1.731**
(Paquete gomphrenas frambuesa). Ese último producto está **por debajo del piso
de junio** y apenas por encima del de julio. Es el primer candidato a revisar
precio o composición — y no es un detalle menor, porque es Gomphrena, el grupo
con el mayor déficit del catálogo.

⚠️ **Corrección al roadmap.** El bloqueo #5 del `CLAUDE.md` decía "llenar
`costos_productos.csv` desbloquea margen por m² por semana". Eso está mal
planteado: el encabezado de ese archivo es
`Producto, Presentación, Precio $, Costo por cc/g, Proveedor` — es una **lista de
precios de insumos**, útil para el componente 2B (costo por aplicación
fitosanitaria), no el modelo de margen. El margen por tallo vive en
`DCB_Modelo_Costos` y está construido. Son dos bloqueos distintos y el segundo
es mucho más pequeño de lo que el roadmap suponía.

## Lo que bloquea el análisis de rentabilidad hoy

En orden de esfuerzo contra desbloqueo:

1. **`Tallos vendidos en el mes` en `DCB_Modelo_Costos`** → una fila de doce
   números y el costo por tallo real del año queda calculado. Es el dato de
   ventas, no de cosecha.
2. **CONSOLIDADO y RENDIMIENTO** → sin tallos/m² real por lote no hay costo
   agrícola por variedad, que es lo que permite comparar variedades entre sí.
3. **`costos_productos.csv` vacío** → el costo por aplicación no se puede
   atribuir por variedad ni por bloque.
4. **Los 3 parámetros congelados en sept 2025** ($1.329/tallo) → ya no hace
   falta usarlos: el modelo tiene los costos de 2026 cargados.

## Precios de venta de referencia

`07-datos/formulas_productos_bouquets.csv` tiene la composición y el precio de los productos
terminados (ej. Cosecha Grande $125.000 = 11 flores DCB + 4 follaje comprado).

Esto permite cerrar el círculo: **cuántos tallos de qué variedad entran en cada bouquet, a qué
costo, contra qué precio de venta.** Es el puente entre lo agrícola y lo comercial, y es donde
se ve si una variedad "bonita" pero de bajo rendimiento se justifica por su rol en el bouquet.
