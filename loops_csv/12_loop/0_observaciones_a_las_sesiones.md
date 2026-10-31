## Resumen del estado por archivo

| Archivo | Estado | Reglas generales incumplidas | Cantidad filas observadas |
|---|---|---|---:|
| `PF-A1-001.csv` | Completado | Ninguna | 0 |
| `PF-A1-002.csv` | Observado | Progresion y repetición incremental | 1 |
| `PF-A1-003.csv` | Observado | Progresion y repetición incremental | 5 |
| `PF-A1-004.csv` | Observado | Progresion y repetición incremental | 4 |
| `PF-A1-005.csv` | Completado previamente; omitido | Ninguna | 0 |
| `PF-A1-006.csv` | Observado | Progresion y repetición incremental | 8 |
| `PF-A1-007.csv` | Completado previamente; omitido | Ninguna | 0 |
| `PF-A1-008.csv` | Observado | Progresion y repetición incremental | 1 |
| `PF-A1-009.csv` | Completado previamente; omitido | Ninguna | 0 |

## PF-A1-001 — Realizar acciones cotidianas, describir un procedimiento breve o comunicar su resultado — `PF-A1-001.csv` — Completado

**Reglas generales por archivo incumplidas**

- Ninguna. Se verificaron cobertura, formato y codificación UTF-8, y el mínimo de 150 frases: contiene 150 filas.

**Reglas incumplidas por línea**

- Ninguna.

## PF-A1-002 — Indicar cantidad o grado y resolver una petición sencilla de compra/pago — `PF-A1-002.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La fila 083, «Antes de cenar, quiero un poco más de arroz», repite la petición de la fila 074, «Quiero un poco más de arroz», agregando solo el momento. Reemplazar la fila 083 por: `La receta necesita un poco más de mantequilla para que la masa quede suave.;The recipe needs a bit more butter to keep the dough soft.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-003 — Iniciar/cerrar intercambios cercanos y expresar cortesía, deseo o capacidad — `PF-A1-003.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.**
  - **Fila 092:** «Antes de cenar, ella escucha música en casa» repite la escena de la fila 084, «Ella escucha música en casa», añadiendo solo el momento. Reemplazar por: `En el parque, ella escucha el canto de los pájaros.;In the park, she listens to the birds singing.`
  - **Fila 203:** «Durante el viaje, esperamos el tren juntos en la estación» repite la escena de la fila 196, «Esperamos el tren juntos en la estación», añadiendo solo el contexto temporal. Reemplazar por: `Durante el viaje, esperamos la confirmación de la reserva en el hotel.;During the trip, we wait for the booking confirmation at the hotel.`
  - **Fila 232:** «Durante el viaje, quiero un vaso de agua» repite la petición de la fila 231, «Por la noche, quiero un vaso de agua», cambiando únicamente el momento/contexto. Reemplazar por: `En el restaurante, quiero un vaso de agua sin hielo.;At the restaurant, I would like a glass of water without ice.`
  - **Fila 238:** «Después de clase, queremos una mesa cerca de la ventana» repite la misma petición de la fila 229, «Queremos una mesa cerca de la ventana», añadiendo solo el momento. Reemplazar por: `Después de clase, queremos comprar un refrigerio en la cafetería.;After class, we would like to buy a snack at the café.`
  - **Fila 249:** «Durante el viaje, ella escribe mi número de teléfono» repite la acción de la fila 242, «Ella escribe mi número de teléfono», añadiendo solo el contexto temporal. Reemplazar por: `Mi hermana escribe el número de la reserva en su agenda.;My sister writes the booking number down in her diary.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-004 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 1/2) — `PF-A1-004.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.**
  - **Fila 064:** «Caminamos todo el camino hasta la escuela» repite la ruta de la fila 063, «Voy caminando desde casa hasta la escuela», con la misma acción y destino. Reemplazar por: `Caminamos todo el camino hasta el mirador para ver la puesta de sol.;We walk all the way to the viewpoint to watch the sunset.`
  - **Fila 074:** «La ruta del autobús llega hasta el aeropuerto» repite el trayecto al aeropuerto de la fila 071, «El autobús va desde el centro hasta el aeropuerto». Reemplazar por: `El tren atraviesa todo el valle hasta llegar al pueblo.;The train goes all the way through the valley to the town.`
  - **Fila 124:** «El pueblo está lejos, pero el autobús para allí» repite la escena de la fila 123, «El pueblo está lejos, pero el autobús llega allí», cambiando solo la acción del autobús. Reemplazar por: `La playa está lejos del hotel, pero el autobús llega hasta la entrada.;The beach is far away from the hotel, but the bus goes all the way to the entrance.`
  - **Fila 144:** «El tren regresa a la estación por la noche» repite la escena de la fila 142, «El tren vuelve a la estación de origen a medianoche», cambiando solo el momento. Reemplazar por: `El autobús regresa al depósito al final de la ruta.;The bus gets back to the depot at the end of the route.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-005 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 2/2) — `PF-A1-005.csv` — Completado previamente; omitido

Sesión completada previamente; se omitió de esta revisión.

## PF-A1-006 — Responder a situaciones cotidianas con una expresión breve y autónoma — `PF-A1-006.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.**
  - **Fila 025:** «¿Cómo estás hoy?» repite la pregunta de la fila 023, «¿Cómo estás?», añadiendo solo el momento. Reemplazar por: `¿Cómo estás después de recibir el resultado del examen?;How are you after hearing the exam result?`
  - **Fila 040:** El foco «not at all» tiene un solo ejemplo (fila 040) antes de introducir el siguiente foco. Añadir varios ejemplos graduales en contextos distintos; por ejemplo: `No me preocupa en absoluto el examen.;I am not worried about the exam at all.`
  - **Fila 101:** «Preferimos quedarnos en casa esta noche» repite la misma escena de la fila 100, «Nos quedamos en casa esta noche». Reemplazar por: `Mi padre se queda en casa para cuidar a mi abuela después de su operación.;My father stays in to look after my grandmother after her operation.`
  - **Filas 118 y 120:** «Los niños nadan en la piscina del hotel durante las vacaciones» y «En días de lluvia, los niños nadan en la piscina del hotel» repiten la escena de la fila 116, «Los niños nadan en la piscina del hotel», añadiendo solo circunstancias temporales. Reemplazar la fila 118 por: `La piscina del hotel tiene una zona poco profunda para los niños.;The hotel swimming pool has a shallow area for children.` Reemplazar la fila 120 por: `Los niños esperan a sus padres en la piscina del hotel después de nadar.;The children wait for their parents at the hotel swimming pool after swimming.`
  - **Fila 142:** «La estación de tren está en el centro de la ciudad» repite la ubicación de la fila 141, «La estación está en el centro de la ciudad», añadiendo solo «de tren». Reemplazar por: `El ayuntamiento organiza un mercado al aire libre en el centro de la ciudad.;The council holds an outdoor market in the town centre.`
  - **Fila 146:** «El autobús va al centro de la ciudad» repite el trayecto de la fila 139, «Vamos al centro de la ciudad en autobús». Reemplazar por: `Los turistas se pierden en el centro de la ciudad sin un mapa.;Tourists get lost in the town centre without a map.`
  - **Fila 152:** «Me despierto a las siete cada mañana» repite la hora de la fila 151, «Me despierto a las siete», añadiendo solo la frecuencia. Reemplazar por: `Me despierto cuando suena el despertador de mi teléfono.;I wake up when my phone alarm rings.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-007 — Situar una rutina o un relato sencillo en el tiempo y expresar frecuencia — `PF-A1-007.csv` — Completado previamente; omitido

Sesión completada previamente; se omitió de esta revisión.

## PF-A1-008 — Coordinar una tarea sencilla y compartir información o una postura breve — `PF-A1-008.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La fila 083, «Mi hermana y yo trabajamos juntas en el jardín los sábados», repite el escenario de la fila 077, «Mi hermana y yo trabajamos juntas en el jardín», añadiendo solo la frecuencia. Reemplazar por: `Mi hermana y yo trabajamos juntas en el refugio de animales para limpiar las jaulas.;My sister and I work together at the animal shelter to clean the cages.`

La validación por línea se detuvo al observarse una regla general incumplida.

## PF-A1-009 — Describir una situación doméstica o de ocio y expresar una reacción o necesidad cotidiana — `PF-A1-009.csv` — Completado previamente; omitido

Sesión completada previamente; se omitió de esta revisión.

## Sesiones completadas para omitir en la siguiente iteración

- `PF-A1-001` — completada en esta revisión.
- `PF-A1-005` — completada previamente.
- `PF-A1-007` — completada previamente.
- `PF-A1-009` — completada previamente.
