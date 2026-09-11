# El cuestionario por variedad

Para llenar `07-datos/contexto_variedad.csv` sin tener que acordarse de nada.
**Vanessa responde la lista; Claude valida y escribe filas.** No se produce
análisis, ni documento por variedad, ni gráficas, salvo que se pidan aparte.

Lo que no se sepa se responde **«no sé»** y queda como `SIN_DATO` con la
confianza en blanco. Un hueco declarado se llena después; un número inventado
contamina un cálculo para siempre.

## Cómo está armado el archivo

Una fila por **hecho**, no por variedad. Eso permite dictar un tipo de dato nuevo
mañana sin cambiar el esquema.

| Columna | Qué va |
|---|---|
| `variedad` | el grupo homologado |
| `cultivar` | **vacío = aplica a todo el grupo** |
| `cohorte` | **vacío = permanente**; con valor = solo de esa cosecha |
| `categoria` | una de las doce de abajo |
| `dato` · `valor` · `unidad` | el hecho |
| `confianza` | `ALTA` · `MEDIA` · `BAJA` · `SIN_DATO` |
| `fuente` · `fecha` | de dónde salió y cuándo se supo |
| `nota` | **la cita literal**, si la hubo |

La distinción entre permanente y por cohorte es la que hace que esto sirva: el
oidio le pega al lisianthus **siempre**; que esta cosecha se haya perdido la
mitad es **de esta cosecha**. Mezclarlos convierte una mala temporada en una
condena de la variedad.

## Las preguntas

**CICLO** — ¿cuántas semanas del trasplante a la primera flor? ¿cuántas dura la
ventana? ¿hay segunda floración, y de qué tamaño respecto de la primera?

**PLANTULACION** — ¿quién la germina? ¿cuántas semanas en bandeja? ¿entrega de
una vez o por tandas?

**UBICACION** — ¿en qué bloque va bien? ¿en cuál va mal, y por qué? ¿a qué
distancia se siembra? ¿lleva pinch?

**SANIDAD** — ¿qué enfermedad o plaga le pega, y en qué semana del ciclo?
¿cuántas bombas de espalda son una aspersión completa? ¿con qué se choquea?
¿lleva drench, cuántos y con qué?

**NUTRICION** — ¿cómo se preparó la cama? ¿lleva fertirriego, y durante cuánto?

**INFRAESTRUCTURA** — ¿lleva plástico? ¿malla, cuántas líneas? ¿luz, cuántas
horas?

**LABOR** — ¿qué labores pide? ¿cuántos días cada una, y cuántas veces en el
ciclo?

**COSECHA** — ¿cuántos tallos por planta se esperan? ¿se registra por cultivar o
todo junto?

**POSCOSECHA** — ¿cuánto dura en vaso? ¿seca, y con qué rol?

**PRODUCTO** — ¿en qué bouquets entra y cuántos tallos? ¿de qué depende el
conteo?

**COMERCIAL** — ¿qué rol de cartera tiene? ¿cuánto cuesta comprarla en el
mercado?

**DECISION** — ¿qué se decidió sobre ella, por qué, y **cómo resultó**?

> Esa última es la que ninguna planilla guarda y la que más vale. «No pusimos
> plástico para evitar fusarium, costó $1.500.000 en mano de obra y el fusarium
> apareció igual» no está en ningún archivo de Drive, y es lo único que impide
> repetir el error.

## Por qué este formato y no otro

- **CSV y no markdown:** se carga a Postgres directo. Un markdown habría que
  parsearlo, y ese es trabajo que se tira.
- **Formato largo y no ancho:** un dato nuevo es una fila, no una columna. La
  tabla nunca hay que rediseñarla.
- **Un archivo y no veinticuatro:** una lectura en vez de veinticuatro.
- **En el repositorio y no en Drive:** esto no lo captura la gente de campo, es
  conocimiento. Y git guarda el histórico solo, que es lo que `Campo` pide con
  «nada se corrige con `UPDATE`».

## Lo que NO va aquí

Nada que ya esté en Drive. Cosecha, siembras, ventas y germinación los va a leer
`Campo` del original — copiarlos aquí es trabajo que se tira dos veces. Este
archivo guarda **solo lo que no está escrito en ninguna parte**.
