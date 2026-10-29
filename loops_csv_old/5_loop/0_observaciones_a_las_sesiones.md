# Auditoría lingüística y técnica — A1, iteración 4

**Plan aprobado:** `loops_plan/12_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**CSV revisados:** `loops_csv/4_loop/A1/`  
**Mínimo exigido:** 150 pares por CSV  
**Observaciones anteriores consultadas:** `loops_csv/2_loop/0_observaciones_a_las_sesiones.md`, `loops_csv/3_loop/0_observaciones_a_las_sesiones.md` y `loops_csv/4_loop/0_observaciones_a_las_sesiones.md`

## Resultado

**NO COMPLETO. Se requiere otra iteración.** La cobertura, la cantidad y los controles automáticos de estructura y codificación cumplen. Persisten problemas sustanciales de uso del vocabulario, repetición mecánica de marcos, equivalencia y naturalidad, además de errores concretos de traducción y contexto. Estos defectos afectan a muchas sesiones y no se resuelven corrigiendo solo los ejemplos citados.

## Comprobaciones automáticas

- **Cobertura:** el plan contiene 107 ID A1 distintos y existen exactamente `A1-S001.csv`–`A1-S107.csv`; no faltan IDs ni hay archivos ajenos.
- **Cantidad:** los 107 archivos tienen exactamente 150 registros de dos campos cada uno.
- **Formato y UTF-8:** los 107 archivos se decodifican como UTF-8. El análisis estricto confirma dos columnas sin encabezado, separadas por `;`; no se encontraron filas vacías, campos extra, comillas mal cerradas, saltos de línea dentro de campos ni delimitación por comas.
- **Caracteres y preguntas:** no se hallaron `�`, secuencias de mojibake (`Ã¡`, `Ã±`, etc.), `?` sustituyendo letras ni preguntas españolas sin `¿`.
- **Duplicación exacta:** no hay pares idénticos duplicados ni frases españolas repetidas con traducciones distintas dentro de un mismo archivo. Sí hay **119 repeticiones de frases españolas entre archivos con traducciones inglesas distintas** (véase P1).

## Observaciones pendientes priorizadas

### P1 — Persisten miles de filas de plantilla en vez de práctica léxica contextual

En **96 de los 107 archivos**, se encontraron **3.134 filas** que contienen uno o más de estos marcos reutilizados: *“I read about a…”*, *“I learn about a…”*, *“My teacher talks about…”* o *“…is in the picture”*. El conteo identifica filas con esos marcos; no implica que toda mención de una foto o lectura sea incorrecta por sí sola. El problema es su uso serial para llenar los cinco pares de unidades muy distintas, sin enseñar sus sentidos, colocaciones ni funciones comunicativas, en contra del plan, que exige cinco microescenas naturales por unidad y expresamente pide no forzar un único tema.

Ejemplos:

- **`A1-S030.csv`, filas 1–10 y 56–60:** el mismo ciclo de «está en la imagen / leí sobre… / mi maestra habla de… / aprendo sobre…» se aplica a *area*, *arm* y *aunt*. En las filas 2–5, por ejemplo, “Leí sobre un área en mi libro” / “I read about an area in my book” y “Mi maestra habla de un área en la escuela” / “My teacher talks about an area at school” no constituyen cinco usos comunicativos variados del lema.
- **`A1-S011.csv`, filas 46–50:** “Aprendo sobre un hola en clase” / “I learn about a hi in class” trata *hi* como sustantivo contable de manera poco natural; el mismo marco se aplica a *CD*, *TV*, *bag* y *bed*.
- **`A1-S005.csv`, filas 47, 49–50:** “Aprendo sobre un final en clase” / “I learn about an end in class” y “Leí sobre un final en mi libro” / “I read about an end in my book” sustituyen el uso del lema por comentarios vagos sobre él.
- **`A1-S059.csv`, filas 44–45:** “Mi maestra habla de un interés en la escuela” / “My teacher talks about an interest at school” y “Aprendo sobre un interés en clase” / “I learn about an interest in class” repiten el patrón y no modelan de forma idiomática los sentidos y colocaciones de *interest*.

**Cambio requerido:** revisar todas las filas de ese tipo en los 96 archivos, no solo los ejemplos. Reescribir las que mencionan, leen o muestran el lema sin practicar su significado o función. Conservar cinco pares por unidad, pero distribuirlos en escenas distintas y autónomas que usen el sentido, categoría gramatical, colocaciones y complementos previstos por el plan. Comprobar especialmente que las palabras funcionales y las entradas con más de un sentido no se conviertan en objetos de clase o de foto por defecto.

### P1 — Traducciones inglesas incorrectas y traducción inconsistente de una misma frase

Las 119 repeticiones de frases españolas entre archivos no conservan una traducción estable. Hay casos en que una traducción es errónea o no idiomática:

- **`A1-S009.csv:72`, `A1-S042.csv:53`, `A1-S069.csv:58` y `A1-S088.csv:28`:** la misma frase «Ese es un buen lugar para almorzar» se traduce, respectivamente, como “That is a good place for lunch”, “That is a dear place for lunch”, “That is a nice place for lunch” y “That is a strong place for lunch”. **“Dear place”** y **“strong place”** no expresan aquí «buen lugar».
- **`A1-S003.csv:108`, `A1-S060.csv:30` y `A1-S091.csv:30`:** «Lo usamos en casa» se traduce como “We use him at home”, “We use its at home” y “We use that at home”. *Him* no corresponde a «lo» referido a una cosa y *its* no es un objeto directo natural en esa estructura; las versiones no mantienen el mismo referente.
- **`A1-S003.csv:27` y `A1-S004.csv:118`:** «Lo veo en la mesa» aparece como “I see him at the table” y “I see its at the table”; el referente y el pronombre inglés son incorrectos o no están expresados de forma gramatical.
- **`A1-S061.csv:92`:** «Los niños van a la escuela el domingo» se traduce como “The children happen at school on Sunday”, que cambia el verbo y no conserva el sentido.
- **`A1-S023.csv:45` y `A1-S038.csv:57`:** «Mi hermana está en la ciudad ahora» se traduce como “My sister is at the town now” y “My sister is at the city now”; ambas preposiciones son inadecuadas para el sentido de estar en una ciudad.

**Cambio requerido:** corregir cada par incorrecto y revisar equivalencia en toda la colección, no solo las frases repetidas. Mantener el mismo referente, persona, número, tiempo, intención y cortesía en ambos idiomas; cotejar especialmente pronombres de objeto, verbos y preposiciones. No reutilizar traducciones de una frase sin verificar que correspondan a su versión española concreta.

### P1 — El bloque de integración de S107 aún contiene contexto defectuoso y redundancia

La duplicación literal de la taza que se señaló en la iteración anterior ya no aparece; sin embargo, siguen pendientes problemas en el bloque final:

- **`A1-S107.csv:43`:** «En casa, en casa, mi amiga mira la foto los sábados» / “At home, at home, my friend looks at the picture on Saturdays” repite innecesariamente el complemento de lugar.
- **`A1-S107.csv:44`:** «En casa el lunes, los niños pierden mis llaves el domingo» / “At home on Monday, the children lose my keys on Sunday” mezcla sin propósito los marcos «el lunes» y «el domingo» y deja una localización temporal poco clara para una frase de integración.
- **`A1-S107.csv:13`:** «El viernes por la tarde, el domingo pasado cenamos en casa» / “On Friday afternoon, we ate dinner at home last Sunday” añade un marco de viernes que no se integra con la acción del domingo anterior; reescribir en una situación temporal natural y sin adorno de plantilla.

**Cambio requerido:** revisar el bloque de integración de S107, eliminar duplicaciones de complementos y asegurar que cada modificador temporal o espacial corresponda claramente al evento. Mantener el pasado simple previsto por el plan con marcadores temporales coherentes.

### P2 — Persisten pares poco naturales o semánticamente débiles para unidades concretas

- **`A1-S031.csv:21–24`:** “La habitación está mal hoy” / “The room is bad today”, “Mi bolso nuevo está malo” / “My new bag is bad” y “La flor es mala” / “The flower is bad” no expresan de forma natural una propiedad adecuada de *bad*. Las traducciones literales no permiten distinguir si se habla de mal estado, mala calidad u otra valoración.
- **`A1-S059.csv:21`:** “Cada mañana mejoro mi inglés con mi familia” / “I improve my English with my family every morning” fuerza un complemento poco claro para *improve*; la práctica debería especificar una actividad o contexto plausible. Revisar también el resto del bloque de *improve* para que las cinco filas no sean variaciones mecánicas.
- En el material se repiten con frecuencia escenas con días, lugares y actividades añadidos de forma independiente al sentido de la frase. Aunque cada campo pueda decodificarse y estar bien delimitado, esos añadidos producen secuencias poco creíbles y dificultan que cada fila funcione como unidad autónoma.

**Cambio requerido:** reescribir las frases afectadas con un referente y una situación concretos, conservar el sentido de la entrada fuente y hacer que los complementos sean idiomáticos en ambas lenguas. Revisar las series completas de cinco frases por lema, así como la progresión de cortas a largas y la transferencia contextual; no limitarse a cambiar una palabra dentro del mismo molde.

## Resolución de observaciones anteriores

- **Resuelto parcialmente:** los marcos explícitos sobre «la expresión» y los dos ejemplos exactos de manzanas/sillas que se citaron como relleno ya no están repetidos masivamente; las comprobaciones exactas no encuentran duplicados de pares.
- **Resuelto:** la traducción uniforme “Are you getting on?” que aparecía en `A1-S007.csv` fue reemplazada por preguntas distintas y pertinentes.
- **Resuelto parcialmente:** las primeras frases sobre *autumn/away* en `A1-S031.csv` ahora son naturales y completas; en `A1-S059.csv` se corrigieron los errores concretos de *if*, *imagine* y el artículo de *important* previamente citados.
- **No resuelto en el fondo:** el defecto transversal de plantillas y práctica metalingüística persiste en forma de nuevos marcos repetidos —fotos, lecturas, aprendizaje y explicaciones del profesor— en 96 CSV. También persisten errores nuevos de equivalencia y naturalidad. La corrección de ejemplos aislados no satisface la observación de revisar integralmente el uso de cada unidad.
- **Resuelto parcialmente:** ya no se detecta el duplicado exacto de S107 citado en el informe anterior, pero hay redundancia local y problemas de contexto temporal nuevos en el mismo archivo.

## Cambio requerido para la siguiente iteración

Revisar los 107 CSV frente a sus unidades, repaso y foco gramatical; rehacer las 3.134 filas identificadas por patrones cuando no practiquen el uso real de la unidad; corregir los pares de traducción divergente e inglés incorrecto; reconstruir las frases señaladas de S031, S059 y S107; y efectuar una nueva lectura lingüística fila por fila. Mantener exactamente un archivo por cada ID, UTF-8, dos columnas sin encabezado separadas por `;` y al menos 150 pares por archivo.
