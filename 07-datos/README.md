# Datos vivos — CSV exportados de los Excel maestros

Exportados el **30 de julio de 2026** desde:
- `PROGRAMACION_2026_v7_ACTUALIZADO.xlsx`
- `DCB_Registro_Tallos_v7_ORGANIZADO.xlsx`
- `DCB_Maestro_Campo_2026.xlsx`

## Inventario

| Archivo | Filas | Fuente | Estado |
|---|---|---|---|
| `campo_siembras.csv` | 302 | PROGRAMACION → CAMPO | ✅ El registro maestro de siembras |
| `variedades_bitacora.csv` | 78 | PROGRAMACION → VARIEDADES_BITACORA | ✅ Ciclos reales + decisión por variedad |
| `variedades_parametros_siembra.csv` | 55 | PROGRAMACION → VARIEDADES | ✅ Germinación, distancia, net, pinch, tallos/planta |
| `formulas_productos_bouquets.csv` | 126 | PROGRAMACION → FORMULAS_PRODUCTOS | ✅ Composición y precio de bouquets |
| `finca_entregas_plantulas.csv` | 19 | PROGRAMACION → FINCA | ✅ Entregas de proveedor |
| `registro_tallos.csv` | 362 | REGISTRO_TALLOS → REGISTRO | ✅ Cosecha real diaria |
| `homologacion_registro.csv` | 34 | REGISTRO_TALLOS → HOMOLOGACION | ✅ Puente nombre-de-corte → variedad real |
| `capacidad_bloques.csv` | 18 | REGISTRO_TALLOS → CAPACIDAD | ✅ |
| `listas_desplegables.csv` | 18 grupos | REGISTRO_TALLOS → LISTAS | ✅ |
| `aplicaciones_historial.csv` | 16 | MAESTRO_CAMPO → APLICACIONES | ⚠️ Solo semana 27 — **actualizar** |
| `decisiones_manejo.csv` | 2 | MAESTRO_CAMPO → DECISIONES | ⚠️ Apenas iniciada |
| `consolidado_lotes.csv` | **0** | REGISTRO_TALLOS → CONSOLIDADO | ❌ **Sin fórmulas — bloquea rentabilidad** |
| `rendimiento_costo_lote.csv` | **0** | REGISTRO_TALLOS → RENDIMIENTO | ❌ **Vacía** |
| `costos_productos.csv` | **0** | MAESTRO_CAMPO → COSTOS_PRODUCTOS | ❌ **Vacía — bloquea costo por aplicación** |
| `problemas_fisiologicos_variedad.csv` | 4 | Vanessa 2026-08-27, ficha Boca de Dragon | ✅ Desordenes nutricionales/fisiologicos — distinto de plagas y hongos |
| `costos_follaje_comprado.csv` | 6 | Factura FH 2743 + dictado de Vanessa | ✅ **Primer costo real del repo** — con y sin IVA, y estado de compra por ítem |
| `resumen_tallos_dia.csv` | 4 | REGISTRO_TALLOS → RESUMEN | ⚠️ Hoja con fórmulas — export incompleto |

## Advertencias de lectura

- Los CSV son un **snapshot**, no la fuente de verdad viva. Los Excel siguen en Google Sheets.
  Una de las metas de la migración es invertir esto: que el repositorio sea la fuente y los
  Sheets el reflejo.
- Las hojas con fórmulas (RESUMEN, CONSOLIDADO, RENDIMIENTO) exportan vacías o incompletas
  porque el export lee valores en caché. **Vacío aquí no siempre significa vacío allá** —
  pero en el caso de CONSOLIDADO y RENDIMIENTO sí: se confirmó que no tienen fórmulas.
- `campo_siembras.csv` tiene 302 filas contra las 306 siembras activas reportadas.
  La diferencia son filas sin variedad en columna C (filtradas en el export). Verificar.
- Fechas normalizadas a `YYYY-MM-DD`. Hay inconsistencias de formato en el origen que
  **corromperán cálculos automáticos si no se limpian primero.**
- Nombres de variedad inconsistentes entre las tres fuentes. `homologacion_registro.csv` resuelve
  parte del problema, pero no todo.

## Falta traer

- **`DCB_Fitosanidad_Maestro.xlsx`** — 8 hojas (INSUMOS, BUSCAR, ROTACION, REGISTRO, CONSUMO,
  INVENTARIO, GASTO_MENSUAL). No está en el proyecto. **Es la pieza más importante que falta.**
- `DCB_Modelo_Costos.xlsx` y `Calculo_por_tallo.xlsx`
- Análisis de suelo de Inv 3B e Inv 4 (cuando lleguen)
- Google Sheet de registro de Diana en su versión más reciente (el CSV aquí puede estar atrás)
