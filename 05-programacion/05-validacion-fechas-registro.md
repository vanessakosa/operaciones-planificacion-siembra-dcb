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

## ⚠️ Nada de ventanas de confirmación

**Estas funciones no usan `SpreadsheetApp.getUi().alert()` a propósito.**

La primera versión sí lo hacía y falló en la práctica del modo más confuso
posible: `alert()` abre la ventana **en la pestaña de la hoja de cálculo**, no
en la del editor de Apps Script. Ejecutándolo desde el editor, la ventana se
abre sola en la otra pestaña y el script **se queda bloqueado esperando una
respuesta que nadie ve**, hasta que a los 30 minutos Apps Script lo mata con
`Exceeded maximum execution time`. Parece que el script se colgó calculando y
en realidad estaba esperando un clic.

En vez de eso, la confirmación es un **paso separado**: primero corres una
función que solo mira y reporta, lees el resultado en **Registro de ejecución**,
y solo entonces corres la que escribe. Mismo control, sin bloqueo.

## ⚠️ Antes de pegar nada

Este libro **ya tiene un `onEdit`** (los desplegables en cascada de la columna
C, ver `02-registro-de-tallos.md`). Apps Script **no admite dos funciones con el
mismo nombre** en un proyecto: si pegas un `onEdit` u `onOpen` nuevo encima del
que ya existe, gana el de abajo y el de arriba se apaga en silencio, sin dar
error. Conviene pegar esto en un **archivo `.gs` aparte** — todas las funciones
del proyecto se ven entre sí, así que funcionan igual y no se toca nada de lo
que ya existe.

## El código

```javascript
/**
 * Analiza la columna Fecha de REGISTRO y devuelve la lista de correcciones.
 * NO escribe nada. La usan las dos funciones de abajo.
 *
 * Las tres reglas las confirmo Vanessa el 2026-08-12, contra los datos:
 *
 *  a) 33 filas del 6 al 8 de julio fechadas en 2056. Ano mal tecleado: las
 *     filas vecinas son de julio 2026 y los conteos son coherentes.
 *  b) Una fila 2026-09-19 metida entre el 18 y el 19 de junio, con la misma
 *     variedad, bloque y cantidad que la cosecha del 18/06.
 *  c) Una fila 2025-06-17 dentro de la corrida diaria de Ammobium en Inv 3A,
 *     que va del 08/06 al 26/06 de 2026 sin huecos.
 */
function _analizarFechasRegistro() {
  const COL_FECHA = 1;   // A
  const COL_GRUPO = 2;   // B
  const COL_VAR   = 3;   // C
  const COL_BLOQ  = 6;   // F
  const PRIMERA_FILA_DATOS = 3;   // 1 encabezado, 2 instrucciones

  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const ws = ss.getSheetByName('REGISTRO');
  if (!ws) { Logger.log('ERROR: no existe la hoja REGISTRO'); return null; }

  const ultima = ws.getLastRow();
  if (ultima < PRIMERA_FILA_DATOS) { Logger.log('REGISTRO no tiene datos'); return null; }

  const filas = ws.getRange(PRIMERA_FILA_DATOS, 1,
                            ultima - PRIMERA_FILA_DATOS + 1, COL_BLOQ).getValues();

  // Normaliza para comparar: quita espacios y case.
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
      variedad: clave('Ammobium Alatum'),    bloque: clave('Inv 3A') }
  ];

  // Mes mal tecleado: 64 filas de septiembre 2026 que en realidad son de
  // agosto (confirmado por Vanessa el 2026-08-13). Con el mes corregido la
  // corrida queda continua y los dos unicos dias sin cosecha son los dos
  // sabados.
  //
  // EL CANDADO: solo se aplica si la fecha TODAVIA NO OCURRIO. Una cosecha no
  // se registra en el futuro, asi que una fecha futura es por definicion un
  // error de captura. Cuando septiembre llegue de verdad, la regla deja de
  // dispararse sola y los registros legitimos pasan intactos. Por eso no hace
  // falta acordarse de quitarla.
  const CORRIGE_MES_SI_FUTURA = { '2026-09': 8 };

  const finDeHoy = new Date();
  finDeHoy.setHours(23, 59, 59, 999);

  const tz = ss.getSpreadsheetTimeZone();
  const iso = function (d) { return Utilities.formatDate(d, tz, 'yyyy-MM-dd'); };

  const cambios = [];
  for (let i = 0; i < filas.length; i++) {
    const valor = filas[i][COL_FECHA - 1];
    if (!(valor instanceof Date)) continue;

    const actual = iso(valor);
    const mesNuevo = CORRIGE_MES_SI_FUTURA[actual.substring(0, 7)];
    let nueva = null;
    let motivo = '';

    if (valor.getFullYear() === 2056) {
      nueva = new Date(2026, valor.getMonth(), valor.getDate());
      motivo = 'ano 2056 -> 2026';
    } else if (mesNuevo !== undefined && valor > finDeHoy) {
      nueva = new Date(valor.getFullYear(), mesNuevo - 1, valor.getDate());
      motivo = 'mes futuro -> mes correcto';
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

    if (nueva) {
      cambios.push({ fila: PRIMERA_FILA_DATOS + i, de: actual, a: iso(nueva),
                     valor: nueva, motivo: motivo });
    }
  }

  return { ws: ws, colFecha: COL_FECHA, leidas: filas.length, cambios: cambios };
}


/**
 * PASO 1 — solo mira y reporta. No escribe ni una celda.
 * El resultado sale en Ver > Registro de ejecucion.
 */
function revisarFechasRegistro() {
  const r = _analizarFechasRegistro();
  if (!r) return;

  Logger.log('=== REVISION — no se escribe nada ===');
  Logger.log('Filas leidas en REGISTRO: %s', r.leidas);
  Logger.log('Fechas a corregir: %s', r.cambios.length);

  if (r.cambios.length === 0) {
    Logger.log('Nada que corregir. La columna Fecha esta limpia.');
    return;
  }

  const porMotivo = {};
  r.cambios.forEach(function (c) {
    const k = c.de.substring(0, 7) + ' -> ' + c.a.substring(0, 7) + '  (' + c.motivo + ')';
    porMotivo[k] = (porMotivo[k] || 0) + 1;
  });
  Logger.log('--- resumen ---');
  Object.keys(porMotivo).sort().forEach(function (k) {
    Logger.log('  %s filas   %s', porMotivo[k], k);
  });

  Logger.log('--- detalle fila por fila ---');
  r.cambios.forEach(function (c) {
    Logger.log('  fila %s:  %s  ->  %s', c.fila, c.de, c.a);
  });

  Logger.log('Si el resumen cuadra, corre aplicarCorreccionFechas.');
}


/**
 * PASO 2 — escribe las correcciones. Correr solo despues de revisar.
 * Es idempotente: la segunda vez no encuentra nada que hacer.
 */
function aplicarCorreccionFechas() {
  const r = _analizarFechasRegistro();
  if (!r) return;

  if (r.cambios.length === 0) {
    Logger.log('Nada que corregir. No se escribio nada.');
    return;
  }

  r.cambios.forEach(function (c) {
    r.ws.getRange(c.fila, r.colFecha).setValue(c.valor);
    Logger.log('fila %s: %s -> %s (%s)', c.fila, c.de, c.a, c.motivo);
  });

  Logger.log('=== LISTO — %s fechas corregidas ===', r.cambios.length);
  Logger.log('Ahora corre validarColumnaFecha para que no vuelva a pasar.');
}


/**
 * PASO 3 — pone validacion de fecha en la columna A de REGISTRO.
 *
 * NO SE USA requireDateBetween con un rango de anos. Esa fue la primera
 * version y se quedo corta: acepta cualquier fecha entre 2025 y 2027, asi que
 * cierra el digito del ANO pero no el del MES. El 2026-08-13 entraron 64 filas
 * fechadas en septiembre — un mes en el futuro — y la regla las dejo pasar sin
 * chistar.
 *
 * La regla correcta es semantica, no de rango: UNA COSECHA NO SE PUEDE
 * REGISTRAR EN EL FUTURO. Con formula personalizada y HOY(), que se recalcula
 * solo, la validacion se mueve con el calendario sin mantenimiento.
 *
 * setAllowInvalid(false) hace que Sheets RECHACE el valor, no que solo lo
 * marque. Es a proposito: una fecha imposible no rompe nada visible, corre el
 * ciclo y desplaza el calendario en silencio. Vale mas frenar la captura en el
 * momento — cuando Diana todavia recuerda que dia cosecho — que descubrirlo
 * tres meses despues.
 */
function validarColumnaFecha() {
  const PRIMERA_FILA_DATOS = 3;
  const FILAS = 2000;   // margen sobre las ~700 actuales

  const ws = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('REGISTRO');
  if (!ws) { Logger.log('ERROR: no existe la hoja REGISTRO'); return; }

  const rango = ws.getRange(PRIMERA_FILA_DATOS, 1, FILAS, 1);

  // La formula se escribe relativa a la PRIMERA celda del rango; Sheets la
  // ajusta fila por fila sola.
  const formula = '=Y(A' + PRIMERA_FILA_DATOS + '>=FECHA(2025;1;1); ' +
                  'A' + PRIMERA_FILA_DATOS + '<=HOY())';

  const regla = SpreadsheetApp.newDataValidation()
    .requireFormulaSatisfied(formula)
    .setAllowInvalid(false)
    .setHelpText('Fecha de cosecha: no puede ser futura ni anterior a 2025. ' +
                 'Si Sheets la rechaza, revisa el mes y el ano.')
    .build();

  rango.setDataValidation(regla);

  Logger.log('=== LISTO — validacion aplicada ===');
  Logger.log('Columna Fecha de REGISTRO: no se aceptan fechas futuras.');
  Logger.log('Formula: %s', formula);
  Logger.log('Cubre %s filas desde la %s.', FILAS, PRIMERA_FILA_DATOS);
}
```

## Cómo correrlo

Extensiones → Apps Script. Pegar en un archivo `.gs` **nuevo**, guardar
(`Ctrl+S`), y ejecutar **en este orden**, eligiendo cada función en el
desplegable de arriba:

| # | Función | Qué hace | Qué esperar |
|---|---|---|---|
| 1 | `revisarFechasRegistro` | Solo mira | En Registro de ejecución: `Fechas a corregir: 35` |
| 2 | `aplicarCorreccionFechas` | Escribe | `LISTO — 35 fechas corregidas` |
| 3 | `validarColumnaFecha` | Pone la regla | `LISTO — validacion aplicada` |

**Entre el paso 1 y el 2, lee el resumen.** Debe decir 33 filas de `2056-07`,
1 de `2026-09` y 1 de `2025-06`. Si dice otra cosa, no sigas: significa que la
hoja cambió desde que se verificaron las reglas.

La primera ejecución pide autorización — *Revisar permisos* → elegir cuenta →
*Configuración avanzada* → *Ir a … (no seguro)* → *Permitir*. Esa advertencia
sale con cualquier script propio sin verificar comercialmente; es genérica, no
un diagnóstico.

## Comprobar que quedó

- En REGISTRO, ordenar por Fecha de mayor a menor: la más alta debe ser
  **31/07/2026**. Si aparece un 2056, el paso 2 no corrió.
- Escribir `06/07/2056` en una celda vacía de la columna Fecha: **Sheets debe
  rechazarlo**. Si lo acepta, el paso 3 no corrió.

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
