# Auditoría lingüística y técnica A1 — loop 8

**Plan aprobado e inmutable cotejado:** `c:\GIT\english-learning-program\planes_aprobados\oxford_phrase_list\plan_frases_oxford.md`  
**Lista de regresión:** `loops_csv\8_loop\0_observaciones_a_las_sesiones.md`  
**Archivos revisados:** PF-A1-002 a PF-A1-009. PF-A1-001 queda fuera de esta auditoría, según indicación.

## Comprobaciones verificadas por script

- Cobertura de este alcance: los ocho CSV previstos (`PF-A1-002` a `PF-A1-009`) están presentes, uno por ID, sin archivos adicionales en `loops_csv\8_loop\A1`.
- Los ocho archivos decodifican como UTF-8 estricto. Cada uno tiene dos campos no vacíos por fila, sin encabezado, separados por un solo `;`. No hay filas vacías, campos adicionales, comillas dobles, BOM ni delimitadores de coma; no se detectaron saltos de línea incrustados, `�` ni secuencias de mojibake `Ã…`.
- **Mínimo explícito de 150 aplicado individualmente:** PF-A1-002: 169 filas; PF-A1-003: 245; PF-A1-004: 169; PF-A1-005: 150; PF-A1-006: 192; PF-A1-007: 155; PF-A1-008: 152; PF-A1-009: 153. Todos alcanzan el mínimo actual. PF-A1-005 está justo en el mínimo; cualquier eliminación requiere reemplazo para conservar 150 frases.
- Se confirmó que las expresiones foco se trabajan en las sesiones correspondientes; los problemas pendientes son de ortografía, gramática, correspondencia, autonomía, naturalidad, variedad y fidelidad a las instrucciones del plan.

## Observaciones pendientes

### Prioridad alta — resolver antes de aprobar

1. **PF-A1-002 — `frases_PF-A1-002_v1.csv`: caracteres `?` sustituyen letras españolas.** Hay 28 filas afectadas: **59, 69, 70, 73, 83, 87, 89, 93, 96, 102, 119, 120, 127, 128, 130, 132, 138, 139, 141, 145, 147, 150, 151, 159, 161, 162, 166 y 169**. Ejemplos: fila 59 `Esta ma?ana`; fila 87 `Despu?s`; fila 119 `En d?as de lluvia`. Restaurar las letras y tildes correctas en el español; el CSV es UTF-8 válido, pero esos signos `?` son corrupción textual, no puntuación válida.

2. **PF-A1-003 — `frases_PF-A1-003_v1.csv`: error ortográfico reiterado.** Filas **172, 175, 204, 206, 221 y 222** escriben `eél`; corregir a `Él` y conservar la traducción concordante.

3. **PF-A1-003 — preguntas convertidas en combinaciones no naturales.** En filas **92, 96, 111, 114, 158, 177, 181, 196, 208, 224, 231 y 233** se añade un marco temporal o de frecuencia al final de una pregunta sin puntuación ni sintaxis adecuados. Ejemplo, fila 158: `¿puedo hablar con el médico ahora Cada semana?;can I speak to the doctor now Every week?`. Reescribir como pregunta autónoma y natural o separar el marco temporal en otra frase coherente; corregir también mayúsculas y puntuación de ambas columnas.

4. **PF-A1-006 — preguntas mutiladas por inserciones de contexto.** Filas **5, 13, 21, 29, 45 y 53** contienen construcciones como `¿cómo estás A veces?;how are you Sometimes?`. No basta con mayúsculas: hay que rehacerlas como preguntas idiomáticas en ambos idiomas, con el adverbio ubicado correctamente o eliminado.

5. **PF-A1-007 — persiste una estructura fuera del foco gramatical declarado.** Filas **107** (`mi familia va a visitar`) y **147** (`mis amigos van a estudiar`) usan `ir a + infinitivo` / `be going to`. El plan de esta sesión declara presente y pasado simple según el foco. Reformular ambas con gramática y objetivo temporal previstos; la observación previa sobre esta estructura no quedó resuelta y reaparece en dos filas.

### Prioridad alta — autonomía, naturalidad y variedad (regresión persistente)

La observación principal del informe anterior **no está resuelta**. Se sustituyeron muchos prefijos de lugar por adverbios temporales, de frecuencia o situación, pero continúa la producción mecánica de variantes de una misma frase. En numerosas filas el añadido es redundante, contradictorio o no guarda relación con la expresión foco. La meta explícita del plan exige frases independientes y naturales, sin combinar focos como relleno; rehacer los grupos afectados con ejemplos genuinamente distintos, autónomos y pertinentes, no limitarse a cambiar el prefijo.

- **PF-A1-002:** filas **78** (`Esta semana ... cada mes`), **84** (`Cada semana ... hoy`) y **86/123** (acumulan `esta semana/antes de cenar`, `ahora` y `hoy`). Hay incompatibilidades o redundancias entre marcos de tiempo; rehacer esas frases para que expresen una única situación temporal natural. La inserción de contextos también deja la mayor parte del archivo como variaciones de cláusulas ya vistas.
- **PF-A1-003:** además de las preguntas señaladas, frases recurrentes reciben prefijos de tiempo que no añaden contexto útil. Ejemplo, fila **148**: `Los lunes, mis padres se casaron en verano`, que combina una fecha repetitiva con un acontecimiento pasado singular. Revisar las variantes con `Los lunes`, `Esta semana`, `Durante el viaje`, etc. y mantener únicamente las que sean coherentes y practicables por separado.
- **PF-A1-004:** la serie de variantes de `¡Vamos!` no es autónoma ni natural: filas **36, 45 y 50** añaden `A veces`, `En verano` o `Con frecuencia` a `¡Vamos, el autobús está aquí!`; también se repite este patrón con marcos temporales en filas **86, 116, 117, 122, 152 y 153**. Retirar las inserciones incompatibles y crear ejemplos de uso real de `come on!`. La fila **121** (`Esta mañana, el autobús sale el lunes a las ocho`) también mezcla marcos temporales que no concuerdan.
- **PF-A1-005:** filas **17** (`Hoy, mis amigos se van mañana`), **18/24** (`Cada semana/Con frecuencia, voy a casa ahora`) y **41** (`Esta mañana, mis amigos se van mañana`) mezclan o fuerzan los marcos temporales. Revisar además frases como la fila **116** (`Después del trabajo, llegamos a casa después de la escuela`) y **119** (`Antes de cenar, me voy a la cama a las diez`): el marco añadido produce una situación poco verosímil y no ayuda a practicar el foco. Reemplazar por ejemplos coherentes.
- **PF-A1-006:** persiste la yuxtaposición de expresiones formulaicas y marcos ajenos. Ejemplos: filas **37, 65, 79, 87, 90, 99, 114 y 119** anteponen referencias temporales a `Hasta luego` o a una despedida seguida de `nos vemos mañana`; filas **134** (`Los lunes ... el sábado`) y **170** (`En invierno, hoy en día ...`) tienen marcos redundantes o incompatibles. Rehacer los grupos; asimismo, fila **144** sitúa a alumnos “durante el viaje” sentados “en la clase”, combinación que necesita una situación lógica distinta.
- **PF-A1-007:** hay repeticiones y cruces temporales sin propósito: fila **69** repite `Esta mañana` dos veces; fila **113** combina `Esta mañana` y `todos los días`; fila **131** dice `Por la tarde ... por la mañana`; fila **140** junta `Esta semana` y `el próximo año`; fila **130** antepone `Después del trabajo` a `el año pasado`. Revisar estos casos y las variantes similares, usando un solo marco temporal que concuerde con el verbo y la frase.
- **PF-A1-008:** el problema previamente señalado de `I mean` sin antecedente persiste. Filas **17, 30, 36, 40, 63, 84, 85, 90, 103, 124 y 133** presentan `Quiero decir...` sin proporcionar antes, dentro de la propia unidad, qué afirmación se aclara. Ejemplo, fila 17: `Quiero decir que podemos ir mañana`. Reformular como oración independiente que establezca el contexto o practique la expresión en un intercambio completo. También corregir la incoherencia de la fila **77**: `Cada semana, las buenas noticias llegan esta mañana`.
- **PF-A1-009:** se repiten expresiones reactivas con marcos que no funcionan como frases independientes: filas **28, 41, 48 y 90** anteponen frecuencia o clima a `Buena suerte en tu examen`; filas **70, 77 y 82** hacen lo mismo con `¡Qué pena! El parque está cerrado`. Reformularlas en situaciones de uso natural, no añadir adverbios mecánicamente. Hay incompatibilidades adicionales en filas **99** (`Hoy ... el fin de semana`) y **128** (`Los lunes ... el fin de semana`); alinear los marcos temporales.

### Prioridad media — ortografía y presentación en inglés

En todas las sesiones el pronombre inglés de primera persona aparece como `i` minúscula al inicio de la oración. Corregirlo a `I` en estas filas:

- **PF-A1-002:** 2, 23, 26, 36, 43, 50, 52, 53, 55, 59, 62, 64, 66, 69, 70, 72, 76, 78, 80, 86, 90, 93, 99, 100, 102, 104, 110, 114, 115, 118, 120, 123, 127, 128, 132, 133, 134, 138, 139, 140, 145, 147.
- **PF-A1-003:** 5, 14, 23, 26, 29, 39, 41, 46, 53, 60, 64, 65, 85, 87, 95, 98, 102, 107, 119, 130, 135, 141, 157, 165.
- **PF-A1-004:** 53, 57, 58, 59, 65, 94, 95, 110, 118, 129, 136, 143, 147, 157, 160.
- **PF-A1-005:** 18, 19, 20, 21, 24, 26, 28, 33, 35, 38, 45, 49, 51, 53, 58, 59, 70, 71, 77, 99, 119, 120.
- **PF-A1-006:** 36, 58, 62, 63, 72, 74, 78, 83, 86, 89, 92, 96, 97, 98, 102, 104, 107, 113, 116, 123, 129, 145, 153, 168, 169, 171, 183, 189.
- **PF-A1-007:** 19, 26, 41, 44, 47, 55, 58, 62, 68, 72, 73, 74, 87, 91, 109, 113, 115, 126, 131, 155.
- **PF-A1-008:** 11, 38, 39, 57, 62, 63, 66, 69, 70, 71, 72, 74, 75, 81, 91, 103, 104, 109, 110, 113, 116, 117, 124, 126, 133, 135, 136, 138, 141, 148, 151, 152.
- **PF-A1-009:** 51, 53, 56, 57, 62, 92, 94, 101, 107.

Correcciones ortográficas adicionales:

- **PF-A1-004, fila 1:** `¡vamos!;come on!` empieza ambas frases en minúscula. Corregir a `¡Vamos!;Come on!`.
- **PF-A1-004, filas 36, 45, 50, 86, 116, 117, 122, 152 y 153:** además de rehacer las frases por naturalidad, poner mayúscula inicial en la traducción inglesa cuando corresponda (`Come on...`).
- **PF-A1-007, fila 5:** `señora Garcia` debe llevar la tilde del apellido español: `señora García`.

## Regresión y estado para la siguiente iteración

- Algunas correcciones puntuales del informe anterior sí aparecen aplicadas: el ejemplo `tempraño` de PF-A1-009 ya no está; la exclamación autónoma de PF-A1-006 empieza correctamente con `¡Oh, no!`; y las erratas antiguas `amigosí`, concordancia `juntas` y `estudian` no se observaron en los ejemplos revisados.
- No obstante, la observación extensa sobre variedad, autonomía y naturalidad sigue pendiente en las ocho sesiones; PF-A1-007 vuelve a introducir `ir a + infinitivo`, PF-A1-008 conserva los `I mean` sin contexto y PF-A1-002 contiene sustituciones por `?`. Por tanto, loop 8 no resuelve íntegramente la lista de regresión ni cumple los criterios de aprobación.
- **Sesiones que pueden omitirse en la siguiente validación:** PF-A1-001, ya aprobada fuera de este alcance.
- **Sesiones pendientes y que deben volver a validarse:** PF-A1-002, PF-A1-003, PF-A1-004, PF-A1-005, PF-A1-006, PF-A1-007, PF-A1-008 y PF-A1-009. Ninguna de las ocho queda completada en esta auditoría.

## Indicación al orquestador

Informe: `loops_csv\9_loop\0_observaciones_a_las_sesiones.md`. **Se requiere otra iteración** para corregir y volver a validar PF-A1-002 a PF-A1-009. No modificar PF-A1-001 ni los artefactos de iteraciones anteriores.
