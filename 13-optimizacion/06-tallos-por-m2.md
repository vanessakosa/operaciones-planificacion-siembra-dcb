# Tallos por m² — el denominador que faltaba

```bash
python3 motor/cerebro.py m2            # todo el cultivo
python3 motor/cerebro.py m2 Statice    # un grupo
```

> Construido el 2026-08-13 sobre `registro_tallos.csv` (697 filas, 66.417
> tallos) y `campo_siembras.csv`. Nace del pedido de Vanessa: *"lo que yo
> necesito ver es cada variedad, cuántas plantas se sembraron, cuántos tallos
> se cosecharon, cuánta fue su ventana de cosecha y cuánto vendrían siendo los
> tallos por metro cuadrado."*

---

## Por qué m² y no tallos/planta

Tallos/planta ya lo daba `rendimiento`. No alcanza, por tres razones distintas:

1. **Un perenne no tiene denominador de plantas.** Dahlia se propaga por
   división, así que el conteo de plantas deriva con el tiempo. El área no.
   `m2` es el único comando que puede medir Dahlia y Espárrago.
2. **El eje del proyecto es margen por m² por semana de cama ocupada.**
   Tallos/planta no se convierte a plata sin saber cuánta cama costó.
   Tallos/m²/semana sí.
3. **Dos variedades con el mismo tallos/planta rinden distinto si una va a
   7,5 cm y la otra a 30.** Statice da 8 tallos por planta —el mejor del
   cultivo— pero ocupa **cuatro veces más cama por planta** que un lisianthus.
   Por planta gana Statice; por cama, no.

---

## De dónde sale el área — nadie la midió, se deriva

**El área no está registrada en ningún archivo.** Se deriva de dos cosas que sí
están: las plantas trasplantadas y la distancia de siembra.

La malla es de **0,15 m en las dos direcciones** (Vanessa, 2026-08-13:
*"cada hueco tiene cero quince en esa malla"*). De ahí:

```
sitios por m²   = 1 / 0,15²                      = 44,44
plantas por m²  = 1 / (0,15 × distancia_siembra)
área m²         = plantas trasplantadas / plantas por m²
```

Una sola fórmula cubre los tres casos de la finca, sin excepciones:

| Distancia | Qué significa en la malla | Plantas/m² |
|---|---|---|
| 7,5 cm | 2 plantas por hueco | 88,89 |
| 15 cm | 1 planta por hueco | 44,44 |
| 30 cm | 1 planta cada dos huecos | 22,22 |

**Verificación:** Inv 4A son 112 huecos × 8 líneas = **896 sitios**, que es
exactamente el número que Vanessa escribió en el comentario de esa cama. La
geometría cierra.

La columna **FTE** de cada fila dice de dónde salió la distancia:

- **EXA** — `ciclos_variedad.csv` nombra ese cultivo exacto
- **SUB** — el cultivar se resolvió por `subtipos.csv` (Shimmer → plumosa)
- **GRU** — el cultivar no está, pero **todas** las filas del grupo coinciden en
  la distancia, así que el dato no depende del cultivar. Si se contradijeran, no
  se elige una: sale `SIN_DATO`.

---

## El resultado — quién ocupa la finca y quién la paga

Solo lotes de **una** cama, para no contar dos veces las camas que un lote
reclama en conjunto.

| Grupo | m² | % del área | Tallos | T/m² |
|---|---|---|---|---|
| **Statice** | **847,9** | **29,9 %** | 4.155 | **4,9** |
| Boca de Dragón | 414,6 | 14,6 % | 9.359 | 22,6 |
| Celosia | 356,0 | 12,5 % | 3.450 | 9,7 |
| **Ammobium** | 214,1 | 7,5 % | 487 | **2,3** |
| **Strawflower** | 163,1 | 5,7 % | 1.709 | 10,5 |
| Lisianthus | 143,2 | 5,0 % | 5.597 | 39,1 |
| Amaranto | 120,9 | 4,3 % | 1.152 | 9,5 |
| **Gomphrena** | 115,2 | 4,1 % | 5.121 | **44,5** |
| Ammi | 104,8 | 3,7 % | 2.062 | 19,7 |
| Dusty Miller | 88,9 | 3,1 % | 508 | 5,7 |
| Matricaria | 69,1 | 2,4 % | 184 | 2,7 |
| Trachellium | 42,8 | 1,5 % | 200 | 4,7 |
| **Green Ball** | 41,4 | 1,5 % | 2.710 | **65,4** |
| **Campanula** | 37,0 | 1,3 % | 2.721 | **73,6** |
| Larkspur | 35,9 | 1,3 % | 243 | 6,8 |
| Girasol | 19,7 | 0,7 % | 1.047 | 53,2 |
| Dahlias | 17,9 | 0,6 % | 90 | 5,0 |
| Zinnia | 7,3 | 0,3 % | 3.562 | 488,6 ⚠️ |
| **TOTAL** | **2.839,7** | | | |

### Lo que salta

**Statice ocupa el 30 % del área medida de la finca y entrega 4,9 t/m².**
Campanula entrega **73,6 t/m² en el 1,3 % del área.** Quince veces más
producción por cama, en la vigésima parte del espacio.

Antes de sacar la conclusión fácil, tres matices que la moderan y **uno que la
agrava**:

- Statice va a 30 cm, así que su techo por m² es estructuralmente más bajo:
  22 plantas/m² × 8 tallos = **178 t/m² teóricos**. Está en 4,9. El techo no
  es la explicación.
- **Casi todas las ventanas de Statice están marcadas `FRAGMENTO`** — el
  registro cubre pedazos de ventana, no ventanas. Su T/m² real es más alto que
  el que se ve aquí.
- Statice tiene la ventana más larga del cultivo (4–8 semanas), y eso es su
  mayor virtud comercial: sostiene carrito.
- **Lo que agrava:** Statice tiene botrytis documentada y recurrente
  (*"colapso sem 15+"*, *"son un cementerio"*) y es el grupo con **6 % de
  trazabilidad de cultivar**. Ocupa un tercio de la finca y no se sabe qué
  variedad lo sostiene.

**Ammobium es el caso más limpio: 7,5 % del área para 2,3 t/m², y el comentario
de campo ya decía que sobra** — *"demasiada cantidad de flor para la que piden"*,
*"muchas devoluciones y pérdidas en carritos"*. El área confirma lo que la venta
ya había dicho.

⚠️ **Zinnia 488,6 t/m² no es real.** Son 4 siembras en 4B y solo 1 tiene conteo
de plantas, así que el área sale con la cuarta parte del tamaño. Está marcada
`DENOM INCOMPLETO`. Este error **infla**, al revés que los otros.

---

## Los 13 lotes limpios — sin ninguna marca de advertencia

De 63 lotes con área calculable, **13 no tienen ninguna salvedad**: ventana
completa, denominador completo, cierre propio, distancia exacta. Solo con estos
se puede comparar de verdad.

| Grupo | Variedad | Cama | m² | Tallos | T/m² | T/m²/sem |
|---|---|---|---|---|---|---|
| Gomphrena | Quis Sequin | 3A | 16,5 | 1.497 | 90,5 | **26,40** |
| Boca de Dragón | Opus Fresh | 4A | 9,7 | 650 | 66,9 | **26,01** |
| Campanula | Champion Lavender | 3B | 21,6 | 1.231 | 57,1 | 22,19 |
| Campanula | Champion White | 3B | 15,4 | 1.490 | **96,7** | 16,11 |
| Boca de Dragón | Cannes Light Bronze | 3C | 39,6 | 1.360 | 34,4 | 10,94 |
| Boca de Dragón | Cannes Pink | 4B | 9,7 | 300 | 30,9 | 8,64 |
| Boca de Dragón | Cannes Pink | 4C | 28,6 | 853 | 29,9 | 8,36 |
| Boca de Dragón | Monaco Plumblossom | 5 | 21,6 | 790 | 36,6 | 7,54 |
| Amaranto | Love Lies Bleeding | 3A | 24,0 | 558 | 23,2 | 7,40 |
| Boca de Dragón | Cannes Red | 4A | 31,4 | 1.829 | 58,2 | 7,03 |
| Celosia | Cristata Verda Green | 3A | 35,3 | 1.083 | 30,7 | 5,97 |
| Boca de Dragón | Cannes Lavender | 4C | 35,8 | 450 | 12,6 | 3,99 |
| **Strawflower** | Mix | 6 | **163,1** | 1.709 | 10,5 | **1,36** |

**Strawflower es el lote más grande medido de toda la finca —163 m²— y el de
menor ritmo: 1,36 t/m²/semana, veinte veces menos que Gomphrena Quis Sequin.**
Y su ventana está completa, así que no hay excusa de truncamiento.

**Los dos primeros empatan a 26 t/m²/sem por caminos opuestos:** Quis Sequin
produce mucho durante 3,4 semanas; Opus Fresh produce concentrado en 2,6. Uno
sostiene carrito, el otro golpea un pico. Esa diferencia solo se ve en el ritmo,
no en el T/m² total.

---

## Las cuatro marcas — y en qué dirección miente cada una

La tabla no oculta los lotes con problemas: los marca y dice hacia dónde miente
el número. Eso importa porque **no todas mienten en la misma dirección.**

| Marca | Qué pasó | Dirección del error |
|---|---|---|
| `ABIERTA` | seguía produciendo el 2026-08-12 | **SUBESTIMA** — va a subir |
| `ARRANCA EN EL CORTE` | su primer corte es del 2026-05-31, el primer día del registro. Ya venía cosechando de antes | **SUBESTIMA** |
| `CIERRE AJENO` | la cama se cerró por espacio, demanda o sanidad, no porque la planta parara | **SUBESTIMA** |
| `DENOM INCOMPLETO` | hay siembras sin conteo en esa cama, así que el área sale más chica | **INFLA** |
| `FRAGMENTO` | la ventana registrada es más corta que la ventana mínima documentada del grupo | **las dos a la vez** |

`FRAGMENTO` es la que hay que entender bien, porque es la única que miente en
las dos direcciones al mismo tiempo: el **total** sale corto porque falta
cosecha, y el **ritmo** sale largo porque el pedazo registrado suele ser el
pico.

> **Esto no es teórico: pasó en la primera corrida.** Amaranto Emerald Tails
> salió primero del bloque 3A con **48 t/m²/sem** — que eran 380 tallos en
> **dos días**. Por eso el ritmo de un fragmento ya no se imprime y esos lotes
> no entran al ranking. 38 lotes quedan fuera por esto.

---

## Lo que este comando todavía no puede

**30 % de la cosecha (19.856 tallos) se queda sin T/m².** No es un cero: es que
falta el denominador.

| Falta | Lotes | Qué se necesita |
|---|---|---|
| **Plantas trasplantadas** | la gran mayoría | llenar `Cantidad Trasplantada` en CAMPO |
| Distancia ambigua | Celosia Mix 3A (1.960 tallos) | el subtipo de esa cama — cristata y plumosa no van a la misma distancia |
| Distancia sin dato | Colitas de conejo (400 tallos) | distancia de siembra del grupo |

Y lo que sigue faltando para cerrar el eje del proyecto:

- **`costos_productos.csv` está vacío.** Con área ya se puede calcular
  **t/m²/semana**; para llegar a **$/m²/semana** falta el costo de ocupar esa
  cama. Es el último tramo, y es dato de Vanessa.
- **`calidad_tallo.csv` está vacío.** T/m² cuenta tallos, no tallos vendibles.
- **No existe archivo de ventas.** Un T/m² alto de algo que se devuelve no es
  rentabilidad. Ammobium es el ejemplo: bajo T/m² **y** devoluciones.

---

## Nota técnica: el cruce quedó en un solo lugar

`rendimiento` y `m2` ahora usan la misma función `construir_lotes()`. Antes cada
comando armaba el cruce CAMPO↔REGISTRO por su cuenta, y arreglar una grafía de
bloque en uno dejaba al otro dando un número distinto para el mismo lote.

**`matriz` todavía tiene su propio cruce**, y por eso reporta 20 % de cobertura
en la variable 8 donde `rendimiento` reporta 57 %. Sigue pendiente unificarlo —
está en `08-roadmap/03-que-falta-en-la-arquitectura.md` como deuda técnica A3.
