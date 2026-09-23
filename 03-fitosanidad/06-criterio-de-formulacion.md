# Criterio de formulación de la bomba semanal

Vanessa 2026-09-23: *"que cada semana podamos hacer una formulación muy
personalizada, dependiendo del estado fenológico, de los retos fitosanitarios, del
clima... basándonos en la filosofía de John Kempf... y tú tienes que revisar con la
literatura también, porque yo lo estoy haciendo un poco como hamster wheel".*

Este documento es el **porqué**. Los datos de cada producto están en
`07-datos/productos.csv`; el chequeo mecánico lo hace `motor/formular.py`. Cada
afirmación lleva su fuente y su **nivel de evidencia**:

| Nivel | Qué significa |
|---|---|
| **FICHA** | Lo dice la ficha técnica del producto (registro ICA) |
| **LIT** | Literatura técnica o científica, citada |
| **DCB** | Observado en la finca, con fecha y quién |
| **KEMPF** | Marco de Kempf / AEA. Es un modelo de manejo, no un ensayo: se usa para ordenar decisiones, no como prueba |

---


## 0. La regla madre: vegetativo construye, floración responde

Vanessa 2026-09-23: *"empecemos a trabajar muy juiciosos con los escalones en
todo lo que está en vegetativo. En floración tenemos que responder más a las
presiones que tenemos en esta zona por la humedad... a lo largo del tiempo, si con
Kempf, la preparación de camas y el fertirriego logramos mejores niveles, ya no
vamos a tener que responder tanto a presiones."*

| Etapa | Qué manda | Cómo se elige |
|---|---|---|
| **Vegetativo · desarrollo** | Los escalones de Kempf (sección 2) | Nutricional y bioestimulante primero; la protección es preventiva |
| **Prefloración · floración** | **La presión de esta semana**: qué hongo o plaga está activo, en qué cultivo, y si está esporulando | Primero el blanco y el cultivo; después, el mejor producto para ese blanco **de la bodega o del mercado** |

Presión documentada al 2026-09-23 (Vanessa): **oidio alto**; **statice** en la ventana
de mayor susceptibilidad a botrytis; **lisianthus** con historia de botrytis y oidio;
inóculo **esporulando y en el suelo**. Cuando el hongo está esporulando se prefiere un
producto **curativo y antiesporulante** (Timorex Gold, FICHA) sobre uno solo preventivo.

### Buscar fuera de la despensa

La pregunta no es "¿qué tengo?", es "¿qué es lo mejor para este blanco en este
cultivo, compatible con agricultura orgánica?". Si lo mejor no está en bodega, se
busca en la lista del distribuidor (`07-datos/fuentes/lista_precios_agosto_2026.csv`)
y se deja como candidato de compra en **`07-datos/productos_mercado.csv`**, con su
evidencia y su precio. Un candidato entra a formulación solo cuando su ficha se lee
y pasa a `productos.csv`.

Lo que la literatura respalda para floración en invernadero (LIT):

- **Oidio:** azufre es el control inorgánico más confiable (85–96 % en ensayo) ([PMC
  2025, oidio con materiales orgánicos](https://pmc.ncbi.nlm.nih.gov/articles/PMC11813349/));
  *Bacillus pumilus* QST 2808 y *B. amyloliquefaciens* con eficacia reportada;
  *Ampelomyces* suprime pero no iguala un programa completo.
- **Botrytis:** *Bacillus subtilis*, *Aureobasidium pullulans* y *Trichoderma* controlan
  bien cuando se aplican en la etapa correcta; la eficacia varía mucho con temperatura
  y humedad ([PMC 2021, mecanismos de biocontrol de B. cinerea](https://pmc.ncbi.nlm.nih.gov/articles/PMC8707566/));
  *B. subtilis* QST 713 tiene espectro amplio en invernadero (botrytis y oidio) y
  *T. harzianum* T39 se desarrolló contra B. cinerea ([ScienceDirect, biocontrol en
  invernadero](https://www.sciencedirect.com/science/article/abs/pii/0261219495001298)).
- **Resistencia:** Botrytis desarrolla resistencia a varios modos de acción: **rotar**
  ([Plant Disease 2023](https://apsjournals.apsnet.org/doi/10.1094/PDIS-06-23-1213-SR)).
- **Statice (Limonium) específicamente:** no se encontró literatura de biocontrol
  propia del cultivo; se extrapola de otros cultivos con botrytis. Es un hueco.

## 1. Qué lleva toda bomba

**Cuatro componentes, siempre** (DCB, `01-reglas-y-protocolos.md`; Vanessa
2026-09-23: *"por ser un país del trópico, que siempre tenga un insecticida o un
fungicida, sea de contacto o biológico, ayuda muchísimo"*):

| Componente | Para qué | Productos con ficha confirmada hoy |
|---|---|---|
| Nutricional | La base de la pirámide: sin fotosíntesis completa lo demás no ocurre | Amicos MC nt · Glukoplant Ca-BZn · ADNGard |
| Bioestimulante | Energía y aminoácidos para que la planta suba de nivel | Starzyme · (Ascofol, Naturamin: parciales) |
| Fungicida | Preventivo: en el trópico la presión de botrytis y oidio es permanente | Equifun · Solar · Regalia · Timorex Gold |
| Insecticida | Preventivo de chupadores: trips, mosca blanca, áfidos | No Fly · ADN Green · Alysin · Safer Mix |
| + Coadyuvante | Cobertura y protección UV de los biológicos | Neofat (va **primero**) |

**Una bomba por semana, a veces dos.** La segunda es de **refuerzo**, dirigida a un
cultivo o un foco, y también lleva algo nutricional o de bioestimulación (Vanessa
2026-09-23: *"si ya el operario se va a poner la bomba, debería ser una bomba más
completa"*).

## 2. La etapa decide el nutricional (Kempf)

La pirámide de salud vegetal de Kempf tiene cuatro niveles; cada uno da inmunidad a
un grupo de plagas y cada uno depende del anterior (KEMPF — [AEA, Plant Health
Pyramid](https://advancingecoag.com/plant-health-pyramid/)):

| Nivel | Proceso | Minerales que lo habilitan | Qué protege |
|---|---|---|---|
| 1 | Fotosíntesis completa | **Mg, N, Fe, Mn** (Mn parte el agua, primer paso) | Base de todo |
| 2 | Síntesis completa de proteínas | Mo, S, B, Zn y N bien convertido | Insectos chupadores (trips, mosca, áfidos) |
| 3 | Lípidos / ceras en la hoja | energía sobrante + biología del suelo | Hongos aéreos (oidio, botrytis) |
| 4 | Metabolitos secundarios | todo lo anterior | Insectos masticadores, más resistencia |

Traducción a DCB:

- **Vegetativo y desarrollo:** prioridad **nivel 1 y 2**. Mn + Zn (Amicos MC), Mg,
  aminoácidos. Es la etapa donde un déficit cuesta más, porque la planta está
  armando la estructura que va a cargar la flor.
- **Prefloración y floración:** **Ca + B** (Glukoplant) para la pared celular del
  tejido que se está formando, y K para el llenado.
- El diagnóstico de suelo de Bloque 3, 4 y 5 ya está hecho con este marco en
  `02-nutricion/04-diagnostico-kempf-ingham.md`. **La savia es lo que verificaría si
  el mineral llegó**, y no se ha medido (bloqueo 4e de `CLAUDE.md`).

## 3. Lo que la planta absorbe y lo que se bota

**Calcio foliar: solo llega a lo que está creciendo en ese momento.** El Ca no se
mueve por el floema; va por el xilema, con la transpiración, y los tejidos jóvenes
transpiran poco (LIT — [Frontiers in Plant Science, "Calcium—Nutrient and
Messenger"](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2019.00440/full);
[bioRxiv 2025, paradoja de la movilidad del Ca foliar](https://www.biorxiv.org/content/10.1101/2025.07.02.662739.full.pdf)).
Menos del 5 % del Ca aplicado llega al órgano que se quiere proteger. Consecuencias:

- El Ca se aplica **cuando el botón se está formando**, no cuando la flor ya está
  abierta. En flor abierta sirve poco para la pared celular.
- Repetido y en dosis moderadas funciona mejor que una sola dosis alta.
- El Ca sí reduce la botrytis: pared más firme y menos actividad de las enzimas que
  el hongo usa para degradar la pectina (LIT — [ScienceDirect 2024, CaCl₂ contra
  botrytis en rosa de corte](https://www.sciencedirect.com/science/article/pii/S0925521424005374)).

**Elementos que se suman sin que nadie los vea.** El zinc llega hoy por **cuatro
productos** (FICHA): Starzyme 72 g/L, Glukoplant 30 g/L, Naturmix-L 12 g/L, Amicos MC
1 %, ADNGard 0,4 %. `formular.py` suma los gramos de cada elemento por bomba para
que eso se vea antes de mezclar. **El umbral de fitotoxicidad por Zn foliar en estas
especies no está documentado en el repo — pendiente de literatura.**

**Naturmix-L no es foliar.** Su ficha lo registra solo para fertirriego (FICHA,
ICA 5575). En la bomba se estaba usando fuera de etiqueta.

## 4. Dosis: la de la ficha, no la de la costumbre

Lo que las fichas destaparon el 2026-09-23 (FICHA):

| Producto | Ficha | Se venía usando |
|---|---|---|
| No Fly | 50–62,5 g/bomba (2–2,5 g/L) | 10 g — 5 a 6 veces menos |
| Regalia | 37,5–50 cc (1,5–2 L/ha a ~1.000 L/ha) | 25 cc |
| Heveacinna Beta | 250–750 cc (1–3 %) | 50 cc |

**Una dosis subletal de un biológico no es "más suave": es producto botado.** El
entomopatógeno necesita un número mínimo de esporas por insecto para infectar. Por
debajo de eso no hay control y sí hay gasto.

**Las dosis por hectárea** (Starzyme 250 cc/ha, Regalia L/ha) necesitan un dato que
no está: **cuántos litros de caldo por hectárea se asperjan**. Con la regla B4 (1
bomba cada 2 camas de ~20–36 m²) sale del orden de 350–600 L/ha, **no** 1.000. Hasta
medirlo, `formular.py` marca esas dosis como `POR_HA`.

## 5. Compatibilidad: manda la ficha de cada producto

- **Regla por clase (LIT):** un hongo o bacteria vivo en el mismo tanque que un
  fungicida es riesgo; los extractos vegetales suelen ser compatibles con
  *Trichoderma* y otros biológicos, los fungicidas de síntesis no (LIT —
  [Scialert 2012, compatibilidad de *Trichoderma* con fungicidas y
  botánicos](https://scialert.net/abstract/?doi=ijpp.2012.89.94);
  [PMC 2021, *Trichoderma* y fungicidas](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8397002/);
  [GPN, biocontroles con pesticidas](https://gpnmag.com/article/using-biocontrols-with-traditional-pesticides/)).
- **Pero la ficha manda sobre la clase:** Solar declara compatibilidad con la
  mayoría de fungicidas; No Fly con la mayoría de productos. Raxter y Safer Mix sí
  prohíben mezclar con fungicidas (FICHA).
- Cuando la ficha dice "prueba de compatibilidad" (Starzyme, Timorex, No Fly), la
  mezcla nueva se prueba en **jarra** antes de la primera aplicación: 1 L de agua con
  las dosis proporcionales, 15 minutos, mirar si precipita, corta o hace grumos.
- **ADN Green y Fitoderma:** "preferiblemente solos" (FICHA).

## 6. La hora la deciden los vivos

| Si la bomba lleva… | Hora | Fuente |
|---|---|---|
| Hongos entomopatógenos (No Fly, Safer Mix) | **Tarde** (4 p.m.). Alta HR ayuda: riego previo | FICHA No Fly |
| Solar, Botrycid, bacterias vivas | Tarde | `09-procedimientos/E-volumen-bombas.md` |
| ADN Green, ADNGard | **Mañana** (ADN Green ≤ 26 °C) | FICHA |
| Solo extractos y nutricionales, día nublado | Mañana temprano posible, si no hay rocío | Vanessa 2026-09-23 · FICHA Timorex |

**ADN Green y ADNGard piden mañana; los vivos piden tarde.** En el mismo tanque no se
puede cumplir las dos: o se separan, o se elige cuál manda esa semana.

## 7. Vida útil: sin nevera, los vivos duran poco

DCB no tiene nevera (Vanessa 2026-09-23). Botrycid pide 2–8 °C y dura 3 meses
(FICHA): **el stock actual no se cuenta como viable.** No Fly dura 6 meses a
ambiente; Solar 3–6. **Comprar biológicos vivos en la cantidad que se va a usar en
su vida útil**, no por volumen.

## 8. Botrytis: el ambiente pesa tanto como el producto

- Infecta con alta HR y en un rango amplio de temperatura; **más de 4 horas de hoja
  mojada** es la condición a evitar (LIT — [NC State Extension, Botrytis blight of
  greenhouse ornamentals](https://content.ces.ncsu.edu/botrytis-blight-of-greenhouse-ornamentals);
  [Can. J. Plant Pathol. 2020, manejo de Botrytis en
  ornamentales](https://www.tandfonline.com/doi/full/10.1080/07060661.2020.1807409)).
- Por eso: aplicar cuando la hoja **se seque antes de la noche**, y ventilar. Una
  bomba a las 5:30 p.m. en 3C (humedad nocturna, DCB) puede dejar la hoja mojada
  toda la noche.
- Regalia (inductor de resistencia) tiene evidencia limitada específica en flor de
  corte bajo invernadero (LIT — misma revisión); su ficha la registra para rosa
  (FICHA). Se usa como **complemento** preventivo, no como el control principal.

## 9. Rotación y repetición

- No repetir el mismo producto de la semana inmediatamente anterior sin razón
  escrita (DCB, `01-reglas-y-protocolos.md`).
- Respetar el intervalo de ficha: Botrycid 12 semanas, ADN Green 15 días, Glukoplant
  máximo 6 por ciclo, Amicos MC 2–5 aplicaciones cada 8–10 días.

## Lo que falta para que este criterio sea completo

1. **Litros de caldo por hectárea** por bloque — convierte las dosis `POR_HA`.
2. **Umbral de Zn y Cu foliar** en las especies de DCB — literatura.
3. **Análisis de savia** — verifica si lo aplicado llegó.
4. **Clima semanal** (`clima_semanal.csv` vacío) — decide la hora y el riesgo de
   botrytis de la semana.
