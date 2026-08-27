# Celosia — el grupo paraguas y sus tres subtipos

```bash
python3 motor/cerebro.py rendimiento Celosia
```

**`Celosia` es un paraguas correcto para reportar, pero la unidad de manejo es
el subtipo.** Lo confirmó Vanessa el 2026-08-13: *"Celosia es un grupo paraguas
correcto, pero deberíamos manejarlas cada una bien específicas — plumosas,
cristata, spicatas."*

No es una distinción cosmética. Los tres subtipos tienen densidad de siembra,
tallos por planta y rol en el bouquet **distintos**:

| Subtipo | Distancia | Tallos/planta | Rol típico |
|---|---|---|---|
| **cristata** (cresta) | 7,5 cm | **1** | FOCAL — la cabeza es la flor |
| **plumosa** (pluma) | 15 cm | **4** | TEXTURA |
| **spicata** (espiga) | — | — | TEXTURA |

Un error de subtipo no es un error de etiqueta: **cristata a 15 cm desperdicia
la mitad de la cama, y plumosa a 7,5 cm ahoga cuatro tallos por planta.**

## El mapeo — qué está confirmado y qué no

### Confirmado por Vanessa (2026-08-13)

**spicata:** `Dreams` · `Flamingo` · `Celway`

**plumosa:** `Shimmer` · y **todas las de Floret** — `Summer Sherbet` ·
`Rose Gold` · `Spun Sugar` · `Raspberry Lemonade` · `Glowing Embers`

> **En campo a la plumosa se le dice «plumas».** Vanessa lo confirmó el
> 2026-08-13 al dictar la receta de Dream Land. Es vocabulario operativo, igual
> que «Bunny Tails» para Colitas de conejo — conviene que el sistema lo
> reconozca para que un dictado no se pierda.

> **`Floret` es el proveedor de semilla, no un subtipo.** Pero todas las
> celosias que DCB compra a Floret son plumosas, así que en la práctica el
> prefijo funciona como atajo. Conviene no confundir las dos cosas: si algún día
> entra una cristata de Floret, el atajo deja de valer.

### Confirmado por dato — CAMPO escribe el subtipo en el nombre

**cristata:** `Verda Green` · `Indian Summer` · `Enda Rose` · `Reprise Velvet`
· `Reprise Orange` · `Clubs Cocktail` · `Chief Carmine`

Estos no se dedujeron del nombre corto: `campo_siembras.csv` los registra
completos, del tipo `Celosia Cristata Enda Rose`.

### ⚠️ SIN CONFIRMAR — y NO están sembradas

`Sunday` · `Sylphid`

**No se deducen del catálogo del proveedor.** La regla 8 del `CLAUDE.md` prohíbe
asignar por deducción y presentarlo como dato; aquí aplica igual aunque se trate
del subtipo y no del color.

> **Corrección (2026-08-13).** Una versión anterior de esta ficha decía que
> `Sunday` "sí está sembrada, tres lotes en 4A y uno en Inv 2". **Es falso.**
> Esos lotes se sembraron en **agosto de 2025** con inicio de cosecha en
> **octubre de 2025** — llevan casi un año cerrados. El error fue leer
> `campo_siembras.csv` como si fuera el estado actual del campo, cuando es un
> **log histórico que incluye lotes cerrados.** Vanessa lo corrigió: ninguna de
> las dos está sembrada hoy.
>
> **Regla para no repetirlo:** una fila de `campo_siembras.csv` **no significa
> "está en el campo"**. Hay que mirar su fecha de siembra y su inicio de cosecha
> antes de hablar en presente.

### 🆕 `Glowing Embers` — cultivar nuevo, sin registrar

Vanessa lo nombró como plumosa de Floret el 2026-08-13, pero **no aparece en
ningún archivo del repositorio**: ni siembra en `campo_siembras.csv`, ni color en
`paleta_color.csv`, ni cosecha en `registro_tallos.csv`. Falta pedir su siembra y
su color antes de que pueda entrar a una receta.

## Ciclo y ventana por subtipo

| Subtipo | Ciclo | Ventana | Fuente |
|---|---|---|---|
| cristata | 14 | 3 | `variedades_bitacora.csv` (PROGRAMACION dice ventana 1) |
| plumosa | 14 | 3–4 | `parametros_siembra.md` (PROGRAMACION dice 14/4 — coinciden) |
| **spicata** | **13–15** | **2–3** | Derivado: PROGRAMACION `Celway 13/2` y `Flamingo 15/2`, bitácora `Purple Flamingo 15/3` |

El rango de spicata sale de **tres cultivares nombrados**, no de un promedio
inventado. Cuando haya cosecha suficiente por subtipo, se reemplaza por el
observado.

## Lo cosechado hasta hoy (2026-08-13)

6.221 tallos en 54 registros:

| Serie en el registro | Tallos | Bloques | Subtipo |
|---|---|---|---|
| Mix | 1.960 | 3a, Inv3a | **plumosa** ✅ |
| Cristata Verda Green | 1.264 | Inv3a, Inv 3A, Inv 4B, Inv5 | cristata ✅ |
| Shimmer Mix | 1.210 | Inv3a, Inv3b, 3a | **plumosa** ✅ |
| Dreams Mix | 890 | Inv2, 2 | spicata ✅ |
| Summer Sherbet | 830 | Inv3b, Inv3a | **plumosa** ✅ |
| Enda Rose | 67 | 3a | cristata ✅ |

**Todo lo cosechado queda atribuido por subtipo:**

| Subtipo | Tallos | % |
|---|---|---|
| plumosa | 4.000 | 64 % |
| cristata | 1.331 | 21 % |
| spicata | 890 | 14 % |

### La `Mix` no es un dato perdido — es una mezcla real

Vanessa lo explicó el 2026-08-13: **en 3A y MINI están sembrados Shimmer y las
de Floret intercalados en la misma cama.** Cuando se registra un corte como
`Mix`, mezcla de verdad tallos de Shimmer y de las distintas Floret.

Eso cambia el diagnóstico. `Mix` no es un fallo de captura: **es una descripción
correcta de lo que se cortó.** Lo que se pierde es el cultivar exacto, y eso es
irrecuperable por diseño, no por descuido: los tallos vienen físicamente
entremezclados de la misma cama.

### Pero "Mix = plumosa" NO es una regla permanente

**A veces se siembran y cosechan juntas variedades distintas de plumosa, y a
veces separadas.** Depende de cómo esté armada la cama en ese momento. Así que
el subtipo de una `Mix` **hay que resolverlo por período**, contrastando contra
cómo aparece sembrado en CAMPO y sus inicios de cosecha.

**El método:** para cada corte ambiguo, buscar qué lotes de ese bloque tenían
ventana abierta en esa fecha.

Aplicado a la `Mix` de agosto 2026 en 3A:

| Sembrado en 3A | Inicio cosecha | Subtipo | ¿En ventana en agosto? |
|---|---|---|---|
| Cristata Verda Green | JULIO | cristata | sí — **pero** sus cortes propios paran el 20/07 |
| Summer Sherbet | AGOSTO | plumosa | **sí** |
| Shimmer | AGOSTO | plumosa | **sí** |
| Rose Gold | AGOSTO | plumosa | **sí** |
| Raspberry Lemonade | AGOSTO | plumosa | **sí** |
| Cristata Enda Rose | AMOR (sept) | cristata | proyectada para septiembre |

Y lo que de hecho se cortó en 3A durante agosto: `Mix` (1.960), `Shimmer Mix`
(100) y `Enda Rose` (67).

**Conclusión para este período:** la `Mix` es plumosa. Los dos candidatos
cristata quedan descartados por el propio registro — Verda Green no tiene ningún
corte después del 20/07, y Enda Rose se registra por su nombre, aparte.

### ⚠️ Enda Rose no está adelantada: está perdida

Una versión anterior de esta ficha decía que Enda Rose venía *"3 a 4 semanas
adelantada, consistente con los ciclos reales corriendo por delante de lo
proyectado"*. **Es exactamente al revés**, y la explicación estaba en el
comentario de `campo_siembras.csv`, que no se había leído:

> `Sin Bokashi, con Cotes | ALERTA sem28: inducción floral. Falla luz extendida
> sem27, todas fueron a flor. Probablemente se pierda esa cosecha.`

No es un ciclo rápido: es **inducción floral prematura por una falla de luz en
la semana 27**. Las plantas se fueron a flor antes de terminar de formar tallo.

**Pero no es pérdida total.** Vanessa lo precisó el 2026-08-13: *"sí estamos
cosechando los más largos para venderlos."* O sea que el lote **se está
recuperando por selección** — se corta lo que alcanzó largo vendible y se vende.
Los 67 tallos de agosto son producto real, no descarte.

La lectura correcta está en el medio de las dos que escribí antes: **no es una
cosecha adelantada ni una cosecha perdida — es una cosecha reducida y
seleccionada.** El lote rinde menos de lo que debía, y lo que rinde sale por
corte selectivo del tallo largo.

> **Esto es exactamente la variable 9 de la matriz de decisión.** Cuánto se
> salva de un lote inducido depende de **cuántos tallos alcanzaron largo
> vendible** — y `calidad_tallo.csv` está vacío. Sin medir longitud no se puede
> cuantificar el daño de una inducción ni decidir si el lote merece seguir
> ocupando la cama. Es la diferencia entre *"produjo"* y *"produjo vendible"*.

**Y no fue un caso aislado.** La misma falla golpeó tres cristatas a la vez, con
el comentario idéntico:

| Lote | Bloque |
|---|---|
| Cristata Enda Rose | 3A |
| Cristata Reprise Orange | 4A |
| Cristata Clubs Cocktail | 4A |

Un evento de infraestructura —la luz— cruzó dos bloques y arruinó tres lotes de
la misma semana de siembra. **Eso no se ve en ninguna columna estructurada.**

### La limitación que hace esto impreciso

`campo_siembras.csv` guarda el **inicio de cosecha como nombre de mes**
(`AGOSTO`, `MADRES`, `AMOR`), no como fecha o semana. Y el **fin de cosecha está
vacío en el 87 % de las filas**. Con eso, la ventana de un lote solo se puede
acotar de forma gruesa, y el cruce depende de que los cortes propios de cada
cultivar delaten cuándo dejó de producir.

Mientras el fin de cosecha no se registre, **este cruce va a seguir siendo un
argumento y no una prueba.**

### Qué arreglar en `listas_desplegables.csv` (y qué NO)

```
listas_desplegables.csv  →  Celosia,Mix
```

Hoy el desplegable ofrece **una sola opción**. Pero la corrección **no** es
llenarlo de cultivares: en una cama intercalada, pedirle a quien cosecha que
distinga Shimmer de Rose Gold tallo por tallo es pedir un dato que no existe, y
lo que se obtendría sería ruido con apariencia de precisión.

**La corrección es ofrecer el nivel que sí es real:**

| Opción propuesta | Cuándo se usa |
|---|---|
| `Plumosa Mix` | cama intercalada de 3A/MINI — Shimmer + Floret |
| `Shimmer` | si sale de una cama pura |
| `Summer Sherbet`, `Rose Gold`, `Spun Sugar`, `Raspberry Lemonade` | camas puras de Floret |
| `Cristata Verda Green`, `Cristata Enda Rose`, … | cristatas, que sí van separadas |
| `Dreams`, `Celway`, `Flamingo` | spicatas |

Así el registro captura **el subtipo siempre** —que es la unidad de manejo— y el
cultivar **solo cuando es real.** Registrar `Mix` a secas pierde el subtipo sin
necesidad; registrar un cultivar falso inventa precisión.

## El puente roto entre cosecha y siembra

Los nombres del registro **no cuadran** con los homologados de CAMPO:

| Se cosecha como | Se sembró como |
|---|---|
| `Summer Sherbet` | `Floret Rosados Corales` |
| `Spun Sugar` | `Floret Rosados Corales` |
| `Rose Gold` | `Floret Rosados Corales` |

Tres cultivares distintos bajo un solo nombre homologado de color. **Consecuencia
directa: no se puede cruzar la cosecha con las plantas trasplantadas**, y por
tanto no hay tallos/planta para esos lotes. Es el mismo puente roto que en
Colitas de conejo.

## Qué falta

1. **Subtipo de `Sunday` y `Sylphid`** — es lo único del mapeo que sigue
   abierto. `Sunday` está sembrada (tres lotes en 4A, uno en Inv 2) pero
   todavía no ha llegado al registro de cosecha.
2. **`Glowing Embers`** — pedir siembra y color; hoy no existe en el repo.
3. **Arreglar `listas_desplegables.csv`** con los niveles de la tabla de arriba:
   subtipo siempre, cultivar solo cuando la cama es pura.
4. **Deshacer `Floret Rosados Corales`** en homologados por cultivar. Hoy
   agrupa Spun Sugar (1.200 plantas), Summer Sherbet (1.200) y Rose Gold
   (1.231) bajo un solo nombre, así que sus tallos no se pueden cruzar con sus
   plantas y no hay tallos/planta para ninguno.

## Lo que dicen los COMENTARIOS — y por qué hay que leerlos

Vanessa lo señaló el 2026-08-13: **los cierres se explican sobre todo en los
comentarios.** Ahí está si una cama se sacó porque *se necesitaba el espacio* o
porque *se acabó la cosecha* — dos cosas que en los números se ven igual y
significan lo opuesto. Y ahí están las semanas de pico.

### 1. La inducción floral es un patrón, no un incidente

Aparece en **siete** lotes de Celosia:

| Lote | Bloque | Qué dice el comentario |
|---|---|---|
| Cristata Enda Rose | 3A | Falla luz sem27, todas a flor, cosecha probablemente perdida |
| Cristata Reprise Orange | 4A | idéntico |
| Cristata Clubs Cocktail | 4A | idéntico |
| Celosias Lavly | — | `PERDIDA INDUCCION FLORAL` — pérdida total |
| Celosias Lavly | 4 | Inducción floral en semana 11 |
| Celosias Shimmer | 5 | *"no fueron buenos tallos como en cosechas anteriores. ¿Puede ser por la inducción floral/elongación?"* |
| Celosias Dreams | 2 | *"Ya muestran plumas. ¿Inducción floral?"* |
| Cristata Verda Green | 3A | *"En sem 22 ya tienen crestas. Me preocupa si es una inducción"* |

**Por la regla de promoción a norma del `CLAUDE.md` —misma variedad, misma
zona, mismo comportamiento, dos veces o más— esto ya es regla, no observación.**
La Celosia en DCB tiene un problema sistémico de inducción floral ligado a la
luz, y cuesta lotes completos.

### 2. Un cierre no es un final de cosecha

| Lote | Por qué se cerró |
|---|---|
| Celosias Indian Summer (4) | *"Cosechamos tallos buenísimos en semana 19, y **hubiésemos podido extender y engordar hasta la 20, pero los usamos en madres**"* |
| Celosias Asian Garden (2) | *"están desde la 15 pero **esperando salir de las dreams primero**"* |
| Celosias Dreams (4B) | *"excelente semana 15, ya en 16 podríamos pelar, **lo sacamos en la 18**"* |

Ninguno de los tres cerró porque se acabara la producción. **Cerraron por
demanda o por rotación de cama.** Un motor que lea solo las fechas los va a
contar como ventanas terminadas y va a subestimar el potencial de las tres.

### 3. Las semanas de pico están dichas

- **Dreams:** arranca sem 14, **excelente sem 15**, en 16 ya se puede pelar
- **Indian Summer:** tallos buenísimos sem 19, **podía engordar hasta la 20**
- **Cristata Verda Green (3A):** cosecha desde sem 25, con mucha desuniformidad

### 4. Y de paso, conocimiento de bouquet

> Indian Summer: *"Combina lindo con rosado claro solamente. **Con otros colores
> oscurece el bouquet**."*

Eso es una regla de color que no está en `paleta_color.csv` ni en ninguna receta.

### 5. Otras causas de pérdida registradas ahí

- **Verda Green (3B):** *"Se quedaron enanas"* · *"Sem27-28 cosechando pero con
  síntomas de **botritis**"*
- **Verda Green (3A):** *"hay unas cabezas con abanicos grandes y otras muy
  pequeñas. **Creo que con más agua nos puede ir mejor**, pero sí elongaron
  mucho"* — la limitante de riego otra vez
- **Floret (Spun Sugar, Summer Sherbet, Shimmer):** *"Sem27 tallos cortos. Sem28
  más largos. Algunos centros muy maduros cortados cortos con laterales
  inmaduros"* — problema de uniformidad de corte

## Lo que este caso enseña

**La `Mix` parecía un fallo de captura y era una descripción honesta.** La
primera lectura —"el 31 % entró sin cultivar, hay que arreglar el desplegable
para que ofrezca cultivares"— habría llevado a pedirle a quien cosecha un dato
que no existe en el campo, porque la cama está intercalada. El resultado no
habría sido más precisión: habría sido ruido con apariencia de precisión.

La pregunta correcta no era *"¿por qué no anotaron el cultivar?"* sino
**"¿el cultivar es siquiera separable en esa cama?"**. La respuesta era no — y
en cuanto se supo, los 1.960 tallos pasaron de irrecuperables a plenamente
atribuidos al nivel que importa para decidir: el subtipo.

**Y la segunda lección, más cara:** las dos veces que esta ficha se equivocó
—decir que Sunday estaba sembrada, y llamar "adelantada" a una Enda Rose que
está perdida— **el dato correcto estaba en el archivo**, en la fecha de siembra
una vez y en el comentario la otra. No faltaba información: faltaba leerla.

Las columnas estructuradas dicen **qué** pasó. Los COMENTARIOS dicen **por qué**,
y sin el porqué los números mienten en las dos direcciones: un cierre por
demanda parece agotamiento, y una pérdida por inducción parece precocidad.
