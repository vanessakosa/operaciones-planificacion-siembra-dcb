# Análisis de suelo — hallazgos y correcciones permanentes

## Físico-químico · Natural Control · Informe 35739-35740 · Junio 2025

| Parámetro | Inv 3 | Inv 4+5 | Interpretación |
|---|---|---|---|
| pH | 5.9 | 6.2 | **IDEAL — no agregar cal** |
| M.O. % | 19.0 | 25.6 | Excelente — el Bokashi está funcionando |
| P mg/kg | **97.20** | **103.37** | **MUY ALTO — eliminar toda fuente de P** |
| K cmolc/kg | 5.18 | 2.60 | Alto en Inv3 — reducir K en fertirriego |
| Ca | 11.03 | 8.90 | Alto — no agregar Ca al suelo |
| Mg | 1.75 | 1.89 | Medio — mantener |
| Fe mg/kg | 42.6 | 41.3 | Bajo — déficit, corregir |
| **Cu mg/kg** | **2.7** | **2.3** | **BAJO CRÍTICO — ligado a susceptibilidad a Botrytis y Oidium** |
| S mg/kg | 90.84 | 103.07 | Muy alto — **no agregar sulfatos** |
| C.E. | 0.829 | 0.456 | Inv3 con salinidad media activa |

### Lectura agronómica

El hallazgo más importante no es un exceso, es el **déficit crítico de cobre**. En el marco Kempf,
el Cu es cofactor de la lignificación y de las enzimas de defensa. Un cultivo con Cu en 2.3–2.7 mg/kg
en un ambiente de humedad nocturna alta **va a tener botrytis y oidium sin importar cuántos fungicidas
se apliquen**. De ahí la regla fija de Haifa Micro a 180 g/tanque.

El segundo hallazgo es que el suelo está **saturado de P, K, Ca y S**. Toda la estrategia de
fertilización se movió de "agregar" a "corregir lo que falta y dejar de agregar lo que sobra".

## Correcciones permanentes derivadas (NO revertir sin análisis nuevo)

| Insumo | Decisión | Razón |
|---|---|---|
| Roca fosfórica | **ELIMINADA** de Bokashi y de toda preparación de camas | P muy alto |
| Cal agrícola | **ELIMINADA** | pH ideal |
| Harina de roca | **ELIMINADA** | Acumulada en suelo |
| Haifa MKP | **ELIMINADO de TODAS las fórmulas** (Inv 3 e Inv 4+5, sin distinción) | Fuente de P |
| Haifa UP | **ELIMINADO** de todo fertirriego | Fuente de P |
| Cote NP | **ELIMINADO** — solo queda Cote NPK a dosis reducida | Fuente de P |
| Sulfatos | No agregar | S muy alto |
| Haifa Micro Hydroponic | **FIJO en 180 g / tanque 2.000 L** | Déficit crítico de Cu |
| Fullfert | Producto correcto de húmicos/fúlvicos (**reemplazó a Naturhumic**) | — |
| Salvado de trigo | Eliminado del Bokashi | Harina de maíz es más económica |

**Si en el futuro se necesita más K en Inv 4+5:** usar una fuente de K libre de P
(sulfato de potasio o nitrato de potasio). **Nunca MKP.**

**Punto sin resolver:** Bitter Mag introduce azufre adicional en un suelo que ya tiene S muy alto,
sobre todo en Inv 3. Está señalado como pendiente de resolver. Al reevaluarlo, considerar una
fuente de Mg sin sulfato (ej. nitrato de magnesio) y comparar costo.

## Microbiológico · Bioquirama

| Fecha | Trichoderma | Fusarium | Interpretación |
|---|---|---|---|
| Ago 2024 | 1.1×10⁴ UFC/g | 5×10⁴ | Bajo — cultivo vulnerable |
| Nov 2025 | **1.4×10⁶ UFC/g** | 3×10⁴ | Excelente — **127× más Trichoderma** |

**Conclusión: el programa biológico funciona.** Fusarium bajando pero persiste.

Esta cifra es la que justifica todo el enfoque No-Dig: **el Trichoderma en 1.4×10⁶ se destruye
con cada volteo profundo.** No voltear es proteger una inversión biológica de más de un año.

## Estrategia frente a Fusarium

- Fusarium es **condición base del terreno**, presente desde el primer análisis
- **La estrategia NO es eliminarlo — es biosuprimirlo** con diversidad microbiana competitiva
- Biosupresores probados en campo: **marigold, gomphrena, matricaria** intercalados con lisianthus
- Inoculantes específicos: Fitoderma (Trichoderma + Bacillus) y Pokonia (Trichoderma harzianum) en drench

## Análisis pendientes

- Inv 3B e Inv 4 — muestras enviadas, resultado pendiente de incorporar
- Al llegar: comparar contra los valores de junio 2025 para medir si las correcciones
  (eliminar P, K, cal) están moviendo la aguja, y recalibrar las fórmulas de fertirriego

## Dónde subir un análisis nuevo

**Drive → `DCB Claude / 07_Operaciones / 01-infraestructura`**
https://drive.google.com/drive/folders/1YldcNcUhk2mk38A0yvpXYkwhOlZbCau5

El PDF del laboratorio va tal cual, sin transcribir. Nombrarlo con la fecha
adelante para que no se pisen: `2026-08-analisis-suelo-Inv3B.pdf`.

**Por qué Drive y además el repo.** El acceso a Drive está atado a la cuenta,
no al repositorio: desde otra máquina, o con el conector caído, esos PDF no se
pueden abrir. Lo único que viaja siempre con `git pull` es lo commiteado. Por
eso el flujo es el mismo que el del registro de tallos —el Excel vive en Drive
y `07-datos/registro_tallos.csv` es el espejo que viaja—: **Vanessa sube el PDF
a Drive, y los números extraídos más la interpretación se escriben acá.**

El PDF es la fuente; este archivo es lo que leen las fórmulas de fertirriego.

## Qué se recalcula cuando llega un análisis nuevo

No es "actualizar la tabla". Cada valor mueve una decisión concreta que hoy
está congelada, y conviene revisarlas en este orden:

| Si cambió | Qué se revisa |
|---|---|
| **Cu** subió de 2,3–2,7 | Si Haifa Micro puede bajar de los 180 g/tanque fijos. Es la regla más cara del programa y la única razón de que exista |
| **P** bajó de ~100 mg/kg | Si se puede volver a permitir alguna fuente de P. Hoy hay 6 insumos eliminados por esto |
| **K** en Inv 3 bajó de 5,18 | Si se puede volver a subir K en fertirriego, y con qué fuente (nunca MKP) |
| **S** bajó de 90–103 | Destraba el punto pendiente de Bitter Mag, que hoy mete azufre en un suelo saturado |
| **C.E.** de Inv 3 bajó de 0,829 | La salinidad activa de Inv 3 es la causa documentada de los tallos cortos de lisianthus |
| **M.O.** se sostuvo sobre 19 % | Confirma que el bokashi y el No-Dig funcionan, o avisa que hay que ajustar la dosis |
