# Celosia — el grupo paraguas y sus tres subtipos

```bash
python3 motor/cerebro.py rendimiento Celosia
```

**`Celosia` es un paraguas correcto para reportar, pero la unidad de manejo es
el subtipo.** Lo confirmó Vanessa el 2026-08-13: *"Celosia es un grupo paraguas
correcto, pero deberíamos manejarlas cada una bien específicas — plumosas,
cristata, spicatas."*

No es una distinción cosmética. Los tres subtipos tienen densidad de siembra,
tallos por planta y rol en el bouquet **distintos**:

| Subtipo | Distancia | Tallos/planta | Rol típico |
|---|---|---|---|
| **cristata** (cresta) | 7,5 cm | **1** | FOCAL — la cabeza es la flor |
| **plumosa** (pluma) | 15 cm | **4** | TEXTURA |
| **spicata** (espiga) | — | — | TEXTURA |

Un error de subtipo no es un error de etiqueta: **cristata a 15 cm desperdicia
la mitad de la cama, y plumosa a 7,5 cm ahoga cuatro tallos por planta.**

## El mapeo — qué está confirmado y qué no

### Confirmado por Vanessa (2026-08-13)

**spicata:** `Dreams` · `Flamingo` · `Celway`

### Confirmado por dato — CAMPO escribe el subtipo en el nombre

**cristata:** `Verda Green` · `Indian Summer` · `Enda Rose` · `Reprise Velvet`
· `Reprise Orange` · `Clubs Cocktail` · `Chief Carmine`

Estos no se dedujeron del nombre corto: `campo_siembras.csv` los registra
completos, del tipo `Celosia Cristata Enda Rose`.

### ⚠️ SIN CONFIRMAR — no asignar hasta que Vanessa lo diga

`Shimmer` · `Summer Sherbet` · `Sunday` · `Spun Sugar` · `Rose Gold` ·
`Raspberry Lemonade` · `Sylphid`

**No se deducen del catálogo del proveedor.** La regla 8 del `CLAUDE.md` prohíbe
asignar por deducción y presentarlo como dato; aquí aplica igual aunque se trate
del subtipo y no del color.

Nota: `ciclos_variedad.csv` tiene una fila de **plumosa con datos completos pero
ningún cultivar asignado todavía**. Es decir, se conoce el manejo de plumosa sin
saber cuál de las series que se siembran lo es.

## Ciclo y ventana por subtipo

| Subtipo | Ciclo | Ventana | Fuente |
|---|---|---|---|
| cristata | 14 | 3 | `variedades_bitacora.csv` (PROGRAMACION dice ventana 1) |
| plumosa | 14 | 3–4 | `parametros_siembra.md` (PROGRAMACION dice 14/4 — coinciden) |
| **spicata** | **13–15** | **2–3** | Derivado: PROGRAMACION `Celway 13/2` y `Flamingo 15/2`, bitácora `Purple Flamingo 15/3` |

El rango de spicata sale de **tres cultivares nombrados**, no de un promedio
inventado. Cuando haya cosecha suficiente por subtipo, se reemplaza por el
observado.

## Lo cosechado hasta hoy (2026-08-13)

6.221 tallos en 54 registros:

| Serie en el registro | Tallos | Subtipo |
|---|---|---|
| Mix | 1.960 | **SIN_DATO** — ver abajo |
| Cristata Verda Green | 1.264 | cristata ✅ |
| Shimmer Mix | 1.210 | sin confirmar |
| Dreams Mix | 890 | **spicata** ✅ |
| Summer Sherbet | 830 | sin confirmar |
| Enda Rose | 67 | cristata ✅ |

**El 31 % de la Celosia cosechada entró como `Mix` a secas** — 1.960 tallos en
3A/Inv3A entre el 2 y el 12 de agosto, sin atribución de cultivar.

### La causa raíz es el desplegable, no la captura

```
listas_desplegables.csv  →  Celosia,Mix
```

**La única opción que ofrece el desplegable de Celosia es `Mix`.** Las otras
cinco series se escribieron a mano. Mientras eso siga así, el problema se
reproduce cada semana: no es descuido de quien captura, es que no había qué
escoger. **Arreglar LISTAS corta el problema en la fuente.**

## El puente roto entre cosecha y siembra

Los nombres del registro **no cuadran** con los homologados de CAMPO:

| Se cosecha como | Se sembró como |
|---|---|
| `Summer Sherbet` | `Floret Rosados Corales` |
| `Spun Sugar` | `Floret Rosados Corales` |
| `Rose Gold` | `Floret Rosados Corales` |

Tres cultivares distintos bajo un solo nombre homologado de color. **Consecuencia
directa: no se puede cruzar la cosecha con las plantas trasplantadas**, y por
tanto no hay tallos/planta para esos lotes. Es el mismo puente roto que en
Colitas de conejo.

## Qué falta

1. **Subtipo de `Shimmer`, `Summer Sherbet` y `Sunday`** — con eso queda cerrado
   el mapeo de todo lo que hoy se cosecha.
2. **Qué había en la cama de la `Mix`** de agosto, o marcarla `SIN_DATO`
   explícitamente.
3. **Arreglar `listas_desplegables.csv`** para que el desplegable ofrezca las
   series reales.
4. **Deshacer `Floret Rosados Corales`** en tres homologados, uno por cultivar.
