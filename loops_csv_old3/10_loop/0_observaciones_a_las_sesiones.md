# Informe de auditoría lingüística y técnica — A1, loop 9

**Plan aprobado e inmutable cotejado:** `planes_aprobados/oxford_phrase_list/plan_frases_oxford.md`  
**Lista de regresión revisada íntegramente:** `loops_csv/9_loop/0_observaciones_a_las_sesiones.md`  
**Alcance:** PF-A1-002 a PF-A1-009. PF-A1-001 queda excluida y no se modificó ni volvió a auditar.

## Comprobaciones técnicas y de cobertura

- En `loops_csv/9_loop/A1/` hay exactamente un archivo por cada ID solicitado: `PF-A1-002.csv` a `PF-A1-009.csv`; no hay IDs ausentes ni CSV adicionales en esa carpeta.
- Se validó cada archivo con decodificación UTF-8 estricta y parser CSV estricto. Todos tienen dos columnas no vacías, sin encabezado, separadas por un solo `;` por fila; no hay filas vacías, comillas, campos adicionales ni registros multilínea. No se detectaron `�`, secuencias de mojibake ni `?` sustituyendo letras españolas. Los signos de interrogación españoles llevan apertura `¿`.
- **Mínimo de 150 frases verificado individualmente:** PF-A1-002: 173; PF-A1-003: 249; PF-A1-004: 172; PF-A1-005: 153; PF-A1-006: 194; PF-A1-007: 158; PF-A1-008: 155; PF-A1-009: 156. Las ocho sesiones cumplen el mínimo numérico.
- Las expresiones foco se encuentran representadas en sus CSV; las observaciones pendientes son de nombre de archivo, sintaxis/naturalidad, autonomía, variedad y nivel gramatical.

## Observaciones pendientes — requieren corrección

### Prioridad alta — fidelidad técnica al nombre planificado

1. **Nombres de archivo — los ocho IDs.** La columna `CSV planificado` del plan aprobado especifica `frases_PF-A1-002_v1.csv` … `frases_PF-A1-009_v1.csv`; los archivos de esta iteración se llaman `PF-A1-002.csv` … `PF-A1-009.csv`. La correspondencia por ID es inequívoca y la ruta solicitada para esta auditoría contiene los ocho archivos, pero los nombres no son los nombres literales indicados en el plan. El orquestador debe resolver y documentar cuál convención rige el directorio de iteración, sin modificar el plan inmutable ni crear duplicados por ID.

### Prioridad alta — gramática por encima del alcance A1 declarado

2. **PF-A1-003.csv, fila 206:** `Él dice la verdad aunque sea difícil.;He tells the truth even when it is difficult.` La subordinada española usa subjuntivo (`sea`), fuera del alcance A1 declarado. Sustituirla por una formulación A1 con indicativo y traducción equivalente, o separar la idea sin subjuntivo.

3. **PF-A1-004.csv, fila 50:** `¡Vamos, llegaremos tarde al partido!;Come on, we will be late for the match!` Usa futuro simple (`llegaremos / will be`) que no pertenece a la gramática foco de esta sesión (preposiciones, ubicaciones, preguntas con *where*, *there + be* e imperativos de orientación). Reformular con estructuras A1 previstas, conservando el uso natural de *come on!*.

4. **PF-A1-005.csv, filas 60, 111, 130 y 132:** `Vamos a volver al parque después de comer.;We go back to the park after lunch.` (y variantes con `Esta semana`, `Antes de cenar`, `Después de clase`). `Ir a + infinitivo` no figura en la gramática foco y, además, el español expresa futuro mientras el inglés está en presente simple. Sustituir por una construcción del alcance de la sesión y alinear el tiempo verbal en ambas columnas; no replicar la misma frase añadiéndole marcos temporales.

5. **PF-A1-006.csv, fila 86:** `Mi hermana te llamará esta tarde.;My sister will call you this afternoon.` Introduce futuro simple no declarado en el foco de esta sesión. Reformular con presente simple y un contexto compatible con la despedida, o con otra estructura A1 del plan.

6. **PF-A1-006.csv, fila 87:** `Eso es, ya compramos los billetes para el tren.;That is it, we have already bought the train tickets.` La traducción inglesa usa *present perfect* (`have already bought`), mientras el español está en pretérito (`compramos`); además, la sesión declara presente simple, *be/have* y expresiones formulaicas. Cambiar a una oración con la gramática declarada y correspondencia temporal inequívoca.

7. **PF-A1-009.csv, filas 70, 77 y 82:** ejemplos como `¡Qué pena que la piscina esté cerrada hoy!`, `¡Qué pena que el parque cierre tan temprano!` y `¡Qué pena que el programa termine esta noche!` usan subjuntivo presente (`esté`, `cierre`, `termine`), por encima del nivel A1 declarado. Mantener el sentido de *too bad* con una estructura de A1, por ejemplo una reacción breve seguida de una oración en indicativo.

### Prioridad alta — sintaxis, traducción o naturalidad que impiden usar la fila de forma autónoma

8. **PF-A1-004.csv, filas 125, 130 y 138:** `¿A qué hora regresa tu familia del viaje A veces?`, `… En verano?`, `… Esta semana?` / `What time does your family get back from the trip Sometimes/In summer/This week?` Los marcos temporales se añadieron después de la pregunta y la traducción inglesa queda agramatical. Reescribir cada fila como pregunta completa y natural, con el marco integrado correctamente o eliminado; revisar mayúscula y puntuación en ambas columnas.

9. **PF-A1-005.csv:**
   - **Fila 57:** `Hoy, ella vuelve a la escuela el lunes.;Today, she goes back to school on Monday.` Combina `hoy` y `el lunes` sin que el contexto diga que hoy es lunes. Escoger un único marco temporal coherente.
   - **Fila 39:** `Los lunes, el tren sale ahora mismo.;On Mondays, the train leaves right now.` Mezcla un horario habitual con `ahora mismo`. Reescribir como hábito o como salida inmediata, no ambas cosas.
   - **Filas 83 y 91:** `Cada semana/Con frecuencia, gira a la izquierda en la calle.;Every week/Often, turn left in the street.` La frecuencia no funciona con una instrucción puntual de dirección y `en la calle` no identifica claramente el cruce. Crear instrucciones de ruta situadas y utilizables por separado, o usar la expresión de frecuencia en una oración declarativa.
   - **Filas 23, 68, 90 y 94:** `La farmacia está a la izquierda` aparece sola o con añadidos temporales (`Esta semana`, `Antes de cenar`, `Después de clase`), pero no dice a la izquierda de qué punto y los añadidos no aportan una situación útil. Añadir un referente espacial claro (por ejemplo, la estación) y retirar los marcos irrelevantes.

10. **PF-A1-006.csv:**
    - **Fila 8:** `¿Cómo está tu madre Hoy?;How is your mother Today?` Corrige la mayúscula interna (`hoy/today`) y elimina la inserción mecánica.
    - **Fila 47:** `¿Cómo estás hoy En días de lluvia?;How are you today On rainy days?` Combina `hoy` con `en días de lluvia` de manera redundante y deja mayúsculas/puntuación impropias. Reformular como una sola pregunta natural, por ejemplo eligiendo uno de los dos marcos.
    - **Filas 53, 58 y 65:** `A veces/En verano/Con frecuencia, la piscina está abierta hoy.;Sometimes/In summer/Often, the swimming pool is open today.` Se repite la misma cláusula con marcos incompatibles o redundantes entre hábito/temporada y un día concreto. Reemplazar por frases distintas y coherentes, no limitarse a permutar el adverbio.

11. **PF-A1-007.csv:**
    - **Fila 82:** `A veces, esta vez, mi amigo llega temprano.` Combina frecuencia con un caso puntual; conservar un solo marco.
    - **Fila 99:** `Esta semana, esta vez, tengo la respuesta correcta.` Acumula dos marcos temporales equivalentes; simplificar y crear una variante con contenido nuevo.
    - **Fila 111:** `Hoy, mi hermano siempre llega a tiempo a clase.` Contrapone un día concreto con un hábito permanente; elegir entre `hoy` y `siempre`.
    - **Fila 115:** `Antes de cenar, digo buenos días a los clientes.` El saludo de la mañana no concuerda con el momento previo a la cena. Cambiar el saludo o el marco horario.
    - **Filas 152 y 153:** `Por la noche/Después del trabajo, primero que nada, mi hermana prepara el desayuno.` Los contextos fuerzan una actividad rutinaria de desayuno en horario impropio. Reformular con un momento coherente y retirar las combinaciones artificiales.

### Prioridad media — progresión, variedad y repetición mecánica

12. **PF-A1-002.csv, filas 55, 72 y 120:** ejemplos como `En invierno, tengo unos pocos libros`, `Por la noche, tengo unos pocos libros` y `Por la tarde, tenemos muchos libros en casa` agregan marcos de tiempo que no aportan contexto útil a la cantidad que se practica. Revisar estas variantes y las similares: conservar la repetición del cuantificador, pero situarlo en una situación natural que lo justifique. La fila 102 (`A veces, ¿quieres un poco más de leche?;Sometimes, would you like a bit more milk?`) también requiere una formulación más idiomática en inglés o un contexto que justifique la pregunta ocasional.

13. **PF-A1-004.csv, filas 70 y 76:** `Antes de cenar/Después de clase, mi sueño se hace realidad` y sus traducciones repiten el mismo foco con tiempos añadidos que no construyen una situación verosímil. Variar el sujeto/resultado y mantener solo contextos que tengan relación lógica con que un sueño se haga realidad. Hay repeticiones semejantes en las variantes de esta expresión; no alcanzar la cantidad requerida mediante prefijos intercambiables.

14. **PF-A1-008.csv, filas 17, 30, 36, 40, 63, 84, 90, 103, 124, 130, 133 y 150:** el problema anterior de `I mean` sin antecedente se corrigió: ahora las frases explicitan una primera afirmación y su rectificación. Sin embargo, las doce apariciones usan prácticamente el mismo molde `A, quiero decir, B`. Variar la función y el patrón de aclaración en inglés y español, manteniendo el contexto necesario dentro de cada fila y sin añadir frases de relleno.

## Regresión y sesiones para la siguiente iteración

- Se resolvieron hallazgos del informe anterior: PF-A1-002 ya no presenta corrupción de caracteres; PF-A1-003 corrigió `eél` y las preguntas con texto incrustado; PF-A1-007 eliminó los ejemplos anteriores de `ir a + infinitivo` señalados en las filas 107 y 147; PF-A1-008 da ahora contexto explícito a las rectificaciones con `I mean`; las preguntas malformadas anteriores de PF-A1-006 fueron sustituidas.
- Persisten los problemas de combinación mecánica de marcos temporales y falta de naturalidad, especialmente en PF-A1-004, PF-A1-005, PF-A1-006 y PF-A1-007; los ejemplos concretos y las filas vigentes se detallan arriba.
- **Sesiones completadas que pueden omitirse en la siguiente validación:** ninguna de PF-A1-002 a PF-A1-009.
- **Sesiones que requieren otra validación:** PF-A1-002, PF-A1-003, PF-A1-004, PF-A1-005, PF-A1-006, PF-A1-007, PF-A1-008 y PF-A1-009.
- PF-A1-001 sigue previamente aprobada, permanece excluida del alcance y puede omitirse sin volver a revisarla.

## Indicación al orquestador

Informe: `loops_csv/10_loop/0_observaciones_a_las_sesiones.md`. **Se requiere otra iteración** para resolver las observaciones y volver a validar PF-A1-002 a PF-A1-009. No modificar PF-A1-001, el plan aprobado ni los artefactos de loops anteriores.
