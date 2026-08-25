# Espejo automático — leer PROGRAMACION_2026 sin tocar nada

## El problema, medido

Claude no puede leer `PROGRAMACION_2026_v8_ACTUALIZADO.xlsx` (12,2 MB) desde el
conector de Google Drive. Dos fallas distintas, ambas reproducidas el 2026-08-25:

| Intento | Resultado |
|---|---|
| `download_file_content` | `File too large for download, over limit of 10 MB` |
| `read_file_content` | 241.054 caracteres — **truncado, sin aviso** |

**El techo de 10 MB es del conector, no de Google Drive.** La API de Drive no lo
tiene. Pero la política de red de este entorno bloquea `googleapis.com`:

```
gateway answered 403 to CONNECT (policy denial)
  host: oauth2.googleapis.com:443
  host: www.googleapis.com:443
```

Así que la service account `salesmachinebot@dcb-sales-machine` que está en las
variables de entorno no sirve desde aquí: no falla por permisos, no puede ni
marcar.

**La salida es invertir la dirección.** En vez de que Claude vaya a buscar el
archivo grande, Google empuja pedazos chicos a una carpeta que Claude sí lee.
Eso corre del lado de Google, en un disparador de tiempo, sin que nadie haga
clic.

## Por qué no sirve el script que ya existe

`generarExportCalendario` (ver `03-apps-script.md`) termina en:

```javascript
SpreadsheetApp.getUi().alert('... Ahora: Archivo → Descargar → CSV');
```

`getUi()` **lanza excepción cuando el script corre desde un disparador de
tiempo** — solo funciona con un humano haciendo clic en el menú. Y el paso final
es una descarga manual. El script de abajo no usa `getUi()` en ningún lado.

## Qué hace el espejo

Cada vez que corre, por cada archivo fuente:

1. Si la fuente es `.xlsx`, saca una **copia convertida a Google Sheet** (la API
   de Drive convierte al copiar). Lee siempre la versión actual del `.xlsx` — si
   Vanessa sube una versión nueva, el espejo la toma en la siguiente corrida.
2. Exporta cada hoja pedida como un CSV independiente.
3. **Sobrescribe el contenido del CSV anterior en vez de crear uno nuevo**, para
   que el ID de Drive no cambie nunca. Eso es lo que permite que Claude tenga los
   IDs fijos y no tenga que buscar el archivo cada sesión.
4. Borra la copia temporal.
5. Escribe `_ESPEJO_ESTADO.csv` con la fecha de la corrida y las filas exportadas
   por hoja.

`_ESPEJO_ESTADO.csv` no es decorativo: es lo que deja ver **si el espejo dejó de
correr**. Sin él, un CSV viejo se lee igual que uno fresco, y la regla
APLICACIONES pasaría a apoyarse en datos muertos sin que nadie se entere.

## El script

Proyecto **standalone** en [script.google.com](https://script.google.com) — no
va pegado al `.xlsx` (un `.xlsx` no acepta Apps Script; por eso este script vive
aparte y trabaja sobre una copia convertida).

```javascript
/**
 * Espejo automático DCB — exporta hojas de los libros maestros a CSV
 * en una carpeta de Drive, para que Claude las lea sin topar el
 * límite de 10 MB del conector.
 *
 * Corre desde un disparador de tiempo. NO usa getUi().
 */

const CONFIG = {
  // Carpeta donde quedan los CSV. Crear en Drive y pegar el ID de la URL.
  CARPETA_DESTINO_ID: 'PEGAR_ID_DE_LA_CARPETA',

  FUENTES: [
    {
      etiqueta: 'PROGRAMACION_2026',
      fileId: '1NaGlBEY5j-e-rLx_7NvdIWWPWCiGxv0x',
      esXlsx: true,
      hojas: ['CAMPO', 'VARIEDADES_BITACORA', 'EXPORT_CALENDARIO'],
    },
    // Cuando aparezca el libro que contiene APLICACIONES, agregarlo aquí.
    // Si ya es Google Sheet nativo, poner esXlsx: false.
    // {
    //   etiqueta: 'MAESTRO_CAMPO',
    //   fileId: 'PEGAR_ID',
    //   esXlsx: true,
    //   hojas: ['APLICACIONES', 'INVENTARIO'],
    // },
  ],
};

function espejarTodo() {
  const carpeta = DriveApp.getFolderById(CONFIG.CARPETA_DESTINO_ID);
  const estado = [['archivo_fuente', 'hoja', 'csv', 'filas', 'estado']];
  const corridaTs = Utilities.formatDate(
    new Date(), 'America/Bogota', 'yyyy-MM-dd HH:mm');

  CONFIG.FUENTES.forEach(function (fuente) {
    let idParaLeer = fuente.fileId;
    let temporal = null;

    try {
      if (fuente.esXlsx) {
        temporal = convertirASheet_(fuente.fileId, fuente.etiqueta);
        idParaLeer = temporal;
      }
      const ss = SpreadsheetApp.openById(idParaLeer);

      fuente.hojas.forEach(function (nombreHoja) {
        const hoja = ss.getSheetByName(nombreHoja);
        const nombreCsv = fuente.etiqueta + '__' + nombreHoja + '.csv';

        if (!hoja) {
          estado.push([fuente.etiqueta, nombreHoja, nombreCsv, 0,
                       'HOJA_NO_ENCONTRADA']);
          return;
        }
        const datos = hoja.getDataRange().getValues();
        escribirCsv_(carpeta, nombreCsv, aCsv_(datos));
        estado.push([fuente.etiqueta, nombreHoja, nombreCsv,
                     Math.max(0, datos.length - 1), 'OK']);
      });
    } catch (e) {
      estado.push([fuente.etiqueta, '—', '—', 0, 'ERROR: ' + e.message]);
    } finally {
      if (temporal) {
        try { DriveApp.getFileById(temporal).setTrashed(true); } catch (e) {}
      }
    }
  });

  estado.push(['_corrida', corridaTs, '—', '—', '—']);
  escribirCsv_(carpeta, '_ESPEJO_ESTADO.csv', aCsv_(estado));
}

/** Copia un .xlsx convirtiéndolo a Google Sheet. Devuelve el ID de la copia. */
function convertirASheet_(fileId, etiqueta) {
  const url = 'https://www.googleapis.com/drive/v3/files/' + fileId +
              '/copy?supportsAllDrives=true&fields=id';
  const res = UrlFetchApp.fetch(url, {
    method: 'post',
    contentType: 'application/json',
    headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() },
    payload: JSON.stringify({
      name: '_tmp_espejo_' + etiqueta,
      mimeType: 'application/vnd.google-apps.spreadsheet',
    }),
    muteHttpExceptions: true,
  });
  if (res.getResponseCode() >= 300) {
    throw new Error('conversion fallo (' + res.getResponseCode() + '): ' +
                    res.getContentText().slice(0, 200));
  }
  return JSON.parse(res.getContentText()).id;
}

/** Sobrescribe el CSV si ya existe, para conservar el ID de Drive. */
function escribirCsv_(carpeta, nombre, contenido) {
  const existentes = carpeta.getFilesByName(nombre);
  if (existentes.hasNext()) {
    existentes.next().setContent(contenido);
  } else {
    carpeta.createFile(nombre, contenido, MimeType.CSV);
  }
}

function aCsv_(filas) {
  return filas.map(function (fila) {
    return fila.map(function (celda) {
      const s = (celda === null || celda === undefined) ? '' : String(celda);
      return /[",\n\r]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
    }).join(',');
  }).join('\n');
}

/** Correr UNA vez a mano para crear el disparador diario. */
function instalarDisparador() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'espejarTodo') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('espejarTodo').timeBased().everyDays(1).atHour(5).create();
}
```

En `appsscript.json` (Configuración → mostrar archivo de manifiesto):

```json
{
  "timeZone": "America/Bogota",
  "oauthScopes": [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/script.external_request",
    "https://www.googleapis.com/auth/script.scriptapp"
  ]
}
```

## Puesta en marcha — una sola vez

Automatizar algo siempre cuesta un montaje inicial. Lo que no vuelve a pasar es
el trabajo recurrente: después de estos pasos, nadie toca nada nunca más.

1. Crear una carpeta en Drive (ej. `DCB Claude / 07_Operaciones / _espejo`) y
   copiar su ID de la URL.
2. `script.google.com` → Nuevo proyecto → pegar el script.
3. Pegar el ID de la carpeta en `CARPETA_DESTINO_ID`.
4. Ejecutar `espejarTodo` una vez a mano y autorizar los permisos.
5. Ejecutar `instalarDisparador` una vez. Listo — corre solo cada día a las 5am.
6. Pasarle a Claude los IDs de los CSV generados, para fijarlos en `CLAUDE.md`.

## Lo que esto no resuelve

`APLICACIONES` **no está dentro de `PROGRAMACION_2026`**. Verificado: `Neofat`
—producto que sí aparece en `aplicaciones_historial.csv`— no da resultado al
buscar por contenido dentro de ese libro. Las dos veces que aparece la palabra
"APLICACIONES" en el texto extraído son el sustantivo común ("Máx 2
aplicaciones seguidas"), dentro de un catálogo de productos.

El repositorio nombra ese libro de tres maneras y **ninguna existe en el Drive
de `contact@dreamscanbloom.com`**:

| Dónde | Nombre que usa |
|---|---|
| `07-datos/README.md` | `MAESTRO_CAMPO → APLICACIONES` |
| skill `dcb-fitosanidad` | hoja de `DCB_Maestro_Campo_2026.xlsx` |
| `CLAUDE.md` Nivel 0 | `DCB_Fitosanidad_Maestro.xlsx` (8 hojas) |

Hasta que aparezca ese libro, la regla APLICACIONES sigue bloqueada — y no por
el tamaño de `PROGRAMACION_2026`. Son dos problemas separados. El espejo resuelve
el primero; el segundo necesita ubicar el archivo.
