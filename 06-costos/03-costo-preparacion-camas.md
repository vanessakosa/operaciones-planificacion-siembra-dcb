# Costo de preparación de camas

Estado al 2026-09-03. Fuente de cantidades: **`Protocolo_Preparacion_Camas_DCB_v7.pdf`**
(compartido por Vanessa el 2026-09-03) cruzado con las áreas de cama de
`01-infraestructura/03-no-dig-y-preparacion-camas.md`.

Nota para David: `06-costos/DCB-Preparacion-Camas-David.pdf`.

## El protocolo tiene cinco productos, y solo uno tiene costo

| Producto | Dosis | Estado del costo |
|---|---|---|
| **Bokashi** | Sacos por cama, tabla abajo | ✅ **$10.075 / saco de 25 kg** |
| **Haifa Cote NP** | ⅓ del Cote total | ✅ $245.916 / 25 kg = **$9.837/kg** |
| **Haifa Cote NPK** | ⅔ del Cote total | ✅ $239.941 / 25 kg = **$9.598/kg** |
| **Naturcomplet-G** (leonardita) | STD 300 g fijos · PREMIUM 50 g/m² · EMERG. 60 g/m² | ✅ $195.300 / 25 kg = **$7.812/kg** |
| **Sáfer Terra Life GR** | **100 g/m²** en los tres protocolos | ✅ $110.000 / 50 kg = **$2.200/kg** |
| **Sáfer Micorrizas** | Solo camas nuevas · dosis sin dato | ✅ $75.946 / 50 kg = **$1.519/kg** |

**Cote total: 100 g/m² en ESTÁNDAR y EMERGENCIA · 200 g/m² en PREMIUM.** Relación NP:NPK ≈ 1:2.

## Cantidades por cama, verificadas contra el área

| Bloque | Área | Bokashi STD | Bokashi PREM | Terra Life | Cote STD | Cote PREM |
|---|---|---|---|---|---|---|
| Inv 3B | 48,1 m² | 3 sacos | 4 sacos | 4,81 kg | 4,81 kg | 9,62 kg |
| Inv 4C | 40,5 m² | 2,5 sacos | 3 sacos | 4,05 kg | 4,05 kg | 8,10 kg |
| Inv 3A | 35,6 m² | 2 sacos | 3 sacos | 3,56 kg | 3,56 kg | 7,13 kg |
| Inv 5 | 31,7 m² | 2 sacos | 2,5 sacos | 3,17 kg | 3,17 kg | 6,34 kg |
| Inv 4A · 4B | 20,2 m² | 1 saco | 1,5 sacos | 2,02 kg | 2,02 kg | 4,05 kg |
| Inv 3C | 18,0 m² | 1 saco | 1,5 sacos | 1,80 kg | 1,80 kg | 3,60 kg |

**Inv 1 e Inv 2 se preparan con la dosis de Inv 4A/4B**, según nota del protocolo v7.
**El Mini no tiene fila** — hueco confirmado, ya anotado en el protocolo de No-Dig.

## Costo por cama, solo Bokashi

| Sacos | Receta anterior | **V1** | Ahorro |
|---|---|---|---|
| 1 | $14.400 | **$10.075** | $4.325 |
| 1,5 | $21.600 | **$15.113** | $6.488 |
| 2 | $28.800 | **$20.150** | $8.650 |
| 2,5 | $36.000 | **$25.188** | $10.813 |
| 3 | $43.200 | **$30.225** | $12.975 |
| 4 | $57.600 | **$40.300** | $17.300 |

**Piso anual** con las 60 camas contadas (3A 11 · 3C 8 · Inv 4A/4B 28 · Inv 5 13) = 84 sacos por
vuelta: **$363.300 de ahorro por vuelta**, o **$727.000 – $1.090.000 al año** a 2–3 vueltas.
Piso, no estimado: **falta contar 3B** (la dosis más alta), Inv 2, Mini, exteriores e Inv 6.

---

# 🔴 Los cotes: el renglón más grande, sin precio y sin aplicar

**Dato de Vanessa 2026-09-03:** los cotes **no se aplican desde hace unos dos meses**, pero los
que ya están en el suelo **siguen liberando** — son de liberación lenta, así que el efecto de
haberlos suspendido todavía no se ve completo. Es la razón por la que esto hay que revisarlo a
fondo antes de concluir nada sobre rendimiento.

**Cantidades que el protocolo v7 sigue pidiendo**, solo con las 60 camas contadas:

| Protocolo | Por vuelta | A 2–3 vueltas/año |
|---|---|---|
| ESTÁNDAR (100 g/m²) | 151 kg | **300 – 450 kg/año** |
| PREMIUM (200 g/m²) | 303 kg | 600 – 900 kg/año |

Sin 3B, que es el bloque de camas más grandes. **Con el precio por kg de Cote NP y Cote NPK el
número se cierra en una línea**, y de ahí sale la decisión: los cotes vuelven, o el ahorro se
registra y el protocolo v7 se reescribe sin ellos.

## Ya hay un ensayo comparativo en campo, armado solo

`07-datos/campo_siembras.csv` tiene **20 lotes anotados** en COMENTARIOS con qué recibieron:

| Anotación | Lotes |
|---|---|
| "Sin Bokashi, con Cotes" | 15 |
| "SIN COTES SOLO BOKASHI" | 4 |
| "Sin Cotes ni Bokashi" | 1 |

⚠️ **Grupos desbalanceados y no aleatorizados** — 15 contra 4 contra 1, y las semanas de siembra
no coinciden, así que arrastran efecto de temporada. No es un ensayo limpio. Pero **cruzarlo con
`registro_tallos.csv` normalizado por ventana** es la primera evidencia propia disponible sobre
si los cotes aportaban algo que el Bokashi no aporta. Es más de lo que había.

---

# 🔴 Error de expresión en la calculadora v7

**El Naturcomplet-G en protocolo ESTÁNDAR se pide como 300 g fijos por cama**, sin importar el
área. En PREMIUM y en EMERGENCIA sí se pide como tasa (50 y 60 g/m²). Resultado:

| Cama | Área | 300 g fijos equivalen a |
|---|---|---|
| Inv 3B | 48,1 m² | **6,2 g/m²** |
| Inv 3C | 18,0 m² | **16,7 g/m²** |

**2,7× de diferencia por el mismo renglón del protocolo.** Es el mismo tipo de artefacto que el
"3 sacos por cama" ya documentado en No-Dig: dosis fija sobre camas de área distinta. Corregirlo
es reescribirlo en g/m², costo cero — pero **mientras no se corrija, cualquier costo por cama que
se calcule sobre ese renglón está mal.**

**Segundo hallazgo menor:** el Terra Life de Inv 3C se calcula sobre **18 m²**, mientras que
`03-no-dig-y-preparacion-camas.md` registra la cama grande de 3C en **25,2 m²** y la pequeña en
**12,6 m²**. Los 18 m² no son ninguna de las dos — parecen un promedio. Si es así, la cama grande
está subdosificada y la pequeña sobredosificada en los tres productos que van por tasa.

---

# Pendientes

| # | Pendiente | Quién | Desbloquea |
|---|---|---|---|
| 1 | **Precio por kg de Cote NP y Cote NPK** | Vanessa / Haifa | El renglón más grande del costo por cama |
| 2 | **Precio de Naturcomplet-G** | Vanessa | Costo por cama |
| 3 | **Precio de Sáfer Terra Life GR** | Vanessa | Costo por cama |
| 4 | **Área real de las camas de Inv 3C** — ¿25,2 y 12,6, o 18? | Vanessa | Corrige 3 productos por tasa |
| 5 | Reescribir Naturcomplet STD en g/m² | Decisión de Vanessa | Costo cero |
| 6 | Contar camas de Inv 2, Mini, exteriores e Inv 6 | Vanessa | Convierte el piso anual en cifra |
| 7 | Cruzar los 20 lotes con/sin cote contra `registro_tallos.csv` | Motor | La decisión sobre los cotes |


---

# El costo real por cama, con precios · 2026-09-03

## Protocolo ESTÁNDAR

| Bloque | m² | Bokashi | Cote NP | Cote NPK | TerraLife | Natur | **Total** | $/m² |
|---|---|---|---|---|---|---|---|---|
| Inv 3B | 48,1 | $30.225 | $15.661 | $30.884 | $10.582 | $2.344 | **$89.696** | $1.865 |
| Inv 4C | 40,5 | $25.188 | $13.187 | $26.004 | $8.910 | $2.344 | **$75.632** | $1.867 |
| Inv 3A | 35,6 | $20.150 | $11.591 | $22.858 | $7.832 | $2.344 | **$64.775** | $1.820 |
| Inv 5 | 31,7 | $20.150 | $10.321 | $20.354 | $6.974 | $2.344 | **$60.143** | $1.897 |
| Inv 4A · 4B | 20,2 | $10.075 | $6.577 | $12.970 | $4.444 | $2.344 | **$36.410** | $1.802 |
| Inv 3C | 18,0 | $10.075 | $5.861 | $11.557 | $3.960 | $2.344 | **$33.797** | $1.878 |

## Protocolo PREMIUM

| Bloque | m² | Bokashi | Cote NP | Cote NPK | TerraLife | Natur | **Total** | $/m² |
|---|---|---|---|---|---|---|---|---|
| Inv 3B | 48,1 | $40.300 | $31.322 | $61.768 | $10.582 | $18.788 | **$162.760** | $3.384 |
| Inv 4C | 40,5 | $30.225 | $26.373 | $52.009 | $8.910 | $15.819 | **$133.336** | $3.292 |
| Inv 3A | 35,6 | $30.225 | $23.182 | $45.716 | $7.832 | $13.905 | **$120.861** | $3.395 |
| Inv 5 | 31,7 | $25.188 | $20.643 | $40.708 | $6.974 | $12.382 | **$105.894** | $3.341 |
| Inv 4A · 4B | 20,2 | $15.112 | $13.154 | $25.940 | $4.444 | $7.890 | **$66.541** | $3.294 |
| Inv 3C | 18,0 | $15.112 | $11.721 | $23.115 | $3.960 | $7.031 | **$60.940** | $3.386 |

## 🔴 Dónde está el dinero, y no es donde lo estábamos buscando

| | ESTÁNDAR | PREMIUM |
|---|---|---|
| **Los dos cotes juntos** | **50 – 52 %** | **57 %** |
| Bokashi | 28 – 34 % | 23 – 25 % |
| TerraLife | 12 – 13 % | 6 – 7 % |
| Naturcomplet | 3 – 7 % | 12 % |

**El ahorro del Bokashi V1 es real pero es la palanca chica.** Con las 60 camas contadas:

| Palanca | Ahorro por vuelta |
|---|---|
| Bokashi V1 (receta nueva) | $363.300 |
| **Sacar los dos cotes** | **$1.464.383** |

**Los cotes son 4 veces la palanca del Bokashi.**

---

# Lo que dice el análisis de suelo, producto por producto

| Producto | Veredicto | Qué dice el suelo |
|---|---|---|
| **Cote NPK** | 🔴 **Fuera de todos los bloques** | Saturación de K de **23,7 – 30,0 %** contra una referencia de 2 – 5 %. Es el renglón más grande del protocolo y entrega el elemento que está en exceso |
| **Cote NP** | 🔴 **Fuera de Bloque 3 y 5** · duda en Bloque 4 | P alto en Bloque 3 (40,73 · clave A), medio en Bloque 5 (21,22 · M), **bajo solo en Bloque 4** (10,74 · B) |
| **Naturcomplet-G** | 🟢 **Queda — el único que el análisis respalda directo** | Ver abajo: es el que ataca la fijación de fósforo |
| **Sáfer Terra Life** | 🟡 Queda, pendiente de ficha | $220/m². Hay que ver si el compost térmico lo desplaza |
| **Micorrizas** | 🟡 Solo camas nuevas | Ya decidido: camas con 4+ cosechas ya las tienen |
| **Yeso agrícola** | 🟢 **Entra en Bloque 4** | Ver abajo: el hallazgo de la lista de Alma Agrícola |

## Por qué el Naturcomplet es el que se queda

**Un dato de los informes de agosto lo decide solo:**

| | P total (mg/kg) | P soluble (mg/L) |
|---|---|---|
| **Bloque 3** | **40,73** — el más alto | **0,036** — el más bajo |
| Bloque 5 | 21,22 | 0,059 |
| **Bloque 4** | **10,74** — el más bajo | **0,107** — el más alto |

**Bloque 3 tiene 4 veces el fósforo total de Bloque 4 y un tercio del fósforo soluble.**
Es la firma de un **andisol**: la alofana fija el fosfato y lo vuelve indisponible. Agregar más
fósforo a Bloque 3 es agregarlo a un suelo que ya tiene cuatro veces más y no lo puede usar.

**Lo que sí lo libera son los ácidos orgánicos**, que compiten por los sitios de sorción de la
alofana. Es exactamente el mecanismo de la leonardita — y es el mismo argumento por el que
entran los solubilizadores biológicos (ver `02-nutricion/07-programa-biologico.md`).

> **El Naturcomplet no aporta fósforo: destraba el que ya está.** En un suelo con esta firma vale
> más que cualquier fuente de P que se compre.

### ⚠️ Pero la dosis PREMIUM está por encima de la etiqueta

La etiqueta es **100 – 400 kg/ha/año**, no por aplicación:

| Protocolo | Dosis | kg/ha/año a 2,5 aplicaciones |
|---|---|---|
| ESTÁNDAR — 300 g fijos en cama de 48,1 m² | 6,2 g/m² | 156 — **dentro** |
| ESTÁNDAR — 300 g fijos en cama de 18 m² | 16,7 g/m² | 417 — al tope |
| **PREMIUM — 50 g/m²** | 50 g/m² | **1.250 — 3 veces la etiqueta** |

**Propuesta: una sola tasa de 16 g/m² para los dos protocolos.** Da 400 kg/ha/año, el tope de la
etiqueta, que es lo justificado dada la fijación. Y corrige de paso el artefacto de los 300 g
fijos, que hoy entrega 2,7 veces más por m² en la cama chica que en la grande.

## El yeso agrícola: el hallazgo de la lista

**$30.572 / 25 kg = $1.223/kg** — la fuente de calcio más barata de la lista y **8 veces más
barata por kg que el Cote NPK.** Ya está en el protocolo para camas con historial de lisianthus
(200–300 g/m²); el análisis dice que debería ser general en un bloque.

**Por qué es el producto correcto para este suelo:**

- Saturación de Ca de **37,8 – 42,6 %** contra una referencia de 60 – 70 %. Ca en clave **M** en
  los tres bloques: no está deficiente en absoluto, está **desplazado** por el K y el Mg.
- El yeso **no mueve el pH.** A pH 5,6 – 5,8, que ya es el ideal, la cal está descartada — y el
  yeso es la única enmienda de calcio que no alcaliniza.
- **El sulfato desplaza el K y el Mg del complejo de intercambio y se los lleva.** No solo agrega
  calcio: corrige la relación.

**Y va en Bloque 4, por tres razones independientes que coinciden:**

| Razón | Bloque 3 | Bloque 4 | Bloque 5 |
|---|---|---|---|
| Saturación de Ca — dónde más falta | 42,6 % | **37,8 %** 🟢 | 38,5 % |
| Azufre — el yeso aporta 18,6 % de S | 51,67 · **A** 🔴 | 26,55 · M 🟢 | 42,68 · **A** 🔴 |
| Riego — hace falta agua para lixiviar el K desplazado | Bajo | **El mejor de la finca** 🟢 | El peor |

> 🔴 **El azufre es el que manda, no el calcio.** El yeso es 18,6 % de S: a 100 g/m² aporta
> **186 kg de S por hectárea.** Sobre Bloque 3 y Bloque 5, que ya están en **S alto**, eso no se
> puede hacer. Y no hay forma de separarlo: **el sulfato ES el mecanismo** que se lleva el
> potasio. No hay versión del yeso sin azufre.
>
> Por eso entra **solo en Bloque 4, a 100 g/m²** — la mitad de la dosis del protocolo de
> lisianthus — y como ensayo, no como regla. Cuesta **$2.470 por cama de Inv 4A/4B**, contra
> $19.547 de cotes que salen de esa misma cama.

## ¿Y el nitrógeno que aportaban los cotes?

Salir de los cotes quita nitrógeno de liberación lenta. **No es un riesgo, y probablemente sea
parte del arreglo:**

- **N-NO₃ está en 40 – 64 mg/kg** en los tres bloques. No hay deficiencia.
- **M.O. de 18,6 – 23,4 %.** Con ~180 t/ha de materia orgánica en los primeros 15 cm y una
  mineralización de 1 – 1,5 % al año, eso son del orden de **100 – 135 kg de N/ha/año** que el
  suelo libera solo. ⚠️ *Regla de dedo, no medición — se confirma con análisis de savia.*
- El Bokashi aporta N, y el fertirriego ahora entrega N por el Calcinit (15,5 % N).
- **Y bajo Kempf, el nitrato soluble en exceso es exactamente lo que vuelve la planta atractiva
  para chupadores y susceptible a patógenos de suelo** — que es la debilidad documentada de la
  finca, con 29 incidencias en `07-datos/incidencia_fitosanitaria.csv`.

---

# La preparación propuesta

**Sale:** Cote NPK en todos los bloques · Cote NP en Bloque 3 y 5.
**Queda:** Bokashi (igual) · TerraLife 100 g/m² · Naturcomplet **a 16 g/m²** en vez de 300 g fijos.
**Entra:** Yeso agrícola 100 g/m², solo Bloque 4.
**Pendiente:** la fuente de P para Bloque 4 — Cote NP, MAP o DAP, según ficha.

## Costo por cama, actual contra propuesto

| Bloque | ESTÁNDAR hoy | Propuesto | Ahorro | | PREMIUM hoy | Propuesto | Ahorro |
|---|---|---|---|---|---|---|---|
| Inv 3B | $89.696 | $46.819 | **−48 %** | | $162.760 | $56.894 | **−65 %** |
| Inv 4C | $75.632 | $44.112 | **−42 %** | | $133.336 | $49.150 | **−63 %** |
| Inv 3A | $64.775 | $32.432 | **−50 %** | | $120.861 | $42.507 | **−65 %** |
| Inv 5 | $60.143 | $31.086 | **−48 %** | | $105.894 | $36.124 | **−66 %** |
| Inv 4A · 4B | $36.410 | $19.514 | **−46 %** | | $66.541 | $24.552 | **−63 %** |
| Inv 3C | $33.797 | $16.285 | **−52 %** | | $60.940 | $21.322 | **−65 %** |

## El anual, con las 60 camas contadas

| | |
|---|---|
| Costo actual por vuelta | $2.784.224 |
| Costo propuesto por vuelta | $1.437.542 |
| **Ahorro por vuelta** | **$1.346.682 · −48 %** |
| **A 2 vueltas al año** | **$2.693.364** |
| **A 3 vueltas al año** | **$4.040.046** |

**De dónde sale, palanca por palanca (por vuelta):**

| Palanca | |
|---|---|
| Sacar Cote NPK | +$971.663 |
| Sacar Cote NP | +$492.720 |
| Naturcomplet a tasa de 16 g/m² | −$48.534 |
| Agregar yeso en Bloque 4 | −$69.166 |
| **Neto** | **+$1.346.682** |

⚠️ **Sigue siendo un piso.** No incluye Inv 3B, que es la cama más grande y la de dosis más alta,
ni Inv 2, Mini, exteriores ni Inv 6 — esas camas no están contadas.

---

# La lista de Alma Agrícola: qué sirve y qué no

**Naturcomplet, los Cote y el TerraLife NO están en la lista de Alma Agrícola** — son de otro
proveedor, así que ahí no hay competencia de precio para ellos.

## Lo que sirve

| Producto | Precio | Para qué |
|---|---|---|
| **Yeso agrícola** (sulf. calcio) | $30.572 / 25 kg = **$1.223/kg** | 🟢 El calcio de Bloque 4. Ver arriba |
| **DAP** 18-46-0 | $240.350 / 50 kg = **$4.807/kg** → $10.450 por kg de P₂O₅ | 🟡 P para Bloque 4, el más barato por unidad de P |
| **MAP** Amilsol 12-61-0 | $212.302 / 25 kg = **$8.492/kg** → $13.921 por kg de P₂O₅ | 🟡 25 % más caro por unidad de P que el DAP, pero **de reacción ácida y sin amoníaco libre** — más seguro en aplicación localizada |
| **Calcinit** | $79.581 / 25 kg = **$3.183/kg** | ✅ Confirma el precio del comparativo de fertirriego |

## Lo que NO sirve, y por qué

| Producto | Por qué no |
|---|---|
| QROP KS · Allganic Makro 60 · cloruro de potasio · sulfato de potasio · MKP | **Todos son potasio.** Saturación de K en 23,7 – 30 % |
| Cal agrícola · dolomita · cal viva · cal apagada | pH 5,6 – 5,8 ya es el ideal. La dolomita además agrega Mg |
| Kieserita · MF Magnox (óxido de Mg) | **Mg alto** en los tres bloques — saturación 32 – 38 % |
| Azufre micronizado M-325 | **S alto** en Bloque 3 y 5 |
| Roca fosfórica | Ya eliminada. En un andisol la alofana la fija igual |

## Fichas que sí cambian una decisión

| # | Ficha | Qué decide | Prioridad |
|---|---|---|---|
| 1 | **Haifa Cote NP — la fórmula NPK** | Sin el grado no se puede comparar su $/kg de P₂O₅ contra el DAP y el MAP. Es lo único que falta para cerrar la decisión de Bloque 4 | 🔴 **Esencial** |
| 2 | **Sáfer Terra Life GR — organismos y UFC** | Son $220/m². Si son micorrizas + Trichoderma + bacterias, el compost térmico y su extracto cubren esa función **y además traen protozoos y nematodos, que nadie vende** | 🔴 **Esencial** |
| 3 | **Black Diamond GR** (Peti Rouge) | $147.818 / 25 kg = $5.913/kg. Si es leonardita o húmico granulado, es un competidor del Naturcomplet **24 % más barato** | 🟡 Útil |
| 4 | **Vicor** (Colinagro) | $127.650 / 46 kg = **$2.775/kg**, edáfico, el más barato de la lista. No se sabe qué es | 🟡 Útil |
| 5 | Agrimins granulado | $154.961 / 46 kg = $3.369/kg. Suele ser Ca-Mg-S-micros — y el Mg y el S ya están altos, así que probablemente no sirva | ⚪ Baja |
