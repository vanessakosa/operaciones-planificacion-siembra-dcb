# Qué falta en la arquitectura — para revisar con David

> Escrito el 2026-08-13. **Recomendación de fondo: un solo repositorio, no dos.**
> Cada error encontrado hoy nació en una frontera entre sistemas
> (`Inv5` vs `Inv 5`, `Boca de Dragón` vs `Snapdragon`, la hoja de Drive contra
> el espejo del repo). Partir en dos crea una frontera nueva y permanente.
> Los especialistas ya existen y son las **skills** de `.claude/skills/`: separan
> la mirada sin separar el dato.

---

## Lo que no se puede responder hoy, y por qué

| Pregunta del negocio | Bloqueada por | Quién lo resuelve |
|---|---|---|
| ¿Qué variedad deja más margen? | `costos_productos.csv` vacío · pestaña RENDIMIENTO vacía | **Vanessa** (dato) |
| ¿Qué variedad da tallo vendible? | `calidad_tallo.csv` vacío | **Vanessa** (medición) |
| ¿Qué producto rota más rápido? | no existe archivo de ventas | **Vanessa** (fuente nueva) |
| ¿Qué se devuelve y por qué? | solo frases en comentarios | **Vanessa** (fuente nueva) |
| ¿Qué diseño se vende mejor? | no existe | **Vanessa** (fuente nueva) |
| ¿Qué se aplicó desde la sem 28? | APLICACIONES no se puede exportar | **David** (plomería) |
| ¿Qué dice la bitácora hoy? | PROGRAMACION pesa 11,5 MB | **David** (plomería) |

**Cuatro de siete son datos que nadie captura todavía. Tres son plomería.**

---

## A · Lo que David puede construir

### A1. Lectura y escritura sobre `PROGRAMACION_2026` — el bloqueo mayor

**El problema:** el libro pesa 11,5 MB. Drive responde `File too large for
export` y la lectura en texto **trunca sin avisar** (devolvió 204 KB de 11,5 MB).
El conector de Drive **no tiene herramienta para escribir en celdas.**

Consecuencia hoy: no se puede leer `APLICACIONES` —lo que bloquea todo el
programa fitosanitario— ni verificar la bitácora, ni escribir nada.

**Solución propuesta: n8n como puente bidireccional.**

```
LECTURA:    Claude → webhook n8n → n8n lee la hoja → JSON de vuelta
ESCRITURA:  Claude → webhook n8n → n8n escribe la celda → confirmación
```

Credenciales de Google **solo en n8n**, nunca en el repo. n8n deja registro de
cada ejecución, así que queda auditoría.

Necesita: URL alcanzable desde el entorno de Claude · credencial de Google en
n8n (cuenta de servicio con la hoja compartida) · token compartido para que los
webhooks no queden abiertos.

**Salvaguarda que conviene exigir:** Claude escribe libre en pestañas derivadas
(`EXPORT_CALENDARIO`, columnas calculadas), pero **en las columnas que llena
Vanessa solo con confirmación previa**, mostrando celda y valor antes de
escribir. Toda escritura se registra en el repo. Si no, quedan **dos escritores
sobre una fuente primaria** — y el error del año `2056` fue con un solo escritor.

**Alternativa más barata si n8n se complica:** un Apps Script en el libro que
exporte `APLICACIONES`, `CAMPO` y `VARIEDADES_BITACORA` a un archivo liviano
aparte. Resuelve la lectura, no la escritura.

### A2. Refresco automático del registro de tallos

Hoy es manual: bajar el XLSX y correr `motor/importar_tallos.py`. Funciona bien y
es idempotente. Automatizarlo es cómodo pero **no es prioridad** — el bloqueo
real es A1.

### A3. Deuda técnica del motor

- `cerebro.py matriz` calcula la variable 8 con un cruce **distinto** al de
  `rendimiento`. Da 20 % contra 57 %. Hay que unificarlos.
- No existe un comando de vista por variedad que junte cosecha, ciclo, cierres,
  fitosanidad y comentarios. Hoy se arma a mano.
- El cálculo de margen no existe porque no hay costos.

---

## B · Lo que solo Vanessa puede capturar

Ordenado por retorno.

### B1. Cultivar en el registro de cosecha — **el más grande**

**41 % de la cosecha no se puede atribuir a una variedad.** Cuatro grupos
completamente ciegos: Statice (6 % trazable), Lisianthus, Zinnia y Strawflower
(0 %). Son **23.155 tallos**.

Sin esto **no se puede decidir qué variedad eliminar** en cuatro de los seis
grupos más grandes.

En Celosia se encontró la causa: `listas_desplegables.csv` ofrece **una sola
opción** para ese grupo. Hay que revisar si pasa lo mismo en los otros cuatro.

> Con el matiz aprendido: a veces `Mix` es correcto, cuando la cama está
> intercalada. La pregunta por grupo es **¿el cultivar es separable en esa cama?**

### B2. Costos — desbloquea todo el eje de rentabilidad

`costos_productos.csv` vacío y la pestaña `RENDIMIENTO` vacía en la fuente. Sin
área en m², costo de semilla y costo de insumos **no hay margen por m² por semana
de cama ocupada**, que es el eje que el `CLAUDE.md` define como el que une
calidad, rentabilidad y recursos.

Hoy el sistema cuenta tallos. Con esto, decide plata.

### B3. Longitud y grado de tallo

`calidad_tallo.csv` vacío. Es la diferencia entre *"produjo"* y *"produjo
vendible"*. Sin esto no se puede cuantificar el daño de una inducción floral ni
decidir si un lote merece seguir ocupando cama. La decisión del ensayo Dusty
Miller (semana 35) se va a tomar a ojo si no se mide.

### B4. Ventas y devoluciones — la mitad que no existe

**No hay ningún archivo de ventas ni de devoluciones.** Lo que se sabe está en
frases sueltas dentro de comentarios de campo:

> *"muchas devoluciones y pérdidas en carritos"* · *"se despetalaban en el
> carrito"* · *"no tengo a quién vendérselo"* · *"más de lo que se puede vender"*

Mínimo necesario para que el lado planificador exista: **qué producto, qué
semana, cuántos, cuánto se devolvió y por qué.** Sin eso, un "planificador" no
tiene con qué planificar — y por eso hoy **no tiene sentido separarlo en otro
proyecto**.

### B5. Cierre de cama

**0 de 697 filas** del registro tienen la columna `¿Cierre cama?` llena, y solo
39 de 302 siembras tienen `Fin de cosecha`. Hoy el cierre se infiere de "dejó de
aparecer", que confunde tres cosas distintas: cerró, pausó, o nadie registró.

Es **una palabra por cama** y arregla la medición de ventana de todo el sistema.

### B6. Microclima y clima semanal

`microclima_bloques.csv` en cualitativo (0/18 zonas con números) y
`clima_semanal.csv` vacío. Son las variables 3 y 7 de la matriz de decisión.
Sin ellas no se puede separar el efecto de temporada del efecto de variedad.

---

## Orden recomendado

| # | Qué | Quién | Desbloquea |
|---|---|---|---|
| 1 | Puente n8n de lectura | David | Programa fitosanitario completo |
| 2 | Cultivar en Statice, Lisianthus, Zinnia, Strawflower | Vanessa | Selección de variedades |
| 3 | Costos | Vanessa | Margen por m² por semana |
| 4 | Cierre de cama | Vanessa | Ventana real de todo el sistema |
| 5 | Longitud de tallo | Vanessa | Calidad vendible |
| 6 | Puente n8n de escritura | David | Dictado directo a la hoja |
| 7 | Ventas y devoluciones | Vanessa | El lado planificador |

**Los puntos 2 a 5 no necesitan que David construya nada.** Son captura, y son
los de mayor retorno.
