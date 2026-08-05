# La matriz de decisión de campo

```bash
python3 motor/cerebro.py matriz     # cuánto de esta matriz está cubierto hoy
```

Este documento es el corazón del proyecto. Las dos piernas visibles del objetivo
—color en el punto de venta y combinación del bouquet— se resuelven con recetas.
**La tercera pierna, el medio de la cadena, es una matriz de once variables, y
ahí es donde se gana o se pierde la rentabilidad de la finca.**

## Qué decide una siembra

Una decisión de siembra no es una fecha. Son cinco respuestas simultáneas:

| Salida | Pregunta | Hoy la responde |
|---|---|---|
| **QUÉ** | qué variedad y qué cultivar | demanda de color (motor: `explotar`) |
| **CUÁNTA** | cuántas plantas | tallos/planta + merma (motor: `sembrar`) |
| **DÓNDE** | qué bloque y qué cama | **nada — es el hueco central** |
| **CUÁNDO** | semana de bandeja y de trasplante | ciclo (motor: `sembrar`) |
| **CÓMO** | manejo, nutrición, preventivos | reglas de `03-fitosanidad/` |

El motor ya responde QUÉ, CUÁNTA y CUÁNDO. **DÓNDE y CÓMO todavía viven en
prosa**, repartidos entre `01-invernaderos.md`, los COMENTARIOS de
`campo_siembras.csv` y la memoria de Vanessa. Convertirlos en matriz consultable
es el trabajo.

## Las once variables

### 1. Demanda de color y producto
Fija QUÉ y CUÁNTA. Es la única variable que se lee de izquierda a derecha: la
demanda manda sobre la siembra. Bloqueo actual: 83 tallos DCB del catálogo piden
un *grupo* ("Zinnia") y no un *cultivar*, así que no piden un color.

### 2. Ciclo, ventana, tallos/planta, densidad, pinch
Fija CUÁNDO y CUÁNTAS plantas. Fuente primaria para el calendario de clientes:
`variedades_bitacora.csv`. Fuente de manejo interno: `ciclos_variedad.csv`.
Bloqueo actual: 10 grupos sin `tallos_planta` — Daucus carota, Celosia Purple
Flamingo, Carthamus, Dianthus, Ptilotus, Heliperum, Marigold, Orlaya, Scabiosa,
Dahlia. Es un número por grupo.

### 3. Microclima del bloque y de la cama
**La variable que decide DÓNDE.** Temperatura, humedad relativa, humedad
nocturna, radiación, ventilación. Hoy es cualitativo: `microclima_bloques.csv`
describe 18 zonas en ALTA/MEDIA/BAJA derivadas de `01-invernaderos.md`, con
`confianza = CUALITATIVA`. Cero mediciones numéricas.

**Por qué importa que sea numérico:** la botrytis no responde a "húmedo",
responde a horas de humedad relativa sobre ~85 % con temperatura entre 15 y
25 °C. Sin números no hay umbral, y sin umbral no hay predicción — solo
intuición retrospectiva.

El gradiente dentro de un mismo bloque es tan fuerte como el gradiente entre
bloques: en 3A las camas superiores mataron el Dianthus y las inferiores son las
mejores de larkspur. **La unidad de decisión es la cama, no el invernadero.**

### 4. Presión y uniformidad de riego
**La limitante dominante de la finca.** Solo ~22 % del área funciona a pleno
potencial, y la causa no es agronómica: es presión de agua. Está confirmado
como causa, no supuesto — trachelium y matricaria se quedaron vegetativos sin
florar en Inv 5 por estrés hídrico.

La lección transferible más importante que documenta el repositorio:
**camas cortas = presión uniforme = riego homogéneo.** Es la razón por la que
Inv 4 es el mejor bloque del cultivo. Cualquier inversión en camas nuevas debería
copiar esa geometría antes de copiar cualquier otra cosa.

### 5. Suelo por zona
M.O., C.E., compactación, inóculo. Casos duros ya documentados: Inv 4 con M.O.
25.6 % contra 3B con salinidad activa (C.E. 0.829) y compactación en la
"barriga" de la cama. El suelo no se cambia en una semana, así que esta variable
funciona como **restricción**, no como palanca: decide qué variedad tolera esa
cama mientras se mejora.

### 6. Histórico de plagas y hongos por variedad × bloque × semana de ciclo
`incidencia_fitosanitaria.csv` — 29 eventos, extraídos de texto libre.

Lo que ya se ve al ordenarlo:

| Patrón | Evidencia | Tipo |
|---|---|---|
| Botrytis en Statice entre semana 16 y 21 de cosecha | Forever Silver, Quis Apricot, Hipster White, Forever Happy | **ventana temporal, no variedad** |
| Mosca blanca en Matricaria Vegmo en 3C y Inv 5 | 4 lotes, 3 sacrificados | **inóculo de suelo, no variedad** |
| Fusarium en Lisianthus en Mini/3C/3B | 11 cultivares del mismo lote, 1 resistente (Megalo I Yellow) | **suelo + zona, con diferencia varietal real** |
| Mildeo en Inv 1 y Inv 2 | rosas, dahlias | **humedad nocturna** |

El tercero es el más valioso: **de once cultivares de lisianthus en la misma
condición, uno resistió.** Eso no es azar de manejo, es una diferencia varietal
que vale plata. Con más ciclos se vuelve una regla de selección.

**Trampa activa en este dato:** las semanas en los comentarios mezclan semana ISO
del año con semana de campo del cultivo. `tipo_semana` marca ISO, CAMPO o
AMBIGUA. Resolver esa ambigüedad es requisito para poder predecir.

### 7. Clima de la temporada
Antioquia es bimodal: lluvias mar–may y sep–nov, seco dic–feb y jun–ago. El
clima corre el ciclo y dispara el hongo. `clima_semanal.csv` está vacío.

Ya se documentó en `05-programacion/04-como-predecir-ciclos.md` por qué el
intento de derivar el efecto de temporada desde los datos actuales falló: el
efecto medido de temporada era 0.7 semanas contra 4.1 semanas de ruido en el
registro de la fecha de inicio de cosecha. **El ruido de medición era seis veces
más grande que la señal.** Sin clima registrado semana a semana, la temporada no
es una variable, es una anécdota.

### 8. Histórico de tallos, normalizado por ventana
`cerebro.py rendimiento`. La normalización a **tallos/planta/día** no es
cosmética: es lo que evitó sacar del cultivo una variedad viable. Ver
`04-variedades/03-campanula-champion-lavender.md`.

Bloqueo actual: solo 13 de 62 lotes cosechados se pueden cruzar con su número de
plantas. Sin plantas no hay divisor, y sin divisor no hay rendimiento — solo
conteo.

### 9. Calidad del tallo
**Cero registros en todo el repositorio.** No se mide longitud ni grado en
ninguna parte. Esto es un hueco estructural, no un dato faltante más:

- Separa "produjo" de "produjo vendible". Un lote con 1.200 tallos de 40 cm
  puede valer menos que uno con 700 de 70 cm.
- Es la razón real por la que se propuso sacar la campánula de 3B — "tallo
  corto". Esa frase no se puede evaluar porque no es un dato.
- Es la mitad del objetivo declarado: *tallos extraordinarios en calidad y
  presentación.* Hoy el sistema optimiza cantidad porque es lo único que mide.

### 10. Capacidad de camas
Restricción dura del calendario: 13 de 18 bloques medidos. Faltan Ext 3B, Inv 2,
Mini, Inv 4C e Inv 6.

### 11. Costo de semilla, insumos y mano de obra
`costos_productos.csv` está vacío, y con él está bloqueado el único eje que une
los otros tres.

## La unidad correcta de eficiencia

**Margen por m² por semana de cama ocupada.**

No tallos por planta. No tallos por m². Una cama ocupada 30 semanas por un
cultivo de bajo precio pierde contra 18 semanas de uno alto, incluso si produce
más tallos. El tiempo de cama es el recurso escaso de la finca, y hoy no se
cobra en ninguna cuenta.

```
margen_m2_semana = (tallos × precio_por_tallo − costo_lote) / (área_m² × semanas_ocupada)
```

De los cinco términos, hoy se tienen tres: tallos, área y semanas. Faltan
`precio_por_tallo` real por variedad y `costo_lote`. **Ese es el bloqueo #5 y el
de mayor apalancamiento de todo el proyecto**, porque convierte cada una de las
otras diez variables en una cifra comparable.

## Cómo se usará la matriz cuando esté llena

Comandos que el motor podrá ofrecer, en orden de dependencia:

| Comando | Qué responderá | Necesita variables |
|---|---|---|
| `zona <variedad>` | mejor bloque y cama para esta variedad, con la razón | 3, 4, 5, 6 |
| `riesgo <variedad> <bloque> <semana>` | qué problema esperar y en qué semana de ciclo | 6, 7 |
| `margen <lote>` | margen por m² por semana de ese lote | 8, 9, 11 |
| `plan <demanda.csv>` | siembra completa con bloque asignado y preventivos fechados | todas |

`plan` es el objetivo final: la demanda de color entra, y sale un plan de siembra
con **variedad, cantidad, bloque, cama, semana de bandeja, semana de trasplante y
calendario de preventivos** — cada línea justificada con el dato que la sostiene.

## Los tres modos de error que la matriz debe impedir

1. **Ventana truncada.** Un lote interrumpido parece de bajo rendimiento cuando
   solo fue interrumpido. Ya codificado en `rendimiento`.
2. **Confundir efecto de zona con efecto de variedad.** El caso lisianthus lo
   muestra en las dos direcciones: once cultivares fallaron por zona, uno resistió
   por genética. Sin separar las dos causas se saca la variedad equivocada.
3. **Confundir semana ISO con semana de campo.** Un patrón fechado en la semana
   equivocada predice el problema en el momento equivocado, que es peor que no
   predecirlo.

---
*Estado medido de cada variable: `python3 motor/cerebro.py matriz`*
*Qué falta y en qué orden: `08-roadmap/02-informacion-que-falta.md`*
