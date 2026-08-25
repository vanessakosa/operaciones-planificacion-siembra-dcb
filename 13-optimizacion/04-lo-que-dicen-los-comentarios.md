# Lo que dicen los COMENTARIOS de CAMPO

Barrido completo de los **202 comentarios** de `campo_siembras.csv`
(23.133 caracteres), hecho el 2026-08-13 a pedido de Vanessa:

> *"Los cierres están explicados sobre todo en los comentarios, para justamente
> tener info cualitativa de si se sacó porque se necesitaba la cama, porque se
> acabó la cosecha, y entender bien cuáles semanas son los picos."*

Salieron tres archivos consultables, **cada fila con la cita literal que la
sustenta** para que nada quede inventado:

| Archivo | Filas | Qué responde |
|---|---|---|
| `07-datos/cierres_lote.csv` | 36 | **Por qué** se cerró cada cama |
| `07-datos/picos_cosecha.csv` | 16 | En qué semana rinde de verdad |
| `07-datos/desajuste_demanda.csv` | 13 | Dónde sobró o faltó flor |

---

## 1. El 89 % de los cierres NO fue porque se acabara la cosecha

| Motivo | Lotes | |
|---|---|---|
| **demanda** — se cortó para un pico comercial | 6 | 17 % |
| **sanitario** — sacrificado por plaga u hongo | 5 | 14 % |
| **espacio** — se necesitaba la cama | 4 | 11 % |
| **pérdida total** | 4 | 11 % |
| **agotamiento** — se acabó de verdad | **4** | **11 %** |
| **temprano** — se sacó pudiendo aguantar más | 4 | 11 % |
| **calidad** — deformidad o vida en florero | 3 | 8 % |
| **tardío** — se pasó de punto | 3 | 8 % |
| **pérdida parcial** | 2 | 6 % |
| **rotación** — esperando salir otro lote | 1 | 3 % |

**Solo 4 de 36 lotes cerraron porque la planta dejó de producir.**

### Por qué esto invalida el cálculo de ventana

`cerebro.py rendimiento` mide la ventana como *primer corte → último corte*. Si
el 89 % de los lotes se cerró por una razón ajena a la planta, **esa ventana no
mide la variedad: mide una decisión de Vanessa.**

Los casos son explícitos:

> **Zinnia Aurora (Inv 5):** *"las sacamos en semana 24 para sembrar dusty.
> **aún estaban produciendo!**"*
>
> **Anémonas (3C):** *"**Aún sigue produciendo**, las trasplanté en semana 16
> por el espacio"*
>
> **Celosias Indian Summer (4):** *"**hubiésemos podido extender y engordar
> hasta la 20**, pero los usamos en madres"*
>
> **Ammobium Alatum (Inv 2):** *"tuvimos segunda floración en semana 13, 14, 15
> — ahí las saqué **porque necesitaba el espacio**"*

Los cuatro rinden por debajo de su potencial **en el papel**, y ninguno rindió
mal. Es el mismo sesgo que el caso Campanula Champion Lavender ya documentó,
pero mucho más extendido de lo que se creía.

---

## 2. El corte se desfasa sistemáticamente — y siempre alrededor de la sem 27

Siete lotes traen una nota de arrepentimiento de timing, todos en semanas 27–28:

**Se cortó una semana antes de tiempo** (4 lotes):
> *"Fin cosecha sem27. Flores de menor calidad, algunas en el piso.
> **Hubiesen aguantado 1 sem más**."* — Ammi Majus + Ammobium (4EXT), Ammobium
> Winged Everlasting (3 EXT), Ammobium Alatum (3A)
>
> *"Sem27 aún había flores pero maleza adelantada. Hubiesen aguantado 1 sem más
> de menor calidad."* — Gomphrena Sequin

**Se cortó una semana tarde** (3 lotes):
> *"Cama sacada sem28. **Ideal hubiese sido sacarla en sem27**."* — Snapdragon
> Monaco Orange (4A), Amaranto Green Tails (5), Amaranto Emerald Tails (3A)

**Que el error se concentre en las semanas 27–28 sugiere una causa común**, no
siete descuidos: probablemente presión de calendario o de mano de obra en esas
dos semanas. Vale la pena mirarlo — una semana de corte mal puesta cuesta
calidad en un lote entero.

---

## 3. Cinco lotes de Zinnia sobreproduciendo la misma semana

> *"Sem28 muchísima producción. **Más de lo que se puede vender**."*

| Lote | Bloque |
|---|---|
| Zinnia Benarys Giant Carmen Rose | 3AB |
| Zinnia Benary Giant Bright Pink | 4B |
| Zinnia Aurora, Bailarina, Benary | 4B |
| Zinnia Aurora | Inv 5 |
| Zinnia Ballerina | Inv 5 |

**Esto no es un problema de cultivo: es un problema de escalonamiento.** Cinco
camas de Zinnia en tres bloques llegaron a pico a la vez, y la flor sobró.

Es exactamente lo que el motor existe para prevenir — y la señal estaba escrita
en el archivo desde la semana 28.

Y no es solo Zinnia:

> **Gomphrena Quis Carmine:** *"mucha producción para lo que vendemos"*
> **Ammobium Alatum:** *"Demasiada cantidad de flor para la que piden"*
> **Snapdragon Monaco Dark Pink:** *"Tallos extraordinarios con cabezas gruesas.
> **No tengo a quién vendérselo**"*

Del otro lado, falta:

> **Snapdragon Opus Fresh (4):** *"Poquita cantidad de blanco, es lo mínimo
> semanal para condolencias etc"*

**El blanco escasea mientras el rosado y el naranja sobran.** Eso es una
decisión de mezcla de siembra, y está documentada en prosa desde hace semanas.

---

## 4. La vida en florero ya cerró camas

Dos lotes de Campanula Champion Lavender (3A y Inv 5):

> *"**Sacrificada sem27 por problemas de florero al final de la ventana**."*

No es un problema de campo: es de postcosecha, y **acortó la ventana útil de dos
camas**. `10-postcosecha/` y `vida_en_vaso.csv` tienen una sola fila de datos.
Este es el segundo caso documentado de una variedad cuya ventana comercial
termina antes que su ventana agronómica.

---

## 5. Fusarium en 11 lotes de Lisianthus, con el mismo texto

Once variedades de Lisianthus en Mini/3C/3B comparten comentario:

> *"En semana 20 segunda labor de desyerbe, **mucha mortalidad en campo por
> fusarium**"*

Solo una se salvó y está dicho:

> **Megalo I Yellow:** *"primera en florecer. Esta variedad le fue bien, elongó,
> y hoy cosechamos unos 10 tallos. **Buena resiliencia**."*

**Eso es un dato de resistencia varietal que no está en ninguna parte
estructurada del repositorio.**

---

## 6. Reglas que Vanessa ya escribió y nadie había recogido

> **Snapdragon Monaco Plumblossom:** *"PÉRDIDA >50 %. Desyerbe tardío + malla
> tarde = tallos torcidos irrecuperables. **REGLA: malla y desyerbe antes sem 4
> post-trasplante**."*
>
> **Snapdragon Monaco Orange:** *"Es **DEMASIADO importante la doble malla**
> para no perder tallos arqueados"*
>
> **Snapdragon Cannes Pink:** *"Tallos DELGADOS — **cama post-lisianthus depletó
> calcio**. Próximo ciclo: yeso agrícola 200-300 g/m² + Glukoplant sem 5-8
> obligatorio"*
>
> **Limonium Forever Happy:** *"**NO sembrar lisianthus ni campanula en estas
> camas inmediatamente** — ciclo biosupresor primero (gomphrena o matricaria)"*

Las cuatro son reglas de manejo formuladas, con su justificación. Ninguna estaba
en `09-procedimientos/` ni en `04-variedades/notas-campo.md`.

---

## 7. Diferencia de patrón de apertura — relevante para planificar

> **Monaco Orange:** *"**Sale toda al tiempo** a diferencia de Plumblossom"* ·
> *"muy concentrada la cosecha en una semana"*
>
> **Monaco Plumblossom:** *"**Va aperturando en fases** a diferencia de Monaco
> Naranja"*

Dos cultivares del mismo grupo con perfiles de entrega opuestos. **Uno sirve
para golpear un pico comercial; el otro para sostener un carrito semanal.** Esa
distinción no existe en `ciclos_variedad.csv`, que trata la ventana como un
bloque uniforme.

---

## Qué hacer con esto

1. **`cerebro.py rendimiento` debería leer `cierres_lote.csv`** y marcar los
   lotes cerrados por espacio, demanda o sanidad — hoy los cuenta como ventanas
   completas y subestima esas variedades.
2. **Escalonar Zinnia.** Cinco camas a pico la misma semana es un error de
   calendario, no de cultivo.
3. **Subir las cuatro reglas** del punto 6 a `09-procedimientos/`.
4. **Investigar la semana 27.** Siete lotes con el corte desfasado en la misma
   ventana de dos semanas no es coincidencia.

## La lección de método

**Ninguno de estos siete hallazgos requería medir nada nuevo.** Todos estaban
escritos, en prosa, dentro de un CSV que el motor ya leía — pero leía solo sus
columnas numéricas.

Las columnas dicen **qué** pasó. Los comentarios dicen **por qué**. Y sin el
porqué los números mienten en las dos direcciones: un cierre por demanda parece
agotamiento, y una pérdida por inducción parece precocidad.
