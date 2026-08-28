# Cómo predecir ciclos — y por qué hoy todavía no se puede predecir por clima

```bash
python3 motor/cerebro.py ciclos
```

Deriva el ciclo real de trasplante a primera cosecha desde
`07-datos/campo_siembras.csv` (la hoja CAMPO), 302 siembras registradas.

## Lo que sí salió: Green Ball

Era el último grupo del catálogo sin ciclo. Se derivó de sus siembras reales:

| Siembra | Bloque | Inicio cosecha | Ciclo |
|---|---|---|---|
| 2025-08-28 | 3A y 4 | NOVIEMBRE | 9–13 sem |
| 2025-09-10 | 3c | DICIEMBRE | 12–16 sem |
| 2025-12-12 | 3B | MARZO | 11–16 sem |

**Punto medio 12.9 semanas.** Registrado como 11–15 en `ciclos_variedad.csv`
con fuente `campo_siembras.csv (derivado, n=3)`.

De paso: **Green Ball es un Dianthus.** El nombre homologado en CAMPO es
`Dianthus Green Ball`. No estaba escrito en ningún otro archivo.

Con esto **los 13 grupos del catálogo son planificables.** Lo único que le
falta a Green Ball es `tallos_planta`.

## Actualización 2026-08-14 — la fecha de siembra dejó de ser el cuello de botella

Esto de abajo se escribió cuando el ciclo solo se podía calcular con
`Fecha siembra campo`, llena en 37 % de las filas. Vanessa aclaró ese mismo
día: *"Fecha a siembra a campo está vacío porque dejé de usarla, ahora trabajo
solo con las semanas... la columna que sigue es la semana que se trasplantó...
eso lo hago porque a veces puede pasar que en esa semana se sembró en dos días
distintos, y proyectamos todo por semana. Ese dato sí está en todo."**

Comprobado: la columna `Semana` de trasplante (la que va justo al lado de
`Fecha siembra campo` — el archivo tiene dos columnas llamadas igual, y por
eso el lector genérico no la veía) está llena en **294 de 302 filas (97 %)**.
`cerebro.py ciclos` ahora la usa como fuente principal — toma el lunes de esa
semana ISO como fecha estimada — y la fecha exacta queda de respaldo para las
pocas filas que todavía la traen.

**Resultado: el ciclo calculable pasó de 111 a 258 filas — de 37 % a 85 %.**
Y el punto 4 de abajo ("falta medio año") queda resuelto: los 258 casos ya
cubren los 12 meses del año.

## Lo que NO se puede hacer todavía, y por qué

Pediste sacar también la ventana y las condiciones climáticas para hacer
predicciones certeras. Con el dato actual todavía no se puede, por dos
razones que la fecha de siembra no arregla — se arreglan cambiando cómo se
anota la COSECHA, no la siembra.

### 1. La ventana no existe en el dato

`Fin de cosecha` está lleno en **39 de 302 filas (13 %)**. Y filas con las tres
fechas — siembra, inicio y fin — hay exactamente **1 de 302**.

La ventana de cosecha **no es derivable**. Para Green Ball las tres siembras
tienen `Fin de cosecha` vacío.

### 2. El inicio de cosecha es un mes, no una fecha

Los 272 valores de `Inicio cosecha` son texto: `NOVIEMBRE`, `JULIO/AGOSTO`,
`ABRIL?`, `JUN-JUL`. Ninguno es una fecha.

Eso mete un **ruido de medición de ~4.2 semanas** en cada ciclo calculado: si
la cosecha empezó "en noviembre", pudo ser el 1 o el 30.

### 3. El efecto de temporada, con 258 filas, ya es medible — y sigue por debajo del ruido

| Temporada | n | Ciclo medio |
|---|---|---|
| SECA (dic–feb, jun–ago) | 84 | 13.4 sem |
| LLUVIA (mar–may, sep–nov) | 174 | 15.4 sem |

**Diferencia: 2.0 semanas. Ruido de medición: 4.2 semanas.**

Con 111 filas la diferencia era 0.7 sem — casi invisible. Con 258 subió a 2.0,
pero el ruido de anotar la cosecha por mes (no por fecha) sigue siendo el
doble. **Todavía no se puede afirmar que la temporada mueva el ciclo**, pero
la brecha con el ruido se cerró a la mitad. Es la razón #2 de arriba la que
falta cerrar ahora — el cuello de botella se movió de la siembra a la cosecha.

Antes también se sospechaba que "falta medio año" — todas las siembras con
fecha caían entre julio y diciembre de 2025. Con la semana de siembra como
fuente, los 258 casos **ya cubren los 12 meses**, así que ese problema quedó
resuelto. El que persiste es distinto: **qué variedades se sembraron en cada
mes sigue mezclado con el efecto de temporada**, porque `Inicio cosecha`
en mes no alcanza para separarlos con precisión.

## Lo que sí valida el ejercicio

Los ciclos derivados de CAMPO **corroboran la bitácora**, lo cual sube la
confianza en ella:

| Homologado | CAMPO (piso–techo) | Bitácora | ¿Coincide? |
|---|---|---|---|
| Campanula Pink | 10.2–14.4 | 12 | sí |
| Green Tails (Amaranto) | 9.1–13.3 | 10 | sí |
| Opus Fresh | — | 10 | sí (11.0 medio) |
| Statice Apricot | 13.7–17.8 | 15 | sí |
| Ammi | — | 12 | sí (13.3 medio) |
| Trachelium White | 14.8–19.1 | 15 | en el borde bajo |

Dos números de la bitácora quedan sospechosos y vale revisarlos:
**Dusty New Look 19.4–23.6 sem** (la bitácora dice 25 y la variedad está
descartada) y **Ammi Dara 18.5–22.7**, muy por encima del Ammi Majus.

## Qué cambiar para poder predecir de verdad

La siembra ya no es el problema. Quedan dos cambios en cómo se anota la
COSECHA, en orden de impacto:

1. **`Inicio cosecha` como fecha, no como mes.** Solo esto baja el ruido de
   ~4.2 semanas a ~0.5 y hace visible cualquier efecto de temporada real.
2. **Llenar `Fin de cosecha`.** Sin esto la ventana no existe, y la ventana es
   lo que determina si hace falta escalonar siembras para no quedar
   monocromático en el punto de venta.

Con un año completo anotado así, el análisis por temporada pasa a ser válido —
y ahí sí conviene separar por variedad para no confundir clima con mezcla de
siembra.

**Mientras tanto: los ciclos son utilizables, la ventana y el clima no.** El
motor refleja exactamente eso — reporta lo que puede calcular y nombra lo que
falta, en vez de rellenarlo.
