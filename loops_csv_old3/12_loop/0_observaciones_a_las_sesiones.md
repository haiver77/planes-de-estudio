# Auditoría lingüística y técnica — A1, loop 11

**Plan aprobado e inmutable cotejado:** `planes_aprobados/oxford_phrase_list/plan_frases_oxford.md`  
**Lista de regresión revisada íntegramente:** `loops_csv/10_loop/0_observaciones_a_las_sesiones.md`  
**Alcance:** PF-A1-002 a PF-A1-009. PF-A1-001 queda excluida por estar previamente aprobada.

## Comprobaciones técnicas, nombres y cobertura

- En `loops_csv/11_loop/A1/` hay exactamente ocho CSV: uno por cada ID PF-A1-002 a PF-A1-009; no hay IDs solicitados ausentes ni CSV adicionales.
- Los ocho nombres coinciden literalmente con la columna `CSV planificado` del plan: `frases_PF-A1-002_v1.csv` a `frases_PF-A1-009_v1.csv`.
- Se verificaron individualmente con decodificación UTF-8 estricta y parser CSV: PF-A1-002: **173** filas; PF-A1-003: **249**; PF-A1-004: **172**; PF-A1-005: **153**; PF-A1-006: **194**; PF-A1-007: **158**; PF-A1-008: **155**; PF-A1-009: **156**. Todos cumplen el mínimo explícito de 150.
- Los ocho archivos tienen dos campos no vacíos por fila, sin encabezado, separados por un solo `;`. No se detectaron filas vacías, campos adicionales, comillas mal cerradas, saltos de línea dentro de registros, caracteres de reemplazo, mojibake ni `?` sustituyendo letras. Los signos diacríticos españoles están codificados correctamente; las preguntas en español incluyen apertura `¿` y cierre `?`.
- Las expresiones foco de las sesiones están representadas. Las observaciones pendientes se refieren a gramática A1, autonomía, equivalencia contextual, naturalidad y variedad; se detallan por archivo y fila abajo.

## Observaciones — requieren corrección

### Prioridad alta — alcance A1, autonomía y coherencia

1. **`frases_PF-A1-002_v1.csv`, fila 55:** `Quedan unos pocos minutos antes de que empiece la película.;There are a few minutes before the film starts.` La subordinada española `antes de que empiece` exige subjuntivo, fuera del nivel A1 declarado. Sustituirla por una construcción A1 (por ejemplo, dos oraciones simples con indicativo) y conservar el sentido de que queda poco tiempo.

2. **`frases_PF-A1-003_v1.csv`:**
   - **Filas 120 y 123:** `Cada semana/Con frecuencia, ellos quieren casarse en junio.;Every week/Often, they want to get married in June.` Aplicar frecuencia a la misma intención de casarse en junio resulta poco verosímil y parece una variante mecánica. Cambiar los contextos para que la frecuencia tenga una razón comunicativa o reemplazar una de las filas por otro foco de la sesión.
   - **Fila 151:** `Cada semana, mi número de teléfono es nuevo.;Every week, my phone number is new.` No expresa una situación natural. Reformular con una idea verosímil relacionada con el número de teléfono o usar otro foco.
   - **Fila 173:** `A veces, ella habla con su madre cada día.;Sometimes, she speaks to her mother every day.` `A veces` contradice `cada día`. Elegir un solo marco de frecuencia y alinear ambas columnas.
   - **Fila 206:** `Él dice la verdad. Es difícil.;He tells the truth. It is difficult.` La sustitución eliminó el subjuntivo del ejemplo anterior, pero `Es difícil/It is difficult` queda sin referente y la relación entre las oraciones no se entiende de forma autónoma. Reescribir con una conexión explícita y natural, sin salir de A1.

3. **`frases_PF-A1-006_v1.csv`:**
   - **Fila 104:** `Hoy, mi hermana se queda en casa el sábado.;Today, my sister stays in on Saturday.` Se acumulan `hoy/today` y `el sábado/on Saturday` sin aclarar que hoy sea sábado; la fila queda temporalmente ambigua. Conservar un solo marco o indicar de forma inequívoca que se habla del mismo día.
   - **Filas 161 y 162:** `En verano/Esta semana, los niños se ponen de pie en el aula.;In summer/This week, the children stand up in the classroom.` Los marcos temporales no dan una razón natural para la acción. Reemplazar por contextos que expliquen el acto de ponerse de pie; no variar solo el prefijo temporal.
   - **Fila 173:** `Después del trabajo, los niños nadan en la piscina del hotel.;After work, the children swim in the hotel swimming pool.` El contexto de trabajo para niños no resulta verosímil. Cambiarlo por una situación coherente con la edad/sujeto o por otro ejemplo que practique el foco.

4. **`frases_PF-A1-007_v1.csv`:**
   - **Fila 92:** `Esta mañana, la próxima vez, llevo mi paraguas.;This morning, next time, I take my umbrella.` `Esta mañana` y `la próxima vez` no forman aquí un marco temporal coherente. Retirar uno y redactar una oración completa y natural.
   - **Filas 96 y 101:** ejemplos como `A veces/A menudo, primero que nada, leo...;Sometimes/Often, first of all, I read...` acumulan frecuencia y orden inicial sin una relación comunicativa clara. Reescribir para que cada fila use de manera natural el foco de frecuencia o el de secuenciación, sin yuxtaponerlos mecánicamente.

5. **`frases_PF-A1-008_v1.csv`, filas 26, 27, 51, 79, 81, 91, 100, 113, 116, 126, 128 y 134–138:** las frases con `Creo que sí...;I think so...` se presentan sin la pregunta o afirmación previa a la que responde `sí/so`; por ejemplo, fila 26: `Creo que sí, el café está abierto.;I think so, the café is open.` La respuesta no es autónoma, requisito de las indicaciones. Incorporar en la misma fila una pregunta/afirmación antecedente que permita usar `I think so`, o reformular las frases que no practiquen ese foco.

6. **`frases_PF-A1-009_v1.csv`:**
   - **Fila 76:** `Durante el viaje, cenamos en casa los viernes.;During the trip, we have dinner at home on Fridays.` El viaje y cenar habitualmente en casa quedan en conflicto sin contexto explicativo. Sustituir uno de los marcos o proporcionar una situación que los haga compatibles.
   - **Fila 115:** `En días de lluvia, ¡Qué pena! El parque está cerrado.;On rainy days, too bad! The park is closed.` La exclamación se inserta con mayúscula y puntuación impropias en mitad de la oración. Integrarla correctamente (por ejemplo, `En días de lluvia, ¡qué pena! ...`) y ajustar la traducción para conservar la misma estructura.
   - **Fila 123:** `Esta mañana, visitamos a nuestros abuelos el fin de semana.;This morning, we visit our grandparents at the weekend.` Se combinan `esta mañana` y `el fin de semana` sin que se indique que ambos marcos coincidan. Elegir un solo momento o aclarar la situación.
   - **Fila 140:** `Durante el viaje, la sala de estar tiene una ventana grande.;During the trip, the living room has a big window.` El viaje no guarda relación clara con la descripción de una sala de estar y hace que la fila parezca un prefijo de relleno. Dar un contexto coherente o retirar el marco.

### Prioridad media — naturalidad, variedad y repetición mecánica

7. **`frases_PF-A1-002_v1.csv`, filas 142, 152 y 154:** se repite `mi hermano trabaja mucho más en verano / my brother works a lot more in summer` añadiendo `A veces`, `Cada semana` y `Con frecuencia`. La frecuencia semanal/ocasional no aporta una situación distinta y su combinación con el aumento estacional resulta forzada. Mantener el vocabulario de cantidad, pero crear ejemplos distintos y contextualizados.

8. **`frases_PF-A1-003_v1.csv`:**
   - **Filas 66, 78 y 129:** `Cada semana/Con frecuencia/En días de lluvia, gracias por el té.;Every week/Often/On rainy days, thank you for the tea.` Los marcos de frecuencia/clima no encajan naturalmente con una fórmula de agradecimiento autónoma. Eliminar esos añadidos o incluir una situación completa que los justifique.
   - **Filas 144, 163 y 169:** ejemplos como `Cada semana/Antes de cenar/Después de clase, perdón, no entiendo la pregunta.` insertan marcos temporales arbitrarios en expresiones formulaicas. Convertirlos en intercambios situacionales naturales o sustituir las variantes repetidas por contextos útiles.

9. **`frases_PF-A1-004_v1.csv`:**
   - **Filas 61, 73 y 87:** ejemplos como `Por la noche, mi madre trabaja el lunes`, `Durante el viaje, mi madre trabaja el lunes` y `En días de lluvia, la clase es el lunes` combinan marcos que no aportan contexto lógico a la acción/horario y dan impresión de relleno.
   - **Fila 119:** `Los lunes, el autobús sale el lunes a las ocho.;On Mondays, the bus leaves on Monday at eight.` Repite el mismo marco temporal en ambas columnas. **Fila 154** (`Por la tarde, el autobús sale el lunes a las ocho`) agrega además una hora del día sin relación clara con la salida fijada para el lunes. Reescribir estas filas con un solo marco temporal pertinente y diversificar los ejemplos.

10. **`frases_PF-A1-005_v1.csv`, fila 120:** `Después de clase, me voy a la cama a las diez.;After class, I go to bed at ten.` Sin contexto de clase nocturna, resulta poco natural como ejemplo independiente. Dar un contexto que justifique irse a dormir a esa hora o sustituir la combinación por una situación cotidiana más verosímil.

11. **`frases_PF-A1-006_v1.csv`:**
   - **Fila 55:** `Los niños crecen con el cuidado y el cariño.;Children grow up with care and love.` La formulación española es poco idiomática. Reformular con una combinación natural en español y equivalente en inglés, conservando el foco `grow up`.
   - **Fila 154:** `Después del trabajo, hoy en día, estudio inglés en casa.;After work, these days, I study English at home.` `Después del trabajo` y `hoy en día` se acumulan sin aportar contraste útil. Mantener un solo marco y variar el contexto de la expresión.

## Regresión y sesiones para la siguiente iteración

- Se resolvieron varios hallazgos de la lista anterior: los nombres de archivo ahora coinciden literalmente con el plan; se corrigieron los ejemplos con subjuntivo señalados en PF-A1-009 (filas 70, 77 y 82); se mejoraron las preguntas y marcos temporales de PF-A1-004; se corrigieron las filas temporales de PF-A1-005 y PF-A1-006; y los ejemplos de `I mean` de PF-A1-008 presentan ahora más variedad.
- No se observan regresiones técnicas de formato, codificación, cobertura ni cantidad. Persisten problemas lingüísticos y de naturalidad, y hay hallazgos nuevos especificados por fila en este informe.
- **Sesiones completadas que pueden omitirse en la siguiente iteración:** ninguna de PF-A1-002 a PF-A1-009.
- **Sesiones que requieren otra iteración y validación:** PF-A1-002, PF-A1-003, PF-A1-004, PF-A1-005, PF-A1-006, PF-A1-007, PF-A1-008 y PF-A1-009.
- PF-A1-001 permanece previamente aprobada, excluida de este alcance y puede seguir omitiéndose.

## Indicación al orquestador

Informe: `loops_csv/12_loop/0_observaciones_a_las_sesiones.md`. **Se requiere otra iteración** para corregir las observaciones lingüísticas indicadas y volver a validar PF-A1-002 a PF-A1-009. No modificar el plan aprobado, PF-A1-001 ni artefactos de loops anteriores.
