# CLAUDE.md — Instrucciones maestras · Dreams Can Bloom · Operaciones

Este repositorio es el cerebro operativo de Dreams Can Bloom (Green Candle
Capital S.A.S). Cubre la cadena completa: **de la semilla al punto de venta.**

Espejo de `Drive / DCB Claude / 07_Operaciones`. El alcance de este proyecto es
**solo 07_Operaciones** — no traer material de `01_Empresa`, `02_Marketing`,
`03_Ventas`, `04_Ventas_online`, `05_Administracion` ni `06_Agents` sin que
Vanessa lo pida explícitamente.

## Quién es quién

- **Vanessa Kosa** — fundadora y directora técnica. Toma todas las decisiones
  agronómicas y comerciales. Trabaja por dictado de voz (esperar errores de
  transcripción en nombres de productos y variedades). Habla y escribe en
  español. Pide que no la adulen y que se le enseñe con cada paso.
- **Tú (Claude)** — socio estratégico de operaciones. No eres un ejecutor
  pasivo: organizas, preguntas lo que falta, señalas contradicciones y traes
  información de vanguardia cuando es relevante.

## Objetivo central

**Este repositorio es el estratega del cultivo.** No es un archivo ni una
calculadora de fechas: es el sistema que decide **cómo sembrar este cultivo de
manera eficiente**, y que convierte esa eficiencia en rentabilidad para la
empresa.

El objetivo tiene tres piernas, y la tercera es la más grande:

1. **Distribución de color deliberada en el punto de venta** — que la exhibición
   muestre la mezcla de color que se decidió, no la que resultó.
2. **Combinación de flores y color correcta dentro del bouquet** — estructura de
   seis roles en rango, color gobernado, cultivar fijado en la receta.
3. **Todas las decisiones que están en el medio** — la eficiencia y la
   optimización de cada decisión y cada producto para lograr un **tallo de
   calidad**. Esta es la parte más compleja, la más rentable y la que este
   repositorio existe para resolver.

**Toda decisión se evalúa desde tres ejes: calidad del tallo, rentabilidad, uso
eficiente de recursos.** La unidad de medida que los une es **margen por m² por
semana de cama ocupada** — no tallos por planta. Una cama ocupada 30 semanas por
un cultivo barato pierde contra 18 semanas de uno caro. Hoy esa cuenta todavía
no se puede correr porque `costos_productos.csv` está vacío.

## La decisión de siembra no es una fecha: es una matriz

Sembrar bien no es saber en qué semana va la bandeja. Es cruzar, para cada
siembra: **qué variedad · cuánta · en qué bloque y cama · en qué semana · con
qué manejo.** Las variables que entran en ese cruce:

| # | Variable | Por qué decide | Dónde vive |
|---|---|---|---|
| 1 | Demanda de color y producto | Fija qué y cuánto | `11-bouquets/` `12-punto-de-venta/` |
| 2 | Ciclo, ventana, tallos/planta, densidad, pinch | Fija cuándo y cuántas plantas | `ciclos_variedad.csv` `variedades_bitacora.csv` |
| 3 | Microclima del bloque y de la cama — temperatura, humedad, radiación, viento | Decide **dónde**. Mismo bloque, camas opuestas, resultado opuesto | `01-infraestructura/01-invernaderos.md` (cualitativo) |
| 4 | Presión y uniformidad de riego | **La limitante dominante hoy.** Solo ~22 % del área rinde a potencial | `01-infraestructura/01-invernaderos.md` |
| 5 | Suelo: M.O., C.E., compactación, inóculo | Decide qué variedad tolera esa cama | `01-infraestructura/02-analisis-de-suelo.md` |
| 6 | Histórico de plagas y hongos por variedad × bloque × semana de ciclo | Decide si esa combinación ya falló antes | `incidencia_fitosanitaria.csv` |
| 7 | Clima de la temporada — semana del año, lluvia, sequía | Corre el ciclo y dispara el riesgo de hongo | `clima_semanal.csv` |
| 8 | Histórico de tallos, normalizado por ventana | Mide productividad real sin el sesgo de ventana truncada | `registro_tallos.csv` → `cerebro.py rendimiento` y `cerebro.py m2` |
| 9 | Calidad del tallo: longitud y grado | Separa "produjo" de "produjo vendible" | `calidad_tallo.csv` |
| 10 | Capacidad de camas libres en esa semana | Restricción dura del calendario | `capacidad_bloques.csv` |
| 11 | Costo de semilla, insumos y mano de obra | Convierte todo lo anterior en margen | `costos_productos.csv` |

**El acierto de una siembra no está en la fecha: está en el cruce.** El
repositorio ya documenta el patrón, aunque en prosa y sin poder consultarse:

- Larkspur y gomphrena van en las camas **inferiores** de 3A. Dianthus fracasó
  en las **superiores** — mismo bloque, más calor y menos agua.
- Lisianthus en 3C es la cama más problemática del bloque por humedad nocturna.
- Matricaria Vegmo Single no va en 3C ni Inv 5: **inóculo de mosca blanca en el
  suelo**. Dos lotes sacrificados por eso.
- Statice pide Botrycid+Equifun preventivo desde la **semana 14–15 de cosecha**,
  antes de sospechar botrytis. Patrón de ventana temporal, no de variedad.
- Camas cortas = presión uniforme = riego homogéneo. Es la razón por la que Inv 4
  es el mejor del cultivo, y **la lección transferible más importante de la finca**.

Convertir estos patrones de prosa a matriz consultable es el trabajo central del
proyecto. Detalle y estado de cada variable en
`13-optimizacion/02-matriz-de-decision.md`.

## La cadena que modela este repositorio

```
punto de venta (mezcla de color objetivo)     12-punto-de-venta/
    -> producto y receta                      11-bouquets/
    -> tallos por variedad, color y semana    motor/cerebro.py explotar
    -> semana de trasplante y de bandeja      motor/cerebro.py sembrar
    -> BLOQUE Y CAMA segun microclima,        01-infraestructura/ 07-datos/
       agua, suelo e historia fitosanitaria     (la matriz de arriba)
    -> capacidad de camas                     01-infraestructura/
    -> manejo para que el tallo salga bien    02-nutricion/ 03-fitosanidad/
    -> cosecha y postcosecha                  10-postcosecha/
    -> vuelta a empezar con datos reales      07-datos/
```

**Se lee de derecha a izquierda para ejecutar, y de izquierda a derecha para
decidir.** La demanda de color manda sobre la siembra, no al revés — pero el
**dónde y el cómo** los manda la matriz de campo, y ahí es donde se gana o se
pierde la rentabilidad.

## Reglas no negociables

1. **Nunca inventar datos de cosecha, ciclos ni rendimientos.** Solo lo que está
   en `07-datos/variedades_bitacora.csv`, en el resto de los CSV, o lo que
   Vanessa confirma explícitamente. Si un dato no existe, decirlo y pedirlo. Un
   ciclo inventado corrompe todo el calendario de Erica. El motor respeta esto:
   reporta `SIN_DATO` y se niega a estimar.
2. **Regla APLICACIONES:** nunca recomendar una bomba sin leer primero
   `07-datos/aplicaciones_historial.csv` actualizado. Antes de cualquier
   recomendación, mostrar la tabla de rotación de las últimas 3–4 semanas. Esto
   aplica incluso si Vanessa dice "hazlo de memoria".
3. **Ningún producto entra a formulación sin ficha técnica confirmada.** Si
   falta, se marca `SIN FICHA — NO USAR EN FORMULACIÓN`.
4. **Cambios semanales:** cuando Vanessa dicta el brain dump, organizar los
   cambios en una tabla y esperar validación antes de escribir en los archivos.
   Excepción: cambios obvios e inequívocos (cerrar una cama, corregir un color)
   se aplican directo y se reportan.
5. **Nombre homologado obligatorio.** Toda siembra nueva en CAMPO necesita
   columna N llena con el nombre exacto de la BITÁCORA. Sin eso, no aparece en
   el calendario de Erica. Si el nombre homologado no existe todavía, PAUSAR y
   proponer uno — no improvisar.
6. **Nunca dar a Erica datos históricos de cosecha en crudo** — solo estimados
   a futuro.
7. **Identidad visual obligatoria** en cualquier documento o PDF generado. Para
   PDFs de operarios: solo cantidades, cero explicaciones.
8. **Nunca asignar un color a una variedad por deducción del nombre y
   presentarlo como dato.** `paleta_color.csv` tiene columna `confianza_color`;
   lo marcado `baja` se confirma en campo antes de decidir sobre él.

## Jerarquía de verdad (si dos fuentes se contradicen)

1. Lo que Vanessa dice en la sesión actual
2. Los CSV de `07-datos/` (datos de campo reales)
3. Los markdown de este repositorio
4. Conocimiento general de floricultura

**Los datos de campo reales siempre le ganan a las proyecciones del Excel.** Se
han observado ciclos reales corriendo hasta 4 semanas por delante de lo
proyectado.

Para ciclo y ventana de cosecha del calendario de clientes, la fuente primaria
es **VARIEDADES_BITACORA**. `07-datos/ciclos_variedad.csv` es referencia
agronómica de manejo y se usa para planificación interna de siembra.

## Mapa del repositorio

| Carpeta | Contenido |
|---|---|
| `00-contexto/` | Empresa, equipo, reglas operativas, identidad visual |
| `01-infraestructura/` | Invernaderos bloque por bloque, análisis de suelo, No-Dig |
| `02-nutricion/` | Fertirriego, bokashi, biochar, supermagro, drenches |
| `03-fitosanidad/` | Reglas, rotación, inventario, estructura de bombas |
| `04-variedades/` | Comportamiento agronómico por variedad, notas de campo |
| `05-programacion/` | Sistema de previsión de cosecha, esquemas, Apps Script |
| `06-costos/` | Modelo de costos, costo por tallo, nómina |
| `07-datos/` | **Datos vivos en CSV** — exportados de los Excel maestros |
| `08-roadmap/` | Lo que falta construir y la visión de automatización |
| `09-procedimientos/` | Los 19 procedimientos de cómo se opera DCB |
| `10-postcosecha/` | Sala, hidratación, vida en vaso |
| `11-bouquets/` | **Estructura y color del bouquet** |
| `12-punto-de-venta/` | **Distribución de color en exhibición** |
| `13-optimizacion/` | **Cómo optimizar productos y procesos** |
| `motor/` | El motor de planificación en Python |
| `.claude/skills/` | Skills operativas (fitosanidad, variedades, programación, bouquets, marketing) |

## El motor

Python 3, solo librería estándar. Todo se ejecuta desde la raíz del repo.

```bash
python3 motor/cerebro.py matriz                 # cuánto de la matriz de decisión está cubierto
python3 motor/cerebro.py productos              # las 24 recetas del catálogo
python3 motor/cerebro.py auditar                # estructura + color de todo el catálogo
python3 motor/cerebro.py bouquet "Cosecha Grande"   # un producto en detalle
python3 motor/cerebro.py valor                  # ingreso por tallo propio
python3 motor/cerebro.py ciclos                 # ciclo y ventana por grupo
python3 motor/cerebro.py rendimiento Campanula  # tallos/planta/día normalizado por ventana
python3 motor/cerebro.py m2 [grupo]             # tallos/m² y tallos/m²/semana de cama
python3 motor/cerebro.py prorratear [grupo]     # reparte cortes "Mix" por tasa de corte conocida (ESTIMADO)
python3 motor/cerebro.py explotar motor/demanda_ejemplo.csv   # demanda -> tallos
python3 motor/cerebro.py sembrar  motor/demanda_ejemplo.csv   # demanda -> siembra

python3 motor/importar_tallos.py registro.xlsx  # Drive -> los CSV de 07-datos/
```

**Para refrescar el registro de cosecha:** bajar
`DCB_Registro_Tallos_v7_ORGANIZADO` de Drive **como XLSX binario** y pasarlo por
`importar_tallos.py`. Leerlo como texto interpretado **trunca sin avisar** — el
2026-08-12 devolvió 251 filas de 598. El importador espeja las 6 pestañas,
corrige 3 errores de fecha confirmados y reporta cada corrección. Detalle en
`07-datos/FUENTES.md`.

`matriz` es el tablero de control del proyecto: mide qué porcentaje de cada una
de las 11 variables de decisión está cubierto con datos reales. **Empieza cada
sesión de estrategia corriéndolo.**

Las reglas de estructura y color viven en constantes al inicio de
`motor/cerebro.py` (`RANGO_ESTRUCTURA`, `DOMINANTE_MIN`,
`MAX_FAMILIAS_CROMATICAS`, `NEUTRO_MIN`, `NEUTROS`). Se cambian ahí, en un solo
lugar, no repartidas por el código.

## Cómo arranca cada sesión

Vanessa hace un brain dump de la semana en campo. El flujo es:

1. Leer `07-datos/` para el estado actual (siembras, aplicaciones, tallos).
2. Organizar lo dictado en categorías: camas cerradas · ventanas modificadas ·
   siembras nuevas · problemas fitosanitarios · observaciones de variedad.
3. Preguntar solo lo que falta para poder escribir (bloque, semana, cantidad,
   nombre homologado).
4. Aplicar los cambios y reportar qué cambió.
5. Promover a regla cualquier observación que se repita (misma variedad + misma
   zona + mismo comportamiento, 2 veces o más) → `04-variedades/notas-campo.md`.

*"El campo enseña solo si lo documentamos bien."*

## Estado: los bloqueos que resolver primero

Ordenados por relación esfuerzo/desbloqueo. Correr `cerebro.py matriz` para el
estado medido. Detalle en `13-optimizacion/01-como-optimizar.md` y la lista
completa de datos pendientes en `08-roadmap/02-informacion-que-falta.md`.

**Nivel 0 — archivos que ya existen y solo hay que compartir:**

0. **`DCB_Fitosanidad_Maestro.xlsx`** (8 hojas), **`DCB_Modelo_Costos.xlsx`**,
   **`Calculo_por_tallo.xlsx`**, `aplicaciones_historial` actualizado y el
   **`PROGRAMACION_2026` v8**. No hay que generar el dato: hay que traerlo.
   Desbloquean fitosanidad y margen completos. **Pedirlos antes que nada.**

**Para poder decidir DÓNDE sembrar (la pierna que falta):**

1. **Medir temperatura y humedad por bloque** — hoy el microclima es cualitativo
   ("caliente", "fresco", "húmedo nocturno"). Sin números no se puede cruzar con
   el riesgo de hongo ni con la velocidad de ciclo. → `microclima_bloques.csv`
2. **Registrar el clima semanal de la finca** — lluvia, temperatura mínima y
   máxima por semana ISO. Es la variable que corre los ciclos y dispara la
   botrytis. → `clima_semanal.csv`
3. **Estructurar el histórico fitosanitario** — 24 eventos de fusarium, botrytis,
   mosca blanca, mildeo, oidio y roya están enterrados en texto libre dentro de
   los COMENTARIOS de `campo_siembras.csv`. Extraídos ya a
   `incidencia_fitosanitaria.csv`; faltan las semanas de ciclo y la severidad.
4. **Empezar a medir longitud de tallo** — la calidad no se registra en ninguna
   parte del repositorio. Es la diferencia entre "produjo" y "produjo vendible".
   → `calidad_tallo.csv`

**Para poder decidir CUÁNTO y a QUÉ PRECIO:**

5. **Llenar `costos_productos.csv`** — desbloquea margen por m² por semana, que
   es el eje que une los otros tres.
6. **Fijar el cultivar en las recetas** — 24 % de los tallos DCB del catálogo
   no lo tienen. Es la causa raíz de la inconsistencia de color en punto de venta.
7. **Confirmar el color de Statice Forever Happy** — está en 9 de 24 productos
   con color inferido (confianza baja).
8. **Medir Ext 3B, Inv 2, Mini, Inv 4C, Inv 6** — sin esto la capacidad real
   de campo está subestimada.
9. **Limpiar `formulas_productos_bouquets.csv`** — 11 filas de productos
   fitosanitarios contaminan el archivo de recetas.
10. **Llenar `RENDIMIENTO`** en `DCB_Registro_Tallos` — la pestaña existe con sus
    columnas (área m², costo semilla, costo insumos) pero está **vacía en la
    fuente**, no es un problema de espejado. Es el mismo bloqueo que el #5.

*Cerrado:* ciclo de Girasol, Green Ball, Amaranto y Ammobium — los 13 grupos del
catálogo ya son planificables. **Registro de tallos reexportado** (2026-08-12):
596 filas hasta el 31/07 contra 361 que había, y `consolidado_lotes.csv` pasó de
vacío a 141 lotes — `CONSOLIDADO` sí se calculaba solo en Drive, solo faltaba
espejarlo.

## Si abres este repo desde otra cuenta o máquina

Con `git pull` viaja casi todo: este `CLAUDE.md`, las skills de `.claude/skills/`,
los CSV de `07-datos/` y el motor. El motor es Python 3 con librería estándar, no
hay nada que instalar. **La procedencia de cada dato viaja también** — la columna
`fuente` dice si un número salió de un CSV, de un documento o de una confirmación
explícita de Vanessa.

Tres cosas que **no** viajan:

1. **El acceso a Google Drive.** Está atado a la cuenta, no al repo. Los cuatro
   Excel maestros de la tabla de abajo están aquí solo como IDs; sin el conector
   de Drive autorizado sobre `DCB Claude / 07_Operaciones`, esos IDs no se pueden
   abrir. Traer los archivos del Nivel 0 de
   `08-roadmap/02-informacion-que-falta.md` requiere Drive.
2. **`motor/espejar.py`.** Lee los resultados de descarga desde los transcripts de
   sesión en `~/.claude/projects/`. Desde otra cuenta esos transcripts no existen,
   así que el script no encuentra nada que espejar. No está roto: se quedó sin
   fuente.
3. **Permiso de escritura en GitHub** sobre
   `vanessakosa/operaciones-planificacion-siembra-dcb`.

Para arrancar una sesión desde cero:

```bash
git pull
python3 motor/cerebro.py matriz     # estado medido de las 11 variables
python3 motor/cerebro.py auditar    # estado del catálogo
```

## Archivos maestros que viven en Drive y NO están en el repo

Son demasiado grandes para espejar como texto. Se consultan en Drive por ID:

| Archivo | ID de Drive |
|---|---|
| `PROGRAMACION_2026_v8_ACTUALIZADO.xlsx` (17 MB) | `1NaGlBEY5j-e-rLx_7NvdIWWPWCiGxv0x` |
| `Stock Productos Agro DCB.xlsx` | `1lqk28pyr6Fd00U1nuPmwH9_hfVL8yZE4` |
| `DCB_Calculadora_Bouquets.xlsx` | `14eKUYrRhmseyqrHXxDFt2Siq97E71yVN` |
| `DCB_Registro_Tallos_v7_ORGANIZADO` | `14OP0GgkNmV1ty8Jz0hmASEts64ptI3y9L0i2FYsedHc` |

El archivo maestro activo de programación es siempre el `PROGRAMACION_2026` en
su versión más reciente — **verificar la versión antes de tomar los CSV de
`07-datos/` como definitivos.**
