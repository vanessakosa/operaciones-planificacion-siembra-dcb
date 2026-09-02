# Diagnóstico y propuesta de manejo de suelo — marcos Kempf e Ingham

> Sesión 2026-09-02, a partir de los informes de suelo 38189/38190/38191 (agosto 2026).
> **Estado: DIAGNÓSTICO ACEPTADO en la parte de causas. Las acciones que cambian fórmulas o
> dosis están marcadas `PENDIENTE DE VALIDACIÓN` y no se han aplicado a ningún archivo operativo.**

## Los dos marcos, sin confundirlos

Es fácil intercambiarlos. No dicen lo mismo y no están de acuerdo:

| | **Elaine Ingham** | **John Kempf** |
|---|---|---|
| Tesis | La mayoría de los suelos ya contienen décadas de reservas minerales. Con red trófica completa **la biología las libera**. Los insumos minerales son en gran medida innecesarios | **La biología sola es demasiado lenta.** Aplicar minerales dirigidos para forzar los saltos de fase, y medir en savia si llegaron |
| Herramienta | Compost aeróbico, extracto de compost, conteo de biología | **Análisis de savia** + corrección mineral |
| Sobre M.O. | Hábitat | Casi no habla de M.O. — habla de minerales y fases |

**Kempf es el mineralista. Ingham es la que dice que no apliques minerales.**

### Cómo se reparten en DCB

- **Ingham tiene razón sobre los macronutrientes.** M.O. 18.6–23.4%, K saturado al 24–30%,
  Mg al 32–38%, S alto, P total alto. No falta nada de eso: falta el motor que lo libere. La
  prueba está en el P — **P total alto y P soluble bajo en los tres bloques simultáneamente.**
- **Kempf tiene razón sobre los micronutrientes y sobre la velocidad.** El Cu en 2.9 mg/kg en
  Bloque 5 no se corrige solo con biología, y cada ciclo de statice perdido por botrytis en la
  semana 16 cuesta plata hoy.

> **Regla operativa: marco Ingham para los macronutrientes (dejar de agregarlos, construir la
> biología que los libere). Marco Kempf para los micronutrientes y para la medición (corregir
> Cu y B dirigido, verificar en savia).**

## Las 4 fases de Kempf y dónde está DCB

| Fase | Qué logra la planta | Contra qué la protege |
|---|---|---|
| 1 | Sin nitratos ni aminoácidos libres en savia | Patógenos de suelo, **chupadores (mosca blanca, áfidos)** |
| 2 | Fotosíntesis completa → proteína completa | Larvas |
| 3 | **Síntesis de lípidos por encima de la demanda** | **Hongos aéreos — botrytis, oidio, mildeo** |
| 4 | Metabolitos secundarios | Bacterias, autodefensa, vida en florero |

**Las 29 incidencias de `07-datos/incidencia_fitosanitaria.csv` no son cinco problemas
distintos. Son dos fallas de fase, repetidas:**

**Falla de Fase 1 — N soluble en savia.** Mosca blanca en matricaria (4 lotes, 2 sacrificados),
fusarium en lisianthus (11 registros en semana 20), fusarium en Green Ball. Mosca blanca y
fusarium son ambos indicadores de nitrato. N-NO₃ en 64.4 / 44.4 / 40 mg/kg, y el N-NH₄ ni
medido.

**Falla de Fase 3 — síntesis de lípidos bloqueada.** Botrytis en statice y limonium (6+
registros, siempre entre semana 14 y 21 de cosecha), oidio en lisianthus 3B, mildeo en dahlias
y rosas. Los cofactores de la síntesis de lípidos:

| Cofactor | B3 | B4 | B5 | Veredicto |
|---|---|---|---|---|
| Cu | 3.4 M | 3.7 M | **2.9 B** | Limitante clásico. B5 deficiente |
| Mn | 14.4 A | 14.0 A | 15.0 A | OK |
| B | 1.00 M | 1.64 M | 1.37 M | Suficiente, no holgado |
| Zn | 6.3 A | 6.9 A | 5.0 A | OK |
| **P soluble** | **0.036 B** | **0.107 B** | **0.059 B** | **Bajo en los tres** |

**Los dos limitantes de Fase 3 en DCB son el Cu y el P soluble.**

## El eslabón que explica 3C, 4B, Inv 1 y las noches

El **Ca soluble está ALTO en los tres bloques** (0.976 / 0.422 / 0.372) y aun así hay síntomas
de Ca en tejido: botrytis, pétalos separados en bocas de 4B, tallos delgados en lisianthus.

La razón: **el Ca no se absorbe activamente — entra por flujo de masa arrastrado por la
transpiración.** Sin transpiración no hay entrega de Ca al tejido en crecimiento, aunque el
suelo esté lleno.

Y el perfil de microclima dice exactamente eso:
- **3C: humedad nocturna alta** → poca transpiración nocturna → *"la cama más problemática del
  bloque para lisianthus"*. Ya estaba documentado, sin la explicación.
- **Inv 1: humedad nocturna alta** → mildeo en rosas.
- **4B: bocas con pétalos separados**, hipótesis del repo *"estrés hídrico o déficit de Ca/B"*.
  **Son la misma cosa: el estrés hídrico ES el déficit de Ca, porque corta el vehículo.**

> **En DCB el Ca no es problema de dosis, es problema de entrega.** Se corrige con movimiento de
> aire nocturno, no regando al atardecer, y Ca foliar en la ventana correcta — **no con más Ca
> al suelo.**

---

# Por qué el patrón es generalizado: tres causas, no una

| Hallazgo en los 3 bloques | Causa dominante |
|---|---|
| M.O. 18.6–23.4% · D.ap 0.56–0.71 · Sat. humedad 133–155% · pH 5.6–5.8 · franco arenoso | **Característica del suelo** |
| **P soluble bajo aunque el P total sea alto** | **Característica del suelo** |
| **K y Mg altos, Ca relativamente bajo** | **Hídrico (falta de lixiviación) + aporte** |
| **Ca no llega al tejido pese a Ca soluble A** | **Hídrico (transpiración)** |
| **Cu bajo, y por qué B5 no respondió** | **Hídrico (entrega desigual)** + característica |
| **Fe "bajo"** | **Probable artefacto del umbral del laboratorio** |
| Extracción por cultivo | **Real, pero la menor. Y hoy juega a favor** |

## 1. Característica del suelo — lo que no se va a cambiar

El perfil (D. aparente 0.56–0.71 contra 1.2–1.4 de un suelo mineral normal; M.O. 18–23% contra
3–6%; sat. humedad 133–155%; pH ácido; P total alto con P soluble bajo) es el de un **suelo
derivado de ceniza volcánica (andisol)**, que es lo que domina el altiplano del Oriente
Antioqueño. *La taxonomía es conocimiento general — jerarquía nivel 4 — pero los cinco
indicadores son datos propios y apuntan todos en la misma dirección.*

> **La fijación de fósforo es LA propiedad firma de los andisoles.** Los complejos de alófana y
> Al-humus atrapan el fosfato con fuerza extraordinaria. De ahí P total 40.73 y P soluble 0.036
> en el mismo bloque.

**Consecuencia: ese P bajo no se resuelve comprando P.** Es lo que pasó con los años de roca
fosfórica — el P total subió a 97–103 y el disponible nunca subió. La única vía que funciona en
un andisol es la biológica: bacterias solubilizadoras y el ciclo de depredación de protozoos,
que liberan P en la rizosfera antes de que la alófana lo reatrape. **En este suelo el argumento
de Ingham no es filosofía: es la única química que funciona.**

Lo mismo aplica en parte al Cu: **la M.O. es el quelante más fuerte que existe para el cobre.**
Con 20% de M.O., una fracción del Cu está secuestrada por causa estructural.

Y explica por qué la M.O. no se sustrae: la alófana la protege de la descomposición.

## 2. Hídrico — el hilo que conecta más hallazgos

**Mecanismo A — no hay lixiviación, así que nada sale.** 66–74% de arena. En campo abierto, con
la lluvia de Rionegro, el K y el Mg se lavarían del perfil. Pero: **bajo plástico no entra
lluvia**, y **el riego por déficit nunca aplica por encima de capacidad de campo el tiempo
suficiente para arrastrar sales bajo la zona radicular.**

> **El sistema no tiene fracción de lavado. Todo lo que entra, se queda.** Y lo que más entra y
> más soluble es, es potasio. **El problema del agua y el problema del potasio son el mismo problema.**

**Mecanismo B — el Ca no viaja sin transpiración.** Ver sección anterior.

**Mecanismo C — la entrega de fertirriego es proporcional a la entrega de agua.** Ver la nota
sobre Bloque 5 y el cobre en `01-infraestructura/02-analisis-de-suelo.md`. Bloque 5 tiene los
cuatro indicadores de tanque en su mínimo simultáneamente. **Es la prueba empírica de que el
fertirriego amplifica la desigualdad del riego.**

## 3. Extracción por cultivo — la menor, y hoy a favor

Test lógico que zanja el asunto:

> **Las flores de corte son acumuladoras de potasio** — el K es el catión dominante en savia.
> **Si la extracción fuera el motor del desbalance, el K sería el elemento más BAJO del análisis.
> Es el más ALTO. Por lo tanto el aporte supera a la extracción por un margen enorme.**

Segunda razón por la que pesa poco: **el sistema es casi cerrado.** Solo se exporta el tallo
cosechado; follaje, raíz, descarte y limpieza basal vuelven vía la pila de composta.

**Donde sí hay extracción neta relevante: el calcio** (inmóvil, no se retransloca, sale entero
en el tallo; statice con 8 tallos/planta durante 20 semanas es un sumidero real). Pero con Ca
soluble ALTO, vuelve a ser problema de entrega, no de reserva.

**La ironía útil:** statice y limonium son hoy **lo único que saca potasio del sistema.** Son
herramienta de remediación. Un argumento más para no reducirlos.

## La prueba que está en casa: Inv 4

| | Inv 4 | Bloque 3 |
|---|---|---|
| Bokashi que recibe | **1–1.5 sacos** (el que MENOS) | 2–4 sacos (el que MÁS) |
| M.O. resultante | **23.4%** (la más alta) | **18.6%** (la más baja) |
| Presión de agua | **Alta y uniforme** | Insuficiente y desigual |
| Desempeño | **El mejor del cultivo** | El más problemático |

**El bloque que recibe menos Bokashi tiene más materia orgánica y produce mejor.** Demuestra dos
cosas: (1) la M.O. de Inv 4 no viene del Bokashi, viene del suelo más el No-Dig — argumento a
favor de recortar dosis ahí; (2) **la variable que separa a Inv 4 de Bloque 3 no es la nutrición,
es la uniformidad del agua** — que es justo lo que el repo declara como *"la lección
transferible más importante de toda la finca"*.

## Caveat sobre los datos: las tres muestras son compuestas

Promedian. Pero está documentado que dentro de un mismo bloque hay resultados opuestos: 3A
superiores vs inferiores, el gradiente de erosión en la "barriga" de 3B, la cama de 3C pegada al
humedal. Con riego desigual hay zonas que reciben tres veces más fertirriego que otras.

**Es posible que existan puntos con K al 40% de saturación y otros al 15%, promediados en 25%
sin mostrar ninguno de los dos.** No invalida la dirección del diagnóstico, pero el próximo
muestreo debería separar zona buena de zona mala dentro del mismo bloque.

---

# Propuesta de manejo

## Principio rector

> **Dejar de alimentar el suelo y empezar a alimentar el desbalance.** El suelo tiene reservas
> para años en K, Mg, S, P-total y M.O. Lo que falta es (a) el balance catiónico, (b) los
> cofactores de defensa, (c) el motor biológico que libere lo que ya está guardado.

## Capa 1 — Bokashi: la dosis está bien, el protocolo está mal escrito

**Hallazgo #1 — el protocolo está en sacos por cama, y las camas van de 6.3 a 48.1 m².**
Ver la tabla de conversión a kg/m² en `01-infraestructura/03-no-dig-y-preparacion-camas.md`.
La cama pequeña de 3B recibe **6.41 kg/m² contra 1.56 de la cama grande del mismo bloque** — no
es una decisión, es un artefacto de cómo está escrita la tabla.

**Hallazgo #2 — el Bokashi es una fuente de potasio no contabilizada.** La receta de
`02-bioinsumos.md` tiene **cuatro fuentes de K**: equinaza 800 kg (el estiércol equino es rico
en K), ceniza de madera 40 kg (*potash*, la más concentrada), melaza 60 kg (rica en K), king
grass 160 kg (las gramíneas son acumuladoras de K). Aplicado a 1.0–2.1 kg/m², 2–3 veces al año.

> **El Polyfeed no es la única fuente del exceso de K. El Bokashi probablemente es la más
> grande, porque el volumen es mucho mayor. Sacar Polyfeed y Bitter Mag del tanque es necesario
> pero NO suficiente si el Bokashi sigue con la misma receta.**

*Nota justa: la ceniza también aporta Ca en proporción mayor al K en peso, así que no es la
villana clara — son la equinaza, la melaza y el king grass. No se puede cuantificar sin análisis.*

**Hallazgo #3 — el objetivo de M.O. está cumplido.** M.O. de 18.6% a 23.4% con No-Dig y Bokashi
encima, en un suelo cuya alófana la protege de descomponerse, y con noches de 11 °C que frenan
la mineralización. **No se está sustrayendo: se está acumulando.** El Bokashi dejó de ser
constructor de M.O. y hoy es principalmente aporte de nutrientes y biología.

**Lo que sí está bien y no hay que tocar:** la lógica inversa del protocolo. Bloque 3 (M.O. más
baja, suelo erosionado) recibe más; Bloque 4 (M.O. más alta) recibe menos. Eso está correcto.

**Orden de magnitud del ahorro** (supuestos: ~2.500 m² tratados, 2.5 aplicaciones/año, promedio
1.35 kg/m², $14.700/saco): **~340 sacos/año ≈ 5.6 tandas ≈ ~$5.0M COP/año.** Reescribir en kg/m²
y bajar Inv 4 a ~1.0 kg/m² plausiblemente ahorra **$1.5–2.5M COP/año y baja el K al mismo
tiempo.** Para cerrar el número falta el conteo real de camas que reciben Bokashi.

## Capa 2 — Composta aeróbica: el activo sin explotar, y un riesgo

**El riesgo, primero.** Hoy se ponen *"todos los restos del cultivo"* en una pila fría. Esos
restos cargan **Fusarium, Botrytis y mosca blanca** — 29 registros lo documentan. **Una pila
fría no mata nada de eso.** Si esa composta vuelve a las camas, se reinocula el patógeno que se
lleva dos años combatiendo, y ya hay inóculo confirmado en suelo de 3C, Inv 5 e Inv 4.

**Solo el compostaje térmico aeróbico lo resuelve: 55–65 °C sostenidos al menos 3 días**, con
volteos que lleven todo el material al centro caliente. Por encima de 70 °C se mata también la
biología que se quiere. **No negociable si los restos de cultivo vuelven al campo.**

**El activo.** Bokashi y compost aeróbico no compiten — hacen trabajos distintos:

| | **Bokashi** (existe) | **Compost aeróbico** (falta) |
|---|---|---|
| Proceso | Fermentación, bajo oxígeno | Térmico, aeróbico, con volteo |
| Perfil biológico | Bacteriano | **Fúngico + protozoos + nematodos** |
| Función | **Alimenta** | **INOCULA** |
| Patógenos del residuo | No los mata | **Los mata a 55–65 °C** |
| Carga de K | Alta | Mucho menor sin ceniza ni melaza |
| Marco | Restrepo | **Ingham** |

**Y esto cierra el círculo con el P soluble bajo:** el compost aeróbico es lo que trae
**protozoos y nematodos bacterívoros**, que liberan N y P en la rizosfera al depredar bacterias.
Ese es el motor que falta. El Bokashi no lo trae — la fermentación anaeróbica no cría protozoos.

Además es la materia prima del **extracto de compost**, que puede empezar a reemplazar
Fitoderma, Estabios, Promobac y Pokonia comprados — lo que `02-bioinsumos.md` ya señala como
*"la palanca de reducción de costos más clara"*.

**Recomendación: no sustituir, sumar.** Bokashi al preparar cama (dosis por m², receta revisada
para bajar K). Compost aeróbico como programa nuevo y separado, alimentado con los propios
restos, para inocular y para hacer extracto.

## Capa 3 — Edáfico: la vía es correcta, la composición no

**El miedo a la salinidad no aplica hoy.** C.E. en 0.280 / 0.260 / 0.202, todas marcadas B.
Inv 3 venía de 0.829 en 2025 — ahí sí había salinidad activa, y es la que la bitácora culpa por
el lisianthus de tallo corto y delgado. **Hoy está en un tercio de eso**, y con M.O. 18–23% y
sat. humedad 133–155% la capacidad de amortiguación es altísima.

**Por qué el edáfico es MEJOR que el fertirriego en esta finca:**

> **Con riego desigual, el fertirriego es el peor método de entrega, porque la entrega de
> nutriente es proporcional a la entrega de agua.** En Inv 5 (*"la peor presión del sistema"*) y
> en 3B (*"presión insuficiente"*) las plantas reciben menos agua **y** menos fertilizante — el
> déficit se multiplica. **El fertirriego está amplificando la desigualdad del riego.**

El repo ya tenía la intuición correcta: *"la utilidad principal [de los Cotes] es compensar riego
irregular."* La decisión de usar edáfico fue buena. **Lo que hay que cambiar es qué se pone.**

| Nutriente | ¿Edáfico? | Por qué |
|---|---|---|
| **Cu** | ✅ **la mejor vía** | Dosis bajas, cero riesgo de salinidad, corrige la reserva. **Prioridad Bloque 5** |
| **B** | ✅ dosis baja | Margen estrecho entre deficiencia y toxicidad |
| **N** | ✅ liberación lenta | **Con riego irregular es lo correcto** — evita picos de nitrato |
| **P** | ✅ **solo Bloque 4** | Único con P total bajo (10.74 B) |
| **Ca** | ❌ **no sirve edáfico** | Ca soluble ya ALTO. **No falta en el suelo — no llega al tejido** |
| **K** | 🔴 **CERO** | Saturación 24–30% |
| **Mg** | 🔴 **CERO** | Saturación 32–38% |
| **S** | 🔴 **CERO** | Ya alto. Ojo: "sulfato de X" trae S escondido |

**Veredicto sobre Cote NPK:** el problema nunca fue que sea edáfico ni de liberación lenta.
**Fue la K.** Mantener la vía, cambiar la fórmula a un recubierto de N o N-Ca **sin K**.

**Regla que convierte el miedo en número:** pedir **C.E. trimestral**. Línea base 0.20–0.28. Si
un bloque pasa de ~0.6, frenar el edáfico ahí. Marca histórica de "esto ya duele" = 0.829.

## Capa 4 — Fertirriego: aquí está el error grande

`PENDIENTE DE VALIDACIÓN — no aplicado a 01-fertirriego-formulas.md`

| Producto | Propuesta | Razón |
|---|---|---|
| **Polyfeed 10-10-43** | **ELIMINAR de todas las fórmulas** | 43% K₂O sobre saturación de K de 24–30% |
| **Bitter Mag 16MgO** | **ELIMINAR** | Saturación Mg 32–38%. **Resuelve además el pendiente del azufre**: con Mg saturado no se repone Mg en ninguna forma, así que la pregunta de "qué fuente de Mg sin sulfato" se vuelve irrelevante |

Eso deja el tanque en: **N-Cal GG + Haifa Micro + Fullfert.** Más simple, más barato, alineado
con lo que el suelo pide.

| Necesidad | Qué entra | Diferenciación por bloque |
|---|---|---|
| **Cu** | **NO por el tanque — vía edáfica.** El Haifa Micro tiene Cu 0,2%: 80 tanques y $577.489 para corregir B5. Sulfato de cobre: 113 g y $1.126 | **Solo B5** (2.9 B). B3 y B4 ya respondieron |
| **Micro completo** | **Candidato a eliminar.** 81% de su carga es Fe, Mn y Zn (adecuados o altos en suelo) y el Fe viene en EDDHA, quelato para pH 7–9 que no aplica a pH 5,7. Reemplazar por **B + Cu + Mo separados** | Igual en los tres |
| **P disponible** | **Biológico primero.** Fuente mineral solo en B4 | **B4 (10.74 B) es el único candidato** |
| **Ca** | Mantener N-Cal, pero **la entrega es foliar y ambiental** | Prioridad 3C, Inv 1, 4B |
| **N** | **Bajar el total y cambiar la forma** — menos nitrato, más aminoácidos | B3 primero (N-NO₃ 64.4 A) |

**Sobre el N:** bajar el N-Cal es riesgoso porque es la única fuente de Ca del tanque. La salida
de Kempf no es bajar el N sino **cambiar de nitrato a formas que la planta no tenga que
reducir** — aminoácidos y N orgánico. Ya hay Naturamin y Starzyme en bodega. Ataca
simultáneamente mosca blanca (Fase 1), fusarium y costo.

## Capa 5 — Foliar: cambio de lógica, no de productos

`PENDIENTE — requiere aplicaciones_historial.csv actualizado (Regla APLICACIONES)`

Los productos son buenos. **El programa es reactivo en vez de constructivo.**

| Fase del cultivo | Objetivo | Componente que no puede faltar |
|---|---|---|
| Trasplante → sem 4 | Fase 1: enraizar sin nitrato en savia | Biológico + aminoácidos. **Sin N mineral foliar** |
| Sem 4 → prefloración | Fase 2: fotosíntesis completa | Mn, Mg, Fe |
| **Prefloración → inicio cosecha** | **Fase 3: lípidos = inmunidad a botrytis** | **Cu + B + Zn + P foliar** |
| Cosecha activa | Fase 4 + entrega de Ca | Ca foliar + silicio |

> **La regla actual de Statice dispara Botrycid+Equifun en semana 14–15 de cosecha. Bajo Kempf
> eso es tarde: es tratamiento, no inmunidad. La botrytis de la semana 16 se decide en la
> prefloración, seis a ocho semanas antes**, y se juega con Cu, B y P foliar. La regla de
> sem 14–15 **se degrada de estrategia a red de seguridad**, no se elimina.

Detalle relacionado: si se construye Fase 3, se deja de necesitar Botrycid semanal — lo que
resuelve solo el hallazgo ya registrado de que un producto con intervalo de etiqueta de 12
semanas aplicado cada semana es **sobreuso, no resistencia**.

## Capa 6 — Rotación de cama bajo los ciclos reales

| Grupo | Ciclo + ventana | Lectura Kempf/Ingham |
|---|---|---|
| **Statice / Limonium** | 13–15 sem + ventana 4–8 | **El mayor extractor de K.** Perversamente, la mejor herramienta de remediación. **Mantener** |
| **Lisianthus** | 19–23 sem, raíz 25 cm | El más largo, caro y enfermo. No-Dig marcado "NO por ahora" — correcto |
| **Gomphrena** | 13–15 sem, raíz 10–12 cm | **Candidata perfecta a No-Dig** y biosupresora. Cultivo puente ideal |
| **Matricaria / Marigold** | 12–13 sem | Biosupresores confirmados. Marigold libera tiofenos |
| **Bocas de dragón** | 9–12 sem, ventana crítica 2 sem | Alta demanda de Ca y B. Donde antes se verá el efecto de corregir el balance |

**Regla propuesta:** toda cama que sale de un ciclo largo (lisianthus, statice) pasa por un
**ciclo corto biosupresor** (gomphrena, matricaria, marigold) antes de volver a un exigente.
Esto ya existe como excepción escrita para las camas de Statice Forever Happy (*"ciclo
biosupresor primero"*) — la propuesta es **convertirla en la regla por defecto.**

---

# Cómo se mide — sin esto todo lo anterior es fe

| Indicador | Estado hoy | Acción |
|---|---|---|
| **Análisis de savia** | No existe | La herramienta central de Kempf. Preguntar a Natural Control |
| **Longitud y grado de tallo** | `07-datos/calidad_tallo.csv` **VACÍO** | Sin esto no se puede probar que nada de esto mejoró algo. Es gratis |
| **F:B, protozoos, nematodos** | No existe | Ingham completo. Preguntar a Bioquirama |
| **N-NH₄** | Vino vacío en los 3 informes | Pedirlo |
| **Análisis del Bokashi** | No existe | **Es la fuente de K no contabilizada** |
| **Litros de tanque por m² por bloque** | No existe | **Dato pendiente #1** — cierra el argumento del Cu en B5 y cuantifica el aporte de K |
| **Conteo de camas con Bokashi** | Parcial (3B está en huecos, no camas) | Cierra el cálculo de ahorro |

# Orden de ejecución propuesto

1. **Fertirriego — primero.** Es el error que corre cada tanque, y **se acabaron los productos**:
   no hay mejor momento para cambiar una fórmula que cuando hay que recomprar de todos modos.
2. **Reescribir dosis de Bokashi en kg/m² — próxima salida de cama.** Cero costo.
3. **En paralelo, los análisis baratos:** Bokashi, N-NH₄, y preguntar por savia y por el panel
   biológico completo.
4. **Composta térmica** — barato, retorno lento, resuelve P soluble y el riesgo de reinoculación.
5. **Foliar — al final.** Requiere el historial actualizado, y **si se cambia el foliar antes que
   el fertirriego no se va a poder saber qué funcionó.**

# Magnitud del cambio por categoría

| Categoría | Magnitud |
|---|---|
| Bokashi | **AJUSTE** — reescribir en kg/m², analizar el abono, bajar K de la receta |
| Composta | **CONSTRUIR NUEVO** — barato |
| Edáfico | **CAMBIO DE COMPOSICIÓN** — sacar K, mantener la vía |
| **Fertirriego** | **🔴 TRANSFORMACIÓN** |
| Foliar | **CAMBIO DE LÓGICA, no de productos** |

# Efecto cruzado no contabilizado: la bomba de ~6M COP

La inversión para resolver presión de agua no es solo productividad. También:
- Corrige la **entrega desigual de cobre** en Inv 5
- Permite **entregar Ca al tejido** (transpiración)
- Habilita eventualmente una **fracción de lavado** para bajar el K

**Es la inversión con más efectos cruzados sobre la mesa, y ninguno de esos tres beneficios está
contabilizado hoy en su justificación.**
