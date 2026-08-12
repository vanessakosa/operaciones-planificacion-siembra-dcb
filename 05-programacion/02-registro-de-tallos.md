# Registro de tallos — DCB_Registro_Tallos (v7)

Herramienta de **Diana**. Registro de cosecha en campo. Formato nativo Google Sheets
(obligatorio: los desplegables en cascada requieren Named Ranges + INDIRECT).

## Hojas

| Hoja | Contenido | Estado |
|---|---|---|
Verificado contra el libro el **2026-08-12**: son **6 hojas**, no 7.

| Hoja | Contenido | Estado |
|---|---|---|
| **REGISTRO** | Una fila por corte: Fecha · Grupo · Variedad/Serie · Tallos frescos · Tallos secos · Bloque · ¿Cierre cama? · Notas · CLAVE_LOTE (auto) | ✅ **596 registros** con fecha válida, hasta el 31/07/2026 |
| **LISTAS** | Grupos y sus opciones — alimenta los desplegables en cascada | ✅ 18 grupos |
| **RESUMEN** | Semana · Fecha · Total tallos | ⚠️ Con fórmulas. Solo 4 filas: se quedó en la semana 22 |
| **CONSOLIDADO** | Grupo · Variedad · Bloque · Frescos · Secos · Total · #Registros · Primera cosecha · Última cosecha · key_helper | ✅ **141 lotes — sí se calcula solo** |
| **RENDIMIENTO** | Grupo · Variedad · Bloque · Fecha siembra · Total tallos · Área m² · Tallos/m² · Costo semilla · Costo insumos · Costo total · $/tallo · Ingreso estimado · Utilidad · Decisión | ❌ **VACÍA — faltan los datos, no las fórmulas** |
| **HOMOLOGACION** | Nombre en registro → Variedad real · Serie · Bloque/Cama · Estado · Acción | ✅ 34 filas |

**No existe hoja `CAPACIDAD`** en este libro. La capacidad por bloque vive en
`07-datos/capacidad_bloques.csv`.

## ⚠️ Dónde está el bloqueo de verdad

Este documento decía antes que CONSOLIDADO estaba vacía por falta de fórmulas, y que ése era
el eslabón roto. **No es así** — se verificó el 2026-08-12: CONSOLIDADO agrega correctamente
sus 141 lotes en Drive. Lo que pasaba es que nunca se había **espejado** al repositorio
(`consolidado_lotes.csv` estaba con solo el encabezado). Ya está resuelto con
`motor/importar_tallos.py`.

La cadena real es:

```
REGISTRO (596 filas) → CONSOLIDADO (141 lotes) → RENDIMIENTO (tallos/m², $/tallo, utilidad)
      ✅ ok                   ✅ ok                        ↑ ROTO AQUÍ
```

**RENDIMIENTO no necesita fórmulas: necesita datos que nadie ha medido.** Sus columnas de
entrada son `Área m²`, `Costo semilla $` y `Costo insumos $`, y las tres están vacías en la
fuente. Sin ellas no hay `$/tallo` ni utilidad, y por lo tanto no hay **margen por m² por
semana de cama ocupada** — el eje que el `CLAUDE.md` define como la unidad que une calidad,
rentabilidad y uso de recursos.

Es el mismo bloqueo que `07-datos/costos_productos.csv`. Se cierran juntos o no se cierra
ninguno.

## Desplegables en cascada

Un handler `onEdit` de Apps Script pobla la columna C (variedad/serie) según el grupo elegido
en la columna B, usando la hoja LISTAS.

**Causa raíz del fallo histórico:** la nueva UI de validación de datos de Google Sheets
**no acepta fórmulas INDIRECT directamente en el campo de rango**. Por eso se resolvió con
Apps Script en lugar de validación nativa.

## Nombres a homologar

La hoja HOMOLOGACION resuelve el problema de que Diana registra "Snapdragon / Fucsia" cuando la
variedad real es "Snapdragon Monaco Dark Pink". Cada fila incluye además el estado del lote
(CERRADA / EN PICO / ACTIVA / ÚLTIMOS TALLOS) y la acción para el cortador
("No cosechar más" / "Cosechar todos los días").

> **Oportunidad:** esta hoja es esencialmente una orden de corte diaria generada a partir del
> estado del lote. Se puede automatizar cruzando CAMPO (ventanas) con REGISTRO (cosecha real).

## Reglas de datos

- **A Erica nunca se le muestran datos históricos de cosecha en crudo** — solo estimados
  de cantidad de tallos a futuro, calculados a partir de ellos
- Errores de formato de fecha e inconsistencias de nombres de variedad entre las tres hojas
  **corromperán los cálculos automáticos** si no se limpian primero. Ya pasó: 35 filas con el
  año mal tecleado (33 en `2056`). El importador las corrige, y
  `05-validacion-fechas-registro.md` tiene el Apps Script para arreglarlas en la hoja y poner
  validación de rango en la columna Fecha para que no vuelva a entrar ninguna
- Al leer con openpyxl: la hoja CAMPO requiere `max_row` de al menos 150 para capturar todas
  las filas pobladas. No confiar solo en `extract-text` + grep
