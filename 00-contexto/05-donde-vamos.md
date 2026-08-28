# Dónde vamos — contexto para retomar

> Última actualización: **2026-08-13**, commit `9ce281f` + cruce por ventana
> de siembra (sin commitear al momento de escribir esto).
> Este archivo es el punto de entrada cuando se retoma después de una pausa.
> Si algo de acá contradice a `07-datos/`, gana `07-datos/`.

---

## Arranque de sesión — tres comandos

```bash
git pull
python3 motor/cerebro.py matriz     # estado medido de las 11 variables
python3 motor/cerebro.py m2         # tallos/m2 por lote  <- nuevo
python3 motor/cerebro.py auditar    # estado del catalogo (31 productos)
```

---

## 🔴 En qué estábamos exactamente

**Revisión de variedades una a una**, con las columnas que pidió Vanessa:
plantas sembradas · tallos cosechados · ventana · **tallos/m²** · ventas y
devoluciones por carrito · bouquets que la llevan · % vendido · problemas de
bitácora · **bombas recibidas y plata invertida** · labores culturales ·
requerimientos de postcosecha.

| Variedad | Estado |
|---|---|
| Boca de Dragón | ✅ hecha |
| **Statice** | ⬅️ **la que sigue** |
| Las otras 19 | pendientes |

**Statice va primero por tres razones que se refuerzan:** es la #2 en volumen
(10.535 tallos), **ocupa el 29,9 % del área medida de la finca entregando
4,9 t/m²**, y tiene **6 % de trazabilidad de cultivar** — o sea que no se sabe
qué variedad sostiene un tercio del cultivo.

De las columnas que pidió, **cuatro no se pueden llenar todavía** y hay que
decirlo en cada ficha en vez de dejarlas en blanco: ventas, devoluciones,
% vendido y plata en bombas. Ver "Lo que sigue bloqueado".

---

## Lo que se construyó (y sirve desde ya)

### `cerebro.py m2` — tallos por metro cuadrado

El área **no está registrada en ningún archivo**: se deriva de plantas ×
distancia de siembra sobre la malla de 0,15 m.
`plantas/m² = 1 / (0,15 × distancia)`. Verificado contra campo: Inv 4A son
112 × 8 = **896 sitios**, el número del propio comentario de Vanessa.

Es el único comando que puede medir un **perenne**: Dahlia se propaga por
división, el conteo de plantas deriva pero el área no.

**Quién ocupa la finca** (solo lotes de una cama, sin doble conteo):

| Grupo | m² | % área | T/m² |
|---|---|---|---|
| **Statice** | 847,9 | **29,9 %** | **4,9** |
| Boca de Dragón | 414,6 | 14,6 % | 22,6 |
| Celosia | 356,0 | 12,5 % | 9,7 |
| **Ammobium** | 214,1 | 7,5 % | **2,3** |
| **Strawflower** | 163,1 | 5,7 % | 10,5 |
| **Campanula** | 37,0 | **1,3 %** | **73,6** |

Detalle completo, matices y las 5 marcas de advertencia:
`13-optimizacion/06-tallos-por-m2.md`.

### Los tres escalones de producto

Definición de Vanessa: **paquete sólido < paquete mixto < bouquet.** Un paquete
mixto puede ser 100 % lineal y estar bien construido, así que **la regla de seis
roles solo aplica a bouquets**. `My Love` quedó recategorizado a `Paquete mixto`.

**Hallazgo:** por unidad la escalera se cumple (45k → 55k → 125k); **por tallo
no** (4.333 → 4.231 → 4.565). El escalón se cobra en tallos, no en precio: la
mezcla sale gratis y cuesta más cama. Detalle en
`11-bouquets/02-paquetes-mixtos.md`.

### Cruce por ventana de siembra + prorrateo de "Mix"

Vanessa preguntó si el cruce siempre revisa la ventana de siembra, y encontró
sola el caso que lo probaba: Boca de Dragón, Potomac Appleblossom, sembrado
dos veces en 3B (2.880 y 3.014 plantas) — el motor las sumaba sin poder decir
cuál produjo el corte. Arreglado con **ventanas de cosecha estimadas por
siembra** (fecha de siembra + ciclo). Cuando se puede aislar una sola siembra
activa, se usa esa; cuando no, queda marcado `AMBIGUO(n siembras)` en vez de
sumarse en silencio.

Se construyó también `cerebro.py prorratear` — reparte cortes "Mix" entre
cultivares activos por **tasa de corte limpia**, como pidió Vanessa
("prorratea como el 2"). Tres pasos hasta llegar a un número usable:

1. Primera corrida: **0 %**. El motor usaba `Fecha siembra campo` (37 %
   llena).
2. Vanessa aclaró que dejó de usarla — hoy trabaja **por semana de
   trasplante**, llena en **97 %** de las filas pero en una columna que el
   lector genérico no podía ver (el archivo tiene DOS columnas "Semana" y
   `csv.DictReader` colapsaba a la última). Arreglado leyendo por posición.
   `ciclos` subió de 37 % a **85 %** calculable, `prorratear` de 0 % a 8 %.
3. Vanessa: *"los fines de cosecha están en las notas, en los comentarios...
   si no existe [ventana] para prorratear, se divide entre las variedades
   sembradas de esa especie."* Se conectó `cierres_lote.csv` (ya extraído de
   comentarios en otra sesión) como fin de ventana REAL, y se agregó una
   escalera de respaldo por partes iguales cuando no hay tasa o no hay
   ventana. **`prorratear` subió de 8 % a 73 %.**

El 27 % restante es honesto: el grupo nunca se sembró en esa cama según
CAMPO. Y **cada fila del CSV dice qué método se usó** — tasa (el más
confiable) vs. partes iguales (dos niveles, menos confiables) — para que no
se sumen como si pesaran igual. Detalle completo en
`13-optimizacion/07-cruce-por-ventana-de-siembra.md`.

---

## Decisiones tomadas que no hay que volver a discutir

| Decisión | Quién / cuándo |
|---|---|
| Malla de siembra = **0,15 m** en las dos direcciones | Vanessa 2026-08-13 |
| **Ventana cerrada → leer t/planta. Ventana abierta → normalizar por día** | Vanessa 2026-08-13 |
| Una cama se considera cerrada cuando dejó de mostrar tallos | Vanessa 2026-08-13 |
| Un ciclo real puede correr **hasta 4 semanas** por delante del Excel | histórico |
| `Inv 4C` = `Inv 4 baja` — mismo sitio, dos nombres | Vanessa 2026-08-13 |
| Inv 2 **no** es "el bloque de pruebas": tiene camas productivas. Es el más irregular, por eso ahí van los ensayos | Vanessa 2026-08-13 |
| Celosia: subtipo es la unidad de manejo. Shimmer y las de Floret son **plumosas**; Dreams, Flamingo y Celway **spicatas** | Vanessa 2026-08-13 |
| Al yugo van los lisianthus de **cabeza** más pequeña, no de tallo más corto | Vanessa 2026-08-13 |
| Enda Rose: **reducida y seleccionada**, no perdida — hubo inducción floral por falta de luz y se cosechan los más largos | Vanessa 2026-08-13 |
| Un producto es distinto si **el cliente lo pide por su nombre**; si se decide al armar el ramo, es una sustitución | Vanessa 2026-08-13 |
| `campo_siembras.csv` es un **log histórico**, no el estado actual del campo | error corregido 2026-08-13 |

---

## Preguntas abiertas para Vanessa

1. **Precios de los 6 productos nuevos** — Yugo pequeño/grande, Greenery,
   Greenery con lisianthus, Bocas y Statice, Dream Land, My Love. Sin precio no
   entran a `valor` ni a la escalera.
2. **`Paquete zinnias sunset` no lleva zinnias** — su receta es 10 Green Ball +
   3 statice. ¿Está mal el nombre o la receta? No se toca hasta saberlo.
3. **Plantas por hueco** — la derivación 7,5 cm → 2 por hueco, 15 cm → 1,
   30 cm → 1 cada dos reproduce los tres casos de la finca, pero conviene
   confirmarla en campo.
4. **Amaranto vino de My Love** — ¿Velvet Curtains o Love Lies Bleeding?
5. **Cultivar del Snapdragon vino de My Love** — el documentado es Potomac
   Crimson.
6. **Bomba 3 sigue trabada**: qué es *"javeana / gviana"*, dosis de Rutastar,
   stock de Neofat, última fecha de Botrycid, cuántas aplicaciones de
   Glukoplant lleva el ciclo. Ver `03-fitosanidad/04-bombas-semana-33.md`.

---

## Lo que sigue bloqueado (y quién lo desbloquea)

`cerebro.py matriz`: **0 de 11 variables listas.**

| # | Falta | Quién | Qué desbloquea |
|---|---|---|---|
| 1 | `costos_productos.csv` vacío | **Vanessa** | margen por m² por semana — el eje del proyecto |
| 2 | Cultivar en Statice, Lisianthus, Zinnia, Strawflower | **Vanessa** | 23.155 tallos sin atribuir. Selección varietal |
| 3 | **No existe archivo de ventas ni devoluciones** | **Vanessa** | 4 de las columnas que pidió para las fichas |
| 4 | `calidad_tallo.csv` vacío | **Vanessa** | "produjo" vs "produjo vendible" |
| 5 | `Inicio cosecha` y `Fin de cosecha` como fecha exacta, no mes | **Vanessa** | Ventana real de cosecha + separar temporada de mezcla de variedad |
| 5b | `Cantidad Trasplantada` en CAMPO | **Vanessa** | 30 % de la cosecha no tiene T/m² por esto |
| 5c | Cultivar en Statice/Lisianthus/Zinnia/Strawflower (ver #2) | **Vanessa** | También desbloquea `prorratear` para esos 4 grupos — hoy sin tasa |
| 6 | `clima_semanal.csv` vacío · microclima cualitativo | **Vanessa** | separar efecto de temporada del de variedad |
| 7 | Leer/escribir `PROGRAMACION_2026` (pesa 11,5 MB) | **David** | fitosanidad completa + dictado directo |
| 8 | Exportar `APLICACIONES` | **David** | el historial se corta en la semana 27 |

**Para el archivo de ventas alcanzan cuatro columnas:** producto · semana ·
vendidos · devueltos. Con eso `combinaciones_venta.csv` deja de ser una lista de
impresiones y pasa a ser un ranking.

Detalle completo: `08-roadmap/03-que-falta-en-la-arquitectura.md`.

---

## Deuda técnica del motor

- **`matriz` calcula la variable 8 con un cruce distinto al de `rendimiento`**:
  reporta 20 % donde `rendimiento` reporta 57 %. `rendimiento` y `m2` ya
  comparten `construir_lotes()`; falta meter `matriz` ahí.
- No existe un comando de vista por variedad que junte cosecha, ciclo, cierres,
  fitosanidad y comentarios. Las fichas se arman a mano.
- El margen no existe porque no hay costos.
- `motor/espejar.py` se quedó sin fuente: leía los transcripts de sesión de
  `~/.claude/projects/`, que no viajan con el repo.

---

## Errores que ya se cometieron — para no repetirlos

- **Leer un XLSX de Drive como texto trunca sin avisar.** Devolvió 251 filas de
  598. Siempre bajar el binario y pasarlo por `motor/importar_tallos.py`.
- **Un filtro por redacción rompe en silencio.** `cargar_recetas()` exigía la
  frase *"flores DCB"* en la cabecera y tiró a la basura Dream Land y My Love:
  el archivo decía 31 productos y el motor veía 29. Ahora filtra por categoría,
  con lista blanca, para que una categoría nueva se **reporte** en vez de
  desaparecer.
- **Un ritmo sobre una ventana fragmentada miente al revés.** Amaranto Emerald
  Tails encabezaba su bloque con 48 t/m²/sem, que eran 380 tallos en **dos
  días**. Por eso existe la marca `FRAGMENTO`.
- **Escribir un CSV con `DictWriter` sin `restkey` pierde filas** cuando alguna
  está malformada. Corrompió `ciclos_variedad.csv` una vez.
