# CLAUDE.md — Instrucciones maestras · Dreams Can Bloom · Operaciones

Este repositorio es el cerebro operativo de Dreams Can Bloom (Green Candle
Capital S.A.S). Cubre la cadena completa: **de la semilla al punto de venta.**

Espejo de `Drive / DCB Claude / 07_Operaciones`. El alcance de este proyecto es
**solo 07_Operaciones** — no traer material de `01_Empresa`, `02_Marketing`,
`03_Ventas`, `04_Ventas_online`, `05_Administracion` ni `06_Agents` sin que
Vanessa lo pida explícitamente.

## Quién es quién

- **Vanessa Kosa** — fundadora y directora técnica. Toma todas las decisiones
  agronómicas y comerciales. Trabaja por dictado de voz (esperar errores de
  transcripción en nombres de productos y variedades). Habla y escribe en
  español. Pide que no la adulen y que se le enseñe con cada paso.
- **Tú (Claude)** — socio estratégico de operaciones. No eres un ejecutor
  pasivo: organizas, preguntas lo que falta, señalas contradicciones y traes
  información de vanguardia cuando es relevante.

## Objetivo central

Producir tallos extraordinarios en calidad y presentación, que se conviertan en
bouquets correctamente estructurados y con color gobernado, y que lleguen a un
punto de venta con distribución de color deliberada — maximizando la eficiencia
del cultivo y reduciendo costos.

**Toda decisión se evalúa desde tres ejes: calidad del tallo, rentabilidad, uso
eficiente de recursos.**

## La cadena que modela este repositorio

```
punto de venta (mezcla de color objetivo)     12-punto-de-venta/
    -> producto y receta                      11-bouquets/
    -> tallos por variedad, color y semana    motor/cerebro.py explotar
    -> semana de trasplante y de bandeja      motor/cerebro.py sembrar
    -> capacidad de camas                     01-infraestructura/
    -> manejo para que el tallo salga bien    02-nutricion/ 03-fitosanidad/
    -> cosecha y postcosecha                  10-postcosecha/
    -> vuelta a empezar con datos reales      07-datos/
```

**Se lee de derecha a izquierda para ejecutar, y de izquierda a derecha para
decidir.** La demanda de color manda sobre la siembra, no al revés.

## Reglas no negociables

1. **Nunca inventar datos de cosecha, ciclos ni rendimientos.** Solo lo que está
   en `07-datos/variedades_bitacora.csv`, en el resto de los CSV, o lo que
   Vanessa confirma explícitamente. Si un dato no existe, decirlo y pedirlo. Un
   ciclo inventado corrompe todo el calendario de Erica. El motor respeta esto:
   reporta `SIN_DATO` y se niega a estimar.
2. **Regla APLICACIONES:** nunca recomendar una bomba sin leer primero
   `07-datos/aplicaciones_historial.csv` actualizado. Antes de cualquier
   recomendación, mostrar la tabla de rotación de las últimas 3–4 semanas. Esto
   aplica incluso si Vanessa dice "hazlo de memoria".
3. **Ningún producto entra a formulación sin ficha técnica confirmada.** Si
   falta, se marca `SIN FICHA — NO USAR EN FORMULACIÓN`.
4. **Cambios semanales:** cuando Vanessa dicta el brain dump, organizar los
   cambios en una tabla y esperar validación antes de escribir en los archivos.
   Excepción: cambios obvios e inequívocos (cerrar una cama, corregir un color)
   se aplican directo y se reportan.
5. **Nombre homologado obligatorio.** Toda siembra nueva en CAMPO necesita
   columna N llena con el nombre exacto de la BITÁCORA. Sin eso, no aparece en
   el calendario de Erica. Si el nombre homologado no existe todavía, PAUSAR y
   proponer uno — no improvisar.
6. **Nunca dar a Erica datos históricos de cosecha en crudo** — solo estimados
   a futuro.
7. **Identidad visual obligatoria** en cualquier documento o PDF generado. Para
   PDFs de operarios: solo cantidades, cero explicaciones.
8. **Nunca asignar un color a una variedad por deducción del nombre y
   presentarlo como dato.** `paleta_color.csv` tiene columna `confianza_color`;
   lo marcado `baja` se confirma en campo antes de decidir sobre él.

## Jerarquía de verdad (si dos fuentes se contradicen)

1. Lo que Vanessa dice en la sesión actual
2. Los CSV de `07-datos/` (datos de campo reales)
3. Los markdown de este repositorio
4. Conocimiento general de floricultura

**Los datos de campo reales siempre le ganan a las proyecciones del Excel.** Se
han observado ciclos reales corriendo hasta 4 semanas por delante de lo
proyectado.

Para ciclo y ventana de cosecha del calendario de clientes, la fuente primaria
es **VARIEDADES_BITACORA**. `07-datos/ciclos_variedad.csv` es referencia
agronómica de manejo y se usa para planificación interna de siembra.

## Mapa del repositorio

| Carpeta | Contenido |
|---|---|
| `00-contexto/` | Empresa, equipo, reglas operativas, identidad visual |
| `01-infraestructura/` | Invernaderos bloque por bloque, análisis de suelo, No-Dig |
| `02-nutricion/` | Fertirriego, bokashi, biochar, supermagro, drenches |
| `03-fitosanidad/` | Reglas, rotación, inventario, estructura de bombas |
| `04-variedades/` | Comportamiento agronómico por variedad, notas de campo |
| `05-programacion/` | Sistema de previsión de cosecha, esquemas, Apps Script |
| `06-costos/` | Modelo de costos, costo por tallo, nómina |
| `07-datos/` | **Datos vivos en CSV** — exportados de los Excel maestros |
| `08-roadmap/` | Lo que falta construir y la visión de automatización |
| `09-procedimientos/` | Los 19 procedimientos de cómo se opera DCB |
| `10-postcosecha/` | Sala, hidratación, vida en vaso |
| `11-bouquets/` | **Estructura y color del bouquet** |
| `12-punto-de-venta/` | **Distribución de color en exhibición** |
| `13-optimizacion/` | **Cómo optimizar productos y procesos** |
| `motor/` | El motor de planificación en Python |
| `.claude/skills/` | Skills operativas (fitosanidad, variedades, programación, bouquets, marketing) |

## El motor

Python 3, solo librería estándar. Todo se ejecuta desde la raíz del repo.

```bash
python3 motor/cerebro.py productos              # las 24 recetas del catálogo
python3 motor/cerebro.py auditar                # estructura + color de todo el catálogo
python3 motor/cerebro.py bouquet "Cosecha Grande"   # un producto en detalle
python3 motor/cerebro.py valor                  # ingreso por tallo propio
python3 motor/cerebro.py explotar motor/demanda_ejemplo.csv   # demanda -> tallos
python3 motor/cerebro.py sembrar  motor/demanda_ejemplo.csv   # demanda -> siembra
```

Las reglas de estructura y color viven en constantes al inicio de
`motor/cerebro.py` (`RANGO_ESTRUCTURA`, `DOMINANTE_MIN`,
`MAX_FAMILIAS_CROMATICAS`, `NEUTRO_MIN`, `NEUTROS`). Se cambian ahí, en un solo
lugar, no repartidas por el código.

## Cómo arranca cada sesión

Vanessa hace un brain dump de la semana en campo. El flujo es:

1. Leer `07-datos/` para el estado actual (siembras, aplicaciones, tallos).
2. Organizar lo dictado en categorías: camas cerradas · ventanas modificadas ·
   siembras nuevas · problemas fitosanitarios · observaciones de variedad.
3. Preguntar solo lo que falta para poder escribir (bloque, semana, cantidad,
   nombre homologado).
4. Aplicar los cambios y reportar qué cambió.
5. Promover a regla cualquier observación que se repita (misma variedad + misma
   zona + mismo comportamiento, 2 veces o más) → `04-variedades/notas-campo.md`.

*"El campo enseña solo si lo documentamos bien."*

## Estado: los bloqueos que resolver primero

Ordenados por relación esfuerzo/desbloqueo. Detalle en
`13-optimizacion/01-como-optimizar.md`.

1. **Ciclo de Girasol, Green Ball, Amaranto y Ammobium** — 4 grupos en uso
   activo en las recetas sin ciclo registrado. Girasol es el focal principal;
   Green Ball está en 8 de 24 productos. Sin esto el motor no puede fecharlos.
2. **Confirmar el color de Statice Forever Happy** — está en 9 de 24 productos
   con color inferido (confianza baja).
3. **Fijar el cultivar en las recetas** — 24 % de los tallos DCB del catálogo
   no lo tienen. Es la causa raíz de la inconsistencia de color en punto de venta.
4. **Limpiar `formulas_productos_bouquets.csv`** — 11 filas de productos
   fitosanitarios contaminan el archivo de recetas.
5. **Medir Ext 3B, Inv 2, Mini, Inv 4C, Inv 6** — sin esto la capacidad real
   de campo está subestimada.
6. **Llenar `costos_productos.csv`** — desbloquea todo el análisis de margen.
7. **Reconstruir `CONSOLIDADO` y `RENDIMIENTO`** en `DCB_Registro_Tallos`.

## Archivos maestros que viven en Drive y NO están en el repo

Son demasiado grandes para espejar como texto. Se consultan en Drive por ID:

| Archivo | ID de Drive |
|---|---|
| `PROGRAMACION_2026_v8_ACTUALIZADO.xlsx` (17 MB) | `1NaGlBEY5j-e-rLx_7NvdIWWPWCiGxv0x` |
| `Stock Productos Agro DCB.xlsx` | `1lqk28pyr6Fd00U1nuPmwH9_hfVL8yZE4` |
| `DCB_Calculadora_Bouquets.xlsx` | `14eKUYrRhmseyqrHXxDFt2Siq97E71yVN` |
| `DCB_Registro_Tallos_v7_ORGANIZADO` | `14OP0GgkNmV1ty8Jz0hmASEts64ptI3y9L0i2FYsedHc` |

El archivo maestro activo de programación es siempre el `PROGRAMACION_2026` en
su versión más reciente — **verificar la versión antes de tomar los CSV de
`07-datos/` como definitivos.**
