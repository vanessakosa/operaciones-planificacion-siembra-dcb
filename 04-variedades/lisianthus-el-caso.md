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

| | |
|---|---|
| Semillas enviadas a germinar | ~27.000 *(Vanessa, de memoria — confirmar contra factura)* |
| Plantas trasplantadas | 12.728 |
| **Merma de plantulación** | **53 %** — 14.272 plantas |
| Tallos cosechados (ventana abierta) | 6.926 |
| **Tallos por planta observados** | **0,54** contra **2** esperados = **27 %** |

Ese 27 % es el precio del oidio, y coincide con la lectura de campo:

> *"La mitad se perdió en primera floración con oidio, porque teníamos que hacer
> labores culturales semanalmente. El oidio generó una mortalidad inicial
> importante y generó además una aplicación adicional de inputs. Pero eso
> tampoco canceló toda la producción."*

**Dos advertencias sobre ese 0,54.** La ventana sigue abierta —la segunda
floración está en curso— así que es un piso, no un resultado. Y el 53 % de merma
de plantulación es un costo **anterior** al campo: si se corrige, el mismo manejo
rinde el doble sin cambiar nada de la cama.

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
3. **Confirmar las 27.000 semillas** contra la factura del plantulador (Andrés).
4. **El costo del oidio** — aplicaciones adicionales y labores culturales
   semanales. `aplicaciones_historial.csv` tiene 16 filas y sólo una toca
   Lisianthus.
5. **Fin de cosecha** en las 21 siembras: 0 lo tienen anotado.
