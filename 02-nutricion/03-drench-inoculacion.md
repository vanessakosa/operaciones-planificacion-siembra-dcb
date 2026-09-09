# Drench / trench de inoculación

> **🔴 REESCRITO EL 2026-09-09.** Llegaron las fichas de Promobac, Fitoderma, Raizal 400 y
> Fullfert — los cuatro renglones del tanque que nunca habían pasado por el filtro de UFC
> por organismo y dosis de etiqueta. El resultado cambió la dosis, el momento y la lista de
> productos. **El razonamiento completo, con los números, está en
> `02-nutricion/09-inoculacion-el-analisis.md`.** La hoja de operario es
> `05-programacion/hojas-operario/inoculacion.html`.

## Lo que cambió, en cuatro líneas

| | Antes | Ahora |
|---|---|---|
| **Dosis** | Fija por tanque de 2.000 L, igual para todos los bloques | **Por m² del bloque**, a la dosis de etiqueta |
| **Momento** | Calendario, cada 3–4 semanas (≈15 al año) | **Una vez por vuelta de cama**, el día que se prepara |
| **Productos** | Fitoderma · Estabios · Promobac · Raizal · Fullfert | **Promobac · Fosfolip** (+ **Fitoderma solo en Inv 3**) |
| **Costo/año** | $3.688.159 | **$611.550** solo con la dosis · **$122.310** con dosis y momento |

## Lógica: por tanque, no por cama individual

Alexander prepara el tanque completo y riega por goteo. Es más eficiente que aplicar cama
por cama y reduce jornal. **Eso no cambia** — lo que cambia es que la cantidad se calcula
con el **área real del bloque**, no con un número fijo por tanque.

## Dosis por bloque

Etiquetas: **Promobac 1 L/ha · Fosfolip 2 L/ha · Fitoderma 500 g/ha.** Agua a ~2 L/m², que
es la práctica actual (2.000 L para los 1.025 m² de Inv 3).

| Grupo | m² | Agua | Promobac | Fosfolip | Fitoderma |
|---|---|---|---|---|---|
| **Inv 3** | 1.025 | 2.000 L | 100 cc | 200 cc | **50 g** |
| **Inv 4** | 680 | 1.400 L | 70 cc | 140 cc | — |
| **Inv 5** | 412 | 800 L | 40 cc | 80 cc | — |
| Mini (7 camas) | 69 | 140 L | 7 cc | 14 cc | — |
| Ext 3A + Ext 3B | 92 | 185 L | 9 cc | 19 cc | — |
| Ext 4 + Ext 5 + Inv 6 | 104 | 210 L | 10 cc | 21 cc | — |

Redondeado hacia arriba desde etiqueta. **Inv 1, Inv 2 y las 3 camas de Ext Inv 2 no tienen
área medida** y quedan fuera de la tabla hasta medirlas.

**Si el Fosfolip no ha llegado**, va Estabios en la misma cantidad (2 L/ha). El Estabios
está en ensayo partido en Inv 4 — ver `02-nutricion/07-programa-biologico.md`.

## Reglas

- **Fitoderma solo en Inv 3** — por *Fusarium* activo (3×10⁴ UFC/g). 🟡 Pero el análisis
  microbiológico **no registra de qué bloque se tomó**, y toda esta restricción descansa en
  que Inv 3 sea distinto, que nunca se midió. Pregunta abierta a Bioquirama.
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

- **🔴 ¿De qué bloque es el análisis microbiológico de Bioquirama?** Sostiene o cae la
  restricción del Fitoderma a Inv 3
- **🔴 *Trichoderma* por bloque** — sostiene o cae el cambio de calendario
- **🟡 Dosis de inmersión de raíz / hueco de trasplante del Fitoderma.** Su ficha da 500 g/ha
  al suelo y menciona uso foliar, pero no da tasa para plúgula. Es donde su 1×10⁸ UFC/g
  realmente gana, porque la raíz nueva no tiene colonizadores. **No inventarla** — pedirla a
  Alma Agrícola
- **🟡 ¿El Promobac se está guardando refrigerado?**
- **🟡 ¿Llegó el Fosfolip?** Si no, corre con Estabios a 2 L/ha
- **🟡 Precio del Raizal 400**, para cerrar el ahorro completo
- **🟡 Área de Inv 1 e Inv 2** — el único bloque que seguiría con dosis fija
- Si el trench de inoculación **reemplaza completamente el volteo** de cama
