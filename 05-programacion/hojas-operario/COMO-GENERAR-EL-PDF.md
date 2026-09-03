# Cómo convertir una hoja de operario a PDF

Las hojas de `05-programacion/hojas-operario/` son HTML. Para el operario se
entregan en **PDF por WhatsApp**, no como link: el artefacto de Claude es
**privado de la cuenta** y no abre desde un correo reenviado ni desde el teléfono
de un operario.

## Opción 1 — desde el navegador (la de siempre)

1. Abrir el archivo `.html` en Chrome.
2. `Ctrl + P` (o `Cmd + P` en Mac).
3. Destino: **Guardar como PDF**.
4. **Márgenes: predeterminados.** Ya vienen en el CSS (`@page{margin:11mm 13mm}`).
5. **Desmarcar "Encabezados y pies de página"** — si no, imprime la URL y la fecha.
6. Guardar.

## Opción 2 — por comando, sin abrir nada

```bash
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=DCB-Bokashi-y-Compost.pdf \
  05-programacion/hojas-operario/preparacion-camas-bokashi-y-compost.html
```

## Reglas de la hoja de impresión

Cada hoja está escrita para **caber en papel carta**, y el bloque
`@media print` del CSS es lo que lo logra:

- `@page{margin:11mm 13mm}` — márgenes de la página
- `body{font-size:10pt}` — la escala de pantalla es más grande y no cabe
- `section{page-break-inside:avoid}` — una tabla **nunca** se corta a mitad
- `.salto{page-break-before:always}` — cada pila o cada tema arranca en hoja nueva

> ⚠️ **Si se cambia el contenido de una hoja, verificar el número de páginas.**
> La primera versión de esta hoja salía en **7 páginas** porque el `@media print`
> estaba en 12pt con los paddings de pantalla. Quedó en 4 al bajar la escala.
> Verificar con:
> ```bash
> python3 -c "d=open('archivo.pdf','rb').read(); print(d.count(b'/Type /Page')-d.count(b'/Type /Pages'))"
> ```

## PDFs generados

Viven en `05-programacion/hojas-operario/pdf/`. Se regeneran cuando cambia el
HTML — no se editan a mano.
