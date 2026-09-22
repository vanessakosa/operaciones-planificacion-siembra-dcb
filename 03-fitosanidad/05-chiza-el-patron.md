# Chiza (gallina ciega) — es un patrón de VENTANA, no de variedad

> Reconstruido con Vanessa el 2026-09-16. Ella hizo la pregunta que lo ordenó todo:
> **¿por qué las bocas de dragón, y por qué en tres bloques distintos a la vez?**
> La respuesta es que no fueron elegidas.

## Los dos eventos, fechados

| Evento | Semana ISO | Qué atacó | Bloques | Estado del cultivo |
|---|---|---|---|---|
| **1** | **~13 de 2026** (finales de marzo) | **Dianthus rosado** — *Brianthus Hilverda*, trasplante sem 2, cosecha sem 13 | 3A | **en cosecha** |
| **1** | **misma semana 13** | **Statice Forever Happy**, trasplantado sem 13 | 3A + 3B + 4A | **recién trasplantado** |
| **2** | **38 de 2026** (mediados de septiembre) | **Bocas de dragón** | 3B + 4A + 4B | jóvenes |

*Siembra del evento 1 **confirmada por Vanessa el 2026-09-16**: `Brianthus Hilverda` /
homologado `Brianthus Jolly`, fila 126 de `campo_siembras.csv`.*

## Lo que prueban esos dos renglones de la semana 13

**La misma semana, la chiza atacó un dianthus EN COSECHA y un statice RECIÉN TRASPLANTADO.**
Dos variedades distintas, dos edades opuestas, el mismo momento.

> **No selecciona variedad. No selecciona edad. No selecciona bloque. Selecciona SEMANA.**

Cuando la larva llega a su estadio voraz, come lo que tenga encima. Lo demás es coincidencia de
lo que estuviera sembrado.

**Es la misma forma de patrón que el repositorio ya tiene escrito para el statice** — *"Botrycid
+ Equifun preventivo desde la semana 14–15 de cosecha, antes de sospechar botrytis. Patrón de
ventana temporal, no de variedad."* Son dos casos de lo mismo: el calendario manda sobre la
especie.

## Y por eso la boca de dragón parecía elegida, sin serlo

Dos datos de `campo_siembras.csv`:

1. **Es el 20 % de todas las siembras de la finca** — 60 de 302 filas, en 13 bloques. En 4A es
   el 40 % de lo sembrado, en 4B el 29 %, en 3B el 24 %. Si una plaga de suelo aparece en tres
   bloques a la vez, es la variedad con más probabilidad de estar en los tres.
2. **En 3A la chiza NO fue a las bocas de dragón**, y 3A tiene 13 siembras de boca de dragón
   registradas. Fue al dianthus y al statice. Si hubiera preferencia, ahí habría ido.

## El ciclo: es SEMESTRAL, no anual

**Semana 13 y semana 38. Veinticinco semanas — seis meses casi exactos.**

Caen en el arranque de las dos temporadas de lluvia del altiplano (marzo–mayo y
septiembre–noviembre). Los adultos emergen y vuelan con las primeras lluvias fuertes, ponen, y
la larva empieza a comer semanas después.

> ⚠️ **El régimen bimodal de lluvias es conocimiento general, no un dato medido de esta finca.**
> Es exactamente lo que `clima_semanal.csv` —pendiente #2 del roadmap— confirmaría o tumbaría.
> Con dos eventos hay un intervalo, no todavía una serie.

### La consecuencia práctica, que es toda la razón de este documento

| | |
|---|---|
| **Próxima ventana de riesgo** | **semanas 12–14 de 2027** |
| La siguiente | semanas 37–39 de 2027 |
| Qué cambia | El drench va **antes** de ver plantas muertas, no después |

Hoy el manejo es reactivo: se actúa cuando ya hay mortalidad y la raíz ya se perdió. Con la
ventana identificada, el mismo producto puesto tres semanas antes vale mucho más.

## Lo que falta para cerrarlo

| # | Falta | Qué desbloquea |
|---|---|---|
| 1 | **Un tercer evento** (o revisar 2025) | Dos puntos dan un intervalo; tres dan un ciclo |
| 2 | **`clima_semanal.csv`** | Ata la ventana a la lluvia y la vuelve predecible, no solo repetible |
| 3 | **Conteo de trampa de luz, semana a semana** | Es la única forma de medir presión con el ground cover puesto — y lo que avisaría de la ventana **antes** del daño |
| 4 | **Dosis y resultado del control del evento 1** | Funcionó, y no está escrito con qué números |

## El producto de fondo: RAXTER MIX SC

**Ficha técnica confirmada** — FT 8030 v2, 2026-02-10, registro ICA 14487, BIO-CROP S.A.S.
(Palmira, Valle). Aportada por Vanessa el 2026-09-22.

| | |
|---|---|
| *Metarhizium anisopliae* | 2,0×10⁸ UFC/cc |
| *Beauveria bassiana* | 2,0×10⁸ UFC/cc |
| *Bacillus thuringiensis* var. *kurstaki* | 2,0×10⁸ UFC/cc |
| ***Bacillus popilliae*** | **2,0×10⁸ UFC/cc** |

***Bacillus popilliae* es el diferenciador.** Es el patógeno específico de larvas de escarabajo
—la enfermedad lechosa— y es lo más dirigido que existe contra chiza. Ninguno de los otros
productos del repositorio lo tiene.

> **Ornamentales · Chizas · 50 cc por cama · repetir a los 15 días mediante drench.**

Es dosis **por cama**, para **ornamentales**, contra **chiza**, en **drench**. Exactamente los
cuatro atributos que a la ficha del Deep Green le faltaban y que costaron tres rondas de
sesión. A 50 cc/cama, un litro rinde **20 camas**.

**Compatibilidad, textual:** *"Puede usarse en mezcla con insecticidas, herbicidas y
fertilizantes. **No debe usarse en mezcla con fungicidas y bactericidas.** Puede usarse con
coadyuvantes que no tengan alcohol."*

> ⚠️ **Corrección a lo que yo había dicho:** advertí que el drench debía ir en tanque de agua
> sola por la C.E. del fertirriego. **La ficha autoriza la mezcla con fertilizantes**, y la
> ficha manda sobre mi precaución. Lo que sí se mantiene, y ahora con respaldo de etiqueta, es
> la prohibición con fungicidas.

**Sin categoría toxicológica, sin período de carencia y sin período de reingreso.** Para flor de
corte eso vale mucho: se aplica sin sacar gente del invernadero y sin esperar para cosechar.

### Deep Green o Raxter

| | Deep Green | **Raxter Mix SC** |
|---|---|---|
| Organismos | *Metarhizium* solo | **4, con *B. popilliae*** |
| Dosis ornamental/chiza/drench | **no la trae** | **50 cc/cama** |
| Concentración UFC/cc | **SIN_DATO** | 2,0×10⁸ de cada uno |
| Ficha en el repositorio | parcial | **completa** |
| Ya está comprado | **sí, ~800 cc** | por confirmar |

**No hay que elegir hoy:** el Deep Green está en finca y ya controló el evento de marzo, así que
es lo que entra en la ventana abierta. El Raxter es el producto de fondo — para los pases 2 y 3
y para la ventana de marzo de 2027.

🟡 **Pregunta pendiente al proveedor del Deep Green: ¿cuántas UFC/cc tiene?** Es el único dato
que permite comparar las dos dosis en la misma unidad. Sin él, "1 cc/L" y "50 cc/cama" no son
comparables.

## Manejo vigente

`07-datos/decisiones_manejo.csv` (2026-09-16) y la hoja
`05-programacion/hojas-operario/drench-chiza.html`.

**Deep Green 1 cc/L en tanques de 200 L, por fertirriego, con la cama llevada a capacidad de
campo antes.** Dosis dictada por Vanessa: 0,7 cc/L normal, **1 cc/L en incidencia alta**.
2–3 pases cada 15 días. Operario: Tilio.
