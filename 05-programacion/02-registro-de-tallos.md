# Registro de tallos — DCB_Registro_Tallos (v7)

Herramienta de **Diana**. Registro de cosecha en campo. Formato nativo Google Sheets
(obligatorio: los desplegables en cascada requieren Named Ranges + INDIRECT).

## Hojas

| Hoja | Contenido | Estado |
|---|---|---|
Verificado contra el libro el **2026-08-12**: son **6 hojas**, no 7.

| Hoja | Contenido | Estado |
|---|---|---|
| **REGISTRO** | Una fila por corte: Fecha · Grupo · Variedad/Serie · Tallos frescos · Tallos secos · Bloque · ¿Cierre cama? · Notas · CLAVE_LOTE (auto) | ✅ **696 registros** con fecha válida, hasta el **12/08/2026**. Columna `Tallos secos` **vacía en las 696 filas** |
| **LISTAS** | Grupos y sus opciones — alimenta los desplegables en cascada | ✅ **19 grupos, 96 opciones** en hasta 19 columnas por fila. El espejo tenía solo 19 (una por grupo) hasta el 2026-09-10 |
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
REGISTRO (696 filas) → CONSOLIDADO (141 lotes) → RENDIMIENTO (tallos/m², $/tallo, utilidad)
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

⚠️ **Y por eso el desplegable de la columna C se sigue rompiendo.** Un `onEdit` solo actúa
sobre la fila que se está editando, así que cada fila nueva nace sin desplegable y volver a
pegar el script no recupera las que quedaron huérfanas. `INDIRECT` no es necesario: la
validación puede leer un rango cuyo contenido lo calcule una fórmula, y eso sí es permanente.
**El arreglo definitivo, con los scripts, está en `07-desplegables-registro.md`.**

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

## Cuando Drive va atrasado: captura por dictado

`importar_tallos.py` reescribe `registro_tallos.csv` **completo** desde el XLSX
(abre el archivo en modo `w`). Cualquier fila escrita a mano en ese CSV
desaparece en la siguiente importación, y desaparece en silencio.

Por eso lo dictado no se escribe ahí. Se escribe en
`07-datos/registro_tallos_dictado.csv` — una sala de espera que sobrevive a la
importación — y `motor/dictar_tallos.py` lo valida y lo mezcla:

```bash
python3 motor/dictar_tallos.py estado    # hasta qué fecha llega el registro y qué falta
python3 motor/dictar_tallos.py validar   # revisa grupo, fecha, bloque y duplicados; no escribe
python3 motor/dictar_tallos.py aplicar   # mezcla en registro_tallos.csv, ordenado por fecha
python3 motor/dictar_tallos.py pegar     # bloque TSV listo para la hoja REGISTRO de Drive
python3 motor/dictar_tallos.py vaciar    # cierra la sala de espera cuando Drive ya lo trae
```

Lo que `validar` bloquea (marca ERROR y `aplicar` se niega a correr):

- grupo que no está en `listas_desplegables.csv` — propone el más cercano
- fecha ilegible o **futura**: una cosecha no se registra antes de cortarla
- fila sin bloque — sin bloque el dato no cruza con microclima ni con capacidad
- fila sin tallos, o cantidad no numérica

Lo que solo avisa: variedad fuera del desplegable que **ya se cosechó antes**
así (el dato real le gana al desplegable), bloque nuevo, variedad vacía.

Duplicados: la identidad de un corte es fecha + grupo + variedad + bloque +
cantidades. Lo que ya está en el registro se salta, así que `aplicar` se puede
correr dos veces sin duplicar nada.

**Drive sigue siendo la fuente de verdad.** La sala de espera es un puente, no
un segundo registro: el paso `pegar` no es opcional. Dos cosas que la mezcla
local **no** arregla: `consolidado_lotes.csv` y `resumen_tallos_dia.csv` se
calculan con fórmulas en Drive, así que no incluyen lo dictado hasta que Drive
se actualice y se vuelva a importar.
