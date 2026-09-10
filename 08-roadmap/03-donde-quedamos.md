# Dónde quedamos — sesión del 2026-09-10

**Para retomar en otra conversación.** Lee este archivo primero y corre los tres
comandos de abajo; con eso queda el estado completo sin releer la sesión.

```bash
git pull
python3 motor/cerebro.py cartera          # la mesa de la sesión, ya por niveles
python3 motor/dictar_tallos.py estado     # hasta qué fecha llega la cosecha
python3 motor/cerebro.py matriz           # las 11 variables de decisión
```

Rama de trabajo: `claude/registro-de-tallos-gouhsr`. Todo está pusheado.

---

## 1. Lo que estábamos haciendo

**Sesión de cartera:** decidir variedad por variedad qué se queda, qué se va, de
qué sembrar más y de qué menos. Se interrumpió dos veces por problemas técnicos
(el desplegable del registro) y por dos correcciones de fondo que cambiaron el
marco del análisis.

**El estado de la sesión:** los 23 grupos ya tienen rol de cartera y regla de
siembra. **Falta el paso siguiente: convertir esas reglas en calendario** — o sea
decidir, con la cadencia de cada grupo, qué se siembra en qué semana y en qué
cama.

## 2. Las tres cosas que cambiaron el marco (leer antes de decidir nada)

### a) La cartera tiene niveles, no es una lista

`BASE` · `BASE_ENCAJE` · `FOCAL` · `FOLLAJE` · `TOQUE` · `TOQUE_ENSAYO`. Cada uno
se juzga distinto. **Medir un TOQUE por volumen es un error de categoría.** Vive
en `07-datos/roles_cartera.csv`, explicado en
`13-optimizacion/03-estrategia-de-surtido.md`.

### b) El registro de cosecha es una foto de 12 semanas, no del año

Va de la **semana ISO 22 a la 33** (31/05 → 12/08/2026). Está truncado por los
dos lados:

- **Por la izquierda:** 9 grupos tienen picos o cierres documentados *antes* de
  la semana 22. Su columna OFERTA no mide la variedad, mide desde cuándo se anota.
- **Por la derecha:** faltan las semanas 33 a 37, así que todo lote abierto al
  12/08 sale subestimado.

**El caso que lo enseñó:** Larkspur aparecía con 243 tallos y yo lo presenté como
el caso más claro de "se va". Falso — eran 4.788 plantas con pico en la semana 21,
antes del registro, y el comentario de campo dice *"cosecha extraordinaria en
semana 21 y 22, un balde diario"*. `cerebro.py cartera` ahora advierte de las dos
truncaduras y marca los grupos afectados con `<TRUNCADO`.

### c) El modelo de costo por tallo ya existe y le falta una fila

`DCB_Modelo_Costos` (Google Sheet, Drive) tiene la hoja *"Parámetros mensuales de
costo por tallo"* con las fórmulas corriendo y los costos de 2026 cargados. **Su
único campo manual es `Tallos vendidos en el mes`, en 0 los doce meses.** Doce
números y el costo por tallo real del año queda calculado.

Piso ya calculable contra la cosecha registrada: **$1.379/tallo en junio, $869 en
julio**. Contra ingresos por tallo propio de $10.000 (Dream Big) a $1.731
(Paquete gomphrenas frambuesa) — **ese último está por debajo del piso de junio.**

---

## 3. Lo que quedó pendiente de Vanessa

Ordenado por lo que más desbloquea.

| # | Qué | Por qué importa |
|---|---|---|
| 1 | **Las 4 semanas del registro** (13/08 → hoy) | La operaria las estaba subiendo. Sin ellas, 16 grupos salen subestimados. Cuando estén: bajar el XLSX **binario** y correr `importar_tallos.py` |
| 2 | **`Tallos vendidos` por mes** en `DCB_Modelo_Costos` | 12 números → costo por tallo real, y las decisiones de cartera pasan de volumen a plata |
| 3 | **Contar el larkspur y el ammobium secos** en bodega | El material seco es el fuerte en dinero de diciembre (coronas y guirnaldas) y no se cuenta en ninguna parte. Archivo listo: `07-datos/inventario_seco.csv` |
| 4 | **Tres arreglos en LISTAS (Drive)** | ⚠️ **Los 5 grupos nuevos YA los agregó Vanessa** el 2026-09-10 — LISTAS tiene 25 grupos, no volver a pedirlo. Lo que queda es quitar el plural: `Craspedias` → `Craspedia` y `Esparragos` → `Esparrago` (en plural no cruzan con `campo_siembras.csv` ni con los 40 tallos ya registrados), y poner `Potomac Appleblossom` en `S2` |
| 5 | **Precio de los dos Yugos** | Son los únicos productos sin precio, los de mayor color libre (75 % y 84 %), y **las únicas dos recetas que piden Celosia** — la siembra más grande de la finca |
| 6 | **Composición de "Dusty con colitas"** | Producto nuevo, solo se sabe que lleva 7 colitas. Ver `11-bouquets/03-recetas-pendientes.md` |
| 7 | **Semilla de Girasol `Pro Cut Plum`** por Andrés | Ball no la germina. Es el girasol más vendible por paquete |
| 8 | **Dahlias en Drive:** 3 filas en la BITÁCORA + columna N | `Dahlia Ball` · `Dahlia Mix DCB` · `Dahlia Italiana` ya aprobados. Sin homologado no entran al calendario de Erica |

## 4. Lo siguiente que hay que hacer aquí

1. **Green Ball: calcular la cadencia.** Vanessa lo pidió explícitamente:
   contrastar **las dos camas de 4A contra la de 4B** — sembrado vs cosechado,
   ventana real y tallos — porque se solaparon en cosecha y *"perdemos un
   montón"*. El resultado decide si se espacia más la siembra. Es la única tarea
   de análisis que quedó nombrada y pendiente.
2. **Convertir las cadencias en calendario de siembra.** Ya hay cadencia escrita
   para Amaranto (3 sem), Celosia spicata (3 sem), Cristata (mensual), plumosa
   (3 sem) y Dusty Miller New Look (mensual). Falta cruzarlas con
   `capacidad_bloques.csv` y con las camas ocupadas para ver si caben.
3. **Terminar el recorrido de cartera.** Campánula es el único `FALTA` limpio (no
   truncado, sin cosecha desde el 15/07). Boca de Dragón sale `SOBRA +10 pp` y es
   BASE, así que hay que mirarlo con calma.
4. **El rediseño de la captura.** Vanessa se lo va a plantear a David: que la
   operaria dicte por WhatsApp en vez de llenar la hoja. La capa de validación ya
   existe y está probada (`motor/dictar_tallos.py`); **lo único que falta es el
   transporte.**

## 5. Cosas que se arreglaron hoy y conviene no volver a romper

- **El desplegable del registro** ya no depende de ningún script: la validación
  vive dentro del archivo. Si vuelve a fallar, el arreglo completo con sus
  scripts está en `05-programacion/07-desplegables-registro.md`. **Y ojo: en esa
  hoja las fórmulas van con punto y coma**, no con coma (configuración de
  Colombia).
- **Una validación tiene DOS rangos y los dos se quedan cortos.** El de *a dónde
  se aplica* (`B3:B2000`) y el de *de dónde lee* (`LISTAS!A2:A100`). El primero
  fue el fallo de la columna C; el segundo apareció después — Vanessa agregó 6
  grupos a LISTAS y el desplegable de Grupo seguía leyendo el rango angosto con
  el que se creó cuando había 19, así que a Diana no le aparecían Craspedia ni
  Scabiosa. **Dejar los dos rangos generosos**: agrandarlos no cuesta nada y
  quedarse corto falla en silencio.
- **`listas_desplegables.csv` tenía 19 opciones y la hoja tiene 96.** Era un bug
  de `importar_tallos.py`, que cortaba cada fila al ancho del encabezado.
  Corregido, pero **verificar en la próxima importación** que reporte las
  columnas sin título.
- **`paleta_color.csv` tiene columna `subtipo`** y el motor resuelve
  `"<grupo> <subtipo>"`. Es lo que hace que "Celosia plumosa" de las recetas
  encuentre sus cultivares.
- **Nada se escribe a mano en un archivo espejado.** `registro_tallos.csv`,
  `campo_siembras.csv`, `formulas_productos_bouquets.csv` y la BITÁCORA se
  reescriben completos desde Drive. Para eso están las salas de espera:
  `registro_tallos_dictado.csv` y `11-bouquets/03-recetas-pendientes.md`.

## 6. Preguntas abiertas que nadie ha contestado

- **Celosia:** 41.330 plantas, la siembra más grande de la finca, y solo la piden
  los dos Yugos sin precio. Vanessa dijo que es BASE y que *"hay que analizar un
  poco las ventas y las devoluciones"* de la plumosa. Sin eso no se sabe si sobra
  o si el catálogo la subusa.
- **Ammobium:** el campo dijo *"demasiada cantidad de flor para la que piden"* y
  *"muchas devoluciones y pérdidas en carritos, pudrición de la parte baja del
  tallo"*. Es BASE y se seca súper bien. Las dos cosas no se han conciliado.
- **Misty Lavender (larkspur):** ¿se retira? Light Blue seca mejor. Vanessa
  mencionó que *"el rosado se seca buenísimo"*, pero en LISTAS no hay ningún
  larkspur rosado — solo `Mix`, `Misty Lavender` y `Light Blue`.
- **El complemento del Amaranto Velvet y del Cocoa.** Al Velvet le iría bien
  *"algo rosado"*; el Cocoa necesita *"algo que le dé vida, que todavía no sé qué
  es"*.
- **Inv 1 no aparece ni una vez en el registro de cosecha**, y ahí están las rosas
  de jardín injertadas de ~7 años, el cultivo de mayor ticket de la finca.
