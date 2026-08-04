# Visión de la migración a Claude Code

## Por qué se migra

La limitación central identificada: **en el chat no hay escritura de vuelta a los archivos
reales.** Cada sesión termina con un archivo descargado que Vanessa sube a mano. Eso significa
que el sistema depende de ella para cada actualización, y que los datos de ventas, costos y
campo viven en silos que nunca se cruzan solos.

Claude Code resuelve tres cosas a la vez: **escritura directa a los archivos**, **acceso a todos
los departamentos en un solo lugar**, y **tareas que corren sin que Vanessa las pida.**

## Lo que Vanessa quiere que el sistema haga

Ordenado por dependencia técnica, no por deseo — cada nivel necesita el anterior.

### Nivel 0 — Desbloquear los datos (prerrequisito de todo)

Nada de lo demás funciona sin esto.

1. **Reconstruir las fórmulas de CONSOLIDADO y RENDIMIENTO.** Es la cadena
   `REGISTRO → CONSOLIDADO → RENDIMIENTO` que hoy está cortada
2. **Llenar `costos_productos.csv`** — precio por presentación y costo por cc/g de cada insumo
3. **Unificar el esquema de VARIEDADES_BITACORA** (hoy hay dos estructuras incompatibles
   circulando — es la causa raíz del bug de cicloMap vacío)
4. **Limpiar fechas y nombres de variedad** en las tres fuentes
5. Traer `DCB_Fitosanidad_Maestro.xlsx` al repositorio

### Nivel 1 — Automatizar lo que ya se hace a mano

6. **Actualización semanal de PROGRAMACION** desde el dictado, con escritura directa al archivo
7. **Generación de los tres PDF de operario** (drenches, bombas, tareas culturales) con la
   identidad visual aplicada, listos para WhatsApp los domingos
8. **Regenerar el calendario de Erica** sin intervención manual — eliminar los 6 pasos de export/import
9. **Revisar el registro de tallos continuamente** y avisar de inconsistencias
   (nombres huérfanos, fechas raras, lotes sin cierre) el mismo día, no tres meses después
10. **Reporte de lo que viene en campo:** qué entra en cosecha, qué ventanas de labor cultural
    se están por perder, qué bandejas llegan a fecha límite de trasplante

### Nivel 2 — Análisis que hoy no se puede hacer

11. **Rentabilidad por variedad:** tallos/m² real × precio de venta − costo agrícola − los 3
    parámetros. El objetivo es una tabla de MANTENER / REDUCIR / DESCARTAR generada con números,
    no con impresiones. El caso de Campanula Lavender (0.64 vs 0.92 tallos/planta) es el modelo
    a escalar a todas las variedades
12. **Cruzar programación con registro de tallos** para detectar patrones estacionales:
    ¿qué se sembró en qué semana y qué rindió de verdad, por época del año?
13. **Optimización de la fórmula nutricional:** cruzar fórmula aplicada × bloque × calidad de
    tallo cosechado. Hoy las fórmulas se ajustan por análisis de suelo y por marco teórico,
    pero nunca se han validado contra el tallo que salió
14. **Revisar y optimizar gastos de campo** — atribuir el gasto de insumos por bloque y por
    variedad, no como bolsa común
15. **Programar contra demanda estacional:** cruzar los picos de venta (Día de la Madre,
    Navidad, temporada de bodas) con los ciclos reales para sembrar hacia atrás desde la fecha
    de venta, no hacia adelante desde la fecha de siembra

### Nivel 3 — Predicción

16. Proyección de disponibilidad con ajuste estacional aplicado automáticamente
    (+1 a +2 sem en Sep–Nov, −1 sem en Dic–Feb)
17. Alerta preventiva de riesgo fitosanitario por combinación variedad × bloque × semana ×
    condición climática, basada en el historial acumulado
18. Predicción de rendimiento de una siembra nueva a partir del histórico de esa variedad en
    ese bloque

## Lo que NO debe cambiar en la migración

- **La regla APLICACIONES.** Ninguna automatización justifica recomendar una bomba sin historial real
- **Nunca inventar ciclos.** Un ciclo inventado corrompe el calendario que ve el cliente
- **Erica nunca ve datos históricos de cosecha en crudo**
- **Los PDF de operario siguen siendo solo cantidades.** Cero explicaciones
- **La validación de Vanessa** antes de escribir cambios dictados que no sean obvios
- La identidad visual

## Nota sobre los sistemas heredados

Dos cosas conviene rediseñar en lugar de portar tal cual:

- **La heurística `semana > 26 → año 2025`** tiene fecha de caducidad. Usar la fecha de siembra
  de la columna G, que ya existe en CAMPO, o una columna de año explícita
- **El descarte silencioso de siembras huérfanas** (`if (!datos) continue`) es lo que permitió
  que 278 de 311 siembras desaparecieran del calendario sin que nadie se enterara.
  Todo cruce debe reportar lo que no cruzó
