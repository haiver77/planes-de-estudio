## Resumen del estado por archivo

| Archivo | Estado | Reglas generales incumplidas | Filas CSV | Filas observadas puntualmente |
|---|---|---|---:|---:|
| `PF-A1-001.csv` | Observado | Progresion y repetición incremental | 160 | 19 |
| `PF-A1-002.csv` | Observado | Progresion y repetición incremental | 186 | 16 |
| `PF-A1-003.csv` | Observado | Progresion y repetición incremental | 268 | 36 |
| `PF-A1-004.csv` | Observado | Progresion y repetición incremental | 184 | 5 |
| `PF-A1-005.csv` | Observado | Progresion y repetición incremental | 165 | 0 |
| `PF-A1-006.csv` | Observado | Progresion y repetición incremental | 211 | 16 |
| `PF-A1-007.csv` | Observado | Progresion y repetición incremental | 176 | 7 |
| `PF-A1-008.csv` | Observado | Progresion y repetición incremental | 167 | 15 |
| `PF-A1-009.csv` | Observado | Progresion y repetición incremental | 167 | 2 |

La cobertura coincide con los nueve ID del plan. Los nueve archivos tienen al menos 150 filas y son legibles como UTF-8, pero hay texto corrupto con el carácter de reemplazo `�` en ocho archivos. No se detectaron filas vacías ni campos adicionales.

## PF-A1-001 — `PF-A1-001.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** A partir de la fila 138 se retoman focos ya vistos, se introducen expresiones ajenas a la lista planificada y se añaden bloques aislados al final (por ejemplo, «feel better», nuevas variantes de «get ready» y «make a mistake», y «take something off»). En los bloques anteriores también hay variantes que solo cambian el marcador temporal. Mantener el orden de los focos del plan y consolidar cada uno con ejemplos graduales y contextos distintos, sin añadir bloques de repaso o expresiones no planificadas.

**Reglas incumplidas por línea**
- **Filas 018, 044, 088, 099, 111, 116, 130, 144 y 150 — Regla: Sin caracteres extraños.** Los fragmentos «�Puedes», «�A qu� hora» y «�D�nde» contienen `�` en lugar de `¿` o letras acentuadas. Restaurar los signos de apertura y caracteres españoles correctos en todas las filas indicadas.
- **Fila 002 — Regla: Frase con sentido.** «Ponerse mejor;Get better» vuelve a presentar el foco aislado después de la fila 001. Reemplazar por: `Mi hermana espera ponerse mejor pronto.;My sister hopes to get better soon.`
- **Fila 007 — Regla: Frase con sentido.** «Perderse;Get lost» repite de forma aislada el foco de la fila 006. Reemplazar por: `Mi hermano no quiere perderse en el centro.;My brother does not want to get lost downtown.`
- **Fila 023 — Regla: Frase con sentido.** «Prepararse;Get ready» repite de forma aislada el foco de la fila 022. Reemplazar por: `Mi hermano se prepara para la escuela.;My brother gets ready for school.`
- **Fila 036 — Regla: Frase con sentido.** «Levantarse;Get up» repite de forma aislada el foco de la fila 035. Reemplazar por: `Mi padre se levanta antes de las siete.;My father gets up before seven.`
- **Fila 051 — Regla: Frase con sentido.** «Cometer un error;Make a mistake» repite de forma aislada el foco de la fila 050. Reemplazar por: `Olvidé la respuesta y cometí un error.;I forgot the answer and made a mistake.`
- **Fila 062 — Regla: Frase con sentido.** «Asegurarse;Make sure» repite de forma aislada el foco de la fila 061. Reemplazar por: `Antes de salir, me aseguro de cerrar la ventana.;Before I leave, I make sure to close the window.`
- **Fila 078 — Regla: Frase con sentido.** «Recoger algo;Pick something up» vuelve a presentar aislado el foco ya introducido en la fila 077. Reemplazar por: `Mi hija recoge sus juguetes del suelo.;My daughter picks her toys up from the floor.`
- **Fila 107 — Regla: Frase con sentido.** «Participar;Take part» repite de forma aislada el foco de la fila 106. Reemplazar por: `Mi amigo participa en el partido de fútbol.;My friend takes part in the football match.`
- **Fila 123 — Regla: Frase con sentido.** «Tener lugar;Take place» repite de forma aislada el foco de la fila 122. Reemplazar por: `El evento tiene lugar en el museo.;The event takes place at the museum.`
- **Fila 158 — Regla: Frase con sentido.** «Quitarse algo;Take something off» vuelve a presentar aislada una variante de «take off» después de su bloque. Reemplazar por: `Me quito los guantes antes de preparar la cena.;I take my gloves off before making dinner.`

## PF-A1-002 — `PF-A1-002.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** En bloques como las filas 018–030 («a bit more») y 045–058 («a little») se repiten estructuras casi idénticas cambiando principalmente el marcador temporal. Además, las filas 182–186 incorporan ejemplos de «too many» y «how much», que no son los focos listados para esta sesión. Variar los contextos y la estructura de los ejemplos para consolidar gradualmente cada foco, y retirar o integrar de forma pertinente el material ajeno al plan.

**Reglas incumplidas por línea**
- **Filas 007, 020, 023, 024, 026, 030, 075, 076, 078, 079, 084, 085, 086, 184, 185 y 186 — Regla: Sin caracteres extraños.** Los fragmentos «�Est� el caf�» y «�Quieres» contienen `�` en lugar de `¿` o letras acentuadas. Restaurar los signos de apertura y caracteres españoles correctos en todas las filas indicadas.

## PF-A1-003 — `PF-A1-003.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** Se anticipan focos antes de su bloque —por ejemplo, «in love» en la fila 005 y «speak to»/«each other» en las filas 017–018— y las filas 251–268 vuelven a introducir focos anteriores después del bloque «phone number». También hay series que solo añaden marcadores temporales. Mantener un foco por bloque, con progresión gradual, y ceñir el cierre de la sesión a los focos planificados.

**Reglas incumplidas por línea**
- **Filas 017, 031–038, 040, 042, 044, 077, 112, 129, 131–132, 138, 143, 145–146, 149, 152, 202, 205, 240, 246–247, 261–262 y 268 — Regla: Sin caracteres extraños.** Los fragmentos «�Puedo», «Perd�n, �puedo» y «�d�nde» contienen `�` en lugar de `¿` o letras acentuadas. Restaurar los signos de apertura y caracteres españoles correctos en todas las filas indicadas.
- **Fila 041 — Regla: Frase con sentido.** «Esta semana, perdón, no entiendo la pregunta» combina el marcador temporal con la interjección de forma poco natural. Reemplazar por: `Perdón, ¿dónde está la salida?;Excuse me, where is the exit?`
- **Fila 058 — Regla: Frase con sentido.** «En días de lluvia, ellos quieren casarse en junio» mezcla circunstancias sin una relación lógica clara. Reemplazar por: `Mis amigos quieren casarse en junio y ya eligieron el lugar.;My friends want to get married in June and have already chosen the venue.`
- **Fila 073 — Regla: Frase con sentido.** «Los lunes, mi hermana está enamorada» presenta un estado afectivo como rutina semanal sin contexto natural. Reemplazar por: `Mi hermana está enamorada de su novio.;My sister is in love with her boyfriend.`
- **Fila 225 — Regla: Frase con sentido.** «Quiero un vaso de agua.;I would like a glass of water» no conserva el matiz de cortesía de «would like». Reemplazar por: `Me gustaría pedir una botella de agua.;I would like to order a bottle of water.`
- **Fila 226 — Regla: Frase con sentido.** «Quiero hablar con el médico.;I would like to speak to the doctor» no conserva el matiz de cortesía de «would like». Reemplazar por: `Quisiera hablar con el médico en privado.;I would like to speak to the doctor in private.`

## PF-A1-004 — `PF-A1-004.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** Las filas 137–184 añaden secuencias de expresiones no incluidas en los focos de esta sesión —por ejemplo, «the class is on Monday», «a long time ago» y «the bus leaves at eight»— y alternan entre focos ya presentados. Reorganizar o retirar estas líneas para mantener el bloque de cada expresión planificada y consolidarlo con ejemplos graduales antes de pasar a otra.

**Reglas incumplidas por línea**
- **Filas 086, 088, 130 y 135 — Regla: Sin caracteres extraños.** Los fragmentos «�Cu�ndo» y «�A qu� hora» contienen `�` en lugar de `¿` o letras acentuadas. Restaurar los signos de apertura y caracteres españoles correctos en todas las filas indicadas.
- **Fila 091 — Regla: Frase con sentido.** «¡Vamos!;Come on!» repite de forma aislada la expresión ya presentada en la fila 090. Reemplazar por: `¡Vamos, el autobús ya está aquí!;Come on, the bus is already here!`

## PF-A1-005 — `PF-A1-005.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** Después del bloque «right now» (filas 146–150), las filas 151–165 vuelven a «on the left», «on the phone» y otras expresiones que no consolidan ese foco ni corresponden a los focos planificados para esta sesión. En los bloques anteriores también se repiten frases con cambios mínimos de tiempo o circunstancia. Mantener los ejemplos agrupados por foco y hacer que cada bloque lo refuerce con contextos variados y una progresión real.

## PF-A1-006 — `PF-A1-006.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** Las filas 174–211 añaden secuencias de focos ajenos a la lista de esta sesión —como «Oh no», «How is your mother?» y «on the right»— y retoman varias expresiones ya tratadas. También hay repeticiones que solo cambian el marcador temporal. Retirar o reorganizar el material para que cada bloque desarrolle un solo foco planificado.

**Reglas incumplidas por línea**
- **Filas 023–030, 115, 144, 175–176, 179 y 187 — Regla: Sin caracteres extraños.** Los fragmentos «�C�mo est�s» y «�La piscina» contienen `�` en lugar de `¿` o letras acentuadas. Restaurar los signos de apertura y caracteres españoles correctos en todas las filas indicadas.
- **Fila 024 — Regla: Frase con sentido.** «¿Cómo estás?;How are you?» repite como fragmento aislado el foco ya presentado en la fila 023. Reemplazar por: `¿Cómo estás después de un día largo?;How are you after a long day?`
- **Fila 040 — Regla: Frase con sentido.** «No hay de qué. Me alegra ayudar.;Not at all. I'm happy to help» traduce «No hay de qué» como «Not at all», aunque significa «You're welcome». Reemplazar por: `El café no me gusta en absoluto.;I do not like coffee at all.`
- **Fila 060 — Regla: Frase con sentido.** «¡Hasta luego! Mi hermana trabaja esta tarde» no establece una relación lógica entre la despedida y la información añadida. Reemplazar por: `¡Hasta luego! Nos vemos después del trabajo.;See you later! See you after work.`

## PF-A1-007 — `PF-A1-007.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** Varios bloques repiten una misma frase con cambios menores de circunstancia y, tras el último foco, las filas 171–176 añaden ejemplos que no refuerzan ninguna de las expresiones listadas. Sustituir las variaciones mecánicas por contextos distintos y graduales, y ceñir el cierre de la sesión a los focos planificados.

**Reglas incumplidas por línea**
- **Filas 068–070, 072, 077 y 087 — Regla: Sin caracteres extraños.** Los fragmentos «Buenos d�as» y «�Tienes» contienen `�` en lugar de letras acentuadas o de `¿`. Restaurar los caracteres españoles y el signo de apertura correctos en todas las filas indicadas.
- **Fila 016 — Regla: Frase con sentido.** «Después de clase, trabajo todo el día en la tienda de mi padre» hace poco coherente que el trabajo dure todo el día después de clase. Reemplazar por: `Los sábados, trabajo todo el día en la tienda de mi padre.;On Saturdays, I work all day in my father's shop.`

## PF-A1-008 — `PF-A1-008.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** El bloque «on the phone» (filas 152–164) repite varios patrones con cambios mínimos de frecuencia o momento; las filas 165–167 añaden intercambios que no consolidan los focos planificados. Variar la estructura y extensión de los ejemplos y evitar añadir secuencias ajenas al plan.

**Reglas incumplidas por línea**
- **Filas 042, 124–133, 136 y 165–167 — Regla: Sin caracteres extraños.** Los fragmentos «�Puedo», «�Tiene» y «�Crees» contienen `�` en lugar de `¿` o letras acentuadas. Restaurar los signos de apertura y caracteres españoles correctos en todas las filas indicadas.
- **Fila 165 — Regla: Frase con sentido.** «¿Crees que sí?;Do you think so?» pregunta si alguien cree algo, mientras que el foco planificado es la afirmación «I think so». Reemplazar por: `Creo que sí, el autobús llega a las ocho.;I think so, the bus arrives at eight.`

## PF-A1-009 — `PF-A1-009.csv` — Observado

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** Las filas 152–167 introducen y repiten «TV show» y «good idea», expresiones que no forman parte de los focos de esta sesión; otras variantes cambian principalmente el marcador temporal. Rehacer este tramo para consolidar los focos planificados con ejemplos independientes, variados y graduales, sin introducir nuevos focos como relleno.

**Reglas incumplidas por línea**
- **Filas 100 y 159 — Regla: Sin caracteres extraños.** Los fragmentos «�Est�s» y «�Qu�» contienen `�` en lugar de `¿` o letras acentuadas. Restaurar los signos de apertura y caracteres españoles correctos en ambas filas.

**Sesiones completadas para omitir de la siguiente iteración:** ninguna. Las nueve sesiones A1 quedan observadas y requieren otra iteración.
