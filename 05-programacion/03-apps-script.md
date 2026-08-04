# Apps Script — calendario de cosecha

## Versión correcta

**El cambio crítico es `semS > 26` (no `> 40`).** Esto asegura que las siembras de las semanas
27–52 se traten como año 2025.

```javascript
function generarExportCalendario() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const wsCampo = ss.getSheetByName('CAMPO');
  const wsBitacora = ss.getSheetByName('VARIEDADES_BITACORA');
  if (!wsCampo || !wsBitacora) {
    SpreadsheetApp.getUi().alert('Error: No se encontro CAMPO o VARIEDADES_BITACORA');
    return;
  }
  const bitacoraData = wsBitacora.getDataRange().getValues();
  const cicloMap = {};
  for (let i = 3; i < bitacoraData.length; i++) {   // datos desde fila 4
    const nomHom   = bitacoraData[i][1];  // col B
    const paraguas = bitacoraData[i][0];  // col A
    const colorDcb = bitacoraData[i][3];  // col D
    const ciclo    = bitacoraData[i][6];  // col G
    const ventana  = bitacoraData[i][8];  // col I
    if (nomHom && !isNaN(ciclo) && !isNaN(ventana) && ciclo > 0) {
      cicloMap[String(nomHom).trim()] = {
        ciclo: Number(ciclo), ventana: Number(ventana),
        paraguas: String(paraguas||''), colorDcb: String(colorDcb||'')
      };
    }
  }
  const campoData = wsCampo.getDataRange().getValues();
  const hoy = new Date();
  const rows = [];
  for (let i = 2; i < campoData.length; i++) {
    const variedad = campoData[i][2];   // col C
    const color    = campoData[i][3];   // col D
    const semSiem  = campoData[i][7];   // col H
    const nomHom   = campoData[i][13];  // col N
    if (!variedad || !nomHom || !semSiem) continue;
    const semS = parseInt(semSiem);
    if (isNaN(semS) || semS <= 0) continue;
    const datos = cicloMap[String(nomHom).trim()];
    if (!datos) continue;
    const { ciclo, ventana, paraguas, colorDcb } = datos;

    // CRÍTICO: semana > 26 = siembra de 2025
    const anoSiem = semS > 26 ? 2025 : 2026;
    const semIniTotal = semS + ciclo;
    const semIni = ((semIniTotal - 1) % 52) + 1;
    const anoIni = anoSiem + Math.floor((semIniTotal - 1) / 52);
    const semFinTotal = semIniTotal + ventana;
    const semFin = ((semFinTotal - 1) % 52) + 1;
    const anoFin = anoSiem + Math.floor((semFinTotal - 1) / 52);
    const fIni = semAFecha(semIni, anoIni);
    const fFin = semAFecha(semFin, anoFin);
    if (fFin < hoy) continue;

    rows.push([
      String(nomHom).trim(), paraguas,
      color || colorDcb || '',
      semS, semIni, semFin,
      Utilities.formatDate(fIni,'America/Bogota','yyyy-MM-dd'),
      Utilities.formatDate(fFin,'America/Bogota','yyyy-MM-dd'),
      'SI'
    ]);
  }
  let wsExport = ss.getSheetByName('EXPORT_CALENDARIO');
  if (!wsExport) wsExport = ss.insertSheet('EXPORT_CALENDARIO');
  else wsExport.clearContents();
  const headers = ['Nombre_Homologado','Variedad_Display','Color',
    'Sem_Siembra','Sem_Inicio_Cosecha','Sem_Fin_Cosecha',
    'Fecha_Inicio','Fecha_Fin','Activo'];
  wsExport.getRange(1,1,1,headers.length).setValues([headers]);
  wsExport.getRange(1,1,1,headers.length)
    .setBackground('#1A3A2A').setFontColor('#FFFFFF').setFontWeight('bold');
  if (rows.length > 0)
    wsExport.getRange(2,1,rows.length,headers.length).setValues(rows);
  wsExport.setFrozenRows(1);
  wsExport.autoResizeColumns(1, headers.length);
  ss.setActiveSheet(wsExport);
  SpreadsheetApp.getUi().alert(
    'Calendario actualizado\n\n' + rows.length + ' siembras procesadas\n\n' +
    'Ahora: Archivo → Descargar → CSV');
}

function semAFecha(sem, ano) {
  const jan4 = new Date(ano, 0, 4);
  const diaSemana = jan4.getDay() || 7;
  const lunes = new Date(jan4);
  lunes.setDate(jan4.getDate() - (diaSemana - 1));
  lunes.setDate(lunes.getDate() + (sem - 1) * 7);
  return lunes;
}

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('DCB Calendario')
    .addItem('Actualizar Calendario de Cosecha', 'generarExportCalendario')
    .addToUi();
}
```

## Diagnóstico — el bug de "0 siembras"

Agregar después del for loop de BITÁCORA:

```javascript
Logger.log('Variedades en cicloMap: ' + Object.keys(cicloMap).length);
Logger.log('Primera clave: ' + Object.keys(cicloMap)[0]);
```

Ver en: Ver → Registros de ejecución.

| Síntoma | Causa |
|---|---|
| `cicloMap` con 0 entradas | Cómo se pegó VARIEDADES_BITACORA — **las filas de datos no empiezan en fila 4**, o el esquema de columnas no coincide (ver la advertencia de las dos estructuras en `01-sistema-prevision-cosecha.md`) |
| `cicloMap` con entradas pero `rows = 0` | El cruce con CAMPO falla — nombres homologados que no coinciden **exactamente** (espacios, acentos, mayúsculas) |

## Observaciones para la migración a Claude Code

Tres problemas de diseño que vale la pena resolver al reescribir:

1. **`isNaN(ciclo)` acepta strings vacíos** — `isNaN('')` es `false`, así que una celda vacía
   pasa el filtro y entra como ciclo 0... salvo que `ciclo > 0` la atrape. Funciona por accidente.
2. **La regla `semS > 26 → 2025` es una heurística con fecha de caducidad.**
   Rompe en cuanto haya siembras de 2026 sem 27+ y 2027. **Lo correcto es una columna de año
   explícita en CAMPO**, o usar la fecha de siembra de la columna G que ya existe.
3. **No hay reporte de huérfanos.** Las siembras que no cruzan se descartan en silencio
   (`if (!datos) continue`). Debería registrar y mostrar cuáles no cruzaron — así el problema
   de homologación se detecta el mismo día, no tres meses después.

## Otros scripts existentes

- **`onEdit`** — desplegables en cascada de REGISTRO (ver `02-registro-de-tallos.md`)
- **Script del calendario v3** — referencias de columna corregidas + función de Diagnóstico incorporada
- **`generarEstimadoCosecha()`** — estimador de Erica. Escrita y guardada.
  Regla: solo estimados a futuro, nunca datos históricos en crudo
