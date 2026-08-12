# Fechas de REGISTRO — limpieza y validación

Apps Script para el libro **`DCB_Registro_Tallos_v7_ORGANIZADO`**
(`14OP0GgkNmV1ty8Jz0hmASEts64ptI3y9L0i2FYsedHc`).

Resuelve dos cosas distintas y en este orden:

1. **Corregir** las 35 filas que hoy tienen la fecha mal tecleada.
2. **Impedir** que vuelva a entrar una fecha imposible.

Lo segundo es lo que de verdad importa. Corregir 35 celdas es barato; lo caro
es que la clase de error siga abierta. Un año mal tecleado no rompe nada
visiblemente — corre el ciclo, mueve la semana ISO y desplaza el calendario de
Erica sin que nadie lo note.

## Por qué hay que arreglarlo en la hoja y no solo en el repo

`motor/importar_tallos.py` ya corrige estas fechas al importar, así que **los
CSV del repositorio están correctos.** Pero la hoja es lo que ve Diana y es la
fuente de verdad para todo lo que no pasa por el motor. Mientras la hoja tenga
`2056`, cualquiera que la lea directo saca conclusiones falsas.

## ⚠️ Antes de pegar nada

Este libro **ya tiene un `onEdit`** (los desplegables en cascada de la columna
C, ver `02-registro-de-tallos.md`). Apps Script **no admite dos funciones con el
mismo nombre** en un proyecto: si pegas un `onEdit` u `onOpen` nuevo encima del
que ya existe, rompes los desplegables. Las funciones de abajo tienen nombres
propios y no colisionan. Para el menú, ver la nota al final.

## 1 · Corregir las fechas

Extensiones → Apps Script → pegar → ejecutar `corregirFechasRegistro`.

**Muestra exactamente qué va a cambiar y pide confirmación antes de escribir.**
Nada se corrige en silencio. Si lo corres dos veces, la segunda no encuentra
nada que hacer.

```javascript
/**
 * Corrige las fechas mal tecleadas de la hoja REGISTRO.
 *
 * Las tres reglas las confirmo Vanessa el 2026-08-12, contra los datos:
 *
 *  a) 33 filas del 6 al 8 de julio fechadas en 2056. Ano mal tecleado: las
 *     filas vecinas son de julio 2026 y los conteos son coherentes.
 *  b) Una fila 2026-09-19 metida entre el 18 y el 19 de junio, con la misma
 *     variedad, bloque y cantidad que la cosecha del 18/06.
 *  c) Una fila 2025-06-17 dentro de la corrida diaria de Ammobium en Inv 3A,
 *     que va del 08/06 al 26/06 de 2026 sin huecos.
 *
 * Es una limpieza de una sola vez. Pide confirmacion mostrando cada cambio,
 * asi que tampoco puede hacer dano si se corre por accidente mas adelante.
 */
function corregirFechasRegistro() {
  const COL_FECHA = 1;   // A
  const COL_GRUPO = 2;   // B
  const COL_VAR   = 3;   // C
  const COL_BLOQ  = 6;   // F
  const PRIMERA_FILA_DATOS = 3;   // 1 encabezado, 2 instrucciones

  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ws = ss.getSheetByName('REGISTRO');
  const ui = SpreadsheetApp.getUi();
  if (!ws) { ui.alert('No se encontro la hoja REGISTRO'); return; }

  const ultima = ws.getLastRow();
  if (ultima < PRIMERA_FILA_DATOS) { ui.alert('REGISTRO no tiene datos'); return; }

  const filas = ws.getRange(PRIMERA_FILA_DATOS, 1,
                            ultima - PRIMERA_FILA_DATOS + 1, COL_BLOQ).getValues();

  // Normaliza para comparar: quita espacios, acentos de mayuscula y case.
  // Asi 'Inv 3A', 'inv3a' e 'Inv3A' son la misma cosa.
  const clave = function (t) {
    return String(t || '').trim().toLowerCase().replace(/\s+/g, '');
  };

  // Reglas por CONTENIDO, no por numero de fila: siguen funcionando si la
  // hoja se reordena o se ordena por fecha.
  const reglaFila = [
    { de: '2026-09-19', a: '2026-06-19', grupo: clave('Amaranto'),
      variedad: clave('Love Lies Bleeding'), bloque: clave('Inv 3A') },
    { de: '2025-06-17', a: '2026-06-17', grupo: clave('Ammobium'),
      variedad: clave('Ammobium Alatum'),    bloque: clave('Inv 3A') },
  ];

  const iso = function (d) {
    return Utilities.formatDate(d, ss.getSpreadsheetTimeZone(), 'yyyy-MM-dd');
  };

  const cambios = [];
  for (let i = 0; i < filas.length; i++) {
    const valor = filas[i][COL_FECHA - 1];
    if (!(valor instanceof Date)) continue;

    const fila = PRIMERA_FILA_DATOS + i;
    const actual = iso(valor);
    let nueva = null;
    let motivo = '';

    if (valor.getFullYear() === 2056) {
      nueva = new Date(2026, valor.getMonth(), valor.getDate());
      motivo = 'ano 2056 -> 2026';
    } else {
      for (let r = 0; r < reglaFila.length; r++) {
        const regla = reglaFila[r];
        if (actual !== regla.de) continue;
        if (clave(filas[i][COL_GRUPO - 1]) !== regla.grupo) continue;
        if (clave(filas[i][COL_VAR - 1])   !== regla.variedad) continue;
        if (clave(filas[i][COL_BLOQ - 1])  !== regla.bloque) continue;
        const p = regla.a.split('-');
        nueva = new Date(Number(p[0]), Number(p[1]) - 1, Number(p[2]));
        motivo = 'fila fuera de su corrida diaria';
        break;
      }
    }
    if (nueva) cambios.push({ fila: fila, de: actual, a: iso(nueva), valor: nueva, motivo: motivo });
  }

  if (cambios.length === 0) {
    ui.alert('Nada que corregir\n\nNo se encontraron fechas fuera de rango en REGISTRO.');
    return;
  }

  // Resumen agrupado + las primeras filas en detalle, para poder revisar
  // antes de aceptar.
  const porMotivo = {};
  cambios.forEach(function (c) {
    const k = c.de.substring(0, 7) + ' -> ' + c.a.substring(0, 7) + '  (' + c.motivo + ')';
    porMotivo[k] = (porMotivo[k] || 0) + 1;
  });
  let msg = 'Se van a corregir ' + cambios.length + ' fechas en REGISTRO:\n\n';
  Object.keys(porMotivo).sort().forEach(function (k) {
    msg += '  ' + porMotivo[k] + ' filas   ' + k + '\n';
  });
  msg += '\nDetalle (primeras 10):\n';
  cambios.slice(0, 10).forEach(function (c) {
    msg += '  fila ' + c.fila + ':  ' + c.de + '  ->  ' + c.a + '\n';
  });
  if (cambios.length > 10) msg += '  ... y ' + (cambios.length - 10) + ' mas\n';
  msg += '\n¿Aplicar?';

  if (ui.alert('Corregir fechas de REGISTRO', msg, ui.ButtonSet.YES_NO) !== ui.Button.YES) {
    ui.alert('Cancelado. No se escribio nada.');
    return;
  }

  cambios.forEach(function (c) {
    ws.getRange(c.fila, COL_FECHA).setValue(c.valor);
    Logger.log('fila %s: %s -> %s (%s)', c.fila, c.de, c.a, c.motivo);
  });

  ui.alert('Listo\n\n' + cambios.length + ' fechas corregidas.\n\n' +
           'El detalle quedo en Registros de ejecucion.\n' +
           'Ahora conviene correr "Validar columna Fecha" para que no vuelva a pasar.');
}
```

## 2 · Impedir que vuelva a pasar

Ejecutar `validarColumnaFecha` una sola vez. Deja la columna A de REGISTRO
aceptando **solo fechas entre 2025-01-01 y 2027-12-31**, y **rechazando** lo
que esté fuera — no avisando, rechazando. Un `2056` deja de ser capturable.

El rango es deliberadamente ancho: no estorba la captura diaria y aun así
atrapa el error que importa, que es el dígito del año.

```javascript
/**
 * Pone validacion de fecha en la columna A de REGISTRO.
 *
 * setAllowInvalid(false) hace que Sheets RECHACE el valor, no que solo lo
 * marque. Es a proposito: una fecha imposible no rompe nada visible, corre el
 * ciclo y desplaza el calendario en silencio. Vale mas frenar la captura que
 * descubrirlo tres meses despues.
 */
function validarColumnaFecha() {
  const PRIMERA_FILA_DATOS = 3;
  const FILAS = 2000;   // margen sobre las ~600 actuales

  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ws = ss.getSheetByName('REGISTRO');
  const ui = SpreadsheetApp.getUi();
  if (!ws) { ui.alert('No se encontro la hoja REGISTRO'); return; }

  const regla = SpreadsheetApp.newDataValidation()
    .requireDateBetween(new Date(2025, 0, 1), new Date(2027, 11, 31))
    .setAllowInvalid(false)
    .setHelpText('Fecha de cosecha: solo entre 2025 y 2027. ' +
                 'Si Sheets la rechaza, revisa el ano antes que nada.')
    .build();

  ws.getRange(PRIMERA_FILA_DATOS, 1, FILAS, 1).setDataValidation(regla);

  ui.alert('Validacion aplicada\n\n' +
           'La columna Fecha de REGISTRO ahora solo acepta fechas entre 2025 y 2027.\n' +
           'Cubre ' + FILAS + ' filas desde la ' + PRIMERA_FILA_DATOS + '.');
}
```

## 3 · Menú (opcional)

Si el libro **no** tiene ya un `onOpen`, se puede pegar esto para tener las dos
funciones a mano. Si **sí** lo tiene, no pegues otro: agrega las dos líneas de
`addItem` dentro del `onOpen` que ya existe.

```javascript
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('DCB Datos')
    .addItem('Corregir fechas de REGISTRO', 'corregirFechasRegistro')
    .addItem('Validar columna Fecha',       'validarColumnaFecha')
    .addToUi();
}
```

## Después de correrlo

Las correcciones de `motor/importar_tallos.py` quedan inertes por sí solas: al
no encontrar coincidencias, no hacen nada. **No hay que quitarlas** — sirven de
red por si el libro se restaura desde una copia vieja, y el import da el mismo
resultado en los dos casos.

Lo que sí conviene: volver a bajar el XLSX y correr el importador, para que el
repositorio y la hoja queden idénticos también en la fuente.

```bash
python3 motor/importar_tallos.py registro.xlsx
```
