# Drench / trench de inoculación

> **🔴 REESCRITO EL 2026-09-09** con las fichas de Promobac, Fitoderma, Raizal 400 y Fullfert, y
> corregido tres veces el mismo día por Vanessa: el método (bomba de espalda, no tanque), el
> volumen (80–100 L por cama) y la base de la dosis. **El razonamiento completo y lo que se
> retiró están en `02-nutricion/09-inoculacion-el-analisis.md`.** Hoja de operario:
> `05-programacion/hojas-operario/inoculacion.html`.

## Lo que cambió

| | Antes | Ahora |
|---|---|---|
| **Método** | Tanque de 2.000 L por bloque, por goteo | **Bomba de espalda de 20 L, cama por cama** |
| **Alcance** | El bloque entero, camas en producción incluidas | **Solo las camas que se están preparando** |
| **Momento** | Calendario, cada 3–4 semanas (≈15/año) | **Una vez por vuelta de cama**, el día que se prepara |
| **Dosis** | 500 cc fijos por tanque → 4,9 L/ha en Inv 3, 12,1 en Inv 5 | **10 mL por bomba de 20 L** → 12,6 L/ha en todas |
| **Técnica** | Sin riego de arrastre | **Arrastre con agua sola después, antes del plástico** |
| **Productos** | Fitoderma · Estabios · Promobac · Raizal · Fullfert | **Promobac · Fosfolip** (Fitoderma solo en el ensayo de Inv 3) |
| **Costo/año** | $4.446.915 | **$900.234** con más cobertura |

## 🔴 Cama por cama, con bomba de espalda de 20 L

**Corrige lo que decía este archivo hasta el 2026-09-09** (*"por tanque… es más eficiente y
reduce jornal"*). Esa eficiencia era real pero se pagaba aplicando producto a camas que no lo
necesitaban — y **con las camas mezcladas dentro de cada bloque, a camas que no lo debían
recibir.** Y es lo único compatible con inocular el día que se prepara la cama.

## La dosis: 10 mL de cada uno por bomba de 20 L

> **Por cada bomba de 20 L: 10 mL de Promobac + 10 mL de Fosfolip.**
> **De cada uno va la misma cantidad. Todas las bombas se dosifican igual.**

**Se moja la cama con 80–100 L**, o sea 4 a 5 bombas. Eso da **45 mL de cada producto por cama
de 35,6 m²**, que son **0,5 cc/L · 1,26 mL/m² · 12,6 L/ha.**

**No hace falta tabla por cama.** Mientras se moje igual por m², la dosis por bomba y la dosis
por área son la misma cosa: cama más grande → más bombas → más producto, en proporción.

**Por qué 12,6 L/ha y no la etiqueta (1 L/ha) ni la convención de 1–2 cc/L (22–56 L/ha):** en un
drench la dosis va **por área** y el agua es un parámetro aparte; los cc/L son el cociente. La
regla de 1–2 cc/L coincide con la etiqueta cuando el carrier es el típico de drench (1.200–2.000
L/ha), y se dispara a 22–56× cuando el agua son 80–100 L por cama (22.500–28.100 L/ha). Los 12,6
L/ha son **el techo de lo que la finca ya aplicaba** (Inv 5) — no un recorte y no una invención.
Detalle y retractación en el análisis.

**Costo: $5.001 por cama**, los dos productos. **Si el Fosfolip no ha llegado**, va Estabios en
la misma cantidad.

## 🔴 La técnica — es aquí donde se decide si "queda corto"

**La dosis está dentro de un factor de 2–3. La técnica puede dejar la aplicación en cero.**

1. **🟢 El agua: cloro descartado.** Las guías piden cloro libre bajo 0,5 ppm y pH 5,5–7,5.
   **El agua es de nacimiento y no tiene cloro** (Vanessa, 2026-09-09). Era el único riesgo que
   podía anular todo el programa biológico y no existe. *Corrige a
   `00-contexto/01-empresa-y-objetivos.md`, que decía "agua de acueducto (no nacimiento)".*
2. **Suelo húmedo, no saturado, antes de aplicar.** Ya está: es el paso 4 de la preparación
   (riego suave con agua sola). Estaba bien puesto.
3. **🔴 Riego de arrastre con agua sola inmediatamente después del drench, ANTES del plástico.**
   Descartado el cloro, **este es el candidato #1 a "queda corto"**. No estaba en el protocolo:
   los 90 L por cama son
   2,5 mm de agua, que sobre suelo húmedo mueven el producto unos pocos centímetros. Sin
   arrastre el inoculante se queda en la superficie, donde le da el sol y no hay raíz. Después
   del plástico ya no hay forma de moverlo.
4. **Al final de la tarde**, nunca a pleno sol — UV y calor.
5. **Usar la bomba dentro de 2–3 horas** de mezclada. No se guarda de un día para otro.
6. **Agitar durante la aplicación** — las esporas de *Bacillus* sedimentan: la primera bomba
   sale cargada y la última pobre.
7. **Bomba lavada, nunca la de fungicidas.** Residuo en el tanque anula la aplicación completa.
8. **Boquilla de chorro o abanico grueso, baja presión.** Aquí se quiere volumen sobre el suelo,
   no niebla.

### La medición gratis que contesta la pregunta

> **Después de la próxima cama inoculada: abrir un hueco con pala o barreno y medir en
> centímetros hasta dónde llegó el frente de humedad.** Si no llegó a 10 cm, falta arrastre o
> falta agua.

Sin laboratorio, sin proveedor, sin presupuesto. Anotar cama, litros aplicados y centímetros en
`07-datos/decisiones_manejo.csv`. **Tres aplicaciones y la pregunta queda cerrada con datos de
la finca.**

## Reglas

- **🔴 El Fitoderma sale del drench de rutina.** La muestra microbiológica es un **compuesto de
  Bloque 3 + Bloque 4** (Vanessa, 2026-09-09), así que Inv 3 **está dentro** de la medición de
  1,4×10⁶ UFC/g: los 500 g aportaban 0,044 % y a etiqueta aportarían 0,0045 %. Y la regla vieja
  estaba invertida en los dos extremos — Inv 4 es el bloque con *Fusarium* descrito como
  *"generalizado en suelo"* e **Inv 5 nunca se midió**, que era la razón declarada para
  excluirlo. Queda en **ensayo partido en Inv 3** (mitad de las camas con 50 g/ha, mitad sin
  nada, leído en mortalidad por *Fusarium* en lisianthus), **con la cantidad ya pesada por
  Vanessa**: su dosis por cama son 1,8 g y eso no es pesable en campo. Lo que sostiene el
  ensayo no es el *Trichoderma* sino su 40 % de oligosacarinas, que son elicitores y actúan a
  concentraciones bajas — sin dosis-respuesta, así que se mide.
- **🔴 El Promobac se aplica a 2× etiqueta, no a etiqueta.** No está refrigerado (su ficha
  exige ≤12 °C; Rionegro está a 18–22 °C), así que la carga real es desconocida y los 500 cc de
  hoy eran justamente el margen que cubría ese error. El 2× cuesta $37.170/año y **se retira
  con un conteo de viabilidad** sobre el frasco de la bodega.
- **Meter el Promobac a la nevera hoy**, y anotar fecha de compra y lote.
- **No fertirriego** en ese bloque en toda la semana de la inoculación. Solo agua. (Antes
  decía *"Haifa: sí reducido"* en Inv 4 y 5 — se extendió a un no plano.)
- **No mezclar con ningún fungicida.** La ficha del Promobac: *"no mezclar con fungicidas de
  compatibilidad desconocida"*.
- **El Promobac se guarda a ≤12 °C** — su ficha lo exige, y Rionegro está a 18–22 °C
  ambiente. 🟡 Si lleva meses sin refrigerar, la carga declarada no es la que se aplica.
- **Pokonia:** drench mensual, para *Fusarium* y nematodos. Sin ficha en el repositorio.
- Requisito para variedades donde se usan micorrizas al trasplante: suelo sin fungicidas
  recientes.

## Lo que salió del tanque, y por qué

| Producto | Por qué sale |
|---|---|
| **Raizal 400** | Es un producto **de trasplante por etiqueta** (*"plantas jóvenes"*, *"al momento del trasplante"*, *"repetir 2 a 3 veces"*), no de mantenimiento indefinido. Su dosis es **por planta**, no por área. Y a 300 g en 2.000 L entrega su complejo auxínico **33–67× más diluido que la etiqueta**: se paga la hormona y no llega. Su 45 % de P₂O₅ lo fija el alofano mientras se paga por separado un solubilizador para desfijar P |
| **Fullfert** | **Ya está en el tanque de fertirriego**, que es donde su rol de complejante tiene sentido. En el de biológicos aportaba 0,06 g de C/m² contra los **450 g de C/m² del Bokashi** — 7.500× menos. Su masa es irrelevante en los dos sentidos, así que estaba subdosificado 4–19× **y no importa** |
| **Estabios** | Declara 1×10⁸ UFC **total** entre cuatro organismos: **$590 por 10⁹ UFC** contra $148 del Promobac. Ensayo partido en Inv 4 antes de sacarlo del todo |

## 🔴 Lo que hay que tener presente sobre lo que un drench puede y no puede hacer

El suelo mide **1,4×10⁶ UFC/g de *Trichoderma***. En los 82 t de suelo que moja el tanque de
Inv 3 eso son 1,15×10¹⁴ UFC. **Los 500 g de Fitoderma aportaban 0,04 % de eso.** El Sáfer
Terra Life se descartó por aportar 0,0009 %; nunca se le aplicó el mismo filtro al
Fitoderma.

**Un drench no mueve una población establecida.** Lo que sí puede hacer es llevar organismos
**a donde la población residente todavía no llegó**: la cama recién enmendada, la raíz
cortada, el hueco de trasplante. Por eso la inoculación se mudó al día de la preparación de
la cama, y por eso es el **paso 5** de la hoja de preparación.

El aumento de 127× del *Trichoderma* entre 2024 y 2025 **no lo puede explicar el drench**
aportando 0,04 % por aplicación. Lo explican el **Bokashi** y el **No-Dig**. Es el punto de
Ingham: se inocula una vez y después se alimenta.

**Y es comprobable:** pedirle a Bioquirama el ***Trichoderma* por bloque**. Si el drench
fuera el motor, el conteo escalaría con las aplicaciones.

## Protocolo obligatorio de pre-siembra — Matricaria Vegmo Single

Hay inóculo de mosca blanca en el suelo de Inv 5 y 3C. Antes de plantar Vegmo Single en
**cualquier** bloque:

1. Drench pre-siembra obligatorio con **Beauveria bassiana o Paecilomyces**
2. Prevención foliar post-trasplante
3. Nunca sembrarla en Inv 5 ni en 3C

## Pendiente de decidir

- **🔴 Al proveedor: el 1 L/ha del Promobac, ¿en cuántos litros de agua?** Es la pregunta que
  convierte la dosis de juicio en dato, y reconcilia la etiqueta con la regla de 1–2 cc/L
- **🔴 Medir los centímetros de infiltración** en la próxima cama inoculada
- **🔴 Conteo de viabilidad del Promobac** que está en la bodega, con fecha y lote — decide si es
  el producto más barato del programa o el más caro
- **🟡 Bioquirama: separar el compuesto** — Bloque 3 solo, Bloque 4 solo, **y Bloque 5, que nunca
  se ha medido.** El compuesto promedia, y Bloque 4 tiene la M.O. más alta de la finca. Es lo
  que ya pasó con la salinidad de 3B (C.E. 0,829), que el compuesto había vuelto invisible
- **🟡 *Trichoderma* por bloque en el tiempo** — sostiene o cae el cambio de calendario
- **🟡 Dosis de inmersión de raíz del Fitoderma** — es la única vía que le queda al producto
- **🟡 Temperatura de almacenamiento del Fosfolip y del Estabios** — también son líquidos
- **🟡 Jornal real:** 4–5 bombas por cama × 60 camas es el único renglón donde esta propuesta
  cuesta más que hoy, y no está cuantificado
- Si el trench de inoculación **reemplaza completamente el volteo** de cama
