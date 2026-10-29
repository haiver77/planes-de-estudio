# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración de entrada:** 31  
**Mínimo obligatorio:** 150 pares por CSV  
**Plan aprobado:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Alcance exclusivo:** `loops_csv/31_loop/A1/A1-S001.csv` a `A1-S005.csv`.

## Evidencia comprobada

- **Cobertura y cantidad:** existen exactamente los cinco IDs solicitados en el directorio auditado, sin faltantes ni archivos ajenos al alcance. Cada CSV tiene 150 pares (750 en total), cumple el mínimo y no tiene encabezado.
- **Bytes, UTF-8 y formato:** se leyeron los bytes reales y se decodificaron con UTF-8 estricto, sin BOM. Tamaños: S001 13.941 bytes; S002 14.895; S003 14.480; S004 15.349; S005 15.629. `csv.reader` en modo estricto devuelve 150 registros por archivo. Cada uno tiene 150 líneas físicas, exactamente un `;` por línea y dos campos no vacíos; no hay filas vacías, campos extra, comillas mal cerradas, saltos incrustados ni líneas delimitadas por coma. No aparecen U+FFFD ni secuencias de mojibake; todas las preguntas en español llevan `¿` de apertura y no se detectó `?` sustituyendo letras.
- **Repetición exacta:** no hay pares duplicados ni frases españolas o inglesas duplicadas entre los 750 registros. Sí hay repeticiones cercanas de contexto que requieren atención en las observaciones siguientes.
- **Plan, catálogo y secuencia:** se cotejaron las 12 unidades nuevas de cada sesión con el catálogo, en bloques de cinco filas (60 pares nuevos por CSV). Los repasos previstos contienen 12/12 unidades: S002 filas 61–72 (S001); S003 filas 61–72 (S002); S004 filas 61–72 (S003) y 73–84 (S001); S005 filas 61–72 (S004) y 73–84 (S002). Se revisaron los 30 pares gramaticales de cada sesión, alineados con G01–G05, y las cantidades de integración del plan: 60, 48, 48, 36 y 36. Los grupos de cinco ejemplos crecen en longitud en ambos idiomas; las observaciones señalan los casos donde la extensión no resulta suficientemente natural o útil.
- **Revisión focalizada de las diez correcciones del informe 31:** S005-21 conserva la cita exacta de la fuente en pasado una sola vez; S005-22–25 usan presente simple y no se detectó otro pasado simple productivo en la sesión. S004-4/5 ya expresa distancia con *far away from*. S005-49/50 aporta ejemplos verificables diferentes para *end in* y una extensión informativa. S002-25 amplía *all day* con una consecuencia plausible. S003-28–30 y 33–35 sitúan objetos o acciones de forma verosímil *at the end / at the end of*; S003-38–40 ordena naturalmente *at the moment* y añade acciones; S003-49/50 evita repetir el marcador temporal y amplía el plan de mudanza; S004-23–25 varía los aspectos negativos del invierno y los contextos. En S001-38–40 sí se concretó la acción de llamar a Ana y se añadió contexto, pero la construcción inglesa aún necesita naturalidad (observación 1).
- **Historial:** se cotejaron el informe de entrada 31 y las observaciones pertinentes de los informes 30 y 29. Se mantienen corregidos, entre otros, S001-24/25; S002-30, 33–35 y 49/50; S003-70/105/149 y la posesión de S003-126; S004-4/5, 8–10, 34–35 y 44–45; S005-4/5, 20, 48–50, 57/58; y los ejemplos históricos de S002-48/49 y S005-18/19/23/82. S003-23–25 conserva una repetición cercana del ejemplo de evento escolar que conviene resolver junto con la observación 4.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta

1. **A1-S001.csv, filas 38–40 — inglés poco idiomático en la progresión de *That’s a good idea*.**  
   `¡Esa es una buena idea: llamar a Ana desde casa esta tarde!;That is a good idea: calling Ana from home this afternoon!` La idea y la secuencia de contexto están presentes, pero el giro inglés con dos puntos seguido de un gerundio suena forzado; las filas 39–40 prolongan la misma construcción. **Cambio requerido:** mantener la acción concreta y su ampliación lógica, pero formular el inglés con una cláusula natural y completa, conservando el sentido y la cortesía del español sin recurrir a un imperativo.

2. **A1-S004.csv, filas 14–15 — contexto ambiguo y acumulación poco natural en *bad news*.**  
   `Es una mala noticia para mi familia hoy sobre el viaje antes de la cena.;It is bad news for my family today about the trip before dinner.` No se identifica qué noticia afecta al viaje, y `antes de la cena / before dinner` queda como circunstancia añadida sin relación clara. **Cambio requerido:** expresar una noticia concreta y verosímil sobre el viaje, y ubicar el momento de forma inequívoca; hacer que la fila 15 amplíe información útil en vez de añadir otro complemento suelto.

3. **A1-S005.csv, fila 60 — sintaxis ambigua y orden poco natural.**  
   `Mi teléfono celular está aquí sobre la mesa para la llamada junto a las llaves antes de salir.;My cell phone is here on the table for the call beside the keys before we leave.` No queda claro si el teléfono, la llamada o las llaves están junto a qué elemento, y `for the call` no tiene un contexto establecido. **Cambio requerido:** reformular ambas columnas para indicar claramente dónde están el teléfono y las llaves y qué llamada se hará antes de salir, en una oración natural y autónoma.

### Prioridad media

4. **A1-S003.csv, filas 23 y 25 — repetición cercana y léxico difícil para A1.**  
   Ambas filas describen el mismo evento escolar y repiten que los estudiantes presentan una canción para sus familias; la fila 25 añade `proyecto solidario / class charity project`, una expresión poco básica para este nivel. **Cambio requerido:** variar uno de los contextos para que haya transferencia real y sustituir esa expresión por vocabulario sencillo, manteniendo el foco *at the beginning of* y una ampliación significativa.

5. **A1-S005.csv, filas 29–30 — colocación inglesa mejorable y extensión de relleno.**  
   `Las diferencias entre el té y el café son claras para los niños en esta clase con ejemplos sencillos durante la actividad.;The differences between tea and coffee are clear for children in this class with simple examples during the activity.` En inglés, `clear for children` resulta menos idiomático que `clear to the children`; además, la fila 30 conserva la misma comparación y solo añade `during the activity`, sin aportar una transferencia o información relevante. **Cambio requerido:** usar una colocación inglesa natural y hacer que la quinta frase añada un uso, resultado o contexto concreto, no solo otra circunstancia.

6. **A1-S002.csv, filas 54–55 — redundancia temporal y progresión débil.**  
   `Un viaje alrededor del mundo es emocionante para mi familia en verano con dos amigos durante las vacaciones.;A trip around the world is exciting for my family in summer with two friends during the holidays.` `En verano / in summer` y `durante las vacaciones / during the holidays` se solapan; la segunda fila apenas repite la misma escena con un marcador temporal adicional. **Cambio requerido:** conservar una sola referencia temporal y ampliar con un detalle distinto y pertinente sobre el viaje o los participantes.

7. **A1-S003.csv, filas 44–45 — orden inglés poco natural y acumulación de circunstancias.**  
   `Ellos llegan al mismo tiempo a la estación hoy con sus amigos antes de la cena.;They arrive at the same time at the station today with their friends before dinner.` En inglés, la secuencia `at the same time at the station` resulta pesada; las filas 44–45 mantienen la misma oración y la última solo agrega `before dinner`. **Cambio requerido:** colocar primero el destino (`arrive at the station at the same time`) y hacer que la extensión aporte un dato o consecuencia útil, no otro marcador temporal aislado.

8. **A1-S003.csv, fila 25 y A1-S004.csv, filas 34–35 — complejidad léxica/sintáctica alta para A1.**  
   Además de la expresión señalada en la observación 4, aparecen `brief update on the project's progress`, `graduation dinner` y `a toast from the principal` en ejemplos largos de *begin with*. Son contextos menos cotidianos y contienen vocabulario y estructuras por encima de lo necesario para practicar estas unidades iniciales. **Cambio requerido:** sustituirlos por situaciones familiares y vocabulario A1, conservando *begin with* y una progresión que añada significado sin depender de cláusulas o conceptos avanzados.

**Resultado:** permanecen observaciones lingüísticas, de progresión y adecuación al nivel. Corregirlas y volver a auditar únicamente A1-S001.csv a A1-S005.csv en la iteración siguiente.
