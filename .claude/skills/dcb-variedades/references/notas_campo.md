# Notas de Campo Acumuladas

Registro cronológico de observaciones de campo reportadas por Vanessa. Formato: fecha, variedad, zona, observación.

**Regla de promoción automática:** si la misma variedad + misma zona + mismo tipo de comportamiento aparece reportada dos o más veces en este log, se promueve automáticamente a `reglas_agronomicas.md` como regla establecida — sin esperar confirmación explícita de Vanessa. Un patrón repetido en campo ya es una regla. Al promoverla, anotar aquí la fecha de promoción y dejar la entrada original como historial.

Si una observación nueva contradice una regla ya establecida (no la repite, la contradice), esa sí requiere pausar y preguntar antes de tocar la regla existente.

---

## 2026-09-09 · Dahlia · Inv 2 zona baja — mildeo polvoso y pulgones

Vanessa: *"cuando la sembré en el 2, la sembré en la parte baja porque es la parte
más fresca y pues obviamente estando abajo es donde reciben como más agua. Pero
igual han tenido mildeo, igual han tenido pulgones."*

**La zona se eligió deliberadamente por fresca y con más agua, y aun así falló.**
Descarta el estrés hídrico como causa única.

🟢 **PROMOVIDA A REGLA el 2026-09-09.** Es la segunda vez que se documenta el mismo
patrón en la misma zona: ya estaba en `07-datos/incidencia_fitosanitaria.csv` id 8
— *"Dahlias · Inv 2 · MILDEO · semana 21 · PERSISTENTE"*. Ver
`reglas_agronomicas.md`.

## 2026-09-09 · Dahlia · Inv 1 — mildeo polvoso y pulgones

Vanessa: *"también la sembré en el 1. Ahí pasó lo mismo."*

Segunda zona distinta, mismo resultado. **Inv 1 ya tiene mildeo documentado en
otro cultivo:** `01-invernaderos.md` registra *"ventilación buena por viento, pero
humedad nocturna alta → mildeo en rosas"*, y `microclima_bloques.csv` marca Inv 1
como `humedad_rel = ALTA_NOCTURNA` y `SIN_FERTIRRIEGO`.

## 2026-09-09 · Dahlia · frecuencia de cosecha DIARIA

Vanessa: *"la ventana de corte de ellas es diaria."*

**Dato operativo que no estaba en ningún CSV.** La dalia se corta todos los días,
y es perenne sin cierre de cama (`ciclos_variedad.csv`). Consecuencia directa:
**dos sitios con dalia = dos rondas de corte diarias, indefinidamente.** Es
probablemente el mayor costo de jornal de cosecha por m² del catálogo, y es un
argumento duro a favor de concentrar toda la dalia en un solo invernadero.

## 🟡 Candidata a regla — pendiente de juicio de Vanessa

**"La dalia no va en zona fresca ni sombreada."** Los tres intentos documentados
—Inv 2 (registro id 8), Inv 2 zona baja, e Inv 1— comparten el mismo perfil:
**baja radiación y/o humedad nocturna alta**, elegido a propósito para protegerlas
del calor de mediodía. La literatura de *Golovinomyces cichoracearum* en dalia
señala como condiciones predisponentes **humedad alta, temperaturas moderadas de
20–30 °C y baja luz** — exactamente ese perfil.

**No se promueve automáticamente** porque el criterio del log pide *misma zona*
repetida, y aquí son zonas distintas con una característica en común. Es una
generalización, no una repetición. **Requiere que Vanessa la valide.**

Si se valida, la consecuencia práctica es: **la dalia va en radiación alta y buena
ventilación, y el achicopalamiento de mediodía se resuelve con agua y enfriamiento
evaporativo, no con sombra.**

