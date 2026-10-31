## Resumen del estado por archivo

| Archivo | Estado | Reglas generales incumplidas | Cantidad filas observadas |
|---|---|---|---:|
| `PF-A1-001.csv` | Observado | Progresion y repetición incremental | 1 |
| `PF-A1-002.csv` | Observado | Progresion y repetición incremental | 1 |
| `PF-A1-003.csv` | Observado | Progresion y repetición incremental | 6 |
| `PF-A1-004.csv` | Observado | Progresion y repetición incremental | 1 |
| `PF-A1-005.csv` | Completado previamente; omitido | Ninguna | 0 |
| `PF-A1-006.csv` | Observado | Progresion y repetición incremental | 1 |
| `PF-A1-007.csv` | Observado | Ninguna | 1 |
| `PF-A1-008.csv` | Observado | Progresion y repetición incremental | 1 |
| `PF-A1-009.csv` | Completado | Ninguna | 0 |

Los ocho CSV abiertos del nivel tienen codificación UTF-8 válida, dos columnas sin encabezado, al menos 150 filas y no presentan filas vacías ni caracteres de reemplazo. La cobertura de IDs abiertos es completa. `PF-A1-005` ya estaba completado en la revisión anterior y se omitió.

## PF-A1-001 — Realizar acciones cotidianas, describir un procedimiento breve o comunicar su resultado — `PF-A1-001.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La fila 068, «Antes de salir, compruebo que tengo las llaves», repite la escena de la fila 064, «Me aseguro de llevar las llaves antes de salir», con una paráfrasis de la misma comprobación. Sustituir la fila 068 por: `Antes de empezar el examen, me aseguro de que tengo un lápiz y una goma.;Before the exam starts, I make sure I have a pencil and an eraser.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-002 — Indicar cantidad o grado y resolver una petición sencilla de compra/pago — `PF-A1-002.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La fila 113, «Durante el viaje, el tren sale en media hora», repite la misma escena de la fila 104, «El tren sale en media hora»; solo añade el contexto temporal del viaje. Sustituir la fila 113 por: `El museo cierra en media hora, así que terminamos la visita.;The museum closes in half an hour, so we finish our visit.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-003 — Iniciar/cerrar intercambios cercanos y expresar cortesía, deseo o capacidad — `PF-A1-003.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.**
  - **Fila 068:** «Después del trabajo, lo siento, no tengo tu libro» repite la situación del libro de la fila 069, «Lo siento, olvidé devolverte el libro ayer». Sustituir por: `Lo siento, olvidé avisarte que la reunión cambió de hora.;I'm sorry, I forgot to tell you the meeting time changed.`
  - **Fila 094:** «Después de clase, ella escucha música en casa» repite la misma escena de la fila 092, «Antes de cenar, ella escucha música en casa», cambiando únicamente el momento. Sustituir por: `Después de clase, ella escucha los anuncios de la estación antes de tomar el tren.;After class, she listens to the station announcements before taking the train.`
  - **Fila 109:** «Esta mañana, ella mira a su hermano» repite la escena de la fila 103, «Ella mira a su hermano», añadiendo solo el momento. Sustituir por: `Ella mira a su hermano mientras él presenta su proyecto.;She looks at her brother while he presents his project.`
  - **Fila 116:** «Después de clase, los estudiantes miran la foto en la pared» repite la escena de la fila 111, «Los estudiantes miran la foto en la pared», añadiendo solo el momento. Sustituir por: `Los estudiantes miran las notas del experimento para comparar resultados.;The students look at the experiment notes to compare results.`
  - **Fila 217:** «Esta mañana, puedo nadar» repite la misma capacidad de la fila 215, «Puedo nadar», añadiendo solo el momento. Sustituir por: `Puedo preparar una ensalada para la cena.;I am able to make a salad for dinner.`
  - **Fila 222:** «Antes de cenar, mi hermano puede leer este libro» repite la capacidad y el objeto de la fila 220, «Mi hermano puede leer este libro», añadiendo solo el momento. Sustituir por: `Mi hermano puede arreglar la bicicleta de su amiga.;My brother is able to repair his friend's bicycle.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-004 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 1/2) — `PF-A1-004.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La fila 081, «Mi padre vuelve a casa después del trabajo», repite la escena de la fila 079, «Mi padre vuelve del trabajo en autobús»: ambas describen el mismo regreso del padre del trabajo. Sustituir la fila 081 por: `Mi padre vuelve a la cocina para apagar el horno.;My father comes back to the kitchen to turn off the oven.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-005 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 2/2) — `PF-A1-005.csv` — Completado previamente; omitido

Completado en la iteración anterior; se omite de esta revisión.

## PF-A1-006 — Responder a situaciones cotidianas con una expresión breve y autónoma — `PF-A1-006.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La fila 052, «En días de lluvia, veo a un agente de policía cerca del banco», repite la escena de la fila 044, «Veo a un agente de policía cerca del banco», cambiando solo la circunstancia temporal. Sustituir la fila 052 por: `Un agente de policía devuelve una mochila perdida a su dueña en la estación.;A police officer returns a lost backpack to its owner at the station.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-007 — Situar una rutina o un relato sencillo en el tiempo y expresar frecuencia — `PF-A1-007.csv` — Observado

**Reglas generales por archivo incumplidas**

- Ninguna.

**Reglas incumplidas por línea**

- **Fila 125 — Regla: Sin caracteres extraños.** «El espectéculo comenzó a tiempo a pesar de la lluvia» tiene la tilde mal colocada en «espectáculo». Sustituir por: `El espectáculo comenzó a tiempo a pesar de la lluvia.;The show started on time despite the rain.`

## PF-A1-008 — Coordinar una tarea sencilla y compartir información o una postura breve — `PF-A1-008.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La fila 129, «Creo que sí, el café está abierto por la noche y cierra a las diez», repite la escena de la fila 128 sobre el horario de apertura y cierre del mismo café, cambiando únicamente el horario. Sustituir la fila 129 por: `Creo que sí, la farmacia está abierta porque veo gente dentro.;I think so, the pharmacy is open because I can see people inside.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-009 — Describir una situación doméstica o de ocio y expresar una reacción o necesidad cotidiana — `PF-A1-009.csv` — Completado

No se observaron incumplimientos de las reglas generales por archivo ni de las reglas por línea.

## Sesiones completadas para omitir en la siguiente iteración

- `PF-A1-005` — completada en la iteración anterior.
- `PF-A1-007` — completada en esta revisión.
- `PF-A1-009` — completada en esta revisión.
