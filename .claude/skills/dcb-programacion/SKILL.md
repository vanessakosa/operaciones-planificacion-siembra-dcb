---
name: dcb-programacion
description: Cómo funciona el Sistema de Previsión de Cosecha de Dreams Can Bloom (DCB) — el archivo PROGRAMACION_2026, la hoja CAMPO, la VARIEDADES_BITACORA, el script de Apps Script que genera el calendario, y el calendario_dcb_v3.html que usa Erica. Usar esta skill SIEMPRE que Vanessa haga su brain dump semanal de campo, dicte cambios de siembra, pregunte por ventanas de cosecha, disponibilidad futura de una variedad, calcule fechas de cosecha, mencione "nombre homologado", "columna N", "EXPORT_CALENDARIO", el calendario de Erica, o pida actualizar/generar el PROGRAMACION_2026. También usar si algo del calendario no está funcionando (ej. "0 siembras", una variedad no aparece) o si se va a agregar una siembra nueva y hay que decidir el nombre homologado correcto. No usar para temas de fertirriego, fitosanidad o costos — esos son otras skills/contextos de DCB.
---

# DCB Programación

Esta skill enseña cómo funciona el Sistema de Previsión de Cosecha de Dreams Can Bloom, para que Claude pueda mantener el archivo maestro de programación, calcular ventanas de cosecha correctamente, y ayudar a Vanessa a decidir cómo registrar cambios semanales sin romper el calendario que usa Erica.

El documento completo de referencia es `DCB_Contexto_Operaciones.docx` (vive en el proyecto). Esta skill resume lo operativo; si hay duda sobre un detalle, revisar ese documento.

## Lo esencial en 5 puntos

1. **Dreams Can Bloom** es un multicultivo de flores orgánicas en Rionegro, Antioquia. El archivo principal es **PROGRAMACION_2026**, con tres hojas clave: **CAMPO** (todas las siembras), **VARIEDADES_BITACORA** (ciclos reales de cosecha por variedad) y **EXPORT_CALENDARIO** (se genera automáticamente con un script, no se edita a mano).
2. En CAMPO, las columnas más importantes son: **C = Variedad, D = Color DCB, H = Semana de siembra, N = Nombre Homologado**. La columna N es crítica — debe coincidir EXACTAMENTE con la columna B de VARIEDADES_BITACORA o esa siembra no aparece en el calendario.
3. Cuando Vanessa dicta cambios semanales, Claude debe: (a) organizar los cambios en categorías — camas sacadas, ventanas actualizadas, siembras nuevas, notas — (b) presentar ese resumen para validación, y solo (c) después aplicarlos al archivo. Nunca al revés.
4. **Semanas de siembra > 26 corresponden al año 2025. Semanas ≤ 26 corresponden a 2026.** Esto es crítico para calcular fechas de cosecha correctamente — es la lógica exacta que usa el script (`semS > 26`).
5. **Nunca inventar ciclos ni ventanas de cosecha** — solo usar los que están en VARIEDADES_BITACORA o los que Vanessa confirma explícitamente en la sesión.

## El sistema en una frase

`PROGRAMACION_2026` (hoja CAMPO, llenada por Vanessa) se cruza con `VARIEDADES_BITACORA` (ciclos reales por variedad) usando la columna **N — Nombre Homologado**. Un script de Apps Script genera `EXPORT_CALENDARIO`, Erica lo descarga como CSV y lo sube a `calendario_dcb_v3.html`, que es lo que ven los clientes.

Si la columna N está vacía o el nombre no coincide EXACTAMENTE con la columna B de la BITACORA, esa siembra simplemente no aparece — sin error visible. Este es el punto de falla más común del sistema y el primero que hay que revisar cuando algo "no aparece".

## Las tres piezas del sistema

1. **PROGRAMACION_2026_v7.xlsx** — archivo maestro, vive en Google Sheets. Vanessa lo actualiza semanalmente (siembras, ventanas, notas de campo). Este es siempre el archivo activo en su versión más reciente — nunca trabajar sobre una versión vieja.
2. **DCB_CalendarioScript.gs** — Apps Script instalado dentro del archivo de programación. Lee CAMPO + VARIEDADES_BITACORA y genera la hoja EXPORT_CALENDARIO.
3. **calendario_dcb_v3.html** — herramienta web que usa Erica. Se actualiza subiendo el CSV exportado de EXPORT_CALENDARIO. No se toca desde aquí; Erica la actualiza en su computador.

## Estructura de la hoja CAMPO (lo que el script realmente lee)

| Columna | Letra | Contenido | ¿Obligatorio para el calendario? |
|---|---|---|---|
| C | 3 | Variedad (nombre en archivo, referencia) | No |
| D | 4 | Color DCB | Recomendado |
| H | 8 | Semana de siembra (número) | **Sí** |
| N | 14 | Nombre Homologado (= columna B de BITACORA) | **Sí — sin esto no aparece en el calendario** |

Regla crítica: **cada vez que se agrega una siembra nueva en CAMPO, la columna N debe llevar el Nombre Homologado exacto, tal como aparece en VARIEDADES_BITACORA columna B.** No hay margen de error de tipeo — el cruce es por coincidencia exacta de string (con `.trim()`, pero nada más de tolerancia).

Ver `references/nombres_homologados.md` para la lista completa de nombres homologados válidos por paraguas. Si Vanessa va a sembrar una variedad/color que no está en esa lista, hay que decidir el nombre nuevo con ella y confirmar que también exista (o se agregue) en VARIEDADES_BITACORA columna B — de lo contrario el cruce sigue fallando aunque N esté lleno.

## VARIEDADES_BITACORA — qué contiene

150+ variedades organizadas en 20 paraguas (Bocas de Dragón, Celosías Plumosas, Celosías Spicata, Celosías Dreams Mix, Celosías Crestadas, Gomphrenas, Campanulas, Amarantos, Zinnias, Matricaria, Statice, Trachelium, Ammi, Strawflowers, Helipterum, Dusty Miller, Lisianthus, Dianthus & Brianthus, Ammobium, Girasol, Marigold, Matilda).

Columnas relevantes:
- B — Nombre Homologado (el puente con CAMPO)
- D — Color DCB (nombre en lenguaje de cliente)
- G — Ciclo promedio (semanas desde trasplante a primera cosecha)
- I — Ventana de cosecha (semanas que dura la cosecha)
- J — Tallos por paquete
- K — Ubicación (Invernadero o Exterior)

**Regla dura: nunca inventar ni estimar un ciclo o ventana de cosecha.** Si una variedad no está en la BITACORA, revisar primero `references/ciclos_confirmados.md` (datos que Vanessa ya confirmó en sesiones anteriores fuera de la BITACORA en vivo). Si tampoco está ahí, decirlo explícitamente y preguntar — no rellenar con un número "razonable". Esto alimenta compromisos comerciales reales con wedding planners y clientes B2B. Cuando Vanessa confirme un ciclo nuevo en sesión, agregarlo a `references/ciclos_confirmados.md` para no tener que volver a preguntarlo.

**Ajuste de ciclos por época del año** (aplicar sobre el ciclo base de la BITACORA, calibrado en Mar–May):
- Sep–Nov (nuboso/lluvioso): +1 a +2 semanas
- Dic–Feb (verano/más luz): −1 semana
- Mar–May: referencia base, sin ajuste

## Cómo el script calcula las fechas (para poder verificar a mano)

Del `DCB_CalendarioScript.gs` (versión correcta, umbral `semS > 26`, NO `> 40`):

- Si semana de siembra > 26 → se asume siembra de **2025** (año calendario anterior); si ≤ 26 → **2026**. Este umbral es el que estaba mal antes y causaba errores de año — si alguna vez alguien reporta fechas corridas un año, revisar primero si el script instalado tiene `> 26` o si volvió a quedar en `> 40`.
- `semana_inicio_cosecha = semana_siembra + ciclo` (con wraparound de 52 semanas y acarreo de año)
- `semana_fin_cosecha = semana_inicio_cosecha + ventana`
- Las fechas de lunes de cada semana ISO se calculan con `semAFecha(semana, año)` — ancla en el 4 de enero de ese año.
- Solo se exportan filas cuya fecha de fin de cosecha sea >= hoy (siembras ya cerradas no aparecen).

Cuando Claude necesite calcular a mano una ventana de cosecha para responder a Vanessa (sin abrir el Sheet), replicar esta misma lógica: `semana_siembra + ciclo` = inicio, `+ ventana` = fin, usando los datos de BITACORA que Vanessa haya confirmado.

## Diagnóstico rápido: "el calendario no muestra nada" o "falta una variedad"

Orden de revisión (de más común a menos común):
1. ¿La siembra tiene algo en columna N? Si está vacía, ese es el problema.
2. ¿El texto de columna N coincide letra por letra con columna B de BITACORA? (mayúsculas, espacios, tildes cuentan)
3. ¿Esa variedad/color existe en BITACORA en absoluto? Si no, hay que agregarla ahí primero.
4. ¿La hoja BITACORA tiene sus filas de datos empezando en la fila correcta? (el script asume que los datos empiezan en la fila 4 — si alguien pegó mal el archivo y quedaron headers extra, `cicloMap` queda vacío)
5. ¿La fecha de fin de cosecha ya pasó? Si sí, es comportamiento esperado — no aparece porque ya cerró.
6. Si nada de esto explica el problema, sugerir pedirle a Erica que agregue el log de diagnóstico (`Logger.log`) descrito en la sección 7 del documento de contexto y revise "Ver → Registros de ejecución".

## Protocolo semanal (cómo arranca cada sesión de programación)

**Lunes — Vanessa dicta (con Claude, ~15 min):**
- Camas que se sacaron (marcar en gris + fecha de fin de cosecha real)
- Ventanas de cosecha que cambiaron (inicio o fin, por observación de campo)
- Siembras nuevas: variedad, semana, bloque, cantidad de plantas
- Notas de campo relevantes (problemas, observaciones)

Claude debe **organizar el dictado en categorías** (cama, cambio, dato viejo → dato nuevo) — pero no todo necesita validación previa. La regla es:

- **Cambios obvios y sin ambigüedad → aplicarlos directo**, sin pausar a preguntar. Ejemplos: una cama sacada con fecha de cierre clara; una ventana de cosecha corrida con un número exacto de semanas; una nota de campo. Vanessa no necesita confirmar lo evidente.
- **Detenerse a preguntar SOLO cuando:**
  - falta o no se puede confirmar el nombre homologado de una siembra nueva
  - el ciclo o la ventana de cosecha de una variedad no está confirmado (ni en BITACORA, ni en `references/ciclos_confirmados.md`, ni dicho explícitamente por Vanessa en la sesión)
  - la instrucción admite más de una interpretación razonable (ej. "la cama de arriba" sin decir cuál bloque, o una fecha ambigua)

Cuando Claude aplica algo directo, lo resume igual al final (qué se aplicó) para que quede trazabilidad — pero sin esperar luz verde. Cuando algo cae en la lista de "detenerse", Claude lo separa claramente del resto y pregunta puntualmente solo por eso.

Después de aplicar/confirmar, Claude genera el `PROGRAMACION_2026_vX` actualizado (siguiente número de versión) para que Vanessa lo descargue y suba a Google Sheets.

**Lunes — Erica (aparte, no es tarea de Claude pero ayuda saber el flujo):**
1. Abre PROGRAMACION_2026_vX en Google Sheets, confirma que BITACORA esté en el mismo archivo
2. Menú 🌸 DCB Calendario → Actualizar Calendario de Cosecha
3. Archivo → Descargar → CSV
4. Sube el CSV a calendario_dcb_v3.html → Actualizar datos

## Nombres homologados — exclusividades y notas comerciales a tener presentes

Algunas variedades tienen restricciones comerciales que afectan cómo se describen en el catálogo (no cómo se programan, pero vale la pena saberlo al conversar sobre disponibilidad):
- Madame Butterfly y Doubleshot: exclusivas DCB en Colombia
- Zinnias: solo para eventos, vida en florero 5–7 días
- Matilda: solo dos cultivos en Colombia la producen
- Minis de Lisianthus: exclusivas DCB en Colombia

Las descripciones completas por paraguas y color viven en `DCB_Descripciones_Catalogo.docx` — no reproducirlas de memoria, consultar ese archivo si Vanessa pide texto de catálogo.

## Reglas duras (no negociables)

- Nunca inventar datos de ciclo, ventana de cosecha o tallos/paquete. Solo BITACORA confirmada, `references/ciclos_confirmados.md`, o lo que Vanessa diga en la sesión.
- Aplicar directo los cambios obvios y sin ambigüedad (cama sacada con fecha clara, ventana corrida con número exacto, notas de campo). Detenerse a preguntar SOLO cuando falte un nombre homologado, un ciclo/ventana sin confirmar, o la instrucción admita varias interpretaciones. No pedir validación de lo evidente.
- El archivo activo es siempre la versión más reciente de PROGRAMACION_2026 — si hay ambigüedad sobre cuál es la última versión, preguntar en vez de asumir.
- Toda siembra nueva necesita nombre homologado confirmado antes de darse por registrada — si no se puede confirmar en la sesión, dejarlo marcado como pendiente explícitamente, no dejarlo en blanco silenciosamente.
