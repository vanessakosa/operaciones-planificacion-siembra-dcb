# Dónde quedamos — el eje de ocupación ya corre, 2026-09-10 (noche)

**Para retomar en otra conversación.** Continúa
`04-donde-quedamos-rentabilidad.md`, que era la sesión de la tarde.

```bash
git pull
python3 motor/ocupacion.py                # AHORA SÍ ordena — el eje central
python3 motor/ficha_variedad.py           # qué dato hay por grupo y cuál falta
python3 motor/calibrar_rendimiento.py     # lo teórico del ciclo vs lo real
python3 motor/cerebro.py cartera          # sobra/falta por volumen
python3 motor/dictar_tallos.py estado     # hasta dónde llega la cosecha
```

---

## 1. Lo que cambió, en una frase

**El bloqueo dominante de la sesión anterior no existía.** Se creía que faltaba
la columna `Fecha siembra campo` y que sin ella el área no se podía recortar a
la ventana del registro. La columna que hace ese trabajo **ya estaba llena**,
con otro nombre, y por eso el eje ingreso/m²/semana ahora corre y ordena.

## 2. Por qué no se veía

| Columna | Filas | Plantas |
|---|---|---|
| `Fecha siembra campo` (idx 6) | 112/302 (37 %) | 32.487 (**14 %**) |
| `Semana` de trasplante (idx 7) | 294/302 (97 %) | 221.208 (**95 %**) |

Vanessa ya lo había dicho el 2026-08-14: *"dejé de usarla, ahora trabajo solo
con las semanas... la columna que sigue es la semana que se trasplantó... eso lo
hago porque a veces puede pasar que en esa semana se sembró en dos días
distintos, y proyectamos todo por semana."*

Y había una razón **mecánica** por la que el motor no podía verla:
`campo_siembras.csv` tiene **dos columnas llamadas `Semana`** — trasplante
(idx 7) e inicio de cosecha (idx 10) — y `csv.DictReader` colapsa encabezados
repetidos quedándose con la última. `C._leer_csv()` nunca pudo leer la de
siembra. **Ahora se leen por posición.**

El año no está en el archivo. Se infiere por secuencia: las 302 filas son un log
cronológico y una caída grande en el número de semana es el cruce de diciembre a
enero. **Verificado contra las 111 filas que todavía traen fecha exacta:
coinciden las 111**, en año y en semana (±1).

## 3. Qué se construyó

`motor/ocupacion.py` recorta el área a la ventana de cosecha **propia de cada
grupo** — no a una global. Si se usara una global, un grupo cuyos tallos se
registraron dos semanas cargaría con el área de camas que produjeron doce: el
numerador y el denominador tienen que cubrir el mismo periodo.

De 142.067 plantas ubicadas, **47.272 caen fuera** de la ventana de su grupo.
Ese era el sesgo, y era un tercio del denominador.

**La tabla trae su propia validación.** Si el recorte fuera equivocado, el
`tallos/planta` implícito se iría lejos del documentado en `ciclos_variedad.csv`.
Se acerca en **11 grupos de 15**, se aleja en 1, y en 3 no quita ninguna planta.
Los residuos tienen causa conocida y salen marcados:

- **Sobre el doc** (Zinnia 2,69 y Green Ball 2,77 contra 1) — cultivos de corte
  repetido cuyo `tallos_planta` en el ciclo está subestimado.
  `calibrar_rendimiento.py` da la misma señal por su lado: Zinnia 15,7× lo
  teórico. **Dos herramientas independientes coinciden: ese ciclo está mal.**
- **Bajo el doc** (Statice 1,46 contra 8) — ventana larga a la que el registro
  sólo le vio un tramo.

## 4. Dos advertencias que no hay que perder

**El orden es sensible al largo del registro, y no poco.** Al entrar las semanas
ISO 33-35 en esta misma sesión:

| | antes (corte 08-12) | después (corte 08-27) |
|---|---|---|
| Lisianthus | **$78.474/m²/sem — 1.º** | **$17.749 — 4.º** |
| plantas en ventana | 2.106 | 11.400 |
| tallos/planta implícito | 2,69 ("coherente") | 0,61 (bajo el doc de 2) |

La ventana más larga le solapó 5,4× más área pero sólo 1,22× más tallos. Lo que
antes se leía como "coherente" era un artefacto de la ventana corta. **Un
cultivo de ocupación larga y ventana corta de cosecha es el más expuesto a
esto.** Mientras falten semanas por registrar, el orden es provisional.

**`sem_a_campo` se cuenta desde el TRASPLANTE, no desde la semilla.** Se
verificó contra `cerebro.plan_siembra` (línea 737): hace
`sem_campo = sem_cosecha - sem_a_campo` y sólo después resta la germinación para
llegar a la semana de bandeja. Así que las semanas de cama son
`sem_a_campo + ventana` y la germinación —que es en bandeja— no entra. La
fórmula que ya tenía `ocupacion.py` era correcta.

## 5. El registro de tallos

Bajado de Drive como **XLSX binario** (318 KB, magic `PK`) y pasado por
`importar_tallos.py`. Leerlo como texto interpretado trunca sin avisar.

| | antes | después |
|---|---|---|
| filas | 696 | 822 |
| corte | 2026-08-12 | **2026-08-27** |
| tallos | 66.417 | 83.315 (+25 %) |
| lotes en `CONSOLIDADO` | 141 | 221 |

Entraron las semanas **33, 34 y 35**. **Faltan la 36 y la 37** — la operaria
subió hasta el 27/08. La 35 está parcial porque el corte cae a media semana.

## 6. La tabla de hoy

```
GRUPO              ROL     PLANTAS   (ACUM)  DIST  AREA m2  TALLOS TALLOS/m2  SEM   $/m2/SEM
Zinnia             FOCAL     1.895    1.895   15cm     42.6    5091    119.4   16     59.856
Green Ball         TOQUE     1.745    2.641   15cm     39.3    4836    123.2   16     36.476
Girasol            FOCAL     1.750    2.700    8cm     19.7    1144     58.1   15     26.273
Lisianthus         FOCAL    11.400   12.728    8cm    128.2    6926     54.0   29     17.749
Ammi               BASE_E    3.014    7.798   15cm     67.8    3132     46.2   16     17.358
Campanula          BASE      8.768   23.646    8cm     98.6    4728     47.9   16     15.577
Gomphrena          TOQUE     5.120    9.667   15cm    115.2    6788     58.9   21     11.318
Amaranto           BASE      3.086    3.686   15cm     69.4    2155     31.0   18      8.398
Statice            BASE      8.909   10.856   30cm    400.9   13013     32.5   23      7.039
Ammobium           BASE      6.401    6.401   15cm    144.0    2922     20.3   16      5.935
Strawflower        BASE      7.249   10.724   15cm    163.1    2059     12.6   21      2.459
Larkspur           TOQUE     4.788    4.788    5cm     35.9     243      6.8   14      2.267  [FRAGMENTO]
```

**Es INGRESO, no margen.** Sigue faltando la fila de tallos vendidos del modelo
de costos para poder restar.

**Boca de Dragón queda fuera con 14.769 tallos** — el grupo de más volumen del
cultivo — porque no tiene una sola planta trasplantada vinculada. Y **Celosia
con 11.320** porque su distancia depende del subtipo (cristata 7,5 cm, plumosa
15 cm) y el grupo no tiene una sola. Esos dos son el hueco más grande que queda.

## 7. Lo siguiente, en orden

1. **Vincular plantas trasplantadas a Boca de Dragón.** Es el grupo de más
   tallos del cultivo y no entra a la tabla. Con Celosia son 26.089 tallos
   fuera del eje.
2. **Corregir `tallos_planta` de Zinnia y Green Ball** en
   `ciclos_variedad.csv`. Figuran con 1 y dos herramientas independientes dicen
   que producen 2,7×. Ese número corre todo el planificador de siembra, no sólo
   esta tabla.
3. **Semanas ISO 36 y 37** cuando la operaria las suba, y volver a correr — el
   orden puede moverse otra vez.
4. **Tallos vendidos por mes** en `DCB_Modelo_Costos`: 12 números, único campo
   manual, en 0 en los 12 meses. Es lo que convierte ingreso en margen.
5. **Distancia por subtipo de Celosia** en `ciclos_variedad.csv`, para que deje
   de promediarse.

## 8. La decisión de arquitectura que quedó abierta

`cerebro.py m2` **no está en `main`**, y ahora hay dos documentos que lo
referencian (`13-optimizacion/06-tallos-por-m2.md` y `07-...`, ambos traídos de
`dcb-planning-system-wvnda6`). Los dos quedaron anotados diciéndolo, para que no
mientan.

Los dos linajes de `cerebro.py` divergieron de verdad:

- **`main`** ganó `cmd_cartera` y sus ayudantes (`cargar_roles`,
  `demanda_catalogo`, `oferta_registrada`, `por_subtipo`…)
- **`dcb-planning-system-wvnda6`** ganó `cmd_m2`, `cmd_prorratear`,
  `cmd_chequear` y una familia de **907 líneas** para ubicar siembras en el
  tiempo (`construir_lotes`, `_ventana_estimada`, `siembras_activas`,
  `cobertura_registro`, `tasas_limpias`…)
- **15 funciones compartidas difieren** entre los dos, entre ellas
  `_plantas_del_lote`, `cmd_rendimiento`, `resolver` y `cargar_ciclos`.

**Portar `m2` tal cual dejaría la misma lógica en dos lugares**, porque
`ocupacion.py` ya implementa "ubicar una siembra en el tiempo" por su lado
(`_semanas_de_siembra`, `_mes_anclado`, `ventanas_de_siembra`). `CLAUDE.md`
prohíbe justamente eso. Hay que decidir una de tres:

1. Extraer un módulo `motor/tiempo.py` con la lógica de ubicación, y que
   `ocupacion.py` y un `cmd_m2` portado lo importen los dos. **Es la limpia.**
2. Portar `cmd_m2` reescrito sobre los ayudantes que ya tiene `ocupacion.py`.
   Más barato, pierde `prorratear` y `chequear`.
3. Reconciliar los dos `cerebro.py` de una vez. Es el trabajo grande.

Lo que aporta `m2` y hoy no existe en `main`: la vista **por lote** (grupo ×
variedad × bloque) y la comparación **dentro de un mismo bloque** — mismo riego,
misma luz, mismo suelo, que es donde la comparación es limpia.

## 9. Las preguntas para Vanessa

1. ~~**Inv 3C pequeña**: 90 huecos o 70.~~ **CERRADO 2026-09-10.** No eran dos
   fuentes contradiciéndose: eran **dos secciones distintas**, y cada fuente
   tenía razón sobre una parte. Vanessa: *"hay una sección que podríamos llamar
   A que tiene las camas largas y tiene cuatro camas largas que tienen noventa
   huecos. Y luego hay una sección B que tiene tres camas cortas que tienen
   setenta huecos."* Los 90 huecos que `capacidad_bloques.csv` le tenía puestos
   a la sección de 3 camas eran de las **largas**. Inv 3C queda en **7 camas y
   102,6 m²** (antes 8 camas y 175,5), y el total de la finca baja de 1.857 a
   **1.784,7 m²**.

   **Pero abrió una discrepancia nueva en la sección A**, y es grande: este
   dictado dice 4 camas de 90 huecos (64,8 m²), mientras `capacidad_bloques.csv`
   (5 × 141h) y `01-invernaderos.md` (5 × 140h) **coincidían entre sí** en
   126,9 m². Son 72,9 m² —el 41 % del bloque— y una cama de diferencia. Se
   aplicó el dictado por jerarquía de verdad y quedó marcado en los tres
   archivos. **Vale una segunda confirmación en campo.**
2. **Cuántas camas tienen Inv 3A e Inv 3B** — hay área por cama pero no cuántas,
   así que no suman al total. **Subió de prioridad:** es la que despeja la
   discrepancia de 3C-A. `01-invernaderos.md` dice que Inv3A + Inv3C suman
   556 m²; con 3C en 102,6 quedan 453,4 m² para 3A, que son **12,72 camas** de
   35,64 — no es entero. Con el 3C anterior daban 10,68, tampoco. Así que
   **uno de los tres datos está mal**: el 556 de la zona, el área por cama de
   3A, o la sección A de 3C. Saber cuántas camas tiene 3A resuelve los otros
   dos.
3. **`MADRES` y `AMOR`** en la columna `Inicio cosecha` de `campo_siembras.csv`
   son nombres de evento comercial, no meses. `MAYO MADRES` confirma que Madres
   es mayo; `AMOR` sola no se deduce. Son ~13 filas y hoy quedan sin ubicar.

Y una cuarta que salió de esta sesión:

4. **¿Qué hacer con las 7 ramas sueltas?** Se auditó una octava que no estaba en
   la tabla anterior: **`claude/analisis-bloques-gfv7w1`** (2026-09-09), que trae
   trabajo de inoculación presiembra, hoja de camas v10 y `paleta_color.csv`
   con 178 líneas de cambios. No se tocó.
