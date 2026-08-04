# Registro de tallos — DCB_Registro_Tallos (v7)

Herramienta de **Diana**. Registro de cosecha en campo. Formato nativo Google Sheets
(obligatorio: los desplegables en cascada requieren Named Ranges + INDIRECT).

## Hojas

| Hoja | Contenido | Estado |
|---|---|---|
| **REGISTRO** | Una fila por corte: Fecha · Grupo · Variedad/Serie · Tallos frescos · Tallos secos · Bloque · ¿Cierre cama? · Notas · CLAVE_LOTE (auto) | ✅ Con datos reales (~360 registros) |
| **LISTAS** | Grupos y sus opciones — alimenta los desplegables en cascada | ✅ 18 grupos |
| **RESUMEN** | Semana · Fecha · Total tallos | ⚠️ Con fórmulas (no exportables en frío) |
| **CONSOLIDADO** | Grupo · Variedad · Bloque · Frescos · Secos · Total · #Registros · Primera cosecha · Última cosecha · key_helper | ❌ **VACÍA — sin fórmulas activas** |
| **RENDIMIENTO** | Grupo · Variedad · Bloque · Fecha siembra · Total tallos · Área m² · Tallos/m² · Costo semilla · Costo insumos · Costo total · $/tallo · Ingreso estimado · Utilidad · Decisión | ❌ **VACÍA** |
| **HOMOLOGACION** | Nombre en registro → Variedad real · Serie · Bloque/Cama · Estado · Acción | ✅ 34 filas |
| **CAPACIDAD** | Huecos × líneas · 1/hueco · 2/hueco · zigzag · # camas por bloque | ✅ |

## ⚠️ El bloqueo crítico del sistema

**REGISTRO tiene datos reales de cosecha, pero CONSOLIDADO y RENDIMIENTO están vacías porque
les faltan las fórmulas.**

Consecuencia directa: **no se puede calcular rentabilidad por variedad.** Todo el objetivo de
"análisis financiero por variedad" está bloqueado por esto. La cadena rota es:

```
REGISTRO (datos reales) → CONSOLIDADO (agregación) → RENDIMIENTO (tallos/m², $/tallo, utilidad)
                              ↑ ROTO AQUÍ
```

**Esta es la tarea de mayor retorno de toda la migración.** Con la agregación funcionando,
la decisión de "sacar Campanula Lavender porque rindió 0.64 vs 0.92" pasa de ser un hallazgo
casual a ser un reporte automático de todas las variedades.

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
  **corromperán los cálculos automáticos** si no se limpian primero
- Al leer con openpyxl: la hoja CAMPO requiere `max_row` de al menos 150 para capturar todas
  las filas pobladas. No confiar solo en `extract-text` + grep
