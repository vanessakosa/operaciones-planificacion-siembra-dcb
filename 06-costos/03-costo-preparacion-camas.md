# Costo de preparación de camas

Estado al 2026-09-03. Fuente de cantidades: **`Protocolo_Preparacion_Camas_DCB_v7.pdf`**
(compartido por Vanessa el 2026-09-03) cruzado con las áreas de cama de
`01-infraestructura/03-no-dig-y-preparacion-camas.md`.

Nota para David: `06-costos/DCB-Preparacion-Camas-David.pdf`.

## El protocolo tiene cinco productos, y solo uno tiene costo

| Producto | Dosis | Estado del costo |
|---|---|---|
| **Bokashi** | Sacos por cama, tabla abajo | ✅ **$10.075 / saco de 25 kg** |
| **Haifa Cote NP** | ⅓ del Cote total | 🔴 **Falta precio por kg** |
| **Haifa Cote NPK** | ⅔ del Cote total | 🔴 **Falta precio por kg** |
| **Naturcomplet-G** (leonardita) | STD 300 g fijos · PREMIUM 50 g/m² · EMERG. 60 g/m² | 🔴 **Falta precio** |
| **Sáfer Terra Life GR** | **100 g/m²** en los tres protocolos | 🔴 **Falta precio** |

**Cote total: 100 g/m² en ESTÁNDAR y EMERGENCIA · 200 g/m² en PREMIUM.** Relación NP:NPK ≈ 1:2.

## Cantidades por cama, verificadas contra el área

| Bloque | Área | Bokashi STD | Bokashi PREM | Terra Life | Cote STD | Cote PREM |
|---|---|---|---|---|---|---|
| Inv 3B | 48,1 m² | 3 sacos | 4 sacos | 4,81 kg | 4,81 kg | 9,62 kg |
| Inv 4C | 40,5 m² | 2,5 sacos | 3 sacos | 4,05 kg | 4,05 kg | 8,10 kg |
| Inv 3A | 35,6 m² | 2 sacos | 3 sacos | 3,56 kg | 3,56 kg | 7,13 kg |
| Inv 5 | 31,7 m² | 2 sacos | 2,5 sacos | 3,17 kg | 3,17 kg | 6,34 kg |
| Inv 4A · 4B | 20,2 m² | 1 saco | 1,5 sacos | 2,02 kg | 2,02 kg | 4,05 kg |
| Inv 3C | 18,0 m² | 1 saco | 1,5 sacos | 1,80 kg | 1,80 kg | 3,60 kg |

**Inv 1 e Inv 2 se preparan con la dosis de Inv 4A/4B**, según nota del protocolo v7.
**El Mini no tiene fila** — hueco confirmado, ya anotado en el protocolo de No-Dig.

## Costo por cama, solo Bokashi

| Sacos | Receta anterior | **V1** | Ahorro |
|---|---|---|---|
| 1 | $14.400 | **$10.075** | $4.325 |
| 1,5 | $21.600 | **$15.113** | $6.488 |
| 2 | $28.800 | **$20.150** | $8.650 |
| 2,5 | $36.000 | **$25.188** | $10.813 |
| 3 | $43.200 | **$30.225** | $12.975 |
| 4 | $57.600 | **$40.300** | $17.300 |

**Piso anual** con las 60 camas contadas (3A 11 · 3C 8 · Inv 4A/4B 28 · Inv 5 13) = 84 sacos por
vuelta: **$363.300 de ahorro por vuelta**, o **$727.000 – $1.090.000 al año** a 2–3 vueltas.
Piso, no estimado: **falta contar 3B** (la dosis más alta), Inv 2, Mini, exteriores e Inv 6.

---

# 🔴 Los cotes: el renglón más grande, sin precio y sin aplicar

**Dato de Vanessa 2026-09-03:** los cotes **no se aplican desde hace unos dos meses**, pero los
que ya están en el suelo **siguen liberando** — son de liberación lenta, así que el efecto de
haberlos suspendido todavía no se ve completo. Es la razón por la que esto hay que revisarlo a
fondo antes de concluir nada sobre rendimiento.

**Cantidades que el protocolo v7 sigue pidiendo**, solo con las 60 camas contadas:

| Protocolo | Por vuelta | A 2–3 vueltas/año |
|---|---|---|
| ESTÁNDAR (100 g/m²) | 151 kg | **300 – 450 kg/año** |
| PREMIUM (200 g/m²) | 303 kg | 600 – 900 kg/año |

Sin 3B, que es el bloque de camas más grandes. **Con el precio por kg de Cote NP y Cote NPK el
número se cierra en una línea**, y de ahí sale la decisión: los cotes vuelven, o el ahorro se
registra y el protocolo v7 se reescribe sin ellos.

## Ya hay un ensayo comparativo en campo, armado solo

`07-datos/campo_siembras.csv` tiene **20 lotes anotados** en COMENTARIOS con qué recibieron:

| Anotación | Lotes |
|---|---|
| "Sin Bokashi, con Cotes" | 15 |
| "SIN COTES SOLO BOKASHI" | 4 |
| "Sin Cotes ni Bokashi" | 1 |

⚠️ **Grupos desbalanceados y no aleatorizados** — 15 contra 4 contra 1, y las semanas de siembra
no coinciden, así que arrastran efecto de temporada. No es un ensayo limpio. Pero **cruzarlo con
`registro_tallos.csv` normalizado por ventana** es la primera evidencia propia disponible sobre
si los cotes aportaban algo que el Bokashi no aporta. Es más de lo que había.

---

# 🔴 Error de expresión en la calculadora v7

**El Naturcomplet-G en protocolo ESTÁNDAR se pide como 300 g fijos por cama**, sin importar el
área. En PREMIUM y en EMERGENCIA sí se pide como tasa (50 y 60 g/m²). Resultado:

| Cama | Área | 300 g fijos equivalen a |
|---|---|---|
| Inv 3B | 48,1 m² | **6,2 g/m²** |
| Inv 3C | 18,0 m² | **16,7 g/m²** |

**2,7× de diferencia por el mismo renglón del protocolo.** Es el mismo tipo de artefacto que el
"3 sacos por cama" ya documentado en No-Dig: dosis fija sobre camas de área distinta. Corregirlo
es reescribirlo en g/m², costo cero — pero **mientras no se corrija, cualquier costo por cama que
se calcule sobre ese renglón está mal.**

**Segundo hallazgo menor:** el Terra Life de Inv 3C se calcula sobre **18 m²**, mientras que
`03-no-dig-y-preparacion-camas.md` registra la cama grande de 3C en **25,2 m²** y la pequeña en
**12,6 m²**. Los 18 m² no son ninguna de las dos — parecen un promedio. Si es así, la cama grande
está subdosificada y la pequeña sobredosificada en los tres productos que van por tasa.

---

# Pendientes

| # | Pendiente | Quién | Desbloquea |
|---|---|---|---|
| 1 | **Precio por kg de Cote NP y Cote NPK** | Vanessa / Haifa | El renglón más grande del costo por cama |
| 2 | **Precio de Naturcomplet-G** | Vanessa | Costo por cama |
| 3 | **Precio de Sáfer Terra Life GR** | Vanessa | Costo por cama |
| 4 | **Área real de las camas de Inv 3C** — ¿25,2 y 12,6, o 18? | Vanessa | Corrige 3 productos por tasa |
| 5 | Reescribir Naturcomplet STD en g/m² | Decisión de Vanessa | Costo cero |
| 6 | Contar camas de Inv 2, Mini, exteriores e Inv 6 | Vanessa | Convierte el piso anual en cifra |
| 7 | Cruzar los 20 lotes con/sin cote contra `registro_tallos.csv` | Motor | La decisión sobre los cotes |
