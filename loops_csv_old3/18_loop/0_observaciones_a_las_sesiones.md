# Informe de auditoría lingüística y técnica — A1, iteración 17

**Plan aprobado e inmutable cotejado:** `c:\GIT\english-learning-program\planes_aprobados\oxford_phrase_list\plan_frases_oxford.md`  
**Indicaciones aplicadas:** `indicaciones_csv.md`  
**Lista de regresión leída íntegramente:** `loops_csv\16_loop\0_observaciones_a_las_sesiones.md`  
**Alcance:** PF-A1-002 a PF-A1-009. PF-A1-001 se omite por aprobación previa.  
**Resultado:** quedan observaciones; se requiere otra iteración.

## Cobertura, nombres y comprobaciones técnicas

El plan aprobado especifica nombres literales con el patrón `frases_PF-A1-NNN_v1.csv`. En `loops_csv\17_loop\A1\` no existe ninguno de esos nombres. Se encontraron ocho CSV con nombres distintos: `PF-A1-002.csv` a `PF-A1-009.csv`. Por tanto, aunque hay un archivo de contenido asociado a cada ID, la cobertura por nombre literal **no cumple**: faltan los ocho archivos requeridos y los ocho existentes no tienen el nombre del plan. Renombrar/entregar los archivos con los nombres literales esperados; no basta con que el ID aparezca en el nombre.

Se revisaron los ocho archivos existentes, incluyendo lectura UTF-8 estricta, conteo de filas y análisis de estructura. El mínimo explícito de **150 frases se aplicó individualmente a los ocho archivos**:

| ID | Nombre literal exigido por el plan (ausente) | Archivo encontrado (nombre no válido) | Filas |
|---|---|---|---:|
| PF-A1-002 | `frases_PF-A1-002_v1.csv` | `PF-A1-002.csv` | 173 |
| PF-A1-003 | `frases_PF-A1-003_v1.csv` | `PF-A1-003.csv` | 249 |
| PF-A1-004 | `frases_PF-A1-004_v1.csv` | `PF-A1-004.csv` | 172 |
| PF-A1-005 | `frases_PF-A1-005_v1.csv` | `PF-A1-005.csv` | 153 |
| PF-A1-006 | `frases_PF-A1-006_v1.csv` | `PF-A1-006.csv` | 194 |
| PF-A1-007 | `frases_PF-A1-007_v1.csv` | `PF-A1-007.csv` | 158 |
| PF-A1-008 | `frases_PF-A1-008_v1.csv` | `PF-A1-008.csv` | 155 |
| PF-A1-009 | `frases_PF-A1-009_v1.csv` | `PF-A1-009.csv` | 156 |

Los ocho archivos encontrados superan el mínimo de 150 filas. Todos son UTF-8 válido; las filas físicas se parsean como dos campos sin encabezado, separados por `;`; no se hallaron campos vacíos, filas vacías, delimitadores alternativos, puntos y coma dentro de campos, comillas mal formadas, saltos de línea incrustados, caracteres de reemplazo `�` ni mojibake (`Ã…`). Los acentos y signos españoles aparecen correctamente y las preguntas españolas revisadas incluyen `¿`. No se detectaron duplicados exactos de pares bilingües. La comprobación de vocabulario frente a la tabla A1 del plan encuentra los focos de las sesiones 002–008; en 009 no se encontró el uso de `yourself` en el foco `take care of sb/sth/yourself` (véase observación).

## Observaciones pendientes

### Prioridad alta — nombre/entrega, equivalencia y alcance A1

1. **Cobertura literal de las ocho sesiones:** `loops_csv\17_loop\A1\PF-A1-002.csv` a `PF-A1-009.csv` (todos los archivos encontrados). Faltan, respectivamente, `frases_PF-A1-002_v1.csv`, `frases_PF-A1-003_v1.csv`, `frases_PF-A1-004_v1.csv`, `frases_PF-A1-005_v1.csv`, `frases_PF-A1-006_v1.csv`, `frases_PF-A1-007_v1.csv`, `frases_PF-A1-008_v1.csv` y `frases_PF-A1-009_v1.csv`. **Cambio requerido:** entregar cada CSV bajo el nombre exacto de su sesión indicado en el plan.

2. **`PF-A1-006.csv`, fila 35:** `No hay de qué. Me alegra ayudar.;Not at all. I'm happy to help.` `No hay de qué` significa `You're welcome`, no `Not at all`. **Cambio requerido:** corregir la primera equivalencia, por ejemplo `You're welcome. I'm happy to help.` El foco `not at all` debe aparecer en un uso que conserve ese significado, como negar una molestia o problema.

3. **`PF-A1-006.csv`, fila 44:** `¿Cómo estás después de caminar hasta casa?;How are you after walking home?` `after + gerund` introduce una estructura superior a las expresiones formulaicas y estructuras simples previstas para A1. **Cambio requerido:** mantener `How are you?` en una pregunta breve y eliminar el complemento con gerundio o sustituirlo por un marco nominal A1.

4. **`PF-A1-005.csv`, fila 148:** `... después de leer un libro.;... after reading a book.` Persiste el gerundio inglés tras preposición que ya se había señalado en la regresión anterior en esa sesión, aunque cambiara el ejemplo. **Cambio requerido:** sustituirlo por una referencia nominal sencilla (por ejemplo, `after the story`) o por dos frases simples, manteniendo el nivel A1.

5. **`PF-A1-007.csv`, fila 113:** `... antes de ir a clase.;... before going to class.` El complemento `before + gerundio` rebasa el alcance A1 aplicado en la revisión anterior. **Cambio requerido:** expresar el marco con un sustantivo o separar en frases simples, sin gerundio.

6. **`PF-A1-007.csv`, fila 141:** `Mis amigos pasan tiempo en el parque mientras sus perros juegan.;My friends spend time in the park while their dogs play.` La subordinada con `while` añade una estructura no contemplada por los focos de presente/pasado simple de esta sesión. **Cambio requerido:** convertirlo en una oración simple/coordinación A1 o usar la cláusula solo si se justifica y mantiene el nivel.

7. **`PF-A1-006.csv`, fila 147:** `La dirección es difícil de recordar, así que ella la anota.;The address is hard to remember, so she writes it down.` La frase apila `hard to remember`, la relación causal y el pronombre objeto además del foco `write sth down`; no respeta la indicación de una estructura pertinente por frase. **Cambio requerido:** simplificar y centrar la fila en `write sth down`, por ejemplo con un objeto/lugar sencillo.

8. **`PF-A1-009.csv`, filas 24, 30, 57 y 107:** `Le deseo buena suerte...;I wish ... good luck.` El patrón `wish + persona + good luck` introduce una construcción menos básica que el uso formulaico A1 `good luck` y no es necesario para el objetivo de la sesión. **Cambio requerido:** practicar `Good luck!` en situaciones cortas y autónomas con vocabulario A1.

9. **`PF-A1-009.csv`, fila 5:** `Buena suerte en tu examen.;Good luck in your exam.` La preposición inglesa no es idiomática en esta colocación. **Cambio requerido:** usar `Good luck with your exam` o `Good luck on your exam`.

10. **`PF-A1-009.csv`:** el plan incluye explícitamente el foco `take care of sb/sth/yourself`, pero las filas encontradas practican animales, plantas y a otra persona; no aparece la variante reflexiva `yourself`. **Cambio requerido:** incluir al menos un ejemplo autónomo con `take care of yourself` y una traducción española equivalente.

### Prioridad media — naturalidad, autonomía, progresión y variedad

11. **`PF-A1-002.csv`, filas 37, 69, 100, 105 y 110:** se reitera que el café está frío, con marcos como `A veces`, `En verano` y `Esta semana`; estos marcos temporales no explican el estado estático. **Fila 108:** `En verano, ¿quieres un poco más de leche?;In summer, would you like a bit more milk?` también añade una circunstancia que no motiva una oferta puntual. **Cambio requerido:** retirar los marcos irrelevantes y construir situaciones verosímiles distintas para practicar cantidad/grado, por ejemplo temperatura y una petición contextualizada.

12. **`PF-A1-003.csv`, filas 229, 240, 242 y 245:** se repite `mis amigos y yo nos vemos el uno al otro cada semana / see each other every week`, alterando solo `a veces`, `en verano` o `con frecuencia`. Además, `a veces`/`con frecuencia` junto a `cada semana` resulta redundante o contradictorio. **Cambio requerido:** conservar el foco `each other` en ejemplos con acciones o situaciones diferentes, sin rotar únicamente el adverbio temporal.

13. **`PF-A1-003.csv`, filas 106, 184, 190 y 216** (y el mismo patrón de vaso de agua en filas 19, 98, 130 y 141): se repite la misma petición `would like a table near the window` o `would like a glass of water`, añadiendo estación, semana, tarde o viaje sin motivo comunicativo. **Cambio requerido:** sustituir las variaciones superficiales por peticiones de objetos/situaciones diferentes y autónomas, con progresión breve a más completa.

14. **`PF-A1-004.csv`, filas 49 y 91:** `Caminamos todo el camino hasta la escuela` / `El autobús va todo el camino hasta el centro` calcan `all the way` de forma redundante en español. **Cambio requerido:** usar una expresión española natural (`hasta la escuela/el centro`, o `durante todo el trayecto` si se necesita enfatizarlo) y hacer que ambos idiomas conserven el mismo sentido. La frase de la fila 49 requiere corrección clara.

15. **`PF-A1-004.csv`, filas 39, 49, 91, 103, 109, 140, 155 y 156:** se concentra `all the way` en trayectos o carreras muy parecidos y algunos ejemplos repiten `ella corrió ... hasta casa` cambiando solo el marco (`En verano`, `Esta semana`, `Después de clase`). **Cambio requerido:** diversificar rutas/acciones o retirar esos marcos cuando no aporten contexto; evitar usar la misma plantilla como relleno para alcanzar cantidad.

16. **`PF-A1-005.csv`, fila 20:** `Vuelvo a la tienda después de la compra.;I go back to the shop after the purchase.` La nominalización `after the purchase` suena poco natural y no queda claro qué compra ni por qué se vuelve a la tienda. **Cambio requerido:** crear un contexto autónomo y natural con un marco sencillo, sin recurrir al gerundio rechazado en la iteración anterior.

17. **`PF-A1-005.csv`, filas 7 y 17:** `Mis amigos se van mañana` reaparece como `Mis amigos se van mañana por la mañana`; además, `go to school by bus` se repite con cambios mínimos en filas 15, 35, 55 y 58. **Cambio requerido:** reducir variantes de una misma frase y añadir contextos/acciones distintos para los focos de desplazamiento.

18. **`PF-A1-006.csv`, filas 26, 32, 67, 84, 87, 90, 94, 99, 110 y 116:** `That's it` se antepone repetidamente a datos diferentes (`la puerta está cerrada`, `el tren sale`, `el libro está en la mesa`, etc.) sin un contexto claro que haga de cada fila una confirmación o cierre natural. **Cambio requerido:** reservar `that's it` para situaciones donde realmente signifique «eso es/eso es todo» y variar los actos comunicativos.

19. **`PF-A1-006.csv`, filas 83, 115, 120, 144, 152 y 168:** se repite `me pongo de pie cuando entra la profesora / stand up when the teacher comes in`, añadiendo días o franjas horarias. **Filas 72, 127, 141, 151 y 179:** se repite `mi amiga me avisa cuando llega el tren / my friend lets me know when the train arrives` con el mismo tipo de marcos. **Cambio requerido:** mantener los focos `stand up` y `let me know`, pero crear escenas autónomas variadas en lugar de cambios superficiales de tiempo.

20. **`PF-A1-006.csv`, filas 69 y 137:** vuelve el patrón ya señalado en la iteración anterior del agente de policía situado en la calle, ahora con un marco temporal añadido en una de las filas. **Cambio requerido:** variar la acción/ubicación con un propósito comunicativo claro y retirar el marco temporal ornamental.

21. **`PF-A1-007.csv`, filas 50, 62, 122, 133 y 146:** reaparece la concentración de amigos/familia que «pasan tiempo en el parque», con cambios menores de sujeto o una actividad añadida. La iteración anterior había dado por corregida esta familia de repeticiones. **Cambio requerido:** diversificar quién pasa tiempo, dónde y qué actividad concreta ocurre; no reciclar el parque como contexto por defecto.

22. **`PF-A1-008.csv`, filas 45, 67, 106, 128 y 134:** `Of course, my sister knows the way` se repite con `hoy`, `en invierno`, `por la noche` o `durante el viaje`, sin que esos marcos cambien el sentido ni expliquen la afirmación. **Cambio requerido:** variar la situación/acción de `of course` o eliminar los añadidos temporales irrelevantes.

23. **`PF-A1-008.csv`, filas 19, 71, 74, 104 y 109:** se repite `tengo malas noticias sobre el autobús` con verano, esta semana, antes de cenar y después de clase. Una noticia estática no queda motivada por esos marcos, igual que los marcos irrelevantes señalados en el informe de regresión. **Cambio requerido:** usar noticias distintas y situaciones que expliquen por qué se comunican.

24. **`PF-A1-008.csv`, filas 92, 141, 148, 151 y 152:** vuelve la plantilla `voy a la oficina de correos después del trabajo`, ahora con adverbios de frecuencia o condiciones de lluvia. Aunque se eliminó la duplicación exacta previamente señalada, sigue habiendo variación superficial. **Cambio requerido:** dejar solo una progresión útil de esa acción y construir otros ejemplos para `post office`.

25. **`PF-A1-008.csv`, fila 86:** `Durante el viaje, mi padre está en el trabajo.;During the trip, my father is at work.` La combinación de viaje y estar en el trabajo carece de contexto que la haga coherente. **Cambio requerido:** aclarar la situación o reemplazarla por una frase autónoma y lógica que practique `at work`.

26. **`PF-A1-009.csv`, filas 58, 103, 108, 126 y 127:** se repite `mi hermana cuida de su abuela en casa` variando solo lunes, mañana, tarde o antes de cenar. **Filas 61, 91, 113, 114 y 137:** se repite la fiesta de la prima con `hoy`, invierno, esta mañana o durante el viaje. **Cambio requerido:** diversificar actividades/escenas domésticas y de ocio, retirar marcos temporales que no aportan lógica y mantener las filas utilizables por separado.

27. **`PF-A1-009.csv`, filas 5, 41, 48, 94 y 101:** la expresión `good luck` se practica repetidamente con distintos eventos/trabajos, pero algunos usos difieren solo por el complemento (`exam`, `interview`, `competition`, `job`, `game`). **Cambio requerido:** mantener solo una secuencia breve y natural que enseñe el uso autónomo de `good luck`; corregir en especial la fila 5 (`Good luck with/on your exam`) y evitar multiplicar ejemplos casi equivalentes.

## Regresión y sesiones para la siguiente iteración

Se revisaron como regresión los hallazgos lingüísticos, de complejidad y de variedad del informe de la iteración 16. Hay correcciones verificables: la repetición exacta de `get married` ya no aparece en PF-A1-003; los marcos de ubicación/free-map de PF-A1-004 están más variados; PF-A1-005 sustituyó varias construcciones anteriores con gerundio, aunque aún conserva la fila 148; en PF-A1-006 se cambió `before leaving` por `before the trip`, aunque aparece otro `after + gerund` y persisten plantillas repetidas; en PF-A1-007 se corrigieron el momento del día de la fila 131, el sujeto explícito de la fila 40 y la construcción compleja de `next time`, pero reaparecen patrones de repetición y una construcción con gerundio; PF-A1-008 ya no tiene la duplicación literal previa, pero mantiene la variación mecánica de `of course`, noticias y oficina de correos. En PF-A1-009 se diversificaron varios ejemplos de cama/hogar/programa, pero persisten los grupos repetitivos descritos.

- **Sesiones completadas que pueden omitirse en la siguiente iteración:** ninguna entre PF-A1-002 y PF-A1-009.
- **Sesiones que requieren corrección y nueva validación:** PF-A1-002, PF-A1-003, PF-A1-004, PF-A1-005, PF-A1-006, PF-A1-007, PF-A1-008 y PF-A1-009.
- **PF-A1-001:** previamente aprobada, fuera de este alcance y puede seguir omitiéndose.

## Indicación al orquestador

Informe: `loops_csv\18_loop\0_observaciones_a_las_sesiones.md`. **Se requiere otra iteración**: corregir los nombres literales de los ocho CSV y resolver las observaciones lingüísticas, de equivalencia, alcance A1, naturalidad y variedad señaladas. Volver a validar las ocho sesiones. No modificar el plan aprobado, PF-A1-001 ni artefactos anteriores.
