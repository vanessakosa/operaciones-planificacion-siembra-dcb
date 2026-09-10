# La cadencia de Green Ball — y por qué el registro no la puede calcular

```bash
python3 motor/cerebro.py cartera "Green Ball"
```

**Encargo de Vanessa (2026-09-10):** *"Green Ball debemos revisar lo que se sembró
versus lo que se ha cosechado, en las camas del 4A, que fueron las dos camas que
cosechamos, que se solaparon con la cama del 4B, para poder definir cuánto ha
sido la ventana de cosecha, los tallos, y contrastar con la programación si hay
que espaciar un poco más la siembra."*

Con la duda que ella misma planteó: **¿una cama al mes, o cada seis semanas?**

## Los tres lotes

| Fila CAMPO | Bloque | Plantas | Inicio cosecha | Comentario de campo |
|---|---|---|---|---|
| 156 | **4A** | 800 | JUNIO | *"Comenzando cosecha en semana 19 y 20. Esta semana tallos más bien delgados no tan chéveres"* |
| 195 | **4A** | 945 | JULIO/AGOSTO | *"Toca desyerbar por segunda vez. **Esta sí recibió pinch** hace 2 semanas"* |
| 240 | **4B** | 896 | SEPTIEMBRE | *"Plantas = capacidad de cama 4B (896), cama completa"* |

Capacidad nominal de 4A y 4B: **112 huecos × 8 líneas = 896 sitios cada una.**
Documentado para Green Ball: **ciclo 13 semanas · ventana 3 semanas · 1 tallo por
planta · 15 cm · desbrotar laterales.**

## Lo cosechado, semana por semana

| Bloque | Tallos | Semanas ISO con corte |
|---|---|---|
| **4A** | **2.605** | **26, 27, 28, 29, 30, 31, 32, 33 — ocho seguidas, sin un hueco** |
| `Inv4` (¿4A o 4B?) | 623 | 22, 23 |
| 3B | 228 | 23 |
| 4B | 105 | 25 |
| `4z` (error de tipeo) | 190 | 33 |

**Rendimiento de 4A:** 2.605 tallos sobre 1.745 plantas = **1,49 tallos/planta**.
Si los 623 de `Inv4` también fueran de 4A, sube a **1,85**. Contra **1 tallo por
planta documentado** — o sea que el pinch está entregando entre 50 % y 85 % más
de lo que dice la ficha.

## Por qué esto no contesta la pregunta

**El registro anota el BLOQUE, no la CAMA.** Los dos lotes de 4A se escriben
igual — `4A`, `Inv 4A`, `Inv4a`, `inv4a` — así que el `CLAVE_LOTE` de los dos es
`Green Ball|Punky Ball|4a` y **se fusionan en uno solo.**

Consecuencia: las ocho semanas seguidas de cosecha en 4A admiten **dos lecturas
que los datos no pueden separar:**

| Lectura | Qué implicaría |
|---|---|
| **A — Sucesión perfecta** | Cada cama duró ~4 semanas y entraron una detrás de la otra, sin solaparse. La cadencia habría estado **bien** |
| **B — Solapamiento** | Las dos estuvieron en cosecha al mismo tiempo. La cadencia estuvo **corta** |

Las dos producen exactamente la misma huella en el registro: 8 semanas continuas
de "4A". **Vanessa dice que se solaparon y que "perdemos un montón"** — y por la
jerarquía de verdad de este repositorio, su observación de campo manda sobre una
inferencia mía. Pero **el dato no lo demuestra ni lo puede demostrar.**

### Y hay 813 tallos que no se pueden ubicar

Los 623 de `Inv4` (¿4A o 4B?) más los 190 de `4z` (error de tipeo) son **813
tallos, el 22 % de todo el Green Ball del período**, sin cama asignable. Ese es el
costo concreto de registrar solo el bloque.

*(Aparte: los 105 tallos anotados en `4B` en la semana 25 contradicen su propia
ficha de CAMPO, que dice cosecha desde SEPTIEMBRE. Casi seguro es un `4A` mal
escrito.)*

## Lo que sí se puede recomendar hoy

La respuesta a *"¿al mes o cada seis semanas?"* se apoya en dos hechos duros:

1. **El pinch alarga y engorda la ventana.** 1,49–1,85 tallos/planta contra 1
   documentado no sale de la nada: sale de que la cama con pinch produce más
   tallos durante más tiempo. La ventana documentada de **3 semanas describe una
   cama sin pinch**, y las camas de hoy llevan pinch.
2. **La ventana observada es mayor que 3 semanas.** El lote de 3B lo dice:
   *"buenísimos tallos en semana 16, en semana 20 ya quedan tallos más pequeños,
   ya la semana que viene la sacamos"* — cuatro semanas de tallo bueno, más una de
   caída.

**Entonces: seis semanas, no un mes.** Con ventana real de 4–5 semanas y pinch,
una cadencia de 4 semanas deja las camas pisándose; una de 6 deja ~1 semana de
margen. Es la opción conservadora, y el costo de equivocarse hacia el lado corto
(dos camas en pico simultáneo, que es lo que Vanessa ya vivió) es mayor que el de
equivocarse hacia el largo (una semana sin Green Ball, que es un TOQUE y admite
respiro por diseño).

⚠️ **Es una recomendación, no una medición.** Queda como `¿4 o 6 semanas?` en
`07-datos/roles_cartera.csv` hasta que haya el dato de cama.

## Lo que cierra esto de verdad

**Anotar la cama en el registro de cosecha, no solo el bloque.** Hoy `4A` puede
ser cualquiera de dos camas de 896 sitios. Con la cama anotada:

- la ventana real por cama se mide en vez de estimarse
- el solapamiento se ve en la tabla, no depende de la memoria
- los 813 tallos huérfanos dejan de existir
- y el efecto del pinch se puede aislar, porque hoy una cama con pinch y otra sin
  pinch están sumadas en la misma cifra

Ya está anotado como pendiente para Inv 2 en el plan semanal (*"anotar cama
exacta de cada ensayo"*). **Esto lo extiende a 4A y 4B, que es donde ya costó
plata.**

Es el mismo patrón que apareció tres veces en la sesión del 2026-09-10: el dato
existe en el campo y se pierde en la captura. Ver
`05-programacion/07-desplegables-registro.md` y
`13-optimizacion/03-estrategia-de-surtido.md`.
