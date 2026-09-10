# Recetas dictadas que todavía no están en Drive

`07-datos/formulas_productos_bouquets.csv` es **espejo** del archivo de recetas
de Drive. Una receta escrita a mano en el espejo desaparece en la siguiente
importación, igual que pasaba con el registro de tallos. Así que lo dictado
espera aquí hasta que entre a Drive, y esta ficha es la lista de lo que falta
subir.

Mientras una receta esté en esta ficha y no en Drive, el motor **no la ve**:
`cerebro.py cartera` reporta esas flores como `COSECHA SIN RECETA`, que es
correcto — el catálogo formal no las pide todavía.

---

## Colitas de conejo (*Lagurus ovatus*) — dictado de Vanessa 2026-09-10

Color **BEIGE** (confirmado en campo), rol TEXTURA, neutro. 1.170 plantas en
Inv 2, primera vez bajo invernadero, cosechando desde la semana 32. **400 tallos
registrados hasta el 11/08 y ninguna receta la nombra.**

| Producto | Colitas por unidad | Estado del producto |
|---|---|---|
| **Dusty con colitas** | **7** | ⚠️ **NO existe en el catálogo.** Producto nuevo: hay que crearlo con precio y composición completa |
| Arreglos secos | 1 a 3 | Los arreglos secos no están en el catálogo de 26 productos |
| **Yugo pequeño** | 1 | ✅ Existe (18 tallos, **sin precio**) |
| **Yugo grande** | 1 | ✅ Existe (21 tallos, **sin precio**) |
| Boutonnière | 1 | ⚠️ No existe en el catálogo |
| "Algunos bouquets" | 1 | Sin especificar cuáles — pendiente de precisar |

**Lo que falta para poder subirlo:**

1. La composición completa de **Dusty con colitas** — hoy solo se sabe que lleva
   7 colitas. Falta el resto de los tallos y el precio.
2. El precio de los **dos Yugos**. Son los únicos productos del catálogo sin
   precio, y además los de mayor color libre (75 % y 84 %), así que no se les
   puede calcular ni ingreso por tallo ni margen.
3. Si los **arreglos secos** y los **boutonnières** son productos de venta con
   precio o extras que se regalan. Si son de venta, entran al catálogo.

**El excedente no es sobrante:** Vanessa lo guarda seco para las coronas de
Navidad. O sea que la producción de colitas tiene dos destinos y el segundo es
inventario, no descarte — eso cambia cómo se lee un "SOBRA" en la cartera.

---

## Espárrago — dictado de Vanessa 2026-09-10

Ya está en las recetas de Drive (2 productos, 1 tallo cada uno) y ya resuelve en
la paleta, así que **no está pendiente de subir**. Queda anotado aquí porque su
dato de siembra sí falta:

- Es el **único follaje propio** del catálogo. Todo el demás follaje se compra
  (Ruscus), así que cada tallo de espárrago propio **desplaza una compra** — su
  valor no es el precio del tallo, es el costo que evita.
- Sembrado de semilla, ensayo en **Bloque 2**, **~30 plantas** aproximadas.
- Ciclo **15 semanas, estimado por Vanessa, no medido.** No tiene fila en
  `campo_siembras.csv`, así que no hay fecha de siembra contra la que verificar.
  Primer corte 2026-08-10 (sem 33): con ciclo 15 la siembra caería cerca de la
  semana 18. **Por confirmar.**
- La intención es sembrar más.
