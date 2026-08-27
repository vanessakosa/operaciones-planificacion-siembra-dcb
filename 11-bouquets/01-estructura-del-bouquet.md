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

---

## Tres tipos de flexibilidad en las recetas — y por qué importan al motor

Descubierto el 2026-08-13 al cargar seis productos que no estaban en el
catálogo. **Ninguna de estas tres reglas estaba escrita en ningún lado**: las
tres salieron porque Vanessa las mencionó al pasar. Es muy probable que haya
más en los otros productos.

Importan porque `cerebro.py explotar` convierte demanda en tallos multiplicando
recetas. **Si trata como fija una receta que flexiona, pide de más o de menos —
y el error no se ve: simplemente se siembra mal.**

### 1 · Sustitución simple — «el que haya»

> **Yugos:** `Trachelium o Ammi, 1` — se usa el que esté disponible.

Se registra como **un solo renglón**, no dos ingredientes. Si se registraran
por separado, el motor pediría sembrar los dos.

### 2 · Sustitución condicional — un ingrediente cubre la falta de otro

> **Dream Land:** *"a veces puede llevar 5 bocas, cuando no tenemos
> lisianthus"*.

Se registra con **rangos**: `Lisianthus 0-5` y `Snapdragon naranja 3-5`. No se
parte en dos productos, porque no son dos productos: es el mismo armado con lo
que haya ese día.

> **Contraste — cuándo SÍ se parte en dos:** `Greenery` y `Greenery con
> lisianthus` son dos productos separados, porque son dos cosas que **se venden
> distinto** y el cliente pide una u otra. La regla es: si se pide por su
> nombre, es un producto; si se decide al armar, es una sustitución.

### 3 · Producto definido por VOLUMEN y PALETA — el más difícil

> **Dream Land es un maxi bouquet.** Vanessa: *"suele ser en tonos rosados,
> rojos, vinos, por lo que se adaptan los tallos más o menos para lograr ese
> volumen. A veces si no hay flores grandes toca echarle más de lo que esté en
> cosecha para que tenga el mismo tamaño."*

Aquí **el invariante no es la lista de ingredientes: es el tamaño del ramo y su
familia de color.** La receta registrada es un *ejemplo típico*, no una
especificación.

Tres consecuencias que hay que tener presentes:

1. **El número de tallos es inversamente proporcional al tamaño de flor.** Flor
   pequeña → más tallos para el mismo volumen. Así que la demanda de tallos de
   un maxi **no se puede calcular sin saber el calibre de lo que hay en campo**,
   y `07-datos/calidad_tallo.csv` está vacío.
2. **La restricción dura es el color, no el ingrediente.** Cualquier tallo de la
   familia rosado/rojo/vino sirve. Eso da libertad de sustitución, pero exige
   que la paleta esté bien clasificada — y `paleta_color.csv` tiene variedades
   con `confianza_color = baja`.
3. **Los neutros no rompen la paleta.** Dream Land lleva 8 statice blanco y 1
   girasol blanco sobre 33 tallos DCB: 27 % de neutros, dentro de la regla
   `NEUTRO_MIN = 15 %`. El blanco no contradice "rosados, rojos, vinos" — es el
   descanso visual que la regla exige.

### Qué falta hacer con esto

- **Repasar los otros 24 productos** con una sola pregunta: *¿qué se cambia por
  qué cuando no hay?* Cada respuesta es una regla que hoy vive solo en la cabeza
  de quien arma el ramo.
- **Marcar cuáles productos son de volumen** y cuáles de lista fija. Hoy el
  motor los trata a todos igual.
