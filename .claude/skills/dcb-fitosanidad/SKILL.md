---
name: dcb-fitosanidad
description: "Diseño de bombas fitosanitarias, rotación de productos, y manejo de enfermedades/plagas en Dreams Can Bloom (DCB) — Botrytis, Fusarium, mildeos, trips, pulgones. Usar esta skill SIEMPRE que Vanessa pida diseñar o recomendar una bomba (mezcla de tanque), pregunte qué aplicar esta semana, reporte un problema fitosanitario (lesiones, plagas, enfermedad activa), pida evaluar el inventario de insumos, o mencione rotación de productos, Botrycid, Equifun, Regalia, ADNGard, o cualquier fungicida/insecticida/bioestimulante del cultivo. CRÍTICO — antes de recomendar cualquier bomba, esta skill exige pedir el archivo APLICACIONES actualizado (hoja de DCB_Maestro_Campo_2026.xlsx); nunca recomendar rotación basándose en memoria o en una tabla estática. NO usar para decisiones de dónde sembrar o comportamiento agronómico general — eso es DCB Variedades. NO usar para nombres homologados o calendario — eso es DCB Programación."
---

# DCB Fitosanidad

Esta skill enseña las reglas fijas de manejo fitosanitario de DCB (horarios, incompatibilidades, estructura de rotación) — pero la recomendación específica de qué producto usar esta semana SIEMPRE depende del historial real de aplicaciones, no de una tabla memorizada.

## Regla no negociable: pedir APLICACIONES antes de recomendar

**Antes de diseñar o recomendar cualquier bomba, Claude debe pedir el archivo o los datos actualizados de la hoja APLICACIONES de `DCB_Maestro_Campo_2026.xlsx`** (una fila por producto por bomba, con fecha y bloque/cama). Si Vanessa no lo ha subido en la sesión, Claude se detiene y lo pide explícitamente — no asume qué se aplicó la semana pasada, no recomienda "a ciegas", y no rellena con la última rotación que recuerde de una conversación anterior.

**Esta regla es absolutamente no negociable — ni siquiera si Vanessa dice explícitamente "hazlo de memoria" o "no tengo el archivo a mano, recomienda igual".** En ese caso, Claude explica por qué no puede: una rotación sin historial real puede repetir un producto recién aplicado (rompiendo la disciplina anti-resistencia) o saltarse una alerta activa que el historial mostraría. Una rotación mal fundamentada es peor que no dar rotación — el riesgo de resistencia y de daño al cultivo es real y no se compensa con la urgencia de la conversación. Claude puede ofrecer alternativas útiles mientras tanto (explicar la estructura odd/even en abstracto, recordar las reglas fijas de horario/limpieza física, o ayudar a Vanessa a ubicar o exportar el archivo APLICACIONES), pero no debe emitir una recomendación de bomba concreta sin el historial.

Excepción real (no una forma de saltarse la regla): si Vanessa dicta explícitamente en la sesión qué se aplicó y cuándo, bloque por bloque ("la semana pasada usamos Botrycid + Equifun en 3B, nada en 3C, Regalia en 4"), eso cuenta como historial confirmado para esa conversación — porque sigue siendo información real, solo que dictada en vez de leída del archivo. Lo que nunca es aceptable es proceder sin ningún historial, ni real ni dictado.

Antes de presentar cualquier recomendación de bomba, Claude presenta primero una tabla de historial reciente relevante (bloque, producto, fecha de última aplicación) — así Vanessa puede verificar que la lectura del historial es correcta antes de que Claude proponga la rotación.

## Reglas fijas (siempre aplican, sin importar el historial)

Ver `references/reglas_fijas.md` para el detalle completo. Resumen:

- **Horario de fungicidas: SIEMPRE 3-4pm, NUNCA en la mañana.** A las 7-8am el tejido lleva toda la noche húmedo y las esporas ya penetraron; a las 3-4pm el tejido está seco y el producto actúa justo antes de la ventana de infección nocturna.
- **Limpieza física primero:** antes de cualquier fungicida en un brote activo, retirar manualmente el tejido afectado en bolsas fuera del invernadero. Sin esto, los fungicidas no pueden con Botrytis ya establecida.
- **Fertirriego no se suspende por problema fúngico:** las plantas bajo presión fúngica necesitan nutrición para defenderse — suspenderlo las hace más vulnerables, no menos.
- **Estructura de cuatro componentes por bomba:** toda bomba debe incluir fungicida + insecticida + bioestimulante + nutricional — sin importar si hay o no una presión específica detectada, esa es la estructura base.
- **Disciplina de rotación:** nunca re-recomendar un producto aplicado en la aplicación inmediatamente anterior en ese bloque, sin señalarlo explícitamente. Esto es lo que hace obligatorio revisar APLICACIONES primero.

## Estructura de rotación odd/even (el patrón, no el dato)

DCB rota entre semanas impares y pares para evitar resistencia. La estructura de combinaciones vive en `references/estructura_rotacion.md` — pero **cuál de las dos combinaciones toca esta semana, y si algún producto de esa combinación ya se aplicó recientemente en ese bloque específico, se decide siempre contra el historial real de APLICACIONES, nunca contra la estructura sola.** La estructura dice qué combinaciones existen; el historial dice cuál usar hoy.

## Ventanas de enfermedad conocidas (para prevención, no para diagnóstico retroactivo)

- **Botrytis en Statice:** ventana consistente semanas 16-21 de cosecha, sin importar variedad. Aplicar preventivo desde semana 14-15, antes de síntomas visibles.
- **Fusarium en suelo:** condición base del terreno desde el inicio, no contaminación puntual. Estrategia es biosupresión (diversidad microbiana), no eliminación — ver inoculantes en `references/reglas_fijas.md`.

Estas ventanas informan CUÁNDO anticipar un problema, pero el producto específico a aplicar sigue dependiendo del historial real.

## Redundancias e inventario

Ver `references/redundancias.md` — productos que se solapan en función y no deben mantenerse ambos en bodega/plan (ej. ajo-ají, Beauveria mix, exceso de productos anti-Botrytis). Si Vanessa pregunta por inventario o pide simplificar el stock, usar esta referencia como punto de partida, pero confirmar contra el stock real si está disponible — el inventario documentado tiene fecha y puede estar desactualizado.

## Vigencia con investigación externa

En sesiones de diagnóstico fitosanitario, buscar en la web desarrollos recientes de manejo fitosanitario orgánico, resistencia a fungicidas biológicos, y nutrición defensiva (framework Kempf) — no depender solo de conocimiento de entrenamiento, especialmente para problemas que no calzan con las reglas ya documentadas aquí.

## Reglas duras

- Nunca recomendar una bomba sin haber pedido y revisado (o recibido dictado explícito de) el historial real de APLICACIONES.
- Nunca re-recomendar un producto aplicado en la rotación inmediatamente anterior sin señalarlo.
- Nunca mover el horario de fungicida fuera de 3-4pm, ni sugerir suspender fertirriego por presión fúngica.
- Toda bomba recomendada debe tener los cuatro componentes (fungicida, insecticida, bioestimulante, nutricional) o justificar explícitamente por qué se omite alguno.
- No decidir dónde sembrar ni comportamiento agronómico general aquí — eso es DCB Variedades. No tocar nombres homologados ni calendario — eso es DCB Programación.
