# Lisianthus — el sustento para la decisión de portafolio

> Vanessa 2026-09-11: *"David siempre me dice… tenemos que evaluar si esta debe
> seguir en el portafolio, y yo por el contrario la amo, porque siento que ella
> es la base de todos los bouquets: **todo lo que se ponga alrededor de un
> lisianthus se vende**. Necesito tener el sustento de que lo que estoy diciendo
> es así, que no estoy perdiendo dinero."*

Esto es lo que dicen los datos del 2026-09-11, con lo que falta señalado.

## La hipótesis se sostiene, pero hay que medirla en la ventana correcta

**Vanessa 2026-09-11, corrigiendo la primera versión de esta cuenta:** *"Mamá de
los sueños fue antes de que empezáramos a cosechar lisianthus. Esos lisianthus
eran comprados. Entonces tú tienes que cruzarlo desde que empezamos a cosechar,
según la semana que empezamos a cosechar, inicio de la ventana de corte."*

Es la misma regla que ya rige el área en `ocupacion.py`: **numerador y
denominador tienen que cubrir el mismo periodo.** La primera versión sumaba
venta de todo el año contra cosecha de once semanas, y metía MADRES —donde el
lisianthus fue **comprado**— del lado propio.

La cosecha propia registrada va de la **semana 25 a la 35**. Recortado ahí:

| | Productos | Unidades | Ingreso | $/unidad |
|---|---|---|---|---|
| **CON lisianthus** | 19 | 598 | **$43.952.200** | **$73.499** |
| SIN lisianthus | 92 | 2.776 | $148.248.284 | $53.404 |

- **Ticket 1,38× mayor** — no 1,5× como decía la primera cuenta.
- **23 % del ingreso** pasa por un producto con lisianthus, siendo el 17 % del
  catálogo — no 29 %.

**El argumento sobrevive al recorte, más chico pero en pie.** Y sobrevive
justamente porque el recorte quita la temporada más fuerte del año: si el
lisianthus solo levantara el ticket en MADRES, al sacar MADRES se caía.

*(Para referencia, la cuenta sin recortar —que NO sirve para decidir sobre la
cama, porque mezcla tallo propio con tallo comprado— daba 20 productos, 960
unidades, $83.943.950 y ticket 1,48×.)*

**Las 303 unidades y 379 tallos vendidos antes de la semana 25 no son
nuestros.** Los dos grandes son `Bouquet mamá de los sueños petit` (164) y
`grande` (84). `ficha_completa.py` ya los separa y los imprime aparte en vez de
atribuirlos al grupo.

No prueba causalidad —puede ser que el lisianthus se ponga en los productos que
ya iban a ser caros— pero **es consistente con la hipótesis y no con la
contraria.**

## Lo que costaría no producirlo

Los **2.826 tallos propios vendidos dentro de la ventana**, si hubiera que
comprarlos en el mercado:

| Precio de compra | Costo |
|---|---|
| $700/tallo | $1.978.000 |
| $900/tallo | $2.543.000 |
| *(una rosa, para comparar: $3.000)* | *$8.478.000* |

**Comprarlo es barato** — menos del 6 % del ingreso que pasa por sus productos.
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

## Lo que costó de verdad esta siembra

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

> ⚠️ **El 14.337 está SIN CONFIRMAR.** Es la suma de una columna de la hoja de
> Andrés titulada `Plantas viables WK 23` — doce celdas, una por cultivar. Lo
> único que respalda leerla como «plantas vivas en cama» es que en los doce
> cultivares `entregado − viables = pérdida`, exacto. Pero **no se sabe quién la
> contó, cuándo ni cómo**, y hay dos señales en contra: `Celeb 2 Lovely Pink`
> registra 1.812 viables contra 1.032 entregadas —780 plantas imposibles, la
> pérdida sale en negativo— y el 26 % de mortalidad que arroja **contradice la
> lectura de campo de Vanessa**, que fue *"la mitad se perdió en primera
> floración con oidio"*. Si la buena es la mitad, el tramo de campo no es 25,7 %
> sino ~50 %, y los tallos por planta suben en vez de bajar. **Hay que preguntar
> antes de decidir sobre este número.**

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
**$/m²/semana inflado**. En esta siembra el área real es **52 % mayor** que la que
suma el registro: 19.301 plantas contra 12.728. De las 111 filas de la hoja de Andrés sólo 13 tienen entregas
parciales —las 12 de Lisianthus y `Snapdragon Cannes Light Bronze`— así que el
radio de daño está acotado, pero hay que mirarlo antes de leer un
`$/m²/semana` de un lote entregado por tandas.

### La siembra siguiente está pedida, no sembrada

La misma hoja registra **26.000 semillas de 8 cultivares nuevos**, con fecha
03/06 (semana 23) y **entrega estimada semana 38**.

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

**Las ocho filas tienen la entrega en blanco**, y Vanessa lo confirmó el
2026-09-11: *"la segunda siembra de lisianthus todavía no se ha hecho, ni
siquiera me han entregado esas plántulas."* Así que la hoja y el campo dicen lo
mismo: **está pedida, no entregada, y la siembra no ocurrió.**

*(Queda por confirmar si la semilla llegó a salir hacia Andrés en la semana 23 o
si esa fila es solo la intención de pedido. La hoja no lo distingue.)*

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
