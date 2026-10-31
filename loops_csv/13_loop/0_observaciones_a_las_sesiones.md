## Resumen del estado por archivo

| Archivo | Estado | Reglas generales incumplidas | Cantidad filas observadas |
|---|---|---|---:|
| `PF-A1-002.csv` | Completado | Ninguna | 0 |
| `PF-A1-003.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-004.csv` | Completado | Ninguna | 0 |
| `PF-A1-006.csv` | Observado | Progresion y repetición incremental | 5 |
| `PF-A1-008.csv` | Observado | Progresion y repetición incremental | 3 |

## PF-A1-002 — Indicar cantidad o grado y resolver una petición sencilla de compra/pago — `PF-A1-002.csv` — Completado

**Reglas generales por archivo incumplidas**
- Ninguna. El CSV tiene 181 filas, codificación UTF-8 y formato de dos columnas; cumple el mínimo de 150 frases. La observación previa de progresión en la fila 083 está corregida.

**Reglas incumplidas por línea**
- Ninguna.

## PF-A1-003 — Iniciar/cerrar intercambios cercanos y expresar cortesía, deseo o capacidad — `PF-A1-003.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.**
  - **Fila 015:** «Después del trabajo, mi mejor amigo y yo estudiamos juntos» repite la escena de la fila 005, «Mi mejor amigo y yo estudiamos juntos», añadiendo solo el momento. Reemplazar por: `Mi mejor amigo y yo preparamos una presentación para la clase de ciencias.;My best friend and I prepare a presentation for science class.`
  - **Fila 206:** «Después del trabajo, ella espera a su amiga fuera de la tienda» repite la misma espera de la fila 199, «Ella espera a su amiga fuera de la tienda», añadiendo solo el momento. Reemplazar por: `Después del trabajo, ella espera a su amiga en el vestíbulo del teatro.;After work, she waits for her friend in the theatre lobby.`

La validación de las reglas por línea se detuvo al observarse una regla general incumplida.

## PF-A1-004 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 1/2) — `PF-A1-004.csv` — Completado

**Reglas generales por archivo incumplidas**
- Ninguna. El CSV tiene 150 filas, codificación UTF-8 y formato de dos columnas; cumple el mínimo de 150 frases. Las observaciones previas de progresión en las filas 064, 074, 124 y 144 están corregidas.

**Reglas incumplidas por línea**
- Ninguna.

## PF-A1-006 — Responder a situaciones cotidianas con una expresión breve y autónoma — `PF-A1-006.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.**
  - **Fila 037:** «Después de clase, avísame por teléfono» repite la instrucción de la fila 032, «Avísame por teléfono», añadiendo solo el momento. Reemplazar por: `Después de clase, avísame si encuentras mi cuaderno en el aula.;After class, let me know if you find my notebook in the classroom.`
  - **Fila 061:** «¡Hasta luego! Nos vemos después de clase» repite el contenido de la fila 058, «Nos vemos después de clase», agregando solo otro saludo. Reemplazar por: `¡Hasta luego! Te escribiré cuando termine el entrenamiento.;See you later! I will text you when training ends.`
  - **Fila 108:** «Después de la lluvia, nos quedamos en casa para ver una película» repite la escena de la fila 107, «Esta noche, nos quedamos en casa y vemos una película», cambiando únicamente el momento/contexto. Reemplazar por: `Después de la lluvia, nos quedamos en casa para jugar a un juego de mesa con los niños.;After the rain, we stay in to play a board game with the children.`
  - **Fila 161:** «Los días de clase, mi hermano se despierta temprano» repite la situación de la fila 159, «Mi hermano se despierta temprano para ir a la escuela», variando únicamente la referencia temporal. Reemplazar por: `Mi hermano se despierta antes del amanecer para ayudar en la granja.;My brother wakes up before dawn to help on the farm.`
  - **Fila 174:** «Antes del viaje, ella anota la dirección» repite la escena de la fila 167, «Ella anota la dirección antes del viaje». Reemplazar por: `Antes del viaje, ella anota el número de la reserva en su cuaderno para tenerlo a mano.;Before the trip, she writes the booking number in her notebook to keep it handy.`

La validación de las reglas por línea se detuvo al observarse una regla general incumplida.

## PF-A1-008 — Coordinar una tarea sencilla y compartir información o una postura breve — `PF-A1-008.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.**
  - **Fila 031:** «Mi madre está en el trabajo hasta las cinco» repite la escena de la fila 022, «Mi madre está en el trabajo», añadiendo solo la hora de salida. Reemplazar por: `Mi madre está en el trabajo y atiende a los clientes en la recepción.;My mother is at work and helps customers at reception.`
  - **Fila 078:** «Mi hermana y yo trabajamos juntas después de clase» repite el trabajo no especificado de la fila 076, «Mi hermana y yo trabajamos juntas en la cocina», sin añadir una tarea o contexto relevante. Reemplazar por: `Después de clase, mi hermana y yo ensayamos juntas una obra para el festival escolar.;After class, my sister and I work together to rehearse a play for the school festival.`
  - **Fila 079:** «Después del trabajo, mis amigos y yo trabajamos juntos» repite la escena de la fila 072, «Mis amigos y yo trabajamos juntos», añadiendo solo el momento. Reemplazar por: `Después del trabajo, mis amigos y yo trabajamos juntos para organizar un mercadillo benéfico en el barrio.;After work, my friends and I work together to organise a charity sale in the neighbourhood.`

La validación de las reglas por línea se detuvo al observarse una regla general incumplida.

## Sesiones completadas para omitir en la siguiente iteración

`PF-A1-001`, `PF-A1-002`, `PF-A1-004`, `PF-A1-005`, `PF-A1-007` y `PF-A1-009`.
