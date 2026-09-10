# Dónde quedamos — sesión de rentabilidad, 2026-09-10 (tarde)

> **SUPERADO EN PARTE — leer `05-donde-quedamos-ocupacion.md`.** La sección 3 de
> este documento nombra como bloqueo dominante la falta de `Fecha siembra campo`
> en `campo_siembras.csv` (13 % de las plantas). **Ese bloqueo no existía:** esa
> columna se dejó de usar y la de `Semana` de trasplante, que hace el mismo
> trabajo, está llena en el 95 % de las plantas. No se veía porque el archivo
> tiene dos columnas llamadas `Semana` y `csv.DictReader` colapsa encabezados
> repetidos. El eje ingreso/m²/semana **ya corre y ordena** desde el 2026-09-10.
> La sección 5 (la tensión volumen contra $/tallo) sigue válida, pero sus
> números de Lisianthus cambiaron al entrar las semanas 33-35.

**Para retomar en otra conversación.** Este archivo continúa
`03-donde-quedamos.md`, que cubre la sesión de cartera de la mañana.

```bash
git pull
python3 motor/ficha_variedad.py           # qué dato hay por grupo y cuál falta
python3 motor/ocupacion.py                # tallos y $ por m² por semana
python3 motor/ocupacion.py camas          # área de cada cama de la finca
python3 motor/dictar_tallos.py estado     # hasta dónde llega la cosecha
```

Rama de trabajo: `claude/epic-cerf-d05qp9`. **Está mergeada a `main`** — las dos
apuntan al mismo commit.

---

## 1. Lo que se pedía

Decidir **qué variedades son rentables y cuáles no**, y cuáles sobran o faltan en
la programación. Antes de decidir, Vanessa pidió ver el esqueleto de datos de
cada variedad y qué falta para poder hacer ese análisis.

## 2. La respuesta corta

Son **dos preguntas con salud de datos opuesta**:

| Pregunta | Se puede hoy | Con qué |
|---|---|---|
| ¿Sobra o falta en la programación? (volumen) | **Sí, 21 de 24 grupos** | `cerebro.py cartera` |
| ¿Es rentable? (plata) | **No, 0 de 24 grupos** | falta lo de abajo |

## 3. Lo que falta para la pregunta de rentabilidad

Tres piezas, ninguna es de cálculo:

1. **`Fecha siembra campo`** en `campo_siembras.csv` — llena en 112 de 302 filas.
   **Solo el 13 % de las plantas trasplantadas tiene fecha, y ese 13 % es de
   2025.** El área sale de plantas acumuladas de todo el histórico y los tallos
   de una ventana de 12 semanas: sin fecha no se recorta el área a la ventana, y
   tallos/m² no compara entre grupos. `ocupacion.py` detecta la condición y se
   niega a nombrar mejor ni peor mientras dure.
2. **Tallos vendidos por mes** — en 0 en los 12 meses de `DCB_Modelo_Costos`, que
   ya tiene los costos de 2026 cargados. Es su único campo manual. Vanessa quedó
   en subirlo. Piso ya calculable: $1.379/tallo en junio, $869 en julio.
3. **`calidad_tallo.csv`** — vacío. Separa "produjo" de "produjo vendible".

*(`costos_productos.csv` también está vacío pero NO es el bloqueo del margen:
es la lista de precios de insumos para costo por aplicación.)*

## 4. Lo que sí quedó resuelto

**El área de cama no hay que medirla: es una constante.** La finca tiene una sola
geometría — huecos cada 15 cm, 8 líneas, 1,20 m de ancho = **0,18 m² por hueco**.
Cierra contra todo lo documentado: Inv 4 completo 677,3 m² (doc: 677), Inv 5
411,8 m² (doc: 412). Nuevo: `07-datos/area_camas.csv`, 21 camas, 19 con área.

**Un error corregido dentro de la misma sesión.** La primera versión calculaba
el área como `plantas × (distancia/100)²`. Solo acierta a 15 cm: a 7,5 cm daba la
mitad del área real y a 30 cm el doble. La correcta es

```
área m² = plantas × 0,15 × (distancia_cm / 100)
```

porque la malla es 0,15 m **fijo en una dirección** y la distancia manda solo en
la otra — sembrar más denso mete más plantas en la MISMA cama. Statice pasó de
977 a 488 m² y Campanula de 133 a 266.

## 5. La tensión que hay que resolver cuando entren los datos

Cruzando el balance de volumen con el ingreso por tallo:

| Grupo | $/tallo | Balance en `cartera` |
|---|---|---|
| Lisianthus | 9.531 | SOBRA +6,7 pp |
| Zinnia | 8.021 | SOBRA +5,3 pp |
| Boca de Dragón | 6.029 | SOBRA +10,5 pp |
| Campanula | 5.200 | FALTA −6,3 pp |

**Tres de los cuatro grupos que "sobran" son el top 4 de ingreso por tallo.**
Decidir por volumen solo arrancaría lo que más plata deja. Y al revés: Lisianthus
rinde $9.531 por tallo pero ocupa la cama 29 semanas; Boca de Dragón $6.029 en
~15. Por semana de cama el orden puede invertirse — eso es lo que la fecha de
siembra permitiría calcular.

## 6. Preguntas abiertas para Vanessa

1. **Inv 3C pequeña**: `capacidad_bloques.csv` dice 90 huecos (16,2 m²) y
   `01-invernaderos.md` dice 12,6 m² (=70 huecos). 28,6 % de diferencia.
2. **Número de camas de Inv 3A y Inv 3B** — hay área por cama pero no cuántas hay,
   así que esos dos bloques no suman al total (hoy 1.857 m² de los conocidos).
3. **Las 7 ramas con trabajo fuera de `main`** — ver abajo.

## 7. Ramas con trabajo que NO está en `main`

Auditadas el 2026-09-10. `main` quedó consolidado con la rama de cartera y la de
esta sesión; estas siguen sueltas:

| Rama | Último | Archivos únicos | Qué trae |
|---|---|---|---|
| `harvest-gaps-analysis-1cofhy` | 09-03 | 11 | **`motor/calibrar_rendimiento.py`**, proyección de cosecha calibrada contra registro real, huecos sem 36 |
| `dcb-planning-system-wvnda6` | 09-01 | 8 | **`cerebro.py m2` y `13-optimizacion/06-tallos-por-m2.md`** — la fórmula de área correcta, análisis de suelo de agosto |
| `continue-previous-session-k4ye92` | 08-28 | 6 | hueco de registro 13–24 ago, costos de follaje comprado, problemas fisiológicos |
| `trench-operarios-archivo-k2gpwc` | 09-08 | 4 | trench de inoculación presiembra + hojas de operario en PDF |
| `planificador-siembras-huecos-wef7z5` | 09-03 | 4 | huecos de cosecha, proyección sem 38, `mortalidad_siembras.csv` |
| `nice-wozniak-t2vopo` | 09-09 | 1 | plantulación propia sem 37 |
| `dahlia-cultivation-protocol-xu4vzd` | 09-09 | 1 | protocolo de las 160 dahlias italianas |

`dreams-camp-bloom-drive-access-ov6t34`, `campanula-lavender-decision` y
`registro-de-tallos-gouhsr` **no tienen archivos únicos**: nada que perder.

**La más urgente es `dcb-planning-system-wvnda6`**: tiene `cerebro.py m2`, que es
la herramienta que esta sesión reconstruyó sin saber que existía. Traerla evita
que vuelva a pasar.

## 8. Lo siguiente

1. Importar las semanas ISO 33–37 (la operaria las estaba subiendo a Drive).
2. Vanessa sube los tallos vendidos por mes.
3. Decidir qué hacer con las 7 ramas — al menos traer `m2` y
   `calibrar_rendimiento.py`.
4. Llenar `Fecha siembra campo`. Es la columna que desbloquea el eje central.
