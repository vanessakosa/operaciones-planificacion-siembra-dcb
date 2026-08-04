# B4 — Cálculo de volumen de bombas

## La fórmula

```
bombas_necesarias = área_en_etapa × nivel_de_aplicación × coeficiente_operario
```

## Regla principal de proyección

**1 bomba de 25 L por cada 2 camas — nivel general.**
**1 bomba por cama — nivel dirigido.**
Redondear siempre hacia arriba.

*Calibrado con: 13 camas (7 statice + 6 lisianthus) = 6 bombas. Verificado en campo.*

## Cómo se agrupa el área

**No se agrupa por bloque — se agrupa por etapa fenológica.**
Todas las camas en vegetativo van juntas, sin importar en qué invernadero estén.
Eso es lo que hace que el inventario de camas con ID sea la base del sistema.

| Etapa | Semanas post-trasplante | Fórmula de fertirriego que recibe |
|---|---|---|
| Vegetativo | 1–6 | Fórmula A |
| Prefloración | 7–9 | Fórmula B |
| Floración / Cosecha | 10+ | Fórmula C |
| Endurecimiento (solo Dusty Miller) | 18+ | Fórmula dedicada |

## Niveles de aplicación

| Nivel | Cuándo | Qué significa para el operario |
|---|---|---|
| **General** | Preventiva de rutina, cama sana | Va a buen paso, cobertura uniforme |
| **Dirigida** | Problema activo, ventana crítica, variedad sensible | Cubre envés, trabaja foco por foco, más lento |

**El nivel va explícito en el PDF del operario.** Si no está escrito, el operario decide solo — y Alexander y Wilson deciden distinto.

## Las dos ventanas de aplicación

| Ventana | Horario | Para qué sirve |
|---|---|---|
| **Mañana** | 7:00 – 9:00 am | Nutricionales, bioestimulantes, Bacillus (esporas UV-resistentes), insecticidas de blanco diurno |
| **Tarde** | ~3:30 – 6:00 pm | Fungicidas, **todos los biológicos fúngicos**, blancos nocturnos |

**Regla de asignación:** primero se clasifica la bomba por producto. Los productos estrictos de tarde se agendan primero y ocupan esa ventana. Los flexibles se mueven a la mañana según radiación de la semana y disponibilidad de mano de obra.

### Clasificación de productos por ventana

| Producto | Ventana | Razón |
|---|---|---|
| BTK | **Tarde estricta** | Las proteínas activas se degradan por UV — pierde 80% de viabilidad en 2 min de UVC |
| Safer Mix (Beauveria) | **Tarde estricta** | La radiación solar inactiva los conidios sin formular |
| Deep Green (Metarhizium) | **Tarde estricta** | 93% de reducción en germinación tras 40 seg de UVC |
| No Fly (Paecilomyces) | Tarde preferible | Tiene mecanismo de reparación, más resistente que Beauveria |
| Botrycid (Burkholderia) | Tarde | Bacteria vegetativa |
| **Amicos MC, Promobac, Estabios (Bacillus)** | **Flexible** | Las endosporas de Bacillus sobreviven radiación extrema |
| Equifun, Regalia, ADNGard, Glukoplant, Starzyme, nutricionales | **Flexible** | No son organismos vivos |

**Nota estacional:**
- Verano activo (ahora), alta radiación, viento: mañana solo para los flexibles. Tarde para todo lo fúngico
- Días nublados, lluvia: mañana viable también para fungicidas preventivos. Excepción: si el tejido amaneció mojado de rocío, aplicar fungicida encima prolonga la humedad foliar — es contraproducente

**El blanco activo manda sobre la preferencia estacional.** Si el insecto tiene más movimiento en la mañana, la bomba va en la mañana aunque haya verano.

## Techo de capacidad por sesión

| Parámetro | Valor |
|---|---|
| Tiempo por bomba (cargar + aplicar) | ~20–25 min |
| Operarios en paralelo | **1** — casi nunca aplican al tiempo, uno riega o hace otra labor |
| Duración de sesión | 2 a 2.5 horas |
| **Techo por sesión** | **6 bombas** (medido) · tope absoluto ~8 |

**Regla de techo:** si el programa semanal necesita más de 6 bombas en una ventana,
se parte en dos días. Lo que se cae cuando no alcanza el tiempo es la preventiva
de rutina — nunca lo dirigido.

## Priorización cuando no alcanza

1. Camas con **problema activo** — primero siempre
2. Camas en **ventana crítica** (bocas de dragón sem 5–8, statice en cosecha)
3. Preventiva de rutina

Y dentro de la sesión: las camas prioritarias van **primero** — las últimas de la
sesión caen dentro de la ventana de infección nocturna.

## El orden va en el PDF

El PDF especifica el orden de aplicación, no solo las camas. La cama #1 en el PDF
es la primera que Alexander aplica — tiene que ser la más crítica.

## Coeficientes de operario

| Operario | Coeficiente | Estado |
|---|---|---|
| **Alexander** | 1.0 (referencia) | ✅ Confirmado — aplica con detalle, usa más bombas |
| Wilson | 🔴 pendiente | ⏳ Sale del reporte de bombas usadas (~5 semanas) |
| Atilio | 🔴 pendiente | ⏳ Idem |

## El operario reporta

Al final de cada sesión, el operario anota en el PDF o por WhatsApp:
- Hora de inicio
- Hora de fin
- Bombas usadas de verdad

Tres datos. Con 4–5 semanas de registros, el coeficiente de cada operario sale
de datos reales y la proyección se corrige sola.

## Pendientes de B4

| Pendiente | Cómo se resuelve |
|---|---|
| m² por cama individual | Medición de campo — ver `01-infraestructura/04-inventario-camas-borrador.md` |
| ID de camas | Idem |
| Coeficiente Wilson y Atilio | Reporte de bombas usadas, ~5 semanas |
