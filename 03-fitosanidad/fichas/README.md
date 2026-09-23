# Fichas técnicas

El PDF (o foto) de cada ficha técnica va aquí, con el nombre del producto tal como
está en `07-datos/productos.csv`: `Equifun.pdf`, `Safer-Mix-WP.pdf`.

Cuando una ficha entra, se pasan sus datos a `productos.csv` (dosis de etiqueta,
intervalo, carencia, reingreso, restricciones), sus ingredientes a
`producto_ingredientes.csv` y sus compatibilidades a `compatibilidad.csv`, y
`ficha_estado` pasa a `CONFIRMADA`. Con eso ya puede entrar a una formulación
(regla 3 de `CLAUDE.md`).
