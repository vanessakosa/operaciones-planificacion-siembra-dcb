# Consolidación de fórmulas de fertirriego · inoculación · drench

> **Estado: PROPUESTA, PENDIENTE DE VALIDACIÓN DE VANESSA.** Nada de esto se ha aplicado a
> `01-fertirriego-formulas.md` ni a `03-drench-inoculacion.md`. Sesión 2026-09-02.
>
> **Dos decisiones abiertas** al cierre de la sesión, ver el final del documento.

## 1. Las fórmulas diferenciadas ya no se justifican

### Qué diferenciaba realmente las cuatro fórmulas

| Diferenciador | Inv 3 vs Inv 4+5 | Vegetativo vs Floración |
|---|---|---|
| **Polyfeed** | 250 vs 600 g | baja (250→150 / 600→400) |
| **Bitter Mag** | 400 vs 600 g | igual |
| Fullfert | 80 vs 100 cc | igual |
| N-Cal | igual | **1.200 → 1.400 g** |
| Haifa Micro | igual | igual |

> **La distinción entre invernaderos existía ÚNICAMENTE por el Polyfeed y el Bitter Mag.
> Al eliminar los dos, desaparece por completo.**

Y la distinción vegetativo/floración se reduce a **200 g más de nitrato de calcio** — un 17% en
un solo producto.

### Por qué esos 200 g no se justifican

La razón escrita en `01-fertirriego-formulas.md` es correcta en principio: *"el Ca es inmóvil en
la planta, necesita suministro continuo para el tejido floral."*

**Pero el calcio de DCB no es problema de suministro.** El Ca soluble sale **ALTO en los tres
bloques** (0,976 / 0,422 / 0,372 cmolc/kg). El cuello de botella es la **entrega por
transpiración** — 3C con humedad nocturna, 4B con pétalos separados, Inv 1 con mildeo.
Ver `04-diagnostico-kempf-ingham.md`.

**Subir el nitrato de calcio un 17% no mueve la transpiración**, y empuja más nitrato, que es
justo lo que hay que bajar (N-NO₃ en 64,4 mg/kg en Bloque 3).

### Propuesta: una sola fórmula base

| | Hoy | Propuesto |
|---|---|---|
| Fórmulas distintas | 4 (+1 Dusty Miller) | **1** |
| Productos por fórmula | 5 | **3** |
| **Números que el operario puede equivocar** | **20–25** | **3** |

No es solo simplicidad, es **reducción de riesgo operativo medible.**
`00-contexto/02-equipo-y-operarios.md` documenta que **Wilson subaplica** si no recibe el conteo
total de tanques, y que **Atilio detectó un error de copia en la fórmula de Floración de Inv 3.**
Con 20 números en juego ese error era cuestión de tiempo; con 3 casi no hay superficie de error.

**Fórmula base propuesta, tanque de 2.000 L, todos los bloques, todas las etapas:**

| Producto | Dosis |
|---|---|
| Nitrato de Calcio (Calcinit) | **1.200 g** |
| Borosol (20,5% B) | **12,3 g** |
| Amilsol Micro Cu 15 (15,0% Cu-EDTA) | **2,4 g** |

Costo: **$4.191/tanque**, contra $24.561–30.436 de las fórmulas actuales.

### Dónde va la diferenciación que se quita del fertirriego

**A la foliar** — que es lo que `01-fertirriego-formulas.md` ya declara como principio:
*"El ajuste fino por variedad se hace en la foliar, no en el fertirriego."* La propuesta es
cumplirlo.

| | Fertirriego | Foliar |
|---|---|---|
| Volumen | 2.000 L | **25 L — 80× menos** |
| Granularidad | bloque completo | unas camas |
| Velocidad de respuesta | semanas | **días** |
| Con plástico | por goteo, bien | **llega igual** |

**El cobre de Bloque 5 NO crea una segunda fórmula:** va como **corrección edáfica única**
(~400 g de Cu15 sobre las 13 camas de Inv 5), no como cambio de tanque. Corregir suelo necesita
masa, no concentración.

## 2. Inoculación inicial — costo/beneficio

**Precios faltantes:** Fitoderma, Estabios, Promobac, Raizal, Pokonia, TerraLife y Endhoriza
**no están en la lista de Alma Agrícola.** Solo aparece Safer Micorrizas ($3.272/kg). Hace falta
pedirlos al proveedor de biológicos para cerrar el costo por m².

Pero el juicio de costo/beneficio no depende del precio: depende de **si el producto agrega algo
que el suelo no tenga ya.** Y el dato duro es que **el Trichoderma está en 1,4×10⁶ UFC/g**
(subió 127× en 15 meses).

| Producto | Qué aporta | Veredicto |
|---|---|---|
| **Estabios** (Azotobacter + Pseudomonas) | PGPR y **solubilización de fosfatos** | ✅ **MANTENER y candidato a SUBIR.** El único que ataca directamente el P soluble bajo — el cuello de botella del andisol |
| **Promobac** (Bacillus mix) | PGPR, género distinto | ✅ Mantener — no redundante con Trichoderma |
| **TerraLife** | Biología superficial | ✅ Mantener |
| **Pokonia** (Trichoderma harzianum, drench **mensual**) | Trichoderma | 🔴 **CUESTIONAR.** Trichoderma mensual sobre un suelo con 1,4×10⁶ UFC/g es alimentar una población ya alta |
| **Fitoderma** (Trichoderma + Bacillus) | Trichoderma | ✅ Ya restringido a Inv 3 por Fusarium activo — **ese razonamiento es correcto**, y es el mismo que aplica a Pokonia |
| **Micorrizas** (Endhoriza / Safer) | Colonización radicular | 🔴 **REDUCIR** — ya decidido. Razón nueva: **el P bajo FAVORECE la micorriza nativa** (el P alto la suprime). En camas con 4+ cosechas no aporta |

### El hallazgo de fondo

> **La plata se está yendo a bacterias y hongos que ya existen en el suelo. El grupo funcional
> que falta no se puede comprar.**

Faltan **protozoos y nematodos bacterívoros** — los depredadores que liberan N y P en la
rizosfera. Ningún inoculante comercial los trae; solo salen de un **compost aeróbico** y de su
extracto. Es la misma conclusión del análisis de P soluble, llegando por otro camino.

### Ensayo propuesto para el Pokonia

Suspender el Pokonia mensual en **la mitad de las camas de Inv 4** durante un ciclo, mantenerlo
en la otra mitad, y mandar dos muestras a Bioquirama al cierre. Si el Trichoderma no baja, es una
línea de costo eliminada con evidencia. **Inv 4 es el único bloque donde el ensayo es válido**,
por la uniformidad de riego.

## 3. El drench y el plástico — el problema estaba mal planteado

La cuenta intuitiva era 100 L (bomba de espalda) contra 2.000 L (tanque) = 20× más costo.
**Pero esas dos cifras no cubren la misma área.**

| | Volumen | Área | **L/m²** |
|---|---|---|---|
| Bomba de espalda, 1 cama de Inv 5 | 100 L | 31,7 m² | **3,2** |
| Tanque, Inv 5 completo | 2.000 L | 412 m² | **4,9** |
| Tanque, Inv 4 completo | 2.000 L | 677 m² | **3,0** |

> **El agua por m² es prácticamente la misma. El costo por m² no se multiplica por 20 — se
> mantiene.** Lo que se multiplica es el área: 13 camas en vez de 1.
>
> **El problema no es de volumen. Es de granularidad:** no se puede fertirrigar una sola cama.

### Y el plástico no rompió el drench: hizo obsoleta la bomba de espalda

La cinta de goteo está **debajo** del plástico, en la zona radicular — exactamente donde debe
llegar un inoculante. Un drench con bomba por encima del plástico siempre fue peor: parte se
evapora, parte escurre afuera, y lo que entra llega a la superficie, no a la raíz.

En marco Ingham: goteo bajo plástico, en suelo húmedo, con la humedad retenida por el mismo
plástico = **condiciones casi ideales para que el inoculante se establezca.**

### Las tres ventanas, en orden de valor

**1. PRE-SIEMBRA — aquí van el dinero y el diseño.**
Es la ventana de máximo valor, y resuelve el problema de granularidad: **es el único momento en
que se puede aplicar cama por cama, a la dosis que se quiera, sin depender del bloque.** La cama
está abierta, no hay plástico, se puede incorporar mecánicamente, y se coloniza antes de que
llegue el patógeno. Aquí van TerraLife, Estabios, Promobac, el Naturcomplet, y el drench
obligatorio de Beauveria/Paecilomyces para Matricaria Vegmo.

**2. PREFLORACIÓN vía tanque — sí se justifica.**
El costo por m² es comparable al drench viejo, y el bloque casi siempre se siembra en cohorte
(misma semana, misma etapa), así que tratar el bloque completo **es el objetivo correcto**, no un
desperdicio. **Mejor costo/beneficio en esta ventana: el Estabios**, por la solubilización de
fosfatos — coincide con la ventana de máxima demanda de P (formación de botón). Si hubiera que
escoger un solo producto para un drench de prefloración, es ese.

**3. EL "EMPUJÓN" A UNA CAMA ESTRESADA — esto es lo que genuinamente se perdió.**
Y el reemplazo **no es fertirriego** (2.000 L, granularidad de bloque): **es foliar.** 25 L por
bomba, llega a la planta sin importar el plástico, actúa en días, granularidad de pocas camas.
Tallos cortos, producción baja, planta estresada: se corrige más rápido por hoja que por raíz.

## Hoja de operario

Borrador en **`05-programacion/hojas-operario/fertirriego-formula-base.html`**, hecho con las
reglas de PDF de operario de `00-contexto/02-equipo-y-operarios.md`: Helvetica sin itálicas, solo
blanco/beige/negro, solo cantidades, cero explicaciones, ningún producto en dosis 0.

| Elemento | Razón operativa |
|---|---|
| Una sola tabla de tres productos | De 20–25 números a 3 |
| Casillas separadas "Pesado" y "Al tanque" | Pesar y echar son dos errores distintos |
| Orden de mezcla numerado | Es un *cómo*, no un *por qué* |
| **Tabla de tanques por bloque, en blanco** | **Para Wilson** — subaplica si no recibe el conteo total explícito. Vanessa la llena cada domingo |
| "Si la casilla está vacía, ese bloque no se riega" | Elimina la interpretación |
| Corrección de Cu de Inv 5 en caja sellada "UNA SOLA VEZ" | Única diferenciación por bloque que sobrevive; separada para que no se vuelva rutina |
| "NO agregar ningún otro producto" | El Fullfert a pH 12 precipitaría el calcio. No se explica en la hoja: se prohíbe |

**Los 400 g de Cu15 de Inv 5** salen de: 28,7 g de Cu teóricos × factor 2 de fijación ÷ 15% de
Cu = ~383 g, redondeado a 400 para que sea pesable.

## 🔴 Decisiones abiertas — pendientes de Vanessa

1. **La dosis base está puesta en 1.200 g de Calcinit, no 1.400.** Es la que tenía el vegetativo.
   Bajar el nitrato total va en la dirección de Fase 1 y el calcio no está limitado por
   suministro. **Alternativa: arrancar en 1.300 g como transición**, para no cambiar dos cosas a
   la vez. **Sin decidir.**
2. **El conteo de tanques por bloque está en blanco y no se puede llenar** — es el mismo dato
   pendiente de siempre (litros por m²). Si Alexander mide cuántos tanques le corren a cada
   invernadero por aplicación, se puede pre-llenar esa columna y cerrar el costo por m² por año.

## Datos que faltan para cerrar

- **Precios de Estabios, Promobac, Pokonia, TerraLife y Fitoderma** → costo por m² de cada
  ventana de inoculación
- **`aplicaciones_historial.csv` actualizado** (el disponible llega a la semana 33) → programa
  foliar, que ahora carga toda la diferenciación por variedad y etapa
- **Litros de tanque por m² por bloque** → conteo de tanques y costo por m² por año
