# Sistema de previsión de cosecha

## Propósito

Que **Erica** (logística y ventas) pueda consultar qué flores estarán disponibles en cualquier
semana futura, generar reportes para wedding planners y clientes corporativos, y responder
preguntas de disponibilidad **sin depender de Vanessa**.

El sistema es tan preciso como la información que lo alimenta.

## Arquitectura — las tres piezas

| Pieza | Qué hace | Dónde vive |
|---|---|---|
| **PROGRAMACION_2026** (v7 → v8) | Archivo maestro. Vanessa lo actualiza semanalmente | Google Sheets |
| **DCB_CalendarioScript.gs** | Apps Script. Genera la hoja `EXPORT_CALENDARIO` | Apps Script en el archivo de programación |
| **calendario_dcb_v3.html** | Herramienta web que ve el cliente | Computador de Erica |

## El flujo semanal

1. Vanessa actualiza la hoja **CAMPO** (siembras nuevas, ventanas, notas)
2. Erica abre el archivo en Google Sheets
3. Erica: 🌸 DCB Calendario → Actualizar Calendario de Cosecha
4. El script genera `EXPORT_CALENDARIO`
5. Erica exporta: Archivo → Descargar → CSV
6. Erica sube el CSV al `calendario_dcb_v3.html` → pestaña Actualizar datos
7. Calendario actualizado para clientes

**Tiempo real: Vanessa 15 min los lunes, Erica 5 min.**

## EL PUENTE — columna N

**El script lee la columna N (Nombre Homologado) de CAMPO y la cruza con VARIEDADES_BITACORA
para calcular las ventanas. Sin nombre homologado en columna N, esa siembra NO EXISTE para
el calendario.**

Esta es la falla #1 histórica del sistema. En un momento solo ~33 de 311 siembras cruzaban.
Después de la reparación de homologación quedaron **306 de 306 siembras activas cruzando**.

**Al agregar una siembra nueva:** si el nombre homologado no existe en la BITÁCORA,
**PAUSAR y proponerlo** — no improvisar uno, porque crea un huérfano silencioso.

## Estructura de la hoja CAMPO

Los datos empiezan en **fila 3** (fila 1 = "ETAPA 0", fila 2 = encabezados).

| Col | Índice JS | Contenido | Obligatorio para el calendario |
|---|---|---|---|
| B | 1 | Proveedor | No |
| **C** | **2** | Variedad (nombre en archivo) | No — solo referencia |
| **D** | **3** | Color DCB | Recomendado |
| E | 4 | Cantidad recibida | No |
| F | 5 | Cantidad trasplantada | No |
| G | 6 | Fecha siembra campo | No |
| **H** | **7** | **Semana de siembra** | **SÍ** |
| I | 8 | Bloque sembrado | No (pero crítico operativamente) |
| J | 9 | Inicio cosecha (mes) | No |
| K | 10 | Semana inicio cosecha | No |
| L | 11 | Fin de cosecha | No |
| M | 12 | COMENTARIOS | Aquí van las observaciones cualitativas de campo |
| **N** | **13** | **Nombre Homologado** | **SÍ — sin esto no aparece** |
| O | 14 | Tallos vendidos | No |
| P | 15 | Fecha homologada | No |
| S–U | 18–20 | Ventas WIX · Utilidad · Ventas por tallos calculadas | Análisis financiero |

**Código de color de la hoja:** camas cerradas en gris · siembras nuevas en verde ·
ensayos internos en naranja.

## Estructura de VARIEDADES_BITACORA

⚠️ **Hay DOS estructuras distintas circulando. Esto es fuente de bugs.**

**Estructura A — la que está en `PROGRAMACION_2026_v7` (hoja VARIEDADES_BITACORA), 78 filas,
datos desde fila 2:**

| Col | Índice | Contenido |
|---|---|---|
| A | 0 | Variedad |
| B | 1 | Proveedor |
| C | 2 | Zona óptima |
| D | 3 | Zona mala / descartar |
| E | 4 | **Ciclo real (sem)** |
| F | 5 | **Ventana cosecha (sem)** |
| G | 6 | Ciclo total (sem) |
| H | 7 | Calidad tallo (★) |
| I | 8 | Uso principal |
| J | 9 | Canal |
| K | 10 | Decisión (MANTENER / REDUCIR / DESCARTAR) |
| L | 11 | Cantidad referencia |
| M | 12 | Observaciones clave |

**Estructura B — la que asume el Apps Script (archivo standalone
`DCB_VARIEDADES_BITACORA`, 101 variedades, datos desde fila 4):**
col A = Paraguas · **col B = Nombre Homologado** · col D = Color DCB ·
col G = Ciclo promedio · col I = Ventana · col J = Tallos por paquete · col K = Ubicación

> **⚠️ ESTA ES LA CAUSA RAÍZ DEL BUG DE "0 SIEMBRAS" / cicloMap vacío.**
> Si se pega la Estructura A en el archivo donde el script espera la Estructura B, el script
> lee "Proveedor" como nombre homologado y "Ciclo total" como ciclo — y no cruza nada.
> **Primera tarea de la migración: unificar en un solo esquema documentado.**

## Ajuste de ciclos por época

| Época | Ajuste |
|---|---|
| Sep–Nov (nuboso/lluvioso) | **+1 a +2 semanas** al ciclo |
| Dic–Feb (verano / más luz) | **−1 semana** al ciclo |
| Mar–May | Referencia base — los ciclos están calibrados en esta época |

## Los 20+ paraguas

Bocas de Dragón · Celosías Plumosas · Celosías Spicata · Celosías Dreams Mix ·
Celosías Crestadas · Gomphrenas · Campanulas · Amarantos · Zinnias · Matricaria · Statice ·
Trachelium · Ammi · Daucus · Strawflowers · Helipterum · Dusty Miller · Lisianthus ·
Dianthus & Brianthus · Ammobium · Girasol · Marigold · Matilda · Limonium (nuevo, en ensayo)

Lista completa de nombres homologados: `skills/dcb-programacion/references/nombres_homologados.md`

## Estado del sistema

✅ **Funcionando:** BITÁCORA con ciclos reales · columnas N y D llenadas · script instalado con
umbral sem>26 · calendario HTML v3 con lector CSV, galería, modal zoom y reportes PDF ·
descripciones de catálogo aprobadas · estructura de carpetas de fotos en Drive definida ·
homologación reparada (306/306)

⏳ **Pendiente:**
- Unificar el esquema de la BITÁCORA (ver advertencia arriba) — resuelve el cicloMap vacío
- Cargar fotos en el calendario (Erica, desde Drive)
- Integrar descripciones en el HTML
- Verificar siembras faltantes: Girasol, Marigold, Ammobium, Matilda
- Definir los 8 nombres homologados de los Limonium Hilverda
- **CONSOLIDADO sin fórmulas activas** — ver `02-registro-de-tallos.md`
- Errores de formato de fecha e inconsistencias de nombres entre las tres hojas
- Función `generarEstimadoCosecha()` para el estimador de Erica (escrita y guardada)

## Sistema de fotos

Estructura en Drive: `DCB Fotos Calendario / [Paraguas] / [Serie] / [Color DCB] /`

**URLs directas obligatorias.** El link normal de Drive no funciona. Formato:
`https://drive.google.com/uc?export=view&id=ID_DE_LA_FOTO`
El ID está en el link normal, después de `/d/`.

**Nunca links de iCloud ni accesos directos.** Solo URLs directas a imágenes (.jpg, .png).
Las fotos se guardan en el navegador — se cargan una sola vez.
