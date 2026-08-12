# Lo que falta para construir la estrategia

```bash
python3 motor/cerebro.py matriz     # estado medido de las 11 variables
```

Esta es la lista de datos que faltan para que el proyecto pueda decidir **dónde
y cómo** sembrar, no solo qué y cuándo. Ordenada por relación
**esfuerzo / desbloqueo**: primero lo que cuesta minutos y desbloquea mucho.

Cada bloque dice: qué se necesita, en qué formato entra al repo, y qué se puede
decidir cuando esté.

---

## NIVEL 0 — Archivos que ya existen: solo hay que compartirlos

Esto es lo más barato de todo: **no hay que generar el dato, hay que darle acceso
al repositorio.** `07-datos/README.md` los lista como pendientes de traer.

### 0.1 · `DCB_Fitosanidad_Maestro.xlsx`
Ocho hojas: INSUMOS, BUSCAR, ROTACION, REGISTRO, CONSUMO, INVENTARIO,
GASTO_MENSUAL. El propio diccionario de datos del repo la llama **"la pieza más
importante que falta"**.

Desbloquea de golpe:
- la regla APLICACIONES con historial real y no solo la semana 27
- el costo por aplicación y por bomba (mitad de la variable 11)
- el cruce entre qué se aplicó y qué problema apareció después — que es lo que
  convierte `incidencia_fitosanitaria.csv` de registro en herramienta de decisión

### 0.2 · `DCB_Modelo_Costos.xlsx` y `Calculo_por_tallo.xlsx`
Desbloquean la variable 11 completa: **margen por m² por semana**, el eje que
vuelve comparables las otras diez variables. Si estos archivos ya tienen los
costos, el punto 1.4 de abajo sobra.

### 0.3 · `aplicaciones_historial.csv` actualizado
Hoy tiene 16 filas, todas de la semana 27. La regla no negociable #2 de
`CLAUDE.md` prohíbe recomendar una bomba sin leer este archivo actualizado —
así que mientras no llegue, **no se puede recomendar rotación**, y eso es un
bloqueo operativo, no solo analítico.

### 0.4 · `PROGRAMACION_2026` en su versión v8
Los CSV de `07-datos/` se exportaron de la v7. La v8 tiene la homologación
reparada (306/306 siembras cruzando contra 302 hoy). Reexportar desde v8 mejora
directamente la variable 8, que hoy está en 21 % justamente por nombres que no
cruzan.

---

## NIVEL 1 — Minutos de Vanessa, desbloqueo inmediato

### 1.1 · Tallos por planta de 10 grupos
**Faltan:** Daucus carota · Celosia Purple Flamingo · Carthamus · Dianthus ·
Ptilotus · Heliperum · Marigold · Orlaya · Scabiosa · Dahlia

Un número por grupo. Es el multiplicador que convierte "necesito 400 tallos" en
"necesito 400 plantas" o "necesito 133". Sin él el motor no puede calcular la
cantidad a sembrar de esos diez grupos.

→ `07-datos/ciclos_variedad.csv`, columna `tallos_planta`

### 1.2 · La semana en los comentarios: ¿ISO o semana de campo?
En los COMENTARIOS de `campo_siembras.csv` aparecen frases como *"en semana 16
tiene mucha botrytis"* y también *"Sem24: 15 semanas campo"*. La primera es
ambigua; la segunda deja claro que hay dos relojes en uso.

**La pregunta:** cuando se escribe "semana 16" en un comentario de siembra, ¿es
la semana 16 del año o la semana 16 desde el trasplante?

Sin resolverlo, los 29 eventos fitosanitarios no se pueden fechar y el patrón de
botrytis en Statice no se puede convertir en un preventivo automático.

→ `07-datos/incidencia_fitosanitaria.csv`, columna `tipo_semana`

### 1.3 · Precio de venta por tallo, por variedad
Hoy solo se conoce el precio del producto terminado. Para calcular **margen por
m² por semana** hace falta el valor del tallo suelto por variedad — aunque sea
un rango o el precio al que se vende a mayoristas.

→ nuevo `07-datos/precio_tallo.csv`

### 1.4 · Costo de semilla
Precio del sobre o de la bandeja, y cuántas semillas o plántulas trae. Con eso
más el porcentaje de germinación que ya está en
`variedades_parametros_siembra.csv` sale el costo por planta establecida.

→ `07-datos/costos_productos.csv` (hoy vacío)

### 1.5 · Color confirmado de Statice Forever Happy
Está en 9 de los 24 productos con color inferido y confianza baja. Una foto o
una confirmación en campo cierra el hueco.

→ `07-datos/paleta_color.csv`, columna `confianza_color`

---

## NIVEL 2 — Requiere una compra pequeña, desbloquea la variable central

### 2.1 · Termómetro / higrómetro de máxima y mínima por bloque
**Esta es la compra de mayor apalancamiento del proyecto después de la bomba.**

Lo mínimo útil: **un medidor de máx–mín por invernadero** (Inv 1, 2, 3A, 3B, 3C,
Mini, 4, 5, 6 y una referencia en exterior = 10 puntos). Se lee una vez por
semana y se anota. No hace falta datalogger ni conexión: máxima, mínima y humedad
relativa máxima, una vez por semana, ya permite:

- fijar el umbral de botrytis por bloque (HR alta + rango 15–25 °C)
- explicar por qué 3C mata el lisianthus y 3A superior mató el Dianthus, con
  números en vez de adjetivos
- corregir el ciclo esperado por temperatura de la zona, no solo por variedad

**Si el presupuesto solo alcanza para dos:** uno en Inv 4 (la referencia buena)
y uno en 3B (el problemático). El contraste medido entre esos dos vale más que
diez estimaciones.

**La pregunta:** ¿hay algún termómetro o higrómetro en la finca hoy? ¿Cuál es el
presupuesto para esto?

→ `07-datos/microclima_bloques.csv`, columnas `temp_min_c`, `temp_max_c`,
`hum_rel_max_pct`

### 2.2 · Pluviómetro o fuente de clima semanal
Lluvia en mm y días de lluvia por semana. Si no hay pluviómetro, sirve la
estación meteorológica más cercana a Rionegro — pero hay que decidir la fuente y
usar siempre la misma.

**La pregunta:** ¿hay pluviómetro? ¿Prefieres registro propio o tomar una
estación de referencia?

→ `07-datos/clima_semanal.csv` (hoy vacío, solo encabezado)

---

## NIVEL 3 — Requiere una rutina nueva de operarios

### 3.1 · Longitud de tallo en cosecha
**El hueco más grande del repositorio: la calidad no se mide en ninguna parte.**

Rutina mínima: en cada cosecha, de cada lote, **medir 10 tallos al azar** y
anotar el largo mínimo, el promedio aproximado y el máximo. Dos minutos por lote.

Lo que desbloquea:
- juzgar si "tallo corto en 3B" es una impresión o un hecho — es la razón real
  por la que se propuso sacar la campánula
- distinguir el lote que produjo del lote que produjo vendible
- optimizar por calidad, que es la mitad del objetivo declarado y hoy la mitad
  que el sistema no puede ver

→ `07-datos/calidad_tallo.csv` (hoy vacío, solo encabezado)

### 3.2 · Plantas trasplantadas por lote
Solo 13 de 62 lotes cosechados se pueden cruzar con su número de plantas. Sin el
divisor no hay rendimiento, solo conteo de tallos.

La causa no es que falte el dato: es que `Bloque sembrado` en CAMPO y `Bloque` en
REGISTRO se escriben distinto, y a veces falta el nombre homologado. El motor ya
normaliza los bloques (`norm_bloque`); lo que falta es **llenar la columna N y
`Cantidad Trasplantada` en toda siembra nueva, sin excepción.**

→ `07-datos/campo_siembras.csv`

### 3.3 · Severidad en el registro fitosanitario
Cuando aparece un problema, anotar además de qué es: **en qué semana desde el
trasplante, qué porcentaje de la cama, y qué se hizo.** Los 29 eventos históricos
tienen el qué pero casi ninguno tiene el cuándo exacto ni el cuánto.

→ `07-datos/incidencia_fitosanitaria.csv`

---

## NIVEL 4 — Decisiones de Vanessa, no datos

### 4.1 · El cultivar en las recetas
83 tallos DCB del catálogo (26 %) piden un grupo y no un cultivar. Es una
decisión comercial producto por producto, no un dato que se pueda derivar.

### 4.2 · La mezcla de color objetivo del punto de venta
`objetivo_color_pdv.csv` está marcado `PROPUESTA — SIN VALIDAR`. Los datos de
rotación real viven en `03_Ventas`, que está fuera del alcance de este proyecto.
Mientras eso siga así, la mezcla objetivo tiene que salir del criterio de
Vanessa, no de los datos.

### 4.3 · Medir las camas de Ext 3B, Inv 2, Mini, Inv 4C e Inv 6
Cinco bloques sin huecos ni líneas registradas. La capacidad real de la finca
está subestimada hasta que se midan.

### 4.4 · ¿Hay comprador para el lavanda?
`decisiones_manejo.csv` dice que la flor se marchitó sin comprador; la bitácora
dice *"vende muy bien"*. Es una contradicción entre fuentes que solo Vanessa
resuelve. Ver `04-variedades/03-campanula-champion-lavender.md`.

---

## Errores de dato a corregir en la fuente

| Dónde | Qué | Efecto |
|---|---|---|
| `DCB_Registro_Tallos` hoja REGISTRO | 33 filas del 6–8 de julio fechadas en **2056**, una fila en `2026-09-19` y una en `2025-06-17` | Corregidas al importar (`motor/importar_tallos.py`, confirmadas por Vanessa 2026-08-12). **Siguen mal en Drive** — no hay herramienta de escritura sobre Sheets; conviene arreglarlas en la hoja |
| `campo_siembras.csv` | `Carthamus Zanzíbar` tiene nombre homologado `Dianthus Sweet Cherry` | Aparece en el calendario de Erica como la variedad equivocada |
| `formulas_productos_bouquets.csv` | 11 filas de productos fitosanitarios dentro del archivo de recetas | Contaminan la auditoría del catálogo |

---

## Orden recomendado

1. **Nivel 0 primero, siempre.** Es acceso, no trabajo. Cuatro archivos que ya
   existen y que desbloquean fitosanidad completa y margen completo.
2. **Nivel 1 completo** — una sesión de dictado. Desbloquea cantidad de siembra
   en 10 grupos, el fechado de las plagas y el arranque del cálculo de margen.
3. **2.1, aunque sea con dos medidores** — es la variable que hoy está en cero y
   la que decide DÓNDE, que es el hueco central de la estrategia.
4. **3.1 y 3.2 como rutina fija** — no dan resultado esta semana, dan resultado
   en tres meses. Por eso hay que arrancarlas ya.
5. **Nivel 4** cuando haya tiempo de decidir con calma, producto por producto.

Con el Nivel 0 y el Nivel 1 se puede armar la primera estrategia de siembra con
**cantidad y margen** justificados. Con 2.1 encima, la estrategia incluye
**bloque asignado y preventivos fechados** — que es la estrategia completa. Sin
2.1, el bloque se seguirá asignando por intuición.
