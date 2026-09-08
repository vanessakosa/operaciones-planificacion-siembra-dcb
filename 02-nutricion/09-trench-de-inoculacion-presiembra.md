# Trench de inoculación pre-siembra · una hoja por cama

> **Cierra el paso 7 de la preparación de camas v8** — *"drench de inoculación al sembrar"* —
> que quedó nombrado y sin dosis en `01-infraestructura/06-formulacion-camas-v8.md`, y que la
> hoja de operario v9 remite a *"el drench que entrega Vanessa aparte"*.
>
> **Hoja de operario:** `05-programacion/hojas-operario/trench-inoculacion-camas.html`
> **PDF:** `pdf/DCB-Trench-Inoculacion-Camas.pdf` · 2 páginas
>
> Sesión 2026-09-08. **La dosis y el alcance del Fitoderma piden confirmación de Vanessa**
> — ver *Decisiones abiertas* al final.

## Qué es el trench, y qué no es

El repositorio usa "trench" y "drench" como sinónimos, y eso ha estado escondiendo que son
**dos ventanas distintas con lógicas opuestas**:

| | **Trench pre-siembra** *(este documento)* | Drench de tanque |
|---|---|---|
| Cuándo | Al armar la cama, antes de sembrar | Cada 3–4 semanas, en cultivo |
| Granularidad | **Una cama** | Un invernadero completo |
| Se puede diferenciar por variedad | **Sí** | No — el bloque va en cohorte |
| Vía | Caneca + regadera, sobre la cama abierta | Cinta de goteo |
| Veces por ciclo | **Una** | 4 a 6 |

`06-consolidacion-formulas-e-inoculacion.md` ya lo había identificado: *"es el único momento en
que se puede aplicar cama por cama, a la dosis que se quiera, sin depender del bloque."*

> **Por eso la pregunta "¿priorizamos por bloque o por variedad?" no tiene que resolverse:
> en el trench pre-siembra se sabe el bloque Y la variedad al mismo tiempo.** No compiten.
> Lo que hay que decidir es **qué decide cada uno.**

## La arquitectura: tres preguntas, tres fuentes

| Pregunta del operario | La contesta | Por qué esa y no otra |
|---|---|---|
| **¿Cuánto?** | **Los m² de la cama** | La carga biológica se mide por área, no por cama. Es el mismo error que tenía el Bokashi en sacos |
| **¿Qué lleva además?** | **El inóculo confirmado del bloque** | El bloque es lo que fija qué patógeno vive en ese suelo |
| **¿Qué tan profundo se tapa?** | **La raíz de la variedad** | Es lo único de la variedad que cambia la geometría del trench |

Tres preguntas, tres columnas de una tabla, cero decisiones para el operario.

## El filtro que reduce 78 variedades a dos reglas

La tentación es armar una matriz variedad × producto. **No hace falta, y la razón está en los
datos:** de las 29 incidencias de `07-datos/incidencia_fitosanitaria.csv`,

| Dónde vive el problema | Incidencias | ¿El trench puede hacer algo? |
|---|---|---|
| **En el suelo** — Fusarium (13) · mosca blanca (6) | **19** | **Sí** |
| **En el aire** — Botrytis (6) · mildeo (2) · oidio (1) | **9** | **Nunca** |
| Mixta — Fusarium+Botrytis+Oidio | 1 | Solo la parte de suelo |

> **Regla: el reto de una variedad entra al trench solo si el patógeno vive en el suelo.
> Si vive en el aire, el trench no lo toca — y meterle producto es plata botada.**

Esto es lo que hay que decir en voz alta, porque es contraintuitivo: **el Statice es la variedad
con más incidencias después del lisianthus, y no lleva nada especial en el trench.** Su problema
es Botrytis, que llega por el aire a la semana 14–15 de cosecha. Su manejo es foliar —
Botrycid + Equifun, ya está en `04-variedades/02-notas-campo.md` — y ninguna cantidad de
inoculante en el suelo lo adelanta.

Aplicado el filtro, quedan **dos reglas de variedad**, no setenta y ocho:

| Variedad | Patógeno de suelo | Qué cambia en el trench |
|---|---|---|
| **Lisianthus** | Fusarium — **11 de los 13 registros son suyos**, 10 de ellos mortalidad en campo | Lleva **Fitoderma en cualquier bloque**, y se tapa a **20–25 cm** |
| **Matricaria Vegmo Single** | Mosca blanca — inóculo confirmado en suelo de 3C e Inv 5 | Nunca en 3C ni Inv 5. En otro bloque, **drench previo de Beauveria/Paecilomyces** |

Dianthus Green Ball tiene un registro de Fusarium grave en 3C, pero 3C ya lleva Fitoderma por
bloque: no necesita regla propia. Esa es la señal de que la arquitectura está bien repartida —
**la variedad solo agrega regla cuando el bloque no la cubre.**

## La profundidad — la única variable genuinamente de variedad

La tabla de profundidad de raíz de `01-infraestructura/03-no-dig-y-preparacion-camas.md` cruzada
con la banda donde ya van el Bokashi y la leonardita (10–15 cm):

| Variedad | Raíz | ¿La banda de 10–15 cm le sirve? |
|---|---|---|
| Gomphrena | 10–12 cm | Sí |
| Campanula · Ammi · Amaranto · Celosia | 15 cm | Sí |
| Snapdragon · Statice | 20 cm | Sí — la raíz baja al perfil aflojado |
| **Lisianthus** | **25 cm** | **No — es la única que se sale de la banda** |

> **De toda la tabla de raíces del repositorio, una sola variedad exige otra profundidad.**
> Por eso la hoja de operario tiene dos niveles y no siete: **10–15 cm en todo, 20–25 cm en
> lisianthus.** Las variedades sin profundidad de raíz documentada van al nivel estándar — no se
> les inventa un número.

Y no es casualidad que sea el lisianthus: es la raíz más profunda, el ciclo más largo
(19–23 semanas + 4–6 de ventana) y el dueño de 11 de los 13 registros de Fusarium. **Es la única
variedad donde el trench tiene que trabajar más hondo y por más tiempo.**

## La dosis — de dónde sale cada número

**No se inventó ninguna.** Se tomó lo que ya se aplica en `03-drench-inoculacion.md` (500 cc de
Estabios y 500 cc de Promobac por tanque de 2.000 L) y se convirtió a por m² con las áreas de
bloque:

| Bloque | Área | **cc/m² que se aplican hoy** |
|---|---|---|
| Inv 3 | 1.024 m² | **0,49** |
| Inv 4 | 677 m² | 0,74 |
| Inv 5 | 412 m² | 1,21 |
| Inv 2 | ~200 m² | **2,50** |

> 🔴 **El mismo artefacto del Bokashi, otra vez.** La dosis dice "500 cc por tanque" y suena
> uniforme, pero **Inv 2 recibe 5,1 veces más inoculante por m² que Inv 3** — y es Inv 3 el que
> tiene el Fusarium activo y el P soluble en 0,036, el peor de la finca. **No es una decisión
> agronómica: es la consecuencia de expresar la dosis por tanque en vez de por m².**

**La mediana de esos cuatro valores es 0,98 cc/m². Se adopta 1 cc/m².** Y con 1 L/m² de agua
—la cama ya viene regada con agua sola, así que el agua es vehículo, no humectación— la
concentración en la caneca queda en **1 cc/L**.

> **Ese número cierra un pendiente abierto.** `07-programa-biologico.md` anotó que la etiqueta
> del Estabios pide **1,0–2,0 cc/L** y que *"lo que se aplica hoy es 0,25 cc/L → 4 a 8× por
> debajo"*. A 1 cc/m² con 1 L/m², **el trench es la primera aplicación de Estabios a dosis de
> etiqueta**, y llega en el límite inferior del rango. La masa por área sale de la práctica
> propia; la concentración sale de la ficha. **Las dos rutas coinciden.**

**Fitoderma: 0,5 g/m²** — es exactamente la tasa que ya recibe Inv 3 (500 g / 1.024 m² = 0,49).
Sin cambio, solo expresada en la unidad correcta.

### Dónde va el Fitoderma, y por qué no es "solo Inv 3"

La regla vigente es *"Fitoderma solo en Inv 3, porque en Inv 4+5 el Trichoderma ya está alto
(1,4×10⁶)"*. Se mantiene Bloque 3 y se le suma el **Mini** —11 de los 13 registros de Fusarium
están marcados textualmente *"Mini + 3C + 3B"*— y **cualquier cama que vaya a lisianthus, en cualquier
bloque.** Lo que no se cambió, y hay que mirarlo: ver *Decisiones abiertas* #2.

Inv 5 y exterior **no llevan Fitoderma**: no tienen un solo registro de Fusarium.

## Cantidad y costo por cama

Precios de `07-programa-biologico.md`: Estabios y Promobac $59.000/L · Fitoderma $120.922/kg.

| Cama | m² | Agua | Estabios | Promobac | Fitoderma | **$/cama** |
|---|---|---|---|---|---|---|
| Inv 3A | 35,6 | 36 L | 36 cc | 36 cc | 18 g | **$6.353** |
| Inv 3B larga | 48,1 | 48 L | 48 cc | 48 cc | 24 g | **$8.584** |
| Inv 3B corta | 11,7 | 12 L | 12 cc | 12 cc | 6 g | **$2.088** |
| Inv 3C larga | 25,2 | 25 L | 25 cc | 25 cc | 13 g | **$4.497** |
| Inv 3C corta | 12,6 | 13 L | 13 cc | 13 cc | 6 g | **$2.249** |
| Mini larga | 12,6 | 13 L | 13 cc | 13 cc | 6 g | **$2.249** |
| Mini corta | 6,3 | 6 L | 6 cc | 6 cc | 3 g | **$1.124** |
| Inv 4A · 4B | 20,2 | 20 L | 20 cc | 20 cc | 10 g *solo lisianthus* | **$2.384** |
| Inv 4C larga | 40,5 | 40 L | 40 cc | 40 cc | 20 g *solo lisianthus* | **$4.779** |
| Inv 4C media | 38,2 | 38 L | 38 cc | 38 cc | 19 g *solo lisianthus* | **$4.508** |
| Inv 4C corta | 36,0 | 36 L | 36 cc | 36 cc | 18 g *solo lisianthus* | **$4.248** |
| Inv 5 | 31,7 | 32 L | 32 cc | 32 cc | — | **$3.741** |
| Ext 3A | 32,6 | 33 L | 33 cc | 33 cc | — | **$3.847** |
| Ext 3B larga | 48,1 | 48 L | 48 cc | 48 cc | — | **$5.676** |
| Ext 3B corta | 11,7 | 12 L | 12 cc | 12 cc | — | **$1.381** |
| Ext 4 | 40,3 | 40 L | 40 cc | 40 cc | — | **$4.755** |
| Ext 5 | 31,7 | 32 L | 32 cc | 32 cc | — | **$3.741** |
| Inv 6 | 31,7 | 32 L | 32 cc | 32 cc | — | **$3.741** |

| | |
|---|---|
| Costo base, todas las camas | **$118/m²** |
| Con Fitoderma (Bloque 3, Mini, cama de lisianthus) | **$178/m²** |
| Preparación de cama v8, para comparar | $640–782/m² |
| **Lo que el trench agrega a preparar una cama** | **+18 % a +23 %** |
| Vuelta completa · 100 camas · 2.756 m² | **$391.297** |

## 🔴 Lo que el trench hace visible: la plata está en la otra ventana

| | Veces al año | $/vez | **$/año** |
|---|---|---|---|
| **Trench pre-siembra** (2–3 vueltas de cama) | 2–3 | $391.297 | **$783.000 – 1.174.000** |
| **Drench de tanque cada 3–4 semanas**, si se corre como está escrito | ~15 | $237.461 | **~$3.560.000** |

> **El drench recurrente cuesta 3 a 4,5 veces más que el trench, y es el que no se puede
> diferenciar por cama.** `06-consolidacion-formulas-e-inoculacion.md` ya propuso colapsarlo a
> **una sola pasada de prefloración** más manejo foliar. Si eso se hace, la inoculación completa
> de la finca baja de ~$3,8M a ~$1,2M al año **aplicando más producto por m², no menos.**
>
> ⚠️ El $3,56M es **condicional**: `07-datos/aplicaciones_historial.csv` **no tiene un solo
> registro de drench** —solo foliares, y solo hasta la semana 27— así que la frecuencia real de
> 3–4 semanas no se puede auditar. Es la primera cosa que hay que medir.

## Lo que NO entra al trench, y por qué

| Producto | Por qué no |
|---|---|
| **Pokonia** | A dosis de etiqueta (1 L/ha) una cama de 35,6 m² pide **3,6 cc**. No es pesable ni medible por cama: su vía correcta es el tanque. Y sigue en pie que **nunca se han contado nematodos** |
| **Micorrizas (Endhoriza)** | Ya decidido: solo camas nuevas sin historial. Y la ficha del Terra Life dejó el argumento de que las propágulas **no viajan bien en líquido** — si se quieren, van granuladas |
| **Sáfer Terra Life** | Salió del programa el 2026-09-03. Aporta 0,0009 % del Trichoderma que ya hay |
| **Fosfolip** | Va a entrar y **reemplaza al Estabios en la función de fósforo**, pero todavía no está en la finca. Cuando llegue, va al trench: es la ventana correcta para un solubilizador de P |
| **Botrycid · Equifun · Regalia** | Botrytis, oidio y mildeo **viven en el aire**. Son foliares, nunca trench |
| **Cualquier fertilizante químico** | La ficha del Fosforiz lo prohíbe junto a biológicos, y el instinto de *"Inv 3 — Haifa: NO esa semana"* era correcto. **Se extiende a todos los bloques:** el día del trench la cama va con agua sola |

## Decisiones abiertas — piden confirmación de Vanessa

**1. La dosis base en 1 cc/m² sube el gasto de Estabios y Promobac.**
Es la mediana de lo que ya se aplica, y es dosis de etiqueta. Pero contra la práctica de Inv 3
es **2× más**. La alternativa conservadora es arrancar en 0,75 cc/m². **Sin decidir.**

**2. El Fitoderma de Inv 4 — la razón para excluirlo no está medida.**
La regla dice *"en Inv 4+5 el Trichoderma ya está alto (1,4×10⁶)"*. Pero ese número es **un solo
dato de finca de Bioquirama (nov 2025), sin desglose por bloque** — `02-analisis-de-suelo.md`
entrega una cifra, no cinco. Y al mismo tiempo `incidencia_fitosanitaria.csv` registra
**inóculo de Fusarium confirmado en el suelo de Inv 4**, y `01-invernaderos.md` lo llama
*"alerta estructural: Fusarium generalizado en suelo"*.
**La exclusión de Inv 4 descansa en una atribución, no en una medición.**
Por eso la hoja lo dejó en *"solo si la cama va a lisianthus"* — la mitad prudente.
Extenderlo a todo Inv 4 cuesta **+339 g de Fitoderma por vuelta = $41.000**.
Lo que lo resolvería de verdad: **pedir el microbiológico por bloque, no por finca.**

**3. Falta la dosis del drench de Beauveria/Paecilomyces para Matricaria Vegmo.**
La obligación está escrita en el repositorio desde hace tiempo; **el número no está en ninguna
parte.** No se inventó. La hoja de operario dice *"no sembrarla sin la hoja aparte"*, que es una
prohibición ejecutable y no un cálculo pendiente. Hay Safer Mix (Beauveria, 500 g) y No Fly
(Paecilomyces, 600 g) en bodega. **Pedir la dosis de drench de suelo al proveedor.**

**4. 🔴 La hoja v9 manda aflojar 25–30 cm en TODA cama. Eso contradice el No-Dig.**
`03-no-dig-y-preparacion-camas.md` dice **No-Dig completo en Inv 4** y **horquilla 5 cm en Inv 5
y 3C**; `02-analisis-de-suelo.md` dice que *"el Trichoderma en 1,4×10⁶ se destruye con cada
volteo profundo"*. La v9 —que es la hoja en vigor— aflojar 25–30 cm en todas.
**Una de las dos está mal, y la que está en manos de Wilson es la v9.**
Importa para el trench porque decide dónde queda el inoculante, pero importa más por sí sola.

**5. El Promobac no alcanza.** Una vuelta completa pide **2.756 cc** y en bodega hay **1.000 cc**
(inventario de marzo, desactualizado). Estabios alcanza justo (3.000 cc). Fitoderma alcanza para
Bloque 3 + Mini (546 g de 600 g) y **no** si se extiende a Inv 4.

## Archivos que este documento deja desactualizados

| Archivo | Qué quedó viejo |
|---|---|
| `02-nutricion/03-drench-inoculacion.md` | Su tabla es la del drench de tanque. Cierra sus dos pendientes: **el trench es por caneca y por cama, no por inyector ni por tanque**, y **no reemplaza el volteo — va montado en la pasada de horquilla que ya se hace** |
| `01-infraestructura/03-no-dig-y-preparacion-camas.md` | Su tabla *"Stack de inoculación al preparar"* todavía dice **TerraLife SÍ siempre** y **Naturcomplet solo PREMIUM**; los dos salieron el 2026-09-03 |
