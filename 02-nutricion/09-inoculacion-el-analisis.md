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
