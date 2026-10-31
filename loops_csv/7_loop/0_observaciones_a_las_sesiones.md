## Resumen del estado por archivo

| Archivo | Estado | Reglas generales incumplidas | Cantidad filas observadas |
|---|---|---|---:|
| `PF-A1-001.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-002.csv` | Observado | Progresion y repetición incremental | 4 |
| `PF-A1-003.csv` | Observado | Progresion y repetición incremental | 7 |
| `PF-A1-004.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-005.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-006.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-007.csv` | Observado | Progresion y repetición incremental | 2 |
| `PF-A1-008.csv` | Observado | Progresion y repetición incremental | 3 |
| `PF-A1-009.csv` | Observado | Progresion y repetición incremental | 4 |

**Comprobaciones mecánicas y cobertura:** el plan contiene nueve IDs A1 y existen exactamente los nueve archivos correspondientes, de `PF-A1-001.csv` a `PF-A1-009.csv`; no hay IDs faltantes, extra ni inválidos. Todos se decodifican como UTF-8 estricto, tienen dos columnas sin encabezado separadas por `;`, no tienen filas vacías ni delimitadores/campos adicionales, y alcanzan el mínimo de 150 filas. Conteos: 150, 181, 250, 150, 150, 173, 170, 164 y 151. La búsqueda mecánica no encontró caracteres de reemplazo, firmas de texto corrupto ni preguntas en español sin `¿`.

**Corte de validación:** los nueve archivos incumplen una regla general. Conforme a las indicaciones, no se continuó con la revisión de las reglas por línea en ninguno de ellos. El informe del ciclo 6 se contrastó como lista de regresión; los hallazgos que siguen corresponden a las filas actuales.

## PF-A1-001 — Realizar acciones cotidianas, describir un procedimiento breve o comunicar su resultado — `PF-A1-001.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 063 («Asegúrate de cerrar la puerta») y 070 («Antes de dormir, asegúrate de cerrar la puerta») repiten la misma instrucción y escena; la segunda solo añade el momento. Sustituir una de las variantes por un ejemplo que practique el foco en una situación distinta y aporte contexto relevante.

## PF-A1-002 — Indicar cantidad o grado y resolver una petición sencilla de compra/pago — `PF-A1-002.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 094 y 096 repiten exactamente «Este abrigo cuesta mucho más que la camisa»; las filas 106 y 107 repiten exactamente «La película dura media hora». Reemplazar una fila de cada pareja por ejemplos distintos que consoliden el vocabulario foco en contextos nuevos, en lugar de duplicar la misma escena.

## PF-A1-003 — Iniciar/cerrar intercambios cercanos y expresar cortesía, deseo o capacidad — `PF-A1-003.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.**
  - Las filas 004 y 014 repiten la escena «Mi mejor amigo toca la guitarra en una banda» sin añadir contexto.
  - Las filas 142 («Quiero hablar con mi profesor») y 148 («Antes de cenar, quiero hablar con mi profesor») mantienen la misma conversación y solo varían el momento.
  - Las filas 155 («Ellos hablan de su familia»), 161 («Antes de cenar, ellos hablan de su familia») y 162 («Después de clase, ellos hablan de su familia») reiteran la misma escena cambiando únicamente el marco temporal.

  Sustituir las variantes reiterativas por ejemplos que practiquen los focos con interlocutores, propósitos, acciones u objetos distintos y una progresión contextual real.

## PF-A1-004 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 1/2) — `PF-A1-004.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 041 («Los niños juegan en la playa») y 048 («Después de clase, los niños juegan en la playa») describen la misma acción y escena; solo cambia el momento. Sustituir una de ellas por un ejemplo que use el foco en un contexto distinto, no limitado a variar el marco temporal.

## PF-A1-005 — Pedir/dar direcciones y situar personas, lugares o datos en un contexto cotidiano (parte 2/2) — `PF-A1-005.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 050 («Mi madre va a casa a pie desde el trabajo») y 053 («Mi madre vuelve a casa a pie después del trabajo») repiten el mismo trayecto, participante y medio de transporte; cambia la formulación, pero no se aporta un contexto nuevo. Reemplazar una por un ejemplo del foco que represente una situación diferente.

## PF-A1-006 — Responder a situaciones cotidianas con una expresión breve y autónoma — `PF-A1-006.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 033 («Avísame al llegar a casa») y 034 («Avísame cuando llegues a casa») expresan la misma petición y tienen la misma traducción inglesa («Let me know when you get home»). Reemplazar una por un ejemplo de «let me know» en una situación distinta, con contexto nuevo.

## PF-A1-007 — Situar una rutina o un relato sencillo en el tiempo y expresar frecuencia — `PF-A1-007.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 124 («Mi hermano siempre llega a tiempo a clase») y 150 («Esta mañana, mi hermano llega a tiempo a clase») conservan la misma acción, participante y destino; solo cambia la referencia temporal. Sustituir una por un ejemplo que practique el foco en una escena diferente y no se limite a cambiar el momento.

## PF-A1-008 — Coordinar una tarea sencilla y compartir información o una postura breve — `PF-A1-008.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** Las filas 003 («Mis amigos están en la escuela»), 015 («Antes de cenar, mis amigos están en la escuela») y 016 («Después de clase, mis amigos están en la escuela») repiten la misma escena y participantes, variando únicamente el marco temporal. Reemplazar al menos las variantes reiterativas por ejemplos de «at school» en situaciones distintas y con contenido contextual relevante.

## PF-A1-009 — Describir una situación doméstica o de ocio y expresar una reacción o necesidad cotidiana — `PF-A1-009.csv` — Observado

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.**
  - Las filas 031 («¡Buena suerte en tu entrevista!») y 037 («¡Buena suerte en tu entrevista de trabajo!») repiten la misma situación con una reformulación, sin aportar contexto nuevo.
  - Las filas 096 («Desayunamos en casa los domingos») y 101 («Mi familia desayuna en casa los domingos») describen la misma escena, sin añadir información contextual relevante.

  Sustituir una variante de cada pareja por ejemplos que mantengan los focos, pero aporten participantes, propósitos, acciones o situaciones diferentes.

## Sesiones completadas para omitir en la siguiente iteración

Ninguna. Los nueve archivos quedan observados.
