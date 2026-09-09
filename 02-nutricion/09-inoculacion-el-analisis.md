# La inoculación · el análisis de las cuatro fichas

> **Fecha:** 2026-09-09. Vanessa entregó en una sola sesión las cuatro fichas que
> faltaban del tanque de inoculación: **Promobac**, **Fitoderma**, **Raizal 400** y
> **Fullfert**. Los cuatro renglones nunca habían pasado por el filtro de *UFC por
> organismo y dosis de etiqueta* — el mismo filtro que sacó el Estabios y el Terra Life.
> Este documento es lo que aparece al aplicarlo.

## El resumen en una línea

**El programa de inoculación está sobredosificado entre 5× y 12× contra etiqueta, y
está apuntado al lugar equivocado.** Corregir solo la dosis, sin tocar el calendario,
ahorra **$3,08 M/año**. Corregir además el momento lo lleva a **$3,57 M/año**.

---

## 1. Lo que dice cada ficha

| Producto | Composición garantizada | Dosis de etiqueta | Lo que se aplica hoy |
|---|---|---|---|
| **Promobac** | 4 *Bacillus* (subtilis, thuringiensis kurstaki, pumilus, amyloliquefaciens) a **1×10⁸ UFC/mL cada uno** | **1 L/ha** | 500 cc/tanque |
| **Fitoderma** | *Trichoderma harzianum* **1×10⁸ UFC/g** + *Bacillus subtilis* **1×10⁸ UFC/g** · C orgánico 38 % · N 4 % · CIC 52,6 meq/100 g | **500 g/ha** | 500 g/tanque (solo Inv 3) |
| **Raizal 400** | **9-45-11** + Mg 0,6 % + S 0,8 % + **complejo auxínico 400 ppm** · pH 2–3,5 al 10 % | **0,5–1 kg en 100 L**, 50–80 mL de esa solución **por planta al trasplante** | 300 g/tanque, cada 3–4 semanas, todo el ciclo |
| **Fullfert** | K₂O 40 g/L · S 9 g/L · **CEHT 150 g/L** (húmicos 90, fúlvicos 60) · pH 12 al 10 % | **4–15 L/ha** drench | 40–100 cc/tanque |

Dos cosas que las fichas cierran de una vez:

- **El Promobac declara UFC por organismo, no como consorcio.** Es la especificación que
  el repositorio venía exigiendo. Es lo contrario del Estabios (1×10⁸ *total* entre
  cuatro), y es lo que lo vuelve el biológico **más barato por unidad del organismo útil
  de todo el programa**.
- **El Fullfert por fin tiene su % de húmicos** — la pregunta abierta de $3.366 por tanque
  desde el 2026-09-02. Son **150 g/L de carbono húmico total**, o **$224.433 por kg de
  carbono húmico**. Con eso la comparación contra el Campofert Humus 15 ($26.165/L) ya se
  puede hacer sobre la base correcta, en cuanto llegue su ficha.

### Costo por unidad del organismo útil

| | $ por 10⁹ UFC |
|---|---|
| **Promobac** — los 4 organismos | **$148** |
| **Promobac** — solo los 3 útiles en drench | **$197** |
| Fosfolip (*Penicillium* 1×10⁸) | $521 |
| Estabios (1×10⁸ **total** entre 4) | $590 |

El *Bacillus thuringiensis* var. *kurstaki* del Promobac es **carga muerta en un drench al
suelo**: es específico de lepidópteros y actúa por ingestión en el intestino de la larva.
Es la cuarta parte de la carga declarada. Aun descontándolo, el Promobac gana por 2,6×
contra el segundo. **El producto pasa el filtro con holgura.**

---

## 2. La sobredosis: el mismo artefacto de siempre

Es el error de clase que ya se corrigió en el Bokashi (sacos fijos por cama), en el
Naturcomplet (300 g fijos) y en los cotes: **una dosis fija por tanque aplicada a bloques
de área muy distinta.**

| Bloque | m² | Promobac etiqueta | Se aplica | Sobre etiqueta | Fitoderma etiqueta | Se aplica |
|---|---|---|---|---|---|---|
| **Inv 3** | 1.025 | 103 cc | 500 cc | **4,9×** | 51 g | 500 g → **9,8×** |
| **Inv 4** | 680 | 68 cc | 500 cc | **7,3×** | 34 g | — |
| **Inv 5** | 412 | 41 cc | 500 cc | **12,1×** | 21 g | — |

Las áreas se derivaron de las dosis en L/ha del Fosfolip y **se verificaron contra el
conteo real de camas** de `capacidad_bloques.csv`: Inv 5 da 412 m² contra 410 asumidos;
Inv 4 da 680 contra 675. La regla de 0,18 m²/hueco vuelve a sostener el cálculo.

El **Fullfert es el único que va al revés: está subdosificado 4× a 19×.** Ese caso se
resuelve abajo, y no como uno esperaría.

---

## 3. 🔴 El hallazgo que cambia el programa: un drench no mueve una población establecida

El suelo de la finca mide **1,4×10⁶ UFC/g de *Trichoderma*** (Bioquirama, nov 2025). Puesto
en el volumen de suelo que el drench moja:

| Bloque | Suelo 0–10 cm | *Trichoderma* residente | Fitoderma 500 g aporta | Fitoderma a etiqueta |
|---|---|---|---|---|
| Inv 3 | 82,0 t | 1,15×10¹⁴ UFC | 5,0×10¹⁰ = **0,044 %** | **0,0045 %** |
| Inv 4 | 54,4 t | 7,62×10¹³ UFC | — | 0,0045 % |
| Inv 5 | 33,0 t | 4,62×10¹³ UFC | — | 0,0045 % |

*(densidad aparente de andisol 0,8 g/cm³)*

**El repositorio ya usó exactamente este argumento para descartar el Sáfer Terra Life**,
que aportaba 0,0009 % de lo que ya hay. El Fitoderma es 48 veces mejor que el Terra Life
— y sigue siendo 0,04 %. Nunca se le aplicó el filtro. Ahora sí.

### La objeción, y por qué no salva el argumento

Un agrónomo diría, con razón: el conteo de 1,4×10⁶ incluye esporas dormidas repartidas en
todo el volumen, mientras el drench entrega organismos **vivos, activos y en agua, a la
rizosfera**. No es comparable uno a uno.

Es cierto y no alcanza. Son **cuatro órdenes de magnitud**. Aun suponiendo un factor de
concentración de 100× en la rizosfera, el inóculo queda en 4 %. Y el agua del drench moja
la cama entera, no solo la rizosfera. **La conclusión sobrevive a su propia objeción.**

### Entonces, ¿de dónde salió el 127× de aumento?

El *Trichoderma* pasó de 1,1×10⁴ (ago 2024) a 1,4×10⁶ (nov 2025). Si el drench fuera el
responsable, tendría que explicar un factor de 127 aportando 0,04 % por aplicación —
0,6 % acumulado en un año de aplicaciones. **Aritméticamente no puede.**

Lo que sí puede: el **Bokashi** (1–2 kg/m², 2–3 veces al año — masa de alimento y hábitat,
órdenes de magnitud por encima), el **No-Dig** (dejar de destruirlo) y el mulch. Es
literalmente el punto de Ingham: **se inocula una vez y después se alimenta.** El 127 % es
evidencia a favor del Bokashi y del No-Dig, y evidencia de que el drench no fue el motor.

**Y es comprobable.** Si el drench fuera el motor, el conteo escalaría con las
aplicaciones. → **Pedirle a Bioquirama el *Trichoderma* por bloque.** La respuesta sostiene
o mata esta decisión.

### 🟡 El dato que falta y que debilita el caso en Inv 3

**El análisis microbiológico no registra de qué bloque se tomó.** El archivo de drench dice
*"en Inv 4+5 el Trichoderma ya está alto (1,4×10⁶)"*, lo que sugiere que la muestra no es
de Inv 3. Y toda la decisión de *Fitoderma solo en Inv 3* descansa en que Inv 3 sea
distinto — **que nunca se midió**. Es la primera pregunta de la lista.

Para el *Bacillus* del Promobac **no existe línea base**: Bioquirama entrega dos organismos
(*Trichoderma* y *Fusarium*). Así que el argumento de futilidad **no está disponible para el
Promobac**. Su dosis es una pregunta de etiqueta, no de futilidad. Esa asimetría es real y
hay que respetarla.

---

## 4. Raizal 400: la auxina que se paga y no llega

La ficha resuelve la contradicción que el protocolo cargaba desde el principio.

**Es un producto de trasplante, por etiqueta:** *"desarrollada primordialmente para
proveer de nutrientes y estimular el crecimiento de raíces de **plantas jóvenes**
provenientes de trasplantes o de siembra directa"*, *"preferentemente al momento del
trasplante o inmediatamente después"*, *"repetir 2 a 3 veces a intervalos de 2 semanas"*.
Hoy va en **todos** los tanques de mantenimiento, cada 3–4 semanas, indefinidamente.

**Y su dosis es por planta, no por área.** 300 g fijos por tanque no es ninguna de las dos.

Lo decisivo es la dilución. El diferencial del Raizal contra cualquier NPK soluble es su
complejo auxínico de 400 ppm:

| | g/L de producto | mg/L de auxina |
|---|---|---|
| Etiqueta 0,5 kg/100 L | 5,0 | **2,000** |
| Etiqueta 1 kg/100 L | 10,0 | **4,000** |
| **Tanque de hoy: 300 g/2.000 L** | 0,150 | **0,060** |

**El tanque entrega la auxina 33× a 67× más diluida que la etiqueta.** Lo único que
justifica el precio del Raizal llega en concentración irrelevante. Se está pagando una
hormona que no se aplica.

Y el fósforo va al lugar equivocado. 300 g entregan 135 g de P₂O₅ = 0,13–0,33 g/m² según
el bloque. En un andisol con **P soluble de 0,107 mg/L**, el alofano lo fija en días. Ese es
el argumento honesto: **no es que dañe — es que se desperdicia.** Y se desperdicia mientras
se paga por separado un solubilizador de fósforo (Fosfolip/Estabios) para desbloquear el P
que el suelo ya tiene fijado. **Pagar por meter P que se fija, y pagar por desfijar P, es
circular.**

**Veredicto: el Raizal sale del tanque de mantenimiento.** Al trasplante es defendible por
etiqueta, pero su fósforo es el nutriente equivocado para este suelo. Que se quede solo
donde haya un problema de enraizamiento documentado — **y no se compre más hasta saber qué
problema se compró a resolver.**

*Nota de compatibilidad:* pH 2–3,5 al 10 %. En el tanque va a 0,015 %, así que el efecto
sobre el pH del tanque es menor de lo que el número sugiere. Pero la ficha del Fullfert
prohíbe expresamente tanques con **pH menor a 4**, y la del Promobac dice *"no almacenar
junto con pesticidas químicos y fertilizantes"*. Meter un fertilizante 9-45-11 ácido en un
tanque de biológicos no tiene defensa en ninguna de las tres fichas.

---

## 5. Fullfert: está subdosificado y no importa

Este es el caso donde el resultado va contra la intuición y contra mi propia expectativa.

El Fullfert está **4× a 19× por debajo de etiqueta** (410–1.537 cc para Inv 3 contra los 80
que se aplican). El reflejo es subirlo. La ficha permite calcular qué pasaría si se sube:

| Fuente de carbono | g de C por m² |
|---|---|
| Fullfert a etiqueta baja (4 L/ha) | **0,060** |
| Fullfert a etiqueta alta (15 L/ha) | 0,225 |
| **Bokashi 1,5 kg/m² al 30 % C** | **450** |

**El Bokashi entrega 7.500 veces más carbono que el Fullfert a dosis de etiqueta.** La masa
del Fullfert es irrelevante en los dos sentidos: subirlo a etiqueta no alimenta a nadie que
el Bokashi no esté alimentando ya.

Su valor, si lo tiene, **no es como alimento sino como complejante** — competir con el
alofano por los sitios de sorción de fósforo y quelatar los micros. Eso es un efecto de
concentración en la solución del suelo, no de masa. **Y ese rol ya lo cumple en el tanque de
fertirriego**, donde vive con su renglón propio de $3.366 (11–17 % del tanque).

**Veredicto: el Fullfert sale del tanque de biológicos, y NO se sube a etiqueta.** La dosis
de etiqueta está pensada para fincas cuyo único aporte orgánico es el húmico líquido, no
para una que aplica 1–2 kg/m² de Bokashi dos o tres veces al año. Ahorra $2.693–3.366 por
tanque sin ninguna pérdida biológica.

---

## 6. La propuesta

### Qué sale y qué queda

| Producto | Decisión | Razón en una línea |
|---|---|---|
| **Promobac** | ✅ **Queda**, a etiqueta (1 L/ha) | El más barato por UFC útil del programa, y sin línea base de *Bacillus* que permita descartarlo |
| **Fitoderma** | ✅ **Queda en Inv 3**, a etiqueta (500 g/ha) | *Fusarium* activo documentado (3×10⁴ UFC/g). Pero su lugar es la raíz del plántula, no la cama |
| **Fosfolip** | ✅ Entra en lugar del Estabios | Ya decidido — ensayo partido en Inv 4 |
| **Estabios** | ⚠️ Ensayo partido | 1×10⁸ **total** entre 4 organismos: $590 por 10⁹ contra $148 |
| **Raizal 400** | 🔴 **Sale del mantenimiento** | Producto de trasplante por etiqueta · auxina 33–67× subdosificada · P que el alofano fija |
| **Fullfert** | 🔴 **Sale del tanque de biológicos** | Ya está en el de fertirriego, que es donde su rol de complejante tiene sentido |

### El cambio de momento: del calendario a la vuelta de cama

Hoy: **tanque por invernadero cada 3–4 semanas**, sobre suelo establecido — 15 aplicaciones
al año por bloque.

Propuesto: **una inoculación por vuelta de cama**, en el momento de la preparación, cuando
la cama está recién enmendada y la raíz nueva va a entrar. Es el paso 5 de la hoja de
preparación de camas. **Dos a cuatro veces al año por bloque**, según la rotación.

El argumento es el de la sección 3: un drench no cambia una población establecida, pero sí
puede llevar organismos **a donde la población residente todavía no llegó** — la cama recién
removida, la raíz cortada, el hueco de trasplante.

### Dosis ejecutable por bloque

| Bloque | m² | Fitoderma | Promobac | Fosfolip | Agua (~2 L/m²) |
|---|---|---|---|---|---|
| **Inv 3** | 1.025 | **50 g** | **100 cc** | **200 cc** | 2.000 L |
| **Inv 4** | 680 | — | **70 cc** | **140 cc** | 1.400 L |
| **Inv 5** | 412 | — | **40 cc** | **80 cc** | 800 L |

Redondeado hacia arriba desde etiqueta (51 / 34 / 21 g y 103 / 68 / 41 cc). Los 2 L/m² no
son un supuesto: es la práctica actual — 2.000 L para los 1.025 m² de Inv 3.

**Todas las cifras son medibles.** Ese fue el criterio de diseño, el mismo que obligó a
sacar los 2,4 g de cobre de la hoja de fertirriego: nada que un operario no pueda pesar o
medir sin error mayor al 10 %.

### El ahorro, separado por decisión

| | Por aplicación (3 bloques) | Al año |
|---|---|---|
| **HOY** — 15 aplicaciones/año | $245.877 | **$3.688.159** |
| Solo corregir la **dosis**, mismo calendario | $40.770 | $611.550 → **ahorro $3,08 M** |
| Corregir dosis **y** momento, a 3 vueltas/año | $40.770 | $122.310 → **ahorro $3,57 M** |

*(sin contar el Raizal: no hay precio en el repositorio. Sin contar Inv 2: no tiene área
medida.)*

**La separación importa.** El grueso del ahorro — $3,08 M — está en la dosis, y esa
corrección es de bajo riesgo: es simplemente aplicar la etiqueta del fabricante. El cambio
de calendario añade $0,49 M y descansa en el argumento de la sección 3, que es más fuerte
pero es mío, no del fabricante. **Se pueden tomar por separado.**

---

## 7. Lo que este análisis NO resuelve

1. **🔴 ¿De qué bloque es el análisis microbiológico?** Toda la restricción del Fitoderma a
   Inv 3 descansa en un dato que no está registrado. → Bioquirama / Vanessa.
2. **🔴 *Trichoderma* por bloque** — es la medición que sostiene o mata el cambio de
   calendario. → Bioquirama.
3. **🟡 La dosis de inmersión de raíz del Fitoderma.** Su ficha da 500 g/ha al suelo y
   menciona uso foliar, pero **no da tasa para plúgula o hueco de trasplante**. Es donde el
   1×10⁸ UFC/g realmente gana, porque la raíz nueva no tiene colonizadores. **No la voy a
   inventar** — regla 1 y regla 3. → pedirla a Alma Agrícola.
4. **🟡 ¿El Promobac se está guardando a ≤12 °C?** La ficha lo exige. Rionegro está a
   18–22 °C ambiente. Si lleva meses sin refrigerar, la carga declarada no es la que se
   está aplicando y todo el cálculo de costo por UFC cambia. → Vanessa.
5. **🟡 ¿Llegó el Fosfolip?** Si no, la hoja corre con Estabios a la misma tasa de 2 L/ha.
6. **🟡 Precio del Raizal 400** — para cerrar el ahorro completo.
7. **🟡 Ficha del Campofert Humus 15** — ahora que el Fullfert declara 150 g/L de CEHT, la
   comparación se puede hacer por kg de carbono húmico y no por litro.
8. **🟡 Área de Inv 2** — es el bloque de ensayos y no tiene m² medidos, así que es el único
   que sigue con dosis fija.

## 8. La regla que sale de esto

> **Una dosis fija por tanque es un error de diseño, no un redondeo.** Es la cuarta vez que
> aparece en este repositorio: sacos por cama en el Bokashi, 300 g de Naturcomplet, los
> cotes, y ahora los 500 cc de Promobac. **Toda dosis se escribe por m² o por planta, y se
> convierte a cantidad al final, con el área real de su bloque.**

> **Y un inoculante compite contra lo que ya vive en ese suelo.** Antes de comprar un
> biológico, dividir su carga entre la población residente. Si da menos de 1 %, no es un
> inoculante: es un gasto. Ese cociente descartó el Terra Life en 0,0009 % y le pone un
> signo de pregunta al Fitoderma en 0,04 %.

---

# Addenda 2026-09-09 · las respuestas de Vanessa

Dos respuestas, y cada una mueve algo distinto.

## R1. La muestra microbiológica es de **Bloque 3 y Bloque 4 mezclados**

### Lo que resuelve

**El argumento de futilidad aplica a Inv 3 sin caveat.** Inv 3 está dentro de la muestra que
midió 1,4×10⁶ UFC/g de *Trichoderma*. Ya no hay duda: los 500 g de Fitoderma aportaban
**0,044 %** de la población de ese mismo suelo, y a etiqueta aportarían **0,0045 %**.

### 🔴 Lo que destapa: la regla del Fitoderma está invertida en los dos extremos

El repositorio decía: *"Fitoderma solo en Inv 3 — por Fusarium activo. En Inv 4+5 el
Trichoderma ya está alto (1,4×10⁶)."*

Con la procedencia real de la muestra, **las dos mitades de esa frase son falsas**:

| | Lo que decía el repositorio | Lo que es |
|---|---|---|
| **Inv 3** | Se le pone Fitoderma porque no sabemos que su *Trichoderma* esté alto | **Está DENTRO de la muestra.** Es uno de los dos bloques medidos |
| **Inv 4** | No se le pone porque su *Trichoderma* ya está alto | Está dentro de la muestra, sí — **pero es el único bloque de la finca con *Fusarium* descrito como "generalizado en suelo, inóculo en suelo"** |
| **Inv 5** | No se le pone porque su *Trichoderma* ya está alto | **Nunca se midió.** No está en la muestra. La razón para excluirlo no existe como dato |

Es la misma clase de inversión que apareció al pasar los sacos de Bokashi a kg/m²: la regla
se veía bien orientada y estaba al revés.

### Y el registro de campo no rescata la regla

Los 24 eventos de `incidencia_fitosanitaria.csv`, por bloque:

| Bloque | *Fusarium* | Otros |
|---|---|---|
| **Bloque 3** (3B, 3C, Mini) | **13 eventos** — 11 de mortalidad masiva en lisianthus, Green Ball grave, 3B recurrente con salinidad | Oidio, mosca blanca |
| **Inv 4** | **1 evento, y es el más grave de todos:** *"Fusarium generalizado en suelo, inóculo en suelo"* | Botrytis ×3 |
| **Inv 5** | **CERO** | Mosca blanca (inóculo en suelo) ×3, Botrytis ×2 |

El *Fusarium* vive en Bloque 3 **y** en Inv 4 — que es exactamente lo que la muestra compuesta
cubre: **muestrearon donde está el problema.** Y en Inv 5 no hay un solo evento de *Fusarium*:
sus problemas son mosca blanca y botrytis, y el *Trichoderma* del Fitoderma no es la
herramienta para ninguno de los dos (la mosca blanca ya tiene su protocolo de
Beauveria/Paecilomyces).

**Así que "solo en Inv 3" no tiene apoyo ni en el laboratorio ni en el campo.** Las dos
fuentes dicen Bloque 3 y Bloque 4, no Bloque 3 solo.

### 🟡 El límite de la muestra compuesta

Es un compuesto de dos bloques, así que **promedia**. Bloque 4 tiene la M.O. más alta de la
finca (23,4 % contra 18,6 % de Bloque 3) y es el mejor manejado: es perfectamente posible que
el 1,4×10⁶ sea mayoritariamente suyo y que Bloque 3 esté materialmente más abajo. Es
exactamente lo que pasó con la salinidad de 3B (C.E. 0,829), que el compuesto de Bloque 3
había promediado hasta hacerla invisible.

Eso no cambia la decisión — cuatro órdenes de magnitud aguantan un promedio — pero sí cambia
la petición al laboratorio. **No es "de qué bloque es": es separar el compuesto.**

→ **Pedirle a Bioquirama: Bloque 3 solo, Bloque 4 solo, y Bloque 5, que nunca se ha medido.**

### La decisión sobre el Fitoderma

**Sale del drench.** No porque no sirva, sino porque el drench no es la vía: 0,0045 % de la
población residente del mismo suelo que se está inoculando. Ahorra **$60.461 por aplicación**
de Inv 3 — la mitad del tanque.

Pero hay una razón honesta para no cerrarlo del todo, y no es el *Trichoderma*. El Fitoderma
**no es solo un inoculante**: declara 38 % de carbono orgánico oxidable, 25 % de proteína,
CIC 52,6 meq/100 g y **40 % de EXLV tipo oligosacarinas**. Las oligosacarinas son
**elicitores** — disparan resistencia sistémica inducida, y los elicitores actúan a
concentraciones muy bajas, así que el argumento de masa que descarta al *Trichoderma* no las
descarta automáticamente. **No tengo dosis-respuesta para eso y no la voy a inventar.**

→ **Ensayo partido en Inv 3**, que es el único bloque que lo recibe: mitad de las camas con
50 g a etiqueta, mitad sin nada. Se lee en **mortalidad por *Fusarium* en lisianthus**, que es
el cultivo con los 11 eventos documentados. Mismo patrón que el ensayo Fosfolip/Estabios de
Inv 4.

**Y lo que sí tiene evidencia de campo contra el *Fusarium* no es el drench: es la rotación
biosupresora** — marigold, gomphrena y matricaria intercalados con lisianthus, ya registrada
en el repositorio como *"biosupresores probados en campo"*. Más el Bokashi y el No-Dig, que
son los que explican el 127×.

---

## R2. El Promobac **no** se está guardando refrigerado

Su ficha exige **≤12 °C**. Rionegro está a 18–22 °C ambiente.

### Lo que esto le hace al análisis

**Los $148 por 10⁹ UFC son el mejor caso, no el caso.** El 1×10⁸ UFC/mL por organismo es una
garantía **en las condiciones de almacenamiento de la etiqueta**. Fuera de ellas, el conteo
decae, y cuánto no se puede sacar de la ficha. Si la viabilidad estuviera al 10 %, el Promobac
pasaría a $1.480 por 10⁹ — **de ser el más barato del programa al más caro.** Toda la razón
por la que se queda depende de una condición que no se está cumpliendo.

La matización honesta en la otra dirección: los *Bacillus* de estas formulaciones son
**endosporas**, que son genuinamente robustas — sobreviven mucho peor que 22 °C, y el producto
tiene que aguantar transporte y estantería, que rara vez están a 12 °C. El límite de la
etiqueta es una garantía de vida útil, no un acantilado. **Pero no sé cuánto decayó, y ese es
el punto.**

### 🔴 Esto me hace retroceder en parte de la corrección de dosis

Aquí hay una interacción que no había visto: **los 500 cc de hoy son 5–12× sobre etiqueta, y
ese exceso es exactamente el margen que ha estado cubriendo el error de almacenamiento.**
Bajar de golpe a etiqueta retira el colchón justo cuando no sabemos la potencia real.

Así que la dosis del Promobac **no baja a etiqueta: baja a 2× etiqueta.**

Y sale un regalo operativo: **2× etiqueta del Promobac (2 L/ha) es exactamente la etiqueta del
Fosfolip (2 L/ha)** — los dos quedan en **0,2 mL/m²**, así que la hoja del operario se
simplifica a *"de cada uno va la misma cantidad"*. La tabla por cama está en R3, abajo.

**El margen 2× cuesta $37.170/año** a 3 vueltas de cama (o $185.850 si se mantuviera el
calendario de 15 aplicaciones). Es seguro barato contra una pérdida de potencia que no se ha
medido, y **el conteo de viabilidad es lo que lo retira.**

### Qué hacer, en orden

1. **Meter el Promobac a la nevera hoy.** Gratis, reversible, no requiere ninguna decisión.
   Y **nunca al lado de fungicidas ni fertilizantes** — la ficha también lo prohíbe.
2. **Anotar la fecha de compra y el lote.** Sin eso el conteo de viabilidad no se puede
   interpretar.
3. **Conteo de viabilidad sobre el frasco que está en la bodega** — no sobre uno nuevo. Es
   una siembra en placa de *Bacillus*, barata, y es la única medición que decide si el
   Promobac es el producto más barato del programa o el más caro. Si vuelve cerca de 1×10⁸,
   la dosis baja a etiqueta y el margen 2× se retira.
4. **Verificar la temperatura de almacenamiento del Fosfolip y del Estabios** antes de
   comprarlos: también son líquidos. El Fitoderma es polvo seco al 3 % de humedad y su ficha
   no pide refrigeración — *aunque tampoco declara condiciones de almacenamiento, así que eso
   lo estoy infiriendo de la formulación, no leyendo de la etiqueta.*

---

## El costo, con las dos respuestas dentro

| | Por aplicación (3 bloques) | Al año |
|---|---|---|
| **HOY** — 15 aplicaciones/año | $245.877 | **$3.688.155** |
| Dosis corregida, mismo calendario | $46.679 | $700.182 → **ahorro $2,99 M** |
| Dosis y momento, a 3 vueltas/año | $46.679 | **$140.036** → **ahorro $3,55 M** |

Bajó $0,09 M contra la versión anterior: es lo que cuestan el margen 2× del Promobac y nada
más — el Fitoderma sale del drench, que va en la dirección contraria y compensa.

## Lo que quedó abierto después de estas dos respuestas

1. **🔴 Bioquirama: separar el compuesto** — Bloque 3 solo, Bloque 4 solo, **y Bloque 5, que
   nunca se ha medido.** Es lo que dice si Bloque 3 está materialmente por debajo del
   promedio, como pasó con la salinidad de 3B.
2. **🔴 Conteo de viabilidad del Promobac que está en la bodega**, con fecha y lote.
3. **🟡 *Trichoderma* por bloque a lo largo del tiempo** — sigue siendo la medición que
   sostiene o tumba el cambio de calendario.
4. **🟡 Dosis de inmersión de raíz del Fitoderma** — ahora es más importante, porque es la
   única vía que le queda al producto. → Alma Agrícola.
5. **🟡 Temperatura de almacenamiento del Fosfolip y del Estabios.**

---

## 🔴 R3. El drench se aplica con **bomba de espalda de 20 L, cama por cama** — no por el tanque

> *"El drench de inoculación lo estamos haciendo en bomba de espalda de 20 litros, porque si no
> hacemos por el tanque le aplica a un bloque entero, y recuerda que las camas están todas
> mezcladas."* — Vanessa, 2026-09-09

**Tiene razón y me tumba la tabla.** Yo construí todas las dosis sobre un tanque de 2.000 L por
bloque porque eso es lo que decía el repositorio: *"Alexander prepara el tanque completo y riega
todo el invernadero por goteo. Es más eficiente que aplicar cama por cama y reduce jornal."*
**Ese párrafo está desactualizado**, y arrastró todo el cálculo.

### Y el error era peor que una unidad equivocada

Aplicar por bloque es **incompatible con lo que yo mismo acababa de recomendar.** El cambio de
momento — inocular el día que se prepara la cama — solo funciona si se puede aplicar **a esa
cama**. Por el goteo de un bloque entero el producto le cae a todas las camas, incluidas las que
están en plena producción y no se están preparando. Es decir: **la bomba de espalda no es un
apaño, es el único método compatible con el cambio de calendario.** La corrección de Vanessa
arregla una inconsistencia interna de mi propia propuesta, no solo un dato.

Es la misma clase de error que el de los cotes: defendí un diseño sobre una premisa que estaba
en el repositorio y que ya no era cierta. **La premisa había que verificarla, no suponerla
plausible.**

### La regla que resuelve la bomba de 20 L

Con 20 L por bomba y camas de 6 a 48 m², una bomba no cubre una cama grande. Y ahí está la
trampa que hay que evitar: **si la dosis se escribe "por bomba", se vuelve otra dosis fija por
envase** — el cuarto error de esta misma familia.

> **El número de la tabla es lo que va en la CAMA, no en la bomba.
> Si la cama necesita dos bombas, va la MITAD de la dosis en cada una.**

Así la tasa por m² se respeta sin importar cuántos litros de agua se usen. La dosis y el agua
quedan desacopladas, que es exactamente el arreglo.

### Dosis por cama · 0,2 mL/m² de cada producto

| Cama | m² | Promobac | Fosfolip |
|---|---|---|---|
| **Inv 3A** | 35,6 | 7 mL | 7 mL |
| **Inv 3B larga** | 48,1 | 9,5 mL | 9,5 mL |
| **Inv 3B corta** | 11,7 | 2,5 mL | 2,5 mL |
| **Inv 3C larga** | 25,2 | 5 mL | 5 mL |
| **Inv 3C corta** | 12,6 | 2,5 mL | 2,5 mL |
| **Mini** (larga) | 12,6 | 2,5 mL | 2,5 mL |
| **Inv 4A · Inv 4B** | 20,2 | 4 mL | 4 mL |
| **Inv 4C larga** | 40,5 | 8 mL | 8 mL |
| **Inv 4C media** | 38,2 | 7,5 mL | 7,5 mL |
| **Inv 4C corta** | 36,0 | 7 mL | 7 mL |
| **Inv 5** | 31,7 | 6,5 mL | 6,5 mL |
| **Ext 3A** | 32,6 | 6,5 mL | 6,5 mL |
| **Ext 3B larga** | 48,1 | 9,5 mL | 9,5 mL |
| **Ext 3B corta** | 11,7 | 2,5 mL | 2,5 mL |
| **Ext 4** | 40,3 | 8 mL | 8 mL |
| **Ext 5** | 31,7 | 6,5 mL | 6,5 mL |
| **Inv 6** | 31,7 | 6,5 mL | 6,5 mL |

Redondeado a los 0,5 mL. **Las 17 filas son las mismas y en el mismo orden que la hoja de
preparación de camas**, para que el operario lea las dos hojas igual. En el Mini se aplica la
regla que ya tiene esa hoja: *en la cama corta va la mitad de todo* (1,5 mL).

Todo se mide con **una jeringa de 10 mL**. Nada por debajo de 1,5 mL.

### Lo que cambia y lo que no

| | Efecto |
|---|---|
| **La tasa por m²** | No cambia. Es la misma que la de la tabla por bloque |
| **El costo** | No cambia: **$22,23 por m² inoculado** ($0,2 mL × $111,14/mL entre los dos productos) |
| **El agua** | Pasa de ~2 L/m² por goteo a ~0,4–0,6 L/m² por bomba. La concentración en la bomba sube a 0,035 %, que es una concentración normal de drench. Y el paso 4 de la preparación ya moja la cama con agua sola, así que el suelo está húmedo y el inoculante solo tiene que entrar |
| **El jornal** | 🟡 Sube: es cama por cama en vez de abrir una válvula. Ese costo no está cuantificado y es el único renglón donde la propuesta cuesta más que hoy |
| **El Fitoderma** | Su dosis por cama a etiqueta son 1,8 g (Inv 3A) — **no es pesable en campo.** Queda fuera de la hoja: va solo en las camas del ensayo partido, con la cantidad **ya pesada por Vanessa** |

### Y el párrafo del repositorio que hay que corregir

*"Por tanque, no por cama individual… es más eficiente que aplicar cama por cama y reduce
jornal."* Corregido en `02-nutricion/03-drench-inoculacion.md`. La eficiencia de jornal era real
pero se pagaba aplicando producto a camas que no lo necesitaban — **y con las camas mezcladas,
a camas que no lo debían recibir.**

---

## 🔴 R4. La dosis, investigada · **retiro la sobredosis de 5–12×**

> *"7 cc por cama es una locura, cuando suelen recomendar 1 cc a 2 cc por litro."*
> *"Normalmente para mojar una cama son entre 80 y 100 litros."*
> *"Debes investigar más sobre la mejor forma de aplicar un drench, porque si no se cumple el
> objetivo y queda corto es una absoluta pérdida de tiempo."* — Vanessa, 2026-09-09

Tiene razón, y el error mío es más de fondo que un número: **estaba mezclando dos bases de
dosificación distintas y comparando una contra la otra.**

### Lo que dice la literatura de drench

Lo decisivo (Sprayers101, extensión agrícola): **en un drench la dosis va por área y el volumen
de agua es un parámetro APARTE**, elegido por la profundidad de infiltración que se quiere, y
ajustado por textura, compactación y porosidad del suelo. El carrier típico que citan para un
drench es **1.200–2.000 L/ha** — muy por encima de un volumen foliar, y aun así muy por debajo
del suyo.

Los cc/L **no son la especificación: son el cociente de las dos cosas.**

### Y aquí las dos reglas se reconcilian

| | Dosis resultante |
|---|---|
| **1 cc/L en 1.200–2.000 L/ha** (el carrier típico) | **1,2–2,0 L/ha** ← **es exactamente la etiqueta del Promobac (1 L/ha)** |
| 1 cc/L en 80–100 L por cama | **22–28 L/ha** |
| 2 cc/L en 80–100 L por cama | **45–56 L/ha** |

**La regla de 1–2 cc/L y la etiqueta no se contradicen: coinciden.** Se separan porque
**80–100 L por una cama de 35,6 m² son 22.500–28.100 L/ha** — de 11 a 23 veces el carrier de
drench típico. A ese volumen de agua, sostener 1–2 cc/L multiplica la dosis por área entre 22 y
56 veces.

Dicho de otro modo: **dos fincas que las dos "aplican a 1 cc/L" aplican cantidades
completamente distintas si mojan distinto.** Por eso mis 7 mL y sus 20–40 cc por bomba están tan
lejos: no es un desacuerdo sobre la dosis, es un desacuerdo sobre la base.

### 🔴 Lo que retiro

**La "sobredosis de 4,9× a 12,1× contra etiqueta" no es un hallazgo válido.** La medí contra un
número por hectárea que la ficha da **sin especificar volumen de aplicación**, lo que lo vuelve
inutilizable para un drench sin ese dato. Puesta en la banda de lo que la práctica de campo
realmente usa, la tasa por área de hoy **está dentro de lo defendible, no por encima.**

| | L/ha | Contra etiqueta |
|---|---|---|
| Etiqueta Promobac | 1,0 | 1× |
| **HOY, Inv 3** | 4,9 | 4,9× |
| **HOY, Inv 5** | 12,1 | 12,1× |
| Lo que yo propuse | 2,0 | 2× |
| 1–2 cc/L a 80–100 L/cama | 22–56 | 22–56× |

**El nivel de hoy no estaba mal. Lo que estaba mal era el ALCANCE** — aplicarlo al bloque
entero, incluidas las camas en producción, en vez de a las camas que se están preparando — **y
la variación de 2,5× entre bloques**, que sí es real: Inv 3 recibe 4,9 L/ha e Inv 5 recibe 12,1
por la misma dosis fija de 500 cc. **Estandarizar esa tasa sigue siendo un arreglo. Recortarla
5–12× no.** Y todo el ahorro viene del alcance y del momento, no de bajar la dosis.

### La dosis que propongo, y por qué

El criterio de decisión es el que ella puso: **si queda corto, se pierde la aplicación, el
jornal y la ventana de trasplante; si sobra, se pierde plata.** El error es asimétrico, así que
bajo incertidumbre se va arriba. Pero 22–56× la etiqueta no lo puedo justificar con nada de lo
que encontré.

> **10 mL de Promobac y 10 mL de Fosfolip por cada bomba de 20 L.**

Que a 90 L por cama son **0,5 cc/L · 1,26 mL/m² · 12,6 L/ha · 45 mL por cama.**

Por qué ahí:

- Es **el techo de lo que la finca ya aplica** por área (los 12,1 L/ha de Inv 5), no una
  invención. Nadie ha reportado que sobre.
- Es **la mitad del extremo bajo de la convención** (1 cc/L), y esa diferencia es exactamente el
  exceso de agua contra el carrier típico.
- Cubre el problema de refrigeración: 12,6 L/ha deja margen de sobra si la viabilidad decayó.
- **Y se autoajusta al tamaño de la cama sin ninguna tabla:** cama más grande → más bombas →
  más producto, en proporción. La dosis por bomba y la dosis por m² son la misma cosa mientras
  se moje igual. Eso elimina la tabla de 17 filas y el problema de "¿va en la cama o en la
  bomba?" de un solo golpe.

**Lo que cierra la discusión de verdad es una pregunta al proveedor: *el 1 L/ha de la etiqueta,
¿en cuántos litros de agua?*** Con ese dato las dos bases se reconcilian y la dosis deja de ser
un juicio.

### Costo

| | Al año |
|---|---|
| **HOY** — 15 aplicaciones × 4 bloques por goteo + Fitoderma | **$4.446.915** |
| **Propuesto** — 60 camas × 3 vueltas, 45 mL de cada uno por cama | **$900.234** |
| | **ahorro $3.546.681, y con MÁS cobertura** (hoy el Mini y los exteriores no reciben nada) |

$5.001 por cama, los dos productos.

---

## 🔴 R5. La técnica: donde de verdad se decide si "queda corto"

Esto es lo que la investigación cambió más, y no es la dosis. **La dosis está dentro de un
factor de 2–3; la técnica puede dejar la aplicación en cero.**

### 1. 🟢 El agua: cloro descartado

Las guías piden **cloro libre por debajo de 0,5 ppm** (el cloro residual mata *Bacillus* y
*Trichoderma*) y **pH entre 5,5 y 7,5**.

> **🟢 CERRADO (Vanessa, 2026-09-09): el agua es de nacimiento y no tiene cloro.**

Era el riesgo que podía anular todo el programa biológico, y no existe. **Con eso, la falta de
riego de arrastre pasa a ser el candidato #1 a "queda corto".**

**Y esto corrige el repositorio:** `00-contexto/01-empresa-y-objetivos.md` decía *"Agua de
acueducto (no nacimiento)"* — exactamente al revés. De haberlo tomado como cierto, la conclusión
habría sido la contraria. Corregido.

*Detalle menor:* un nacimiento a 2.100 m puede salir a 12–16 °C. El agua fría no mata la espora
de *Bacillus*, solo retrasa su germinación. No cambia la dosis ni la técnica; solo es una razón
más para aplicar al final de la tarde y no en la madrugada.

### 2. Suelo húmedo, no saturado — y **riego de arrastre después**

La secuencia que la literatura da para un drench:

1. **Suelo húmedo pero no saturado antes** de aplicar. En seco el producto se adsorbe en la
   superficie y el agua se va por grietas. → **Esto ya lo hacen**: es el paso 4 de la
   preparación de camas, el riego suave con agua sola. Estaba bien puesto.
2. **Aplicar el drench.**
3. **🔴 Riego de arrastre con agua sola inmediatamente después**, para mover el producto de la
   superficie a los 5–10 cm donde va a estar la raíz nueva. **Este paso NO está en el protocolo
   y es el candidato más fuerte a "queda corto".**

Los 90 L por cama son **2,5 mm de agua**. Sobre suelo ya húmedo eso mueve el producto unos pocos
centímetros; sobre suelo seco, apenas uno. **Sin el arrastre, el inoculante se queda arriba** —
donde le da el sol, se seca, y no hay raíz.

### 3. La medición que responde la pregunta directamente, y es gratis

La misma fuente dice cómo ajustar el volumen: **con un barreno o una pala, mirar hasta dónde
llegó el frente de humedad.**

> **Después de la próxima cama inoculada: abrir un hueco y medir en centímetros hasta dónde
> mojó.** Si no llegó a 10 cm, falta arrastre o falta agua. **Eso no requiere laboratorio, ni
> proveedor, ni presupuesto — y contesta "¿quedó corto?" hoy mismo.**

Anotarlo en `07-datos/decisiones_manejo.csv`: cama, litros aplicados, centímetros de
infiltración. Tres aplicaciones y la pregunta queda cerrada con datos de la finca.

### 4. Lo demás de la técnica

| Regla | Por qué |
|---|---|
| **Aplicar al final de la tarde**, nunca a pleno sol | UV y calor matan el inóculo en la superficie |
| **Usar la bomba dentro de las 2–3 horas** de mezclada | No se guarda de un día para otro |
| **Agitar durante la aplicación** | Las esporas de *Bacillus* sedimentan; la última bomba queda pobre y la primera cargada |
| **Bomba lavada, nunca la de fungicidas** | Residuo de fungicida en el tanque anula la aplicación completa |
| **Boquilla de chorro/abanico grueso, a baja presión** | Un abanico fino es para follaje; aquí se quiere volumen sobre el suelo, no niebla |
| **Nada de fertirriego esa semana** en esa cama | Ya estaba en el protocolo |

### Y una consecuencia sobre el plástico

El paso 6 de la preparación es poner el plástico. **Eso juega a favor**: sella la humedad y
protege el inóculo del sol y del secado. Pero **el arrastre tiene que ir antes del plástico**, o
después ya no hay forma de mover nada.

---

## Lo que hay que preguntar, en orden de lo que desbloquea

1. **🔴 Al proveedor: el 1 L/ha del Promobac, ¿en cuántos litros de agua?** Es la pregunta que
   convierte la dosis de juicio en dato.
2. **🔴 Análisis de agua del nacimiento** — ver § R6, abajo. No es de inoculación: es de
   fertirriego, y es plata.
3. **🔴 Medir los centímetros de infiltración** en la próxima cama inoculada.
4. **🔴 Conteo de viabilidad del Promobac** de la bodega, con fecha y lote.
5. **🟡 Bioquirama: separar el compuesto** (Bloque 3 solo, Bloque 4 solo, Bloque 5).
6. **🟡 Dosis de inmersión de raíz del Fitoderma.**

---

## 🔴 R6. No hay análisis de agua, y eso no es un problema de inoculación: es de fertirriego

Buscando el dato del cloro apareció algo más grande. **No hay una sola variable del agua medida
en ningún archivo del repositorio** — cero resultados para análisis de agua, bicarbonatos,
dureza, C.E. del agua. Las tres analíticas de agosto son de **suelo**.

Para la inoculación no importa mucho: sin cloro y con pH probablemente en rango, el agua sirve.
**Para el fertirriego importa mucho, y en pesos.**

La fórmula de fertirriego que se cerró en esta sesión se diseñó desde el análisis de suelo,
**tratando el agua como un blanco**. Pero un nacimiento en zona volcánica aporta cosas, y dos de
ellas van directo contra decisiones que ya se tomaron:

| Lo que puede traer el agua | Contra qué decisión choca |
|---|---|
| **Calcio y magnesio** | El **Haifa N-Cal es 47–52 % del costo del tanque**. Si el agua ya trae Ca, parte de ese nitrato de calcio es redundante |
| **Bicarbonatos (HCO₃⁻)** | Suben el pH y **consumen ácido**. El tanque corre a 5,6–5,8, que es el pH sobre el que se construyó todo el argumento del quelato de cobre y del *Penicillium* del Fosfolip. Con bicarbonatos altos, mantener ese pH cuesta ácido que hoy no está presupuestado |
| **Azufre como sulfato** | Ya se eliminó el Bitter Mag por exceso de azufre en Bloques 3 y 5. Si el agua trae sulfato, ese diagnóstico está incompleto |
| **Sodio** | El suelo tiene C.E. muy baja (0,202–0,280), pero 3B ya mostró salinidad activa (0,829). El agua es la fuente que nadie ha mirado |
| **Hierro y boro** | El Haifa Micro se compró por sus micros. El agua puede estar aportando parte |

**No estoy afirmando que el agua traiga nada de esto** — no hay dato, y ese es exactamente el
punto. Es una entrada sin medir en una fórmula que ya está corriendo.

**Qué pedir**, al mismo laboratorio que hizo los suelos, en una sola muestra: **pH · C.E. ·
bicarbonatos · Ca · Mg · Na · K · S-SO₄ · Fe · B · dureza total**. Es un análisis estándar y
barato, y es el único insumo que le falta a la fórmula de fertirriego para estar completa.

Y hay un segundo motivo, operativo: el agua de nacimiento **arrastra sedimento**. Con la bomba
nueva y el goteo, eso es taponamiento de goteros — que es precisamente el problema de
uniformidad de riego que el repositorio ya identifica como *la limitante dominante* (solo ~22 %
del área rinde a potencial). **Vale preguntar si hay filtro y de qué malla.**

---

## 🔴 R7. ¿Por qué solo esos dos? · auditoría del argumento

> *"Muéstrame el argumento de que esos dos productos son los únicos para el drench."*
> — Vanessa, 2026-09-09

### Primero, cómo se construyó realmente

**Es un argumento de eliminación, no de diseño.** Tomé la lista de productos que ya estaban en
el tanque y fui tachando:

| Producto | Por qué salió | Fuerza del argumento |
|---|---|---|
| **Raizal 400** | Producto de trasplante por etiqueta · auxina 33–67× diluida · P que el alofano fija | 🟢 **Fuerte.** Tres razones independientes, todas de su propia ficha |
| **Fullfert** | Aporta 0,06 g C/m² contra 450 del Bokashi · ya está en el fertirriego | 🟢 **Fuerte.** Es un balance de masa, no una opinión |
| **Estabios** | 1×10⁸ UFC **total** entre 4 organismos: $590 por 10⁹ contra $148 | 🟡 **Medio.** Es un argumento de precio por función, no de que no sirva. Por eso quedó en ensayo partido |
| **Fitoderma** | 0,0045 % del *Trichoderma* residente | 🟡 **Medio.** El conteo residente es un compuesto de Bloque 3+4, y sus oligosacarinas no las cubre ese argumento. Por eso quedó en ensayo |
| **Terra Life** | 0,0009 % del residente | 🟢 Fuerte para su *Trichoderma* · 🔴 **débil para sus micorrizas** — ver abajo |

Y lo que quedó, quedó **por sobrevivir, no por haber sido elegido:**

| Producto | Por qué se queda |
|---|---|
| **Promobac** | El más barato del programa por UFC útil, y **no hay línea base de *Bacillus*** que permita aplicarle el argumento de futilidad |
| **Fosfolip** | Solubilizador de P — el cuello de botella químico del andisol — y es hongo, que a pH 5,6–5,8 tiene ventaja |

**El problema de un argumento por eliminación es que nunca pregunta la otra dirección:** ¿qué
funciones necesita este suelo en el momento del trasplante, y el conjunto que sobrevivió las
cubre? Eso no lo verifiqué. Al verificarlo aparecen tres huecos.

### La auditoría por función

| Función que este suelo necesita | Evidencia de que la necesita | ¿Cubierta? |
|---|---|---|
| **Antagonismo a *Fusarium*** | 13 eventos en Bloque 3 · Inv 4 *"generalizado en suelo"* · 3×10⁴ UFC/g | 🟢 Sí — los 4 *Bacillus* del Promobac |
| **Solubilización de fósforo** | P soluble **0,107 mg/L**, fijación por alofano | 🟡 Sí, por **una** de las dos vías posibles — ver hueco #1 |
| **PGPR / promoción radicular** | — | 🟢 Sí — Promobac |
| **🔴 Micorrizas** | Andisol que fija P. Es **la otra vía** al fósforo, y la única que lo alcanza por exploración en vez de por solubilización | 🔴 **NO. Y salió con un argumento equivocado** |
| **🔴 Inóculo de mosca blanca en suelo** | Documentado en **3C e Inv 5**. Dos lotes de Matricaria sacrificados | 🔴 **NO en el drench de rutina** — solo como protocolo aparte para Vegmo Single |
| **🟡 Nematodos** | Ninguna. **Nunca se han contado** | 🟡 Pokonia existe, cuesta $129.000/L, y nunca lo analicé |
| **Fijación de N** | Ninguna: se fertirriega N, y Kempf Fase 1 pide **no** exceso de nitrato soluble | 🟢 Correctamente ausente |
| **Carbono / alimento** | — | 🟢 Correctamente ausente: lo hace el Bokashi, 7.500× |

---

### 🔴 Hueco #1 · Micorrizas — apliqué el argumento equivocado

El repositorio las sacó con esto: *"20 esporas/g a 100 g/m² son 2.000 esporas/m² repartidas en
90 kg de suelo. Muy diluido."* Y yo lo dejé pasar sin revisarlo.

**Ese es un argumento de paridad de población, y las micorrizas no funcionan por población.** Un
*Trichoderma* tiene que competir contra 1,4×10⁶ UFC/g que ya están ahí — ahí la paridad manda, y
el argumento es correcto. **Una espora micorrízica no compite contra nada: coloniza una raíz y
después la hifa crece.** Basta un evento de colonización por planta. Es el mismo error que ya
cometí dos veces hoy — juzgar un mecanismo con la vara de otro.

Y hay tres razones más por las que este hueco importa:

1. **Es la otra solución al problema central del suelo.** El andisol fija fósforo; hay dos
   maneras de llegar a ese P: **solubilizarlo** (Fosfolip) o **alcanzarlo con hifas**
   (micorrizas). **Compré una sin compararla con la otra.**
2. **Las condiciones son ideales.** La colonización micorrízica se suprime con P soluble alto.
   El suyo es 0,107 mg/L. No hay nada suprimiéndola.
3. **La comparación de costo está mal planteada.** El Fosfolip se paga **cada aplicación**; una
   micorriza que se establece **persiste y se extiende**, sobre todo en No-Dig. Compararlos por
   aplicación favorece artificialmente al Fosfolip. Hay que compararlos **por año o por vida de
   la cama.**

**Y sin embargo, el argumento correcto puede terminar eliminándolas igual**, por tres razones
distintas de la que se usó:

| | |
|---|---|
| **El No-Dig ya es la intervención micorrízica principal** | No voltear conserva la red de hifas. Es, otra vez, la práctica y no el producto |
| **La rotación biosupresora ya las siembra** | *Marigold* y *matricaria* son Asteraceae, **fuertemente micorrízicas** — la rotación que ya se hace contra el *Fusarium* está construyendo la red gratis |
| **🟡 Casi un tercio del catálogo no es micorrízico** | **Gomphrena, amaranto y celosia** son Amaranthaceae y **dianthus / Green Ball** es Caryophyllaceae: familias mal o no micorrizadas. Una inoculación a toda la finca se desperdicia en esas camas |

**Lo que decide:** el **% de colonización micorrízica en raíz** — análisis estándar, y Bioquirama
ya hace el microbiológico. Con ese número la pregunta se cierra: si la colonización ya es alta,
no se compra nada y el Fosfolip sigue solo; si es baja, hay que comparar en serio contra el
Fosfolip, por año y no por aplicación.

*Nota de precio: el repositorio tiene el Sáfer Micorrizas a **$1.519/kg** en un archivo y a
**$3.272/kg** en otro. Antes de comparar hay que resolver cuál es, y conseguir su **dosis
standalone** — la de 100 g/m² es la del Terra Life, no la suya.*

---

### 🔴 Hueco #2 · La mosca blanca de 3C e Inv 5

El protocolo exige drench de *Beauveria* o *Paecilomyces* antes de plantar **Matricaria Vegmo
Single**, por inóculo de mosca blanca en el suelo de 3C e Inv 5. Eso está bien y es correcto.

**Pero el inóculo está en el suelo independientemente de lo que se siembre encima.** El drench de
preparación de cama en 3C y en Inv 5 es exactamente la oportunidad de atacarlo, y hoy no lo hace:
el protocolo lo trata como un requisito de una variedad, no como una condición de esas camas.

**Pregunta, no recomendación:** ¿el drench de preparación de 3C e Inv 5 debería llevar
*Beauveria*/*Paecilomyces* **siempre**, y no solo cuando entra Vegmo Single? No lo decido solo,
porque depende de si el daño de mosca blanca aparece también en las otras variedades de esas
camas — y eso lo sabe el campo, no el repositorio. Los registros muestran 3 eventos en Inv 5 y 3
en 3C, pero uno de ellos está marcado *"TODAS"*, lo que apunta a que sí.

---

### 🟡 Hueco #3 · Pokonia

*Pochonia chlamydosporia*, nematófago. **Función única — ningún otro producto la cubre.** Cuesta
$129.000/L y está en el protocolo como drench mensual. **No lo analicé**, no tiene ficha en el
repositorio, y sobre todo: **nunca se han contado nematodos en esta finca.** Es el único producto
del programa comprado contra un problema que no está medido.

Se queda como estaba: **ensayo partido en Inv 4** (el único bloque con riego uniforme, o sea el
único donde un ensayo es válido) y **conteo de nematodos por grupo funcional** a Bioquirama.

---

### La respuesta corta a la pregunta

**No, no están demostrados como los dos únicos.** Están demostrados como **los dos que sobreviven
el filtro de costo por UFC entre los productos que ya se estaban comprando** — que es un filtro
bueno para elegir entre productos que hacen lo mismo, y ciego para las funciones que nadie está
comprando.

Lo que sí sostengo con confianza:

- 🟢 **El Raizal y el Fullfert salen.** Balance de masa y etiqueta propia. No dependen de nada
  por medir.
- 🟢 **El Promobac se queda.** Nada lo desplaza por costo por UFC.
- 🟢 **El Fosfolip cubre una función real.** El P soluble en 0,107 mg/L no es discutible.
- 🟡 **Que el Fosfolip sea la MEJOR forma de cubrirla** — eso no lo demostré. Compite con las
  micorrizas y la comparación no se hizo.
- 🔴 **Que sean los únicos DOS** — eso es falso hasta resolver micorrizas y la mosca blanca de
  3C/Inv 5.

**Lo que hay que medir, en orden de lo que desbloquea:** % de colonización micorrízica ·
nematodos por grupo funcional · viabilidad del Promobac. Los tres van en la misma muestra a
Bioquirama, con la separación del compuesto Bloque 3 / Bloque 4 / Bloque 5.
