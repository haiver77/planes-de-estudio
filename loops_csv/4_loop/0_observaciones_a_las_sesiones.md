## Resumen del estado por archivo

| Archivo | Estado | Reglas generales incumplidas | Cantidad filas observadas |
|---|---|---|---:|
| `PF-A1-001.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-002.csv` | Observado | Progresion y repetición incremental | 3 |
| `PF-A1-003.csv` | Observado | Progresion y repetición incremental | 4 |
| `PF-A1-004.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-005.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-006.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-007.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-008.csv` | Observado | Progresion y repetición incremental | 5 |
| `PF-A1-009.csv` | Observado | Progresion y repetición incremental | 2 |

Cobertura: 9/9 IDs A1 del plan; hay exactamente un CSV por ID. Los nueve archivos se leyeron como UTF-8 válido, tienen dos columnas sin encabezado separadas por `;`, no presentan filas vacías, campos adicionales ni saltos de línea dentro de campos, y alcanzan el mínimo de 150 frases. La comprobación automatizada no detectó texto corrupto (`Ã`, `�`) ni preguntas en español sin `¿`.

Como todos los archivos incumplen una regla general, no se validaron sus reglas por línea, conforme al criterio de corte.

## PF-A1-001 — Realizar acciones cotidianas, describir un procedimiento breve o comunicar su resultado — `PF-A1-001.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 025 y 033 expresan la misma frase («Ella se prepara por la mañana» / «Por la mañana, ella se prepara»); la segunda solo cambia el orden y no aporta contexto ni progresión. Sustituir una de ellas por un ejemplo natural y distinto que amplíe gradualmente el uso del foco `get ready`.

## PF-A1-002 — Indicar cantidad o grado y resolver una petición sencilla de compra/pago — `PF-A1-002.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 081, 087 y 088 repiten «Mi hermana necesita un poco más de tiempo», añadiendo únicamente «A veces» o «En verano». Sustituir parte de estas variantes por ejemplos con situaciones y estructuras distintas que consoliden el foco `a little more`, en lugar de reiterar la misma idea con modificadores.

## PF-A1-003 — Iniciar/cerrar intercambios cercanos y expresar cortesía, deseo o capacidad — `PF-A1-003.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 061–067 reiteran disculpas por el mismo error o por llegar tarde; varias solo añaden marcadores como «Hoy», «En invierno» o «Durante el viaje» (por ejemplo, filas 061–062 y 066–067). Sustituir parte del bloque por situaciones de disculpa diferentes y ejemplos gradualmente más desarrollados que practiquen el foco `I'm sorry`.

## PF-A1-004 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 1/2) — `PF-A1-004.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 050 y 051 repiten «La parada está allí»; la fila 051 solo agrega «Hoy». Sustituir una de las variantes por un ejemplo con `over there` en un contexto distinto y con progresión relevante.

## PF-A1-005 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 2/2) — `PF-A1-005.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 004 y 009 repiten «Mi padre llega a casa en autobús»; la fila 009 solo añade «A veces». Sustituir una de ellas por un ejemplo que practique `get home` en una situación diferente, no por una variante de frecuencia.

## PF-A1-006 — Responder a situaciones cotidianas con una expresión breve y autónoma — `PF-A1-006.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 066 y 067 repiten «Los alumnos se sientan en la clase»; la fila 067 solo añade «Hoy». Sustituir una variante por un ejemplo distinto y natural que desarrolle el foco `sit down`.

## PF-A1-007 — Situar una rutina o un relato sencillo en el tiempo y expresar frecuencia — `PF-A1-007.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 029 y 032 repiten la misma situación: la clase termina y el hablante se va a casa de inmediato. La fila 032 solo añade que ocurre por la tarde. Sustituir una de ellas por un ejemplo que practique `at once` en un contexto diferente y aporte progresión relevante.

## PF-A1-008 — Coordinar una tarea sencilla y compartir información o una postura breve — `PF-A1-008.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 051, 057 y 059–061 repiten «Voy a la oficina de correos después del trabajo»; las variantes añaden únicamente frecuencia o circunstancias accesorias («A veces», «Cada semana», «Con frecuencia», «En días de lluvia»). Sustituir parte de la serie por ejemplos con contextos y estructuras distintos que consoliden `post office`.

## PF-A1-009 — Describir una situación doméstica o de ocio y expresar una reacción o necesidad cotidiana — `PF-A1-009.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 072 y 073 repiten «Nos divertimos en la fiesta de mi prima»; la fila 073 solo agrega «Hoy». Sustituir una de ellas por un ejemplo con `have fun` en un contexto distinto y con progresión relevante.

## Sesiones completadas para omitir en la siguiente iteración

Ninguna. Las nueve sesiones requieren correcciones y otra iteración.
