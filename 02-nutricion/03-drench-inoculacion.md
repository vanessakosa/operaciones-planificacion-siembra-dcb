# Drench / trench de inoculación

> **🔴 REESCRITO EL 2026-09-09.** Llegaron las fichas de Promobac, Fitoderma, Raizal 400 y
> Fullfert — los cuatro renglones del tanque que nunca habían pasado por el filtro de UFC
> por organismo y dosis de etiqueta. El resultado cambió la dosis, el momento y la lista de
> productos. **El razonamiento completo, con los números, está en
> `02-nutricion/09-inoculacion-el-analisis.md`.** La hoja de operario es
> `05-programacion/hojas-operario/inoculacion.html`.

## Lo que cambió

| | Antes | Ahora |
|---|---|---|
| **Método** | Tanque de 2.000 L por bloque, por goteo | **Bomba de espalda de 20 L, cama por cama** (Vanessa, 2026-09-09) |
| **Dosis** | Fija por tanque, igual para todos los bloques | **0,2 mL/m² de cada producto**, por cama |
| **Momento** | Calendario, cada 3–4 semanas (≈15 al año) | **Una vez por vuelta de cama**, el día que se prepara |
| **Productos** | Fitoderma · Estabios · Promobac · Raizal · Fullfert | **Promobac · Fosfolip** (Fitoderma solo en el ensayo de Inv 3) |
| **Costo/año** | $3.688.155 | **$700.182** solo con la dosis · **$140.036** con dosis y momento |

## 🔴 Cama por cama, con bomba de espalda de 20 L

**Corrige lo que decía este archivo hasta el 2026-09-09** (*"por tanque, no por cama
individual… es más eficiente y reduce jornal"*). Esa eficiencia era real pero se pagaba
aplicando producto a camas que no lo necesitaban — y **con las camas mezcladas dentro de cada
bloque, a camas que no lo debían recibir.**

Y es lo único compatible con inocular el día que se prepara la cama: por el goteo de un bloque
entero el producto le cae también a las camas en plena producción.

> **El número de la tabla es lo que va en la CAMA, no en la bomba.
> Si la cama necesita dos bombas, va la MITAD de la dosis en cada una.**

Sin esa regla, "tanto por bomba" se vuelve otra dosis fija por envase — el cuarto error de la
misma familia en este repositorio.

## Dosis por cama · 0,2 mL/m² de cada producto

Etiquetas: **Promobac 1 L/ha** (se aplica a **2× etiqueta** mientras no haya conteo de
viabilidad — ver abajo) · **Fosfolip 2 L/ha** · Fitoderma 500 g/ha. Los dos líquidos quedan en
la misma cifra: **de cada uno va la misma cantidad.**

| Cama | m² | Promobac | Fosfolip |
|---|---|---|---|
| Inv 3A | 35,6 | 7 mL | 7 mL |
| Inv 3B larga | 48,1 | 9,5 mL | 9,5 mL |
| Inv 3B corta | 11,7 | 2,5 mL | 2,5 mL |
| Inv 3C larga | 25,2 | 5 mL | 5 mL |
| Inv 3C corta | 12,6 | 2,5 mL | 2,5 mL |
| Mini (larga · en la corta la mitad) | 12,6 | 2,5 mL | 2,5 mL |
| Inv 4A · Inv 4B | 20,2 | 4 mL | 4 mL |
| Inv 4C larga | 40,5 | 8 mL | 8 mL |
| Inv 4C media | 38,2 | 7,5 mL | 7,5 mL |
| Inv 4C corta | 36,0 | 7 mL | 7 mL |
| Inv 5 | 31,7 | 6,5 mL | 6,5 mL |
| Ext 3A | 32,6 | 6,5 mL | 6,5 mL |
| Ext 3B larga | 48,1 | 9,5 mL | 9,5 mL |
| Ext 3B corta | 11,7 | 2,5 mL | 2,5 mL |
| Ext 4 | 40,3 | 8 mL | 8 mL |
| Ext 5 | 31,7 | 6,5 mL | 6,5 mL |
| Inv 6 | 31,7 | 6,5 mL | 6,5 mL |

Redondeado a los 0,5 mL, medido con **jeringa de 10 mL**. Son las **mismas 17 filas y en el
mismo orden** que la hoja de preparación de camas. **Costo: $22,23 por m² inoculado.**

**Inv 1, Inv 2 y las 3 camas de Ext Inv 2** no tienen área medida y quedan fuera hasta
medirlas.

**Si el Fosfolip no ha llegado**, va Estabios en la misma cantidad. El Estabios está en ensayo
partido en Inv 4 — ver `02-nutricion/07-programa-biologico.md`.

🟡 **El jornal sube:** es cama por cama en vez de abrir una válvula. Es el único renglón donde
esta propuesta cuesta más que hoy, y no está cuantificado.

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

- **🔴 Bioquirama: separar el compuesto** — Bloque 3 solo, Bloque 4 solo, **y Bloque 5, que
  nunca se ha medido.** El compuesto promedia, y Bloque 4 tiene la M.O. más alta de la finca:
  es posible que el 1,4×10⁶ sea mayoritariamente suyo. Es lo que ya pasó con la salinidad de 3B
  (C.E. 0,829), que el compuesto de Bloque 3 había vuelto invisible
- **🔴 Conteo de viabilidad del Promobac** que está en la bodega, con fecha y lote — decide si
  es el producto más barato del programa o el más caro
- **🔴 *Trichoderma* por bloque en el tiempo** — sostiene o cae el cambio de calendario
- **🟡 Cuántas bombas de 20 L se gastan por cama** — para poder cuantificar el jornal
- **🟡 Temperatura de almacenamiento del Fosfolip y del Estabios** — también son líquidos
- **🟡 Dosis de inmersión de raíz / hueco de trasplante del Fitoderma.** Su ficha da 500 g/ha
  al suelo y menciona uso foliar, pero no da tasa para plúgula. Es donde su 1×10⁸ UFC/g
  realmente gana, porque la raíz nueva no tiene colonizadores. **No inventarla** — pedirla a
  Alma Agrícola
- **🟡 ¿El Promobac se está guardando refrigerado?**
- **🟡 ¿Llegó el Fosfolip?** Si no, corre con Estabios a 2 L/ha
- **🟡 Precio del Raizal 400**, para cerrar el ahorro completo
- **🟡 Área de Inv 1 e Inv 2** — el único bloque que seguiría con dosis fija
- Si el trench de inoculación **reemplaza completamente el volteo** de cama
