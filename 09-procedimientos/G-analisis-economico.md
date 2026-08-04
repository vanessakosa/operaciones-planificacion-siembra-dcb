# Análisis económico — procedimientos

## Los tres niveles

| Nivel | Pregunta | Frecuencia | Bloqueado por |
|---|---|---|---|
| **Por tallo** | ¿Cuánto cuesta producir este tallo? | Por lote (al cierre) | RENDIMIENTO vacía |
| **Por cama** | ¿Esta cama fue rentable? | Por lote (al cierre) | RENDIMIENTO vacía + costos_productos vacío |
| **Por mes** | ¿El negocio está ganando o perdiendo? | Mensual | Los 3 parámetros congelados en sept/2025 |

---

## Nivel 1 — Costo por tallo

### Componente agrícola (varía por variedad)

```
costo_agricola = (costo_plántula + costo_insumos_cama) ÷ tallos_cosechados_reales
```

| Insumo | De dónde sale | Estado |
|---|---|---|
| Costo plántula | `07-datos/finca_entregas_plantulas.csv` + facturas Ball/Andrés | 🟡 parcial |
| Costo Bokashi por cama | Costo saco ($14.700) × sacos usados en preparación | ✅ calculable |
| Costo Cote NPK por cama | Precio/kg × g/m² × m² de la cama | 🔴 falta precio/kg |
| Costo bombas recibidas | Precio/cc o g de cada producto × dosis × bombas | 🔴 costos_productos vacío |
| Costo fertirriego | Precio/kg de cada haifa × gramos por tanque × tanques recibidos | 🔴 costos_productos vacío |
| Tallos cosechados reales | REGISTRO — suma del lote | 🟡 sin agregar (CONSOLIDADO vacía) |

### Los tres parámetros no agrícolas (cambian cada mes)

| Parámetro | Valor de referencia (sept/2025) | Fórmula |
|---|---|---|
| Poscosecha / tallo | **$800 COP** | (nómina bouqueteadoras + Chrysal + empaques) ÷ tallos procesados |
| Overhead / tallo | **$224 COP** | Gastos 3C del mes ÷ tallos vendidos |
| Logístico / tallo | **$305 COP** | Costo LABAN completo ÷ (tallos × 93%) |
| **Suma no agrícola** | **$1.329 COP/tallo** | |

> ⚠️ Estos tres valores tienen **10 meses de antigüedad** (sept/2025, base = 25.142 tallos).
> Cualquier análisis que los use hoy tiene ese sesgo — hay que declararlo.
> Se recalculan el primer día de cada mes con los datos reales del mes anterior.

---

## Nivel 2 — Rentabilidad por cama / por variedad

### La cadena completa (hoy está cortada)

```
REGISTRO (tallos reales) → CONSOLIDADO (agrupado por lote) → RENDIMIENTO (tallos/m², $/tallo, utilidad)
                              ↑ ROTO — sin fórmulas
```

### Cuando esté funcionando, el cálculo es

```
utilidad_cama = ingreso_cama - costo_agricola_cama - (tallos × $1.329 no_agricola)

ingreso_cama = tallos_vendidos × precio_promedio_por_tallo_de_esa_variedad
```

### El precio por tallo por variedad — dato que falta

Hoy no existe en ningún archivo. Es el puente entre lo agrícola y lo comercial.

| Lo que hay | Lo que falta |
|---|---|
| Precio por bouquet (`formulas_productos_bouquets.csv`) | Precio por tallo por variedad por canal |
| Composición del bouquet | Cuántos tallos de cada variedad entran en cuántos bouquets vendidos |

**Para construirlo:** precio del bouquet ÷ tallos DCB que lleva = precio implícito por tallo.
Es una aproximación, pero es suficiente para ordenar variedades de más a menos rentable.

### Ejemplo con lo que ya existe

```
Cosecha Grande $125.000 = 11 tallos DCB
Precio implícito promedio por tallo DCB = $125.000 ÷ 11 = $11.364

Gomphrena: 5 tallos en Cosecha Grande
Si el 30% del volumen va en bouquets de este tipo → precio Gomphrena ≈ $11.364
Costo agrícola Gomphrena (ciclo 15 sem, densidad 15 cm, rendimiento estimado) = ???
Margen = precio - costo
```

El ??? es lo que desbloquea CONSOLIDADO + RENDIMIENTO.

---

## Nivel 3 — Cierre mensual

### Los pasos (primer día del mes siguiente)

1. Verificar que todos los gastos del mes estén en el Google Form / Registro Gastos
2. Confirmar nómina — marcar inactivos
3. Calcular los 3 parámetros con datos reales del mes:
   - Poscosecha: sumar subcategoría 2E del mes ÷ tallos procesados de Diana
   - Overhead: sumar subcategoría 3C del mes ÷ tallos vendidos
   - Logístico: sumar subcategoría 2F del mes ÷ (tallos × 93%)
4. Actualizar "Parámetros Mensuales" en DCB_Modelo_Costos.xlsx
5. El P&G se actualiza automáticamente

### Lo que Code puede hacer aquí

- Alertar cuando faltan gastos del mes (comparar contra el promedio histórico)
- Calcular los 3 parámetros automáticamente si tiene acceso al Registro Gastos
- Detectar meses donde el costo por tallo sube más del 15% vs. el anterior

---

## Los datos que hay que conseguir para desbloquear todo esto

| Dato | Dónde existe | Cómo traerlo |
|---|---|---|
| Precio por kg/L de cada insumo (~35 productos) | Facturas BAM + Agrotienda | Conteo de bodega + facturas recientes |
| m² real por cama individual | Campo | Media mañana con cinta métrica |
| Precio de venta por tallo por variedad y canal | Erica / lista B2B | Sesión con Erica |
| Ventas históricas por semana (2024–2025) | WIX + puntos físicos | Exportar plataformas |
| Los 3 parámetros del mes actual | Nómina + Registro Gastos | Tatiana / cierre de mes |

**Prioridad:** precio de insumos primero, porque desbloquea el costo por aplicación
y el costo por cama — que son los dos números que más impactan la decisión de
mantener o sacar una variedad del programa.

---

## La decisión que esto habilita

Hoy la BITÁCORA tiene una columna "Decisión: MANTENER / REDUCIR / DESCARTAR"
llenada a mano, por intuición.

Con el análisis económico funcionando, esa columna se genera con datos:

```
Campanula Lavender 3B:
  Rendimiento: 0.64 tallos/planta vs 0.92 de la blanca
  Precio implícito: igual que la blanca
  Costo agrícola: igual (misma densidad, mismo ciclo)
  → SACAR — la blanca da 44% más tallos al mismo costo
```

Ese es el tipo de decisión que hoy se toma bien por instinto,
pero que el sistema debe poder hacer por todas las variedades,
todas las semanas, sin que Vanessa tenga que calcularlo.
