# Dahlia · protocolo completo para las 160 italianas

> **Fecha:** 2026-09-09 · semana ISO 37
> **Alcance:** 160 dalias italianas de regalo — presiembra, inoculación, siembra,
> posiembra, fertilización, control fitosanitario y nutrición foliar.
> **Estado:** propuesta técnica. Tres decisiones necesitan confirmación de Vanessa
> antes de ejecutar (ver *Lo que falta confirmar*, al final).

---

# 1 · El diagnóstico primero: por qué fallaron las anteriores

Vanessa describe el patrón: **éxito cuando la cama estaba bien preparada, con mucha
M.O., con bombas de aspersión y trabajos culturales; mildeo polvoso al final del
ciclo siempre; y últimamente mildeo persistente + pulgones, con estrés hídrico y
achicopalamiento al mediodía.**

Ese patrón no es cinco problemas. Es **una cadena de tres eslabones**, y el
repositorio ya tiene los datos para nombrarla.

## 1.1 · Lo que dicen los datos propios

| Fuente | Dato |
|---|---|
| `campo_siembras.csv` | Lote Ball, 696 plantas, siembra 2025-11-11 (sem 46), Bloque 2: *"Ya semana 6 poco productivas, no me gustaron"* |
| `campo_siembras.csv` | Lote DCB, 100 plantas, Bloque 2: *"Empezaron en la 15, semana 21 floración pero **mildeo persistente, insectos y mildeo semana 24**"* |
| `incidencia_fitosanitaria.csv` id 8 | Dahlias · Inv 2 · MILDEO · semana 21 · **PERSISTENTE** · EN_MANEJO |
| `registro_tallos.csv` | **90 tallos en total**, 2 registros (2026-08-09 y 2026-08-12), Bloque 2 |
| `microclima_bloques.csv` | Inv 2 = `TANQUE_EN_REPARACION` · `SIN_HISTORIAL_FERTIRRIEGO` |
| `capacidad_bloques.csv` | Inv 2 = `NO UNIFORME` — *"camas de distinta medida"* |
| `01-invernaderos.md` | Inv 2 es **el invernadero más irregular de la finca**, y es donde se ensaya *por eso* |
| `variedades_bitacora.csv` | Dahlia · ciclo 16 sem · ventana 4 · calidad ★★★ · B2B, pedidos por encargo |
| `ciclos_variedad.csv` | Ciclo **12 semanas CONFIRMADO** por Vanessa 2026-08-13 (deja sin efecto el 16). Ventana **sin confirmar** (bitácora 4, PROGRAMACION 6) |

**Las dalias han estado sembradas en el peor bloque de la finca para agua, sin
fertirriego, en camas de largo desigual.** No hay que explicar el fracaso con la
variedad: el sitio ya lo explica.

## 1.2 · La cadena causal, eslabón por eslabón

**Eslabón 1 — el agua.** Inv 2 no tiene fertirriego y su tanque estuvo fuera de
servicio. La dalia es de los cultivos de mayor demanda hídrica del catálogo: hoja
enorme, transpiración alta, raíz tuberosa relativamente superficial. El
achicopalamiento de mediodía que Vanessa describe **es el síntoma exacto** de
esa combinación.

**Eslabón 2 — el calcio nunca llegó, y los pulgones tuvieron su comida.** Aquí el
repositorio ya hizo el trabajo, en `02-nutricion/04-diagnostico-kempf-ingham.md`:

> *"El Ca no se absorbe activamente — entra por flujo de masa arrastrado por la
> transpiración. Sin transpiración no hay entrega de Ca al tejido en crecimiento,
> aunque el suelo esté lleno. **En DCB el Ca no es problema de dosis, es problema
> de entrega.**"*

Una planta que cierra estomas al mediodía todos los días **no puede recibir
calcio**, por mucho que el suelo lo tenga (Ca soluble está ALTO en los tres
bloques). Y en paralelo, la planta bajo estrés hídrico acumula **aminoácidos
libres y N soluble en el floema** — que es literalmente el alimento del pulgón.
Eso es la **Falla de Fase 1** que el propio diagnóstico Kempf ya tenía escrita
para la mosca blanca de matricaria y el fusarium de lisianthus. **El pulgón de la
dalia es el mismo fallo, en otra variedad.**

**Eslabón 3 — el mildeo polvoso llegó porque la Fase 3 nunca se construyó.** Las
dalias recibieron **solo bokashi en la base y bombas generales**. El diagnóstico
propio dice cuáles son los dos limitantes de Fase 3 (síntesis de lípidos =
inmunidad a hongos aéreos) en DCB:

| Cofactor | Bloque 4 | Veredicto del repo |
|---|---|---|
| **Cu** | 3,7 M | Limitante clásico |
| **P soluble** | **0,107 B** | **Bajo en los tres bloques** |
| P total | **10,74 B** | **Bloque 4 es el ÚNICO candidato a fuente mineral de P** |
| B | 1,64 M | Suficiente, no holgado |

El bokashi no aporta Cu ni P soluble en cantidad relevante — aporta **K**, sobre
un suelo que ya está en **saturación de K de 24–30 %**. Es decir: la única
fertilización que recibieron las dalias empujaba justamente el elemento que
sobra, y no tocaba ninguno de los dos que faltan.

## 1.3 · El detalle que Vanessa ya había encontrado sin saberlo: las bombas de aspersión

Vanessa lista, entre las condiciones de sus **casos de éxito**, que *"teníamos
bombas de aspersión"*. **Eso no es un detalle de contexto: es probablemente el
control de mildeo más eficaz que ha tenido, y desapareció.**

El mildeo polvoso es la única enfermedad fúngica importante que **se comporta al
revés que todas las demás**:

| | Botrytis, mildeo velloso, fusarium | **Mildeo POLVOSO (oídio)** |
|---|---|---|
| ¿Necesita agua libre en la hoja para germinar? | **Sí** | **No — y el agua libre lo MATA** |
| Efecto del riego por aspersión | **Empeora** la enfermedad | **La reduce** |

Los conidios de mildeo polvoso **germinan mal o no germinan en agua libre, y
cuatro o más horas de exposición a agua libre los daña** (UC IPM; ver
bibliografía). Germinan en aire con humedad relativa alta *dentro del dosel*
(97–99 % de noche) sin necesidad de mojado. Por eso el mildeo polvoso es
**peor bajo cubierta que a campo abierto**: bajo plástico no hay lluvia que lave
y reviente los conidios.

**Conclusión operativa:** el lavado de dosel a mediodía vuelve al protocolo como
intervención central, no como accesorio. Y resuelve dos problemas con una sola
acción, porque también baja la temperatura de hoja en la hora del
achicopalamiento. Detalle de ejecución en la **Etapa 5**.

## 1.4 · Y por qué el mildeo llegaba *siempre al final del ciclo*

Tres cosas coinciden al final del ciclo de una dalia y las tres favorecen al
oídio:

1. **El dosel se cierra.** Máxima área foliar → humedad de dosel alta de noche →
   condición óptima de germinación.
2. **La hoja vieja se vuelve susceptible.** Al entrar en floración la planta
   removiliza N de las hojas basales hacia flores y tubérculos; ese tejido
   senescente es el sustrato preferido del oídio.
3. **En DCB, además, la planta está tuberizando.** Ver la sección 2 — a esta
   latitud la dalia recibe señal de día corto todo el año, y el drenaje de
   asimilados hacia el tubérculo compite con el mantenimiento del dosel.

Es decir: **el mildeo de final de ciclo no es mala suerte, es fenología.** Se
combate construyendo Fase 3 *antes* — que es exactamente lo que el diagnóstico
Kempf ya dice para la botrytis de statice:

> *"La botrytis de la semana 16 se decide en la prefloración, seis a ocho
> semanas antes."*

---

# 2 · El hallazgo que reordena el protocolo: la luz

Vanessa dice que las dalias italianas **"requieren luz"**. Esto contradice
directamente el repositorio:

> `07-datos/variedades_parametros_siembra.csv` → fila `Dahlias`, columna
> **`Light` = NO**

Esa columna **no es decorativa**: en el mismo archivo, Campanula, Celosia
Cristata, Celosia Plumosa y Bupleurum tienen `Light = SI`, y Anémonas y
Ranúnculos tienen `SARAN`. **DCB ya practica manejo de luz en otras variedades.**

Por la jerarquía de verdad del repositorio (lo que Vanessa dice en sesión gana
sobre el CSV), **la fila de Dahlias está mal y hay que corregirla.** Y la
literatura explica por qué, con un mecanismo que además cierra el diagnóstico de
la sección 1.

## 2.1 · La dalia es planta de día corto facultativa, y Bogotá es día corto todo el año

| Hecho | Consecuencia en DCB |
|---|---|
| La dalia forma tubérculo con **fotoperiodo < 12 h**, y días de 16 h lo inhiben | A ~4–5° N el día dura **~12 h 05 min los 365 días**. La señal de tuberización **nunca se apaga** |
| La tuberización es máxima entre **15 y 20 °C**, y cae por encima de 25 °C | La Sabana está justo en la ventana óptima de tuberización |
| Es **día corto facultativa** para floración: noches largas → florece antes | Florece temprano, con planta pequeña y **tallo más corto** |
| Interrupción nocturna (NI) de ~4 h a mitad de noche **retrasa la floración y alarga el tallo** | Es la palanca de longitud de tallo que DCB no está usando |

En el ensayo de referencia sobre *Dahlia hortensis* (día de 9 h ± 4 h de
interrupción nocturna con distintas relaciones R:FR), **la longitud de tallo
aumentó de forma cuadrática al subir la R:FR de la interrupción**, y la
floración quedó **incompleta bajo día corto puro y bajo NI de solo rojo lejano**.

**Traducción para DCB:** a esta latitud una dalia sin manejo de luz está siendo
empujada permanentemente a **florecer temprano y mandar asimilados al tubérculo**
en vez de a construir tallo. Es la explicación más probable de *"ya semana 6 poco
productivas"* — y encaja con que el proveedor italiano advierta que **requieren
luz**.

## 2.2 · Recomendación de luz

> **Interrupción nocturna (NI) de 4 horas, de 22:00 a 02:00, desde el trasplante
> hasta la semana 7 post-trasplante. Después se retira y se deja florecer.**

- **Intensidad:** baja — la NI es una señal fotoperiódica, no fotosíntesis.
- **Espectro:** luz **blanca o rica en rojo**. **No usar rojo lejano solo** — en
  el ensayo la floración quedó incompleta.
- **Ahorro:** la NI **cíclica** (pulsos cada 20–30 min dentro de la ventana)
  reduce el consumo hasta ~80 % con retraso de floración mínimo.
- **Costo en calendario:** retrasa el inicio de cosecha. Con ciclo base de 12
  semanas, **contar 14–15 semanas** con NI hasta semana 7. Ese retraso **se paga
  en longitud de tallo**, que es donde está el precio en un producto ★★★ de B2B
  por encargo.

⚠️ **Esto NO se aplica a ciegas.** Ver la pregunta 2 al final: hay que saber si
lo que dijo el proveedor es fotoperiodo (esto) o simplemente pleno sol (otra
cosa). Y hay que confirmar qué equipo de iluminación existe hoy en la finca —
el `Light = SI` de Campanula sugiere que sí hay algo.

## 2.3 · Y "luz" en el sentido de radiación: dónde NO sembrarlas

Independiente del fotoperiodo, la dalia es cultivo de **alta radiación**. Quedan
descartados por `microclima_bloques.csv`:

| Zona | Por qué se descarta |
|---|---|
| **Mini** | `radiacion_rel = BAJA` — sombra de pinos, producción históricamente menor |
| **Inv 3C** | `radiacion_rel = BAJA`, húmedo nocturno, inóculo de mosca blanca en suelo |
| **Inv 2 zona baja** | Sombreada |
| **Ext Inv2** | Sombra de frutales |

---

# 3 · Dónde van: bloque, cama y densidad

## 3.1 · El bloque

> **Inv 4A e Inv 4B.**

**Razón — la limitante dominante de la finca es el agua, y la dalia es el cultivo
que más la castiga.** `CLAUDE.md` lo dice de frente: *"solo ~22 % del área rinde a
potencial"* por presión y uniformidad de riego, y *"camas cortas = presión
uniforme = riego homogéneo… la lección transferible más importante de la finca"*.

| Candidato | Uniformidad de riego | Radiación | Veredicto |
|---|---|---|---|
| **Inv 4A** | `ALTA_UNIFORME` / `UNIFORME` · M.O. **25,6 %** | Media | ✅ **Elegido** |
| **Inv 4B** | `ALTA_UNIFORME` / `UNIFORME` | Media | ✅ **Elegido** |
| Inv 4C | `ALTA_UNIFORME` pero **camas largas**, con alerta *"revisar si pierden uniformidad"* | Media | Segunda opción |
| Inv 2 | `TANQUE_EN_REPARACION`, `NO UNIFORME`, el más irregular | Alta/media | ❌ **Donde fallaron** |
| Inv 5 | `LA_PEOR_DEL_SISTEMA` en presión de agua | Media | ❌ |
| Exterior (Inv 6, Ext 4) | Ventilación ALTA y lluvia — **lo mejor contra oídio** | Alta | ⚠️ ver 3.2 |

## 3.2 · Por qué no van afuera, aunque el oídio lo pediría

A campo abierto el oídio se controla casi solo: llueve, y la lluvia lava y
revienta los conidios. Es como se produce dalia comercialmente en casi todo el
mundo. **Pero aquí hay dos riesgos que no valen sobre 160 plantas de regalo:**

1. **Heladas.** Sembradas ahora (sem 38–39), con NI hasta la semana 7, la cosecha
   cae en **diciembre–febrero**, que es la ventana clásica de heladas en la
   Sabana. La dalia es **sensible a helada — una noche la mata**. Y
   `clima_semanal.csv` **está vacío**: la finca no tiene un solo registro de
   temperatura mínima semanal con el que dimensionar ese riesgo. Decidir a favor
   del exterior hoy sería decidir a ciegas.
2. **La flor.** La lluvia directa daña el capítulo de las dalias decorativas y
   dispara botrytis en la flor abierta.

> **Decisión:** las 160 van bajo cubierta, en las camas de riego más parejo de la
> finca, y el oídio se ataca con las cinco palancas de la sección 7 —
> **empezando por el lavado de dosel, que reproduce bajo plástico lo que hace la
> lluvia afuera.**
>
> El ensayo exterior vale la pena, pero **con los hijos de la primera división**,
> no con el regalo, y programado para salir de la ventana de heladas.

## 3.3 · Densidad — aquí hay un error a corregir

`variedades_parametros_siembra.csv` dice **`DISTANCIA SIEMBRA = 15 cm`** para
Dahlias. Con la retícula de la finca (8 líneas a 15 cm × huecos cada 15 cm) eso
son **~44 plantas/m²**.

**Para una dalia eso es entre 8 y 12 veces demasiado denso.** La referencia
comercial de dalia de corte es **30–45 cm entre plantas** (12–18 pulgadas, más
para tipos dinnerplate). Y la densidad excesiva es **causa directa de oídio**:
dosel cerrado → humedad de dosel alta de noche → la condición exacta que el
patógeno necesita.

> **Marco propuesto: 2 líneas × 1 planta cada 3 huecos.**

| | Valor |
|---|---|
| Líneas usadas de las 8 | **líneas 2 y 7** → **75 cm entre líneas** |
| A lo largo de la cama | **1 planta cada 3 huecos** → **45 cm** |
| Densidad resultante | **3,7 plantas/m²** |
| Plantas por cama de 112 huecos (Inv 4A o 4B) | **74** |
| **Inv 4A + Inv 4B** | **148 plantas** |
| **Reserva en materas** | **12 plantas** para reponer fallos |
| **Total** | **160** ✅ |

Las 12 de reserva no son sobra: en una colección de regalo **siempre se guarda
material de reposición**, y sirven además como testigo sano si aparece virosis
(sección 4.3).

**El corredor central de 75 cm entre las dos líneas es deliberado:** es el
pasillo de aire que baja la humedad del dosel, y es por donde se entra a
desbotonar, deshojar y cosechar sin pisar la cama.

---

# 4 · Etapa 0 · Recepción y sanidad del material

⚠️ **Esta etapa tiene dos versiones porque falta un dato.** El repositorio dice
que la Dahlia entra como **"Bulbos externos"** (`variedades_bitacora.csv`), así
que la **ruta A (tubérculo) es la que se asume por defecto**. Si llegan plántulas
o esquejes enraizados, aplica la ruta B.

## 4.1 · Ruta A — llegan tubérculos

| # | Paso | Detalle |
|---|---|---|
| 1 | **Inspección planta por planta** | Descartar tubérculos blandos, con pudrición seca, o con costra fúngica blanca a rosada — **eso es Fusarium**, la causa más común de pudrición seca de tubérculo, y sobrevive indefinidamente en el suelo |
| 2 | **Cirugía si vale la pena** | Cortar la zona podrida hasta tejido sano y sellar el corte con **azufre + cal hidratada 50:50**. Solo si el cultivar es irremplazable |
| 3 | **Cuello vivo obligatorio** | Un tubérculo sin yema visible en el cuello **no brota**. Se descarta o se etiqueta como dudoso y va aparte |
| 4 | **Cuchillo desinfectado entre plantas** | **Hipoclorito 10 % un minuto, o alcohol 70 %**, entre cada tubérculo. Es transmisión mecánica de virus, no formalismo — ver 4.3 |
| 5 | **Etiquetar cultivar uno por uno** | Sin esto no hay receta de bouquet ni color de punto de venta posible |
| 6 | **Bodega hasta sembrar** | Fresco, seco, aireado, **nunca en bolsa cerrada** |

## 4.2 · Ruta B — llegan plántulas o esquejes enraizados

Entran al protocolo de bandeja estándar de DCB tal cual está escrito en
`02-nutricion/10-protocolo-inoculacion-por-etapas.md` — ver Etapa 2.

## 4.3 · 🔴 El punto que decide si esta colección dura años o una temporada

**El virus del mosaico de la dalia (DMV) se transmite por 16 especies de pulgón,
de forma NO PERSISTENTE, y se hereda en el tubérculo.**

Tres consecuencias, todas contraintuitivas y todas importantes:

1. **Los insecticidas no previenen la virosis.** En transmisión no persistente el
   pulgón adquiere e inocula el virus **en segundos**, antes de que cualquier
   insecticida lo mate. Matar pulgones reduce la población, no la transmisión.
2. **Lo que sí funciona son los aceites minerales.** En bulbosas ornamentales las
   aspersiones de aceite mineral fueron **significativamente más eficaces que los
   piretroides, que rindieron en promedio la mitad**. El mecanismo es directo:
   el aceite **interfiere la retención de viriones en el estilete y el
   proventrículo del pulgón**. **DCB tiene Agroemulsión en inventario** (700 cc,
   aceites, *"asfixia: ácaros, mosca blanca, áfidos"*).
3. **Un tubérculo infectado infecta para siempre.** Si se multiplica, se
   multiplica el virus. Por eso la regla de cuchillo desinfectado y por eso hay
   que marcar y sacar las plantas con síntoma (mosaico, aclaramiento de nervadura,
   enanismo) **antes** de la división.

> **Regla que se propone para el repositorio:** *en dalia, el objetivo del
> programa de pulgón no es la plaga — es el virus del stock. Se mide en plantas
> sintomáticas descartadas por temporada, no en pulgones vivos.*

**Nota de manejo:** las plantas con síntoma **no se descartan antes del pinch**.
La práctica de los productores especializados es esperar a que la planta esté
establecida y haya recibido nitrógeno, porque muchas sospechas resultan ser
deficiencia nutricional o daño de trasplante, no virus.

---

# 5 · Etapa 1 · Presiembra — preparación de cama

Se sigue **la v10 de `01-infraestructura/06-formulacion-camas-v8.md`** sin
inventar nada, con **una sola adición justificada** para dalia.

## 5.1 · El armado v10, tal como está

| # | Paso |
|---|---|
| 1 | **NO voltear la cama.** Aflojar **solo donde esté compactada** |
| 2 | Mezclar **Bokashi + leonardita** — y **yeso**, porque Inv 4 es Bloque 4 — y aplicar **EN SUPERFICIE**. No enterrar |
| 3 | Nivelar la superficie sin remover |
| 4 | Riego suave, **con agua sola** |
| 5 | **Inocular el suelo. SIEMPRE.** (Etapa 2) |
| 6 | Poner el **plástico** |

**Dosis para Inv 4A y 4B (20,2 m² cada una), de la tabla v10 ya redondeada:**

| Producto | Dosis | Base |
|---|---|---|
| Bokashi V1 | 1 saco de 25 kg por cama = **1,24 kg/m²** | tabla v8/v10 por cama |
| **Black Diamond GR** (leonardita) | **130 g** por cama = **6,5 g/m²** | ficha 2026-09-03, dosis diferenciada inversa a la M.O. |
| **Yeso agrícola** | **2 kg** por cama = **100 g/m²** | solo Bloque 4 |

⚠️ **Incompatibilidad ya registrada:** el Black Diamond granulado es
**incompatible con nitrato de calcio**, que es la línea #1 del tanque. No
coincidir la aplicación de leonardita con un fertirriego de N-Cal.

## 5.2 · La adición para dalia: drenaje del cuello

**Único cambio respecto a cualquier otra cama.** El tubérculo de dalia se pudre
con agua estancada alrededor del cuello, y el suelo de DCB tiene **saturación de
humedad de 133–155 %** y **densidad aparente de 0,56–0,71 g/cm³** — un suelo que
retiene muchísima agua.

> **Sembrar el tubérculo en un lomo o camellón de 10–15 cm sobre el nivel de la
> cama**, no en depresión. El agua se va, la corona queda seca, y el resto del
> perfil sigue húmedo para la raíz.

Esto **no contradice el No-Dig**: es modelado de superficie, no volteo.

## 5.3 · Lo que NO se hace

- ❌ **No se aplica roca fosfórica** aunque el P esté bajo. Salió de la fórmula y
  el problema es de **P soluble**, no de P total — el P total de Bloque 4 ya es
  10,74 y sigue sin ser disponible. La vía correcta es biológica (Fosfolip,
  Etapa 2) y foliar (Etapa 6).
- ❌ **No se agrega potasio en ninguna forma.** Bloque 4: saturación de K **30 %**
  contra un rango de balance de 2–5 %.
- ❌ **No se agrega magnesio.** Saturación de Mg **32,1 %** contra 10–20 %.
- ❌ **No se voltea a 25–30 cm.** Destruye el Trichoderma de 1,4×10⁶ UFC/g, que es
  justamente lo que protege a la dalia del Fusarium de Inv 4A.

---

# 6 · Etapa 2 · Inoculación

## 6.1 · Cama — el estándar de la finca, sin cambios

> **En CADA bomba de 20 L: 1,5 cc de Fosfolip.** Se mojan 80–100 L por cama
> (4–5 bombas). Riego de arrastre con agua sola inmediatamente después, **antes
> del plástico**.

Base: 0,20 cc/m², que es 2× etiqueta, elegido tanto por carga de suelo como
porque a 1× no se mide con jeringa. Da **2,10 L/ha en toda cama**, sin tabla.

**Por qué solo Fosfolip:** por la regla del repositorio — *"BANDEJA = lo que va a
la RAÍZ. CAMA = lo que va al SUELO."* El blanco del Fosfolip (solubilizar el P
del volumen de suelo que la raíz va a explorar) **está en la cama y la bandeja no
lo alcanza**. Y en dalia sobre Bloque 4 este producto vale doble: **Bloque 4 es el
único bloque que el diagnóstico marca como candidato a fuente mineral de P**, y
el **P soluble es uno de los dos limitantes de Fase 3** — la fase que decide el
oídio.

⚠️ **Regla que protege el drench:** **no regar con fertirriego el día de la
inoculación.** El fertilizante químico mata el inoculante.

## 6.2 · Tubérculo — Ruta A

**Aquí sí hay una excepción justificada, y se justifica con la regla propia del
repositorio.** La regla dice: *"¿el patógeno tiene una etapa EN EL SUELO? Un
drench a la raíz solo puede atacar lo que está en el suelo."*

| Patógeno | ¿Etapa en suelo? | ¿Aplica producto dirigido? |
|---|---|---|
| **Fusarium de tubérculo** | **Sí** — *"vive indefinidamente en el suelo"* y `microclima_bloques.csv` marca **Inv 4A: "Fusarium generalizado en suelo"** | 🟢 **Sí** |
| Mildeo polvoso | No — inóculo aéreo | 🔴 No. Solo resistencia inducida |

> **Baño de tubérculo, el día de la siembra, en 5 L de agua:**
>
> | Producto | Cantidad en 5 L | Función |
> |---|---|---|
> | **Endorhiza** | **10 cc** | Micorriza — la única vía al P por exploración de hifas |
> | **Nube** | **10 cc** | *Streptomyces* — resistencia sistémica inducida por fitoalexinas |
> | **Promobac** | **13 cc** | *Bacillus* — segundo género de resistencia inducida; su ficha lista *Fusarium*, *Oidium*, *Botrytis*, *Erysiphe* y *Rizoctonia* |
> | **Fitoderma** | **5 g** | *Trichoderma* — **la excepción**: antagonista directo de *Fusarium*, contra el inóculo documentado de Inv 4A |
>
> **Sumergir 10–15 minutos, escurrir, sembrar en el mismo día. No secar al sol.**

Las tres primeras líneas son **la base de bandeja de DCB tal cual está definida**
(Endorhiza 10 + Nube 10 + Promobac 13 en 5 L). Solo se cambia el vehículo: en vez
de regar una bandeja se sumerge un tubérculo, porque no hay bandeja.

**Sobre el Fitoderma:** el repositorio lo restringe a Inv 3 *porque el Trichoderma
en Inv 4+5 ya está alto (1,4×10⁶ UFC/g)*. La excepción aquí es que **el órgano
que se siembra es un tubérculo carnoso**, el blanco más fácil que existe para
*Fusarium*, entrando a una cama marcada como Fusarium-positiva. **Esto es una
excepción propuesta, no una regla — necesita el visto bueno de Vanessa.**

🟡 **Pendiente heredado que aplica aquí:** las fichas de Bioquirama dicen
literalmente *"consultar al Departamento Técnico"* sobre compatibilidad cruzada
entre *Trichoderma*, micorriza y *Streptomyces*. Es la misma pregunta del correo
que ya está pendiente. Si preocupa, **la alternativa limpia es sacar el Fitoderma
de la mezcla y aplicarlo aparte, al hueco de siembra** — no en otro día, que no
separa nada.

## 6.3 · Ruta B — bandeja

Base estándar sin cambios, en 5 L de agua, un solo pase el viernes:

> **Endorhiza 10 cc + Nube 10 cc + Promobac 13 cc.** Rinde 4 bandejas. Si hace
> falta más agua para mojarlas, se agrega **agua sola**, no más producto.

**Nada extra por el mildeo.** Es enfermedad aérea: un drench no la alcanza. Lo
único que un drench puede hacer contra ella es resistencia inducida, y **eso ya
está en la base** — dos géneros distintos, *Streptomyces* del Nube y *Bacillus*
del Promobac.

---

# 7 · Etapa 3 · Siembra y trabajos culturales

| Práctica | Qué se hace | Cuándo | Fuente |
|---|---|---|---|
| **Profundidad** | Tubérculo **acostado horizontal**, yema hacia arriba, **10–15 cm** de profundidad, sobre el lomo de la 5.2 | Siembra | práctica estándar |
| **Sin riego hasta el brote** | El tubérculo trae su propia reserva de agua; regar antes de que emerja la yema es **la causa #1 de pudrición** | Siembra → emergencia | práctica estándar |
| **Malla — 2 capas, no 1** | `variedades_parametros_siembra.csv` dice `Net = 1`. Con planta de 1–1,5 m y capítulo pesado, **1 capa no sostiene**. Primera a **30 cm**, segunda a **60 cm** | Antes de que la planta las alcance | 🔴 **cambio propuesto al CSV** |
| **Pinch** | Despuntar sobre el **3.º–4.º par de hojas verdaderas**, con la planta a ~30 cm | ~**semana 4** post-trasplante | `variedades_parametros_siembra.csv` (`Pinch = Si, semana 4`) ✅ coincide con la literatura |
| **Desbotone** | Quitar los **dos botones laterales** junto al terminal → un tallo largo con una flor | Cuando los botones son distinguibles | práctica estándar de dalia de corte |
| **Deshoje basal (faldeo)** | Quitar **todas las hojas de los 30–40 cm inferiores** cuando la planta pasa de 60 cm, y repetir | Desde semana 6, cada 2 semanas | **medida anti-oídio directa** |
| **Tallos por planta** | **4** | — | `variedades_parametros_siembra.csv` |

## 7.1 · Por qué el deshoje basal es la medida más subestimada

Hace tres cosas a la vez y no cuesta insumo, solo jornal:

1. **Abre el flujo de aire por la base del dosel** — baja la humedad nocturna del
   dosel, que es la condición que el oídio necesita (97–99 % HR dentro del dosel).
2. **Retira el tejido más susceptible.** La hoja basal senescente es donde el
   oídio arranca siempre.
3. **Quita inóculo físicamente** — y `03-fitosanidad/01-reglas-y-protocolos.md`
   ya lo tiene como regla: *"limpieza física antes de cualquier fungicida —
   tejido afectado en bolsas, fuera del invernadero"*.

Vanessa lo tenía en sus casos de éxito: *"trabajos culturales"*. **Vuelve al
protocolo con nombre, semana y criterio.**

---

# 8 · Etapa 4 · Agua — y el lavado de dosel

## 8.1 · Riego de base

| Etapa | Manejo |
|---|---|
| Siembra → emergencia | **Sin riego.** Humedad residual de la preparación |
| Emergencia → pinch | Riego regular, suelo **húmedo, nunca saturado** |
| Pinch → floración | **Máxima demanda.** Es la etapa donde se pierde el ciclo |
| Cosecha | Sostenido. **El fertirriego NO se suspende bajo presión fúngica** — regla #2 de la finca |

**Nunca regar al atardecer.** El diagnóstico Kempf lo dice para el calcio: la
humedad nocturna alta corta la transpiración y con ella la entrega de Ca. Regar
tarde empeora exactamente el eslabón 2 de la sección 1.

## 8.2 · 🟢 El lavado de dosel de mediodía — la intervención central

> **Aspersión de AGUA SOLA sobre el dosel, entre 10:00 y 13:00, 2–3 veces por
> semana, desde la semana 4 hasta que abra el primer botón de color.**

**Qué hace, y por qué las dos cosas ocurren juntas:**

| Efecto | Mecanismo |
|---|---|
| **Mata el mildeo polvoso** | El conidio de oídio **germina mal o no germina en agua libre**, y **4 h o más de exposición a agua libre lo dañan**. Es lo que hace la lluvia a campo abierto y lo que el plástico impide |
| **Corta el achicopalamiento de mediodía** | Enfriamiento evaporativo en la hora pico de demanda → la planta **no cierra estomas** → **sigue transpirando → sigue entregando Ca al tejido en crecimiento** |
| **Arrastra pulgón y mielato** | Reduce población y limpia la superficie foliar |

**Las tres reglas que hacen que esto no se vuelva un problema:**

1. **Solo entre 10:00 y 13:00.** La hoja tiene que quedar **completamente seca
   antes de la noche**. Mojado nocturno = botrytis, que es el error inverso.
2. **Se suspende cuando abre el color.** El agua sobre pétalo abierto es botrytis
   de flor y mancha de pétalo. A partir de ahí, mildeo se maneja solo por foliar.
3. **No coincide con día de bomba.** El lavado arrastraría el producto. Y
   **nunca el mismo día del drench de inoculación.**

⚠️ Esto **contradice el instinto** de "no mojar la hoja" que es correcto para
botrytis y para mildeo velloso. **Es correcto solo para polvoso**, y por eso va
con hora, ventana y fecha de corte. **Si aparece botrytis, se suspende.**

---

# 9 · Etapa 5 · Fertilización

## 9.1 · Fertirriego — sin fórmula propia

`01-fertirriego-formulas.md` es explícito: *"la foliar es complementaria e
irremplazable para las defensas. **El ajuste fino por variedad se hace en la
foliar, no en el fertirriego.**"* Y operativamente el tanque sirve a Inv 4+5
completo — **no se puede darle a una cama una fórmula distinta.**

Las dalias van con las fórmulas **Inv 4+5 vigentes**, tal cual:

| Producto | Vegetativo | Floración | Tanque 2.000 L |
|---|---|---|---|
| Haifa N-Cal GG | 1.200 g | 1.400 g | Ca — sube en floración porque el Ca es inmóvil |
| Polyfeed 10-10-43 | 600 g | 400 g | ⚠️ ver 9.2 |
| Bitter Mag 16MgO | 600 g | 600 g | ⚠️ ver 9.2 |
| Haifa MKP | **0 g** | **0 g** | Eliminado — P y K saturados en suelo |
| Haifa Micro Hydroponic | 180 g | 180 g | **Siempre 180. No negociable** |
| Fullfert | 100 cc | 100 cc | Húmicos/fúlvicos |

## 9.2 · Y por qué la dalia es el mejor argumento para aprobar el cambio pendiente

La propuesta de **eliminar Polyfeed y Bitter Mag**, pendiente de validación desde
el 2026-09-02, **es más urgente en dalia que en cualquier otro cultivo del
catálogo**, por tres razones que se suman:

1. **Bloque 4 tiene saturación de K en 30 % y de Mg en 32,1 %.** El Polyfeed
   (43 % K₂O) y el Bitter Mag están alimentando los dos elementos que sobran.
2. **El K y el Mg altos bloquean el Ca por antagonismo catiónico** — y el eslabón
   2 del diagnóstico de la dalia es, precisamente, calcio que no llega.
3. **El bokashi ya es una fuente de K no contabilizada** (equinaza + ceniza +
   melaza + king grass, a 1,24 kg/m² en Inv 4). La dalia recibe K por dos vías
   sobre un suelo saturado.

> **Recomendación:** aprobar la eliminación de Polyfeed y Bitter Mag para el ciclo
> Inv 4+5 que empieza con esta siembra. El tanque queda en **N-Cal GG + Haifa
> Micro + Fullfert**, que es más simple y más barato.
>
> **Es decisión de Vanessa, no del protocolo.** Si no se aprueba, las dalias van
> con la fórmula vigente y el déficit de Ca se compensa **solo** por la vía
> foliar y por el lavado de mediodía — que funciona, pero con menos margen.

## 9.3 · Nitrógeno: la cantidad probablemente sobra, la forma está mal

La literatura de dalia de corte da **0,3–0,4 lb N por 100 pie²/año ≈ 15–20 g
N/m²/año**, con la mitad a la siembra y la otra mitad **hacia la semana 8, justo
antes de floración**. La dalia es de N más alto que la media de las flores de
corte.

**Pero:** el bokashi V1 a 1,24 kg/m² es equinaza + king grass + melaza. A
cualquier contenido razonable de N, ese aporte está **en el mismo orden de
magnitud que el requerimiento anual completo** — antes de contar una sola gota
del tanque.

🔴 **No se puede cerrar el número, y el bloqueo ya está identificado en
`CLAUDE.md` como el pendiente 4c:** *"Análisis del Bokashi terminado — sin este
dato el balance de nutrientes no cierra."* **Este protocolo es una razón más para
pedirlo.**

Lo que sí se puede decir sin el análisis, porque viene del diagnóstico propio:

> **La salida de Kempf no es bajar el N: es cambiar de nitrato a formas que la
> planta no tenga que reducir — aminoácidos y N orgánico.** Ataca a la vez la
> Fase 1 (que es el pulgón), el fusarium y el costo. **Ya hay Naturamin y
> Starzyme en bodega.**

En dalia eso significa: el pico de N pre-floración de la semana 8 **se entrega
foliar, como aminoácidos**, no como nitrato al tanque.

---

# 10 · Etapa 6 · Foliar — nutricional y fitosanitario

## 10.1 · 🔴 Regla APLICACIONES — lo que se puede y no se puede afirmar hoy

**`07-datos/aplicaciones_historial.csv` llega hasta la semana ISO 27
(3–5 de julio de 2026). Hoy es semana 37. Faltan diez semanas de registro.**

Rotación documentada — **todo lo que existe**:

| Fecha | Sem | Bomba | Productos | Destino |
|---|---|---|---|---|
| 2026-07-03 | 27 | Choque Botrytis+Oidio (curativo) | Equifun 100 cc · Hevea brasiliensis beta 50 cc · Glukoplant Ca-BZn 37,5 cc · ADNGard 12,5 g · Neofat 12 cc | Lisianthus 3B/3C/Mini, Statice 4A/4C, Cresta 3A/4B, **Dahlias 2** |
| 2026-07-04 | 27 | Prefloración+Floración (prev.) | Glukoplant Ca-BZn 37,5 cc · Starzyme 25 cc · Regalia 25 cc · Solar 50 cc · No Fly 10 g · Neofat 12 cc | 5–6+ sem, todos los inv |
| 2026-07-05 | 27 | Vegetativo (prev.) | Naturmix-L 12,5 cc · Equifun 100 cc · Amicos MC 25 cc · ADN Green 25 cc · Neofat 12 cc | <6 sem, inv 2/3/4/5 + ext |

**Semanas 28 a 37: sin registro.** Se sabe que se **diseñaron** cuatro bombas
para la semana 33 (`03-fitosanidad/04-bombas-semana-33.md`), pero **no hay
registro de que se aplicaran**, y esas ya llevaban su propio hueco declarado.

> **Lo que esto significa para este protocolo:** la **estructura** de la rotación
> de abajo es firme —está construida por mecanismo de acción, que no depende del
> historial—. Los **productos concretos** quedan como **propuesta pendiente de
> confirmar** contra el historial real de las semanas 28–37. **No se prepara
> ninguna bomba sin ese cruce.**

Dos cosas que hay que verificar sí o sí antes de mezclar:

1. **¿Cuándo fue la última aplicación de Botrycid?** Intervalo de etiqueta **12
   semanas**. La bomba de statice de la semana 33 lo tenía asignado.
2. **¿Cuántas aplicaciones de Glukoplant Ca-BZn lleva el ciclo?** Tope **6 por
   ciclo**, y hay **2 documentadas solo en la semana 27**.
3. **Stock de Neofat.** El inventario dice *"probablemente agotado"*. Sin
   surfactante la cobertura foliar cae mucho — y en dalia, con hoja grande y
   cerosa, cae más.

## 10.2 · La lógica: mildeo polvoso NO es mildeo velloso

Distinción que decide qué producto sirve y cuál se desperdicia:

| | **Mildeo POLVOSO / oídio** (*Golovinomyces cichoracearum*) | Mildeo VELLOSO (*Peronospora*) |
|---|---|---|
| Es lo que tiene la dalia | ✅ **Sí** — confirmado por Vanessa: *"las dalias y girasoles que son mildeo polvoso"* | ❌ No |
| Dónde vive | **Sobre** la hoja, superficial, con haustorios solo en la epidermis | Dentro del tejido, con oosporas en suelo |
| Necesita agua libre | **No — el agua libre lo mata** | Sí |
| **Revus** (mandipropamid) e **Infinito** | 🔴 **INÚTILES** — son para oomicetos | ✅ Sí sirven |
| Azufre, aceites, bicarbonato, terpenos | ✅ **Muy eficaces** — el patógeno está expuesto en la superficie | Poco |

> 🔴 **Consecuencia directa:** **Revus e Infinito no entran en ninguna bomba de
> dalia.** Están en la lista de fichas confirmadas y sería fácil usarlos por el
> nombre. Contra oídio no hacen nada.

Y la contrapartida buena: **porque el oídio es superficial, todo lo que lo toca
lo mata.** Es la enfermedad fúngica más tratable de la finca — por eso el lavado
de dosel funciona, y por eso el azufre y los aceites, que son multisitio, no
generan resistencia.

## 10.3 · Programa foliar por fase fenológica — el marco Kempf aplicado a dalia

| Semanas | Fase Kempf | Objetivo | Lo que no puede faltar |
|---|---|---|---|
| Trasplante → 4 | **Fase 1** | Enraizar **sin nitrato en savia** — es lo que quita comida al pulgón | Aminoácidos (**Naturamin**) + biológico. **Sin N mineral foliar** |
| 4 → 7 | **Fase 2** | Fotosíntesis completa | Mn, Mg, Fe (**Naturmix-L**) |
| **7 → primer color** | **🔴 Fase 3** | **Lípidos = inmunidad al oídio. Aquí se decide la enfermedad de la semana 14** | **Cu + B + Zn + P foliar** |
| Primer color → fin | **Fase 4** | Metabolitos + entrega de Ca | **Ca foliar + silicio** |

**La ventana crítica es la 7 a la 11.** El repositorio ya lo tiene escrito para
statice —*"la botrytis de la semana 16 se decide en la prefloración, seis a ocho
semanas antes"*— y en dalia es la misma aritmética: **el mildeo de final de ciclo
que Vanessa ve todos los años se decide entre la semana 7 y la 11.**

## 10.4 · 🟢 MKP foliar — el producto que ya está en bodega y resuelve las dos cosas

**Es la recomendación más costo-eficiente de todo este documento.**

El **fosfato monopotásico (Haifa MKP)** está en bodega y fue **sacado del tanque**
por buenas razones (P y K saturados en suelo). **Pero foliar es otra vía y otro
blanco:**

| Lo que aporta | Evidencia |
|---|---|
| **Suprime mildeo polvoso directamente** | Aspersión foliar de MKP controló oídio en pepino y pimentón, **con desaparición del 99 % de las pústulas 1–2 días después de una sola aspersión**, y protección sostenida en programa de 7–14 días |
| **Induce resistencia sistémica** | El efecto es local **y sistémico**: se aplicó solo en el envés de hojas bajas y protegió el resto de la planta |
| **Entrega el P soluble que falta** | **P soluble = uno de los dos limitantes de Fase 3 en DCB**, y Bloque 4 es el único bloque marcado como candidato a fuente mineral de P |
| **No toca el suelo** | El K foliar no entra al complejo de intercambio. **No viola la regla de MKP = 0 en fertirriego** — es otra ruta y otro objetivo |

> **Dosis propuesta: 0,5 % p/v = 5 g/L = 125 g por bomba de 25 L.**
> **Base:** los ensayos publicados usan **20–25 mM (≈3,4 g/L)** en pepino y
> **1 % (10 g/L)** en pimentón, sin daño visible. Se propone el punto medio.
> **Cadencia: cada 7–14 días, desde la semana 7.**

🔴 **Antes de la primera bomba general: prueba de fitotoxicidad en 5 plantas,
leída a las 48 h.** El cultivar italiano es material desconocido y el pétalo de
dalia es delicado. Sin esa prueba no se aplica al lote.

## 10.5 · Rotación fitosanitaria de 4 semanas — estructura por mecanismo

**Dosis por bomba de 25 L.** Estructura firme; productos **pendientes de cruce
con el historial de las semanas 28–37**.

| Sem | Fungicida / inductor | Insecticida | Nutricional (fase) | Regla que la gobierna |
|---|---|---|---|---|
| **1** | **Azufral** ⚠️ + **Equifun** 100 cc | **ADN Green** 25 cc (Stemona, botánico) | **Naturamin** 25 g (Fase 1) | Azufre = multisitio, no genera resistencia. **Prohibido aceite ±14 días** |
| **2** | **Regalia** 25 cc | **No Fly** 10 g (*Paecilomyces*) | **Naturmix-L** 12,5 cc (Fase 2) | Regalia es **inductor**, no fungicida de amplio espectro → **no mata al entomopatógeno** |
| **3** | **Timorex Gold** ⚠️ + **Equifun** 100 cc + **MKP** 125 g | **Alysin** ⚠️ (ajo-ají, repelente) | **Glukoplant Ca-BZn** 37,5 cc (Fase 3: Ca+B+Zn) | Glukoplant: **máx 6 por ciclo** — contarlas |
| **4** | **MKP** 125 g (solo) | **Agroemulsión** ⚠️ (aceite) | **Engruese** 50 cc (Ca) + **Starzyme** 25 cc | El aceite **es también erradicante de oídio**. 21 días desde el azufre ✅ |

Surfactante **Neofat 12 cc** donde aplique — ⚠️ verificar stock.

### Las tres reglas de compatibilidad que esta tabla respeta y que es fácil violar

1. **🔴 Aceite y azufre nunca juntos ni cerca.** Combinados dan fitotoxicidad
   severa. **Mínimo 14 días de separación** — aquí hay 21.
2. **🔴 Entomopatógeno y fungicida de amplio espectro no van en el mismo tanque.**
   Safer Mix (*Beauveria*) y No Fly (*Paecilomyces*) **son hongos vivos**: el
   azufre, los aceites y los terpenos los matan. Por eso el No Fly va en la
   semana 2, la única sin fungicida de amplio espectro, y las semanas de
   fungicida llevan insecticida **botánico** (ADN Green, Alysin).
3. **Azufre fuera con calor.** Por encima de ~30 °C el azufre quema. Aplicar
   **3–4 pm**, como manda la regla de la finca, cubre las dos cosas.

### Productos con ficha confirmada pero **sin dosis documentada en el repositorio**

⚠️ **Azufral · Timorex Gold · Agroemulsión · Alysin.** Los cuatro están en la
lista de fichas confirmadas de `03-fitosanidad/01-reglas-y-protocolos.md`, pero
**ninguno tiene dosis registrada en ningún CSV ni documento**. **Leer la etiqueta
y anotar la dosis en el repositorio con su base antes de la primera aplicación** —
regla del repositorio: *"toda dosis escrita lleva al lado la base de la que salió"*.

### Un producto que vale la pena comprar

**Bicarbonato de potasio.** En los ensayos de referencia sobre oídio da **96–100 %
de reducción** — el mejor erradicante disponible, barato, y sin riesgo de
resistencia. **No está en el inventario de DCB.**

> `SIN FICHA — NO USAR EN FORMULACIÓN` hasta conseguirla. Se propone
> **evaluarlo como compra**, no se incluye en ninguna bomba de arriba.

### Lo que NO se usa en dalia

| Producto | Por qué no |
|---|---|
| **Revus · Infinito** | Oomicetos. **No tocan el oídio** |
| **Botrycid** | Botrytis específico. Blanco equivocado, e intervalo de 12 semanas: se reserva para statice |
| **Yodosafer** | Sería fuerte contra oídio, pero la etiqueta dice **NO en floración** |
| **Amicos MC** como fungicida | El inventario aclara: es **corrector nutricional Mg/Ca**, no biofungicida. Contarlo como fungicida deja la bomba sin ese componente |
| **Cobre foliar sobre flor abierta** | La regla de Limonium sinensis registra **decoloración permanente**. El Cu de Fase 3 va **antes del color** |

## 10.6 · Pulgón — y el hueco que no se puede tapar con insecticida

Recordando la sección 4.3: **contra la virosis los insecticidas casi no sirven**,
porque la transmisión es no persistente. Las herramientas reales, en orden de
eficacia documentada:

| # | Herramienta | Estado en DCB |
|---|---|---|
| 1 | **Aceite mineral, en cobertura completa y frecuencia alta** — más eficaz que los piretroides, que rindieron **la mitad** en bulbosas ornamentales | ✅ **Agroemulsión, 700 cc en stock.** Semana 4 de la rotación |
| 2 | **Fase 1 de Kempf: bajar el N soluble en savia** — quita la comida | ✅ Aminoácidos en vez de nitrato (9.3) |
| 3 | **Descarte de plantas sintomáticas antes de dividir tubérculos** | ✅ Jornal, cero insumo |
| 4 | **Cuchillo desinfectado entre plantas** al cosechar y al dividir | ✅ Hipoclorito 10 % / alcohol 70 % |
| 5 | **Trampas amarillas** para monitoreo y umbral | 🔴 No están en el protocolo. Se propone instalarlas |
| 6 | **Mulch reflectivo (plateado)** — repele áfidos alados | 🟡 Hoy el plástico es negro. Solo evaluar; la regla *"toda cama va con plástico"* no dice de qué color |
| 7 | Entomopatógenos: No Fly, Safer Mix | ✅ Bajan población, **no previenen virus** |

## 10.7 · La bomba nunca se aplica sola

Estructura obligatoria de toda bomba en DCB — **cuatro componentes siempre, haya
o no problema activo**: fungicida · insecticida · bioestimulante · nutricional,
más surfactante. Las cuatro semanas de arriba la cumplen.

Y las reglas de ejecución, que no cambian:

1. **Fungicidas 3–4 pm. Nunca en la mañana.**
2. **Limpieza física antes de cualquier fungicida** sobre foco activo.
3. **El fertirriego no se suspende** bajo presión fúngica.
4. **Al operario se le entrega el número total de bombas**, no la concentración.
5. **Registrar cada aplicación en `APLICACIONES` el mismo día.** El hueco de las
   semanas 28–37 es exactamente el costo de no hacerlo.

---

# 11 · Cosecha y postcosecha

No estaba en lo pedido, pero decide si el tallo extraordinario llega vendible.

| Punto | Criterio |
|---|---|
| **Estadio de corte** | **⅔ a ¾ abierta.** La dalia **no abre después de cortada** — un botón verde se queda cerrado hasta que se marchita. Pétalos externos desplegados con color pleno, centro aún compacto |
| **Hora** | **Antes de las 9 am**, con el tallo turgente de la noche |
| **Hidratación** | Agua **caliente, 70–80 °C**, unos segundos, y luego a agua fresca. Es lo que abre el vaso en un tallo hueco |
| **Cuchillo** | **Desinfectado entre plantas** — transmisión mecánica de virus |
| **Vida en vaso** | **4–6 días.** Es corta: la dalia es producto de entrega rápida, no de inventario |
| **Registro** | `vida_en_vaso.csv` **está vacío**. Estas 160 plantas son la oportunidad de abrirlo con un dato propio |

---

# 12 · Qué medir — o esto no sirve para la siguiente siembra

`CLAUDE.md`: *"El campo enseña solo si lo documentamos bien."* Este lote puede
cerrar cuatro huecos de la matriz de decisión de una sola vez.

| Qué | Dónde va | Hueco de la matriz que cierra |
|---|---|---|
| **Longitud de tallo, planta por planta, en cada corte** | `calidad_tallo.csv` | Variable 9 — **la calidad no se registra en ninguna parte del repositorio** |
| **Termómetro de mínima/máxima en la cama de dalia** | `microclima_bloques.csv` | Variable 3 — hoy el microclima es cualitativo. **El único dato numérico de temperatura del repo son los 11 °C de Inv 6** |
| **Lluvia y temperatura mín/máx por semana ISO** | `clima_semanal.csv` | Variable 7 — **el archivo está vacío**, y es lo que decidiría el ensayo exterior del año que viene |
| **Semana de ciclo en que aparece la primera pústula de oídio, y severidad** | `incidencia_fitosanitaria.csv` | Variable 6 — el registro id 8 dice *"semana 21"* pero sin severidad estructurada |
| **Ventana de cosecha real** | `ciclos_variedad.csv` | Bitácora dice 4 semanas, PROGRAMACION dice 6. **Sin confirmar** |
| **Vida en vaso** | `vida_en_vaso.csv` | Archivo vacío |
| **Plantas sintomáticas de virosis descartadas** | nuevo | El indicador que dice si la colección sobrevive a la multiplicación |

**Diseño mínimo que hace comparables los datos:** las dos camas reciben protocolo
idéntico. **La única diferencia deliberada permitida es el lavado de dosel** — si
Vanessa quiere medirlo, se hace en 4A y no en 4B, y se cuenta la semana de
aparición de la primera pústula en cada una. Es la única forma de convertir una
hipótesis en dato con el material disponible.

---

# 13 · Lo que falta confirmar

## 🔴 Bloqueantes — hay que responderlos antes de ejecutar

| # | Pregunta | Qué cambia |
|---|---|---|
| 1 | **¿Llegan tubérculos o plántulas/esquejes enraizados?** | Define Ruta A (baño de tubérculo, siembra en lomo, sin riego hasta brote) o Ruta B (bandeja estándar). Es la Etapa 0 completa |
| 2 | **¿Qué dijo exactamente el proveedor con "requieren luz"?** ¿Fotoperiodo/iluminación suplementaria, o pleno sol? **¿Y qué equipo de iluminación existe hoy en la finca?** (Campanula tiene `Light = SI`, así que algo hay) | Define si entra el programa de interrupción nocturna de la sección 2.2 — que es la palanca de longitud de tallo, y suma 2–3 semanas al ciclo |
| 3 | **¿Cultivar o serie exacta, y color?** | Sin esto no hay receta de bouquet, ni distribución de color en punto de venta, ni `paleta_color.csv`. Y la susceptibilidad a oídio varía muchísimo entre cultivares de dalia |
| 4 | **¿Se aprueba el baño de tubérculo con Fitoderma en Inv 4?** | Es una excepción a la regla *"Fitoderma solo en Inv 3"*, justificada por el Fusarium documentado de Inv 4A sobre un órgano carnoso |

## 🟡 Necesarios para completar, no para arrancar

| # | Qué | Para qué |
|---|---|---|
| 5 | **`aplicaciones_historial.csv` actualizado, semanas 28 a 37** | **Sin esto la rotación de la 10.5 queda como estructura, no como bomba.** Es lo primero que hay que traer |
| 6 | **Fecha de entrega de las 160** | Fija la semana ISO de siembra y con ella la ventana de cosecha y el riesgo de helada |
| 7 | **Dosis de etiqueta de Azufral, Timorex Gold, Agroemulsión y Alysin** | Cuatro productos con ficha confirmada y **sin dosis en el repositorio** |
| 8 | **Stock real de Neofat** | El inventario es del 26/03/2026 y dice *"probablemente agotado"* |
| 9 | **Análisis del Bokashi terminado** (pendiente 4c de `CLAUDE.md`) | Sin él no se puede decir cuánto N y cuánto K están entrando ya por la base |

## 🔴 Nombre homologado — PAUSA

`incidencia_fitosanitaria.csv` registra las dalias como **`SIN_HOMOLOGAR`**, y
`campo_siembras.csv` las tiene con la **columna N vacía** en las dos filas.

> **Sin nombre homologado, esta siembra no aparece en el calendario de Erica.**
>
> Por la regla 5 del repositorio, **no se improvisa**: hay que proponerlo y que
> Vanessa lo apruebe. Cuando esté el cultivar (pregunta 3), se propone la forma
> `Dahlia <Serie> <Color>` siguiendo el patrón de la bitácora, y **eso pasa por
> `dcb-programacion`, no por este documento.**

## 🔴 Tres cambios propuestos a los CSV — no aplicados

Ninguno se escribió. Requieren validación:

| Archivo | Campo | Hoy | Propuesto | Razón |
|---|---|---|---|---|
| `variedades_parametros_siembra.csv` | Dahlias · `Light` | `NO` | **`SI`** | Vanessa 2026-09-09 + planta de día corto facultativa a 12 h de fotoperiodo |
| `variedades_parametros_siembra.csv` | Dahlias · `DISTANCIA SIEMBRA` | `15 cm` | **`45 cm (2 líneas)`** | 15 cm son ~44 pl/m²; la referencia de dalia de corte es 30–45 cm. La densidad es causa directa de oídio |
| `variedades_parametros_siembra.csv` | Dahlias · `Net` | `1` | **`2`** | Planta de 1–1,5 m con capítulo pesado |

---

# 14 · Resumen ejecutable

| Etapa | Qué se hace |
|---|---|
| **0 · Recepción** | Inspección planta por planta · descarte de tubérculo con pudrición · **cuchillo desinfectado entre plantas** · etiquetar cultivar |
| **1 · Presiembra** | **Inv 4A + Inv 4B.** No-Dig v10: no voltear · Bokashi 1 saco + leonardita 130 g + yeso 2 kg **en superficie** · **lomo de 10–15 cm** para el cuello |
| **2 · Inoculación** | **Cama:** Fosfolip **1,5 cc en CADA bomba** de 20 L, 4–5 bombas, arrastre con agua sola, luego plástico. **Tubérculo:** baño 10–15 min en 5 L con Endorhiza 10 cc + Nube 10 cc + Promobac 13 cc + Fitoderma 5 g |
| **3 · Siembra** | **2 líneas (2 y 7) × 1 planta cada 3 huecos = 74/cama = 148 + 12 en materas.** Tubérculo horizontal a 10–15 cm. **Sin riego hasta el brote** |
| **4 · Posiembra** | **Pinch semana 4** al 3.º–4.º par · **2 mallas** (30 y 60 cm) · **desbotone lateral** · **deshoje basal desde sem 6, cada 2 semanas** |
| **5 · Agua** | Nunca al atardecer · **LAVADO DE DOSEL con agua sola, 10:00–13:00, 2–3×/semana, desde sem 4 hasta el primer color** |
| **6 · Fertirriego** | Fórmula Inv 4+5 vigente · **Haifa Micro siempre 180 g** · **MKP 0 en el tanque** · pedir aprobación para sacar Polyfeed y Bitter Mag |
| **7 · Foliar** | Kempf por fase · **MKP foliar 125 g/bomba desde sem 7** (previa prueba de fitotoxicidad) · rotación de 4 semanas · **aceite y azufre a 21 días** · **entomopatógeno nunca con fungicida de amplio espectro** |
| **8 · Virus** | Aceite mineral en cobertura completa · bajar N soluble · descarte de sintomáticas **después del pinch** · cuchillo desinfectado |
| **9 · Cosecha** | **⅔–¾ abierta**, antes de las 9 am, agua a 70–80 °C, vida en vaso 4–6 días |
| **10 · Medir** | Longitud de tallo · termómetro en cama · semana de primera pústula · ventana real · vida en vaso |

---

# 15 · Bibliografía externa consultada

**Mildeo polvoso — biología y control cultural**

- [UC IPM · Powdery Mildew, Floriculture and Ornamental Nurseries](https://ipm.ucanr.edu/agriculture/floriculture-and-ornamental-nurseries/powdery-mildew/) — humedad de dosel 97–99 % nocturna / 40–70 % diurna; el agua libre inhibe la germinación
- [Effects of water on germination of powdery mildew conidia · ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0953756209811155) — los conidios mueren en agua libre; 4 h o más de exposición los daña
- [PNW Plant Disease Handbook · Dahlia — Powdery Mildew](https://pnwhandbooks.org/plantdisease/host-disease/dahlia-powdery-mildew) — *Golovinomyces cichoracearum* y *G. spadiceus* como agentes en dalia
- [PNW · Powdery Mildew Diseases (general)](https://pnwhandbooks.org/plantdisease/pathogen-articles/common/fungi/powdery-mildew-diseases) — no requiere agua libre, a diferencia de todos los demás hongos foliares
- [First report of powdery mildew on Dahlia variabilis caused by G. cichoracearum · Springer](https://link.springer.com/article/10.1007/s13314-011-0025-7)
- [American Dahlia Society · Fungus Control for Dahlias](https://www.dahlia.org/docsinfo/articles/fungus-control-for-dahlias-and-the-garden/)

**Fosfato monopotásico foliar**

- [Reuveni et al. · Suppression of cucumber powdery mildew by foliar sprays of phosphate and potassium salts · Plant Pathology 1995](https://bsppjournals.onlinelibrary.wiley.com/doi/abs/10.1111/j.1365-3059.1995.tb02713.x) — 99 % de desaparición de pústulas 1–2 días tras una sola aspersión; programa de 7–14 días a 25 mM
- [Local and systemic control of powdery mildew on pepper by foliar spray of mono-potassium phosphate · Crop Protection](https://www.sciencedirect.com/science/article/abs/pii/S0261219498000775) — 1 % p/v, control local **y sistémico**, sin daño visible
- [Controlling powdery mildew in cucumber by foliar sprays of phosphate and potassium salts · Crop Protection](https://www.sciencedirect.com/science/article/abs/pii/0261219495001093)

**Silicio y bicarbonato**

- [Liang et al. · Foliar- and root-applied silicon and induced resistance to powdery mildew in Cucumis sativus · Plant Pathology 2005](https://bsppjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-3059.2005.01246.x)
- [Effect of root and foliar applications of soluble silicon on powdery mildew control · European Journal of Plant Pathology](https://link.springer.com/article/10.1007/s10658-007-9181-1)
- [Suppression of hemp powdery mildew using root-applied silicon](https://www.researchgate.net/publication/359795305_Suppression_of_hemp_powdery_mildew_using_root-applied_silicon) — bicarbonato de potasio 96–100 % de reducción; silicato de potasio 86–95 %
- [Evaluation of Silicon for Managing Powdery Mildew on Gerbera Daisy](https://www.researchgate.net/publication/228664948_Evaluation_of_Silicon_for_Managing_Powdery_Mildew_on_Gerbera_Daisy) — **resultado negativo en gerbera**: el silicio no es garantía en ornamentales

**Fotoperiodo y luz**

- [Control of Flowering Using Night-Interruption and Day-Extension LED Lighting · Springer](https://link.springer.com/chapter/10.1007/978-981-10-1848-0_14) — *Dahlia hortensis*, día de 9 h ± NI de 4 h; longitud de tallo cuadrática con la R:FR; floración incompleta bajo día corto y bajo NI de solo rojo lejano
- [Effects of LED Applications on Dahlia Seedling Quality · PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12348901/)
- [Manipulating Light to Improve Quality of Cut Flowers · American Floral Endowment](https://endowment.org/news/manipulating-light-to-improve-quality-of-cut-flowers)

**Virosis y pulgón**

- [USU Extension · Dahlia Mosaic Virus](https://extension.usu.edu/planthealth/news/dahlia-mosaic-virus) — 16 especies de pulgón, transmisión no persistente, herencia en tubérculo
- [UMaine Extension Bulletin #5070 · Common Questions about Dahlia Mosaic Virus](https://extension.umaine.edu/publications/5070e/) — hipoclorito 10 % un minuto entre plantas; no descartar sintomáticas antes del pinch y dos aplicaciones de N
- [American Dahlia Society · Understanding Virus in Dahlia](https://www.dahlia.org/docsinfo/understanding_virus_in_dahlia-3/)
- [Control of field spread of non-persistent viruses in flower-bulb crops by pyrethroid, pirimicarb and mineral oils · Crop Protection](https://www.sciencedirect.com/science/article/abs/pii/0261219485900547) — el aceite mineral duplicó la eficacia de los piretroides
- [Use of horticultural mineral oils to control PVY and other non-persistent aphid-vectored viruses · Crop Protection](https://www.sciencedirect.com/science/article/abs/pii/S0261219419300031)
- [Khelifa · Mineral oil interferes with potato virus Y in aphid stylets · Plant Pathology 2023](https://bsppjournals.onlinelibrary.wiley.com/doi/10.1111/ppa.13639)
- [PNW Plant Disease Handbook · Dahlia — Virus Diseases](https://pnwhandbooks.org/plantdisease/host-disease/dahlia-virus-diseases)

**Agronomía de dalia de corte**

- [SARE · Dahlia Cut Flower Production in Utah](https://projects.sare.org/media/pdf/D/a/h/Dahlia-production-fact-sheet-formatted-in-progress.pdf) — 30–45 cm de distancia; pinch a 30 cm de altura; 0,3–0,4 lb N/100 pie²/año, mitad a la siembra y mitad ~8 semanas después
- [Nitrogen Management and Virus Incidence on Cut Flower Production of Dahlia](https://www.researchgate.net/publication/378975978_Nitrogen_Management_and_Virus_Incidence_on_Cut_Flower_Production_of_Dahlia)
- [PNW Plant Disease Handbook · Dahlia — Tuber Storage Rot](https://pnwhandbooks.org/node/2627/print) — *Fusarium* como causa principal de pudrición seca; costra blanca a rosada
- [UConn IPM · Trichoderma for Control of Soil Pathogens](https://ipm.cahnr.uconn.edu/trichoderma-for-control-of-soil-pathogens/) — micoparasitismo sobre *Pythium*, *Rhizoctonia* y *Fusarium*
- [Longfield Gardens · When to Cut Dahlias for Cut Flowers](https://www.longfield-gardens.com/blogs/dahlia-care/when-to-cut-dahlias-for-cut-flowers) — corte a ⅔–¾ de apertura; la dalia no abre después de cortada; vida en vaso 4–6 días

---

## Fuentes internas

`CLAUDE.md` · `07-datos/campo_siembras.csv` · `07-datos/incidencia_fitosanitaria.csv` ·
`07-datos/registro_tallos.csv` · `07-datos/consolidado_lotes.csv` ·
`07-datos/variedades_bitacora.csv` · `07-datos/ciclos_variedad.csv` ·
`07-datos/variedades_parametros_siembra.csv` · `07-datos/microclima_bloques.csv` ·
`07-datos/capacidad_bloques.csv` · `07-datos/analisis_suelo.csv` ·
`07-datos/aplicaciones_historial.csv` · `01-infraestructura/01-invernaderos.md` ·
`01-infraestructura/03-no-dig-y-preparacion-camas.md` ·
`01-infraestructura/06-formulacion-camas-v8.md` · `02-nutricion/01-fertirriego-formulas.md` ·
`02-nutricion/02-bioinsumos.md` · `02-nutricion/03-drench-inoculacion.md` ·
`02-nutricion/04-diagnostico-kempf-ingham.md` ·
`02-nutricion/10-protocolo-inoculacion-por-etapas.md` ·
`03-fitosanidad/01-reglas-y-protocolos.md` · `03-fitosanidad/02-inventario-insumos.md` ·
`03-fitosanidad/04-bombas-semana-33.md` · `04-variedades/02-notas-campo.md`
