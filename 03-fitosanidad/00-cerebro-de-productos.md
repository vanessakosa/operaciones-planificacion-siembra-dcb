# El cerebro de productos

Vanessa 2026-09-23: *"no deberían estar las fórmulas prehechas, sino la información de
cada producto, de forma que cada semana podamos hacer una formulación muy
personalizada, dependiendo del estado fenológico, de los retos fitosanitarios, del
clima"*. Y lo que lo motivó: la bomba de choque de la semana 39 llevaba No Fly
(*Paecilomyces*, hongo vivo) en el mismo tanque que Equifun (fungicida). Nadie lo vio
porque la receta se copió de julio sin razonarla.

## Las piezas

| # | Pieza | Archivo | Estado |
|---|---|---|---|
| 1 | Ficha por producto, con precio | `07-datos/productos.csv` + PDF en `fichas/` | **Esqueleto listo (45 productos)** — 4 fichas confirmadas, 0 precios |
| 1b | Ingredientes activos, formato largo | `07-datos/producto_ingredientes.csv` | Solo los que traen concentración en el repo |
| 2 | Reglas de compatibilidad por clase | `07-datos/compatibilidad.csv` | 9 reglas iniciales |
| 3 | El criterio con fuentes | `03-fitosanidad/06-criterio-de-formulacion.md` | Pendiente |
| 4 | El formulador | `motor/formular.py` | Pendiente — cuando haya fichas que cruzar |

`bombas_catalogo.csv` deja de ser plantilla y queda como **historial** de lo que se
formuló cada semana.

## Comandos

```bash
python3 motor/productos.py                  # qué falta por producto: ficha, dosis, precio, stock
python3 motor/productos.py ficha Equifun    # todo lo que se sabe de un producto
python3 motor/productos.py comparar Mn      # productos con el mismo ingrediente, por costo
```

## Por qué los ingredientes van aparte

Para comparar dos productos que tienen lo mismo (dos Metarhizium, dos fuentes de
manganeso, dos Bacillus) no sirve el precio del frasco: sirve el **costo por unidad de
activo que llega a la planta** — precio ÷ presentación ÷ concentración. Una mezcla de
cuatro microorganismos son cuatro filas, y cada una se compara con su par.

Costo-beneficio no es solo eso: pesan los otros ingredientes de la mezcla, el
intervalo entre aplicaciones (Raxter cada 15 días contra Anisagro cada 3 meses, si se
confirma) y la evidencia de eficacia. El comando da el número; la decisión se razona.

## Estados de ficha

| Estado | Qué significa | ¿Entra a formulación? |
|---|---|---|
| `CONFIRMADA` | La ficha está leída y sus datos en las tablas | Sí |
| `PARCIAL` | Hay ficha pero falta algo clave | Con advertencia |
| `LISTADA_SIN_DATOS` | `01-reglas-y-protocolos.md` la lista "con ficha", pero el repo no tiene ni una línea de su contenido | Con advertencia, hasta traerla |
| `SIN_FICHA` | Nunca se registró ficha | Regla 3: no, salvo decisión explícita de Vanessa |

Las dosis con `dosis_fuente = HISTORIAL` salen de lo que se venía aplicando, **no de la
etiqueta**. Son las que hay que verificar primero: ahí está la pregunta de Vanessa de
si se ha botado producto por dosis de más o de menos.
