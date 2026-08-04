# Modelo de costos y estructura contable

## Estructura aprobada — 4 bloques

### BLOQUE 1 — INGRESOS

| Canal | Descripción |
|---|---|
| 1.1 | Ventas e-commerce / domicilios |
| 1.2 | Ventas puntos físicos (carritos y espacios en centros comerciales) |
| 1.3 | Ventas B2B / mayoristas / wedding planners |
| 1.4 | Ventas ferias y eventos |

### BLOQUE 2 — COGS · alimenta el costo por tallo

| Código | Subcategoría | Ejemplos |
|---|---|---|
| 2A | Material vegetal | Semillas USA/Col, plántulas Ball/Guaqueta, flete, germinación, sustrato |
| 2B | Insumos cultivo | Fertilización, bokashi, agua, energía, mantenimiento riego |
| 2C | Mano de obra campo | Nómina campo y plantulación (prestación de servicios) |
| 2D | Insumos bouquet comprado | Follaje, flores compradas (lisianthus), flores secas |
| 2E | Poscosecha | Nómina bouqueteadoras, Chrysal, papeles, empaques, cintas, sticker |
| 2F | Logístico | Conductor van, gasolina, cuota crédito van, seguro, mototaxi, peajes |

### BLOQUE 3 — GASTOS OPERACIONALES · NO van al costo por tallo

| Código | Subcategoría | Ejemplos |
|---|---|---|
| 3A | Ventas y canales | Arriendos CC (Jardines, San Lucas, Tesoro), nómina vendedoras, comisiones, viáticos B2B |
| 3B | Marketing y herramientas | Meta Ads, Google Ads, Brevo, Zapier, ManyChat, fotógrafo |
| 3C | Administración (overhead) | Nómina admin, contador, Wix, Google Workspace, internet, papelería |
| 3D | Financieros e impuestos | Intereses Sempli, seguros, 4x1000, comisiones bancarias, IVA-DIAN |

### BLOQUE 4 — CAPEX · se deprecia, no es gasto del período

| Código | Subcategoría | Ejemplos |
|---|---|---|
| 4A | Infraestructura | Invernaderos, sistemas de riego por etapas, camas, bodega, biofábrica |
| 4B | Maquinaria y equipo | Van LABAN, motosierra, carritos de flores, mobiliario, equipos tech |

## Flujo de captura

**Gastos variables del día a día:** quien hace el gasto abre el Google Form desde el celular →
fecha, categoría, subcategoría, ítem, monto, forma de pago, tipo (recurrente/amortizable) →
cae en la pestaña `Registro Gastos`.

**Nómina (cierre quincenal):** la administradora abre la pestaña `Nomina`, ingresa el valor
pagado en Q1 (día 15) y Q2 (día 30) por persona activa, e ingresa el total de la planilla de
seguridad social — el Sheet la distribuye por área automáticamente.

**Cierre mensual (primer día del mes siguiente):** verificar gastos del mes → confirmar nómina →
actualizar los 3 parámetros en `Parámetros Mensuales` → el P&G se actualiza automáticamente.

## Nómina — 29 personas, pagos quincenales (día 15 y 30)

| Área | Personas |
|---|---|
| Poscosecha (7) | Adriana Osorio, Diana Osorio, Anlly Yuliana, Ruth Irene, Gloria Marisela, Sindy, Adriana Flores |
| Ventas físicos (7) | Mónica Guzmán, Karen Álvarez, Lesly Álvarez, Sofía Orozco, Mishell Montiel, María José Naranjo, Juan Pablo Henao |
| Ventas online (1) | Erika Ramos |
| Admin (1) | Tatiana Restrepo |
| Marketing (2) | Isabela López, María Adelaida Vélez |
| Campo (9) | Alexander, Yeison, Fabián, Esneider, Elieser, Gregorio, José, Wilson, Junior |
| Logístico (1) | Andrés (conductor van) |
| Honorarios ext. (1) | Juan Zuleta (contador) |

Campo y plantulación son prestación de servicios (sin seguridad social individual).
La planilla corresponde al personal de nómina fija.

## Archivos del sistema financiero

| Archivo | Contenido | Quién lo usa |
|---|---|---|
| DCB_Modelo_Costos.xlsx | Nómina + Registro Gastos + Parámetros Mensuales + P&G | Administradora — cierre mensual |
| Calculo_por_tallo.xlsx | Costo agrícola por especie (columna BY) | Revisar cuando cambia una especie o parámetro |
| Google Form | Captura de gastos variables | Cualquiera que haga un gasto — **pendiente de construir** |
| Flujo_de_caja_mensual_real.xlsx | Historial 2023–2024 | Referencia — pendiente reclasificar |

## Pendientes

- Terminar el Google Form (rubros ya definidos, falta construirlo)
- Actualizar la nómina — marcar inactivos (varios entraron solo para el pico de Día de la Madre)
- Reclasificar histórico enero–mayo 2026 (exportar WhatsApp + fotos de comprobantes)
- Reclasificar flujo de caja 2023–2024 a la estructura COGS / Gastos Op. / Capex
- Conectar 360dialog + Zapier si se mantiene el canal de WhatsApp para registro de gastos
- Actualizar los 3 parámetros del costo por tallo con datos del mes en curso
