# Color del bouquet — y el hallazgo central de esta auditoría

## El hallazgo

**24 % de los tallos DCB del catálogo (83 de 345) no tienen cultivar definido
en la receta.**

No es un problema de sala ni de criterio de las armadoras. Es un problema de
**especificación**: la receta pide "Zinnia", y Zinnia son seis colores
distintos, de crema a rosa fuerte a dorado. La receta pide "Snapdragon (Boca
de Dragón)", y hay diez colores posibles, de marfil a morado.

Cuando la receta no fija el cultivar, el color del bouquet lo decide lo que
haya ese día en la sala. Y lo que hay en la sala lo decidió una siembra de
hace tres meses que no sabía para qué bouquet era.

**Esa es la cadena rota.** No se arregla en el punto de venta ni en la sala;
se arregla en la receta y, hacia atrás, en la siembra.

### Dónde está concentrado

| Producto | Tallos DCB sin color definido |
|---|---|
| Bocas de dragón (paquete) | 100 % |
| Campanula (paquete) | 100 % |
| Paquete campanulas y bocas | 100 % |
| Campanulas y statice (paquete) | 77 % |
| Paquete campanulas y larkspur | 70 % |
| Cosecha Grande | 44 % |
| Dream Big | 44 % |
| Cosecha Pequeño | 33 % |
| Centro de mesa pequeño | 31 % |
| Bouquet pureza | 14 % |

`Bouquet pureza` es el mejor del catálogo en esto — y no por casualidad: es el
de condolencias, donde el color **sí** se especificó (Campanula Champion
White, "preferiblemente blanca"). Cuando el color importaba, se escribió.

## Las tres reglas de color DCB

Aplican a arreglos compuestos, sobre los tallos con color determinado.

### 1. Dominante ≥ 50 %

Una familia de color debe llevar al menos la mitad de los tallos cromáticos.
Sin dominante no hay lectura: el ramo se ve "de colores", que es la manera
elegante de decir que no se decidió nada.

### 2. Máximo 4 familias cromáticas

Sin contar neutros. Más de cuatro y el ramo se vuelve ruido.

### 3. Neutro ≥ 15 % del total

Los neutros son el descanso visual y el puente entre familias que no se
llevarían bien solas.

**Familias neutras en DCB:** BLANCO, MARFIL, CREMA, PLATA, VERDE, VERDE_GRIS,
VERDE_PLATA, VERDE_MARRON, BLANCO_CREMA.

DCB está bien surtida de neutros: Ammi majus, Ammobium, Green Ball, Statice
Forever Silver, Matricaria Snowball, más todo el follaje comprado. El neutro
no es la restricción.

Codificadas en `motor/cerebro.py` → `DOMINANTE_MIN`, `MAX_FAMILIAS_CROMATICAS`,
`NEUTRO_MIN`, `NEUTROS`.

## Cómo cerrar la brecha

La receta debe especificar el cultivar, o especificar **explícitamente** que el
color es libre dentro de una lista cerrada. Dos formas válidas:

**Forma A — cultivar fijo:**
`Zinnia Benary Giant Bright Pink, 3`

**Forma B — color gobernado, cultivar flexible:**
`Zinnia [ROSA_FUERTE | ROSA_MEDIO], 3`

La forma B es la realista para DCB: da a la sala el margen que necesita
cuando la cosecha no salió exacta, sin dejar el color al azar. Lo que **no**
es aceptable es `Zinnia, 3` a secas.

Migrar el catálogo a la forma A o B es la tarea pendiente #1 de este eslabón.
Requiere decisión de Vanessa producto por producto — el motor no la puede
tomar, porque implica criterio comercial.

## Advertencia sobre la paleta

`07-datos/paleta_color.csv` tiene una columna **`confianza_color`**:

- `alta` — el nombre del cultivar declara el color ("Champion White").
- `media` — el nombre lo implica con razonable seguridad ("Crimson", "Plumblossom").
- `baja` — **el nombre no dice nada del color y yo lo inferí.** Hay que
  confirmarlo en campo antes de usarlo para decidir.

Las de confianza baja son: Opus Fresh, Gomphrena Quis Sequin, Zinnia
Ballerina, Zinnia Floret Victorian Wedding, Statice Forever Happy, Amaranto
Mira, Celosia Raspberry Lemonade.

**Statice Forever Happy es la más importante de confirmar**: aparece en 9 de
los 24 productos y hoy la tengo como LILA_ROSADO por deducción — el paquete
que la lleva se llama "statice pink dreams". Si en realidad es una mezcla o
otro tono, varios diagnósticos de color cambian.

## Errores de datos detectados de paso

1. **`Paquete zinnias sunset` ($54.000) no contiene ninguna zinnia.** Lleva
   Green Ball (10) + Statice Forever Happy (3). O el nombre está mal, o la
   receta está mal.
2. **`Team Wheeler (florero)` está listado como ingrediente** del Centro de
   mesa con cantidad 2. Es un contenedor, no un tallo. El motor lo excluye del
   conteo, pero debería salir de la lista de ingredientes florales.
3. **`formulas_productos_bouquets.csv` tiene 11 filas contaminantes** al final:
   productos fitosanitarios (Cantus, Infinito, Pestick, Raizal 400…) con un
   esquema de columnas completamente distinto, pegados dentro del archivo de
   recetas. El motor los descarta y los reporta, pero hay que limpiar el
   archivo fuente en Drive.
4. **`listas_desplegables.csv` tiene contaminación en la última columna**:
   "Forever Happy" aparece como opción de Boca de Dragón y "Forever Silver"
   como opción de Gomphrena. Son nombres de Statice.
5. **Limonium Ruso está duplicado** — aparece como grupo propio y como opción
   dentro de Statice.
