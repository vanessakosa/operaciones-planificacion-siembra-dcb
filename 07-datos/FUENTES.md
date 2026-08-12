# Fuentes en Drive — inventario e IDs

Todo lo de aquí vive en `Drive / DCB Claude / 07_Operaciones`
(carpeta `1rR1-puMEi4hjlC67G4pAztXuUG4q0i5A`).

**Alcance de este proyecto: solo 07_Operaciones.** No traer material de
`01_Empresa`, `02_Marketing`, `03_Ventas`, `04_Ventas_online`,
`05_Administracion` ni `06_Agents` sin pedido explícito de Vanessa.

## Leyenda

- ✅ **espejado** — el archivo está en el repo, byte-exacto contra Drive
- 🔨 **derivado** — creado en el repo a partir de otras fuentes (no existe en Drive)
- ⬜ **pendiente** — está en Drive, todavía no en el repo

**Estado: 45 de 45 archivos de texto espejados, todos verificados byte a byte con
`motor/espejar.py`.** Lo único que queda fuera son los 4 Excel maestros, que no se
pueden espejar como texto.

## Datos (`07-datos/`) — carpeta `1aQWiCSB3c3eWa2p4QpRart7_KjI3-3KI`

| Estado | Archivo | Bytes | Drive ID |
|---|---|---|---|
| ✅ | `formulas_productos_bouquets.csv` | 8209 | `1Y9KhyA71M3DAcZBdWlpPl7Dd5DQvYeT6` |
| ✅ | `capacidad_bloques.csv` | 684 | `1c2wBglS9gXkj50vUIzSaZifIhcH8iw4B` |
| ✅ | `listas_desplegables.csv` | 1671 | `1YmXr9XrBhaLf1J7XJJtWvOSHgyF5hYeJ` |
| 🔨 | `paleta_color.csv` | — | derivado de `listas_desplegables.csv` + recetas |
| 🔨 | `ciclos_variedad.csv` | — | derivado de `dcb-variedades/references/parametros_siembra.md` |
| 🔨 | `objetivo_color_pdv.csv` | — | propuesta sin validar — requiere datos de `03_Ventas` |
| 🔨 | `mezcla_real.csv` | — | derivado de `homologacion_registro.csv` (mezcla observada por Vanessa sem23) |
| 🔨 | `incidencia_fitosanitaria.csv` | — | **extraído** de los COMENTARIOS de `campo_siembras.csv` y de `01-invernaderos.md`. 29 eventos que estaban en texto libre. `texto_original` conserva la frase literal |
| 🔨 | `microclima_bloques.csv` | — | derivado de `01-invernaderos.md`. 18 zonas en cualitativo (`confianza = CUALITATIVA`). Las columnas numéricas están en `SIN_DATO` a la espera de medición |
| ⬜ | `clima_semanal.csv` | — | **solo encabezado.** Esquema listo, sin un solo registro |
| 🔨 | `secado_variedad.csv` | — | derivado de la auditoría ficha-por-variedad (`variedades_bitacora.csv` + dictado de Vanessa). Nueva variable 12 de la matriz de decisión: aprovechamiento en seco. Arranca con 1 fila (Dusty Miller), se llena grupo por grupo |
| 🔨 | `calendario_comercial_colombia.csv` | — | derivado del dictado de Vanessa. Festivos, fechas comerciales, patrones recurrentes y temporadas mensuales — insumo para `colecciones_mensuales` (pendiente de escribir). Marcado `PROPUESTA — SIN VALIDAR` hasta cruzar con ventas reales de `03_Ventas` |
| 🔨 | `vida_en_vaso.csv` | — | derivado de la auditoría ficha-por-variedad. Llena el hueco señalado en `10-postcosecha/README.md` — no existía ni un solo dato de vida en florero antes de esta sesión. Arranca con 1 fila (Boca de Dragón) |
| 🔨 | `combinaciones_venta.csv` | — | derivado de la auditoría ficha-por-variedad. Registra afinidad de combinaciones para la estrategia de surtido (`13-optimizacion/03-...`, pendiente de escribir). Arranca con 1 fila (Boca de Dragón + Statice) |
| ⬜ | `calidad_tallo.csv` | — | **solo encabezado.** La longitud de tallo no se mide hoy en ninguna parte del repositorio |
| ✅ | `variedades_bitacora.csv` | 24535 | `1GaxNGowGOJY3Pxz9uR60XJCtxNU9H_aB` |
| ✅ | `campo_siembras.csv` | 52881 | `1OPZLQANgzQOnkpW08lloc_ALQt-kcm-4` |
| ⚠️ | `registro_tallos.csv` | 18338 | `1gZg39pa3XkpmkVTdJnys6ltRlmEBwY-O` — **DESACTUALIZADO, confirmado 2026-08-12: 361 filas / 30.119 tallos en el repo vs. 598 filas / 52.894 tallos reales en Drive (Vanessa, via Sheets). Falta el 43% del total. Ademas la hoja de Drive tiene 2 pestañas mas (CONSOLIDADO, RENDIMIENTO — esta ultima con columna "Costo semilla $") que nunca se espejaron. No usar este archivo para totales hasta reexportar las 3 pestañas completas** |
| ✅ | `variedades_parametros_siembra.csv` | 4689 | `1yvbrGcio8eEkg2BiApmDUeM1hncu9fDs` |
| ✅ | `homologacion_registro.csv` | 3286 | `1WDAqbMnyYTgaMq0-ocnhIwB9xZO_wVWQ` |
| ✅ | `aplicaciones_historial.csv` | 1784 | `18aAECzxa8DmjIkvRJ3AAMTg3AV7E9XZn` |
| ✅ | `finca_entregas_plantulas.csv` | 932 | `1jp5QnfADBMYJRoPyXE2r-IW8RIb6Zw7m` |
| ✅ | `decisiones_manejo.csv` | 767 | `1j_xX_NA7OMND98HrKPaMsUN5348bdgm-` |
| ✅ | `rendimiento_costo_lote.csv` | 169 | `12NowlTiTZU2izfeBNiMpLUgOSdD4DmV4` |
| ✅ | `consolidado_lotes.csv` | 128 | `1wEnaQgIFpmISQy-W4b8aUv1tb4GeGNas` |
| ✅ | `resumen_tallos_dia.csv` | 106 | `1_8Na6wvwys0I0ruRdRBOshRAlaeP1AZJ` |
| ✅ | `costos_productos.csv` | 58 | `1SR6YgzymEy3xqRLQmc7aPclUr323UUhh` — **vacío (bloqueo #6)** |
| ✅ | `README.md` (diccionario de datos) | 3253 | `1RucCK0U3kZDYKiLjRp3y1ELWRmzuNIfo` |

## Documentación (`.md`)

| Estado | Ruta | Bytes | Drive ID |
|---|---|---|---|
| ✅ | `00-contexto/01-empresa-y-objetivos.md` | 3004 | `1CSr-I6elvejIj0DeDnQ3VPiVSZWX9CYD` |
| ✅ | `00-contexto/02-equipo-y-operarios.md` | 3158 | `1J49WlQZTPgX6_nF-gAj-WcbaaXKS2Czb` |
| ✅ | `00-contexto/03-identidad-visual.md` | 2660 | `130VKisTHycF1OywL0mzKKVt3gh_abXPH` |
| ✅ | `00-contexto/04-reglas-operativas-criticas.md` | 3066 | `1tz3_M0SdTfInHDPEnUR6nZ2_a1TNsLTv` |
| ✅ | `01-infraestructura/01-invernaderos.md` | 7223 | `1GrXr1Yl1IjDjRm0RJjbFsIGDosxgreSc` |
| ✅ | `01-infraestructura/02-analisis-de-suelo.md` | 3982 | `1pByOtqdVuULQ9Qti-3epx2GRnwqwbw0y` |
| ✅ | `01-infraestructura/03-no-dig-y-preparacion-camas.md` | 4759 | `1dfjXXS1KWXfI_2mgGnT1hZnldvrNYebw` |
| ✅ | `01-infraestructura/04-inventario-camas-borrador.md` | 9041 | `183j-TMNGGqqIsMc5zJH3mElt9irLjVcA` |
| ✅ | `02-nutricion/01-fertirriego-formulas.md` | 4352 | `1j-S7qutDebrfm5yQYbhAxq-A_5evw3Mq` |
| ✅ | `02-nutricion/02-bioinsumos.md` | 3098 | `1_Pj4iac5yBMGGm8pGBeLvsV_O_uC0etV` |
| ✅ | `02-nutricion/03-drench-inoculacion.md` | 1629 | `106wpGl1vjNK8yj9xKDiYw3FXWgKD-vwW` |
| ✅ | `03-fitosanidad/01-reglas-y-protocolos.md` | 6032 | `1UshhYg6xPi7hLuKHECs28dAmlRn_bxXi` |
| ✅ | `03-fitosanidad/02-inventario-insumos.md` | 3942 | `1M5AP0XcpvX-mzKRtYqhokSwN96lrUYhi` |
| ✅ | `04-variedades/01-mapa-variedades.md` | 6353 | `1wgesYWEUxJS4va_ptQKJP9DN8bNK6FaX` |
| ✅ | `04-variedades/02-notas-campo.md` | 3559 | `15vK3_mdI5vKOYBYCdtDMt75Y4jy__6Ak` |
| ✅ | `05-programacion/01-sistema-prevision-cosecha.md` | 6406 | `1xHAYZelcRuRZRqhgUpkFXOICpvON5B8i` |
| ✅ | `05-programacion/02-registro-de-tallos.md` | 3475 | `1k_bfgDM6Inv2fcZVxXjn_59P21nYM5Sd` |
| ✅ | `05-programacion/03-apps-script.md` | 5825 | `11BfTI25H5wir1fDe1NQBJk9KBxFEaiWu` |
| ✅ | `06-costos/01-modelo-de-costos.md` | 4458 | `16CTFMNyS5tujKl2Az7_DrlE5vJUAAIa6` |
| ✅ | `06-costos/02-costo-por-tallo.md` | 2708 | `1wNoDkq8nUNCTSxnNY4kfdN9Xa5aQiP5G` |
| ✅ | `08-roadmap/01-vision-claude-code.md` | 4683 | `1ERynJX--dFmYSwQ4QhkSOyqgrDYPiciG` |
| ✅ | `09-procedimientos/README.md` | 2211 | `1jXWgrphM1-OWiAR66fDqKPPqVp44tJkm` |
| ✅ | `09-procedimientos/B-composicion-y-sustitucion.md` | 1755 | `1JeqOdk-ZVYEgdT3riJtgJwsP-yQj2L72` |
| ✅ | `09-procedimientos/C-cierre-de-lote.md` | 4894 | `1nIwRMtalOPIT9mQ4_zcGPA13BGo6TPwa` |
| ✅ | `09-procedimientos/D-prescripcion-post-cierre.md` | 4242 | `1ZTHaDj40g_UPpq5mo8KMPTCj6S1nYMnx` |
| ✅ | `09-procedimientos/E-volumen-bombas.md` | 5165 | `1xY5FvgRjufwt5Cn9nJs5Q0sDuzMHi2n7` |
| ✅ | `09-procedimientos/F-cuando-modificar-formula.md` | 3382 | `1eejMBbfxZddij9Hx_wbauVJbgjIKB55F` |
| ✅ | `09-procedimientos/G-analisis-economico.md` | 5835 | `1g1fDY8h4mfq-2vikXK0M5xjPyAguUQos` |

**El CLAUDE.md de Drive** (`1E20Ek83XZtf6Hq3mCX9nBoJBhJPgkpXz`, 6426 bytes) ya
está incorporado y ampliado en el `CLAUDE.md` de la raíz del repo, con sus
reglas no negociables preservadas.

## Skills — carpeta `1THFw5nna83Ky_-ZUulTTdCc6KT6pq-gQ`

✅ Las 4 skills (`dcb-fitosanidad`, `dcb-programacion`, `dcb-variedades`,
`dcb-marketing`) están en `.claude/skills/`, portadas desde la instalación
local con sus `references/` completas. Se agregó `dcb-bouquets` (nueva).

## Excel maestros — demasiado grandes para espejar como texto

| Archivo | Bytes | Drive ID |
|---|---|---|
| `PROGRAMACION_2026_v8_ACTUALIZADO.xlsx` | 17 212 694 | `1NaGlBEY5j-e-rLx_7NvdIWWPWCiGxv0x` |
| `Stock Productos Agro DCB.xlsx` | 638 333 | `1lqk28pyr6Fd00U1nuPmwH9_hfVL8yZE4` |
| `DCB_Calculadora_Bouquets.xlsx` | 76 823 | `14eKUYrRhmseyqrHXxDFt2Siq97E71yVN` |
| `DCB_Registro_Tallos_v7_ORGANIZADO` | 30 986 | `14OP0GgkNmV1ty8Jz0hmASEts64ptI3y9L0i2FYsedHc` |

Los CSV de esta carpeta son el espejo en texto de estos Excel. **Verificar la
versión del `PROGRAMACION_2026` antes de tomar los CSV como definitivos** — el
export original se armó desde v7 y ya existe v8 con la homologación reparada
(306/306 siembras cruzando).

## Desorden en Drive que conviene arreglar

1. Existe una carpeta con el nombre literal
   `{00-contexto,01-infraestructura,...,skills}` (`1kaU3rBwvfvLOcLr_ZpcdXhuL4zW1mCMK`)
   — es un `mkdir` que no expandió las llaves. Está vacía; se puede borrar.
2. Hay dos carpetas de programación: `05-programacion`
   (`148Xs7HbCb3Q_fwS20D33nINbmpOg1f2s`, con los 3 `.md`) y `10-programacion`
   (`1GizeI-DrwNjhzVSJGyWplhZwKKfZcgii`, que contiene
   `planificaion-siembra/` — con typo — y ahí el `PROGRAMACION_2026_v8`).
   Conviene unificar.
3. Hay `.DS_Store` de macOS dentro de `skills/`, `skills/dcb-fitosanidad/`.
