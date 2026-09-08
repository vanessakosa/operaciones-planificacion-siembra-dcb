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

> 🔴 **CORREGIDO 2026-09-08 por objeción de Vanessa.** La primera versión de este documento
> partía las incidencias en dos —"vive en el suelo" contra "vive en el aire"— y **esa partición
> era falsa.** Vanessa preguntó si las esporas de botrytis y de mildeo no se quedan en el suelo.
> Se quedan, pero **no en el suelo mineral: en el residuo de cosecha que queda sobre la cama.**
> Son tres categorías, no dos, y la del medio es la que estaba faltando — y es la que más
> incidencias explica después del Fusarium.

La tentación es armar una matriz variedad × producto. No hace falta, pero el filtro correcto no
es "suelo o aire": es **qué estructura sobrevive entre ciclos, y dónde.**

| Dónde sobrevive | Estructura | Incidencias | **Qué lo ataca de verdad** |
|---|---|---|---|
| **En el suelo mineral, por años** | Clamidosporas | **Fusarium · 14** | **El inoculante del trench.** La única categoría donde el trench es la herramienta correcta |
| **En el residuo de cosecha, sobre la cama** | Esclerocios · micelio · pupas | **Botrytis 7 · mosca blanca 6** | **Sacar el residuo.** El inoculante solo compite por lo que quede |
| **Solo en tejido vivo** | Conidios en yema · hospedante alterno | **Oidio 2 · mildeo polvoso** | Foliar y **maleza**. El suelo no juega |

*(14 y 7 incluyen la fila mixta Fusarium+Botrytis+Oidio de lisianthus en 3B, contada en las tres.)*

> **La consecuencia de la corrección:** el trench, tal como está diseñado, es la herramienta
> correcta para **14 de las 29 incidencias**. El paso que faltaba —sacar el residuo— cubre otras
> **13**. Es decir: **el paso que no estaba escrito valía casi tanto como todo lo que sí estaba.**
> Ya se agregó a la hoja de operario, en la fila *"Al cerrar la cama anterior"*.

Y no es una práctica nueva ni una idea de laboratorio: **la finca ya la ejecutó y la escribió.**
El registro del colapso de Limonium Forever Happy en Inv 4 dice textualmente
*"retirar plantas en colapso **en bolsa cerrada fuera del invernadero**, cerrar camas
gradualmente"* y *"NO sembrar lisianthus ni campanula en estas camas inmediatamente — ciclo
biosupresor primero (gomphrena o matricaria)"*. **Estaba enterrado en un comentario de
`campo_siembras.csv` y no estaba en ningún protocolo.**

### El Statice sigue sin llevar nada especial en el trench — pero por otra razón

La conclusión no cambia, el motivo sí. No es que su botrytis "viva en el aire": es que **su
esclerocio vive en el residuo, y contra el residuo la herramienta es la bolsa cerrada, no el
inoculante.** Lo que el trench sí puede hacer con el residuo que inevitablemente queda es
**colonizarlo antes que la botrytis** — y eso ya lo hacen el Fitoderma (Trichoderma + Bacillus) y
el Promobac (Bacillus) que están en la tabla. **No hay que agregar producto: hay que agregar el
paso de limpieza.** *(Competencia por residuo: microbiología general, jerarquía nivel 4.)*

### 🔴 Y hay que separar dos cosas que en español se llaman igual

| | Sobrevive en suelo o residuo | Qué se ve en la hoja |
|---|---|---|
| **Mildeo polvoso** (oidio, biótrofo obligado) | **No.** Necesita tejido vivo | Polvo blanco, **cara superior** |
| **Mildeo velloso** (*Peronospora*) | **Sí — oosporas, años** | Manchas arriba, **vello grisáceo en la cara inferior** |

Los dos registros de mildeo del repositorio —**Dahlia en Inv 2** y **rosas en Inv 1**— **no dicen
cuál de los dos es.** Y el inventario tiene Regalia y ADN Fun etiquetados *"mildeo polvoso"*, que
es producto para el biótrofo. **Si alguno de los dos casos es velloso, el producto está mal
elegido y el suelo sí entra en la cuenta.** Se resuelve mirando la cara inferior de la hoja:
es un dato de campo que cuesta un minuto. *(Biología de los dos patógenos: jerarquía nivel 4.)*

## 🔴 La mosca blanca no tiene etapa de suelo — y eso invalida un protocolo vigente

Vanessa lo planteó como duda y el registro le da la razón.

**La mosca blanca no pone huevos en el suelo.** Los pone en la cara inferior de la hoja, y tanto
*Bemisia tabaci* como *Trialeurodes vaporariorum* **empupan sobre la hoja, no en el suelo.**
No hay una fase que viva en el suelo mineral. *(Ciclo del insecto: jerarquía nivel 4.)*

Y al mirar de dónde salió la afirmación contraria:

| | |
|---|---|
| Las dos filas que dicen **`INOCULO_EN_SUELO`** (3C e Inv 5) | Su columna `fuente` es **`01-infraestructura/01-invernaderos.md`** — un markdown, jerarquía nivel 3 |
| Las **cuatro** filas de observación real de campo | Dicen *"les dio mosca blanca y no florecieron"*, *"sacrificada por mosca blanca"*. **Ninguna menciona el suelo** |

> **"Inóculo de mosca blanca en el suelo" es una inferencia del repositorio, no una observación de
> campo.** Y probablemente sea el mecanismo equivocado.

Lo que sí explica que se repitan **los mismos dos bloques** es más simple: la población nunca
salió del bloque. Sobrevive en la **maleza de dentro y del borde** y en las **pupas del residuo
de cosecha** que se dejó en la cama. Eso no es suelo: es residuo y hospedante alterno — la
categoría del medio del filtro de arriba.

**Consecuencia sobre el protocolo:** el *"drench pre-siembra obligatorio con Beauveria bassiana o
Paecilomyces"* de la Matricaria Vegmo **está aplicando el producto correcto en el lugar
equivocado.** Se sacrificaron dos lotes con ese protocolo escrito. Si el reservorio es la
población en pie y el residuo, las palancas son:

1. **Sacar el residuo del ciclo anterior** en bolsa cerrada — ya está en la hoja de operario
2. **Desyerbe del bloque y de sus bordes** antes de sembrar
3. **Beauveria/Paecilomyces FOLIAR** sobre la siembra nueva — y esa dosis **sí existe**:
   No Fly a **10 g / 25 L**, en `07-datos/aplicaciones_historial.csv`

Y la forma correcta ya está escrita para la variedad hermana: la Matricaria **Snowball** tiene
*"protocolo preventivo mosca blanca sem 6–8 y 10"* en `04-variedades/02-notas-campo.md`.
**Ese es el molde. El drench de suelo de la Vegmo es la excepción sin fundamento.**

## 🔴 El hueco del plástico — la observación más fuerte, y es un riesgo nuevo

Vanessa: *"tienes plástico encima, pero el plástico tiene el hueco donde va la planta."*

El hueco es **el único punto de la cama donde el suelo queda expuesto**, y es el punto de mayor
humedad. Tres cosas convergen exactamente ahí:

1. Es la **única vía** por la que el inóculo del suelo alcanza la planta.
2. Es la **única vía** por la que el residuo infectado llega al suelo — y el plástico, al ser
   liso e impermeable, **conduce hacia el hueco** el pétalo caído y la limpieza basal.
3. El plástico **retiene calor nocturno y humedad** — documentado en `01-invernaderos.md` como
   beneficioso porque las noches bajan a 11 °C.

**Cálido + húmedo + residuo acumulado en el cuello de la planta son las condiciones exactas de la
pudrición de cuello.**

Y el registro ya tiene la firma de esa falla: el colapso de Limonium Forever Happy dice
**"pudrición de cuello activa en varias plantas"** y **"necrosis basal severa en camas más
antiguas"**.

> **Ojo con la conclusión:** ese caso fue en **Inv 4, que no tiene plástico.** El plástico no lo
> causó. Lo que significa es peor y más útil: **la pudrición de cuello ya es un modo de falla real
> de esta finca, y el plástico le está construyendo el microclima ideal** justo cuando se está
> expandiendo para eliminar el desyerbe.

### Lo bueno: el experimento ya está montado

`01-invernaderos.md` registra **Ext Inv4-5, 2 camas, comparativo plástico vs sin plástico en
curso**, y hoy mide *retención de humedad, tiempo de instalación y durabilidad*.

> **Agregarle una sola variable: contar plantas con pudrición de cuello y necrosis basal, por
> cama, al cierre del lote.** Costo cero, y es la única forma de saber si el ahorro de 2–3
> operarios de desyerbe se está pagando con enfermedad de cuello.

**Y sobre el trench:** en cama con plástico, **la ventana pre-siembra deja de ser la mejor y pasa
a ser la única.** Una vez puesto el plástico, cualquier corrección por suelo entra por el hueco o
no entra. Por eso la hoja de operario ahora dice explícitamente que **el plástico va después del
trench, nunca antes.**

⚠️ **Contradicción de paso, sin resolver:** `01-invernaderos.md` dice que las 7 camas de Inv 6
están *"todas con mulch plástico negro"*; la hoja de operario v9 dice **"Inv 6 NO tiene
plástico"**. Una de las dos está mal, y la que Wilson tiene en la mano es la v9.

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
| **Botrycid · Equifun · Regalia** | Son fungicidas de tejido, no de suelo: actúan sobre la hoja y la flor. Contra el esclerocio de botrytis que queda en la cama la palanca es **sacar el residuo**, y contra el que quede, el Trichoderma y el Bacillus que ya están en la tabla |
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

**3. El drench de suelo de la Matricaria Vegmo: la dosis no falta — el protocolo está mal.**
La primera versión de este documento pedía la dosis del drench pre-siembra de
Beauveria/Paecilomyces al proveedor. **Ya no hace falta pedirla:** la mosca blanca no tiene etapa
de suelo, así que el drench de suelo es el producto correcto en el lugar equivocado (ver arriba).
La propuesta es **reemplazarlo por residuo + desyerbe + foliar sem 6–8 y 10**, copiando el molde
que ya tiene la Matricaria Snowball, con la dosis de No Fly que ya está registrada (10 g / 25 L).
La hoja de operario sigue diciendo *"no sembrarla sin la hoja aparte"* hasta que decidas.
**Esto necesita tu confirmación: es cambiar un protocolo marcado como obligatorio.**

**3b. Mirar la cara inferior de la hoja en la Dahlia de Inv 2 y en las rosas de Inv 1**, para
saber si el mildeo es polvoso o velloso. Si es velloso, el suelo entra en la cuenta y el producto
está mal elegido. Cuesta un minuto de campo.

**3c. Agregar el conteo de pudrición de cuello al comparativo de plástico de Ext Inv4-5.**
Costo cero, y es lo que dice si el plástico se está pagando con enfermedad de cuello.

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
