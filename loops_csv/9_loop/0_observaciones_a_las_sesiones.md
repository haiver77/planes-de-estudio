## Resumen del estado por archivo

| Archivo | Estado | Reglas generales incumplidas | Cantidad filas observadas |
|---|---|---|---:|
| `PF-A1-001.csv` | Observado | Progresion y repetición incremental | 4 |
| `PF-A1-002.csv` | Observado | Progresion y repetición incremental | 4 |
| `PF-A1-003.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-004.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-005.csv` | Completado | Ninguna | 0 |
| `PF-A1-006.csv` | Observado | Progresion y repetición incremental | 4 |
| `PF-A1-007.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-008.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-009.csv` | Completado | Ninguna | 0 |

## PF-A1-001 — Realizar acciones cotidianas, describir un procedimiento breve o comunicar su resultado — `PF-A1-001.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 038 y 048 repiten que el padre se levanta temprano; la fila 048 solo antepone «Por la mañana», información redundante que no crea otra situación. Reemplazar la fila 048 por: `Mi padre se levanta temprano para pasear al perro antes del desayuno.;My father gets up early to walk the dog before breakfast.`
- **Regla: Progresion y repetición incremental.** Las filas 095 y 104 repiten que ella se quita los zapatos; la fila 104 solo añade «Por la mañana» sin aportar un contexto distinto. Reemplazar la fila 104 por: `Después del paseo, ella se quita los zapatos en la entrada.;After the walk, she takes off her shoes in the hall.`

## PF-A1-002 — Indicar cantidad o grado y resolver una petición sencilla de compra/pago — `PF-A1-002.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 003 y 012 repiten exactamente «El café está un poco frío» / “The coffee is a bit cold”. Reemplazar la fila 012 por: `La sopa está un poco salada.;The soup is a bit salty.`
- **Regla: Progresion y repetición incremental.** Las filas 143 y 147 repiten que se ahorra dinero cada mes; anteponer «Antes de cenar» no añade un contexto relevante a esa misma acción. Reemplazar la fila 147 por: `Ahorro dinero para comprar entradas para el concierto.;I save money to buy tickets for the concert.`

## PF-A1-003 — Iniciar/cerrar intercambios cercanos y expresar cortesía, deseo o capacidad — `PF-A1-003.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 002 y 007 repiten que el mejor amigo vive cerca; «cerca de mi casa» solo explicita la misma ubicación y no introduce otra situación. Reemplazar la fila 007 por: `Mi mejor amigo me espera a la salida de la escuela.;My best friend waits for me outside the school.`

## PF-A1-004 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 1/2) — `PF-A1-004.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 052 y 054 repiten exactamente «La entrada del museo está por allí, junto a la fuente» / “The museum entrance is over there, next to the fountain”. Reemplazar la fila 054 por: `La parada de taxis está por allí, frente al hotel.;The taxi rank is over there, in front of the hotel.`

## PF-A1-005 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 2/2) — `PF-A1-005.csv` — Completado

Sin reglas generales por archivo ni reglas por línea incumplidas.

## PF-A1-006 — Responder a situaciones cotidianas con una expresión breve y autónoma — `PF-A1-006.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 009 y 010 repiten que el bebé se queda dormido en el coche durante el viaje; la fila 010 solo reordena la misma información. Reemplazar la fila 010 por: `El bebé se queda dormido en el coche mientras la madre canta una canción.;The baby falls asleep in the car while the mother sings a song.`
- **Regla: Progresion y repetición incremental.** Las filas 089 y 098 repiten que los niños se ponen de pie en el aula; la fila 098 solo añade «Después de clase» y no aporta otro contexto relevante. Reemplazar la fila 098 por: `Los niños se ponen de pie para cantar una canción en el aula.;The children stand up to sing a song in the classroom.`

## PF-A1-007 — Situar una rutina o un relato sencillo en el tiempo y expresar frecuencia — `PF-A1-007.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 076 y 087 repiten la misma situación de tener tiempo para tomar un café; el cambio de sujeto y de modalidad (afirmación/pregunta) no aporta un contexto distinto. Reemplazar la fila 087 por: `¿Tienes tiempo para ayudarme a preparar la cena?;Do you have time to help me make dinner?`

## PF-A1-008 — Coordinar una tarea sencilla y compartir información o una postura breve — `PF-A1-008.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 066 y 069 repiten que el hermano trabaja duro en la tienda; «Antes de cenar» solo cambia el momento de la misma escena. Reemplazar la fila 069 por: `Mi hermano trabaja duro en la tienda para ordenar las estanterías.;My brother works hard at the shop to organise the shelves.`

## PF-A1-009 — Describir una situación doméstica o de ocio y expresar una reacción o necesidad cotidiana — `PF-A1-009.csv` — Completado

Sin reglas generales por archivo ni reglas por línea incumplidas.

## Sesiones completadas para omitir en la siguiente iteración

- `PF-A1-005`
- `PF-A1-009`
