---
name: dcb-bomba-semanal
description: La sesión semanal de diseño de bomba fitosanitaria de Dreams Can Bloom, que además deja el registro conectado a la ficha de cada cosecha. Usar SIEMPRE que Vanessa diga "diseñá la bomba de esta semana", pregunte qué aplicar, reporte un foco de oidio/botrytis/plaga y quiera decidir la mezcla, o pida registrar una aplicación ya hecha. Esta skill es el procedimiento de ESCRITURA — dcb-fitosanidad tiene el criterio agronómico y el inventario; ésta tiene el orden obligatorio de pasos y el registro por bloque que permite imputar la aplicación a las cosechas que estaban sembradas esa semana. NO usar para decidir dónde sembrar (dcb-variedades) ni para recetas de bouquet (dcb-bouquets).
---

# La bomba de la semana

Existe para que **ninguna aplicación se pierda**: toda bomba que se registre con
su bloque se le suma sola a la ficha de las cosechas que estaban ahí esa semana.
Arquitectura completa en `08-roadmap/06-arquitectura-ficha-cohorte.md`.

## El orden es obligatorio

### 1. Mirar antes de proponer

```bash
python3 motor/bomba.py semana <N>
```

Esto **no es opcional** — es la regla APLICACIONES de `CLAUDE.md` hecha comando.
Imprime la rotación de las 4 semanas anteriores, qué cosechas hay en cada bloque,
y la incidencia conocida de esos bloques.

**Si no hay registro de las semanas anteriores, decirlo y no recomendar
rotación.** No inventar contra qué se está rotando, ni siquiera si Vanessa dice
"hazlo de memoria".

### 2. Diseñar

El criterio agronómico y el inventario están en la skill `dcb-fitosanidad`.
Las bombas ya documentadas con dosis salen de:

```bash
python3 motor/bomba.py catalogo
```

Reglas que no se negocian:

- **Ningún producto sin ficha técnica confirmada.** Si falta, se escribe
  `SIN FICHA — NO USAR EN FORMULACIÓN`. La lista de los que sí la tienen está en
  `03-fitosanidad/01-reglas-y-protocolos.md`.
- Dosis **por tanque de 25 L**. Una aspersión completa de lisianthus son
  **4 tanques**; para otras variedades hay que preguntar, no asumir.
- Si la mezcla es nueva, entra primero a `bombas_catalogo.csv` con su
  `vigencia_desde`, y sólo después se registra la aplicación.

### 3. Registrar

```bash
python3 motor/bomba.py registrar <fecha> <semana> "<bloques>" <bomba_id> <tanques> <operario> "<motivo>"
```

**El bloque es lo único que no puede faltar.** Sin bloque la fila queda huérfana
y no le suma a ninguna ficha — aparece en la sección 9 bajo `NO SE PUDO IMPUTAR`.

El comando dice, al terminar, a qué cosechas se les acaba de sumar. **Leer esa
línea y reportarla**: si sale vacía, falta la cohorte en `ocupacion_lote.csv` y
hay que arreglarlo ahora, no después.

### 4. Cerrar

Confirmar a Vanessa en una tabla corta: bomba, bloques, tanques, a qué cosechas
se imputó, y qué quedó pendiente. Después `git commit` y `git push`.

## Cuando el dato no alcanza

Decirlo y pedirlo. Un `SIN_DATO` explícito vale más que un número plausible:
una bomba mal atribuida ensucia la ficha de dos cosechas a la vez — la que la
recibió y la que no.
