# Fitosanidad — reglas y protocolos

## LA REGLA QUE MANDA: nunca diseñar una bomba sin el historial de aplicaciones

**Antes de recomendar cualquier mezcla de tanque, hay que leer
`07-datos/aplicaciones_historial.csv` y mostrar la tabla de rotación de las últimas 3–4 semanas.**

Esto aplica **incluso si Vanessa dice explícitamente "hazlo de memoria"**. La razón no es
burocracia: recomendar sin historial genera repetición de modo de acción, que es exactamente
cómo se construye resistencia. Un error aquí no se ve esta semana — se ve en tres meses cuando
el Botrycid deja de funcionar.

Si el historial no está disponible, las alternativas son:
- Pedir el archivo actualizado
- Trabajar con la última versión disponible **declarando explícitamente hasta qué semana llega**
- Diseñar la estructura de la bomba (qué categorías) sin fijar los productos concretos

Lo que **no** se hace: producir una recomendación concreta sin historial real.

## Las 3 reglas de aplicación

1. **Fungicidas siempre 3–4 pm.** Nunca en la mañana. Ver `00-contexto/04-reglas-operativas-criticas.md`
2. **No suspender fertirriego** durante presión fúngica
3. **Limpieza física antes de cualquier fungicida** — tejido afectado en bolsas, fuera del invernadero

## Estructura íntegra de toda bomba

Cuatro componentes, siempre, haya o no problema activo:

| Componente | Función |
|---|---|
| **Fungicida** | Botrytis, mildeos |
| **Insecticida** | Trips, mosca blanca, pulgones |
| **Bioestimulante** | Metabolismo, resistencia a estrés |
| **Nutricional** | Corrección de déficits, pared celular |

Más surfactante cuando aplique (Neofat).

**Nunca repetir un producto aplicado en la sesión inmediatamente anterior** sin justificación
explícita escrita.

## Protocolo de rotación anti-Botrytis

Rotar entre dos combinaciones para evitar resistencia (dosis por bomba de 25 L):

| Semana | Combinación |
|---|---|
| **Impar — A** | Botrycid 38 cc + Equifun 100 cc + Neofat 12 cc |
| **Par — B** | Regalia 25 cc + Amicos MC 25 cc + ADNGard 12.5 g |

ADNGard (calcio + aminoácidos) se puede agregar a cualquiera de las dos — fortalece pared celular.

### ⚠️ Hallazgo importante sobre Botrycid

**La etiqueta de Botrycid especifica intervalos de 12 semanas entre aplicaciones.**
Se estaba aplicando semanalmente. Eso puede explicar la caída de eficacia observada:
sobreuso, no resistencia adquirida. **Revisar antes de volver a programarlo.**

## Bombas por etapa fenológica (estructura observada en el historial)

| Bomba | Destino | Composición típica |
|---|---|---|
| **Vegetativo** | < 6 semanas, inv 2/3/4/5 + ext | Naturmix-L 12.5cc + Equifun 100cc + Amicos MC 25cc + ADN Green 25cc + Neofat 12cc |
| **Prefloración + Floración** | 5–6+ semanas, todos los inv + jardín + ext | Glukoplant Ca-BZn 37.5cc + Starzyme 25cc + Regalia 25cc + Solar 50cc + No Fly 10g + Neofat 12cc |
| **Choque Botrytis+Oidio** (curativo) | Focos activos | Equifun 100cc + Hevea brasiliensis beta 50cc + Glukoplant Ca-BZn 37.5cc + ADNGard 12.5g + Neofat 12cc |

Dosis por 25 L. El historial completo está en `07-datos/aplicaciones_historial.csv`.

## Reglas específicas por variedad

| Variedad | Regla |
|---|---|
| **Bocas de dragón/snap, sem 5–8** | Glukoplant Ca-BZn obligatorio, **independientemente** de si la bomba general de prefloración lo incluye |
| **Statice en cosecha activa** | No retirar follaje viejo sin lesiones activas de Botrytis. Cambiar a Fórmula C (K más alto) al inicio de cosecha. Botrycid preventivo cada 10 días — **revisar contra el intervalo de etiqueta de 12 semanas** |
| **Matricaria Vegmo Single** | Drench pre-siembra obligatorio (Beauveria o Paecilomyces) + foliar post-trasplante. Nunca en Inv 5 ni 3C |
| **Matricaria Snowball** | Protocolo preventivo de mosca blanca semanas 6–8 y 10 |
| **Limonium sinensis (Diamond)** | **Evitar fungicidas cúpricos una vez aparece color en la flor** — decoloración permanente |
| **Limonium sinuatum (Wings / Forever Silver)** | Mismo perfil de susceptibilidad a Botrytis que el statice existente. La **remoción manual diaria de focos infectados es el control más efectivo** en condiciones de altiplano colombiano |
| **Glukoplant Ca-BZn** | Máximo 6 aplicaciones por ciclo |
| **Yodosafer** | NO usar en floración |

## Alerta activa registrada — Botrytis en lisianthus (mayo 2026)

Distribución **aleatoria entre camas = inóculo aéreo**, no fuente puntual. Esto cambia el
manejo: no hay foco que eliminar, hay que bajar la presión ambiental y subir la inmunidad
del tejido. Contribuyeron dos errores: aplicaciones en la mañana (inefectivas) y fertirriego
suspendido incorrectamente.

## Regla preventiva derivada de minería de patrones (sem 27)

En **Statice de cualquier serie** se estableció una regla preventiva a partir de 3 registros
históricos coincidentes. Ver `07-datos/decisiones_manejo.csv` para el texto exacto de la
decisión y su razón.

## Base de datos maestra de fitosanidad

Existe `DCB_Fitosanidad_Maestro.xlsx` con 8 hojas conectadas:
`INSUMOS · BUSCAR · ROTACION · REGISTRO · CONSUMO · INVENTARIO · GASTO_MENSUAL`

- INVENTARIO incluye costo por aplicación y alertas de vida en florero.
  Los productos biológicos tienen umbral de alerta más temprano (vida útil más corta).
- **Ningún producto entra sin ficha técnica confirmada.** Sin ficha → `SIN FICHA — NO USAR EN FORMULACIÓN`

**Con ficha confirmada (~18+):** Botrycid, Solar, Regalia, Azufral, Equifun, Timorex Gold,
Hevea brasiliensis beta, ADNGard, Safer Mix, BTK, Cincap, Alysin, No Fly, Tornado, Infinito,
Cantus, Revus, Deep Green (Metarhizium anisopliae), Pokonia, Nube SC, Biohar Forte.

**Pendientes de ficha:** Glukoplant Ca-BZn (parcial), Starz/Starzyme, y otros por confirmar.
Esta lista está incompleta — verificar contra el archivo maestro antes de formular.

> **Tarea de migración:** este archivo no está en el repositorio todavía.
> Hay que exportarlo a CSV y agregarlo a `07-datos/`.
