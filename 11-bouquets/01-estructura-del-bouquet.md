# Estructura del bouquet — los seis roles

Un bouquet DCB no es "un montón de flores bonitas". Es una composición con
roles. Cuando falta un rol, el ojo lo nota aunque el cliente no sepa nombrarlo:
el ramo se ve plano, o desordenado, o barato.

Cada variedad del catálogo tiene un **rol estructural** asignado en
`07-datos/paleta_color.csv`, columna `rol_estructural`.

## Los seis roles

| Rol | Qué hace | Variedades DCB |
|---|---|---|
| **FOCAL** | Detiene el ojo. Es la flor que el cliente ve primero. Grande, redonda, opaca. | Girasol, Lisianthus, Zinnia, Celosia cristata |
| **LINEA** | Da altura, dirección y silueta. Tallos verticales o en espiga. | Boca de Dragón, Larkspur, Campanula, Amaranto (cascada, hacia abajo) |
| **SECUNDARIA** | Acompaña al focal sin competirle. Media escala. | Trachelium |
| **RELLENO** | Cierra huecos y une la composición. Muchas flores pequeñas por tallo. | Statice, Gomphrena, Ammi majus, Ammobium, Matricaria |
| **TEXTURA** | Rompe la monotonía con superficie distinta: mate, rugosa, esférica. | Green Ball, Strawflower, Celosia plumosa |
| **FOLLAJE** | Base verde, marco y volumen barato. | Ruscus, Eucalyptus, Silver Dollar, Helecho (comprados), Dusty Miller |

## Rangos de equilibrio DCB

Proporción sobre el **total de tallos** del arreglo, follaje incluido:

| Rol | Mínimo | Máximo |
|---|---|---|
| FOCAL | 10 % | 30 % |
| LINEA | 15 % | 30 % |
| SECUNDARIA | 0 % | 20 % |
| RELLENO | 20 % | 45 % |
| TEXTURA | 5 % | 20 % |
| FOLLAJE | 20 % | 40 % |

Codificados en `motor/cerebro.py` → `RANGO_ESTRUCTURA`. Para cambiarlos se
edita ahí, en un solo lugar.

### Por qué estos rangos

- **Focal por debajo de 10 %** — el ramo no tiene punto de entrada; el ojo
  patina y el ramo se percibe como "relleno caro".
- **Focal por encima de 30 %** — los focales compiten entre sí y se anulan.
- **Follaje por debajo de 20 %** — el ramo se ve apretado y sin marco; además
  se está pagando con tallo propio (caro) lo que el follaje comprado resuelve
  barato. Es a la vez un problema estético y de margen.
- **Relleno por encima de 45 %** — se ve difuso, sin jerarquía.

## Regla de aplicación: arreglos sí, paquetes no

Estos rangos aplican **solo a arreglos compuestos** — categorías `Bouquet`,
`Bouquet especial`, `Bouquet condolencias`, `Centro de mesa`.

**No aplican a paquetes.** Un ramo de 15 larkspur es 100 % LINEA y está
perfecto: su propuesta de valor es precisamente la repetición. Juzgarlo con
las reglas de un arreglo sólo produce alarmas falsas.

Los paquetes se evalúan con otras dos reglas:

1. **Coherencia nombre-contenido.** Si el nombre comercial promete un grupo
   botánico, la receta debe contenerlo.
2. **Color definido.** Un ramo simple no debería dejar el cultivar abierto:
   es exactamente donde el color se vuelve azar.

## Cómo verificarlo

```bash
python3 motor/cerebro.py bouquet "Cosecha Grande"   # un producto
python3 motor/cerebro.py auditar                    # los 24
```

## Estado actual del catálogo (auditoría de agosto 2026)

Los cinco arreglos compuestos tienen la estructura **dentro de rango** en
casi todos los roles. La estructura no es el problema de DCB hoy.

El problema es el color: ver `02-color-del-bouquet.md`.
