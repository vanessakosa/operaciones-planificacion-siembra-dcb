# Cruce por ventana de siembra — de 0 % a 8 % de "Mix" prorrateado

```bash
python3 motor/cerebro.py rendimiento [grupo]   # marca AMBIGUO(n siembras) o "resuelta por fecha"
python3 motor/cerebro.py m2 [grupo]            # idem
python3 motor/cerebro.py prorratear [grupo]    # reparte "Mix" por tasa de corte
python3 motor/cerebro.py ciclos                # ciclo calculable: 37% -> 85%
```

> Construido en dos pasos, el 2026-08-13 y el 2026-08-14, a partir de tres
> preguntas de Vanessa: *"¿estás seguro que estás cruzando los tallos
> registrados con la ventana de cosecha... y los que están como Mix, por qué
> no los prorrateas?"* → *"prorratea como el 2, y ¿tienes forma de siempre
> cruzar con la ventana de siembra?"* → y la que destrabó todo:
> *"Fecha a siembra a campo está vacío porque dejé de usarla, ahora trabajo
> solo con las semanas... la columna que sigue es la semana que se
> trasplantó... ese dato sí está en todo."*

---

## 1 · El bug real que la primera pregunta encontró

`_plantas_del_lote()` cruzaba **grupo + cultivar + bloque**, sin mirar fechas.
Si el mismo cultivar se sembraba dos veces en el mismo bloque, las plantas de
las dos siembras se sumaban sin poder saber cuál produjo el corte.

No era teórico. Boca de Dragón, bloque 3B:

| Fecha de siembra | Variedad en CAMPO | Plantas |
|---|---|---|
| 2025-11-20 | Snapdragon Potomac early pink | 2.880 |
| *(sin fecha)* | Snapdragon Potomac Appleblossom | 3.014 |

Las dos homologan a **Potomac Appleblossom**. El motor sumaba **5.894
plantas** — el número exacto que aparecía como denominador del corte "Mix" de
esa cama.

## 2 · Qué se construyó para arreglarlo

**`_ventana_estimada()`** — la ventana de cosecha de UNA siembra puntual:
`fecha de siembra + semanas a campo (ciclos_variedad.csv) + duración de la
ventana`. Sin fecha, o sin ningún dato de semanas a campo, no hay ventana —
`(None, None)`, nunca un número inventado.

**`_plantas_del_lote()` reescrito** — cuando dos o más siembras del mismo
cultivar+bloque coinciden:

1. Si se puede aislar **exactamente una** siembra cuya ventana contiene la
   fecha del corte → se usa **solo esa**, marcado `resuelta por fecha`.
2. Si no —falta una fecha, o dos ventanas se solapan— se sigue sumando **para
   no perder tallos**, pero marcado `AMBIGUO(n siembras)`. Antes esto pasaba
   en silencio.

**`prorratear`** — comando nuevo. Reparte cada corte "Mix" de una sola cama
entre los cultivares con ventana activa esa fecha, ponderado por su **tasa de
corte limpia** (tallos/planta/día medida en lotes sin ninguna marca de
advertencia). Nunca por partes iguales, nunca por plantas a secas. Es una
**ESTIMACIÓN** — regla 1 del `CLAUDE.md` — vive en `07-datos/mix_prorrateado.csv`,
nunca sobreescribe `registro_tallos.csv`.

Con esto construido, la primera corrida dio **0 % prorrateado**: solo 37 % de
las siembras tenían `Fecha siembra campo`, y de los 136 cortes "Mix" de una
sola cama, 107 tenían candidatos sin ninguna fecha. El mecanismo estaba bien
construido; el dato de entrada no alcanzaba.

## 3 · El desbloqueo — la columna correcta no era la que se estaba usando

Vanessa lo explicó al ver el 0 %: **dejó de usar `Fecha siembra campo`**. Hoy
trabaja **por semana**, en la columna que va justo al lado — *"a veces se
sembró en dos días distintos [de la misma semana], y proyectamos todo por
semana."*

Esa columna se llama **también** "Semana" — el archivo tiene **dos** columnas
con ese nombre (la otra es la semana de inicio de cosecha, más adelante). Un
lector genérico basado en `csv.DictReader` colapsa encabezados duplicados y se
queda solo con el último, así que el motor **nunca había podido ver esta
columna**, aunque estuviera ahí desde siempre.

Comprobado por posición: está llena en **294 de 302 filas — 97 %**, contra 37 %
de la fecha exacta.

**`_leer_semanas_siembra()`** — lee esa columna por posición (no por nombre),
y le asigna el año por secuencia: las 302 filas son un log cronológico que
cruza de diciembre a enero una vez; una caída grande en el número de semana
(más de 26) es ese cruce, no un error de tipeo. Se validó contra las pocas
filas que sí tienen fecha exacta: 102 de 111 coinciden exacto, 9 difieren por
1 semana (jitter normal del dictado, no afecta el año).

**`_fecha_siembra_estim()`** — usa el **lunes de esa semana ISO** como fecha
estimada. Es una aproximación de hasta 6 días, aceptable para construir una
ventana medida en semanas. La fecha exacta queda de respaldo para las pocas
filas que todavía la traen.

## 4 · El resultado, en las tres funciones que usan fecha de siembra

| | Antes (`Fecha siembra campo`, 37 %) | Ahora (semana de siembra, 97 %) |
|---|---|---|
| `ciclos` — ciclo calculable | 111 de 302 (37 %) | **258 de 302 (85 %)** |
| `ciclos` — meses del año cubiertos | 6 de 12 | **12 de 12** |
| `prorratear` — tallos "Mix" resueltos | 0 de 24.475 (0 %) | **1.960 de 24.475 (8 %)** |
| `m2`/`rendimiento` — lotes resueltos por fecha | 0 | 1 (Celosia Dreams Mix, bloque 2) |

El caso resuelto muestra por qué importa: Celosia "Dreams Mix" en el bloque 2
tenía dos siembras sumadas en **5.067 plantas**. Aislada la que estaba activa,
son **2.600** — el tallos/m² de ese lote **casi se duplica** (de 7,8 a 15,2),
porque antes estaba dividido entre plantas que no correspondían a ese corte.

### Por qué el prorrateo sigue en 8 % y no más

De los 24.475 tallos "Mix":

| Motivo | Tallos |
|---|---|
| Ninguna siembra con ventana activa esa fecha | 11.980 |
| Sin tasa de corte conocida para el cultivar activo | 10.535 |
| **Prorrateados** | **1.960** |

El segundo motivo (10.535 tallos) **coincide con los cuatro grupos ya
identificados como ciegos**: Statice, Lisianthus, Zinnia y Strawflower no
tienen ni una tasa calculable, ni siquiera a nivel de grupo — no existe un
solo lote limpio (cultivar identificado, sin marcas) del que medirla, porque
son justo los grupos con 0–6 % de trazabilidad de cultivar.

**Es el mismo bloqueo de siempre, visto desde otro ángulo:** capturar
cultivar en esos cuatro grupos (bloqueo B1 del roadmap) no solo permitiría
elegir variedades — también desbloquea el prorrateo de sus propios cortes
"Mix", porque hoy no hay con qué medirles una tasa de corte.

## 5 · El efecto de temporada, con 258 filas en vez de 111

`cerebro.py ciclos` también usa esta fecha. Con más que el doble de datos:

| Temporada | n | Ciclo medio |
|---|---|---|
| SECA | 84 (antes 35) | 13.4 sem |
| LLUVIA | 174 (antes 76) | 15.4 sem |

La diferencia observada subió de 0.7 a **2.0 semanas**, pero el ruido de medir
la cosecha por mes (no por fecha) sigue en **4.2 semanas** — el doble. Todavía
no se puede afirmar que la temporada mueva el ciclo, pero la brecha se cerró
a la mitad. El cuello de botella se movió de la siembra a la cosecha —
detalle en `05-programacion/04-como-predecir-ciclos.md`.

## 6 · Pendiente para decidir con Vanessa

`Inicio cosecha` está lleno el 90 % de las veces, pero siempre como nombre de
mes, nunca fecha exacta. Un segundo nivel de ventana basado en eso subiría
algo más la cobertura, pero exige inferir el año de un texto que no lo dice, y
una ventana de un mes entero solapa mucho más fácil entre siembras cercanas.
No se implementa sin decidirlo con ella primero.
