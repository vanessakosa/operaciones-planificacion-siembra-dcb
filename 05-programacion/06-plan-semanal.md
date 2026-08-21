# Plan semanal de campo — SEMANA ISO 33 (10–16 ago 2026)

> Documento vivo: se sobreescribe cada semana. El histórico está en git.
> Generado el 2026-08-13 contra `registro_tallos.csv` (corte 12/08),
> `campo_siembras.csv`, `aplicaciones_historial.csv` (corte **sem 27**) y los
> protocolos de `02-nutricion/` y `01-infraestructura/`.

---

## 🔴 Tres cosas con fecha, primero que todo

### 1. La fórmula de endurecimiento de Dusty Miller se activa ESTA SEMANA

`02-nutricion/01-fertirriego-formulas.md` dice:

> *"**Estado: no activa todavía.** El grupo de ensayo Ball vs. Andrés llega a
> semana 18 alrededor de la **semana ISO 33**."*

**Estamos en la 33.** Toca activarla:

| Producto | Dosis / tanque 2.000 L |
|---|---|
| Haifa N-Cal GG | 800 g |
| Polyfeed 10-10-43 | 700 g |
| Bitter Mag 16MgO | 600 g |
| **Haifa MKP** | **60 g** ← única fórmula donde sobrevive |
| Haifa Micro Hydroponic | 180 g |
| Fullfert | 100 cc |

Ojo a la inversión respecto a las demás fórmulas: aquí el **N-Cal baja** (800 vs
1.400) y el **Polyfeed sube** (700 vs 400). Es deliberado — se busca lignificar,
no seguir creciendo. **Confirmar antes de pasarla a Alexander.**

Y recordar la regla #5: al operario se le da el **número total de tanques**, no
la concentración.

### 2. La prevención de mosca blanca de Matricaria en Inv 5 está VENCIDA

Comentario de `Matricaria Single Vegmo [Inv 5]` en CAMPO:

> *"Amarillamiento inferior — patrón Inv 5. **Preventivo mosca blanca
> OBLIGATORIO sem 28-30**."*

**Estamos en la 33 y el historial de aplicaciones no llega más allá de la 27**,
así que no puedo confirmar si se hizo. Si no se hizo, son **3 semanas de
retraso** sobre una ventana marcada obligatoria — en el bloque que ya tiene
inóculo de mosca blanca en suelo y donde ya se perdieron dos lotes.

**Esto se verifica hoy, no la próxima semana.**

### 3. La decisión del ensayo Dusty Miller Ball vs Andrés es en la sem 35

> *"Sem24 TRIAL: Ball Colombia (plateado) vs Andrés (más verde, inferior calidad
> origen). Sin foliar permitido. Laterales no evaluables aún. **Decisión sem 35**."*

Faltan **dos semanas**. Para decidir con dato y no con impresión hay que medir
ahora: longitud de tallo central, laterales aprovechables y color. Hoy
`calidad_tallo.csv` está vacío, así que **si no se mide esta semana, la decisión
de la 35 se toma a ojo.**

---

## Productividad — semanas 28 a 33

| Semana | Tallos | Los cinco de mayor volumen |
|---|---|---|
| 28 | 5.110 | Statice 1.805 · Bocas 968 · Zinnia 570 · Lisianthus 420 |
| 29 | **7.027** | Statice 1.461 · Bocas 1.222 · Celosia 1.100 · Lisianthus 980 |
| 30 | 5.316 | Celosia 1.230 · Bocas 820 · Lisianthus 810 · Statice 755 |
| 31 | 6.670 | Bocas 1.313 · Statice 1.275 · Lisianthus 1.050 · Green Ball 715 |
| 32 | **7.091** | Statice 1.706 · Celosia 1.330 · Lisianthus 1.155 · Bocas 840 |
| 33 | 3.690 | Celosia 967 · Bocas 565 · Statice 480 · Lisianthus 330 |

**La semana 33 NO es comparable:** solo tiene 3 días registrados (10, 11 y 12).
A ritmo de la 32 debería cerrar cerca de 7.000. Se confirma el lunes.

**Lectura de las seis semanas:** el volumen es estable entre 5.100 y 7.100, sin
tendencia de caída. Los cuatro pilares son **Statice, Bocas, Celosia y
Lisianthus** — entre los cuatro sostienen más de la mitad de cada semana.

### Los 44 lotes con productividad medida limpia

Ventanas **cerradas** — aquí el número que manda es tallos/planta, no por día:

| Grupo | Variedad | Cama | Plantas | Tallos | T/planta |
|---|---|---|---|---|---|
| Green Ball | Punky Ball | 4a | 945 | 2.605 | **2,76** |
| Gomphrena | Quis Sequin | 3a | 735 | 1.497 | **2,04** |
| Gomphrena | Quis Carmine | 3a | 2.785 | 3.179 | 1,14 |
| Campanula | Champion White | 3b | 1.370 | 1.490 | 1,09 |
| Boca de Dragón | Opus Fresh | 4a | 864 | 650 | 0,75 |
| Girasol | Pro Cut White | 4a | 800 | 563 | 0,70 |
| Campanula | Champion Lavender | 3b | 1.918 | 1.231 | 0,64 |
| Celosia | Cristata Verda Green | 3a | 3.134 | 1.083 | 0,35 |

**Green Ball con 2,76 t/planta valida el pinch.** `ciclos_variedad.csv` dice 1
tallo/planta sin pinch, y el comentario de esa cama dice *"esta sí recibió
pinch"*. **Está dando casi 3×** — es el hallazgo de manejo más rentable que hay
medido hoy, y debería extenderse.

---

## Programa fitosanitario — 🔴 NO SE PUEDE GENERAR

**El historial de aplicaciones se corta en la semana 27 y estamos en la 33.**
Faltan seis semanas.

La regla de `dcb-fitosanidad` es explícita y es correcta: sin historial real, una
rotación puede repetir un producto recién aplicado y romper la disciplina
anti-resistencia. **Una rotación mal fundamentada es peor que ninguna.**

Lo último documentado:

| Fecha | Sem | Bomba | Productos |
|---|---|---|---|
| 03/07 | 27 | Choque Botrytis+Oidio | Neofat · Equifun · Hevea beta · Glukoplant · ADNGard |
| 04/07 | 27 | Prefloración | Glukoplant · Starzyme · Regalia · Solar · **No Fly** · Neofat |
| 05/07 | 27 | Vegetativo | Naturmix-L · Equifun · Amicos MC · ADN Green · Neofat |

**Para desbloquear:** traer `APLICACIONES` de `DCB_Maestro_Campo_2026.xlsx`
actualizado, o dictar bloque por bloque qué se aplicó desde la semana 28.

Lo que sí se puede decir sin historial, porque son reglas fijas:

- **Fungicidas 3–4 pm, nunca en la mañana.** A las 7 am el tejido lleva la noche
  húmedo y las esporas ya entraron.
- **Limpieza física antes de cualquier fungicida** en brote activo — bolsas
  fuera del invernadero.
- **El fertirriego no se suspende por presión fúngica.**
- Toda bomba lleva los cuatro componentes: fungicida + insecticida +
  bioestimulante + nutricional.

---

## Fertirriego — revisión

Las fórmulas están completas y confirmadas para Inv 3 y Inv 4+5 en vegetativo y
floración. Tres cosas que sí hay que atender:

**1. Falta la fórmula B (Prefloración, sem 7–9) con dosis explícitas.** Hoy solo
está descrita cualitativamente — *"Polyfeed sube, N-Cal baja levemente"* — y eso
**no se le puede entregar a un operario.** Es el hueco más operativo del
documento.

**2. La advertencia de Lisianthus sigue vigente y es importante.** El ciclo bajó
de 23 a 12–15 semanas con el fertirriego actual, pero:

> *"el exceso de salinidad compromete la inmunidad: causa formación temprana de
> botón con tallos más cortos y delgados."*

Y el comentario de campo lo confirma: **11 lotes de Lisianthus con mortalidad por
fusarium**, y solo uno resistente (`Megalo I Yellow`, *"buena resiliencia"*).
**En un cultivo que busca el tallo extraordinario, acelerar el ciclo no es un
logro si el tallo sale delgado.**

**3. Regla no negociable que conviene repetir:** Haifa Micro Hydroponic **siempre
180 g** por déficit de Cu, y **MKP = 0** en todos los bloques salvo el
endurecimiento de Dusty Miller.

---

## Preparación de camas — revisión

El protocolo está bien resuelto por bloque. Lo que hay que ejecutar y vigilar:

| Bloque | Protocolo | Estado |
|---|---|---|
| Inv 4 | No-Dig completo | Suelo excelente |
| Inv 5 | No-Dig parcial, horquilla 5 cm | **Resolver agua antes de intensificar** |
| Inv 3A | Horquilla 10 cm | Celosia necesita arranque |
| Inv 3B | Horquilla 10–15 cm solo en la barriga | Compactación + salinidad confirmadas |

**Dos reglas que salieron de los comentarios de campo y no estaban en este
documento:**

> *"REGLA: malla y desyerbe **antes de sem 4 post-trasplante**"* — de la pérdida
> >50 % de Monaco Plumblossom por tallos torcidos irrecuperables.
>
> *"Cama post-lisianthus **depletó calcio**. Próximo ciclo: yeso agrícola
> 200–300 g/m² + Glukoplant sem 5–8 obligatorio"* — de Cannes Pink con tallos
> delgados.

La segunda ya está parcialmente en el protocolo de camas con historial largo de
lisianthus. **La primera no está en ninguna parte y costó media cama.**

**El mulch plástico es la palanca económica más grande abierta:** meta de bajar
de 6 a 4 operarios fijos, ~$3,6–4,4 M COP/mes. La referencia real para evaluarlo
es la próxima cama de Inv 4 que se desocupe.

---

## Selección de variedades — lo que se puede evaluar hoy y lo que no

Pediste evaluar no solo productividad sino **aporte en sala, en buckets y en
ventas**. Ese cruce es el correcto y es exactamente el eje del proyecto. Estado
real de cada pata:

| Eje | Archivo | Estado |
|---|---|---|
| Productividad | `registro_tallos.csv` | ✅ 44 lotes medidos |
| Ciclo y ventana | `ciclos_variedad.csv` | ✅ 36 grupos |
| Desajuste con demanda | `desajuste_demanda.csv` | 🟡 13 registros |
| Comportamiento en seco | `secado_variedad.csv` | 🔴 **2 filas** |
| Vida en vaso / sala | `vida_en_vaso.csv` | 🔴 **1 fila** |
| Longitud de tallo | `calidad_tallo.csv` | 🔴 **vacío** |
| Costo y margen | `costos_productos.csv` | 🔴 **vacío** |

**Se puede rankear por tallos y por ciclo. No se puede rankear por rentabilidad
ni por aporte en sala**, porque cuatro de las siete patas están vacías o casi.

### Lo que sí dicen los datos hoy

**Sobra flor de lo que ya sobra:**

> Cinco lotes de Zinnia llegaron a pico la **misma semana 28** — *"muchísima
> producción, más de lo que se puede vender"*. Gomphrena Quis Carmine: *"mucha
> producción para lo que vendemos"*. Ammobium: *"demasiada cantidad de flor para
> la que piden"*. Monaco Dark Pink: *"tallos extraordinarios… **no tengo a quién
> vendérselo**"*.

**Y falta lo que falta:**

> Opus Fresh: *"poquita cantidad de blanco, es **lo mínimo semanal para
> condolencias**"*.

**El blanco escasea mientras el rosado y el naranja sobran.** Eso no es un
problema de rendimiento — es de mezcla de siembra, y es plata dejada en la mesa
en las dos direcciones.

**Tres variedades penalizadas en venta, no en campo:**

| Variedad | Problema | Cita |
|---|---|---|
| Campanula Champion Lavender | **Vida en vaso** | *"Sacrificada sem27 por problemas de florero al final de la ventana"* — cerró **dos** camas |
| Ammobium Alatum | Pudrición basal | *"muchas devoluciones y pérdidas en carritos"* |
| Larkspur / Nigella | Despetalado | *"se despetalaban en el carrito"* |

**Ese es justo el aporte en sala que quieres evaluar** — y las tres pierden ahí,
no en el campo. Una variedad que produce bien y se muere en el bucket es un costo
disfrazado de éxito.

---

## Plan de campo — semana 33

| # | Acción | Dónde | Por qué |
|---|---|---|---|
| 1 | **Verificar preventivo mosca blanca** | Inv 5 | Ventana obligatoria sem 28–30, hoy sin confirmar |
| 2 | **Activar fórmula de endurecimiento** | Dusty Miller | Llega a sem 18 esta semana |
| 3 | **Medir longitud y laterales del ensayo Dusty** | Inv 5 | Decisión Ball vs Andrés en sem 35 |
| 4 | Traer `APLICACIONES` desde sem 28 | — | Desbloquea todo el programa fitosanitario |
| 5 | Confirmar si Colitas de conejo sigue produciendo | Inv 2 | Último corte 11/08, ventana ambigua |
| 6 | Registrar la siembra de Espárrago en CAMPO | Inv 2 | Cosechando desde sem 33 sin fila de siembra |
| 7 | Anotar **cama exacta** de cada ensayo de Inv 2 | Inv 2 | Hoy dicen "2" a secas, y es el bloque más irregular |
| 8 | Extender el pinch de Green Ball | 4A → resto | 2,76 t/planta contra 1 documentado |

---

## Cómo va a funcionar esto cada semana

1. **Refrescar el registro** — bajar el XLSX y correr `importar_tallos.py`
2. **Correr el tablero** — `cerebro.py matriz` y `cerebro.py rendimiento`
3. **Leer los comentarios nuevos** de CAMPO: ahí está el porqué, no en las columnas
4. **Revisar vencimientos** — ventanas de prevención, ensayos con fecha de decisión
5. **Escribir el plan** y marcar lo que quedó bloqueado por falta de dato

**Lo que más rinde no es analizar mejor: es cerrar los cuatro archivos vacíos.**
Con `calidad_tallo` y `costos_productos` llenos, este plan pasa de contar tallos
a decidir plata — que es lo que pediste desde el principio.
