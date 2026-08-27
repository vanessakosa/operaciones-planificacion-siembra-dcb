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
| 🔨 | `combinaciones_venta.csv` | — | derivado de la auditoría ficha-por-variedad. Registra afinidad de combinaciones para la estrategia de surtido (`13-optimizacion/03-estrategia-de-surtido.md`, escrito 2026-08-27). Arranca con 1 fila (Boca de Dragón + Statice) |
| 🔨 | `cierres_lote.csv` | — | derivado del barrido de los 202 COMENTARIOS de `campo_siembras.csv` (2026-08-13). 36 lotes con **motivo de cierre** y cita literal. Hallazgo: solo el 11 % cerró por agotamiento real |
| 🔨 | `picos_cosecha.csv` | — | mismo barrido. 16 lotes con semana de inicio y de **pico** dichas en prosa |
| 🔨 | `problemas_fisiologicos_variedad.csv` | — | nuevo archivo (2026-08-27). Cubre lo que `incidencia_fitosanitaria.csv` no cubre: desordenes fisiologicos/nutricionales (caida de petalos, quiebre de tallo, arqueo de puntas, estres hidrico), distintos de plagas y hongos. Arranca con 4 filas de Boca de Dragon, dictadas por Vanessa al revisar esa ficha |
| 🔨 | `costos_follaje_comprado.csv` | — | **Primer dato de costo real del repositorio.** 6 follajes con proveedor, presentación y costo por tallo. Flower House verificado contra la **factura FH 2743 del 2026-08-20**; Ángela y Solidago por dictado de Vanessa. Trae costo con y sin IVA porque la comparación entre proveedores **cambia de ganador** según si el IVA es descontable. No va en `costos_productos.csv`: esa hoja es de agroquímicos y mide costo por cc/g. Pendiente: régimen de IVA de DCB, proveedor del Solidago, la merma del Helecho, y a qué eucalipto se refiere el `Eucalipto` genérico de los dos Yugos |
| 🔨 | `desajuste_demanda.csv` | — | mismo barrido. 13 registros de flor que **sobró o faltó**, incluidos 5 lotes de Zinnia en pico simultáneo la semana 28 |
| ⬜ | `calidad_tallo.csv` | — | **solo encabezado.** La longitud de tallo no se mide hoy en ninguna parte del repositorio |
| ✅ | `variedades_bitacora.csv` | 24535 | `1GaxNGowGOJY3Pxz9uR60XJCtxNU9H_aB` |
| ✅ | `campo_siembras.csv` | 52881 | `1OPZLQANgzQOnkpW08lloc_ALQt-kcm-4` |
| ✅ | `registro_tallos.csv` | — | **REEXPORTADO 2026-08-12** desde `DCB_Registro_Tallos_v7_ORGANIZADO` (XLSX binario) con `motor/importar_tallos.py`. 596 filas con fecha válida, 54.486 tallos frescos, rango 2026-05-31 → 2026-07-31. Antes tenía 361 filas y cortaba el 03/07: **faltaban 202 filas de todo julio.** Las 6 pestañas del libro quedaron espejadas, no 3 |
| ✅ | `variedades_parametros_siembra.csv` | 4689 | `1yvbrGcio8eEkg2BiApmDUeM1hncu9fDs` |
| ✅ | `homologacion_registro.csv` | 3286 | `1WDAqbMnyYTgaMq0-ocnhIwB9xZO_wVWQ` |
| ✅ | `aplicaciones_historial.csv` | 1784 | `18aAECzxa8DmjIkvRJ3AAMTg3AV7E9XZn` |
| ✅ | `finca_entregas_plantulas.csv` | 932 | `1jp5QnfADBMYJRoPyXE2r-IW8RIb6Zw7m` |
| ✅ | `decisiones_manejo.csv` | 767 | `1j_xX_NA7OMND98HrKPaMsUN5348bdgm-` |
| ⬜ | `rendimiento_costo_lote.csv` | 169 | `12NowlTiTZU2izfeBNiMpLUgOSdD4DmV4` — **solo encabezado, confirmado 2026-08-12 contra Drive.** La pestaña RENDIMIENTO del libro está vacía en la fuente: no es un problema de espejado sino de dato inexistente. Pide área m², costo semilla y costo insumos por lote — el mismo bloqueo que `costos_productos.csv` |
| ✅ | `consolidado_lotes.csv` | — | **REEXPORTADO 2026-08-12** con `motor/importar_tallos.py`. 141 lotes con tallos, número de registros y primera/última cosecha. Antes estaba **vacío (solo encabezado)**: la pestaña CONSOLIDADO de Drive sí se calculaba sola, simplemente nunca se había espejado |
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
| `PROGRAMACION_2026_v8_ACTUALIZADO` — **hoja nativa, 33 pestañas** | — | `1eZdmU5bYJf99SCwXSDgvGsuvUhjtRyJR26mLADv9Ef4` |
| `Stock Productos Agro DCB.xlsx` | 638 333 | `1lqk28pyr6Fd00U1nuPmwH9_hfVL8yZE4` |
| `DCB_Calculadora_Bouquets.xlsx` | 76 823 | `14eKUYrRhmseyqrHXxDFt2Siq97E71yVN` |
| `DCB_Registro_Tallos_v7_ORGANIZADO` | 30 986 | `14OP0GgkNmV1ty8Jz0hmASEts64ptI3y9L0i2FYsedHc` |

**`PROGRAMACION_2026` no se puede bajar entero:** pesa 11,5 MB y Drive responde
`File too large for export`. La lectura en texto sí funciona pero **trunca
fuerte** — el 2026-08-13 devolvió 204 KB de 11,5 MB. Sirve para buscar algo
puntual, **nunca para concluir que un dato no existe**: lo que no aparece pudo
quedar en la parte truncada. Para trabajar con CAMPO completo hay que exportar
esa pestaña sola a CSV desde Sheets.

Dentro trae una **tabla de referencia agronómica** con `SEMANAS SIEMBRA A
COSECHA` y `VENTANA DE COSECHA (SEMANAS)` para ~50 variedades, más germinación,
distancia, densidad, pinch y tallos por planta. **No está espejada en el repo** y
en algún caso contradice a `ciclos_variedad.csv` (ver el conflicto de Dahlia).
Vale la pena espejarla, resolviendo los choques uno por uno contra la jerarquía
de verdad — `VARIEDADES_BITACORA` manda para ciclo y ventana.

**Hay dos `PROGRAMACION_2026_v8_ACTUALIZADO`:** el `.xlsx` subido y una **hoja
nativa de Google Sheets** con otro ID. La nativa es la que tiene Apps Script
encima y 33 pestañas — descubierta el 2026-08-12 al diagnosticar por qué un
script no encontraba su hoja. **Verificar en cuál se está trabajando antes de
editar nada**, porque los dos se llaman igual en Drive.

Detectado también ese día: el proyecto de Apps Script de la hoja nativa
contiene un `onEdit` que busca las pestañas `REGISTRO` y `LISTAS` — que no
existen en ese libro, sino en `DCB_Registro_Tallos`. Es el handler de los
desplegables en cascada de Diana, **pegado en el libro equivocado**, donde no
puede funcionar. Ver `05-programacion/02-registro-de-tallos.md`.

Los CSV de esta carpeta son el espejo en texto de estos Excel. **Verificar la
versión del `PROGRAMACION_2026` antes de tomar los CSV como definitivos** — el
export original se armó desde v7 y ya existe v8 con la homologación reparada
(306/306 siembras cruzando).

## Cómo se refresca el registro de tallos

```bash
python3 motor/importar_tallos.py ruta/al/DCB_Registro_Tallos.xlsx
```

**Bajar el libro como texto interpretado NO sirve: trunca sin avisar.** Medido
el 2026-08-12 sobre la pestaña REGISTRO — la lectura en texto devolvió 251
filas de 598 y se cortaba el 23/06 cuando la hoja llega al 31/07. La prueba
estaba dentro del propio archivo: CONSOLIDADO reportaba 15 registros con última
cosecha 03/07 para un lote cuyas filas ya no venían. Un truncamiento silencioso
es peor que un error, porque el calendario se recalcula con menos cosecha y
nadie se entera. Hay que descargar el **XLSX binario** y parsearlo.

### La validación de rango no basta: hay que prohibir fechas futuras

El refresco del **2026-08-13** trajo **64 filas fechadas del 6 al 12 de
septiembre de 2026** — un mes en el futuro. Vanessa confirmó ese mismo día que
son de **agosto**, con el mes mal tecleado. Con el 09 cambiado por 08 la corrida
queda continua y los **dos únicos días sin cosecha son los dos sábados**:

| Fecha | Día | Filas |
|---|---|---|
| 08-01 | **sábado** | — |
| 08-02 a 08-07 | dom–vie | 8, 6, 13, 9, 14, 8 |
| 08-08 | **sábado** | — |
| 08-09 a 08-12 | dom–mié | 10, 10, 9, 13 |

La lección importante: **la validación de rango 2025–2027 no atrapa esta clase
de error**, porque `2026-09` cae dentro del rango. Cierra el dígito del año, no
el del mes. La regla que sí lo cierra es prohibir fechas futuras, con fórmula
personalizada en la validación de datos de la columna Fecha:

```
=Y(A3>=FECHA(2025;1;1); A3<=HOY())
```

`HOY()` se recalcula solo, así que no necesita mantenimiento, y habría
rechazado las 64 filas **en el momento de capturarlas** — que es cuando Diana
todavía recuerda qué día cosechó.

`importar_tallos.py` también reporta ahora cualquier fecha posterior a hoy,
aunque la importe: perder el dato es peor que tenerlo marcado.

### Correcciones de fecha aplicadas en el import

La hoja de Drive tiene fechas mal tecleadas. `importar_tallos.py` las corrige
de forma explícita y las reporta en cada corrida — **nunca en silencio.** Las
tres reglas las confirmó Vanessa el 2026-08-12:

| Fecha en Drive | Corregida a | Filas | Por qué |
|---|---|---|---|
| `2056-07-06/07/08` | `2026-07-06/07/08` | 61 | Año mal tecleado; filas vecinas son de julio 2026 y los conteos son coherentes |
| `2026-09-19` | `2026-06-19` | 2 | Fila suelta entre el 18 y el 19 de junio, mismo lote y cantidad que la cosecha del 18/06 |
| `2025-06-17` | `2026-06-17` | 2 | Cae dentro de la corrida diaria de Ammobium en Inv 3A, que va del 08/06 al 26/06 de 2026 sin huecos |
| `2026-09-06` a `2026-09-12` | `2026-08-06` a `2026-08-12` | 110 | Mes mal tecleado. **Solo se aplica si la fecha aún no ocurrió** — cuando septiembre llegue de verdad la regla deja de dispararse sola y los registros legítimos pasan intactos |

Cada regla aparece 2 veces porque la fecha mala está también propagada a la
columna `Última cosecha` de CONSOLIDADO (el 2056 afectaba 28 lotes).

**El libro en Drive sigue teniendo los valores originales** — no hay
herramienta de escritura sobre Sheets en este repositorio. Si se arreglan allá,
estas reglas dejan de encontrar coincidencias y no hacen nada: el import es
idempotente en cualquiera de los dos casos. El año 2025 **no** se generaliza a
2026: es una regla de una sola fila, por si el libro trae historia legítima de
2025 más adelante.

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
