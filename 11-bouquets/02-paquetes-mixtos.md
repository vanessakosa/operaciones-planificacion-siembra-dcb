# Los tres escalones de producto — y cuál se está regalando

```bash
python3 motor/cerebro.py valor      # incluye la escalera medida
python3 motor/cerebro.py auditar
```

> Definido por Vanessa el 2026-08-13. Es la pieza que faltaba para saber **a
> qué producto se le aplica la regla de seis roles y a cuál no.**

---

## La definición

> *"Los bouquets suelen tener de todas las formas para tener armonía. Pero
> también hacemos paquetes mixtos, que pueden tener solo lineales por ejemplo
> pero en mezcla de colores o variedades. Esas son de menos valor que un
> bouquet, pero de mayor valor que el paquete sólido de una sola variedad y
> **nos hace únicos**."*

| Escalón | Qué es | Regla que se le aplica |
|---|---|---|
| **1 · Paquete sólido** | una sola variedad | coherencia: el nombre debe corresponder al contenido |
| **2 · Paquete mixto** | mezcla de color o variedad. **Puede ser todo lineal** | coherencia — **NO** la regla de seis roles |
| **3 · Bouquet / arreglo** | todas las formas, para armonía | **sí** la regla de seis roles (`RANGO_ESTRUCTURA`) |

La frase clave es *"pueden tener solo lineales"*. **Un paquete mixto que es 100 %
LINEA no está mal construido: está bien construido para lo que es.** El motor ya
distinguía paquete de arreglo; lo que faltaba era saber que el escalón del medio
existe y es deliberado.

### My Love queda recategorizado

`My Love` estaba cargado como `Bouquet`, y la auditoría lo marcaba con **cinco
roles fuera de rango** — FOCAL 0 %, RELLENO 0 %, TEXTURA 0 %, FOLLAJE 0 %, LINEA
63,6 %. Su receta es 3 bocas vino + 3 Monaco Plumblossom + 3-4 Campanula
Champion White + 1 Amaranto vino: **todo LINEA.**

Con la definición de arriba, eso no es un bouquet incompleto. Es exactamente el
paquete mixto que ella describe. **Recategorizado a `Paquete mixto`**, y la
auditoría deja de marcarlo. Si prefieres que siga siendo Bouquet, es un cambio de
una palabra en `formulas_productos_bouquets.csv`.

> Y sigue en pie lo de la sesión anterior: My Love es una **base de tallos**, no
> una receta fija. *"Otra versión puede ser con campánulas rosadas y bocas
> crimson y blancas."* Lo invariante es la estructura, no el color.

---

## 🔴 El escalón se está cobrando en tallos, no en precio

La escalera se puede medir con los precios que ya están cargados. Da dos
respuestas distintas según la unidad, y ahí está el hallazgo.

| Escalón | N | $/unidad (mediana) | $/tallo (mediana) |
|---|---|---|---|
| 1 · Paquete sólido | 12 | 45.000 | **4.333** |
| 2 · Paquete mixto | 7 | 55.000 | **4.231** |
| 3 · Bouquet / arreglo | 5 | 125.000 | **4.565** |

- **Por unidad la escalera se cumple:** 45.000 → 55.000 → 125.000.
- **Por tallo no se cumple:** 4.333 → 4.231 → 4.565. Es prácticamente plana, y
  el paquete mixto es **el más barato de los tres.**

**Las dos juntas dicen una sola cosa: un paquete mixto vale más porque lleva más
flor, no porque la mezcla se cobre.** El trabajo de mezclar —el que según tu
propia definición *"nos hace únicos"*— hoy sale gratis. Y no es neutro: son más
tallos propios, o sea más cama.

El caso más nítido es una de las combinaciones que nombraste como ganadora:

| Producto | $ | Tallos | $/tallo |
|---|---|---|---|
| Campanula (paquete) — sólido | 40.000 | 10 | 4.000 |
| **Paquete campanulas y bocas — mixto** | 45.000 | 10 | **4.500** |

Mismo número de tallos, **500 pesos de diferencia** por convertir un paquete
sólido en la combinación que mejor se vende. En el otro extremo, *Paquete
campánulas y larkspur* sí cobra la mezcla: **6.500 por tallo**, el más alto del
catálogo fuera de los arreglos grandes. **La misma casa cobra la mezcla 62 % más
en un producto que en otro, sin una razón visible.**

*(Precio de lista, no volumen vendido. Cuánto rota cada uno no se puede
responder: no existe archivo de ventas.)*

---

## Las combinaciones que nombraste

Cargadas en `07-datos/combinaciones_venta.csv`, marcadas como observación de
Vanessa y no como medición.

| Combinación | Resultado | Estado en el catálogo |
|---|---|---|
| **Gomphrena + Statice** | ganadora | ❌ **no existe como producto** |
| **Campanula + Boca de Dragón** | ganadora | ✅ *Paquete campanulas y bocas* — pero casi al precio del sólido |
| **Green Ball + Celosia plumosa** | no ganadora | no existe. Bien que no exista |

**La primera es la oportunidad más directa que sale de esta sesión: la
combinación que llamas ganadora no está en el catálogo.** Lo más cercano es
*Gomphrenas blancas (paquete)* — 4 Audrey White + 5 Statice Forever Happy a
45.000 — que ya es esa mezcla, pero se llama y se cobra como paquete de
gomphrenas.

Y encaja con lo que dice el campo: **Gomphrena rinde 44,5 t/m² y sobra**
(*"mucha producción para lo que vendemos"*), **Statice ocupa el 30 % de la finca
y entrega 4,9 t/m²**. Un producto que consuma las dos ataca los dos problemas a
la vez. Ver `13-optimizacion/06-tallos-por-m2.md`.

### El registro negativo vale tanto como los positivos

**Green Ball + Celosia plumosa es el primer `NO_GANADORA` del archivo.** Es lo
que evita repetir una colección que no funcionó — hoy eso solo vive en tu
memoria.

Una hipótesis, **marcada como hipótesis**: en `paleta_color.csv` las dos son
**TEXTURA**. La mezcla no aporta contraste de forma, así que se lee como un
paquete sólido más caro. Si se confirmara, sería una regla útil —*mezclar dos
del mismo rol no crea un mixto*— pero con un solo caso no es una regla, es una
corazonada.

---

## Lo que falta para responder tu pregunta de verdad

Preguntaste cuáles combinaciones son ganadoras **para armar las colecciones**.
Hoy se puede responder con tres cosas y **no** con la que decide:

| Se puede | No se puede |
|---|---|
| qué combinaciones existen en el catálogo | cuántas se vendieron |
| a qué precio por tallo se cobra cada una | cuántas se devolvieron |
| si la mezcla se está cobrando o no | qué semana rota cada una |
| cuánta cama cuesta cada componente | qué margen deja |

**Con cuatro columnas alcanza** — producto · semana · vendidos · devueltos — y
`combinaciones_venta.csv` deja de ser una lista de impresiones y pasa a ser un
ranking. Es el punto B4 de `08-roadmap/03-que-falta-en-la-arquitectura.md`, y es
el que convierte esta pregunta en algo contestable.

---

## Pendiente encontrado de paso

**`Paquete zinnias sunset` no lleva zinnias.** Su receta son 10 Green Ball
Punky Ball + 3 Statice Forever Happy — que es exactamente *Green ball (paquete)*
más statice. Tiene pinta de copia y pega en el archivo de recetas.

No lo corrijo porque no sé cuál de las dos cosas está mal, si el nombre o la
receta. `auditar` ahora lo reporta en su propia sección en vez de esconderlo
entre los signos de admiración.
