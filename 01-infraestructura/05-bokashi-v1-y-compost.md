# Bokashi V1 y compostaje térmico — preparación de camas

> **Decidido con Vanessa, sesión 2026-09-02.** El Bokashi V1 se prepara **esta semana**.
> La muestra para análisis sale **de esta misma tanda**, cuando esté terminada.
> Resultado esperado en ~15 días.

## Receta V1 — cambios respecto a la actual

| Ingrediente | Actual | **V1** | Decisión |
|---|---|---|---|
| Equinaza fresca | 800 kg | **800 kg** | Sin cambio — gratis, hay mucha |
| Tierra negra | 400 kg | **400 kg** | Sin cambio — gratis, hay mucha |
| King grass picado | 160 kg | **160 kg** | Sin cambio — gratis, hay mucho |
| Biochar | 80 kg | **80 kg** | Sin cambio — propio |
| **Harina de maíz** | 320 kg | **200 kg** | 🔽 **−120 kg** — ver abajo |
| Melaza | 60 kg | **60 kg** | Sin cambio — es el combustible del fermento |
| Levadura | 1 kg | **1 kg** | **Solo esta tanda.** La siguiente va con EM-1 |
| ~~Ceniza de madera~~ | 40 kg | **FUERA** | 🔴 La fuente de K más concentrada de la receta |
| ~~Humus de lombriz~~ | 80 kg | **FUERA** | 🔴 $160.000 — el ingrediente comprado más caro después de la harina |
| ~~Sulfato de cobre~~ | 200 g | **FUERA** | 🔴 El Amilsol Cu15 cubre todo el cobre, y bloquea el EM-1 |

## Costo

| | Actual | **V1** |
|---|---|---|
| Insumos | 1.941 kg | 1.701 kg |
| Produce | 1.500 kg (60 sacos) | **1.314 kg (53 sacos)** |
| Costo total | $883.000 | **$553.000** |
| **Por saco de 25 kg** | $14.717 | **$10.518** |
| | | **−28,5%** |

**De dónde sale el ahorro:** humus de lombriz −$160.000 · harina de maíz −$168.000 ·
sulfato de cobre −$2.000. **Total −$330.000 por tanda.**

## Por qué salen la ceniza y el sulfato de cobre

**Ceniza de madera.** Es el ingrediente **más concentrado en potasio** de la receta — *potash*
viene literalmente de ahí — sobre un suelo con saturación de K de 24–30%. Y hay un argumento de
consistencia: **se eliminó la cal agrícola porque el pH ya estaba ideal, y la ceniza es
alcalinizante igual que la cal.** Es la misma decisión aplicada a otro ingrediente. Además el
fermento del Bokashi debe ser ácido (lactofermentación); la ceniza trabaja en contra.

*Orden de magnitud: 40 kg al 3–8% de K = 1,2–3,2 kg de K por tanda → 27–73 kg K/ha/año →
**0,6 a 1,6 puntos porcentuales de saturación de K al año, solo de la ceniza.***

**Sulfato de cobre.** Quedó redundante al entrar el Amilsol Cu15 (15% Cu-EDTA), que cubre tanto
el tanque como la corrección edáfica de Inv 5. Y **es incompatible con el EM-1**, que es el
reemplazo previsto de la levadura. Sacarlo resuelve tres cosas: mejor entrega de cobre, menos
azufre a un suelo con S alto, y desbloquea el EM-1. **Y elimina la excepción incómoda** anotada
en `02-nutricion/02-bioinsumos.md` sobre mantener sulfatos contra la regla.

## Por qué 200 kg de harina de maíz

| Cantidad | % de los insumos | Costo |
|---|---|---|
| 320 kg (actual) | 17,6% | $448.000 |
| **200 kg (V1)** | **11,8%** | **$280.000** |
| 150 kg | 9,1% | $210.000 |

El bokashi clásico de Restrepo usa el salvado o harina en **10–15%** de la mezcla. Los 320 kg
están en el extremo alto; los 200 kg quedan cómodos dentro del rango.

⚠️ **Es criterio de práctica general, no dato de campo.** **La prueba son las señales que ya
están en el protocolo:** temperatura **45–55 °C**, **olor dulce/fermento**, **lista en 2 semanas**.
Si esta tanda da las tres, los 200 kg quedan validados. Si el fermento arranca flojo o se enfría
rápido, subir a 250 en la siguiente.

**No bajar de 200 en la misma tanda en que además sale el humus** — son dos cosas que quitan
biología y energía a la vez.

---

# La dosis por cama: NO se toca todavía

**Razón de método, no de agronomía:**

> Ya se está cambiando la receta. Si además se cambia la dosis, y en 15 días llega el análisis,
> **no se va a poder atribuir nada.** Un cambio a la vez.

**El análisis de esta tanda convierte la dosis en un cálculo en vez de una estimación:**

```
dosis (kg/m²) =        K objetivo por m² por año
                ──────────────────────────────────────
                % de K del Bokashi × aplicaciones al año
```

Hoy esa cuenta no corre porque el `% de K` es el hueco exacto que llena el análisis.

## Lo único que sí cambia ya, y es gratis

**Reescribir el protocolo en kg/m² en vez de sacos por cama.** El artefacto está documentado en
`03-no-dig-y-preparacion-camas.md`: la cama pequeña de 3B recibe **6,41 kg/m²** contra **1,56**
de la cama grande del mismo bloque, con el mismo "3 sacos". Corregirlo **no altera ninguna
variable agronómica** — solo corrige un error de expresión.

## La diferenciación por bloque ya está bien orientada

El diseño actual es **inverso a la M.O.**, que es lo correcto:

| Bloque | M.O. | Bokashi que recibe |
|---|---|---|
| Bloque 3 | **18,6%** (la más baja) | La dosis más alta |
| Bloque 5 | 22,9% | Intermedia |
| Bloque 4 | **23,4%** (la más alta) | La más baja |

Cuando llegue el análisis, propuesta de simplificar a **dos escalones** en vez de una tabla por
cama: M.O. bajo 20% (Bloque 3) → dosis alta · M.O. 20% o más (Bloques 4 y 5) → dosis baja.
Los números exactos salen del análisis.

---

# Bokashi y compost: dos procesos, y NO compiten por recursos

| | **Bokashi** | **Compost térmico** |
|---|---|---|
| Proceso | Fermentación, bajo oxígeno | Aeróbico, con volteo |
| Temperatura | 45–55 °C | **55–65 °C sostenidos ≥3 días** |
| Tiempo | 2 semanas | 8–12 semanas |
| Función | **Alimenta** | **INOCULA** |
| Perfil biológico | Bacteriano | **Fúngico + protozoos + nematodos** |
| **Insumos** | Equinaza, harina, melaza | **Restos de cultivo y de cocina** |
| Patógenos del insumo | No los mata | **Los mata a 55–65 °C** |

**No hay que dividir recursos: usan materias primas distintas.** El Bokashi corre con equinaza de
los vecinos y lo comprado; el compost corre con lo que hoy va a una pila fría.

## 🔴 Y por qué NO se deben mezclar

> Los restos de cultivo cargan **Fusarium, Botrytis y mosca blanca** — 29 registros en
> `07-datos/incidencia_fitosanitaria.csv`. **El Bokashi a 45–55 °C no los mata.** Solo el compost
> térmico sostenido a 55–65 °C lo hace.
>
> **Meter restos de cultivo al Bokashi sería reinocular** el patógeno que se lleva dos años
> combatiendo, y ya hay inóculo confirmado en suelo de 3C, Inv 5 e Inv 4.

**Único recurso compartido:** el king grass, que en el compost haría de "marrón" (carbono) frente
al verde de los restos de cultivo. No es restricción — hay mucho.

## Para qué sirve cada uno

| | Destino |
|---|---|
| **Bokashi** | Preparación de cama — aporte nutricional y biología bacteriana |
| **Compost térmico** | **Inóculo fúngico** + materia prima del **extracto de compost**, que es lo que trae protozoos y nematodos bacterívoros — el grupo funcional que **ningún inoculante comercial vende** y que es el que libera N y P en la rizosfera |

Esa última línea es la que conecta con el problema de P soluble bajo: ver
`02-nutricion/04-diagnostico-kempf-ingham.md`.

---

# La muestra del Bokashi

- **Tomarla de esta tanda V1**, cuando esté **terminada** — no a mitad de fermentación
- Pedir **análisis de abono orgánico completo**: N, P, K, Ca, Mg, S, M.O. y pH
- **El K decide la dosis.** Los demás cierran el balance de nutrientes de la finca, que hoy no cuadra

## Estimación previa del K del Bokashi, para tener referencia

Con valores de composición generales (⚠️ **no datos propios** — esto es lo que el análisis viene
a reemplazar):

| Fuente | K estimado por tanda de 1.500 kg |
|---|---|
| Equinaza 800 kg | ~2,4 kg |
| Ceniza 40 kg | 1,2 – 3,2 kg |
| Melaza 60 kg | 1,2 – 2,4 kg |
| King grass 160 kg | 0,8 – 1,2 kg |
| **Total** | **5,6 – 9,2 kg de K** |

A 1,35 kg/m² y 2,5 aplicaciones/año eso sería del orden de **169 kg K/ha/año ≈ 3,7 puntos de
saturación al año.** Si se confirma, **el Bokashi solo podría sostener el exceso de potasio** —
sacar el Polyfeed no alcanzaría. Es la razón por la que este análisis es prioritario.

---

# Pendientes de esta sección

| # | Pendiente | Quién |
|---|---|---|
| 1 | **Las proporciones actuales por cama** para reescribir el protocolo en kg/m² | Vanessa |
| 2 | **Análisis del Bokashi V1** — abono orgánico completo | Laboratorio, ~15 días |
| 3 | **Dosis de EM-1 para compostaje** (por m³ de pila) | BIOEM / FUNDASES |
| 4 | Revisar el resto del stack de cama: Cote NPK, TerraLife, Naturcomplet, micorrizas | Sesión siguiente |
| 5 | Edáficos de la lista de Alma Agrícola | Sesión siguiente |

**Nota sobre SQM edáfico:** se revisó su línea completa. **Casi todo es potasio** — Qrop KS,
Allganic Makro 60, cloruro de potasio, SOP, MKP. **Lo único edáfico de SQM que sirve es el
MAP 12-61-0 para Bloque 4**, que ya estaba identificado. No hay nada nuevo ahí.
