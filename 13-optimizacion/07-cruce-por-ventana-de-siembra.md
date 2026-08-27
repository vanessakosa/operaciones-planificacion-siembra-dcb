# Cruce por ventana de siembra — y por qué el prorrateo de "Mix" da 0 % hoy

```bash
python3 motor/cerebro.py rendimiento [grupo]   # ahora marca AMBIGUO(n siembras)
python3 motor/cerebro.py m2 [grupo]            # idem
python3 motor/cerebro.py prorratear [grupo]    # reparte "Mix" por tasa de corte
```

> Construido el 2026-08-13, a partir de dos preguntas de Vanessa: *"¿estás
> seguro que estás cruzando los tallos registrados con la ventana de cosecha
> de cada una... y los que están como Mix, por qué no los prorrateas según lo
> que estaba en cosecha esa semana?"* y *"prorratea como el 2, y ¿tienes forma
> de siempre cruzar con la ventana de siembra?"*

---

## 1 · El bug real que la pregunta encontró

Antes de esta sesión, `_plantas_del_lote()` cruzaba **grupo + cultivar +
bloque**, sin mirar fechas. Si el mismo cultivar se sembraba dos veces en el
mismo bloque, las plantas de las dos siembras se sumaban sin poder saber cuál
produjo el corte.

No era teórico. Estaba pasando en Boca de Dragón, bloque 3B:

| Fecha de siembra | Variedad en CAMPO | Plantas |
|---|---|---|
| 2025-11-20 | Snapdragon Potomac early pink | 2.880 |
| *(sin fecha)* | Snapdragon Potomac Appleblossom | 3.014 |

Las dos homologan a **Potomac Appleblossom**. El motor sumaba **5.894
plantas** — el número exacto que aparecía como denominador del corte "Mix" de
esa cama.

## 2 · Qué se construyó

**`_ventana_estimada()`** — la ventana de cosecha de UNA siembra puntual,
construida solo con datos ya confirmados: `fecha de siembra + semanas a campo
(ciclos_variedad.csv) + duración de la ventana`. Si falta la fecha, o el ciclo
no tiene ningún dato de semanas a campo, no hay ventana que construir —
devuelve `(None, None)`, nunca un número inventado.

**`_plantas_del_lote()` reescrito** — cuando dos o más siembras del mismo
cultivar+bloque coinciden:

1. Si **todas** tienen fecha de siembra y ciclo conocido, y **exactamente una**
   de sus ventanas estimadas contiene la fecha del corte → se usa **solo esa**,
   marcado `multi-siembra: resuelta por fecha`.
2. Si no se puede aislar una sola —falta una fecha, o dos ventanas se
   solapan— se sigue sumando **para no perder tallos**, pero marcado
   `AMBIGUO(n siembras)`. Antes esto pasaba en silencio; ahora se ve.

**`prorratear`** — comando nuevo. Reparte cada corte "Mix" de una sola cama
entre los cultivares con ventana estimada activa esa fecha, ponderado por su
**tasa de corte limpia** (tallos/planta/día, medida en lotes sin ninguna
marca de advertencia — la misma condición que usa el ranking de `m2`). Nunca
por partes iguales, nunca por cantidad de plantas a secas: dos cultivares con
las mismas plantas activas no cortan igual.

Es una **ESTIMACIÓN**, no un dato de cosecha real — regla 1 del `CLAUDE.md`.
Vive aparte en `07-datos/mix_prorrateado.csv`, nunca sobreescribe
`registro_tallos.csv`.

## 3 · La respuesta honesta a "¿siempre?"

**No.** Y hoy, en la práctica, **nunca** — el mecanismo está construido y
corre, pero el resultado sobre los datos actuales es:

| | |
|---|---|
| Tallos "Mix" en todo el cultivo | 24.475 |
| Prorrateados | **0 (0 %)** |
| Casos donde SÍ había un candidato con fecha, y esa fecha caía dentro de la ventana estimada del corte | **0 de 136** |

La razón no es el método: es el dato de entrada. `Fecha siembra campo` está
llena en solo **37 % de las siembras** (mismo número que ya reportaba
`cerebro.py ciclos`). De los 136 cortes "Mix" de una sola cama:

- **107** tienen candidatos en el bloque, pero **ninguno con fecha de
  siembra** — no hay ventana que construir para ninguno.
- **27** no tienen ningún candidato sembrado ahí según CAMPO.
- **2** tienen un candidato con fecha, pero su ventana estimada ya había
  cerrado antes del corte (la siembra de noviembre del ejemplo de arriba:
  para agosto ya llevaba meses sin producir).
- **0** resuelven limpio.

`Inicio cosecha` sí está lleno el 90 % de las veces, pero **siempre como
nombre de mes** ("MAYO", "NOVIEMBRE"), nunca como fecha exacta — no alcanza
para construir una ventana de día preciso, y usar solo el mes obligaría a
inferir el año, lo que puede fallar en silencio. No lo hice sin
confirmarlo con Vanessa primero.

**Lo que esto desbloquea, en el mismo lugar que ya estaba bloqueado:**
llenar `Fecha siembra campo` en CAMPO no solo mejora el cálculo de ciclos —
ahora también es la llave que le falta al prorrateo de "Mix" y a la
desambiguación de siembras repetidas. Es el mismo dato, dos usos.

## 4 · Lo que sí quedó mejor, aunque el prorrateo no corra todavía

- **El caso Potomac Appleblossom ya no se suma en silencio.** Sale marcado
  `AMBIGUO(2 siembras)` en `rendimiento` y `m2`. Se ve el problema aunque
  todavía no se pueda resolver.
- **15 lotes en todo el cultivo quedan marcados `AMBIGUO`** por esta razón —
  antes ninguno lo estaba, porque el cruce ni se intentaba.
- El mecanismo funciona: en cuanto una siembra tenga fecha registrada Y su
  ventana caiga limpio sobre un corte, se va a resolver solo, sin tocar el
  código de nuevo.

## 5 · Pendiente para decidir con Vanessa

¿Vale la pena un segundo nivel de ventana, más ancho, usando `Inicio cosecha`
en meses cuando falta la fecha exacta de siembra? Sube la cobertura (90 %
contra 37 %) pero exige inferir el año de un texto que no lo dice, y una
ventana de un mes entero solapa mucho más fácil entre siembras cercanas. No
se implementa sin decidirlo con ella primero.
