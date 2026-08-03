---
name: dcb-bouquets
description: >
  Estructura y color de los bouquets de Dreams Can Bloom (DCB), y distribución
  de color en el punto de venta. Usar SIEMPRE que Vanessa pregunte por la
  composición de un bouquet o paquete, pida diseñar o revisar una receta,
  mencione que un ramo "se ve plano/desordenado/monocromático", pregunte qué
  color va a faltar o sobrar en exhibición, pida traducir demanda de producto a
  tallos por variedad, o pregunte cuándo y cuánto sembrar para sostener un
  surtido de color. También usar para evaluar precio por tallo propio y
  apalancamiento en follaje comprado. NO usar para diseño de bombas
  fitosanitarias ni rotación de productos — eso es dcb-fitosanidad. NO usar
  para nombres homologados, columna N, VARIEDADES_BITACORA ni el calendario de
  Erica — eso es exclusivamente dcb-programacion. NO usar para comportamiento
  agronómico por variedad o dónde sembrar — eso es dcb-variedades.
---

# DCB Bouquets — estructura, color y punto de venta

## Antes de responder cualquier cosa

**Corre el motor. No respondas de memoria.**

```bash
python3 motor/cerebro.py auditar                    # panorama del catálogo
python3 motor/cerebro.py bouquet "<nombre>"         # un producto en detalle
python3 motor/cerebro.py valor                      # ingreso por tallo propio
python3 motor/cerebro.py explotar <demanda.csv>     # demanda -> tallos
python3 motor/cerebro.py sembrar  <demanda.csv>     # demanda -> siembra
```

Las recetas cambian y el motor lee los CSV en vivo. Una respuesta de memoria
sobre cuántos tallos lleva un bouquet es una respuesta desactualizada.

## Los dos problemas distintos de color

No confundirlos, porque se arreglan en lugares distintos:

- **Color del bouquet** — armonía *dentro* de un ramo. Se arregla en la receta.
- **Color del punto de venta** — distribución *entre* los ramos expuestos. Se
  arregla en la programación de siembra (escalonamiento de ventanas).

Si Vanessa dice "el punto de venta se ve todo igual", la causa casi nunca está
en la exhibición: está en que varias variedades de ventana corta entregaron
juntas. Mirar `ventana_sem_max` en `07-datos/ciclos_variedad.csv`.

## Los seis roles estructurales

FOCAL · LINEA · SECUNDARIA · RELLENO · TEXTURA · FOLLAJE

Rangos de equilibrio en `11-bouquets/01-estructura-del-bouquet.md`, codificados
en `motor/cerebro.py` → `RANGO_ESTRUCTURA`.

**Aplican solo a arreglos compuestos** (`Bouquet*`, `Centro de mesa`). Un
paquete de 15 larkspur es 100 % LINEA y está bien: su valor es la repetición.
Los paquetes se juzgan por coherencia nombre-contenido y color definido.

## Las tres reglas de color

1. Dominante ≥ 50 % de los tallos cromáticos.
2. Máximo 4 familias cromáticas (sin contar neutros).
3. Neutro ≥ 15 % del total.

## Regla crítica: la confianza del color

`07-datos/paleta_color.csv` tiene columna **`confianza_color`**. Lo marcado
`baja` es un color que se **dedujo del nombre del cultivar**, no un dato
confirmado.

**Nunca presentar un color de confianza baja como hecho.** Decir "según la
paleta, sin confirmar en campo".

La más importante de confirmar es **Statice Forever Happy** — aparece en 9 de
los 24 productos.

## Al diseñar o corregir una receta

1. Correr `bouquet "<nombre>"` para ver el estado actual.
2. Revisar los seis roles antes que el color: un ramo desequilibrado en
   estructura no se salva con color.
3. **Nunca dejar un ingrediente como grupo desnudo** (`Zinnia, 3`). Usar
   cultivar fijo (`Zinnia Benary Giant Bright Pink, 3`) o color gobernado
   (`Zinnia [ROSA_FUERTE | ROSA_MEDIO], 3`).
4. Verificar que el nombre comercial corresponda al contenido.
5. Antes de proponer una variedad nueva en una receta, verificar que tenga
   ciclo en `07-datos/ciclos_variedad.csv`. **Girasol, Green Ball, Amaranto y
   Ammobium no lo tienen** — si la receta depende de ellos, no es planificable
   y hay que decirlo.

## Al traducir demanda a siembra

El motor retrocede desde la semana de cosecha usando `sem_a_campo_max` y
`sem_germinacion`. Aplica 15 % de merma por defecto.

**Si falta el ciclo, el motor NO estima** — lo reporta en la sección
"NO PLANIFICABLE". Respetar eso: la regla no negociable #1 dice que un ciclo
inventado corrompe el calendario de Erica. Pedir el dato, no rellenarlo.

Para ciclo y ventana del calendario de clientes la fuente primaria es
**VARIEDADES_BITACORA**, no `ciclos_variedad.csv`.

## Errores de datos conocidos

Están listados en `11-bouquets/02-color-del-bouquet.md`. Los principales:

- `formulas_productos_bouquets.csv` tiene 11 filas de productos fitosanitarios
  contaminando el archivo de recetas. El motor las descarta y las reporta.
- `Paquete zinnias sunset` no contiene ninguna zinnia.
- `Team Wheeler (florero)` está como ingrediente floral; es un contenedor.
- `listas_desplegables.csv` tiene nombres de Statice como opciones de Boca de
  Dragón y Gomphrena.

Si Vanessa pide algo que choca con uno de estos errores, señalarlo en vez de
trabajar sobre el dato malo.
