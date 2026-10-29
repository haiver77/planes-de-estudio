# Informe de auditoría — A1, iteración global 5

**Resultado:** requiere correcciones y otra iteración. Alcance limitado a `A1-S001.csv`–`A1-S005.csv` en `loops_csv/5_loop/A1/`, el plan aprobado de `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo de trazabilidad y el informe previo indicado. No se revisó ningún otro CSV ni `loops_csv_old`.

## Evidencia técnica y conteo

- El plan contiene los cinco IDs objetivo. Los cinco CSV existen, sin archivos requeridos ausentes ni IDs ajenos en este alcance.
- Cada archivo tiene **150 líneas físicas y 150 pares**: 750 en total; cumple el mínimo de 150 por archivo. La decodificación de bytes UTF-8 estricta pasa en los cinco (sin BOM). El lector CSV estricto, aplicado línea por línea, encuentra dos campos en cada fila, sin encabezado, campos vacíos, filas en blanco, comillas mal cerradas ni saltos de línea incrustados. El separador es `;`; las comas son puntuación, no delimitadores. No hay filas duplicadas exactamente.
- Las filas 1–60 de cada archivo se distribuyen en doce bloques consecutivos de cinco, correspondientes a U01–U12 del catálogo: **300 pares nuevos** en total. Las cantidades planificadas de gramática e integración completan las 150 filas por sesión. La revisión de los bloques confirma problemas semánticos o de naturalidad señalados abajo, así como incumplimientos de repaso.
- No se detectan bytes UTF-8 inválidos, secuencias de mojibake ni `?` sustituyendo letras, salvo el caso indicado en S005-25. Los signos de apertura `¿` y cierre `?` se mantienen en las preguntas españolas revisadas; los demás `?` son cierres de pregunta válidos.

## Pendientes priorizados

### Prioridad alta — repaso programado no cubierto

El plan reserva 12 pares de repaso por evento vencido. En los bloques asignados, solo se reconocen directamente **33 de los 72 pares de repaso programados**; el resto debe sustituirse o completarse con las unidades previstas. La cifra cuenta el lema/expresión fuente y su sentido, no una mera coincidencia de palabras relacionadas.

1. **`A1-S003.csv`, filas 61–72 — repaso +1 de A1-S002-U01–U12: 5/12 identificables.** Las filas 67–70 y 72 sí cubren `all over the world`, `anything else`, `anyone else`, `a period of time` y `arrive at`. La 61 solo dice `azúcar / sugar` y omite `a little`; las 62–66 no recuperan, respectivamente, `a lot`, `a lot to do`, `a lot of sth`, `all day` y `all night`; la 71 dice `around the park / city`, no `around the world`. **Cambio requerido:** reescribir esas siete filas para practicar los lemas y sentidos omitidos, manteniendo un par por unidad.

2. **`A1-S004.csv`, filas 61–72 — repaso +1 de A1-S003-U01–U12: 0/12.** El bloque usa principalmente `away from`, `bad for` y `bad news` de la sesión actual, y no las unidades programadas de S003 (`arrive in`, `ask for`, `at home/school`, `at the beginning/end`, `at the moment`, `at the same time`, `at the weekend`, `at university/work`). **Cambio requerido:** sustituir el bloque completo por doce pares que recuperen cada U01–U12 de S003.

3. **`A1-S004.csv`, filas 73–84 — repaso +3 de A1-S001-U01–U12: 1/12.** La fila 81 recupera `agree with sb`. La 82 no expresa `a little food`; la 83 dice que necesita ayuda, pero omite `a little help`; la 84 menciona dinero, pero omite `a little money`. Las filas 73–80 no recuperan las unidades previstas de S001 (incluyen vocabulario de otras sesiones o expresiones no equivalentes). **Cambio requerido:** reemplazar el bloque por un par claro para cada U01–U12 de S001, desde `a few` hasta `a little money`.

4. **`A1-S005.csv`, filas 61–72 — repaso +1 de A1-S004-U01–U12: 8/12 identificables.** Faltan `bad thing` (U04), `because of` (U06) y `be going to do sth` (U08); la fila 61 usa `far from` para el sentido de `away from`, pero no recupera la expresión fuente. **Cambio requerido:** asegurar un par inequívoco para U01–U12, especialmente U04, U06 y U08.

5. **`A1-S005.csv`, filas 73–84 — repaso +3 de A1-S002-U01–U12: 7/12 identificables.** La fila 73 omite `a little` en `a little sugar`; la 74 sustituye `a lot` por `many`; faltan `all night` y `a period of time`; la 83 usa `around the town`, no `around the world`. **Cambio requerido:** restituir los cinco objetivos U01, U02, U06, U10 y U11 con sus sentidos fuente (y mantener los otros siete pares válidos).

### Prioridad alta — integridad y equivalencia

6. **`A1-S005.csv`, fila 25:** `Al mediodía, ?l entró...` contiene `?` ASCII sustituyendo la `É` inicial de `Él`. UTF-8 válido no subsana la sustitución. **Cambio requerido:** guardar `Él` correctamente en UTF-8 y volver a validar los bytes.

7. **`A1-S004.csv`, fila 15:** `¿Son malas noticias para el equipo?;Is it bad news for the team?` no conserva número/estructura: `bad news` funciona aquí como sustantivo incontable singular en inglés. **Cambio requerido:** alinear ambos lados, por ejemplo `¿Es una mala noticia para el equipo?;Is that bad news for the team?`.

8. **`A1-S003.csv`, fila 5:** `un puerto pequeño / a small port` no es uso natural de `arrive in`; para un puerto corresponde `arrive at`. **Cambio requerido:** cambiar ambos lados a una ciudad/país para practicar `arrive in`, o cambiar la preposición inglesa a `at` si se mantiene el puerto.

9. **`A1-S003.csv`, fila 7:** `She asks for the bill from the waiter` es una construcción inglesa poco natural y literal. **Cambio requerido:** `She asks the waiter for the bill` (manteniendo `Ella pide la cuenta al camarero`).

10. **`A1-S003.csv`, fila 54:** `Yo conozco a mis compañeros...;I meet my classmates...` permite una lectura de “conocer/saber quiénes son” en español, no necesariamente la acción habitual de encontrarse que expresa `meet`. **Cambio requerido:** precisar el sentido en ambos lados (p. ej., `Me reúno con mis compañeros en la universidad.;I meet up with my classmates at university.`).

11. **`A1-S003.csv`, fila 95:** `En casa no tengo bolso azul` omite el determinante de un contable singular y no corresponde limpiamente a `I have not got a blue bag`. **Cambio requerido:** añadir `un/una` y usar el mismo sustantivo para el bolso, por ejemplo `En casa no tengo una bolsa azul.;At home, I have not got a blue bag.`

### Prioridad media — naturalidad, contexto y repetición

12. **`A1-S001.csv`, fila 15:** `unas pocas veces` queda forzado al final de `...organizan barbacoas con sus vecinos`; la ubicación temporal suena calcada. **Cambio requerido:** usar una colocación natural, por ejemplo `En verano, ellos organizan barbacoas con sus vecinos unas cuantas veces.`

13. **`A1-S002.csv`, fila 10:** `Ese precio es mucho para mí.;That price is a lot for me.` resulta poco natural en ambos idiomas. **Cambio requerido:** reformular con sentido y colocación idiomáticos manteniendo el foco `a lot`, por ejemplo `Me parece mucho dinero.;That seems like a lot of money to me.`

14. **`A1-S004.csv`, fila 16:** `Perder el autobús es una mala cosa` se entiende, pero suena calcado en español. **Cambio requerido:** naturalizar, por ejemplo `Perder el autobús es algo malo.;Missing the bus is a bad thing.`

15. **`A1-S003.csv`, filas 56 y 60:** ambas tienen la misma plantilla y traducción, cambiando solo `mi madre` por `mi hermana` (`...está en el trabajo hasta las cinco`). **Cambio requerido:** reemplazar una por una transferencia contextual distinta para `at work`, no un cambio mecánico de parentesco.

16. **`A1-S004.csv`, filas 49 y 124:** la pregunta española `¿Prefieres las fotos en blanco y negro?` se repite literalmente; la inglesa solo alterna `photos in black and white` / `black-and-white photos`. **Cambio requerido:** cambiar la fila 124 por un contexto/propósito nuevo que practique la unidad sin duplicar la misma pregunta.

17. **`A1-S005.csv`, fila 42:** `Mi hermana y yo nos llamamos entre nosotros` es redundante/poco natural. **Cambio requerido:** usar `Mi hermana y yo nos llamamos cada semana` (o equivalente natural), conservando `each other` en inglés.

18. **`A1-S005.csv`, fila 59:** `Mi clase de inglés es cada semana.;My English class is every week.` suena poco idiomático, sobre todo en español. **Cambio requerido:** `Tengo clase de inglés todas las semanas.;I have English class every week.`

19. **`A1-S005.csv`, fila 79:** anteponer `El miércoles por la tarde` a la afirmación general de que la gente celebra Año Nuevo en todo el mundo introduce una fecha arbitraria sin función y vuelve confusa la escena. **Cambio requerido:** quitar el marco gratuito o convertirlo en una situación concreta coherente con la celebración.

## Contraste con el informe previo de `loops_csv/4_loop/0_observaciones_a_las_sesiones.md`

La mayoría de los ejemplos concretos anteriores ya fueron cambiados o corregidos: no persiste `caf?` en las cinco filas citadas entonces; el pronombre de S001-66 y los sujetos plurales citados están ahora explícitos; S003-125 ya traduce `terraza` como `terrace`; y los ejemplos anteriores de marcos incompatibles, tiempo ambiguo de S005-66 y duplicados señalados en S001/S003 ya no aparecen en esas mismas filas. Los nuevos incumplimientos de repaso de S003–S005 y los defectos citados arriba son observaciones de esta versión.

No se repiten como errores las observaciones previas que contradecían la fuente: S004-36–40 practica el lema de catálogo `be going to do sth` (A1-S004-U08), y S005-21–25 practica `He came into the room.` (A1-S005-U05). También se conservan conforme al catálogo `a few`/`a little` en S001 y `a lot` en S002. Se señalaron solo los problemas de uso, revisión programada, equivalencia o naturalidad independientes de esos lemas fuente.

**Acción requerida:** corregir todas las filas e IDs de repaso indicados, conservar las 150 filas y la asignación de cinco pares por unidad nueva, guardar en UTF-8 y entregar otra iteración para auditoría.
