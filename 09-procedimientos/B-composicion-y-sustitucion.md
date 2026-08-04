# A7 — Composición de producto y reglas de sustitución

## Estado: PENDIENTE — conversación de diseño con Vanessa

Este procedimiento no se puede construir por inferencia.
Requiere una sesión dedicada donde Vanessa explique:

1. Qué papel juega cada variedad en el ramo — no desde los números, sino desde el diseño
2. Qué puede reemplazar qué, y en qué condiciones
3. Qué combinaciones no funcionan aunque los números cuadren

**Hasta que esa conversación ocurra, este archivo no debe usarse para ninguna
recomendación de programación ni de sustitución.**

## Lo que sí existe y es dato real

La hoja `07-datos/formulas_productos_bouquets.csv` tiene la composición actual
de cada producto — cantidades por variedad, precio, categoría.
Eso es un hecho. La interpretación de por qué esa composición es así, no.

## Preguntas base para la sesión de diseño

- ¿Cómo describís un ramo DCB en términos de lo que debe transmitir?
- ¿Hay variedades que son irremplazables — que si no están, el ramo no es DCB?
- ¿Hay variedades que entran según disponibilidad, sin importar cuál sea?
- ¿Cuándo tenés pocas bocas de dragón, qué hacés?
- ¿Cuándo no hay lisianthus, qué cambia en el Dream Big?
- ¿El Amaranto Tails tiene un rol distinto al de las variedades verticales?
- ¿La Zinnia entra siempre o solo cuando hay?

## Por qué este procedimiento importa

Con las reglas de sustitución escritas, Code puede correr la lógica al revés:
dado lo que va a estar disponible en la semana X, ¿qué combinación de productos
se puede armar? ¿Qué le falta para poder armar el Dream Big?

Hoy esa decisión la toma Vanessa de cabeza cada semana.
Con esto, Code la asiste con datos — y Vanessa confirma o ajusta.
