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

## Lo que NO se puede hacer todavía, y por qué

Pediste sacar también la ventana y las condiciones climáticas para hacer
predicciones certeras. Con el dato actual no se puede, por tres razones
independientes. Ninguna se arregla con más análisis: se arreglan cambiando
cómo se anota.

### 1. La ventana no existe en el dato

`Fin de cosecha` está lleno en **39 de 302 filas (13 %)**. Y filas con las tres
fechas — siembra, inicio y fin — hay exactamente **1 de 302**.

La ventana de cosecha **no es derivable**. Para Green Ball las tres siembras
tienen `Fin de cosecha` vacío.

### 2. El inicio de cosecha es un mes, no una fecha

Los 272 valores de `Inicio cosecha` son texto: `NOVIEMBRE`, `JULIO/AGOSTO`,
`ABRIL?`, `JUN-JUL`. Ninguno es una fecha.

Eso mete un **ruido de medición de 4.1 semanas** en cada ciclo calculado: si
la cosecha empezó "en noviembre", pudo ser el 1 o el 30.

### 3. El efecto de temporada es más chico que el ruido

| Temporada | n | Ciclo medio |
|---|---|---|
| SECA (dic–feb, jun–ago) | 35 | 13.8 sem |
| LLUVIA (mar–may, sep–nov) | 76 | 14.5 sem |

**Diferencia: 0.7 semanas. Ruido de medición: 4.1 semanas.**

El efecto que buscamos es **seis veces más pequeño que el error del
instrumento**. Con este dato no se puede afirmar que la temporada mueva el
ciclo — ni que no lo mueva. Simplemente no alcanza para saberlo.

### 4. Falta medio año

Todas las siembras con fecha caen entre **julio y diciembre de 2025**. Enero a
junio no tiene un solo registro fechado, y no hay un segundo año para comparar.

Cualquier "efecto de temporada" que calcule está midiendo, en realidad, **qué
variedades se sembraron en cada mes** — no el clima. Por eso septiembre sale en
16.7 semanas: no es que septiembre alargue el ciclo, es que en septiembre se
sembró Trachelium y Lisianthus, que son de ciclo largo.

**Ese es el error que hay que evitar.** El promedio por mes parece un dato
climático y es un artefacto de la mezcla de variedades.

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

Tres cambios en cómo se anota, en orden de impacto:

1. **`Inicio cosecha` como fecha, no como mes.** Solo esto baja el ruido de
   4.1 semanas a ~0.5 y hace visible cualquier efecto de temporada real.
2. **Llenar `Fin de cosecha`.** Sin esto la ventana no existe, y la ventana es
   lo que determina si hace falta escalonar siembras para no quedar
   monocromático en el punto de venta.
3. **`Fecha siembra campo` en todas las filas.** Hoy está en 37 %.

Con un año completo anotado así, el análisis por temporada pasa a ser válido —
y ahí sí conviene separar por variedad para no confundir clima con mezcla de
siembra.

**Mientras tanto: los ciclos son utilizables, la ventana y el clima no.** El
motor refleja exactamente eso — reporta lo que puede calcular y nombra lo que
falta, en vez de rellenarlo.
