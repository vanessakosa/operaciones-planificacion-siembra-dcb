# Dahlia · protocolo completo para las 160 italianas

> **Fecha:** 2026-09-09 · semana ISO 37 · **actualizado el mismo día** con las
> respuestas de Vanessa sobre material, luz y propósito del lote.
> **Alcance:** 160 dalias italianas de regalo — presiembra, inoculación, siembra,
> posiembra, fertilización, control fitosanitario y nutrición foliar.
>
> **Tres datos confirmados por Vanessa el 2026-09-09 que gobiernan todo lo demás:**
>
> 1. **Llegan esquejes enraizados de planta madre**, no bulbos → riego inmediato,
>    aclimatación, y el virus entra por propagación vegetativa (sección 4).
> 2. **El proveedor pide luz de 18:00 a 22:00, extensión de día, LED** →
>    fotoperiodo de ~16 h, y el ciclo de 12 semanas del CSV deja de aplicar
>    (sección 2.2).
> 3. **Son pruebas: la cantidad por color todavía no se sabe** → **esto no es un
>    lote de producción, es una evaluación de cultivares**, y eso decide cómo se
>    planta y qué se mide (secciones 4.3 y 12).
>
> **Y cuatro más, de la segunda vuelta del mismo día, que obligaron a rehacer la
> sección 3 completa:** entra riego en Inv 2 · **el corte es diario**, así que dos
> sitios con dalia son dos rondas diarias · **las dalias fallaron también en Inv 2
> zona baja y en Inv 1** —las zonas frescas—, lo que refuta que el bloque fuera la
> causa · y **la densidad propuesta era demasiado holgada**.
>
> **3.ª vuelta — el sitio quedó decidido:** **la cama baja de Inv 3A**, donde hoy
> están las celosias cristata (sección 3.3). Es decisión de Vanessa, y el
> protocolo se ajustó a ella: dosis de Bloque 3, **el Fitoderma vuelve** porque en
> Inv 3 es la regla del bloque, y las tres medidas anti-oídio pasan de
> recomendables a obligatorias.
>
> **Estado:** propuesta técnica. Los puntos bloqueantes están en
> *Lo que falta confirmar*, sección 13.

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

## 2.2 · Recomendación de luz — **CONFIRMADA por el proveedor 2026-09-09**

> **Vanessa 2026-09-09:** *"el proveedor me sugirió luz de 6 a 10 pm, extensión de
> día, LED."*

**El proveedor tiene razón, y su propuesta es mejor que la mía.** Yo había
propuesto interrupción nocturna (NI) de 22:00 a 02:00. Fotobiológicamente las dos
funcionan — las dos rompen la noche larga. **Pero para DCB la extensión de día
gana por una razón operativa, no técnica:**

| | Interrupción nocturna (22:00–02:00) | **Extensión de día (18:00–22:00)** |
|---|---|---|
| Efecto fotoperiódico | Equivalente | Equivalente |
| Consumo | Igual (4 h) | Igual (4 h) |
| **¿Alguien puede verificar que prendió?** | **Nadie está en la finca a esa hora** | **Sí — el turno de la tarde lo ve** |

En una finca donde el repositorio repite *"al operario se le entrega el número
total de bombas, no la concentración"* y *"crítico con Wilson"*, **una intervención
que nadie puede verificar es una intervención que va a fallar en silencio.** A las
18:00 se ve si el LED está encendido. A las 23:00 no.

### El fotoperiodo que resulta

A 4–5° N el sol se pone alrededor de las **18:00–18:20 todo el año**, y el día
natural es de **~12 h 05 min**.

> **12 h 05 min naturales + 4 h de LED = fotoperiodo de ~16 h.**

Eso es exactamente el umbral que la literatura señala: **días de 16 h o más
inhiben la tuberización** y mantienen la planta en producción de hoja y flor. Es
lo que se busca en flor de corte.

### 🔴 Especificación del LED — aquí es donde se puede botar la plata

Dos números que hay que exigirle al proveedor del equipo, porque un LED comprado
por lumen o por vatio puede **no servir**:

| Parámetro | Valor | Por qué |
|---|---|---|
| **Intensidad** | **1–2 µmol/m²/s medidos SOBRE el dosel** (≈ 2 µmol/m²/s, o 10 pie-candela) | Es iluminación **fotoperiódica**, no fotosintética: ~1/100 de la intensidad de una luz de crecimiento. Más es plata tirada |
| **Espectro** | **Rojo (630–660 nm) + rojo lejano (730–760 nm)** | El fitocromo responde a rojo y rojo lejano. **La combinación rojo + rojo lejano a baja intensidad es la más eficaz para promover floración en plantas de día largo** |

> 🔴 **El error caro: comprar un LED blanco frío.** El azul necesita
> **~30 µmol/m²/s para dar la misma respuesta fotoperiódica — 15 a 30 veces más
> que el rojo o el rojo lejano.** Un panel blanco frío (rico en azul, pobre en
> rojo lejano) puesto a 2 µmol/m²/s **puede sencillamente no producir el efecto**,
> y el ensayo quedaría diciendo "la luz no sirvió" cuando lo que no sirvió fue la
> lámpara.
>
> **Pregunta concreta al proveedor del LED: ¿cuál es el PPFD sobre el dosel y qué
> proporción de rojo y rojo lejano emite?** Si no sabe responder eso, no es el
> equipo.

### Cuánto tiempo se deja prendida

**Se deja todo el ciclo del ensayo, sin retirarla.** La razón es que la dalia en
DCB es **perenne con reset** (`ciclos_variedad.csv`) y el objetivo es tallo, no
tubérculo. Mantener 16 h la deja produciendo en vez de mandar asimilados a
tuberizar.

**El intercambio, dicho de frente:** con 16 h **no se van a formar tubérculos de
almacenamiento**, o van a ser pobres. **Eso aquí no importa, y es una ventaja:**

- El material llega como **esqueje de planta madre**, no como bulbo. La vía de
  multiplicación de esta colección **son esquejes, no división de tubérculo** — y
  esa vía es compatible con 16 h. Es más rápida además.
- Si algún día se quisieran tubérculos para almacenar o vender, **se retira la luz
  6–8 semanas antes** y la planta tuberiza sola: días cortos + 15–20 °C es
  exactamente el clima de la Sabana, que es la condición óptima de tuberización.

### 🔴 Y una consecuencia que arruina ensayos: la luz se derrama

Como el umbral fotoperiódico es de **1–2 µmol/m²/s**, **cualquier luz difusa que
llegue a la cama vecina la afecta.** Es por esto que en crisantemo se usan
cortinas de oscurecimiento.

> **Consecuencia práctica: no se puede tener una cama testigo sin luz al lado de
 una cama con luz, dentro del mismo invernadero.** El testigo quedaría
> contaminado y el resultado no significaría nada — y en Inv 2, con circulación
> central y camas a lado y lado, menos todavía.
>
> **Por eso las plantas van todas con luz.** El testigo con y sin luz, si se
> quiere hacer, va en la segunda vuelta —con esquejes propios y en naves
> separadas—, no aquí.

### 🔴 Y el ciclo de 12 semanas deja de aplicar

`ciclos_variedad.csv` tiene **12 semanas CONFIRMADO por Vanessa 2026-08-13**.
**Ese dato se midió sobre bulbos y sin manejo de luz.** Este lote cambia las dos
cosas a la vez:

- **Esqueje enraizado en vez de bulbo:** sin la reserva de carbono del tubérculo,
  el arranque es más lento.
- **Fotoperiodo de 16 h:** retrasa deliberadamente la floración para alargar el
  tallo.

> **El ciclo de este lote es `SIN_DATO`.** Por la regla 1 del repositorio no se
> estima: se mide y se registra. **No entregar todavía una fecha de cosecha a
> Erica** — ver la sección 12.

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

# 3 · Dónde van, y con qué densidad — **revisado 2026-09-09 (2.ª vuelta)**

> **Cuatro datos nuevos de Vanessa que obligan a rehacer esta sección entera:**
>
> 1. *"Ya vamos a empezar a aplicar planes de riego en el 2."*
> 2. *"La ventana de corte de ellas es **diaria**… sí sería un ajuste tener que
>    hacer un corte allá y un corte aquí."*
> 3. *"Cuando la sembré en el 2, la sembré en **la parte baja porque es la parte
>    más fresca**… pero **igual han tenido mildeo, igual han tenido pulgones**.
>    **También la sembré en el 1. Ahí pasó lo mismo.**"*
> 4. *"Esa densidad que tú me diste me parece excesiva… **yo ahorita las tengo
>    sembradas a una por hueco**… si las siembro en zigzag serían 448."*

## 3.1 · 🔴 Primero: mi diagnóstico anterior estaba parcialmente equivocado

La primera versión de este documento decía que **el sitio explicaba el fracaso** —
Inv 2 sin fertirriego, camas desiguales— y que mover el cultivo a Inv 4 era la
palanca. **El punto 3 de arriba lo refuta**, y hay que decirlo claro:

> **Las dalias fallaron en Inv 2 zona baja, que es la fresca y la que más agua
> recibe. Y fallaron igual en Inv 1.** Dos zonas distintas, mismo resultado.
> **El bloque no es la variable.** Cambiar de invernadero, por sí solo, no iba a
> arreglar nada.

## 3.2 · 🟢 Y lo que sí comparten los tres intentos, dicho por ella sin darse cuenta

> *"La sembré en la parte baja **porque es la parte más fresca**."*

Los tres sitios donde la dalia ha fallado tienen el mismo perfil, y no es
coincidencia — **se eligieron a propósito por frescos**, para protegerlas del
achicopalamiento de mediodía:

| Sitio | Perfil en `microclima_bloques.csv` | Antecedente de mildeo del propio repo |
|---|---|---|
| **Inv 2 zona baja** | *"zona baja sombreada"* · `radiacion_rel = BAJA` | `incidencia_fitosanitaria.csv` id 8: MILDEO, sem 21, **PERSISTENTE** |
| **Inv 1** | `humedad_rel = ALTA_NOCTURNA` · `SIN_FERTIRRIEGO` | `01-invernaderos.md`: *"humedad nocturna alta → **mildeo en rosas**"* |

Y la literatura sobre *Golovinomyces cichoracearum* en dalia da como condiciones
predisponentes: **humedad alta, temperaturas moderadas de 20–30 °C, y BAJA LUZ.**

> ### 🔴 El hallazgo de esta sesión
>
> **Buscando protegerlas del calor de mediodía, las ha puesto tres veces
> exactamente en el microclima que el oídio necesita. La sombra resuelve el
> achicopalamiento y crea el mildeo.**
>
> Y la salida no es sombra: **es radiación alta con agua y enfriamiento
> evaporativo** — que es justamente para lo que sirve el lavado de dosel de la
> sección 8.2. Ésa es la pieza que permite poner la dalia a pleno sol sin que se
> achicopale, y es la que ha faltado en los tres intentos.

**Registrado en `.claude/skills/dcb-variedades/references/`:** la observación de
Inv 2 se promovió a regla establecida (segunda vez documentada, misma zona, mismo
comportamiento). La generalización *"la dalia no va en zona fresca ni sombreada"*
quedó como **candidata a regla pendiente del juicio de Vanessa**, porque son zonas
distintas con una característica en común, no la misma zona repetida.

## 3.3 · 🔴 DECISIÓN DE VANESSA 2026-09-09 (3.ª vuelta): cama baja de Inv 3A

> *"Voy a escoger una cama del 3A, que es baja, que es donde ahorita están las
> celosias cristata, que siento que es la que está más pegada al humedal, entonces
> debe tener buen agua y refresca más en la noche."*

**La decisión es suya y el protocolo se ajusta a ella.** Pero tengo que dejar
escrito, porque es mi trabajo, que **es el mismo criterio de los tres intentos
anteriores** — fresco, húmedo, con más agua — y ese criterio es el que la sección
3.2 identificó como la causa probable del oídio recurrente.

### Lo que dice el repositorio de esa cama exacta

`microclima_bloques.csv`, fila **Inv 3A · camas inferiores**:

| Variable | Valor | Lo que la dalia necesita |
|---|---|---|
| `temperatura_rel` | BAJA | — |
| **`humedad_rel`** | **ALTA** | 🔴 **Es la condición que el oídio necesita para germinar** |
| **`radiacion_rel`** | **MEDIA** | ALTA. Y *baja luz* es condición predisponente del oídio |
| `presion_agua` | MEDIA | Alta y uniforme |
| `uniformidad_riego` | **SIN_DATO** | 🔴 No está medida |
| `suelo_estado` | BUENO | ✅ |
| **Nota del repo** | *"Frescas y húmedas. Exitosas: larkspur, gomphrena — **toleran frescura sin botrytis**"* | **La cama está caracterizada por servirle a cultivos que toleran frescura. La dalia no está en esa lista** |

Y del análisis de suelo de **Bloque 3**, dos cifras que pesan aquí:

| | Bloque 3 | Comparación |
|---|---|---|
| **P soluble** | **0,036 mg/L** | 🔴 **El más bajo de los tres bloques** (B4 0,107 · B5 0,059). Y el **P soluble es uno de los dos limitantes de Fase 3** — la fase que gobierna la inmunidad al oídio |
| **Saturación de humedad** | **154,8 %** | 🔴 **La más alta de los tres** (B4 141,5 %). Sobre una cama que ella misma describe como *"tiene buen agua"* |
| M.O. | 18,6 % | La más baja — por eso lleva **más** bokashi y **el doble** de leonardita |

### 🟢 Y lo que la decisión sí resuelve, que es real

| | |
|---|---|
| **Sin dalias viejas al lado** | **Elimina de un golpe el riesgo que yo había marcado como el que podía costar la colección:** el foco de oídio y la transmisión de virus desde las plantas viejas por pulgón (sección 3.4) |
| **Cama medida y con análisis de suelo** | 198 huecos · 35,6 m² · `MEDIDO`. Inv 2 no tiene ni lo uno ni lo otro |
| **Sin registro de incidencia fitosanitaria** | `incidencia_fitosanitaria.csv` **no tiene ni un evento en 3A**. 3B y 3C sí |
| **Fitoderma autorizado** | La regla del repo es *"Fitoderma solo en Inv 3"*. En 3A **deja de ser una excepción y pasa a ser la regla del bloque** — ver 6.3 |
| Presión de agua MEDIA | Mejor que las camas superiores de 3A (BAJA) y que Inv 5 (`LA_PEOR_DEL_SISTEMA`) |

### 🔴 Pero el argumento del corte diario ya no aplica, y conviene saberlo

La razón por la que en la 2.ª vuelta se recomendó Inv 2 era **consolidar toda la
dalia en un sitio** para no hacer dos rondas de corte diarias. **Con la cama en
3A, las dalias viejas siguen en Inv 2 y las rondas van a ser dos de todos modos.**

> **El costo de jornal se paga igual.** Así que la elección de sitio ya no tiene
> que balancear logística contra agronomía: **puede decidirse solo por agronomía.**
> Y si de todos modos se va a cortar en dos sitios, vale la pena volver a mirar la
> pregunta E de la sección 13 —qué pasa con las dalias viejas—, porque su respuesta
> ya no depende de dónde vayan las nuevas.

### Lo que se ajusta en el protocolo por elegir esta cama

Como el sitio sube el riesgo de oídio en vez de bajarlo, **las tres medidas que lo
compensan dejan de ser recomendables y pasan a ser obligatorias**:

| Medida | Sección | Por qué aquí no es opcional |
|---|---|---|
| **Lavado de dosel de mediodía** | 8.2 | Es lo único que mata conidios en una cama de humedad ALTA. Sin esto, el sitio decide el resultado |
| **Deshoje basal desde la semana 6** | 7.1 | Abre el flujo de aire en la base del dosel, que es donde la humedad se acumula |
| **Camellón de 10–15 cm** | 5.2 | **Sat. de humedad 154,8 % + "buen agua" + esqueje sin reserva** = pudrición de cuello. Es la combinación exacta del damping-off |
| **Densidad abierta** | 3.5 | Es la palanca que queda. En esta cama **no se puede ceder más** |

### 🟡 Dos cosas que hay que verificar en campo antes de trazar

1. **¿"Pegada al humedal" es 3A o es 3C?** El repositorio le atribuye *"pegado al
   humedal"* a **Inv 3C**, no a 3A (`microclima_bloques.csv`, fila Inv 3C). Si la
   cama elegida está efectivamente en ese borde, su microclima real puede
   parecerse más al de 3C —`radiacion BAJA`, `humedad ALTA_NOCTURNA` y **inóculo de
   mosca blanca en suelo**— que al de 3A. **Vale la pena confirmarlo antes de
   sembrar**, porque cambia el pronóstico.
2. **Medir la uniformidad de riego de esa cama.** `uniformidad_riego` está en
   `SIN_DATO` para las camas inferiores de 3A. Prueba de vasos a lo largo de la
   cama, antes de sembrar.

### 🟢 Y una nota sobre las celosias cristata que están ahí

La skill `dcb-variedades` dice: *"Celosia cristata — excelente **con calor** ·
Inv2 zona alta, Inv5 · **necesita calor**"*. Está sembrada en una cama de
`temperatura_rel = BAJA`. **Si esa cristata no ha rendido, la causa probable es
esa**, y liberar la cama es una buena decisión por partida doble.

**Al cerrar el lote:** seguir `09-procedimientos/C-cierre-de-lote.md`, retirar el
residuo completo fuera del invernadero, **y no traslapar los dos cultivos**. La
celosia tiene pérdidas documentadas por **pulgón negro**
(`variedades_parametros_siembra.csv`, Celosia Sylphid) y el pulgón es
justamente el vector del virus que amenaza a la colección nueva.

## 3.4 · El riesgo de consolidar en Inv 2 — queda como registro, ya no aplica al sitio elegido

Consolidar en Inv 2 significa poner **160 esquejes vírgenes en la misma nave que
las dalias viejas**, que están registradas con **mildeo persistente `EN_MANEJO`** y
con insectos. Dos consecuencias, y la segunda es la grave:

1. **El oídio es inóculo aéreo dentro de la nave.** Va a llegar. Manejable con
   programa foliar, pero hay que contar con ello desde el día uno.
2. **🔴 Si las viejas tienen virus del mosaico, los pulgones lo pasan a las
   nuevas.** Y como la vía de multiplicación de esta colección **son esquejes**
   (sección 4.4), un lote nuevo infectado en su primera temporada **no se recupera
   nunca**: cada ronda de esquejes multiplica el virus, no la colección.

> **La cuenta es asimétrica: lo que se gana consolidando es jornal. Lo que se
> arriesga es la colección entera.**

### La decisión que resuelve las dos cosas, y es de Vanessa

**¿Qué pasa con las dalias viejas?** Lo que hay registrado:

| Fuente | Dato |
|---|---|
| `campo_siembras.csv` · lote Ball 696 | *"Ya semana 6 **poco productivas, no me gustaron**"* |
| `campo_siembras.csv` · lote DCB 100 | *"**mildeo persistente**, insectos y mildeo semana 24"* |
| `registro_tallos.csv` | **90 tallos en 2 registros** (agosto 2026). ⚠️ El registro puede estar incompleto — no se afirma que hayan producido solo eso |
| `ciclos_variedad.csv` | **Perenne sin cierre de cama** → ocupan Inv 2 **indefinidamente** |

**Si el juicio de campo es que ese lote no va a mejorar, cerrarlo antes de que
lleguen los esquejes resuelve todo de una vez:** elimina el foco de inóculo,
elimina el riesgo de virus, libera el área, y deja la nave limpia para empezar
bien. Es la decisión de mayor apalancamiento de todo este documento.

Y encaja con la unidad de medida del repositorio — **margen por m² por semana de
cama ocupada**: un lote perenne del que la propia Vanessa dijo *"no me gustaron"*,
con mildeo persistente, ocupando cama sin fecha de cierre, es la peor cuenta
posible. **`CLAUDE.md` dice que este repositorio existe justamente para tomar esa
decisión.**

### Si las viejas se quedan — el mínimo no negociable

| # | Medida |
|---|---|
| 1 | **Limpieza física del foco** (tejido afectado en bolsas, fuera del invernadero) **antes** de que entren las nuevas — es regla de la finca |
| 2 | **Programa foliar corriendo en las viejas desde ya**, no cuando lleguen las nuevas. Bajar el inóculo antes, no después |
| 3 | **Máxima separación dentro de la nave:** viejas abajo, nuevas en la zona alta. No elimina el inóculo aéreo, pero el gradiente cae con la distancia |
| 4 | **Aceite mineral en las nuevas desde la primera semana** — es la barrera contra la transmisión no persistente de virus (sección 10.6), y aquí el vector viene de al lado |
| 5 | **Nunca sacar esquejes de las viejas** para ampliar la colección |

### Si el sitio no puede ser Inv 2

La alternativa sigue siendo **una sola cama de Inv 4A o 4B** — riego
`ALTA_UNIFORME` probado, M.O. 25,6 %, cama uniforme y sin dalias vecinas. Se paga
con la ronda doble de corte y con montar malla. **Es la opción correcta si las
viejas se quedan y no se les va a hacer manejo.**

## 3.5 · Densidad — cedo la mitad del área, con el número

Vanessa tiene razón en que dos camas para 160 plantas es demasiado, sobre todo en
un cultivo **perenne sin cierre de cama**, donde el m² se compromete
indefinidamente. Las cuatro referencias, sobre la retícula de 15×15 cm:

| Marco | Distancia efectiva | pl/m² | Área para 160 |
|---|---|---|---|
| **1 por hueco — lo que tiene hoy** | 15 × 15 cm | **44** | 3,6 m² |
| **Zigzag (448 por cama de Inv 4)** | ~21 cm tresbolillo | **22** | 7,2 m² |
| **🟢 PROPUESTO: 1 de cada 3 líneas × 1 de cada 2 huecos** | **45 × 30 cm** | **7,9** | **~20 m² · UNA cama** |
| ~~Propuesta anterior: 2 líneas × cada 3 huecos~~ | 75 × 45 cm | 3,7 | ~43 m² · dos camas |

**Referencia comercial de dalia de corte: 30–45 cm entre plantas.** Los 45 × 30 cm
propuestos caen dentro de ese rango; los 15 × 15 y los 21 cm de zigzag están muy
por debajo.

### Por qué no bajo hasta el zigzag, aunque el área lo pida

**Porque el dosel cerrado es el mecanismo del problema declarado.** El oídio
germina en el aire húmedo *dentro* del dosel (97–99 % HR nocturna); un dosel
impenetrable **fabrica esa humedad**. Y hay evidencia de campo propia:

> **Las dalias actuales están sembradas a 1 por hueco — 44 pl/m² — y tienen mildeo
> persistente.** Eso es un argumento a favor de bajar la densidad, no de subirla.

### El límite hasta donde puedo ceder

**Si el área es la restricción que manda, el piso son 30 × 30 cm** — 1 de cada 2
líneas × 1 de cada 2 huecos, **11 pl/m², ~14,5 m² para las 160**. Sigue dentro del
rango publicado (30 cm = 12 pulgadas) y sigue siendo **4 veces más abierto que hoy**.

**Por debajo de eso volvemos al dosel que causó el problema**, y el ensayo perdería
su sentido: no se podría distinguir un cultivar susceptible de un cultivar bien
sembrado en el sitio equivocado.

**Y esto tiene salida por dato:** si al final del ciclo el oídio quedó controlado,
**la siguiente vuelta se densifica con evidencia**, no con estimación. Eso es
precisamente lo que `calidad_tallo.csv` y el registro de la primera pústula por
cultivar (sección 12) van a permitir decidir.

### 🟢 Corroborado sobre la cama real de Inv 3A — 198 huecos · 35,6 m²

La cama está `MEDIDO` en `capacidad_bloques.csv`: **198 huecos de largo × 8
líneas**, y por la regla verificada de **0,18 m² por hueco** eso da **35,6 m²**.
De ahí sale todo lo demás sin estimar nada:

| | |
|---|---|
| Largo de la cama | 198 × 0,15 m = **29,7 m** |
| Ancho | 35,6 / 29,7 = **1,2 m** |
| Líneas usadas | **3 de las 8** — líneas **1, 4 y 7** → **45 cm entre líneas** |
| Paso a lo largo | **1 planta cada 2 huecos** → **30 cm** |
| Plantas por m² | (3 / 1,2) × (1 / 0,30) = **8,3 pl/m²** |
| **Para 150 plantas** | **50 tramos de 3 plantas = 100 de los 198 huecos** |
| **Largo ocupado** | 50 × 0,30 m = **15 m** |
| **Área ocupada** | 15 × 1,2 = **18 m² — exactamente la mitad de la cama** |

> **Marco para campo: líneas 1, 4 y 7 · una planta cada 2 huecos · los primeros
> 100 huecos de la cama.** 150 plantas en campo + 10 en materas.

### Qué hacer con la otra mitad de la cama

**Dejarla para la primera vuelta de esquejes propios.** Tres razones:

1. **Mantiene toda la dalia junta**, que era el criterio operativo de Vanessa.
2. **Evita un conflicto de manejo.** El **lavado de dosel de mediodía** (8.2) moja
   todo lo que esté en esa cama. Un vecino susceptible a botrytis se dañaría, y un
   vecino que no tolere el programa foliar de dalia obliga a partir las bombas.
3. **No se prepara todavía** — se prepara cuando se siembre, con su propia dosis
   (5.3). Preparar hoy lo que se siembra en tres meses es lixiviar el bokashi.

### ⚠️ Y una advertencia que viene del sitio elegido

Los 45 × 30 cm se acordaron cuando el destino iba a ser una zona **seca y de alta
radiación**. **La cama de 3A es de humedad `ALTA`**, que es la condición que el
oídio necesita. **La densidad deja de tener margen de sobra: es la palanca que
queda.**

- **45 × 30 cm es ahora el piso, no el punto medio.** No se puede ceder más aquí.
- **Si se le puede dar más aire, 45 × 45 cm** (1 de cada 3 huecos → **5,5 pl/m²**,
  150 plantas en 27 m² = 76 % de la cama) **es la mejor apuesta contra el oídio**
  que ofrece este sitio, y sigue dejando cama libre.
- **Y las tres medidas compensatorias de la sección 3.3 dejan de ser opcionales:**
  lavado de dosel, deshoje basal desde la semana 6, y camellón.

---

# 4 · Etapa 0 · Recepción del material — **esquejes enraizados**

> **Confirmado por Vanessa 2026-09-09:** *"plántulas que vienen de plantas madre,
> son esquejes."*
>
> **Esto cierra la pregunta 1 y cambia tres cosas del manejo.** Lo que sigue
> reemplaza por completo la ruta de tubérculo. La ruta de tubérculo queda descrita
> en el anexo 4.4 solo porque **volverá a hacer falta** si algún día se retira la
> luz y la colección se multiplica por división.

## 4.1 · Las tres reversiones respecto a un bulbo

Un tubérculo es un depósito de almidón y agua. **Un esqueje enraizado no tiene
nada de eso.** Todo lo que se sabe de sembrar dalia de bulbo se invierte:

| | Bulbo / tubérculo | **Esqueje enraizado — lo que aplica aquí** |
|---|---|---|
| **Riego a la siembra** | **Sin riego hasta que brote.** Regar antes es la causa #1 de pudrición | 🔴 **AL REVÉS: se riega de inmediato y no se deja secar.** No tiene reserva. Un esqueje que se seca una tarde no se recupera |
| **Reserva de arranque** | Semanas de autonomía | **Ninguna.** Las **dos primeras semanas deciden el lote** |
| **Riesgo dominante los primeros días** | Pudrición del tubérculo | **Desecación y estrés de trasplante** — más el damping-off (*Rhizoctonia*, *Pythium*) en la base del tallo |

🔴 **Y esto choca de frente con la limitante histórica de la finca.** El
diagnóstico de la sección 1 dice que las dalias fracasaron por estrés hídrico.
**Con esquejes ese riesgo no es del ciclo: es de la primera semana, y es
irreversible.** Por eso la **prueba de uniformidad de riego antes de sembrar**
(condición 3 de la sección 3.3) deja de ser una recomendación y pasa a ser
condición: en Inv 2 el riego es nuevo y no está calibrado, y un esqueje no
perdona una cama que riega desigual.

## 4.2 · Recepción y aclimatación

| # | Paso | Detalle |
|---|---|---|
| 1 | **Abrir la caja el mismo día** | Un esqueje en caja cerrada se pudre o se estira. Si llega tarde, abrir igual y regar |
| 2 | **Aclimatar 3–5 días antes de trasplantar** | Bajo media sombra o malla, protegidos de viento y del sol de mediodía, **húmedos permanentemente**. El esqueje viene de un cuarto de propagación con humedad alta: pasarlo directo a cama es el otro error clásico |
| 3 | **Revisar la base del tallo planta por planta** | Descartar los que tengan la base **acuosa, oscura o estrangulada** — eso es damping-off, y en bandeja se propaga a los vecinos |
| 4 | **Revisar la raíz** | Debe estar **blanca y ocupando el cepellón**. Raíz café o cepellón suelto = no está listo. Ese se deja más tiempo, no se siembra |
| 5 | **🔴 Etiquetar el cultivar uno por uno** | Ver la sección 4.3 — en este lote esto no es orden, es el objetivo del ensayo |
| 6 | **Inocular** | Etapa 2, sección 6.3 — la base de bandeja de DCB, sin cambios |
| 7 | **Trasplantar** | Cepellón **al ras del suelo o 1 cm por debajo**, nunca enterrando el punto de crecimiento |

**El deshoje basal (sección 7) no empieza hasta que la planta tenga raíz nueva
afuera del cepellón** — quitarle hoja a un esqueje sin anclar es quitarle su
única fábrica de azúcar.

## 4.3 · 🔴 Lo más importante: esto no es un lote de producción, es una evaluación de cultivares

> **Vanessa 2026-09-09:** *"son pruebas entonces no sé bien cantidad por color
> aún."*

**Eso cambia cuál es el producto de esta siembra.** Si no se sabe la mezcla de
color, entonces el resultado que importa no son los tallos: es **saber cuáles de
estos cultivares italianos merecen comprarse a escala** — y ese resultado se gana
o se pierde en cómo se plantan, no en cómo se cosechan.

La susceptibilidad al mildeo polvoso **varía enormemente entre cultivares de
dalia.** Un lote plantado revuelto da un promedio y no sirve para nada. Un lote
plantado por cultivar identificado da, con el mismo trabajo:

1. **Un ranking de resistencia a oídio** — probablemente lo más valioso, porque
   dice qué comprar en grande.
2. **Longitud de tallo por cultivar** — el que fija el precio.
3. **Ciclo real por cultivar** bajo 16 h de luz — el que Erica necesita.
4. **Color confirmado en campo**, que es lo que después entra a `paleta_color.csv`
   con `confianza_color = alta` en vez de inferido.

### Las cuatro reglas que hacen que el ensayo sirva

| # | Regla | Por qué |
|---|---|---|
| 1 | **Un cultivar por grupo contiguo, nunca revuelto** | Sin esto no hay atribución posible. Es la diferencia entre datos y anécdotas |
| 2 | **Estaca al inicio de cada grupo, con nombre y número de posición** | La etiqueta plástica del proveedor se decolora y se pierde en 3 meses |
| 3 | **Registrar cultivar → cama → posición inicial → posición final → n.º de plantas** | Nuevo archivo: `07-datos/ensayo_dahlia_posiciones.csv`. Se llena el día de la siembra, no después |
| 4 | **🔴 TODAS reciben exactamente el mismo manejo** | Luz, riego, lavado de dosel, bombas, fertirriego: **idénticos**. **El cultivar tiene que ser la única variable.** Nada de "a estas les pongo más" |

**La regla 4 corrige algo que yo mismo había propuesto:** en la primera versión de
este documento sugerí usar 4A con lavado de dosel y 4B sin, para medir el efecto
del lavado. **Con material desconocido eso está mal.** Se estarían moviendo dos
variables a la vez (cultivar y manejo) sobre un n pequeño, y no se podría separar
ninguna de las dos. **El lavado de dosel va a las dos camas**, porque su mecanismo
está bien establecido en la literatura y en la propia historia de Vanessa, y no
necesita que se le sacrifique la mitad del lote para demostrarlo.

### Si sobran o faltan plantas de un cultivar

Lo normal en un regalo es que las cantidades por cultivar sean desiguales.
**No se rellena para emparejar.** Se anota el n real de cada uno y se acepta que
los cultivares con pocas plantas dan una señal más débil. **Un cultivar con 3
plantas sigue diciendo algo si está identificado; no dice nada si está revuelto.**

## 4.4 · 🔴 Virosis — y por qué con esquejes el riesgo entra por otra puerta

Con bulbos el virus del mosaico de la dalia (DMV) entra con el tubérculo. **Con
esquejes de planta madre entra igual, y es la vía de introducción más probable
que existe:** *"DMV es persistente y se propaga fácilmente por propagación
vegetativa"*, y *"la vía más probable de introducción de cepas de DMV a una finca
es vía tubérculos o esquejes infectados"*.

**La consecuencia es dura y hay que decirla:** si la planta madre estaba
infectada, **el 100 % de sus esquejes lo está.** No es probabilidad, es clonación.

Y el segundo golpe: **la vía de multiplicación de esta colección son esquejes.**
Cada ronda de esquejes que Vanessa saque de una planta infectada multiplica el
virus, no la colección.

### Lo que se hace

| # | Acción | Detalle |
|---|---|---|
| 1 | **🔴 Preguntarle al proveedor si el material es indexado** | *"¿las plantas madre están indexadas / libres de virus?"* Existe material comercial **virus-indexed**, propagado por cultivo de meristemo desde madres verificadas en laboratorio. Es la pregunta más barata de este documento y la de mayor consecuencia |
| 2 | **Registrar la respuesta, sea cual sea** | Si no están indexadas no se rechaza el regalo — se sabe que el stock arranca con riesgo, y eso cambia la regla 4 de abajo |
| 3 | **Marcar y NO propagar sintomáticas** | Mosaico, aclaramiento de nervadura, deformación, enanismo. **Pero no descartar antes del pinch** — muchas sospechas resultan ser deficiencia o daño de trasplante |
| 4 | **🔴 Solo se sacan esquejes de plantas sin síntoma** | Ésta es la regla que decide si la colección crece o se degrada |
| 5 | **Cuchillo desinfectado entre plantas** | **Hipoclorito 10 % un minuto, o alcohol 70 %.** Al cosechar y al esquejar. Es transmisión mecánica |
| 6 | **Aceite mineral contra el vector** | Ver 10.6 — **los insecticidas casi no previenen la transmisión no persistente; el aceite sí** |

> **Regla que se propone para el repositorio:** *en dalia, el objetivo del programa
> de pulgón no es la plaga — es el virus del stock. Se mide en plantas
> sintomáticas descartadas por temporada, no en pulgones vivos.*

## 4.5 · Anexo — la ruta de tubérculo, para cuando haga falta

No aplica a esta entrega. Queda escrita porque **volverá a aplicar** si se retira
la luz y la colección se multiplica por división en vez de por esqueje:

- Descartar tubérculo blando, con pudrición seca, o con **costra fúngica blanca a
  rosada — eso es *Fusarium***, causa principal de pudrición seca de tubérculo, y
  sobrevive indefinidamente en el suelo.
- Cortar la zona podrida hasta tejido sano y sellar con **azufre + cal hidratada
  50:50**, solo si el cultivar es irremplazable.
- **Un tubérculo sin yema visible en el cuello no brota.**
- **Sin riego hasta que emerja la yema**, y siembra horizontal a 10–15 cm.
- Cuchillo desinfectado entre tubérculos, igual que arriba.

---

# 5 · Etapa 1 · Presiembra — preparación de cama

Se sigue **la v10 de `01-infraestructura/06-formulacion-camas-v8.md`** sin
inventar nada, con **una sola adición justificada** para dalia.

## 5.1 · Lo más importante de toda la preparación, en tres frases

Antes de las dosis, porque las dosis son la parte fácil:

> **1. No voltear.** El No-Dig es lo que protege el *Trichoderma* de 1,4×10⁶ UFC/g.
> Aflojar **solo donde esté compactada**.
>
> **2. Las enmiendas van EN SUPERFICIE.** Bokashi y leonardita se mezclan entre sí
> y se aplican encima. **No se entierran.** El agua y la biología las incorporan.
>
> **3. En esta cama, el camellón es la línea que decide.** Bloque 3 tiene la
> **saturación de humedad más alta de la finca (154,8 %)**, la cama es de humedad
> `ALTA`, Vanessa la eligió porque *"tiene buen agua"*, y lo que se siembra es un
> **esqueje sin reserva**. Sembrar al ras en esa combinación es damping-off.

Todo lo demás —cuánto bokashi, cuánta leonardita— mueve el resultado mucho menos
que esas tres.

## 5.2 · El armado, paso por paso (v10)

| # | Paso |
|---|---|
| 1 | **Cerrar el lote de celosia** — `09-procedimientos/C-cierre-de-lote.md`. Residuo completo fuera del invernadero. **Sin traslape con la dalia** |
| 2 | **NO voltear.** Aflojar **solo donde esté compactada** |
| 3 | Mezclar **Bokashi + leonardita** y aplicar **EN SUPERFICIE**. No enterrar |
| 4 | **Armar el camellón de 10–15 cm** sobre la línea de siembra. Modelado de superficie, no volteo |
| 5 | Nivelar el resto de la superficie sin remover |
| 6 | Riego suave, **con agua sola** |
| 7 | **Inocular. SIEMPRE.** (Etapa 2) |
| 8 | Poner el **plástico** |

## 5.3 · Las dosis — Inv 3A, cama de 198 huecos · 35,6 m²

La cama está en la tabla de la v10 con dosis ya calculadas. **Y la v9 eliminó la
distinción ESTÁNDAR / PREMIUM**: hay **una sola dosis por cama, que depende del
bloque y no de la variedad** — *"la variedad se ajusta eligiendo el bloque, no
cambiando la receta"*.

| Producto | **Cama completa (35,6 m²)** | **Solo la mitad que se siembra (~18 m²)** | Tasa | Base |
|---|---|---|---|---|
| **Bokashi V1** | **2 sacos · 50 kg** | **1 saco · 25 kg** | **1,40 kg/m²** | Tabla v10, fila Inv 3A |
| **Black Diamond GR** (leonardita) | **450 g** | **230 g** | **12,5 g/m²** | Tasa de Bloque 3 |
| **Yeso agrícola** | **NO** | **NO** | — | *"Solo Bloque 4"* — se apoya en el azufre medido de ese bloque |
| **Compost** | **NO va a la cama** | — | — | Ver 5.4 |

> **Como solo se siembra la mitad de la cama (sección 3.5), se prepara la mitad**
> — 1 saco de Bokashi y 230 g de leonardita. **La otra mitad se prepara cuando se
> siembre**, con su propia dosis. Preparar ahora lo que se va a sembrar en tres
> meses es lixiviar el bokashi.

**Dos cosas que llaman la atención en esas cifras y no son error:**

- **Bloque 3 lleva el DOBLE de leonardita que Bloque 4** (12,5 contra 6,5 g/m²) y
  **más bokashi por m²** (1,40 contra 1,24). Es deliberado: la dosis va **inversa a
  la M.O.**, y Bloque 3 tiene la más baja de los tres (18,6 % contra 23,4 %).
- **Sin yeso.** No es un olvido: el yeso entró solo en Bloque 4 porque ahí el
  azufre está **medido** y bajo (26,55 M). Bloque 3 tiene **S en 51,67 = ALTO**.
  Meterle yeso sería agregar sulfato donde ya sobra.

⚠️ **Incompatibilidad ya registrada:** el Black Diamond granulado es
**incompatible con nitrato de calcio**, que es la línea #1 del tanque. **No hacer
coincidir la leonardita con un fertirriego de N-Cal.**

## 5.4 · El compost: la respuesta es que NO va a la cama, y la razón importa

**El compost no está en la fórmula de preparación de cama, y no debe estarlo.** El
repositorio ya separó los dos procesos y les dio funciones distintas:

| | **Bokashi** | **Compost térmico** |
|---|---|---|
| Proceso | Fermentación, bajo oxígeno | Aeróbico, con volteo |
| **Función** | **ALIMENTA** | **INOCULA** |
| Perfil | Bacteriano | **Fúngico + protozoos + nematodos** |
| Dónde se usa | **Preparación de cama** | **Extracto / té — no como enmienda** |

**Y hay dos razones específicas de esta cama para no echarle compost como
enmienda:**

1. **El objetivo de materia orgánica ya está cumplido.** `CLAUDE.md` lo dice:
   *"con M.O. en 18,6–23,4 % el objetivo de construir materia orgánica está
   cumplido"*. Un suelo mineral normal tiene 3–6 %.
2. **Esta cama ya retiene demasiada agua.** Sat. de humedad **154,8 %**, densidad
   aparente **0,71 g/cm³**, y Vanessa la eligió porque *"tiene buen agua"*.
   **Más materia orgánica empuja justo en la dirección equivocada** para un esqueje
   que se pudre por el cuello.

### 🟢 Pero sí hay una vía de compost que en ESTA cama vale más que en ninguna otra

El **extracto de compost (té)** — no el compost como bulto. El repositorio ya
explica por qué existe:

> *"**Inóculo fúngico** + materia prima del **extracto de compost**, que es lo que
> trae protozoos y nematodos bacterívoros — el grupo funcional que **ningún
> inoculante comercial vende** y que es el que **libera N y P en la rizosfera**."*

**Y el P es exactamente el problema de Bloque 3:** P soluble **0,036 mg/L, el más
bajo de los tres bloques**, sobre un P total ALTO de 40,73. Hay fósforo; **lo que
falta es quien lo libere.** Ese es literalmente el trabajo del bucle
bacteria → protozoo → N y P disponibles.

**Estado, sin adornos:**

| | |
|---|---|
| Compost térmico nuevo | 🔴 **No estará listo hasta la semana 44–46.** Hoy es la 37 |
| **Pila vieja** | 🟢 **Disponible ahora.** Decisión del 2026-09-08: *"el primer té sale de la pila vieja"*, y el filtro es de Vanessa — **va lo "dulce y polvoso" de abajo; no va lo que huela ácido o a podrido, ni lo que tenga pedazos reconocibles** |
| **Dosis y protocolo del té** | 🔴 **NO EXISTEN en el repositorio.** Solo está el principio: *"el extracto es un cultivo, no una dilución — se airea 24–48 h"* |

> **Recomendación:** el té **no entra a este protocolo todavía**, porque escribir
> una dosis sin base sería exactamente el error que el repositorio ya documentó
> tres veces con el Fitoderma. **Pero esta cama es el mejor caso de la finca para
> estrenarlo**, y vale la pena definir su protocolo aparte — la dalia estará ahí
> meses y el té se aplica en cualquier momento del ciclo, no solo a la siembra.

## 5.5 · Lo que NO se hace

- ❌ **No se aplica roca fosfórica**, aunque el P soluble de Bloque 3 sea el más
  bajo de la finca. El **P total es ALTO (40,73)**: el fósforo está ahí y no falta
  — lo que falta es quien lo libere. Agregar más P total no resuelve nada. Las
  vías correctas son **biológica** (Fosfolip, sección 6.1) y **foliar**
  (MKP, sección 10.4).
- ❌ **No se agrega potasio en ninguna forma.** Bloque 3: saturación de K **25,3 %**
  contra un rango de balance de 2–5 %.
- ❌ **No se agrega magnesio.** Bloque 3: saturación de Mg **32,2 %** contra 10–20 %.
- ❌ **No se agrega yeso.** Bloque 3 tiene **S en 51,67 = ALTO**. El yeso es solo
  de Bloque 4, y por su azufre medido y bajo.
- ❌ **No se agrega compost como enmienda.** Ver 5.4 — la M.O. ya está cumplida y
  esta cama ya retiene demasiada agua.
- ❌ **No se voltea a 25–30 cm.** Destruye el Trichoderma de 1,4×10⁶ UFC/g.

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
lo alcanza**.

> 🟢 **Y en la cama de 3A este producto es el más importante del protocolo de
> suelo.** Bloque 3 tiene el **P soluble más bajo de la finca — 0,036 mg/L** sobre
> un **P total ALTO de 40,73**: el fósforo está ahí, sin liberar. Y el **P soluble
> es uno de los dos limitantes de Fase 3**, que es la fase que decide el oídio.
> **Solubilizar ese fósforo es atacar el mildeo por la raíz**, que es lo único que
> se puede hacer contra una enfermedad aérea desde el suelo.

⚠️ **Regla que protege el drench:** **no regar con fertirriego el día de la
inoculación.** El fertilizante químico mata el inoculante.

## 6.2 · Bandeja — el estándar de DCB, sin ninguna adición

Un solo pase, **en 5 L de agua**, el día después de que llegan y antes de
trasplantar:

> **Endorhiza 10 cc + Nube 10 cc + Promobac 13 cc.**
>
> Rinde **4 bandejas**. Si hace falta más agua para mojarlas, se agrega **agua
> sola**, no más producto. Bases: Endorhiza y Nube por su etiqueta; Promobac
> **2,5 cc/L × 5 L = 12,5 → 13 cc**, que es su etiqueta aplicada literal porque en
> bandeja el volumen de agua es el normal de un drench.

| Producto | Qué aporta |
|---|---|
| **Endorhiza** | Micorriza — la única vía al P por exploración de hifas. **Y el P soluble es uno de los dos limitantes de Fase 3** |
| **Nube** | *Streptomyces* — *"induce a la planta a producir fitoalexinas que le dan resistencia sistémica"*. Es el único género que no está en ninguna otra parte del programa |
| **Promobac** | *Bacillus* — segundo género de resistencia inducida. Su ficha lista *Fusarium*, *Oidium*, *Botrytis*, *Erysiphe*, *Peronospora* y ***Rizoctonia*, que es el damping-off de bandeja** |

## 6.3 · 🔴 El Fitoderma VUELVE — porque cambió el bloque, no porque cambié de opinión

Dos vueltas atrás propuse meter Fitoderma como **excepción** a la regla del repo,
cuando el sitio era Inv 4. Luego lo **retiré**, al saber que llegaban esquejes.
**Ahora vuelve, y por una razón distinta de las dos anteriores: el sitio es Inv 3.**

> **La regla del repositorio es literal:** *"Fitoderma — **SOLO Inv 3**, por
> Fusarium activo. Trichoderma ya alto en Inv 4+5."*
>
> **En 3A el Fitoderma no es una excepción: es la regla del bloque.** Y el motivo
> por el que estaba prohibido en Inv 4 —que ahí el *Trichoderma* nativo ya está en
> 1,4×10⁶ UFC/g— **no aplica en Bloque 3.**

Y hay tres razones propias de esta cama que lo hacen valer más aquí que en
cualquier otra:

| # | Razón |
|---|---|
| 1 | **La cama es fría y húmeda, y lo que se siembra es un esqueje.** Frío + húmedo + base de tallo tierna = **damping-off** (*Pythium*, *Rhizoctonia*). Es el riesgo #1 de las dos primeras semanas |
| 2 | **Sat. de humedad 154,8 %** — la más alta de la finca. Un suelo que retiene tanto es donde los patógenos de raíz mandan |
| 3 | **Es el único producto de la bandeja que lista *Peronospora sparsa*** — mildeo **velloso**, que sí tiene etapa en el suelo y sí se favorece con frío y humedad. No es el problema de la dalia (el suyo es polvoso), pero en esta cama es un riesgo que no cuesta cubrir |

### La mezcla de bandeja queda así

> **En 5 L de agua, un solo pase:**
>
> **Endorhiza 10 cc + Nube 10 cc + Promobac 13 cc + Fitoderma 5 g**

**Es exactamente la mezcla que ya reciben lisianthus, dianthus y Green Ball** — no
se inventa nada, no se cambia ninguna base de dosificación, y el Fitoderma entra a
la misma concentración corregida de 5 g (no los 50 g que estuvieron mal escritos
tres veces).

🟡 **La única salvedad, que es la misma de siempre y no es nueva:** las fichas de
Bioquirama dicen *"consultar al Departamento Técnico"* sobre la compatibilidad
cruzada entre *Trichoderma*, micorriza y *Streptomyces*. **Es la misma pregunta del
correo pendiente**, y aplica igual a las otras tres variedades que ya llevan esta
mezcla. **No introduce un riesgo nuevo.** Si preocupa, la alternativa limpia —ya
escrita en el repositorio— es **poner el Fitoderma en el hueco de trasplante en vez
de en la mezcla**, no en otro día, que no separa nada.

# 7 · Etapa 3 · Siembra y trabajos culturales

| Práctica | Qué se hace | Cuándo | Fuente |
|---|---|---|---|
| **Trasplante** | Cepellón **al ras del suelo o 1 cm por debajo**, sobre el lomo de la 5.2. **Nunca enterrar el punto de crecimiento** | Siembra | esqueje enraizado |
| **🔴 Riego inmediato** | **Regar al momento de sembrar y no dejar secar en las 2 primeras semanas.** El esqueje **no tiene reserva**: es la reversión total de la regla del bulbo | Siembra → sem 2 | ver 4.1 |
| **Sombra las primeras 48–72 h** | Malla o tela sobre el lomo si el sol de mediodía pega fuerte. Se retira apenas la planta deje de marchitarse al mediodía | Siembra → 72 h | manejo de esqueje |
| **Un cultivar por grupo, con estaca** | Ver 4.3 — **es el objetivo del ensayo, no orden**. Registrar posiciones en `ensayo_dahlia_posiciones.csv` el mismo día | Siembra | 🔴 regla del ensayo |
| **Malla — 2 capas, no 1** | `variedades_parametros_siembra.csv` dice `Net = 1`. Con planta de 1–1,5 m y capítulo pesado, **1 capa no sostiene**. Primera a **30 cm**, segunda a **60 cm** | Antes de que la planta las alcance | 🔴 **cambio propuesto al CSV** |
| **Pinch** | Despuntar sobre el **3.º–4.º par de hojas verdaderas**, con la planta a ~30 cm | ~**semana 4** post-trasplante | `variedades_parametros_siembra.csv` (`Pinch = Si, semana 4`) ✅ coincide con la literatura |
| **Desbotone** | Quitar los **dos botones laterales** junto al terminal → un tallo largo con una flor | Cuando los botones son distinguibles | práctica estándar de dalia de corte |
| **Deshoje basal (faldeo)** | Quitar **todas las hojas de los 30–40 cm inferiores** cuando la planta pasa de 60 cm, y repetir. **No empezar hasta que haya raíz nueva fuera del cepellón** | Desde semana 6, cada 2 semanas | **medida anti-oídio directa** |
| **Tallos por planta** | **4** — a confirmar bajo 16 h de fotoperiodo | — | `variedades_parametros_siembra.csv` |

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
| **🔴 Trasplante → semana 2** | **Riego inmediato y sostenido. NO dejar secar ni una tarde.** Con esqueje no hay reserva que aguante — es lo contrario de lo que se hace con bulbo (ver 4.1) |
| Semana 2 → pinch | Riego regular, suelo **húmedo, nunca saturado** |
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
foliar, no en el fertirriego.**"* Y operativamente el tanque sirve al bloque
entero — **no se le puede dar a una cama una fórmula distinta.** Esa es la razón
de fondo por la que todo el manejo dirigido a dalia de este documento vive en la
foliar y no en el tanque.

### 🔴 Inv 2 no tiene fórmula de fertirriego

Las fórmulas vigentes son **Inv 3** e **Inv 4+5**. **Inv 2 no tiene ninguna**, y
tampoco tiene análisis de suelo (ver 5.1). El riego apenas está entrando.

> **Default propuesto: usar la fórmula de Inv 4+5**, por la misma analogía que el
> repositorio ya acepta para la preparación de cama (*"Inv 1 e Inv 2 usan la fila
> de Inv 4A/4B"*). **Es una analogía, no una medición** — y por eso hay que
> declararla como tal en la hoja de operario, no presentarla como fórmula
> calibrada de Inv 2.

⚠️ **Y hay que verificar de qué tanque cuelga Inv 2** antes de entregar dosis: si
comparte tanque con otro bloque, la fórmula la manda ese bloque, no la dalia.

Con esa salvedad, las fórmulas **Inv 4+5 vigentes**:

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
   ⚠️ **Este número es de Bloque 4, no de Inv 2** — que no tiene análisis. Pero el
   patrón es **el mismo en los tres bloques medidos** (K 24–30 %, Mg 32–38 %), así
   que la presunción razonable es que Inv 2 se le parece. **Presunción, no dato:**
   se confirma con el muestreo pedido en 5.1.
2. **El K y el Mg altos bloquean el Ca por antagonismo catiónico** — y el eslabón
   2 del diagnóstico de la dalia es, precisamente, calcio que no llega.
3. **El bokashi ya es una fuente de K no contabilizada** (equinaza + ceniza +
   melaza + king grass, a 1,24 kg/m² — la misma tasa que hereda Inv 2). La dalia
   recibiría K por dos vías sobre un suelo que muy probablemente ya lo tiene
   saturado.

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

# 12 · Qué medir — es el producto de esta siembra

`CLAUDE.md`: *"El campo enseña solo si lo documentamos bien."* Y como Vanessa
dijo que **son pruebas**, aquí el dato **no es un subproducto de la cosecha: es la
cosecha.** Este lote puede cerrar cinco huecos de la matriz de decisión a la vez.

## 12.1 · El registro que hay que abrir el día de la siembra

**`07-datos/ensayo_dahlia_posiciones.csv`** — sin este archivo, ninguno de los de
abajo sirve, porque no habrá cómo atribuir nada a un cultivar.

| Columna | Contenido |
|---|---|
| `cultivar` | Nombre exacto del proveedor, tal cual venga |
| `color_declarado` | Lo que dice la etiqueta |
| `color_confirmado_campo` | Se llena en la primera floración |
| `cama` | Identificación exacta de la cama — **en Inv 2 esto es indispensable**, no basta "bloque 2" (ver 3.3) |
| `linea` | `2` o `7` |
| `posicion_inicio` / `posicion_fin` | Número de hueco a lo largo de la cama |
| `n_plantas` | Reales, sin emparejar |
| `fecha_trasplante` | — |

## 12.2 · Lo que se mide, y qué hueco cierra

| Qué | Cada cuánto | Dónde va | Hueco que cierra |
|---|---|---|---|
| **🔴 Semana de aparición de la primera pústula de oídio, POR CULTIVAR, y severidad 0–3** | Revisión semanal desde la sem 4 | `incidencia_fitosanitaria.csv` | **El resultado más valioso del ensayo: qué cultivar italiano comprar a escala.** Hoy el registro id 8 solo dice *"semana 21"*, sin severidad y sin cultivar |
| **Longitud de tallo, tallo por tallo, en cada corte** | Cada cosecha | `calidad_tallo.csv` | Variable 9 — **la calidad no se registra en ninguna parte del repositorio**. Es lo que separa *"produjo"* de *"produjo vendible"* |
| **🔴 Ciclo real: fecha de trasplante → primer corte, por cultivar** | Una vez | `ciclos_variedad.csv` | **Las 12 semanas del CSV se midieron con bulbo y sin luz. Aquí no aplican** — ver 2.2. Es `SIN_DATO` hasta que se mida |
| **Ventana de cosecha real** | Una vez | `ciclos_variedad.csv` | Bitácora dice 4 semanas, PROGRAMACION dice 6. **Sin confirmar desde siempre** |
| **Tallos por planta reales bajo 16 h** | Al cierre | `ciclos_variedad.csv` | El CSV dice 4; con fotoperiodo extendido puede ser otro |
| **Termómetro de mínima/máxima en la cama** | Lectura diaria | `microclima_bloques.csv` | Variable 3 — hoy el microclima es cualitativo. **El único dato numérico de temperatura de todo el repositorio son los 11 °C de Inv 6** |
| **Lluvia y temperatura mín/máx por semana ISO** | Semanal | `clima_semanal.csv` | Variable 7 — **el archivo está vacío**. Es lo que va a decidir si el ensayo exterior del año que viene se puede hacer sin riesgo de helada |
| **Color confirmado en campo** | Primera floración | `paleta_color.csv` | Entra con `confianza_color = alta`, no inferido del nombre — regla 8 |
| **Vida en vaso** | 3 tallos por cultivar | `vida_en_vaso.csv` | Archivo vacío |
| **Plantas sintomáticas de virosis marcadas** | Semanal desde el pinch | `ensayo_dahlia_posiciones.csv` | El indicador que dice si la colección sobrevive a la multiplicación |

## 12.3 · 🔴 El diseño: una sola variable

**Todas las plantas reciben exactamente el mismo manejo — luz incluida.**
Cultivar es la única variable. Las razones están en 4.3 y en 2.2:

- **Con material desconocido, partir el manejo arruina las dos lecturas.** No se
  podría separar *"este cultivar es malo"* de *"a esta mitad le hicimos otra cosa"*.
- **La luz no se puede partir dentro de la misma nave:** el umbral fotoperiódico
  es de **1–2 µmol/m²/s** y la luz difusa alcanza esa cifra en la cama vecina. Un
  testigo sin luz al lado de uno con luz **no es un testigo**.

**Esto corrige la primera versión de este documento**, donde propuse usar 4A con
lavado de dosel y 4B sin, para medir el lavado. Con este material, no.

## 12.4 · Y lo que NO se le entrega a Erica todavía

Por la regla 6 del repositorio —*"nunca dar a Erica datos históricos de cosecha en
crudo, solo estimados a futuro"*— y por la regla 1 —*"nunca inventar ciclos"*—:

> **No hay fecha de cosecha que dar.** Esqueje + 16 h de fotoperiodo dejan el
> ciclo en `SIN_DATO`. Se entrega un estimado **solo cuando aparezca el primer
> botón visible** en el lote, que es el primer punto donde se puede proyectar
> honestamente.

---

# 13 · Lo que falta confirmar

## ✅ Resuelto en la sesión del 2026-09-09

| # | Pregunta | Respuesta | Qué cambió |
|---|---|---|---|
| 1 | ¿Tubérculos o esquejes? | **Esquejes enraizados de planta madre** | Etapa 0 reescrita (sección 4): riego inmediato en vez de "sin riego hasta el brote", aclimatación de 3–5 días, y el riesgo de virosis pasa a ser el de propagación vegetativa |
| 2 | ¿Qué significaba "requieren luz"? | **Extensión de día, LED, 18:00–22:00**, sugerido por el proveedor | Sección 2.2 reescrita. Fotoperiodo de ~16 h. **Mejor que la interrupción nocturna que yo había propuesto**, porque es verificable por el turno de la tarde |
| 4 | ¿Fitoderma en el baño? | **Retirado** | Lo justificaba el tubérculo herido, no el bloque. Con esqueje no aplica, y la regla *"Fitoderma solo en Inv 3"* queda intacta (sección 6.3) |

## 🔴 Bloqueantes — hay que responderlos antes de sembrar

| # | Pregunta | Qué cambia |
|---|---|---|
| A | **🔴 ¿Las plantas madre están indexadas / libres de virus?** Preguntárselo al proveedor por escrito | **Es la pregunta más barata de este documento y la de mayor consecuencia.** Si la madre estaba infectada, **el 100 % de los esquejes lo está** — y la vía de multiplicación de esta colección son esquejes. Ver 4.4 |
| B | **🔴 Especificación del LED: ¿cuántos µmol/m²/s sobre el dosel, y qué proporción de rojo y rojo lejano emite?** | Un blanco frío rico en azul a 2 µmol/m²/s **puede no producir ningún efecto fotoperiódico** — el azul necesita ~30 µmol/m²/s, 15–30× más que el rojo. Se gastaría el equipo y el ensayo diría "la luz no sirvió". Ver 2.2 |
| C | **¿Cuántos cultivares distintos vienen, y cuántas plantas de cada uno?** | No hace falta saber la mezcla de color —eso se confirma en campo—, **pero sí cuántos grupos hay**, para trazar las posiciones antes de sembrar. Es la sección 4.3 y el `ensayo_dahlia_posiciones.csv` |
| D | **Fecha de entrega** | Fija la semana ISO de siembra, y con ella cuándo cae la floración respecto de la ventana de heladas |
| **E** | **🔴 ¿Qué pasa con las dalias viejas de Inv 2 — se cierran o se quedan?** | **Es la decisión de mayor apalancamiento de todo el documento** (sección 3.4). Si se cierran, se resuelven de un golpe el foco de oídio, el riesgo de virus sobre la colección nueva, el área y la ronda doble de corte. Si se quedan, entra el mínimo no negociable de la 3.4 y hay que reconsiderar Inv 4 |
| **F** | **¿Sigue en pie el ensayo de Limonium sinensis Diamond en la zona alta de Inv 2?** | `01-invernaderos.md` tiene esa zona asignada. Es el sitio que se recomienda para la dalia |
| **G** | **¿De qué tanque cuelga Inv 2, y comparte fórmula con otro bloque?** | Sin eso no se puede entregar dosis de fertirriego (sección 9.1) |

## 🟡 Necesarios para completar, no para arrancar

| # | Qué | Para qué |
|---|---|---|
| E | **`aplicaciones_historial.csv` actualizado, semanas 28 a 37** | **Sin esto la rotación de la 10.5 queda como estructura, no como bomba.** Es lo primero que hay que traer |
| F | **Dosis de etiqueta de Azufral, Timorex Gold, Agroemulsión y Alysin** | Cuatro productos con ficha confirmada y **sin dosis en el repositorio** |
| G | **Stock real de Neofat** | El inventario es del 26/03/2026 y dice *"probablemente agotado"*. En hoja de dalia, grande y cerosa, el surfactante pesa más que en otras |
| H | **Análisis del Bokashi terminado** (pendiente 4c de `CLAUDE.md`) | Sin él no se puede decir cuánto N y cuánto K están entrando ya por la base |
| I | **Decisión sobre Polyfeed y Bitter Mag** (sección 9.2) | Pendiente de validación desde el 2026-09-02 |
| J | **🟡 ¿Se valida la regla "la dalia no va en zona fresca ni sombreada"?** | Quedó como candidata en `notas_campo.md` de la skill: son tres fracasos en zonas distintas con la misma característica, no la misma zona repetida, así que no se promovió sola. **Es la regla que evitaría el cuarto intento en el sitio equivocado** |
| K | **Medición de la cama de Inv 2 y análisis de suelo de Inv 2** | La medición desbloquea las dosis de bokashi y leonardita (5.1) y cierra el `PENDIENTE MEDIR` de `capacidad_bloques.csv`. El análisis es el mismo hueco 4f de `CLAUDE.md`, que hasta ahora solo señalaba Inv 1 |

## 🔴 Nombre homologado — PAUSA

`incidencia_fitosanitaria.csv` registra las dalias como **`SIN_HOMOLOGAR`**, y
`campo_siembras.csv` las tiene con la **columna N vacía** en las dos filas.

> **Sin nombre homologado, esta siembra no aparece en el calendario de Erica.**
>
> Por la regla 5, **no se improvisa**. Y aquí hay un matiz: como son varios
> cultivares en ensayo, la pregunta no es *un* nombre sino **si el ensayo entra al
> calendario como un solo renglón o como uno por cultivar.** Eso lo decide
> `dcb-programacion`, no este documento — y de todos modos **no hay fecha de
> cosecha que dar todavía** (ver 12.4).

## 🔴 Cambios propuestos a los CSV — no aplicados

Ninguno se escribió. Requieren validación:

| Archivo | Campo | Hoy | Propuesto | Razón |
|---|---|---|---|---|
| `variedades_parametros_siembra.csv` | Dahlias · `Light` | `NO` | **`SI — extensión de día 18:00–22:00, LED R+FR, 1–2 µmol/m²/s`** | Vanessa + proveedor 2026-09-09. Día corto facultativa a 12 h de fotoperiodo natural |
| `variedades_parametros_siembra.csv` | Dahlias · `DISTANCIA SIEMBRA` | `15 cm` | **`45 × 30 cm — 1 de cada 3 líneas × 1 de cada 2 huecos, ~8 pl/m²`** | 15 cm son ~44 pl/m² y hoy las dalias están así **con mildeo persistente**. La referencia de dalia de corte es 30–45 cm. La densidad es causa directa de oídio |
| `variedades_parametros_siembra.csv` | Dahlias · nueva columna | — | **`frecuencia de cosecha = DIARIA`** | Dato de Vanessa 2026-09-09. No estaba en ningún CSV y es lo que decide el costo de jornal de tener dalia en dos sitios |
| `variedades_parametros_siembra.csv` | Dahlias · `Net` | `1` | **`2`** | Planta de 1–1,5 m con capítulo pesado |
| `ciclos_variedad.csv` | Dahlia · ciclo | `12` | **anotar que el 12 es de BULBO sin luz; para esqueje bajo 16 h es `SIN_DATO`** | Regla 1: no se estima, se mide |
| `07-datos/` | — | — | **crear `ensayo_dahlia_posiciones.csv`** | Sin él el ensayo no produce dato atribuible |

---

# 14 · Resumen ejecutable

| Etapa | Qué se hace |
|---|---|
| **0 · Recepción** | **Abrir la caja el mismo día** · aclimatar **3–5 días** en media sombra, **siempre húmedos** · descartar base acuosa u oscura (damping-off) · **🔴 etiquetar cultivar uno por uno** · preguntar al proveedor si las madres están **indexadas** |
| **1 · Sitio** | **Cama baja de Inv 3A** (decisión de Vanessa, 2026-09-09) · cerrar el lote de celosia sin traslape · **confirmar si la cama es 3A o borde de 3C** · **prueba de vasos del riego antes de sembrar** |
| **2 · Presiembra** | No-Dig: **no voltear** · **Bokashi 1 saco (25 kg) + leonardita 230 g** para la mitad que se siembra · **EN SUPERFICIE, no enterrar** · **SIN yeso** (S alto en Bloque 3) · **SIN compost como enmienda** · **🔴 camellón de 10–15 cm** — es la línea que decide en esta cama |
| **3 · Siembra** | **1 de cada 3 líneas (45 cm) × 1 planta cada 2 huecos (30 cm) = 8,3 pl/m².** **150 en la mitad de la cama (100 de los 198 huecos, ~18 m²) + 10 en materas aisladas como núcleo madre limpio.** Cepellón al ras sobre el camellón · **🔴 un cultivar por grupo, con estaca y posición registrada** |
| **4 · Inoculación** | **Cama:** Fosfolip **1,5 cc en CADA bomba** de 20 L, 4–5 bombas, arrastre con agua sola, luego plástico. **Bandeja:** **Endorhiza 10 cc + Nube 10 cc + Promobac 13 cc + Fitoderma 5 g en 5 L** (rinde 4 bandejas) — **el Fitoderma entra porque el sitio es Inv 3, donde es la regla del bloque** |
| **5 · Agua** | **🔴 Riego inmediato al sembrar y sin dejar secar 2 semanas** — el esqueje no tiene reserva · nunca regar al atardecer · **LAVADO DE DOSEL con agua sola, 10:00–13:00, 2–3×/semana, desde sem 4 hasta el primer color** |
| **6 · Luz** | **Extensión de día, LED, 18:00–22:00, todo el ciclo** · **1–2 µmol/m²/s sobre el dosel** · **rojo + rojo lejano, NO blanco frío** · **todas las plantas, sin testigo** (la luz se derrama entre camas) |
| **7 · Posiembra** | **Pinch semana 4** al 3.º–4.º par · **2 mallas** (30 y 60 cm) · **desbotone lateral** · **deshoje basal desde sem 6, cada 2 semanas**, no antes de que haya raíz nueva |
| **8 · Fertirriego** | Fórmula Inv 4+5 vigente · **Haifa Micro siempre 180 g** · **MKP 0 en el tanque** · pedir aprobación para sacar Polyfeed y Bitter Mag |
| **9 · Foliar** | Kempf por fase · **MKP foliar 125 g/bomba desde sem 7** (previa prueba de fitotoxicidad en 5 plantas) · rotación de 4 semanas · **aceite y azufre a 21 días** · **entomopatógeno nunca con fungicida de amplio espectro** · **Revus e Infinito NO — son para oomicetos** |
| **10 · Virus** | Aceite mineral en cobertura completa · bajar N soluble · marcar sintomáticas **después del pinch** · **🔴 solo esquejar de plantas sin síntoma** · cuchillo desinfectado |
| **11 · Cosecha** | **⅔–¾ abierta**, antes de las 9 am, agua a 70–80 °C, vida en vaso 4–6 días |
| **12 · Medir** | **🔴 Semana de primera pústula POR CULTIVAR** (el resultado principal) · longitud de tallo tallo por tallo · ciclo real · termómetro en cama · color confirmado · vida en vaso |

**Lo que NO se hace:** no se parte el manejo entre camas · no se planta revuelto ·
no se le da fecha de cosecha a Erica todavía · no entra Fitoderma · no entra
Revus ni Infinito · no se agrega K ni Mg al suelo.

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
- [OSU · Photoperiodic Lighting](https://u.osu.edu/indoorberry/photoperiodic-lighting/) y [Ohio CEAC · Photoperiodic Lighting](https://ohceac.osu.edu/CEBPI-Photoperiodic-Lighting) — **1–2 µmol/m²/s sobre el dosel**, ~1/100 de la intensidad de una luz de crecimiento
- [Greenhouse Grower · Greenhouse Lighting for Long Days](https://www.greenhousegrower.com/technology/greenhouse-lighting-for-long-days/) — 2 µmol/m²/s o 10 pie-candela como mínimo; rojo + rojo lejano a baja intensidad es lo más eficaz en plantas de día largo; **el azul necesita ~30 µmol/m²/s, 15–30× más**
- [GPN · Including Far Red in an LED Lighting Spectrum](https://gpnmag.com/article/including-far-red-in-an-led-lighting-spectrum/) — el fitocromo responde a rojo (630–660 nm) y rojo lejano (730–760 nm)
- [Thrive Agritech · Greenhouse Photoperiod Lighting Guide](https://www.thriveagritech.com/blog-posts/greenhouse-photoperiod-lighting-guide)

**Virosis y pulgón**

- [USU Extension · Dahlia Mosaic Virus](https://extension.usu.edu/planthealth/news/dahlia-mosaic-virus) — 16 especies de pulgón, transmisión no persistente, herencia en tubérculo
- [UMaine Extension Bulletin #5070 · Common Questions about Dahlia Mosaic Virus](https://extension.umaine.edu/publications/5070e/) — hipoclorito 10 % un minuto entre plantas; no descartar sintomáticas antes del pinch y dos aplicaciones de N
- [American Dahlia Society · Understanding Virus in Dahlia](https://www.dahlia.org/docsinfo/understanding_virus_in_dahlia-3/)
- [Dahlia Mosaic Virus · ScienceDirect Topics](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/dahlia-mosaic-virus) — **el DMV se propaga fácilmente por propagación vegetativa; la vía más probable de introducción a una finca son tubérculos o esquejes infectados**
- [Spring Hill Nursery · What Are Virus-Indexed Dahlias?](https://springhillnursery.com/pages/what-are-virus-indexed-dahlias) — qué significa material indexado y por qué se pregunta
- [USU Extension · Dahlia Mosaic Virus on Dahlia (ficha PDF)](https://extension.usu.edu/planthealth/factsheets/Dahlia-Mosaic-Virus.pdf)
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
