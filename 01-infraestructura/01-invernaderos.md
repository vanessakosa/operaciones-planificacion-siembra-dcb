# Invernaderos — arquitectura y perfil de cada bloque

> **Dato central:** solo ~22% del área funciona a pleno potencial. La limitante dominante
> no es agronómica, es **presión de agua**.

| Zona | Área | Estado | Limitante / acción |
|---|---|---|---|
| Inv4 completo | 677 m² | Alta productividad | Ninguna — es la referencia del cultivo |
| Inv3A + Inv3C | 556 m² | Media | Resoluble con manejo agronómico |
| Inv3B + Inv5 + Mini | 949 m² | Problemática | **Presión de agua — se resuelve con bomba ~6M COP** |
| Inv1 + Inv2 | 224 m² | Uso especial | Estrategia pendiente de definir |
| Exterior + Inv6 | 616 m² | Variable | Maleza — se resuelve con mulch plástico |

## Áreas de cama (referencia para cálculos de dosis por m²)

| Bloque | Área cama aprox | Estado suelo |
|---|---|---|
| Inv 2 | ~200 m² | Sin historial de fertirriego |
| Inv 3A | 35.6 m² | Bueno |
| Inv 3B grande | 48.1 m² | Salinidad activa (C.E. 0.829) |
| Inv 3B pequeña | 11.7 m² | Similar a 3B |
| Inv 3C grande | 25.2 m² | Bueno |
| Inv 3C pequeña | 12.6 m² | Bueno |
| Mini grande | 12.6 m² | Bueno |
| Mini pequeña | 6.3 m² | Bueno |
| Inv 4A | 20.2 m² | **Excelente — M.O. 25.6%** |
| Inv 4B | 20.2 m² | Excelente |
| Inv 4C | 40.5 m² | Bueno |
| Inv 5 | 31.7 m² | Bueno, seco |
| Exterior | Variable | Nuevo, presión de maleza |

## Invernadero 1 — Rosas y detalles

- 6 camas. C1–C3 rosas de jardín injertadas ~7 años, post-poda baja, en recuperación
- **URGENTE:** verificar punto de injerto. Si los brotes vienen de **abajo** del injerto,
  la planta no es recuperable
- C4: anémonas viejas fin de ciclo — guardar y clasificar cormos al retirar
- C5–C6: bordes ~30 cm, cormos de ranúnculo costosos para multiplicación
- Sin fertirriego → fertilización manual en caneca de 200 L
- Ventilación buena por viento, pero humedad nocturna alta → mildeo en rosas
- Alto valor de ticket: vale la inversión de recuperarlo

## Invernadero 2 — Mejor producción histórica, hoy subutilizado

- ~16 camas lado A y B con circulación central
- Malla de tutorado 15×15 cm, 6 huecos de alto. Zona alta caliente / zona baja sombreada
- Riego instalado pero **tanque fuera de servicio** → diagnosticar y reparar es prioridad
  (nota: en sesiones posteriores el tanque quedó "en reparación, recién activo")
- Exitoso históricamente: celosias de calor, helipterum, ammobium, Scabiosa stellata, strawflower
- **Oportunidad comercial:** convertirlo en vitrina fotográfica — ya lo solicitaron clientes
- Zona alta y seca de Inv 2: destinada al ensayo de Limonium sinensis serie Diamond

### Es el bloque de ENSAYOS (confirmado por Vanessa, 2026-08-13)

**Inv 2 es donde se prueban cultivos nuevos.** Esto no es un detalle: cambia
cómo hay que leer todo número que salga de aquí. Un rendimiento de Inv 2 **no
es comparable de igual a igual** con el de un bloque de producción — es un
cultivo en su primera vuelta, con manejo todavía sin afinar, y muchas veces sin
histórico contra el cual normalizar.

En ensayo a agosto 2026, todos sin nombre homologado en la columna N:

| Cultivo | Plantas | Estado |
|---|---|---|
| Bunny Tails (Colitas de conejo, *Lagurus ovatus*) | 1.170 | Cosechando desde sem 32. **Primera vez bajo invernadero** |
| Dahlias | 696 + 100 | Cosechando desde sem 32. **Perenne con reset** — se sacan hijos, así que el conteo de plantas deriva |
| Espárrago | sin registrar | Cosechando desde sem 33. **Perenne, primera siembra.** No tiene ni fila en `campo_siembras.csv` |
| Echinops | 200 | — |
| Craspedia | 338 | — |
| Scabiosa Estrella | 870 | — |
| Cynoglossum Blue | 597 | — |

**Consecuencia operativa:** sin nombre homologado no entran al calendario de
Erica (regla 5). Para un ensayo eso puede ser lo correcto — todavía no hay nada
que prometerle a un cliente. Pero **ya están produciendo tallos vendibles**, así
que la decisión de cuándo graduarlos a producción y homologarlos es explícita,
no automática.

**Qué medir aquí:** como son primeras siembras, el dato que hay que capturar no
es el ciclo copiado de una bitácora sino **el observado**: semana de siembra,
semana del primer corte, y tallos por semana hasta que la ventana cierre. Para
los perennes, además, **área en m² en vez de número de plantas** — ver la nota
de Dahlia en `07-datos/ciclos_variedad.csv`.

## Invernadero 3 — El principal (mayor área)

### Bloque 3A — 11 camas, 198 huecos × 8 líneas
- **Gradiente marcado:** camas superiores = más calor y menos agua / inferiores = frescas y húmedas
- Camas superiores **NO aptas** para variedades exigentes en agua — Dianthus fracasó, confirmado
- Camas inferiores exitosas: larkspur, gomphrena (toleran frescura sin botrytis)
- King grass en el humedal inferior requiere **calendario fijo de corte**, no reactivo
- Matricaria Snowball viable aquí (y en Mini), nunca en 3C

### Bloque 3B — El más problemático · 267 huecos × 8 líneas + 3 camas de 65h
- **Doble limitante:** suelo degradado por erosión histórica + presión de agua insuficiente
- Centros de cama con menor productividad — gradiente de erosión pronunciado
- Salinidad activa confirmada (C.E. 0.829) · Fusarium + Botrytis + Oidium en lisianthus
- Compactación real en la "barriga" (zona media de la cama)
- Post-solarización despertó malezas → 3 desyerbes intensivos generaron estrés adicional
- Exitoso: celosias, campanula, trachelium, Dianthus Green Ball (parte inferior)
- **Requiere mejora biológica de suelo a largo plazo** (enfoque Kempf / Restrepo)

### Bloque 3C — 5 camas de 140h + 3 camas de 70h
- Perfil: fresco, húmedo, menos radiación, pegado al humedal
- Exitoso: nigela, Dianthus Green Ball, anémonas, celosias Johnnys, statice
- **Problemático:** matricaria y bocas de dragón (necesitan más sol y menos humedad)
- Lisianthus aquí = la cama más problemática del bloque por humedad nocturna
- **Inóculo de mosca blanca en suelo** — evitar Matricaria Vegmo Single aquí y en Inv 5
- Cama angosta del borde: candidata a perenne — Astrantia recomendada

### El Mini — pegado a zona boscosa con pinos
- 4 camas ~70 huecos × 8 + 3 camas ~35 huecos × 8
- Producción históricamente menor por sombra de pinos
- Ensayo activo: trachelium a 1 planta/hueco en camas 5–8 para más laterales

## Invernadero 4 — El mejor del cultivo

- 28 camas (14A + 14B): 112 huecos × 8 líneas (~16.8 m × 1.2 m). Corredor central
- 3 camas inferiores largas: 225h, 212h y ~190h × 8 líneas
- **Razón del éxito: camas cortas = presión de agua uniforme = riego homogéneo.**
  Esta es la lección transferible más importante de toda la finca.
- M.O. 25.6% · suelo no compactado · candidato a No-Dig completo
- **Alerta estructural:** Fusarium generalizado en suelo, manejado con rotación biosupresora
  (intercalar marigold, gomphrena, matricaria entre ciclos de lisianthus)
- **Alerta activa:** riesgo de botrytis con statice masivo en camas 7B, 10B, 13B
- Problema documentado en cosecha de bocas de dragón: pétalos separados
  → posible estrés hídrico o déficit de Ca/B

## Invernadero 5 — Potencial bloqueado

- 13 camas parejas: 176 huecos × 8 líneas (~26.4 m × 1.2 m), un solo bloque sin corredor
- **La peor presión del sistema** — menor capacidad de tanque
- Trachelium y matricaria se quedaron vegetativos sin florar → **causa confirmada: estrés hídrico**
- Exitoso: celosias spicata y Dreams, celosia cristata (con calor), campanulas
- Suelo activo con costra seca superficial → No-Dig parcial con horquilla 5 cm
- **Inóculo de mosca blanca en suelo** — evitar Matricaria Vegmo Single
- **Instalar la bomba transforma este invernadero.** Resolver agua antes de intensificar fertilización.

## Invernadero 6 — Exterior con mulch

- 7 camas exteriores: 176 huecos × 8 líneas, todas con mulch plástico negro
- Observación: maleza en bordes y pasillos pero **centros limpios → el plástico funciona**
- Calor nocturno retenido por el plástico es beneficioso dado que las noches bajan a 11 °C
- Variedades exitosas en exterior: Ammi majus, Ammobium, Strawflower, Daucus carota

## Camas exteriores adicionales

- **Ext Inv2:** 3 camas con sombra de frutales — candidatas a perennes (Daucus carota exitoso)
- **Ext Inv3A:** 3 camas — Ammobium bajo plástico, primera cosecha con tela
- **Ext Inv3B:** 3 grandes + 3 pequeñas — mismos problemas de curvatura que 3B interno
- **Ext Inv4-5:** 2 camas protegidas del viento — comparativo plástico vs sin plástico en curso

## Capacidad de siembra por cama

| Invernadero | 1/hueco | 2/hueco | Zigzag |
|---|---|---|---|
| Inv3A (198 huecos × 8) | 1.584 | 3.168 | 792 |
| Inv3B (267 huecos × 8) | 2.136 | 4.272 | 1.068 |
| Inv4 (112 huecos × 8) | 896 | 1.792 | 448 |
| Inv5 (176 huecos × 8) | 1.408 | 2.816 | 704 |

Bandejas de germinación en uso: **bandeja 200 y bandeja 288**.
Datos completos en `07-datos/capacidad_bloques.csv`.
