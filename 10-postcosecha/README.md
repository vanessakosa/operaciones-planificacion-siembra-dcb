# Postcosecha — el eslabón que falta documentar

Este eslabón está **vacío a propósito**: es el hueco real de la cadena, no un
olvido.

## Por qué importa para el color y la estructura

Entre el corte y el punto de venta hay decisiones que determinan si el tallo que
se sembró para un bouquet específico llega en condiciones de cumplir su rol:

- Un tallo FOCAL que llega abierto de más ya no detiene el ojo: lo satura.
- Un tallo LINEA que se dobla en el balde pierde la silueta que justificaba
  sembrarlo.
- Vida en vaso desigual entre variedades del mismo bouquet hace que el ramo se
  desarme por partes, y el cliente lo lee como mala calidad general.

El punto de corte también mueve el color: la mayoría de estas variedades
cambian de tono entre botón y flor abierta. **El mismo cultivar cortado en dos
puntos distintos son dos colores distintos en el balde.** Eso significa que la
paleta de `07-datos/paleta_color.csv` es incompleta hasta que se le agregue el
punto de corte de referencia.

## Qué hay que traer

El documento existe pero está fuera del alcance de este proyecto:

| Documento | Ubicación | Drive ID |
|---|---|---|
| `DCB Protocolo Sala v4.docx` | Raíz de Mi Unidad, **no** en `07_Operaciones` | `1SXbJRJe6DUPrCG9zd1Ihl97KE7wAGgx8` |

Vanessa pidió quedarse solo en `07_Operaciones`, así que no lo traje. Si se
quiere cerrar este eslabón hay dos caminos:

1. Mover el protocolo a `07_Operaciones/10-postcosecha/` en Drive, o
2. Autorizar explícitamente traerlo desde la raíz.

## Qué falta además del protocolo

Datos que hoy no existen en ninguna parte y que este eslabón necesita:

- **Punto de corte por variedad** — en qué estado fenológico se corta cada una.
- **Vida en vaso por variedad** — días útiles, para poder combinar en un mismo
  bouquet variedades de duración parecida.
- **Merma de sala por variedad** — hoy el motor usa un 15 % plano para todas
  (`motor/cerebro.py`, parámetro `merma` de `explotar`). Es un promedio de
  trabajo, no un dato: variedades con botrytis frecuente como Statice
  seguramente mermen más.
- **Rendimiento de hidratación** — qué proporción del tallo cosechado llega
  vendible.

Con merma por variedad, el plan de siembra dejaría de sobre o subestimar por
grupo. Es la mejora de precisión más directa disponible para el motor.
