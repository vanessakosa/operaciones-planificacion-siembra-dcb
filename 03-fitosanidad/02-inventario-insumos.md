# Inventario de insumos

> **Estado: stock del 26/03/2026 — DESACTUALIZADO.** Neofat y Comcat probablemente agotados.
> Actualizar antes de usar para decisiones de compra.

## Fungicidas

| Producto | Stock | Función |
|---|---|---|
| Equifun (cola de caballo + silicio) | 7.000 cc | Botrytis, alternaria — PREVENTIVO |
| Botrycid (Burkholderia) | 1.000 cc | Botrytis específico — BIOLÓGICO. Intervalo etiqueta 12 semanas |
| Amicos MC (Bacillus subtilis) | 1.000 cc | Mildeos, botrytis, fusarium, trips |
| Regalia (Reynoutria) | 500 cc | Mildeo polvoso, botrytis — inductor de resistencia |
| Yodosafer (yodo PVP) | 500 cc | Fungicida + bactericida. **NO en floración** |
| Rutastar (cítricos) | 250 cc | Botrytis, mildeos, erwinia |
| ADN Fun (extractos) | 250 cc | Mildeo polvoso, botrytis |
| Agua de vidrio (silicio) | 700 cc | Fortalece tejidos |

## Nutracéuticos y nutricionales

| Producto | Stock | Función |
|---|---|---|
| ADNGard (Ca + aminoácidos) | 400 g | Inhibe colonización de hongos — preventivo |
| Glukoplant Cabozan (Ca+B+Zn) | 1.000 cc | **Máx 6 aplicaciones por ciclo** |
| Engruese (calcio) | 4.000 cc | Fortalecimiento celular |
| Tropical | 2.000 cc | Crecimiento vegetativo |

## Inoculantes

| Producto | Stock | Función |
|---|---|---|
| Pokonia | 2.000 cc | Control biológico fusarium / nematodos |
| Fitoderma (Trichoderma + Bacillus) | 600 g | Acondicionador, PGPR, fusarium — **solo Inv 3** |
| Estabios (Azotobacter + Pseudomonas) | 3.000 cc | PGPR, fijación N, solubilización de fosfatos |
| Endhoriza (micorrizas) | 1.500 cc | Colonización radicular — AL TRASPLANTE |
| Promobac (Bacillus mix) | 1.000 cc | Bioestimulante PGPR |

## Insecticidas

| Producto | Stock | Función |
|---|---|---|
| Safer Mix (Beauveria mix) | 500 g | Mosca blanca, trips, spodoptera |
| ADN Green (Stemona) | 1.000 cc | Trips, áfidos, mosca blanca |
| No Fly (Paecilomyces) | 600 g | Mosca blanca, pulgones, trips |
| Agroemulsión (aceites) | 700 cc | Asfixia: ácaros, mosca blanca, áfidos |
| Alysin (ajo-ají) | 500 cc | Repelente — usar hasta agotar |
| BTK (Bacillus thuringiensis) | 250 cc | Defoliadores, trips, spodoptera |
| Azasol (azadiractina 6%) | 15 g | **Reservar para emergencias — casi agotado** |

## Bioestimulantes y acondicionadores

| Producto | Stock | Función |
|---|---|---|
| Ascofol (Ascophyllum) | 1.000 cc | Hormonal: auxinas, citocininas, giberelinas |
| Naturamin (aminoácidos) | 1.000 g | Nutricional, resistencia a estrés |
| Starzyme (aminoácidos + vitaminas) | 500 cc | Activación metabólica. Prefloración sem 5–10 |
| Fullfert (húmicos/fúlvicos) | — | **Reemplazó a Naturhumic** |
| LS60 (extracto de teína) | 700 cc | Molusquicida — babosas y caracoles |

## Redundancias a eliminar (decisión tomada)

| Duplicado | Decisión |
|---|---|
| **Ajo-ají:** Alysin y Apiche | Son lo mismo. Usar Alysin hasta agotar, **no reponer Apiche** |
| **Beauveria:** Safer Mix y Tornado | Casi idénticos. Usar Safer Mix, **descartar Tornado** |
| **Botrytis:** 6 productos en bodega | Máximo necesario: 3 con mecanismos distintos. Los mejores: **Botrycid + Equifun + Regalia**. Solar y ADN Fun son redundantes |

**Nota:** Solar aparece en el historial de aplicaciones de sem 27 a pesar de estar marcado como
redundante. Aclarar si la decisión cambió o si fue por agotar existencias.

## Aclaración de clasificación

**Amicos MC es corrector nutricional (Mg/Ca), no biofungicida** — aunque en el inventario
original está listado como fungicida por su efecto sobre Bacillus subtilis. Cuidado al contarlo
como componente fungicida de una bomba.

## Costos

`07-datos/costos_productos.csv` está **vacío** — la hoja COSTOS_PRODUCTOS del maestro tiene
encabezados pero sin datos. **Sin esto no se puede calcular costo por aplicación ni costo por
tallo del componente fitosanitario.** Es un bloqueo real para el análisis de rentabilidad.
