# Huecos de cosecha — corte semana ISO 36 (2026-09-03)

> Generado con `python3 motor/cerebro.py huecos` contra `campo_siembras.csv`,
> `ciclos_variedad.csv`, `registro_tallos.csv` (corte 12/08) y
> `calendario_comercial_colombia.csv`.
> **Todavía sin un solo porcentaje de mortalidad medido** — ver el bloque final.

---

## 🔴 LEER ESTO PRIMERO — este documento corre sobre un espejo desactualizado

**La curva de abajo NO es un pronóstico. Es lo que se ve desde un CSV viejo.**

`campo_siembras.csv` se exportó el **30 de julio de 2026 desde el
`PROGRAMACION_2026` v7**, y su última siembra es de la **semana 28**. Vanessa
confirmó el 2026-09-03 que **en el `PROGRAMACION_2026 v8 ACTUALIZADO` hay
siembras todas las semanas hasta la 36**. Esas ocho semanas de siembras existen
en el campo y **no están en este análisis**.

La primera versión de este documento leyó ese vacío como "ocho semanas sin
sembrar" y construyó encima un hueco de noviembre. **Eso era un artefacto del
espejo, no un hallazgo.** El motor ahora lo advierte solo: desde el CSV, "no se
sembró" y "el snapshot quedó viejo" se ven exactamente igual, y por eso
`cerebro.py huecos` se niega a que se lea la curva como pronóstico mientras el
atraso sea de 3 semanas o más.

**Estado del intento de traer el v8 (2026-09-03):**

| Fuente | Qué se encontró |
|---|---|
| `PROGRAMACION_2026_v8_ACTUALIZADO.xlsx` (`1NaGlBEY…`) | existe, pero `modifiedTime` **2026-07-22** — más viejo que el propio CSV |
| Hoja nativa v8, 33 pestañas (`1eZdmU5b…`, registrada en `FUENTES.md`) | **el ID ya no resuelve** en Drive |
| Búsqueda de cualquier `PROGRAMACION` nativa reciente | solo aparece `PROGRAMACION 2024-2025`, ajena a esto |

Es decir: **el v8 que se edita de verdad no es ninguno de los dos IDs que tiene
registrado este repositorio.** Hasta que se resuelva cuál es y se reexporte la
hoja CAMPO, todo lo que sigue vale como **método, no como cifra.**

Lo que sí se sostiene sin depender del espejo está marcado ✅ más abajo.

---

## Lo que decía este documento antes de la corrección

*(Se conserva para que quede el rastro de qué se concluyó mal y por qué.)*

La última siembra registrada en CAMPO es de la semana 28. Estamos en la 36:
ocho semanas sin sembrar. Ese vacío no se siente hoy, se siente cuando esas
plantas tenían que estar cosechando — y eso cae en noviembre, el mes que el
calendario comercial marca ALTA. La curva no baja: se corta.

**Por qué estaba mal:** las siembras de las semanas 29 a 36 sí se hicieron y sí
están escritas — en el v8, no en el espejo v7 que leyó el motor.

```
SEM   TALLOS   curva                        VENTA
 38     4.553   ##################           -
 39     5.290   #####################        -
 40     6.433   ##########################   -        <- el techo del semestre
 41     4.420   #################            -
 42     3.379   #############                -
 43     2.980   ############                 -
 44     2.518   ##########                   -
 45     1.619   ######                       ALTA     <  bajo el piso  ***
 46         0                                ALTA     <<< HUECO        ***
 47         0                                ALTA     <<< HUECO        ***
 48         0                                ALTA     <<< HUECO        ***
 49         0                                MIXTA    <<< HUECO
 50         0                                MIXTA    <<< HUECO
 51         0                                MIXTA    <<< HUECO
 52         0                                MIXTA    <<< HUECO
```

El piso de referencia (1.844 tallos/sem) es la **peor semana ya medida** de 2026.
Desde la 45 la proyección va por debajo de esa peor semana, y desde la 46 no hay
ninguna siembra registrada que esté cosechando.

**El pico de la semana 40 no es una buena noticia, es el problema:** es la última
vez que el cultivo llega arriba. Después de eso viene la caída, y la caída no
tiene nada detrás.

---

## Los tres hechos que armaban el hueco — cuál cayó y cuáles siguen en pie

**1. ❌ CAÍDO — "ocho semanas sin sembrar".** Era el espejo viejo, no el campo.
Las siembras de la 29 a la 36 existen en el v8. **Este era el pilar del
argumento, y sin él el hueco de noviembre queda sin base.** Cuánto lo tapan esas
ocho semanas de siembra no se puede calcular hasta reexportar CAMPO.

**2. ✅ EN PIE — Lisianthus está cerrando su primera floración.** Es uno de los cuatro
pilares (Statice, Bocas, Celosia, Lisianthus sostienen más de la mitad de cada
semana). La segunda floración está documentada en `ciclos_variedad.csv` como
**débil** — *"2a floracion debil"* — así que no reemplaza a la primera, la
estira. Y de los 11 lotes de lisianthus con mortalidad por fusarium en la semana
20, uno solo se documentó como resistente.

**3. ✅ EN PIE — Noviembre es mes ALTA.** Y las semanas 45 a 48 son noviembre. Ahí caen
también las **graduaciones de colegio**, que el calendario marca como `SUBE`.
Un hueco en un mes flojo se administra; un hueco en noviembre es plata que no se
hace.

---

## ✅ Lo que la proyección NO está viendo (esto no depende de la versión)

Estos dos hallazgos salen de `ciclos_variedad.csv`, no de la hoja CAMPO, así que
**siguen en pie con el v8**: reexportar CAMPO agrega siembras, pero no les
inventa una fila de ciclo a las celosias que no la tienen.

La curva de arriba sale de **108 lotes**. Quedan **70 lotes fuera**, y el motor
los reporta uno por uno en vez de estimarlos:

| Por qué queda fuera | Lotes | Plantas |
|---|---|---|
| Sin número de plantas en CAMPO | 40 | ? |
| **Sin grupo en `ciclos_variedad.csv`** | 22 | **36.617** |
| Grupo sin tallos/planta | 7 | 7.234 |
| Grupo sin ciclo ni ventana | 1 | 1.170 |

El agujero grande es el segundo, y adentro está **Celosia, que es un pilar**:

| Nombre homologado | Plantas |
|---|---|
| Shimmer Mix | 8.344 |
| Dreams Mix | 5.417 |
| Opus Early Bronze | 4.658 |
| Floret Rosados Corales | 3.631 |
| Achillea Cloth of God | 3.342 |
| Cristata Indian Summer | 2.400 |
| Cristata Reprise Velvet | 2.082 |
| Brianthus Jolly | 1.850 |
| Nigella Miss Jekyll Pink | 1.600 |
| Floret Raspberry Lemonade | 1.158 |
| Achillea Cerise Queen | 1.000 |
| Cynoglossum Blue | 597 |

`ciclos_variedad.csv` tiene `Celosia plumosa`, `Celosia cristata`, `Celosia
spicata` y `Celosia Purple Flamingo`, pero **ninguna de las celosias que están
sembradas cae en esas cuatro filas**. El motor no adivina a cuál pertenece cada
mezcla: eso lo tiene que decir Vanessa.

**Esto ensancha las semanas 38 a 45, no las 46 en adelante.** Se verificó lote por
lote: de los 70 excluidos, solo **cuatro** tienen inicio de cosecha registrado en
la semana 40 o después (Achillea Ext 3 en la 42, y Statice Forever Silver,
Girasol White Lite y Green Ball en la 40, los tres sin número de plantas). Lo
único que produce de verdad después de la 46 son los perennes —Dahlias, Espárrago
y las rosas de Inv 1— y eso es una fracción pequeña del volumen semanal.

**El acantilado de la 46 es real. La profundidad de las semanas 42–45 es la que
está subestimada.**

---

## ✅ Sembrar directo amaranto y celosia: la aritmética no depende del espejo

Esta tabla sale de `ciclos_variedad.csv` y de la semana en curso. **Vale igual
con el v8**: lo que cambia con el v8 es *cuánto* hueco hay que llenar, no *qué
alcanza a llegar*.

El motor calcula qué alcanza a llegar sembrando hoy, semana 36:

| Grupo | Trasplantando hoy | Sembrando en bandeja hoy |
|---|---|---|
| Boca de Dragón | sem 45 | sem 50 |
| **Amaranto** | **sem 46** | **sem 51** |
| Campanula · Matricaria · Ammi · Zinnia · Girasol | sem 48 | sem 52–55 |
| Gomphrena · Statice | sem 49 | sem 53–54 |
| Celosia cristata | sem 50 | sem 55 |

Tres conclusiones que cambian la decisión:

**1. Las semanas 42 a 45 ya no se pueden sembrar.** Nada de lo que se siembre hoy
llega antes de la 45, y eso es lo más rápido que hay (Boca de Dragón,
trasplantando una plántula que hoy no existe porque Andrés no entrega hace dos
meses). Ese tramo se resuelve **estirando lo que ya está en la cama**, no
sembrando.

**2. Amaranto directo sí sirve — pero para noviembre-diciembre, no para
octubre.** Es el grupo más rápido del catálogo (10 semanas desde trasplante) y
germina fácil, que es justo el argumento de la siembra directa. Cae en la
**semana 46–51**, que es exactamente el fondo del hueco. Es la mejor jugada
disponible.

**3. Celosia directa NO alcanza este hueco.** Cristata son 14 semanas desde
trasplante: sembrada hoy llega en la **semana 50 como muy pronto, y más
probablemente en la 55**, o sea febrero. Sembrar celosia hoy es una decisión
correcta pero para **el hueco de enero-febrero**, que es el siguiente, no este.

**Advertencia de dato:** las dos columnas de la tabla son trasplante y bandeja.
**Ninguna es siembra directa en cama.** La siembra directa se salta el trasplante
pero no la germinación, y cuánto adelanta o atrasa **no está medido en ningún CSV
de este repositorio**. Si se hace, hay que registrarla marcada como ensayo — es la
única forma de que la próxima vez esta tabla tenga una tercera columna con dato
real en vez de una suposición.

---

## Los levers que sí actúan sobre las semanas 42 a 45

No son siembras. Son decisiones sobre camas que ya están puestas:

**Estirar las ventanas que se están cortando temprano.** `cierres_lote.csv`
documenta cuatro lotes cerrados con el motivo `temprano` y el comentario textual
*"hubiesen aguantado 1 sem más"* — Ammi Majus + Ammobium (4EXT, sem 27), Ammobium
Winged Everlasting (3 EXT, 27), Ammobium Alatum (3A, 27), Gomphrena Sequin (3A
bajas, 27). Y solo **4 de 36 lotes cerraron por agotamiento real**: el resto se
cerró por espacio, rotación o calidad. En un semestre normal cerrar temprano
libera cama; en este semestre **la cama que se libera no tiene con qué llenarse.**

**La segunda floración de lisianthus.** Está documentada como débil, pero débil no
es cero, y cae justo en el tramo. Vale la pena decidir explícitamente si se
sostiene con manejo en vez de dejar que salga sola.

**Revisar las recetas de bouquet contra el color que va a faltar.** Es el trabajo
de `cerebro.py explotar` y `auditar` — si noviembre va a llegar con poco volumen,
la mezcla de color del punto de venta se decide ahora, no cuando falte.

---

## Lo que falta para cerrar este análisis

**1. Los porcentajes de mortalidad — esto es lo primero.**
`07-datos/mortalidad_siembras.csv` está creado con los **73 lotes** de la
temporada sembrados desde la semana 18, y la columna `pct_mortalidad` **vacía**.
El motor la lee y la aplica sola en cuanto tenga números.

Hoy la curva de arriba **supone que no se murió ni una planta**. Es el techo, no
el pronóstico. Con el verano que hubo, el hueco real es más profundo que el que
muestra este documento.

La calibración contra `registro_tallos.csv` mide un **factor de realización de
0,29**: de cada 100 tallos que el ciclo teórico promete, el cultivo entrega 29.
Ese 71 % se lo reparten tres cosas —mortalidad, descarte de calidad y optimismo de
tallos/planta— y **mientras no haya mortalidad medida no se pueden separar.** Ese
es exactamente el valor de llenar la columna: convierte un factor global que mezcla
tres causas en tres números que se pueden atacar por separado.

**2. A qué grupo de ciclo pertenece cada celosia sembrada** — Shimmer, Dreams,
Rose Gold, Raspberry Lemonade, Spun Sugar, Summer Sherbet, Asian Garden. Son
36.617 plantas invisibles para la planificación.

**3. El número de plantas de 40 lotes** que lo tienen vacío en CAMPO.

**4. Confirmar si hubo siembras entre la semana 29 y la 36** que no se hayan
registrado. Si las hubo, el hueco de noviembre es menos grave de lo que se ve
aquí — y si no las hubo, este documento es el pronóstico.
