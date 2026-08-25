# Comportamiento de todas las variedades sembradas

> Análisis del 2026-08-13 cruzando `registro_tallos.csv` (697 filas, 66.417
> tallos), `campo_siembras.csv` (302 siembras + 202 comentarios),
> `ciclos_variedad.csv`, `incidencia_fitosanitaria.csv`, `cierres_lote.csv`,
> `picos_cosecha.csv` y `desajuste_demanda.csv`.

---

## 🔴 Primero: el 41 % de la cosecha no se puede atribuir a una variedad

Antes de cualquier ranking hay que decir esto, porque **limita directamente la
pregunta de qué variedades eliminar.**

| Grupo | Tallos | Con cultivar | % |
|---|---|---|---|
| Boca de Dragón | 12.409 | 11.571 | **93 %** ✅ |
| **Statice** | **10.535** | **652** | **6 %** 🔴 |
| Gomphrena | 6.248 | 5.436 | 87 % ✅ |
| Celosia | 6.221 | 4.261 | 68 % 🟡 |
| **Lisianthus** | **5.657** | **0** | **0 %** 🔴 |
| **Zinnia** | **5.091** | **0** | **0 %** 🔴 |
| Green Ball | 3.751 | 3.751 | 100 % ✅ |
| Campanula | 3.403 | 3.044 | 89 % ✅ |
| Ammi | 2.562 | 2.562 | 100 % ✅ |
| Ammobium | 2.432 | 2.432 | 100 % ✅ |
| **Strawflower** | **1.872** | **0** | **0 %** 🔴 |
| **TOTAL** | **66.417** | **38.913** | **59 %** |

**23.155 tallos —el 35 % de todo lo cosechado— no tienen ni una letra de
variedad.** Entran como `Mix` o vacío.

### Qué significa en la práctica

**En Statice, Lisianthus, Zinnia y Strawflower no se puede decidir qué variedad
eliminar, porque no se sabe cuál produjo qué.** Statice es el segundo grupo del
cultivo y es prácticamente ciego: de 10.535 tallos, solo 652 dicen cultivar.

No es un problema de análisis — es de captura. Y en Celosia ya se identificó la
causa: **el desplegable de LISTAS ofrece una sola opción**. Vale la pena revisar
si pasa lo mismo con estos cuatro.

Ojo: en Celosia demostramos que a veces `Mix` **es la descripción correcta**
(camas intercaladas). La pregunta a hacerse en cada grupo es la de siempre:
**¿el cultivar es separable en esa cama, o no?**

---

## Ranking por volumen — semanas 22 a 33

| # | Grupo | Tallos | Reg | Sem | Ciclo bit. | Ventana |
|---|---|---|---|---|---|---|
| 1 | Boca de Dragón | 12.409 | 149 | 12 | 9–12 | 2–3 |
| 2 | Statice | 10.535 | 81 | 12 | 13–15 | 4–8 |
| 3 | Gomphrena | 6.248 | 40 | 11 | 13–15 | 3–6 |
| 4 | Celosia | 6.221 | 54 | 9 | 14 | 3–4 |
| 5 | Lisianthus | 5.657 | 33 | 9 | **19–23** | 4–6 |
| 6 | Zinnia | 5.091 | 45 | 10 | 12 | 4 |
| 7 | Green Ball | 3.751 | 34 | 11 | 13 | 3 |
| 8 | Campanula | 3.403 | 61 | 8 | 12–13 | 2–3 |
| 9 | Ammi | 2.562 | 46 | 11 | 12 | 4 |
| 10 | Ammobium | 2.432 | 29 | 10 | 13 | 3 |

**Los cuatro primeros son el 54 % de la cosecha.**

---

## Productividad medida — solo 44 lotes de 139 tienen denominador limpio

Ventanas cerradas, por lo tanto **tallos/planta es el número que manda**:

| Grupo | Cultivar | Cama | Plantas | Tallos | T/planta |
|---|---|---|---|---|---|
| **Green Ball** | Punky Ball | 4a | 945 | 2.605 | **2,76** |
| **Gomphrena** | Quis Sequin | 3a | 735 | 1.497 | **2,04** |
| Gomphrena | Quis Carmine | 3a | 2.785 | 3.179 | 1,14 |
| Campanula | Champion White | 3b | 1.370 | 1.490 | 1,09 |
| Boca de Dragón | Opus Fresh | 4a | 864 | 650 | 0,75 |
| Girasol | Pro Cut White | 4a | 800 | 563 | 0,70 |
| Campanula | Champion Lavender | 3b | 1.918 | 1.231 | 0,64 |
| Celosia | Cristata Verda Green | 3a | 3.134 | 1.083 | 0,35 |

**Green Ball con pinch da 2,76 contra 1 documentado sin pinch.** Es el hallazgo
de manejo más rentable medido hasta hoy, y el comentario de esa cama lo confirma:
*"esta sí recibió pinch"*.

---

## Riesgo fitosanitario — dónde se concentra el daño

| Grupo | Eventos | Cierres sanitarios |
|---|---|---|
| **Lisianthus** | **15** | — |
| **Matricaria** | **8** | **2** (mosca blanca) |
| Statice | 5 | 2 (hongos) |
| Gomphrena | 2 | — |
| Limonium | 1 | 1 + 1 pérdida total |

**Lisianthus concentra el 44 % de todos los eventos fitosanitarios registrados.**
Y es además el de ciclo más largo (19–23 semanas): **ocupa la cama el doble que
casi todo lo demás y es el que más se enferma.**

Una sola variedad salió resistente y está dicho textualmente:

> **Megalo I Yellow** — *"primera en florecer. Esta variedad le fue bien, elongó,
> y hoy cosechamos unos 10 tallos. **Buena resiliencia**."*

**Ese es el dato de selección varietal más valioso del archivo** — y está en un
comentario, no en una columna.

---

## Diagnóstico por grupo

### 🟢 Boca de Dragón — el pilar, y el único donde SÍ se puede decidir

12.409 tallos, **93 % trazable**. Aquí sí hay base para seleccionar.

Lo que dicen los datos y los comentarios:

- **Monaco Orange:** *"ESPECTACULAR… muy concentrada la cosecha en una semana"*,
  *"sale toda al tiempo"* → sirve para **golpear un pico comercial**
- **Monaco Plumblossom:** *"va aperturando en fases"* → sirve para **sostener
  carrito semanal**. Pero perdió >50 % por malla y desyerbe tardíos
- **Monaco Dark Pink:** *"tallos extraordinarios con cabezas gruesas… **no tengo
  a quién vendérselo**"* → problema de venta, no de campo
- **Opus Fresh:** mejor productividad medida del grupo (0,75) y **falta blanco**:
  *"es lo mínimo semanal para condolencias"*
- **Potomac Early:** *"tallos de menor calidad y más variabilidad"* — jerarquía
  ya confirmada: Monaco/Opus > Potomac

**Conclusión: subir Opus Fresh (blanco, escaso y buen rendimiento), bajar Monaco
Dark Pink (sobra), mantener Monaco Orange para picos y Plumblossom para
continuidad.**

### 🔴 Statice — segundo del cultivo y ciego

10.535 tallos con **6 % de trazabilidad**. Botrytis recurrente con patrón
documentado (*"colapso sem 15+"*, *"son un cementerio"*). Ventana larga (4–8 sem)
que es su mayor virtud.

**No se puede seleccionar nada aquí hasta capturar el cultivar.** Es la
intervención de mayor retorno de todo el análisis: es el grupo #2 y no sabemos
qué variedad lo sostiene.

### 🔴 Lisianthus — el más caro y el más frágil

- Ciclo **19–23 semanas**: ocupa cama el doble que el resto
- **15 eventos fitosanitarios**, el 44 % del total
- **0 % de trazabilidad** en 5.657 tallos
- Ventana comprometida por salinidad: *"formación temprana de botón con tallos
  más cortos y delgados"*

**Es el candidato número uno a revisión estratégica.** Ocupa mucho, se enferma
mucho, y no sabemos cuál de sus 11 variedades vale la pena. Lo único sólido es
que **Megalo I Yellow resistió**.

### 🟡 Zinnia — produce bien lo que no se vende

5.091 tallos, **0 % trazable**, y **cinco lotes en pico simultáneo la semana 28**
con *"más de lo que se puede vender"*. Un lote se cerró por espacio *"aún estaban
produciendo"*.

**No es problema de rendimiento: es de escalonamiento y de mezcla.** Candidata a
**reducir área y escalonar**, no a eliminar.

### 🟢 Green Ball — la estrella medida

100 % trazable, **2,76 t/planta con pinch**. Sin problemas fitosanitarios
registrados. **Candidata a aumentar**, y el pinch a extenderse a otros grupos.

### 🟢 Gomphrena — excelente en campo, sobra en venta

87 % trazable. Quis Sequin **2,04 t/planta**, Quis Carmine 1,14 con ventana larga
(*"la más versátil"*). Pero: *"mucha producción para lo que vendemos"*.

**Buena variedad, mal dimensionada.**

### 🟡 Campanula — pierde en sala, no en campo

89 % trazable. **Dos camas cerradas por vida en florero**: *"sacrificada sem27
por problemas de florero al final de la ventana"*.

Champion White 1,09 t/planta contra Lavender 0,64 — **ambas ventanas cerradas, así
que aquí la blanca sí gana.** El caso original (0,64 vs 0,92) no era comparable
porque la lavanda seguía abierta.

### 🔴 Matricaria — riesgo alto para su volumen

Solo 1.460 tallos pero **8 eventos y 2 cierres sanitarios por mosca blanca**.
Regla vigente: **nunca Vegmo Single en Inv 5 ni 3C**, y drench de pre-siembra
obligatorio con Beauveria o Paecilomyces.

### 🟡 Ammobium — se devuelve

100 % trazable, pero: *"demasiada cantidad de flor para la que piden"* y
*"**muchas devoluciones y pérdidas en carritos**. Pudrición de parte baja de
tallos"*. Además techo confirmado: 4.600 plantas fue demasiado, ideal 2.500–3.000.

---

## Lo que este análisis NO puede responder

| Pregunta | Bloqueada por |
|---|---|
| ¿Cuál variedad deja más margen? | `costos_productos.csv` **vacío** |
| ¿Cuál da tallo más largo / vendible? | `calidad_tallo.csv` **vacío** |
| ¿Cuál rota más rápido en punto de venta? | **no existe archivo de ventas** |
| ¿Cuál se devuelve más? | solo frases sueltas en comentarios |
| ¿Cuál dura más en florero? | `vida_en_vaso.csv` **1 fila** |
| ¿Cuál aporta más al bouquet? | `combinaciones_venta.csv` **2 filas** |

**Hoy se puede rankear por tallos, ciclo, riesgo fitosanitario y ajuste con la
demanda. No por rentabilidad ni por desempeño en venta.**

---

## Las cinco acciones que salen de este análisis

1. **Capturar cultivar en Statice, Lisianthus, Zinnia y Strawflower.** Desbloquea
   el 35 % de la cosecha. Revisar primero si el desplegable ofrece opciones —
   como pasó en Celosia.
2. **Revisión estratégica de Lisianthus.** Ciclo doble, 44 % de los eventos
   fitosanitarios, cero trazabilidad. Empezar por confirmar Megalo I Yellow.
3. **Escalonar Zinnia.** Cinco camas a pico la misma semana es calendario, no
   cultivo.
4. **Extender el pinch de Green Ball.** 2,76 contra 1 documentado.
5. **Subir blanco, bajar rosado.** Opus Fresh escasea para condolencias mientras
   Monaco Dark Pink no tiene comprador.
