# El desplegable de variedad en REGISTRO — arreglo definitivo

**Problema reportado (2026-09-10):** el desplegable de la columna C
(Variedad / Serie) desaparece en las filas nuevas del registro de tallos, y hay
que volver a pegar el Apps Script cada vez.

## La causa exacta, y se ve en la propia hoja

En la captura que envió Vanessa, la columna **B (Grupo) tiene desplegable hasta
la fila 731**, mientras la **columna C se corta en la 718**. Esa asimetría es el
diagnóstico completo:

| Columna | Cómo se creó su desplegable | Qué pasa con las filas nuevas |
|---|---|---|
| **B — Grupo** | Validación aplicada **una vez a toda la columna**. Vive dentro del archivo | La hereda cualquier fila nueva, para siempre |
| **C — Variedad** | La escribe el `onEdit` de Apps Script, **fila por fila**, cuando se edita B | No existe hasta que el script corra en esa fila |

Un `onEdit` es un **trigger simple**: solo corre mientras alguien edita la hoja,
solo en la fila editada, y falla en silencio. Basta con que la edición no
dispare el evento (pegado en bloque, arrastrar para rellenar, escribir desde la
app móvil, una autorización caducada, un error en cualquier punto del script) y
esa fila se queda sin desplegable **para siempre**, porque nada vuelve a pasar
por ahí.

**Por eso volver a pegar el script no lo arregla de fondo.** El script recién
pegado solo actúa sobre las ediciones que vengan *después*. Las filas que ya
quedaron huérfanas siguen huérfanas, y en la siguiente falla se repite todo.

## El arreglo: que la columna C se comporte como la B

La validación de la columna B es permanente porque es una **propiedad del
archivo**, no el resultado de un programa que tiene que correr. La columna C
puede tener exactamente eso mismo.

El obstáculo histórico está documentado en `02-registro-de-tallos.md`: la UI
nueva de validación de datos **no acepta `INDIRECT`** en el campo de rango, y
por eso se resolvió con Apps Script. Pero `INDIRECT` no es necesario: lo que se
necesita es que el rango de origen **sea un rango de verdad cuyo contenido lo
calcule una fórmula**. Eso sí funciona, porque la validación lee los *valores*
del rango, no su fórmula.

### Paso a paso — sin una línea de código

**1. Crear la hoja de apoyo.** Nueva hoja llamada `_LISTAS_PLANA`. En la celda
`A1`:

```
=SORT(UNIQUE(FILTER(FLATTEN(LISTAS!B2:S100), FLATTEN(LISTAS!B2:S100)<>"")))
```

Eso baja en una sola columna las 96 variedades de LISTAS, sin repetidos y en
orden alfabético. **Se actualiza sola**: si mañana se agrega un cultivar nuevo
en LISTAS, aparece aquí sin tocar nada. Ocultar la hoja al terminar.

> ⚠️ **Si da error, es el separador de argumentos.** La hoja está configurada en
> formato de Colombia (fechas dd/mm/aaaa), y en esa configuración las fórmulas
> separan los argumentos con **punto y coma**, no con coma. Le pasó a Vanessa el
> 2026-09-10 y se resolvió con eso. La versión que funciona en esta hoja es:
>
> ```
> =SORT(UNIQUE(FILTER(FLATTEN(LISTAS!B2:S100); FLATTEN(LISTAS!B2:S100)<>"")))
> ```
>
> Vale para cualquier fórmula que se pegue en estos archivos, no solo esta. Es
> la primera cosa que hay que revisar cuando una fórmula pegada da `#ERROR!`.

**Alternativa sin fórmula, si vuelve a fallar:** pegar la lista de variedades
como texto plano en `A1` (una por fila). Pierde la actualización automática — hay
que regenerarla cuando entre un cultivar nuevo — pero no puede dar error. La
lista se saca del repositorio con:

```bash
python3 -c "import csv;print(chr(10).join(sorted({o.strip() for f in list(csv.reader(open('07-datos/listas_desplegables.csv',encoding='utf-8')))[1:] for o in f[1:] if o.strip()}, key=str.lower)))"
```

**2. Aplicar la validación a toda la columna C de una vez.** Seleccionar
`C3:C2000` en REGISTRO → *Datos → Validación de datos → Agregar regla*:

- Criterio: **Desplegable (desde un rango)**
- Rango: `_LISTAS_PLANA!A1:A200`
- Si los datos no son válidos: **Mostrar advertencia** — nunca *Rechazar*

**El "Mostrar advertencia" es deliberado.** El campo siempre encuentra un
cultivar nuevo antes que la lista: si la hoja rechaza la entrada, Diana no puede
registrar la cosecha y el dato **se pierde**, que es mucho peor que un dato con
una esquina roja. Con advertencia se captura igual y la marca nos dice qué falta
agregar a LISTAS.

**3. Marcar en rojo las combinaciones imposibles.** Sin cascada, el desplegable
ofrece las 96 variedades sin filtrar por grupo, así que hay que poder ver de un
golpe si alguien eligió una variedad que no pertenece al grupo de la columna B.
Seleccionar `C3:C2000` → *Formato → Formato condicional → La fórmula
personalizada es*:

```
=AND($B3<>"", $C3<>"", IFERROR(COUNTIF(INDEX(LISTAS!$B$2:$S$100, MATCH($B3, LISTAS!$A$2:$A$100, 0)), $C3), 0)=0)
```

Relleno rojo suave. Se enciende cuando la variedad no está entre las opciones de
ese grupo — y también cuando el grupo mismo no existe en LISTAS.

Con esos tres pasos el desplegable **ya no depende de ningún script**: sobrevive
a filas nuevas, a pegados en bloque, a la app móvil, a que nadie autorice nada, y
a que el archivo se copie.

### El mismo arreglo, en un clic

⚠️ **Este script NO toca `_LISTAS_PLANA`.** Una versión anterior de esta ficha
la borraba y le metía la fórmula con **comas**, que en esta hoja falla por el
separador de argumentos. Si la lista de variedades se cargó como texto plano,
esa versión la habría **borrado**. El script asume que `_LISTAS_PLANA` ya existe
y usa lo que tenga, sea fórmula o texto.

```javascript
/**
 * Instala la validacion PERMANENTE de la hoja REGISTRO.
 * Correr UNA vez. Si algo se rompe, volver a correrlo.
 * NO toca _LISTAS_PLANA: usa lo que ya tenga, formula o texto pegado.
 */
function instalarDesplegablesRegistro() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const reg = ss.getSheetByName('REGISTRO');
  const listas = ss.getSheetByName('LISTAS');
  const plana = ss.getSheetByName('_LISTAS_PLANA');
  if (!reg || !listas || !plana) {
    SpreadsheetApp.getUi().alert(
      'Falta REGISTRO, LISTAS o _LISTAS_PLANA. Crear _LISTAS_PLANA primero.');
    return;
  }
  const ULTIMA = 2000;

  // Grupo (B). El rango de origen va HASTA A100, no hasta el ultimo grupo de
  // hoy: si se queda corto, los grupos nuevos de LISTAS no aparecen en el
  // desplegable y la cosecha de esos grupos no se puede registrar. Le paso
  // exactamente eso a Diana con Craspedia y Scabiosa el 2026-09-10.
  reg.getRange(3, 2, ULTIMA - 2, 1).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInRange(listas.getRange('A2:A100'), true)
      .setAllowInvalid(true)
      .setHelpText('Grupo — si falta uno, agregarlo en la hoja LISTAS')
      .build());

  // Variedad (C) desde la lista plana. Sin cascada, pero permanente: el
  // desplegable de Sheets filtra al escribir, asi que "mona" deja solo las
  // Monaco.
  reg.getRange(3, 3, ULTIMA - 2, 1).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInRange(plana.getRange('A1:A200'), true)
      .setAllowInvalid(true)
      .setHelpText('Variedad — se puede escribir una nueva; queda marcada '
                   'en rojo hasta que se agregue a LISTAS')
      .build());

  // Rojo cuando la variedad no pertenece al grupo elegido.
  const destino = reg.getRange(3, 3, ULTIMA - 2, 1);
  const regla = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied('=AND($B3<>"", $C3<>"", IFERROR(COUNTIF(INDEX('
      + 'LISTAS!$B$2:$S$100, MATCH($B3, LISTAS!$A$2:$A$100, 0)), $C3), 0)=0)')
    .setBackground('#F4C7C3')
    .setRanges([destino])
    .build();
  const otras = reg.getConditionalFormatRules().filter(function (r) {
    return !r.getRanges().some(function (x) {
      return x.getA1Notation() === destino.getA1Notation();
    });
  });
  reg.setConditionalFormatRules(otras.concat([regla]));

  SpreadsheetApp.getUi().alert(
    'Listo. Validacion permanente en B3:C' + ULTIMA + '.\n\n'
    + 'Grupo lee LISTAS!A2:A100 — hay aire para grupos nuevos.');
}
```

### Los dos rangos que hay que dejar anchos

Este es el fallo que se repitió el 2026-09-10 y conviene entenderlo, porque no
se ve: **una validación tiene dos rangos y los dos se quedan cortos.**

| Rango | Si se queda corto | Síntoma |
|---|---|---|
| **A dónde se aplica** (`B3:B2000`) | Las filas nuevas del registro nacen sin desplegable | *"Se me cortó el desplegable en la fila 718"* |
| **De dónde lee** (`LISTAS!A2:A100`) | Los grupos nuevos de LISTAS no se ofrecen | *"Agregué Craspedia a LISTAS y a Diana no le aparece"* |

El primero fue el problema original de la columna C. El segundo apareció después:
Vanessa agregó 6 grupos a LISTAS en las filas 21 a 26, y el desplegable de Grupo
seguía leyendo el rango angosto con el que se creó cuando había 19. **Los dos se
arreglan de una vez con rangos generosos** — 2000 filas de registro y 100 de
LISTAS — porque agrandarlos no cuesta nada y quedarse corto falla en silencio.

### Capa 2, opcional: la cascada como comodidad, no como cimiento

Si se quiere recuperar el filtrado por grupo, el `onEdit` puede seguir ahí —
pero ahora **encima** de la validación permanente, no en su lugar. Si el script
muere, la columna C sigue teniendo su desplegable completo y la captura no se
detiene.

```javascript
/** Estrecha la lista de C a las opciones del grupo elegido en B.
 *  Es una comodidad. Si falla, la validacion permanente sigue puesta. */
function onEdit(e) {
  const h = e.range.getSheet();
  if (h.getName() !== 'REGISTRO' || e.range.getColumn() !== 2) return;
  const fila = e.range.getRow();
  if (fila < 3) return;
  const listas = e.source.getSheetByName('LISTAS');
  const datos = listas.getRange('A2:S100').getValues();
  const grupo = String(e.value || '').trim();
  const encontrada = datos.filter(function (r) {
    return String(r[0]).trim() === grupo;
  })[0];
  if (!encontrada) return;      // grupo desconocido: se deja la lista completa
  const opciones = encontrada.slice(1).filter(String);
  if (!opciones.length) return;
  h.getRange(fila, 3).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInList(opciones, true)
      .setAllowInvalid(true)
      .build());
}
```

## La columna Bloque (F) — el mismo arreglo, y el premio es mayor

**45 formas distintas de escribir 13 lugares** en el registro de cosecha, medido
el 2026-09-10. `cerebro.py` normaliza casi todo (`Inv 4B`, `Inv4b`, `inv4b` son
lo mismo para el motor), así que el desorden **no es el argumento principal**:

| | Registros |
|---|---|
| El normalizador los resuelve bien | 650 |
| **Ambiguos: `Inv4` y `Inv3`** — no dicen qué cama | **32** |
| Combinaciones de varias camas (`3a+3b+4c`) | 10 |
| Imposibles de ubicar (`Invt`, `In4a`, `4z`) | 3 |

**El argumento real es el cruce con el área.** `capacidad_bloques.csv` tiene los
m² de cada cama. Si REGISTRO escribe los mismos nombres que ese archivo, la
cosecha se puede dividir por área y sale **tallos por m²**, que es el paso que
falta para llegar a margen por m² por semana de cama ocupada — el eje central
del proyecto. Con `Inv4` ese cruce no se puede hacer: no se sabe si fue 4A, 4B
o 4C.

Los 32 ambiguos no son un error de escritura: son **cosecha que no se puede
atribuir a una cama.**

### Instalador — escribe la lista y aplica la validación

Se escribe la lista desde el script en vez de pegarla a mano: pegar una lista
multilínea en una celda depende de cómo el navegador maneje el portapapeles, y
si cae todo en `C1` el desplegable ofrece una sola opción gigante.

```javascript
/** Bloques: escribe la lista en _LISTAS_PLANA!C y valida REGISTRO!F.
 *  Idempotente. No toca la columna A (las variedades). */
function instalarBloquesRegistro() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const reg = ss.getSheetByName('REGISTRO');
  const plana = ss.getSheetByName('_LISTAS_PLANA');
  if (!reg || !plana) {
    SpreadsheetApp.getUi().alert('Falta REGISTRO o _LISTAS_PLANA');
    return;
  }
  // Los 16 lugares de capacidad_bloques.csv, mas las 5 combinaciones que el
  // campo ya usa: a veces se corta de varias camas al mismo balde, y el
  // desplegable no debe obligar a elegir una sola y mentir.
  const BLOQUES = [
    'Inv 1', 'Inv 2', 'Inv 3A', 'Inv 3B', 'Inv 3C', 'Inv 4A', 'Inv 4B',
    'Inv 4C', 'Inv 5', 'Inv 6', 'Mini', 'Ext 3A', 'Ext 3B', 'Ext 4',
    'Ext 5', 'Exterior',
    '3A+3B+3C', '3A+3B+4C', '3B+3C', '3B+4C', '3B+3C+Mini'
  ];
  plana.getRange('C1:C40').clearContent();
  plana.getRange(1, 3, BLOQUES.length, 1)
       .setValues(BLOQUES.map(function (b) { return [b]; }));

  reg.getRange(3, 6, 1998, 1).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInRange(plana.getRange('C1:C40'), true)
      .setAllowInvalid(true)
      .setHelpText('Bloque — si aparece una cama nueva, se escribe igual')
      .build());

  SpreadsheetApp.getUi().alert(
    BLOQUES.length + ' bloques en la lista y desplegable puesto en F3:F2000');
}
```

## El segundo hallazgo: el desplegable estaba además casi vacío

Al revisar esto salió algo peor que el desplegable roto. **La hoja LISTAS de
Drive tiene 96 variedades** repartidas en hasta 19 columnas por fila — 18 bocas
de dragón, 12 lisianthus, 8 celosias. La copia del repositorio tenía **19: una
sola por grupo.**

La causa era un bug de `motor/importar_tallos.py`. El encabezado de LISTAS tiene
solo dos celdas (`GRUPO` y `OPCIONES (en orden)`) porque las opciones se
extienden a la derecha sin título por columna, y el importador **cortaba cada
fila al ancho del encabezado**. Todas las opciones menos la primera se perdían
en silencio — la misma familia de fallo que el truncamiento de filas del
2026-08-12, y con el mismo síntoma: no avisa.

Corregido el 2026-09-10: el ancho lo manda ahora la fila más ancha con datos, y
el importador reporta cuántas columnas sin título conservó.
`listas_desplegables.csv` se reconstruyó desde Drive con las 96 opciones.

### Cuatro celdas sueltas para limpiar en Drive

Dos variedades que el campo **ya está cortando** no están en LISTAS, así que el
desplegable no las ofrece: **`Cristata Enda Rose`** (Celosia, confirmada por
Vanessa el 2026-09-10 y con 2 registros de cosecha) y **`Potomac Appleblossom`**
(Boca de Dragón, 1 registro). Agregarlas a la fila de su grupo en LISTAS.

Y en la columna **S** de LISTAS hay cuatro variedades de **Statice** metidas en
filas de otros grupos, separadas del bloque por columnas vacías:

| Fila del grupo | Celda suelta en columna S |
|---|---|
| Gomphrena | `Forever Silver` |
| Campanula | `Hipster White` |
| Statice | `Hipster Apricot` (repetida — ya está en su fila) |
| Zinnia | `Ruso` |

Parece una pegada vertical de la columna de Statice que cayó desplazada. Las
cuatro están en el espejo tal como están en Drive, porque el espejo no corrige
la fuente. **Borrarlas en Drive** (cuatro clics) y volver a importar: si no, el
desplegable de Gomphrena ofrece un Statice.

## Y el arreglo de fondo, que es otro

Todo lo de arriba hace que el desplegable deje de romperse. No resuelve que
**capturar en la hoja sea incómodo**, que es la razón por la que el registro se
atrasa cuatro semanas. Ese es el rediseño de captura por voz o WhatsApp que
Vanessa planteó el 2026-09-10: la validación ya está escrita y probada en
`motor/dictar_tallos.py`; lo que falta es el transporte.

Los dos arreglos no compiten. Mientras la hoja siga siendo la fuente de verdad,
su desplegable tiene que aguantar sin mantenimiento.
