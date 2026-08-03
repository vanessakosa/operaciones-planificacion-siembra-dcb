# Distribución de color en el punto de venta

## Qué problema resuelve este eslabón

Un bouquet puede estar perfecto por sí solo y el punto de venta verse mal. Son
dos problemas distintos:

- **Color del bouquet** — la armonía *dentro* de un ramo. Ver `11-bouquets/`.
- **Color del punto de venta** — la distribución *entre* los ramos expuestos.

El segundo falla cuando todos los bouquets del día salen del mismo pico de
cosecha y el punto de venta queda, por ejemplo, 80 % lila porque esa semana
entró toda la Statice Forever Happy junta.

El cliente no compra un bouquet: elige entre los que ve. Si los ocho que ve
son variaciones del mismo lila, no percibe surtido — percibe que no hay de
dónde escoger.

## El mecanismo del problema

```
ventana de cosecha concentrada  ->  todos los tallos del mismo color a la vez
        ->  todos los bouquets del día con el mismo dominante
        ->  punto de venta monocromático
```

La causa raíz está en la **programación de siembra**, no en la exhibición. Una
variedad con ventana de 2 semanas (Campanula, Larkspur, Boca de Dragón)
entrega todo su color en 2 semanas. Si no hay siembras escalonadas de otras
familias que cubran esas mismas semanas, el punto de venta se vuelve
monocromático por construcción.

Por eso este eslabón **manda hacia atrás** sobre la siembra, y no al revés.

## La mezcla objetivo

La decisión comercial es: *qué distribución de color queremos ver en el punto
de venta cada semana*. Esa decisión es de Vanessa; el motor sólo la verifica y
la traduce a siembra.

Se declara en `07-datos/objetivo_color_pdv.csv`:

| Columna | Significado |
|---|---|
| `semana` | Semana ISO. `*` aplica a todas las semanas sin regla propia. |
| `familia_color` | Familia de `paleta_color.csv`, o `NEUTRO` para el agregado. |
| `pct_min` | Piso de participación en los bouquets expuestos. |
| `pct_max` | Techo de participación. |
| `nota` | Motivo comercial (temporada, fecha especial, campaña). |

El archivo está creado con una **propuesta inicial** basada en lo que el
catálogo ya sabe hacer, no en datos de venta. Está marcado como
`PROPUESTA — SIN VALIDAR`. Los datos reales de venta y rotación viven en
`03_Ventas` del Drive, que está fuera del alcance de este proyecto: hay que
traerlos o dictarlos.

## Reglas de exhibición

Independientes de la mezcla objetivo, tres reglas que no dependen de datos de
venta:

1. **Ningún dominante por encima de 40 % de los bouquets expuestos.** Aunque la
   cosecha empuje en esa dirección.
2. **Mínimo 3 familias dominantes distintas en exhibición.** Si la cosecha no
   alcanza, es señal de que la programación de siembra no está escalonada.
3. **Los neutros no cuentan como surtido.** Un punto de venta con ocho ramos
   blancos y verdes no es variado: es blanco.

## Cómo se conecta con la siembra

El flujo completo, y el orden en que se recorre:

```
objetivo_color_pdv.csv          (decisión comercial)
   -> mezcla de productos por semana que la satisface
   -> demanda de productos           (semana, producto, unidades)
   -> motor/cerebro.py explotar      -> tallos por variedad/color/semana
   -> motor/cerebro.py sembrar       -> semana de trasplante y de bandeja
   -> chequeo de capacidad de camas
```

El paso de *objetivo de color* a *mezcla de productos* es el único que todavía
no está automatizado, y es deliberado: requiere fijar primero el color en las
recetas. Hoy 24 % de los tallos DCB no tienen cultivar definido, así que la
mezcla de productos no determina la mezcla de color. **Cerrar esa brecha es
prerrequisito de este eslabón** — no un detalle posterior.

Mientras exista esa indeterminación, el motor puede decir cuántos tallos de
cada grupo hacen falta, pero no puede garantizar el color resultante.
