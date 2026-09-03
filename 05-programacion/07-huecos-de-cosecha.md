# Huecos de cosecha — corte semana ISO 36 (2026-09-03)

> Generado con `python3 motor/cerebro.py huecos` contra `campo_siembras.csv`
> **reexportado del `PROGRAMACION_2026 v8` vivo el 2026-09-03**,
> `ciclos_variedad.csv`, `registro_tallos.csv` (corte 12/08) y
> `calendario_comercial_colombia.csv`.
> **Todavía sin un solo porcentaje de mortalidad medido** — ver el bloque final.

---

## Cómo se corrigió este documento

La primera versión corrió sobre el espejo v7 del 30 de julio, cuya última siembra
era la **semana 28**, y concluyó *"ocho semanas sin sembrar"* y un hueco de
noviembre. **Era falso.** Vanessa lo desmintió: en el v8 hay siembras todas las
semanas hasta la 36. Reexportado CAMPO desde el v8 vivo, aparecen las **36
siembras de las semanas 29 a 36** que faltaban, y noviembre queda cubierto.

Lo que se arregló para que no vuelva a pasar está en el bloque final.

---

## El estado real

```
SEM   TALLOS   curva                        VENTA
 36    1.863   #########                    -        <- el valle es AHORA
 37    2.182   ##########                   -
 38    3.904   ###################          -
 40    4.078   ###################          -
 41    2.793   #############                -        <- segundo valle
 42    2.895   ##############               -
 44    5.303   ##########################   -
 45    5.182   #########################    ALTA
 46    4.074   ###################          ALTA
 47    4.102   ####################         ALTA
 48    3.587   #################            ALTA
 50    3.976   ###################          MIXTA
 52    2.102   ##########                   MIXTA
 53+     244   #                            —        aún sembrable, decidir AHORA
```

**Noviembre está cubierto.** Las semanas 45 a 48 proyectan entre 3.587 y 5.182
tallos, por encima del piso de referencia (1.844, la peor semana ya medida de
2026). El hueco que anunciaba la versión anterior de este documento **no existe**.

Tres cosas que sí dice esta curva:

**1. El valle es ahora, no en noviembre.** Las semanas **36 y 37** proyectan 1.863
y 2.182 tallos, contra las 5.100–7.100 reales de las semanas 28 a 32. Es la caída
más profunda del semestre y **ya está pasando**. Coincide exactamente con lo que
Vanessa reporta: lisianthus cerrando su primera floración.

**2. Hay un segundo valle en las semanas 41 y 42** (2.793 y 2.895). Menos
profundo, pero cae justo antes de que arranque el volumen de noviembre.

**3. La semana 53 en adelante está vacía — y eso es normal.** Es enero de 2027, y
todavía no se ha sembrado para esa fecha porque **todavía se alcanza**. El motor
lo marca `aún sembrable, decidir AHORA` y no como hueco: desde la semana 45 en
adelante cualquier semana vacía se puede llenar sembrando hoy, y confundir las dos
cosas hace sonar la alarma justo por el trabajo que toca hacer.

---

## Sembrar directo amaranto y celosia: apunta al hueco correcto

| Grupo | Trasplantando hoy | Sembrando en bandeja hoy |
|---|---|---|
| Boca de Dragón | sem 45 | sem 50 |
| **Amaranto** | **sem 46** | **sem 51** |
| Campanula · Matricaria · Ammi · Zinnia · Girasol | sem 48 | sem 52–55 |
| Gomphrena · Statice | sem 49 | sem 53–54 |
| **Celosia cristata** | **sem 50** | **sem 55** |

Con el dato real la lectura cambia respecto a la versión anterior:

**Sembrar celosia directa ahora es la decisión correcta**, y apunta justo al único
tramo que de verdad está vacío: **la semana 53 en adelante — enero-febrero de
2027**. Cristata sembrada hoy llega entre la 50 y la 55. No es tarde: es
exactamente a tiempo.

**Amaranto directo llega antes (sem 46–51)** y cae sobre semanas que ya están
cubiertas por noviembre. Sigue teniendo sentido —refuerza el tramo 49–52, que baja
a 2.916 y 2.102— pero **no es urgente de la manera que lo era bajo el diagnóstico
equivocado.**

**Lo que la siembra directa no arregla son las semanas 36, 37, 41 y 42**, porque
nada sembrado hoy llega antes de la 45. Ese valle, que es el que se está sintiendo
en la sala ahora mismo, solo se administra con lo que ya está en la cama:
estirando ventanas, sosteniendo la segunda floración del lisianthus, y ajustando
las recetas de bouquet al color que sí va a haber.

**Advertencia de dato:** las dos columnas son trasplante y bandeja. **Ninguna es
siembra directa en cama.** Cuánto adelanta o atrasa la siembra directa **no está
medido en ningún CSV de este repositorio.** Si se hace, hay que registrarla
marcada como ensayo — es la única forma de que la próxima vez esta tabla tenga una
tercera columna con dato real.

---

## Lo que la proyección sigue sin ver

La curva sale de **183 lotes**. Quedan **46 fuera**, y el motor los reporta uno por
uno en vez de estimarlos. El agujero grande son **33.399 plantas sin fila en
`ciclos_variedad.csv`** — y adentro está **Celosia, que es un pilar**:

| Nombre homologado | Plantas |
|---|---|
| Shimmer Mix | 8.344 |
| Dreams Mix | 5.417 |
| Floret Rosados Corales | 3.631 |
| Achillea Cloth of God | 3.342 |
| Cristata Indian Summer | 2.400 |
| Cristata Reprise Velvet | 2.082 |
| Brianthus Jolly | 1.850 |
| Nigella Miss Jekyll Pink | 1.600 |
| Sunflower Pro Cut Red | 1.440 |
| Floret Raspberry Lemonade | 1.158 |
| Achillea Cerise Queen | 1.000 |
| Cynoglossum Blue | 597 |
| Craspedia | 338 |
| Echinops | 200 |

`ciclos_variedad.csv` tiene `Celosia plumosa`, `Celosia cristata`, `Celosia
spicata` y `Celosia Purple Flamingo`, pero **ninguna de las celosias sembradas cae
en esas cuatro filas**. El motor no adivina a cuál pertenece cada mezcla.

**Esto significa que la curva de arriba está subestimada**, y no poco: 33.399
plantas es una fracción grande del cultivo. Los valles reales de las semanas 36–37
y 41–42 probablemente son menos profundos de lo que se ve.

---

## Lo que falta para cerrar esto

**1. Los porcentajes de mortalidad.** `07-datos/mortalidad_siembras.csv` tiene los
lotes de la temporada con `pct_mortalidad` **vacía**. El motor la lee y la aplica
sola. Hoy la curva **supone que no se murió ni una planta**: es el techo.

La calibración contra `registro_tallos.csv` mide un **factor de realización de
0,24**: de cada 100 tallos que el ciclo promete, el cultivo entrega 24. Ese 76 % se
lo reparten mortalidad, descarte de calidad y optimismo de tallos/planta, y **hasta
que no haya mortalidad medida no se pueden separar.**

**2. A qué grupo de ciclo pertenece cada celosia sembrada** — Shimmer, Dreams,
Rose Gold, Raspberry Lemonade, Spun Sugar, Summer Sherbet, Asian Garden.

**3. El número de plantas de 13 lotes** que lo tienen vacío en CAMPO.

---

## Lo que se arregló para que el error no se repita

**El puente a Drive.** `PROGRAMACION_2026` no se puede bajar entero (11,5 MB,
`File too large for export`), el export a CSV solo devuelve la primera pestaña, y
la lectura en texto trunca CAMPO a 116 filas. Se creó
**`DCB_PUENTE_CAMPO`** (`1ndYgVHA49dGfeTULKkHu8gTLbHJAcfuJSfDRfsDZsSw`), una hoja
de una sola celda con `IMPORTRANGE` sobre `CAMPO!A:U` del v8. Al ser la primera
pestaña de un libro pequeño, **sí exporta a CSV entera y siempre fresca.** Es la
vía para refrescar `campo_siembras.csv` de aquí en adelante.

**La alarma en el motor.** `cerebro.py huecos` ahora compara la última siembra
registrada contra la semana en curso, y si el atraso es de 3 semanas o más se
planta y advierte que *"no se sembró"* y *"el snapshot quedó viejo"* se ven
idénticos desde el CSV. Con el v8 reexportado la alarma no salta: última siembra
semana 36, cero de atraso.

**La columna `Estado`.** El v8 trae `Cerrada` / `Activa`, que el espejo v7 no
tenía. El motor la usa: a un lote cerrado se le respeta lo que aportó hasta la
semana en curso y se le corta el futuro, en vez de proyectarlo produciendo desde
una cama que ya no existe.

**La distinción hueco / horizonte.** Una semana vacía que todavía se alcanza a
sembrar no es un hueco. El motor calcula el horizonte con el ciclo más corto del
catálogo (9 semanas) y marca todo lo que cae después como `aún sembrable`.
