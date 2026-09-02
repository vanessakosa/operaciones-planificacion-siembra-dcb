# Programa biológico — inoculantes, drench y comparativo de proveedores

> **Estado: PROPUESTA. Pendiente de revisión conjunta con Vanessa — sesión del 2026-09-03.**
> Nada aplicado a `03-drench-inoculacion.md` ni a `01-infraestructura/03-no-dig-y-preparacion-camas.md`.
>
> **Lo que se revisa mañana:** la **inoculación inicial** (pre-siembra) y la de **mitad de
> producción** (prefloración), con los precios y fichas que ya están abajo.

## 🔴 Corrección de un error del repositorio

**Pokonia® NO es *Trichoderma harzianum*. Es *Pochonia chlamydosporia*** — un **hongo nematófago**
que parasita huevos de nematodo. Confirmado por ficha, Registro ICA 10977.

| Archivo | Decía | Debe decir |
|---|---|---|
| `01-infraestructura/03-no-dig-y-preparacion-camas.md` | *"Trichoderma harzianum para Fusarium"* | ***Pochonia chlamydosporia* — nematófago** |
| `03-fitosanidad/02-inventario-insumos.md` | *"Control biológico fusarium / nematodos"* | Nematodos correcto; fusarium es secundario |

**Consecuencia:** un análisis previo lo declaró redundante con el Trichoderma residente
(1,4×10⁶ UFC/g). **Ese argumento era falso** — son géneros y funciones distintas, y ningún otro
producto del programa cubre nematodos.

## Precios recibidos · 2026-09-02 · fuente Vanessa

| Producto | Precio | COP/L o /kg |
|---|---|---|
| Estabios | 1 L | **$59.000** |
| Promobac | 1 L | **$59.000** |
| Biohar Forte | 1 L | **$123.000** |
| Pokonia | 1 L | **$129.000** |
| Fitoderma | 500 g | **$120.922/kg** |

De la lista de Alma Agrícola: **Fosfolip** $52.140/L (caneca 20 L) · **EM FUNDASES** $10.447/L
(caneca 20 L) · **Safer Micorrizas** $3.272/kg.

## Costo del tanque de drench de 2.000 L (dosis vigentes)

| Bloque | Composición | Costo |
|---|---|---|
| **Inv 3** | Fitoderma $60.461 + Estabios $29.500 + Promobac $29.500 | **$119.461** |
| Inv 4 / Inv 5 / Inv 2 | Estabios $29.500 + Promobac $29.500 | **$59.000** |

El Fitoderma solo es el **51%** del tanque de Inv 3.

## Ranking por función única

| $/tanque | Producto | Función | Veredicto |
|---|---|---|---|
| **$29.500** | **Estabios** | PGPR + solubilización de fosfatos | ⚠️ Ver análisis por organismo abajo |
| $29.500 | Promobac | Bacillus PGPR | ✅ Género distinto, no redundante |
| $60.461 | Fitoderma | Trichoderma + Bacillus | ✅ Solo Inv 3 por Fusarium activo — correcto |
| — | Pokonia | *Pochonia chlamydosporia*, nematófago | ⚠️ Función única, pero **sin verificar que el problema exista** |

---

# Estabios — 4 organismos, uno aporta valor único

**Ficha confirmada:** *Azotobacter vinelandii · Azospirillum brasilense · Bacillus subtilis ·
Pseudomonas fluorescens* — **1×10⁸ UFC/mL** (aparentemente el total del consorcio).

| Organismo | Qué hace | ¿Sirve en DCB? |
|---|---|---|
| Azotobacter vinelandii | Fija N | 🔴 No — N-NO₃ en 64,4 mg/kg |
| Azospirillum brasilense | Fija N | 🔴 No — y la ficha dice que se asocia *"principalmente gramíneas"* |
| Bacillus subtilis | Fungicida/fungistático + ISR | ⚠️ Sirve, **pero se solapa con el Promobac** |
| **Pseudomonas fluorescens** | **Solubiliza fosfatos fijados** vía ácidos orgánicos | ✅ **El único valor único** |

**Costo por unidad de solubilizador de fósforo:**

| Lectura de la ficha | Estabios | Fosfolip |
|---|---|---|
| **A** (probable): 1×10⁸ es el total → Pseudomonas ~2,5×10⁷/cc | **$236** | **$52,14** — 4,5× más barato |
| B: 1×10⁸ es por organismo | $59 | $52,14 — 1,13× más barato |

**Confirmar con el proveedor cuál lectura es.** Cambia el margen, no la dirección.

### 🔴 Y la dosis que se aplica no es verificable

| | |
|---|---|
| Etiqueta (hortalizas) | **1,0 – 2,0 cc por LITRO de agua** |
| En tanque de 2.000 L | 2.000–4.000 cc = **$118.000 a $236.000/tanque** |
| **Lo que se aplica hoy** | **500 cc = 0,25 cc/L** → 4 a 8× por debajo |

**No es concluyente:** la etiqueta da concentración **sin base de área**. Si asume una caneca de
200–500 L, los 500 cc pueden estar bien en masa y solo diluidos. **Pedir la dosis en L/ha.**

---

# Fosfolip vs Fosforiz — los dos solubilizadores de P

| | **Fosfolip** (BIO-CROP) | **Fosforiz** (FUNDASES) |
|---|---|---|
| Organismo | *Penicillium janthinellum* | *Pseudomonas fluorescens* |
| Tipo | **HONGO** | BACTERIA |
| UFC | 1×10⁸/cc | 1×10⁸/mL |
| Dosis etiqueta | **1–2 L/ha** | **5 L/ha, 2 por ciclo** |
| Vida útil | no declarada | 90 días |
| Precio | **$52.140/L** | **SIN DATO — no lo distribuye Alma Agrícola** |
| Disponibilidad | ✅ mismo pedido | ⚠️ proveedor aparte |

> **Punto de equilibrio: el Fosforiz conviene solo si cuesta menos de $20.856/L**, porque su
> etiqueta pide 2,5× más volumen por hectárea.

**Ventaja no económica del Fosfolip:** es un **hongo**, y a **pH 5,6–5,8** los hongos están
favorecidos sobre las bacterias, producen ácidos orgánicos más fuertes y persisten más en suelo.
La Pseudomonas coloniza rápido pero su población colapsa sin exudado radicular continuo.
*(Microbiología general — jerarquía nivel 4 — pero el pH sí es dato propio.)*

**Mecanismo:** ambos liberan el fosfato produciendo ácidos orgánicos que quelatan el Fe y el Al y
compiten por los sitios de sorción. **Es exactamente la vía que necesita un andisol** — el mismo
argumento por el que funciona la leonardita.

### 🔴 Advertencia de la ficha del Fosforiz que valida el protocolo actual

> *"Materiales a evitar: No almacenar o mezclar junto con oxidantes, fungicidas, bactericidas,
> insecticidas, pesticidas o **fertilizantes químicos**."*

`03-drench-inoculacion.md` ya dice *"Inv 3 — Haifa: NO esa semana"*, pero en Inv 4 e Inv 5 dice
*"Sí reducido"*. **La ficha indica que la semana de drench no debe llevar fertilizante químico en
ningún bloque.** El instinto para Inv 3 era correcto; hay que extenderlo.

## Costo del drench propuesto

| Bloque | HOY (Est + Pro) | Fosfolip 2 L/ha | **PROPUESTO** | Ahorro |
|---|---|---|---|---|
| Inv 3 | $59.000 | 205 cc | **$40.178** | **32%** |
| Inv 4 | $59.000 | 135 cc | **$36.560** | **38%** |
| Inv 5 | $59.000 | 82 cc | **$33.796** | **43%** |

**Y la carga de solubilizador no baja:** Estabios 500 cc entrega 1,25×10¹⁰ UFC de Pseudomonas;
Fosfolip entrega 2,05×10¹⁰ (Inv 3), 1,35×10¹⁰ (Inv 4), 0,82×10¹⁰ (Inv 5).

**Lo que se pierde y hay que decirlo:** la resistencia sistémica inducida de la Pseudomonas. El
Bacillus del Promobac cubre su parte del ISR, pero no es sustitución perfecta. **Por eso se
propone ensayo partido, no cambio a ciegas.**

---

# Pokonia — el costo estaba inflado 10×, y la pregunta real es otra

**Dosis de etiqueta: 1 L/ha, mensual.** *(El "0,5–2,5 cc/L" es la concentración para ~2.000 L de
agua por ha; manda la masa por hectárea.)*

| Bloque | Área | cc/tanque a etiqueta | $/tanque |
|---|---|---|---|
| Inv 3 (3A+3B+3C) | 1.024 m² | **102 cc** | $13.210 |
| Inv 4 | 677 m² | **68 cc** | $8.733 |
| Inv 5 | 412 m² | **41 cc** | $5.315 |
| **Finca (0,218 ha)** | | **218 cc/mes** | **$28.148/mes → $337.774/año** |

Una estimación previa asumió 500 cc/tanque por analogía y dio $774.000–3.096.000/año.
**Estaba inflada.** Los 500 cc equivalen a **12 L/ha en Inv 5, doce veces la etiqueta.**

🔴 **Verificar cuántos cc aplica Alexander por tanque.**

**Vida útil 4 meses.** A dosis de etiqueta un litro dura 4,6 meses → **comprar de 1 L a la vez,
nunca más.**

### La pregunta real

> **Se pagan ~$338.000/año por un controlador de nematodos, y nunca se han contado nematodos.**

No hay un solo conteo en el repositorio. Es plausible que existan (4 años de cultivo continuo,
lisianthus repetido), pero plausible no es medido. **El panel biológico completo de Ingham incluye
nematodos por grupo funcional** — un solo análisis contesta esto y, de paso, si están los
bacterívoros que liberan N y P.

---

# EM-1 — no va al tanque, va al Bokashi

| | UFC |
|---|---|
| EM-1: fotosintéticas 1,6×10⁴ · ácido lácticas 4,3×10³ · levaduras 3,3×10⁴ | ~10⁴ |
| Fosfolip / Fosforiz / Estabios | 1×10⁸ |

**Es ~3.000× menos concentrado. No es un inoculante concentrado: es un cultivo iniciador que se
multiplica.** Activación: 5% EM-1 + 5% melaza + 90% agua, hermético, 3–6 días, hasta pH ≤3,5.

**Al tanque no conviene:** escalando su dosis (10 L por cilindro de 200 L), un tanque de 2.000 L
pediría 100 L activado = **$49.157**, casi lo mismo que el Estabios+Promobac de hoy.

## Donde sí: reemplazar la levadura del Bokashi

| | Costo |
|---|---|
| Levadura actual (1 kg, La Cantaleta) | **$37.000** |
| EM activado ~6 L | **$2.949** |
| | **12,5× más barato** |

Y aporta bacterias fotosintéticas + ácido lácticas + levaduras + enzimas, no solo levadura.

⚠️ **La dosis para compostaje no está en la ficha** (solo bomba de 20 L y cilindro de 200 L).
**Pedirla a BIOEM.** Los 6 L son estimación de práctica general.

## 🔴 El conflicto que se resuelve solo

**EM-1 es incompatible con cloro, desinfectantes, SULFATO DE COBRE, oxidantes y pesticidas.**
La receta del Bokashi tiene **sulfato de cobre 200 g**; el Supermagro tiene 50 g más.

**Pero el Amilsol Cu15 ya cubre todo el cobre** (tanque + corrección de suelo de Inv 5).
**El sulfato de cobre del Bokashi quedó redundante. Sacarlo desbloquea el EM-1.**

Una decisión resuelve tres cosas: cobre mejor entregado (quelatado, sin S), el Bokashi pierde un
aporte de azufre innecesario, y se abre la vía del EM-1. **Y desaparece la excepción incómoda**
anotada en `02-bioinsumos.md` sobre mantener sulfatos contra la regla.

---

# Descartados, con razón

| Producto | Por qué |
|---|---|
| **Nufosol SC** ($7.921/L) | 6 organismos: 2 fijan N (no se necesita), *Rhizobium japonicum* es para leguminosas (inútil aquí), 2 marginales. Su *Penicillium* está a **1×10⁷ — 10× menos que el Fosfolip**. Resulta **1,52× más caro por unidad del organismo útil** pese a ser 6,6× más barato por litro |
| **Azobac** | Fijador de N atmosférico. Mismo problema |
| **Vermiwash** | Enmienda orgánica líquida sobre un suelo con 18–23% de M.O. |
| **Agrocid** | Tercer ajo-ají. Ya está la decisión: *"usar Alysin hasta agotar, no reponer"* |

**Sin resolver:** el **Biohar Forte** ($123.000/L) — no está en la tabla de drench, no tiene dosis
registrada y no se sabe su rol. Segundo producto más caro del programa.

---

# Estado del programa

| Producto | Precio | Veredicto |
|---|---|---|
| **Fosfolip SC** | $52.140/L | ✅ Entra — garrafa 4 L, $217.030 |
| **EM-1** | $10.447/L | ✅ Entra — para Bokashi y composta |
| **Promobac** | $59.000/L | ✅ Se queda — Bacillus, carga el ISR |
| **Fitoderma** | $120.922/kg | ✅ Solo Inv 3 |
| **Pokonia** | $129.000/L | ⚠️ Verificar dosis + **contar nematodos** |
| **Estabios** | $59.000/L | ⚠️ Ensayo partido |
| **Fosforiz** | ? | ⏳ Conviene bajo $20.856/L |
| Nufosol · Azobac · Vermiwash · Agrocid | — | 🔴 Descartados |
| **Biohar Forte** | $123.000/L | ⚠️ Sin rol ni dosis |

## Ensayos propuestos

| Ensayo | Dónde | Indicador | Por qué ahí |
|---|---|---|---|
| **Fosfolip vs Estabios** (ambos con Promobac) | Inv 4, mitad y mitad | **P soluble al cierre** — línea base 0,107 mg/L | Indicador directo, barato, no hay que esperar tallos |
| **Pokonia sí/no** | Inv 4, mitad y mitad | Conteo de nematodos | Inv 4 es el único bloque con riego uniforme: el único donde el ensayo es válido |

## Datos que faltan

| # | Dato | A quién |
|---|---|---|
| 1 | Precio y presentaciones del **Fosforiz** | FUNDASES |
| 2 | **Dosis de EM-1 para compostaje** (por m³ de pila) | BIOEM / FUNDASES |
| 3 | Precio del **Paecilomyces** de FUNDASES | FUNDASES |
| 4 | **cc de Pokonia por tanque** que aplica Alexander | Campo |
| 5 | **Dosis del Estabios en L/ha** y si el 1×10⁸ es total o por organismo | Proveedor |
| 6 | **Qué es el Biohar Forte** y su dosis | Proveedor |
| 7 | **Conteo de nematodos por grupo funcional** | Bioquirama |

## Especificaciones a exigir en toda cotización futura

Esto vale más que esta compra puntual:

1. **UFC por organismo, no el total del consorcio.** El caso Estabios cambia el costo por función 4,5×
2. **Dosis en L/ha, no en cc/L.** Sin base de área nadie puede verificar si se aplica bien
3. **Vida útil.** Pokonia 4 meses, Fosforiz 90 días — comprar envase grande de un biológico es botar plata
