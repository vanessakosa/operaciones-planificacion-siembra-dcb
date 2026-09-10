# La estrategia de surtido — la premisa que ordena la cartera

```bash
python3 motor/cerebro.py cartera     # ahora agrupada por rol de cartera
```

Dictada por Vanessa el 2026-09-10, corrigiendo un error de marco del análisis de
cartera. Es la premisa que faltaba, y sin ella la tabla de cartera compara cosas
que **no compiten entre sí**.

> *"Yo no siembro todo, todo el tiempo."*

## Los tres niveles

`07-datos/roles_cartera.csv` guarda el rol de cada grupo. No son etiquetas
descriptivas: cada nivel se juzga con una regla distinta.

### 1. BASE — siempre debe haber

**Boca de Dragón · Campánula · un encaje**

> *"Hay ciertas variedades como boca de dragón, campánula, un encaje que puede
> ser Ammi o Trachelium, que deberíamos tener siempre."*

Aquí un hueco **es una falla**. Y aquí sí aplica FALTA / SOBRA contra la demanda
del catálogo, porque la continuidad es el objetivo.

**El encaje es un rol, no una especie.** Ammi y Trachelium se sustituyen entre
sí. Eso resuelve algo que este repositorio había marcado como defecto: la receta
que dice *"Trachelium o Ammi"* con la nota *"sustitución: el que haya"* **no es
una receta indecisa** — está declarando el rol y dejando la especie abierta a
propósito. El motor la lee como `SUSTITUCION` y no le carga el tallo a ninguno de
los dos grupos.

### 2. FOCAL — siempre una flor principal

**Lisianthus preferido. Sustitutos: Dianthus · Marigold · Zinnia**

> *"Siempre debe haber una flor principal, ojalá un Lisianthus, o si no una flor
> similar que llene el bouquet como un Dianthus, o un Marigold, o una Zinnia."*

El rol **no puede quedar vacío**, pero se llena con cualquiera de las cuatro. La
pregunta correcta no es "cuánto Lisianthus hay" sino **"¿hay alguna focal?"**.

Consecuencia práctica: el `SOBRA +6,7 pp` de Lisianthus **no es un exceso a
recortar.** Es la focal del catálogo cumpliendo su función, con un ciclo de 19–23
semanas que hace que no se pueda improvisar.

### 3. TOQUE — rota a propósito

**Hoy: Colitas de conejo · Craspedia · Scabiosa Estrella**
**Siguiente en la rotación: Larkspur**
**En ensayo: Cynoglossum**

> *"La idea justamente es que no haya una cosecha siempre de lo mismo, para que
> cuando las personas vayan al carrito o vean nuestro catálogo se antojen porque
> tienen rato que no lo ven. Eso es lo que genera que la gente esté
> constantemente comprando."*

**Esto es estrategia de demanda, no de oferta.** El toque no existe para producir
volumen: existe para que el catálogo se vea distinto cada temporada. Por eso:

- **Poca cantidad**, y
- **en Inv 2**, nunca ocupando el área productiva de Inv 3, que es el mejor.

> *"Sembrar poca cantidad en el invernadero 2, como hicimos ahorita con las
> colitas y con las craspedias, como para generar un toque sin quitar el área
> productiva del invernadero 3."*

Y encaja con lo que ya estaba documentado de Inv 2: es **el invernadero más
irregular**, y por eso es donde se ensaya — *"no se quiere comprometer el espacio
de los otros, que es mucho más parejo"*.

**Medir un TOQUE por volumen contra la demanda del catálogo es un error de
categoría:** mide como fracaso lo que es una decisión. `cerebro.py cartera` ahora
reemplaza el veredicto de los toques por `rotativo (volumen no aplica)`.

#### El caso Larkspur, que es el que enseñó la regla

Larkspur es un toque: *"yo lo hago como para hacer un boost"*. Azul y rosado, los
dos secan bien y **hacen show** en Centro de mesa, Dream Big y Dreamland.

**Pero el lote real fueron 4.788 plantas en 3A** — un toque sembrado a escala de
producción, en el mejor bloque del cultivo. Es exactamente lo que la regla evita.
Compárese con los toques de hoy: Scabiosa Estrella 870, Cynoglossum 597,
Scabiosa Triple Berry 446, Craspedia 338 — **todos en Bloque 2.**

#### TOQUE_ENSAYO tiene fecha de salida

Cynoglossum ("el otro azul") está sembrado para probar. Ya se sabe que **para
fresco no sirve**; el ensayo de **seco** está en curso. La regla que Vanessa dictó
va con el nivel:

> *"Si esa prueba no funcionó, pues hay que sacar la cama."*

Un ensayo sin criterio de salida ocupa cama para siempre. Este lo tiene.

## Lo que este marco destapó de inmediato

**Los tres toques que están produciendo ahora no tienen un solo tallo en el
registro de cosecha.** Craspedia, Scabiosa Estrella y Cynoglossum tienen cosecha
abierta desde agosto en `campo_siembras.csv` y **cero filas** en
`registro_tallos.csv`.

Y la causa probable es mecánica: **ninguno de los tres está en la hoja LISTAS**,
así que no aparecen en el desplegable de la columna Grupo. Un grupo que no se
puede elegir es un grupo que no se registra.

O sea que **la pierna de la estrategia que genera la recompra es la única que no
se está midiendo.** `cerebro.py cartera` ahora lo reporta en su propia sección.

Agregarlos a LISTAS es la acción de menor esfuerzo y mayor efecto de toda esta
ficha — ver `05-programacion/07-desplegables-registro.md`.

## Lo que falta para cerrar el marco

**14 grupos siguen sin rol asignado**, y no se les asigna por deducción: Gomphrena
(el de mayor peso en el catálogo, 8 productos), Statice (10 productos), Green
Ball, Amaranto, Ammobium, Girasol, Strawflower, Celosia, Zinnia, Dusty Miller,
Dahlias, Matricaria, Espárrago, Limonium.

`cerebro.py cartera` los agrupa en `SIN_CLASIFICAR` con la nota
*"PREGUNTAR antes de juzgarlo"*, porque un grupo sin rol no se puede evaluar:
depende de si su trabajo es estar siempre o aparecer de vez en cuando.
