---
name: dcb-variedades
description: Comportamiento agronómico por variedad en Dreams Can Bloom (DCB) — mejor zona de siembra por invernadero/bloque, problemas conocidos, densidad de siembra, comportamiento estacional, y notas de campo acumuladas por variedad. Usar esta skill SIEMPRE que Vanessa pregunte dónde sembrar una variedad, por qué una variedad está fallando en una zona, cómo se ha comportado históricamente algo, densidad o distancia de siembra, o quiera registrar una observación de campo nueva sobre una variedad (éxito, fracaso, comportamiento raro). También usar para decidir en qué bloque/cama poner una siembra nueva antes de que eso pase a DCB Programación para el registro formal. NO usar para nombres homologados, columna N, VARIEDADES_BITACORA, o el calendario de Erica — eso es exclusivamente DCB Programación, no mezclar. NO usar para diseño de bombas fitosanitarias o rotación de productos — eso es DCB Fitosanidad.
---

# DCB Variedades

Esta skill enseña el comportamiento agronómico conocido de cada variedad en el cultivo — no la programación de siembras (eso es DCB Programación) ni el manejo fitosanitario (eso es DCB Fitosanidad). Es la memoria de campo: qué funciona dónde, qué ha fallado, y por qué.

## Límite claro con las otras skills

- **DCB Programación** es dueña de: nombres homologados, columna N, VARIEDADES_BITACORA, EXPORT_CALENDARIO, ciclos y ventanas de cosecha para el calendario de clientes.
- **DCB Fitosanidad** es dueña de: diseño de bombas, rotación de productos, horarios de aplicación.
- **DCB Variedades** es dueña de: dónde sembrar, por qué algo funciona o no en una zona, densidad, comportamiento estacional, notas de campo acumuladas.

Si una conversación mezcla las tres (ej. "voy a sembrar X, dime dónde y cómo se llama homologado y qué bomba necesita"), usar cada skill para su parte — no inventar el nombre homologado aquí, ni recomendar productos aquí.

## Arquitectura de invernaderos (contexto físico de referencia)

Área total ~3.022 m² — bajo invernadero ~2.406 m², exterior ~616 m². Zonas:

| Zona | Estado | Limitante principal |
|---|---|---|
| Inv4 completo | Alta productividad | Ninguna — es la referencia del cultivo |
| Inv3A + Inv3C | Media productividad | Manejable con manejo agronómico |
| Inv3B + Inv5 + Mini | Problemática | Presión de agua insuficiente |
| Inv1 + Inv2 | Uso especial | Estrategia pendiente de definir |
| Exterior + Inv6 | Variable | Maleza — se resuelve con mulch plástico |

Gradientes conocidos dentro de invernaderos:
- **Inv3A:** camas superiores = más calor y menos agua (no aptas para variedades exigentes en agua — Dianthus fracasó ahí); camas inferiores = más frescas y húmedas (larkspur, gomphrena exitosos).
- **Inv3B:** doble limitante — suelo degradado por erosión histórica + presión de agua insuficiente. El bloque más problemático del cultivo.
- **Inv3C:** perfil fresco, húmedo, menos radiación, pegado al humedal — bueno para nigela, anémonas, Dianthus Green Ball; malo para matricaria y bocas de dragón (necesitan más sol).
- **Inv4:** camas cortas (112 huecos x 8) = presión de agua uniforme = riego homogéneo. Por eso es el bloque más exitoso.
- **Inv5:** menor capacidad de tanque y menor presión — la peor presión del sistema. Trachelium y matricaria se quedan vegetativos sin florar por estrés hídrico ahí.

## Mapa de variedades — comportamiento conocido

Ver `references/mapa_variedades.md` para la tabla completa (variedad, resultado, mejor zona, notas clave). Consultar esa tabla antes de recomendar dónde sembrar algo nuevo o de diagnosticar por qué algo está fallando.

## Parámetros de siembra por variedad

Ver `references/parametros_siembra.md` para semanas de germinación, semanas a campo, ventana, distancia de siembra y tallos por planta de las variedades principales. **Regla dura: estos números son de referencia agronómica de campo — no confundir con "ciclo" y "ventana de cosecha" de VARIEDADES_BITACORA, que son los que alimentan el calendario de clientes y viven en DCB Programación.** Si hay una discrepancia entre esta tabla y la BITACORA, señalarla — no asumir cuál tiene razón.

## Reglas agronómicas establecidas

Ver `references/reglas_agronomicas.md` para las reglas específicas ya confirmadas en campo (ej. Dusty Miller nunca debe florar, ventana de Botrytis en statice, timing de malla en bocas de dragón, protocolo de remoción de lisianthus enfermo, etc.). Estas reglas se tratan como hechos establecidos, no como sugerencias — no contradecirlas sin que Vanessa lo indique explícitamente con nueva evidencia de campo.

## Comportamiento estacional

- **Sep–Nov** (nuboso/lluvioso): ciclos más largos, más presión de hongos por humedad nocturna alta.
- **Dic–Feb** (verano/más luz): ciclos más cortos, más calor favorece inducción floral en celosia cristata.
- **Mar–May**: época de referencia — comportamiento base de la mayoría de parámetros documentados.
- Variedades sensibles al frío (larkspur) prefieren zonas frescas; variedades que necesitan calor para inducción floral (celosia cristata) rinden mejor en zonas altas/calientes como Inv2 zona alta o Inv5 con calor.

## Notas de campo acumuladas

Ver `references/notas_campo.md`. Cada vez que Vanessa reporte una observación de campo nueva sobre una variedad (algo que no estaba documentado, un fracaso o éxito inesperado, un cambio de comportamiento), Claude debe:
1. Preguntar solo si la variedad/zona es ambigua — si está clara, registrar directo.
2. Agregar una entrada fechada a `references/notas_campo.md` con: variedad, zona, observación, fecha.
3. **Revisar si esa misma observación (misma variedad + misma zona + mismo tipo de comportamiento) ya aparece registrada antes en el log.** Si es la segunda vez (o más) que se reporta el mismo patrón, promoverla automáticamente a `references/reglas_agronomicas.md` como regla establecida — no hace falta que Vanessa lo pida ni lo confirme explícitamente. Un patrón que se repite dos veces en campo ya es una regla, no una casualidad. Avisar que se hizo la promoción ("esto ya es la segunda vez que se ve X en Y — lo agregué a reglas establecidas") en vez de preguntar si se debe hacer.
4. Si la observación nueva CONTRADICE una regla ya establecida (no la confirma, la contradice), ahí sí detenerse y preguntar — eso sí necesita juicio de Vanessa antes de tocar la regla existente.

El criterio es: repetición del mismo patrón = promoción automática. Contradicción de algo ya establecido = pausa y pregunta.

## Vigencia con investigación externa

En sesiones de diagnóstico o decisión agronómica (no en consultas triviales), buscar en la web desarrollos recientes relevantes de floricultura orgánica, nutrición vegetal (framework Kempf) y manejo de suelo — no depender solo del conocimiento de entrenamiento. Esto aplica sobre todo cuando el problema reportado no tiene una regla ya establecida en las referencias de esta skill.

## Reglas duras

- Nunca inventar un comportamiento agronómico que no esté en las referencias ni haya sido confirmado por Vanessa. Si no hay dato, decirlo y preguntar.
- Nunca tocar nombres homologados, columna N, ni VARIEDADES_BITACORA desde esta skill — eso es DCB Programación.
- Nunca diseñar ni recomendar bombas o rotación de productos desde esta skill — eso es DCB Fitosanidad.
- Toda observación de campo nueva se registra con fecha en `references/notas_campo.md`, nunca se pierde en la conversación.
