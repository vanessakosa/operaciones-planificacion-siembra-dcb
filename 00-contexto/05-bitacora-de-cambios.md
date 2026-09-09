# Bitácora de cambios del programa

Registro fechado de los cambios de nivel programa — no de siembra ni de aplicación semanal.
Las decisiones puntuales van en `07-datos/decisiones_manejo.csv`; el brain dump semanal va en
`04-variedades/notas-campo.md`.

---

# 2026-09-03 · semana ISO 36 · T = 0

# 🟢 ARRANQUE DEL PROGRAMA DE FERTILIZACIÓN INTEGRAL

**Decisión de Vanessa.** Desde hoy se aplica **en todos los bloques**, y reemplaza lo anterior:

| Pieza | Reemplaza a | Documento |
|---|---|---|
| **Fertirriego — fórmula única** | Las 4–5 fórmulas por invernadero y etapa | `05-programacion/hojas-operario/fertirriego-formula-base.html` v3 |
| **Preparación de camas v8** | `Protocolo_Preparacion_Camas_DCB_v7.pdf` | `01-infraestructura/06-formulacion-camas-v8.md` |
| **Bokashi V1** | La receta con humus, ceniza, sulfato de cobre y 320 kg de harina | `01-infraestructura/05-bokashi-v1-y-compost.md` |
| **Compostaje térmico** | La pila fría sin volteo ni temperatura | `01-infraestructura/05-bokashi-v1-y-compost.md` |

**Fundamento:** los tres informes de suelo **38189, 38190 y 38191** de Natural Control
(muestreo 2026-07-29, entrega 2026-08-25), leídos bajo los marcos de **Elaine Ingham** y
**John Kempf**. Decisión razonada en `02-nutricion/08-la-apuesta-ingham-kempf.md`.

## Qué cambia, en una tabla

| | Antes | **Desde hoy** |
|---|---|---|
| Fórmulas de fertirriego | 4–5, por invernadero y etapa | **1**, todos los bloques y etapas |
| Números que maneja el operario | 20–25 | **3** |
| Productos de fertirriego | Polyfeed · Bitter Mag · Haifa Micro · N-Cal · Fullfert | **Calcinit · Borosol · solución de cobre** |
| Productos de preparación de cama | 5 | **3** |
| Estratos de aplicación en cama | 5 pasos con producto | **3** |
| Costo de preparar una cama | $1.802–1.897/m² | **$640–782/m²** · −58 a −66 % |

## Lo que sale, y por qué

| Sale | Razón |
|---|---|
| **Haifa Cote NP y NPK** | La bomba nueva resuelve el pico hídrico que era su premisa · 50–57 % del costo de la cama · recubrimiento polimérico, el residuo más persistente del programa · y los dos marcos los rechazan por caminos opuestos |
| **Polyfeed** | Aporta K a un suelo con saturación de 23,7–30 % contra referencia de 2–5 % |
| **Bitter Mag** | Aporta Mg a un suelo con saturación de 32–38 %. Y es sulfato de magnesio: **es la fuente del azufre alto de Bloques 3 y 5** |
| **Haifa Micro** | $40.294/kg. El cobre por tanque sale a $124 con el quelato simple contra $7.253 con el Micro |
| **Sáfer Terra Life** | Declara **1,1×10⁴ UFC/g** y el suelo mide Trichoderma residente en **1,4×10⁶ UFC/g** — el producto aporta 0,0009 % de lo que ya hay |
| **Naturcomplet** | Es de Bam. Reemplazado por Black Diamond GR, leonardita confirmada, 24 % más barato |
| **Humus de lombriz** (Bokashi) | El ingrediente más caro, sobre un suelo con M.O. de 18,6–23,4 % |
| **Ceniza de madera** (Bokashi) | El ingrediente más concentrado en K de la receta |

---

# El estado del cultivo hoy — la línea base contra la que se mide

**Esta es la razón de fondo para fechar el arranque.** Sin un T = 0 registrado, en seis meses no
se puede atribuir nada.

## Suelo · informes 38189 · 38190 · 38191 · agosto 2026

| | Bloque 3 | Bloque 4 | Bloque 5 |
|---|---|---|---|
| pH | 5,7 | 5,6 | 5,8 |
| M.O. % | **18,6** | **23,4** | 22,9 |
| CICE cmolc/kg | 9,35 | 10,70 | 10,19 |
| Saturación de Ca % | 42,6 | **37,8** | 38,5 |
| Saturación de Mg % | 32,2 | 32,1 | **37,8** |
| **Saturación de K %** | 25,3 | **30,0** | 23,7 |
| P total mg/kg | **40,73** A | 10,74 B | 21,22 M |
| **P soluble mg/L** | **0,036** | **0,107** | 0,059 |
| S mg/kg | **51,67** A | 26,55 M | **42,68** A |
| **Cu mg/kg** | 3,4 M | 3,7 M | **2,9 B** |
| C.E. dS/m | 0,280 | 0,260 | — |
| D. aparente g/cm³ | 0,71 | 0,56 | — |

*Referencia de saturación de bases: Ca 60–70 % · Mg 10–20 % · **K 2–5 %**.*

## Biología · Bioquirama · noviembre 2025

| | |
|---|---|
| Trichoderma | **1,4×10⁶ UFC/g** |
| Fusarium | 3×10⁴ UFC/g |
| Relación | **127× a favor del Trichoderma** |

## Fitosanidad

**29 incidencias registradas** en `07-datos/incidencia_fitosanitaria.csv` — fusarium, botrytis,
mosca blanca, mildeo, oidio y roya. Inóculo confirmado en suelo de **3C, Inv 5 e Inv 4**.

## 🔴 Lo que NO tiene línea base, y es el hueco del arranque

| Instrumento | Estado |
|---|---|
| **Longitud y grado de tallo** | `07-datos/calidad_tallo.csv` **está vacío** |
| **Análisis de savia** | **Nunca se ha hecho** |
| **Suelo de Inv 1** | **Nunca se ha muestreado** — y es el cultivo de mayor ticket |
| Litros de tanque por m² por bloque | Sin dato — traba todo el $/m² |

> **Se arranca el programa con dos de los tres instrumentos de medida sin instalar.** No es un
> riesgo agronómico: es que si la biología no entrega en el primer ciclo, **no hay forma de verlo
> temprano.** Lo que cubre esa brecha:
>
> 1. **Los cotes ya aplicados siguen liberando** — la transición es gradual quiera o no, y ese
>    amortiguador del primer ciclo **ya está pagado.**
> 2. **Empezar a medir longitud de tallo hoy.** Cuesta una cinta métrica.
> 3. **Dejar 3–4 camas de Inv 4A con cote, como control.** Inv 4A tiene el mejor riego de la
>    finca, así que el control mide biología y no agua.

---

# Qué se espera ver, y cuándo

| Plazo | Qué debería moverse | Dónde se lee |
|---|---|---|
| **Inmediato** | El costo por cama, −58 a −66 % | `06-costos/03-costo-preparacion-camas.md` |
| **2 semanas** | Bokashi V1 listo, y su análisis de laboratorio | Análisis de abono orgánico |
| **1–2 ciclos** | Longitud de tallo — que no baje | `calidad_tallo.csv`, si se empieza a llenar |
| **Próximo análisis de suelo** | **S bajando** en Bloques 3 y 5, al salir el Bitter Mag. Si baja a clave M, **el yeso entra en los tres bloques** |
| **Próximo análisis de suelo** | **Saturación de K bajando** desde 23,7–30 %. Es el indicador central de todo el cambio |
| **Próximo análisis de suelo** | Cu de Inv 5 saliendo de clave B |
| **2–3 ciclos** | Incidencias fitosanitarias bajando, por la vía de la Fase 1 de Kempf | `incidencia_fitosanitaria.csv` |
| **⚠️ NO esperar** | Un salto en el CICE por la leonardita — a 125 kg/ha es 0,014 % de la masa del suelo | — |

---

# Pendientes abiertos al momento del arranque

| # | Pendiente | Quién |
|---|---|---|
| 1 | **Pesar un saco lleno de tierra negra** antes de armar el Bokashi — si da 40 kg y no 25, son 10 sacos y no 16 | Campo |
| 2 | **Hortensias: rosado o azul**, para cerrar el destino de los dos bultos de ceniza | Vanessa |
| 3 | **Cuántas camas de Inv 4A quedan con cote** como control | Vanessa |
| 4 | Análisis del Bokashi V1 — **el % de K decide la dosis por cama** | Laboratorio, ~15 días |
| 5 | Litros de tanque por m² por bloque | Campo |
| 6 | Análisis de suelo de **Inv 1** | Natural Control |
| 7 | Primer **análisis de savia** | Natural Control |
| 8 | Contar camas de Inv 2, Mini, exteriores e Inv 6 | Campo |
| 9 | Ficha de **Vicor** ($2.775/kg) y origen del boro del **Borosol** | Alma Agrícola |
| 10 | **Cobre foliar** para la ventana de prefloración — el Kelasys no declara uso foliar | Sesión siguiente |

---

# Cambio de proveedor

**De Bam (Naturcomplet y Haifa) a Alma Agrícola**, decidido por precio. Consecuencias registradas:

- El **Naturcomplet** no está en Alma Agrícola → reemplazado por **Black Diamond GR**
- Los **Cote** y el **Terra Life** tampoco están → salen del programa por otras razones
- El **Cote NP** ya era difícil de conseguir, y por eso se venía aplicando solo NPK a dosis menor
- **Calcinit** en Alma Agrícola a **$3.183/kg** contra $7.614/kg del Haifa N-Cal, **con ficha
  idéntica** ([Y-FPT215], 15,5-0-0-26,0 CaO, doble sal, grado fertirriego)

---

# 2026-09-09 · Protocolo de inoculación nuevo · **T=0 de la inoculación**

**Aprobado por Vanessa. Vigente para toda siembra.** Ejecución en
`02-nutricion/03-drench-inoculacion.md` y en la hoja
`05-programacion/hojas-operario/inoculacion.html`.

## Qué reemplaza

| | Antes | Desde hoy |
|---|---|---|
| **Método** | Tanque de 2.000 L por bloque, por goteo | **Bomba de espalda de 20 L, cama por cama** |
| **Alcance** | El bloque entero, camas en producción incluidas | **Solo las camas que se están preparando** |
| **Momento** | Calendario, cada 3–4 semanas (≈15/año) | **Una vez por vuelta de cama**, más la bandeja |
| **Etapas** | Una | **Dos: bandeja (raíz) y cama (suelo)** |
| **Productos** | Fitoderma · Estabios · Promobac · Raizal · Fullfert | **Bandeja:** Endorhiza · Nube · Promobac (+ Fitoderma o Interactor según variedad) · **Cama:** Fosfolip |
| **Costo** | **$4.446.915/año** | **≈$290.000/año**, con más cobertura |

## Línea base contra la que se va a medir

| Indicador | Valor de partida | Qué contesta |
|---|---|---|
| **P soluble** | **0,107 mg/L** | Si el Fosfolip a 2× etiqueta está trabajando. Directo, barato, sin esperar tallos |
| ***Trichoderma*** | 1,4×10⁶ UFC/g *(compuesto Bloque 3+4)* | Si el drench era el motor del 127× o lo era el Bokashi + No-Dig |
| ***Fusarium*** | 3×10⁴ UFC/g *(mismo compuesto)* | El blanco del Fitoderma en bandeja |
| **Mortalidad por *Fusarium* en lisianthus** | 11 eventos registrados | El desenlace que importa en Bloque 3 |
| **Infiltración del drench** | **no medida** | Abrir un hueco y medir los centímetros del frente de humedad |
| **Bacterias del suelo** | **nunca medidas** | Convertiría el "51× sobre el umbral" en un % de la población real |
| **Colonización micorrízica** | **nunca medida** | Prueba directa de la hipótesis de pérdida de diversidad |

## Lo que hay que pedir para cerrarlo

**A Bioquirama, en un solo correo:** ¿Endorhiza, Nube, Promobac, Interactor y Fitoderma se pueden
aplicar en la misma mezcla? · Panel completo de Ingham (F:B, protozoos por grupo, nematodos por
grupo funcional, % de colonización micorrízica) · **separar el compuesto: Bloque 3 solo, Bloque 4
solo, y Bloque 5, que nunca se ha medido** · conteo de viabilidad del Promobac de la bodega, con
fecha y lote · ¿qué es el Biohar Forte y cuál es su dosis?

**A Alma Agrícola:** precio del Endorhiza, del Interactor y del Nube · UFC/g del No Fly · ¿el
Fosfolip es 1 o 2 L/ha? *(el repositorio tenía 2, Vanessa confirma 1)* · UFC por organismo del
Estabios.

**En la finca:** análisis de agua del nacimiento (pH · C.E. · bicarbonatos · Ca · Mg · Na · K ·
S-SO₄ · Fe · B · dureza) — la fórmula de fertirriego se diseñó tratando el agua como un blanco ·
y refrigerar el Promobac y el Fosfolip.

## Cómo se construyó, para el registro

El protocolo salió de **quince correcciones de Vanessa en una sola sesión**. Las de fondo:

1. **El método:** bomba de espalda, no tanque — las camas están mezcladas dentro de cada bloque.
2. **La base de la dosis:** si la etiqueta la da en la unidad de la mezcla, se usa esa. No se
   deriva, no se convierte, y **no se "verifica" contra otra cifra del mismo análisis** (mi
   comprobación del Fitoderma era circular).
3. **La arquitectura:** base para todas + el específico de cada debilidad, en **un solo pase** —
   separar en dos días no separa nada, porque los organismos conviven en el mismo sustrato
   durante semanas.
4. **Sin duplicados:** ningún producto en dos etapas. Bandeja = raíz, cama = suelo.
5. **Una bomba es una sección de la cama**, no una fracción de la mezcla.
6. **Un umbral biológico se busca y se cita.** El "10⁵–10⁶ UFC/planta" que usé para tres
   decisiones lo había afirmado de memoria; el rango publicado real es **10⁶–10¹¹ UFC/ha**, y
   contra él la etiqueta del Fosfolip resultó bien calibrada y la del Promobac 281× inflada.
