# Cruce por ventana de siembra — de 0 % a 73 % de "Mix" prorrateado

```bash
python3 motor/cerebro.py rendimiento [grupo]   # marca AMBIGUO(n siembras) o "resuelta por fecha"
python3 motor/cerebro.py m2 [grupo]            # idem
python3 motor/cerebro.py prorratear [grupo]    # reparte "Mix" por tasa de corte
python3 motor/cerebro.py ciclos                # ciclo calculable: 37% -> 85%
```

> Construido en tres pasos, el 2026-08-13 y el 2026-08-14, a partir de cuatro
> preguntas de Vanessa: *"¿estás seguro que estás cruzando los tallos
> registrados con la ventana de cosecha... y los que están como Mix, por qué
> no los prorrateas?"* → *"prorratea como el 2, y ¿tienes forma de siempre
> cruzar con la ventana de siembra?"* → la que destrabó la fecha:
> *"Fecha a siembra a campo está vacío porque dejé de usarla, ahora trabajo
> solo con las semanas... ese dato sí está en todo."* → y la que cerró el
> método: *"recuerda que los fines de cosecha están en las notas, en los
> comentarios. Si no existe para prorratear, se divide entre las variedades
> sembradas de esa especie."*

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

## 4 · El resultado del paso 2, con la semana de siembra

| | Antes (`Fecha siembra campo`, 37 %) | Con semana de siembra (97 %) |
|---|---|---|
| `ciclos` — ciclo calculable | 111 de 302 (37 %) | **258 de 302 (85 %)** |
| `ciclos` — meses del año cubiertos | 6 de 12 | **12 de 12** |
| `prorratear` — tallos "Mix" resueltos | 0 de 24.475 (0 %) | 1.960 de 24.475 (8 %) |
| `m2`/`rendimiento` — lotes resueltos por fecha | 0 | 1 (Celosia Dreams Mix, bloque 2) |

El caso resuelto muestra por qué importa: Celosia "Dreams Mix" en el bloque 2
tenía dos siembras sumadas en **5.067 plantas**. Aislada la que estaba activa,
son **2.600** — el tallos/m² de ese lote **casi se duplica** (de 7,8 a 15,2),
porque antes estaba dividido entre plantas que no correspondían a ese corte.

## 5 · El paso 3 — fines de cosecha reales + partes iguales de respaldo

Con la semana de siembra, `prorratear` subió de 0 % a solo 8 %. Vanessa lo
resolvió con dos observaciones más:

> *"Recuerda que los fines de cosecha están en las notas, en los
> comentarios."*

Ya estaban extraídos: `cierres_lote.csv` trae `semana_cierre` para 29 de 36
lotes cerrados, sacado de los comentarios de CAMPO en una sesión anterior —
pero `_ventana_estimada()` todavía no lo usaba, solo estimaba el fin con la
duración genérica del ciclo. Ahora el cierre real **manda** sobre la
estimación: si existe, se usa esa fecha (ancla a la siembra de esa misma
fila, usando el domingo de la semana de cierre como el extremo más
generoso).

> *"Si no existe [ventana con la que prorratear] para prorratear, se divide
> entre las variedades sembradas de esa especie."*

Antes, cuando no se podía aislar quién estaba activo, el corte quedaba sin
prorratear. Ahora hay una escalera de tres métodos, del más al menos preciso
— y cada fila del CSV dice cuál se usó, para que un reparto por partes
iguales nunca se confunda con uno pesado por tasa real:

1. **`tasa`** — el principal: cultivares con ventana activa, ponderados por
   tasa de corte medida.
2. **`partes iguales entre activas (sin tasa)`** — se sabe quién estaba
   sembrado y activo, pero ningún cultivar tiene tasa medible.
3. **`partes iguales entre sembradas (sin ventana)`** — ni siquiera se pudo
   saber quién estaba activo esa fecha; se reparte entre todo lo que CAMPO
   registra sembrado de ese grupo en esa cama, sin filtrar por fecha.

### Resultado: de 8 % a 73 %

| Método | Tallos |
|---|---|
| `partes iguales entre activas (sin tasa)` | 10.535 |
| `partes iguales entre sembradas (sin ventana)` | 5.443 |
| `tasa` | 1.960 |
| **Prorrateados** | **17.938 (73 %)** |
| Sin prorratear — grupo nunca sembrado en esa cama según CAMPO | 6.537 (27 %) |

**Los 10.535 tallos del método 2 son exactamente Statice, Lisianthus, Zinnia
y Strawflower** — los cuatro grupos ya identificados como ciegos (0–6 % de
trazabilidad de cultivar). Se sabe qué cultivares estaban sembrados y
activos esa semana; lo que falta es la tasa, porque no existe un solo lote
limpio de esos grupos del que medirla. **Es el mismo bloqueo de siempre,
visto desde otro ángulo:** capturar cultivar ahí (bloqueo B1 del roadmap) no
solo permite elegir variedad — también sube esos 10.535 tallos del método 2
(partes iguales) al método 1 (tasa real), que es más preciso.

⚠️ **Léase el método antes de creer un número.** `mix_prorrateado.csv` mezcla
tres niveles de confianza en la misma columna `tallos_estimados`. Un reporte
que sume esa columna sin filtrar por `metodo` está tratando una estimación
gruesa igual que una medida.

## 6 · El efecto de temporada, con 258 filas en vez de 111

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

## 7 · Pendiente para decidir con Vanessa

`Inicio cosecha` está lleno el 90 % de las veces, pero siempre como nombre de
mes, nunca fecha exacta. Un segundo nivel de ventana basado en eso subiría
algo más la cobertura, pero exige inferir el año de un texto que no lo dice, y
una ventana de un mes entero solapa mucho más fácil entre siembras cercanas.
No se implementa sin decidirlo con ella primero.
