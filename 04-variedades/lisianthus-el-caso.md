# Lisianthus — el sustento para la decisión de portafolio

> Vanessa 2026-09-11: *"David siempre me dice… tenemos que evaluar si esta debe
> seguir en el portafolio, y yo por el contrario la amo, porque siento que ella
> es la base de todos los bouquets: **todo lo que se ponga alrededor de un
> lisianthus se vende**. Necesito tener el sustento de que lo que estoy diciendo
> es así, que no estoy perdiendo dinero."*

Esto es lo que dicen los datos del 2026-09-11, con lo que falta señalado.

## La hipótesis se sostiene

Se comparó lo vendido en los **20 productos que llevan Lisianthus** contra los
**101 que no**, sobre $291.287.084 de venta real registrada:

| | Productos | Unidades | Ingreso | $/unidad |
|---|---|---|---|---|
| **CON lisianthus** | 20 | 960 | **$83.943.950** | **$87.442** |
| SIN lisianthus | 101 | 3.535 | $207.343.134 | $58.654 |

- **Ticket 1,5× mayor**: $87.442 contra $58.654.
- **1,4× más unidades por producto**: 48,0 contra 35,0.
- **El 29 % del ingreso de la finca pasa por un producto que lleva Lisianthus**,
  siendo el 17 % del catálogo.

No prueba causalidad —puede ser que el lisianthus se ponga en los productos que
ya iban a ser caros— pero **es consistente con la hipótesis y no con la
contraria.**

## Lo que costaría no producirlo

Los 3.370 tallos vendidos, comprados en el mercado:

| Precio de compra | Costo |
|---|---|
| $700/tallo | $2.359.000 |
| $900/tallo | $3.033.000 |
| *(una rosa, para comparar: $3.000)* | *$10.110.000* |

**Comprarlo es barato** — menos del 4 % del ingreso que pasa por sus productos.
Así que el argumento de peso **no es el costo del tallo**: es lo que Vanessa
señala después.

> *"Lo que tiene de maravilloso es que en los carritos dura. Una rosa se
> apertura ahí mismo. El lisianthus tiene una duración muy grande, entonces los
> bouquets permanecen bonitos; así le cambie una boca de dragón o una campánula
> varios días, el lisianthus está bien."*

**Ese es el argumento fuerte y es el único que no está medido.**
`vida_en_vaso.csv` tiene **una sola fila** —Boca de Dragón, 7-10 días,
`PRIMERA_EN_MARCHITAR`— y Lisianthus no está. Si el lisianthus sostiene el
bouquet en exhibición mientras el resto se cambia, reduce reposición y descarte
en punto de venta: **es costo evitado en la sala, no en la cama**, y hoy no se
puede cuantificar.

## Lo que costó de verdad esta cohorte

La pestaña **`Plant Andres`** de `PROGRAMACION_2026_v8` cerró este número el
2026-09-11, y espejada queda en `07-datos/germinacion_andres.csv`. **Vanessa
tenía razón hasta el último dígito: 27.000 semillas exactas**, 12 cultivares,
enviadas a germinar en la semana 47 de 2025 y entregadas en la semana 9 de 2026
— 15 semanas en bandeja.

La merma no era una, eran **dos, y en etapas distintas**:

| Etapa | Plantas | Sobrevive | Dónde se pierde |
|---|---|---|---|
| Semillas enviadas | **27.000** | — | — |
| Plántulas entregadas | **19.301** | **71,5 %** | en el plantulador |
| Viables en campo semana 23 | **14.337** | **74,3 %** | en la cama: oidio + fusarium |
| **De semilla a planta productiva** | | **53,1 %** | |

De esas 14.337, **1.249 quedaron marcadas `pinch enfermas`** (8,7 %) — plantas
vivas pero comprometidas.

**El dato corrige el que traía este documento.** Decía «merma de plantulación
53 %» sobre 12.728 trasplantadas; el 53 % es real pero es lo **contrario**: es
lo que **sobrevive** de punta a punta, y se reparte 28,5 % plantulador + 25,7 %
campo. Son dos problemas distintos, con dueños distintos: uno se negocia con
Andrés, el otro se maneja en la cama.

| | |
|---|---|
| Tallos cosechados (semanas 25-35, ventana abierta) | 6.926 |
| **Tallos por planta viable** | **0,48** contra **2** esperados = **24 %** |
| Tallos por plántula entregada | 0,36 |
| Tallos por semilla enviada | 0,26 |

Ese 24 % es el precio del oidio, y coincide con la lectura de campo:

> *"La mitad se perdió en primera floración con oidio, porque teníamos que hacer
> labores culturales semanalmente. El oidio generó una mortalidad inicial
> importante y generó además una aplicación adicional de inputs. Pero eso
> tampoco canceló toda la producción."*

**Dos advertencias sobre ese 0,48.** La ventana sigue abierta —la segunda
floración está en curso— así que es un piso, no un resultado. Y los dos tramos
de merma son **anteriores e independientes**: arreglar la germinación no arregla
el oidio, y al revés. Cada uno por separado vale ~4.900 plantas.

### El 12.728 era un artefacto del registro, no un dato

`campo_siembras.csv` no registró 12.728 plantas trasplantadas: registró
**la primera de hasta cuatro entregas**. La columna `Cantidad Trasplantada` de
cada cultivar coincide **exactamente** con `entrega_1` de la hoja de Andrés en
**11 de los 12 cultivares** (el doceavo, `Megalo 3 Pink Pop`, quedó en blanco) y
suma 11.400 de las 12.200 que entregó la primera tanda. Las otras 7.101
plántulas llegaron después y entraron como filas sueltas sin cultivar
(«Lisianthus» sem 15 → 1.042, «Lisianthus mas» sem 17 → 286), que sumadas a las
11.400 dan el 12.728 — un número que no es ni la primera entrega ni el total.

**Esto no es sólo de Lisianthus: es una forma en que `campo_siembras.csv`
subcuenta plantas**, y las plantas son el insumo de la fórmula de área
(`plantas × 0,15 × distancia`). Menos plantas contadas = menos área contada =
**$/m²/semana inflado**. En esta cohorte el área real es **52 % mayor** que la que
suma el registro: 19.301 plantas contra 12.728. De las 111 filas de la hoja de Andrés sólo 13 tienen entregas
parciales —las 12 de Lisianthus y `Snapdragon Cannes Light Bronze`— así que el
radio de daño está acotado, pero hay que mirarlo antes de leer un
`$/m²/semana` de un lote entregado por tandas.

### Y la decisión ya no es hipotética

La misma hoja registra la **cohorte siguiente**: **26.000 semillas de 8
cultivares nuevos**, enviadas el 03/06 (semana 23), **entrega estimada semana
38** — es decir, la semana entrante.

| Cultivar | Semillas |
|---|---|
| Macheriena White | 5.000 |
| Corelli Sugoi Deep Pink | 5.000 |
| Megalo 2 Pink Picotee | 5.000 |
| Celeb 3 Pink | 4.000 |
| Celeb Pink | 3.000 |
| Arosa Wine | 2.000 |
| Elegance 3 Champagne | 1.000 |
| Celeb 2 Crystal | 1.000 |

Al 71,5 % de germinación de la cohorte anterior eso son **~18.600 plántulas
llegando a cama**. La conversación con David sobre si el lisianthus sigue en el
portafolio **no es sobre el año entrante: es sobre plantas que ya están en
bandeja**, y lo que está en juego ahora es dónde se siembran y con qué manejo
preventivo de oidio — no si se siembran.

## La segunda floración

En curso al 2026-09-11. Vanessa: **~50 % de la primera**. Los primeros en
florecer son los primeros en la segunda —white, beige neo, apricot— y **los
rosados van al final**.

Eso mueve el eje de ocupación, porque la cama sigue tomada:

| Denominador | $/m²/semana |
|---|---|
| `ciclos_variedad.csv` (29 sem) | $7.600 |
| Real sólo primera floración (25 sem) | $8.816 |
| **Real + segunda (+8 sem)** | **$6.679** |
| Real + segunda (+12 sem) | $5.957 |

**La pregunta operativa no es si el lisianthus rinde: es si la segunda floración
vale la cama.** A la mitad de producción por 8-12 semanas más de ocupación, el
$/m²/semana cae hasta un 32 %. Puede seguir valiendo —por surtido y por vida en
vaso— pero es una decisión distinta de la de sembrarlo.

## Lo que falta para cerrar el argumento

1. **Vida en vaso de Lisianthus** — el argumento central, sin medir. Una sola
   observación en carrito lo resuelve.
2. **Cuál cultivar rindió.** 19 sembrados, todo registrado como `Mix`. Vanessa
   tiene la lectura cualitativa; pasarla a dato permite repetir los buenos.
3. ~~Confirmar las 27.000 semillas~~ — **cerrado** el 2026-09-11 con la pestaña
   `Plant Andres`. Son 27.000 exactas. Lo que sigue abierto es el **precio**:
   la hoja trae cantidades, no costo.
4. **El costo del oidio** — aplicaciones adicionales y labores culturales
   semanales. `aplicaciones_historial.csv` tiene 16 filas y sólo una toca
   Lisianthus.
5. **Fin de cosecha** en las 21 siembras: 0 lo tienen anotado.
