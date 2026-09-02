# Comparativo de casas comerciales — fertirriego

> **Estado: MESA DE TRABAJO ABIERTA.** Faltan (a) precios actualizados de Haifa, (b) fichas
> técnicas y precios de la casa nueva. Las composiciones de Haifa de abajo son **de catálogo y
> están marcadas PENDIENTE CONFIRMAR contra la ficha/etiqueta del lote comprado** — Regla 3:
> ningún producto entra a formulación sin ficha confirmada.

## Los productos Haifa que están en uso hoy

| Producto | Composición de catálogo | Aporta lo que se necesita | Aporta lo que NO se necesita |
|---|---|---|---|
| **Haifa Cal GG** (nitrato de calcio granular) | 15.5% N nítrico · 26.3% CaO (≈18.8% Ca) | ✅ **Ca y N** | Nitrato (hay que bajar la forma nítrica) |
| **Polyfeed 10-10-43** | 10% N · 10% P₂O₅ · **43% K₂O** | P (algo) | 🔴 **K masivo** |
| **Bitter Mag 16MgO** (sulfato de magnesio) | 16% MgO (≈9.6% Mg) · ~32% SO₃ (≈13% S) | — | 🔴 **Mg + S, los dos sobran** |
| **Haifa Micro Hydroponic** | Mezcla de micros quelatados (Fe, Mn, Zn, Cu, B, Mo) | ✅ **Cu, B, Zn, Mn** | **% de Cu SIN CONFIRMAR — es el dato clave que falta** |
| **Haifa MKP** (0-52-34) | 52% P₂O₅ · 34% K₂O | P | 🔴 K — **ya eliminado** |
| **Haifa UP** (12-61-0) | 12% N · 61% P₂O₅ | P | — **ya eliminado** |
| **Fullfert** (no es Haifa) | Húmicos/fúlvicos | ✅ Acondicionador | — |

`PENDIENTE CONFIRMAR` en las cuatro composiciones activas, sobre todo el **% de Cu de Haifa
Micro Hydroponic**: sin ese número no se puede calcular cuánto cobre recibe cada bloque, que es
el centro del problema de Bloque 5.

## Cuánto está entrando por tanque de 2.000 L

Cálculo a partir de las dosis vigentes de `01-fertirriego-formulas.md` y las composiciones de
catálogo. Factores: K₂O→K ×0.83 · MgO→Mg ×0.603 · CaO→Ca ×0.715 · SO₃→S ×0.40 · P₂O₅→P ×0.436

| Fórmula | N | Ca | **K** | **Mg** | **S** | P | **Ca:K** |
|---|---|---|---|---|---|---|---|
| Inv 3 Vegetativo | 211 g | 226 g | **89 g** | 39 g | 51 g | 11 g | 2.5 : 1 |
| Inv 3 Floración | 232 g | 263 g | **54 g** | 39 g | 51 g | 7 g | 4.9 : 1 |
| **Inv 4+5 Vegetativo** | 246 g | 226 g | **🔴 214 g** | **58 g** | **77 g** | 26 g | **🔴 1.05 : 1** |
| Inv 4+5 Floración | 257 g | 263 g | **143 g** | 58 g | 77 g | 17 g | 1.8 : 1 |

**Dos lecturas:**

1. **La fórmula de Inv 4+5 Vegetativo entrega casi tanto K como Ca (1.05:1).** Sobre un suelo
   con saturación de K en 30% y de Ca en 37.8%, eso no corrige el desbalance: lo mantiene.
2. **El S del Bitter Mag es 51–77 g por tanque, todas las semanas,** sobre un suelo con S en
   42–52 mg/kg (alto). Confirma numéricamente el pendiente que estaba abierto.

## El experimento natural que confirma el mecanismo

Los tres bloques forman, sin haberlo planeado, un experimento de tres condiciones:

| Bloque | Polyfeed que recibe | Presión de agua | **K en suelo resultante** |
|---|---|---|---|
| Bloque 3 | **250 g** (dosis baja) | Media | **25.3%** |
| Bloque 4 | **600 g** (dosis alta) | **Alta y uniforme** | **🔴 30.0% — el más alto** |
| Bloque 5 | **600 g** (dosis alta) | **La peor del sistema** | **23.7% — el más bajo** |

> **La saturación de K sigue casi exactamente el producto de (dosis de Polyfeed × entrega de
> agua).** Inv 4 recibe dosis alta y agua uniforme → K más alto. Inv 5 recibe la misma dosis alta
> pero la peor agua → K más bajo. Bloque 3 recibe dosis baja → intermedio.

Esto demuestra dos cosas de una sola tabla:
- **El Polyfeed sí es una fuente material del exceso de K** (no solo el Bokashi).
- **El fertirriego se entrega en proporción al agua** — que es la misma razón por la que el Cu de
  Bloque 5 no respondió a la dosis fija de 180 g de Haifa Micro.

---

# Lista de compra para la casa comercial nueva

Ordenada por impacto en la factura. **El #1 es donde se decide el ahorro, porque es el de mayor
volumen.**

| # | Producto a cotizar | Reemplaza | Qué preguntar específicamente |
|---|---|---|---|
| **1** | **Nitrato de calcio** hidrosoluble | Haifa Cal GG | % N, % CaO, solubilidad. **Producto de mayor volumen** |
| **2** | **Micronutriente completo hidrosoluble quelatado** | Haifa Micro Hydroponic | **Análisis garantizado COMPLETO.** Cu, B, Zn, Mn, Fe **quelatados** (EDTA/DTPA/aminoquelato) y **cero o mínimo K, Mg y S** |
| **3** | **Quelato de cobre** individual | — (nuevo) | Para dosificar Cu por bloque, sobre todo B5. **Quelato, NO sulfato de cobre** |
| **4** | **Aminoácidos / N orgánico** hidrosoluble | Parcialmente el nitrato | % aminoácidos libres, origen. Herramienta contra mosca blanca y fusarium (Fase 1) |
| **5** | **Boro** soluble | — | Octaborato o ácido bórico soluble. **Margen estrecho — dosis conservadora** |
| **6** | **Húmicos / fúlvicos** | Fullfert | % húmicos, % fúlvicos, pH |
| **7** | **Calcio foliar quelatado** | Complementa ADNGard / Glukoplant | Ataca pétalos separados en 4B y botrytis en 3C. **Entrega foliar, no de suelo** |
| **8** | **MAP 12-61-0** o fosfito de **calcio** | — (**solo Bloque 4**) | **MAP es N+P con CERO K.** No aceptar fosfito de **potasio**: trae K |
| **9** | **Recubierto de liberación lenta de N o N-Ca** | Cote NPK | **Sin K.** Si no lo tienen, se descarta la vía |

## 🔴 Lo que NO se debe cotizar

**Ninguna fuente de K, Mg ni S.** Nada tipo Polyfeed / NPK con K alto. Nada "sulfato de X".

> **El ahorro más grande de este ejercicio no viene de cambiar de proveedor. Viene de dejar de
> comprar dos productos que hoy se compran.** Un Polyfeed más barato en la casa nueva sigue siendo
> una mala compra.

---

# Datos que hacen falta para poder decidir

## De Haifa
- [ ] **Precio actual por presentación** de: Haifa Cal GG, Polyfeed 10-10-43, Bitter Mag 16MgO,
      Haifa Micro Hydroponic
- [ ] **Ficha técnica de Haifa Micro Hydroponic** — el **% de Cu** es el dato que falta para
      cerrar el diagnóstico de Bloque 5
- [ ] Tamaño de presentación (kg por saco/bulto) de cada uno

## De la casa nueva
Por cada producto de la lista de 9:
- [ ] **Análisis garantizado completo** (% de cada elemento, incluidos los que no interesan — ahí
      se esconde el S y el K)
- [ ] **Forma química** de cada nutriente: nitrato vs amonio vs urea; quelato (EDTA/DTPA/
      aminoquelato) vs sulfato vs óxido
- [ ] Presentación (kg o L por empaque) y **precio por presentación**
- [ ] Si es 100% hidrosoluble para fertirriego o granular para suelo
- [ ] Pedido mínimo y estabilidad de suministro
- [ ] **Ficha técnica** — sin ficha no entra a formulación (Regla 3)

## De campo
- [ ] **Litros de tanque aplicados por m² por bloque** — sin esto no se puede pasar de "gramos
      por tanque" a "kg por m² por año", que es la unidad en la que se decide

---

# Plantilla de comparación (a llenar cuando lleguen los precios)

La comparación NO es precio por kg de producto. Es en tres columnas:

| Criterio | Por qué |
|---|---|
| **1. Costo por kg de nutriente ÚTIL** | Un producto al 15% de Ca a $X no es comparable con uno al 26% a $X |
| **2. Nutrientes "pasajeros"** | Cuánto K, Mg y S trae escondido. Un producto barato que mete 15% de K₂O no es barato — es un pasivo |
| **3. Forma química** | Quelato vs sulfato vs óxido cambia la disponibilidad real, y por lo tanto el costo por kg **absorbido**, que es lo único que importa |

| Producto | Casa | Presentación | Precio | % nutriente útil | **$/kg nutriente útil** | K/Mg/S pasajero | Forma | Veredicto |
|---|---|---|---|---|---|---|---|---|
| Nitrato de calcio | Haifa | | | 26.3% CaO | | — | Nitrato | |
| Nitrato de calcio | Nueva | | | | | | | |
| Micro completo | Haifa | | | Cu ?% | | | Quelato | |
| Micro completo | Nueva | | | | | | | |
| Quelato de Cu | Nueva | | | | | | | |
| Aminoácidos | Nueva | | | | | | | |
| Boro | Nueva | | | | | | | |
| Húmicos/fúlvicos | Fullfert | | | | | | | |
| Húmicos/fúlvicos | Nueva | | | | | | | |
| Ca foliar | Nueva | | | | | | | |
| MAP (solo B4) | Nueva | | | | | | | |
| Recubierto N sin K | Nueva | | | | | | | |
