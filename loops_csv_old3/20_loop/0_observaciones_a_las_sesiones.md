# Informe de auditoría lingüística y técnica — A1, iteración 19

**Plan aprobado e inmutable cotejado:** `c:\GIT\english-learning-program\planes_aprobados\oxford_phrase_list\plan_frases_oxford.md`  
**Indicaciones aplicadas:** `indicaciones_csv.md`  
**Lista de regresión leída íntegramente:** `loops_csv\18_loop\0_observaciones_a_las_sesiones.md`  
**Alcance:** PF-A1-002 a PF-A1-009. PF-A1-001 se omite por aprobación previa.  
**Resultado:** quedan observaciones lingüísticas y de progresión/variedad. Se requiere corregir y volver a revisar; no se inicia otra iteración.

## Cobertura, nombres, cantidad y comprobación técnica

El plan aprobado pide los nombres literales `frases_PF-A1-NNN_v1.csv`. Los ocho CSV están presentes en `loops_csv\19_loop\A1\` con los nombres exactos. No faltan IDs ni hay archivos CSV adicionales en la carpeta; PF-A1-001 queda fuera del alcance.

Se leyó cada archivo con UTF-8 estricto y se verificó individualmente el mínimo de **150 frases**:

| Sesión | Archivo | Filas/frases | Mínimo |
|---|---|---:|---|
| PF-A1-002 | `frases_PF-A1-002_v1.csv` | 173 | Cumple |
| PF-A1-003 | `frases_PF-A1-003_v1.csv` | 249 | Cumple |
| PF-A1-004 | `frases_PF-A1-004_v1.csv` | 172 | Cumple |
| PF-A1-005 | `frases_PF-A1-005_v1.csv` | 153 | Cumple |
| PF-A1-006 | `frases_PF-A1-006_v1.csv` | 194 | Cumple |
| PF-A1-007 | `frases_PF-A1-007_v1.csv` | 158 | Cumple |
| PF-A1-008 | `frases_PF-A1-008_v1.csv` | 155 | Cumple |
| PF-A1-009 | `frases_PF-A1-009_v1.csv` | 156 | Cumple |

Los ocho archivos son UTF-8 válido y se parsean como dos campos por fila, sin encabezado y separados por `;`. La cantidad de líneas físicas coincide con la de filas parseadas; no se hallaron campos extra o vacíos, filas vacías, comillas mal cerradas, saltos de línea incrustados, punto y coma dentro de los campos, archivos separados por comas, mojibake (`Ã…`), `�` ni signos `?` sustituyendo letras. Las interrogativas españolas revisadas llevan `¿`; el `?` de cierre está bien empleado. No hay pares bilingües exactamente duplicados.

La comprobación técnica y la cobertura están aprobadas. Esto no subsana los problemas de equivalencia, nivel, naturalidad y repetición que siguen.

## Observaciones pendientes

### Prioridad alta — equivalencia, naturalidad y nivel A1

1. **`frases_PF-A1-005_v1.csv`, fila 2:** `Voy a casa ahora.;I go home now.` El presente simple inglés no es natural para una acción que ocurre ahora. **Cambio requerido:** usar una forma natural y equivalente, por ejemplo `Me voy a casa ahora.;I'm going home now.`

2. **`frases_PF-A1-005_v1.csv`, filas 14, 50, 72 y 79:** `El gato se va del jardín.;The cat goes away from the garden.` La construcción inglesa `go away from the garden` no es idiomática para expresar que el gato sale del jardín. **Cambio requerido:** reformular ambas columnas para practicar `go away` en un uso natural, por ejemplo `El gato se va.;The cat goes away.`, o escoger otra escena natural que conserve el foco.

3. **`frases_PF-A1-006_v1.csv`, fila 20:** `¿Cómo estás después de una noche tranquila?;How are you after a quiet night?` La pregunta no suena como un uso autónomo y natural de la expresión formulaica `How are you?`; el complemento temporal también desvía el foco. **Cambio requerido:** usar una pregunta breve y autónoma, como `¿Cómo estás esta mañana?;How are you this morning?`

4. **`frases_PF-A1-006_v1.csv`, fila 38:** `Los niños crecen mucho durante sus primeros años.;Children grow a lot during their first years.` La traducción emplea `grow`, no el foco planificado `grow up`, y no conserva con precisión la idea de crecer/hacerse mayor. **Cambio requerido:** expresar inequívocamente `grow up` en inglés y su equivalente en español con una oración A1 sencilla.

5. **`frases_PF-A1-007_v1.csv`, fila 124:** `Mis amigos trabajan en otra ciudad el próximo año.;My friends work in another city next year.` La combinación de presente simple con `next year` no expresa naturalmente el marco futuro aquí. **Cambio requerido:** ajustar la forma verbal a un futuro elemental y al nivel declarado, o reformular el ejemplo para que el tiempo verbal y el marcador temporal concuerden sin introducir estructuras por encima de A1.

6. **`frases_PF-A1-007_v1.csv`, fila 146:** `Julia pasa tiempo practicando el piano.;Julia spends time practising the piano.` `spend time + gerundio` introduce un complemento con gerundio por encima de las estructuras simples previstas para A1. **Cambio requerido:** mantener el foco `spend time` con un complemento nominal o locativo A1, por ejemplo pasar tiempo con una persona o en un lugar.

### Prioridad media — variedad real, progresión y autonomía

7. **`frases_PF-A1-002_v1.csv`, filas 46, 113 y 117; filas 65, 107, 143 y 164:** se repiten casi literalmente `I wait for half an hour at the stop` y `Do not put too much salt in the soup`, cambiando solo el marco temporal. En particular, `Durante el viaje` aplicado a la sopa no aporta una situación verosímil. **Cambio requerido:** reducir estas variantes y crear escenas distintas y autónomas para `half an hour` y `too much`, con contextos que expliquen la frase en vez de añadir tiempo como relleno.

8. **`frases_PF-A1-003_v1.csv`, filas 3, 23, 53 y 64; filas 6, 29, 39 y 46; filas 13, 38, 82 y 117:** vuelven las mismas frases `I look at the map`, `I wait for the bus` y `We talk about the film`, con adverbios o marcos circunstanciales añadidos. **Cambio requerido:** conservar una progresión breve por foco, pero variar acciones/situaciones y eliminar las rotaciones temporales que no cambian el uso ni hacen cada fila más natural. La variación de `each other` sí está mejorada respecto a la regresión anterior.

9. **`frases_PF-A1-004_v1.csv`, filas 38, 96, 101 y 113:** `Vemos la película gratis en el parque` se repite con cambios de frecuencia/estación. **Filas 13, 54, 60 y 74:** se repite `Mi familia come en la playa`. **Filas 12, 53, 59 y 65:** se repite `Voy al centro por mi cuenta`. **Cambio requerido:** mantener como máximo una secuencia corta útil por ejemplo y sustituir las demás variantes por escenas y acciones diferentes para los focos de gratuidad, playa y autonomía.

10. **`frases_PF-A1-005_v1.csv`, filas 13, 49, 70 y 71:** `I get home at five` se repite cambiando solo el marco temporal; **filas 6, 38 y 53:** se repite `I go to work by train` con marcos temporales ornamentales. **Cambio requerido:** conservar solo la repetición que aporte progresión y crear ejemplos distintos para `get home` y `go to work`. También retirar los marcos horarios que no encajan con la acción.

11. **`frases_PF-A1-006_v1.csv`, filas 4, 21, 22, 39 y 41:** se repite `Let me know by phone` con distintos marcos temporales, sin cambiar el acto comunicativo. **Filas 102, 167, 170, 182 y 188:** se repite `I see a police officer near the bank`, con cambios de frecuencia o tiempo que no diversifican la escena. **Cambio requerido:** reservar una progresión útil y redactar situaciones comunicativas diferentes para `let me know` y `police officer`. Las observaciones anteriores sobre `No hay de qué`, `after + gerund` y la plantilla mecánica de `That's it` sí están corregidas.

12. **`frases_PF-A1-007_v1.csv`, filas 8, 58, 74, 87 y 91:** se repite `I have time for a coffee` añadiendo invierno, noche, viaje o después del trabajo sin desarrollar situaciones diferentes. **Cambio requerido:** conservar una secuencia breve y contextualizada de `have time` y diversificar los complementos/acciones restantes. La repetición anterior de pasar tiempo en el parque y las estructuras con `while`/`before + gerund` están corregidas; no obstante, la fila 146 indicada arriba sigue elevando el nivel.

13. **`frases_PF-A1-008_v1.csv`, filas 16, 68, 73, 101 y 107:** se recicla `My friends and I work together` añadiendo únicamente frecuencia o tiempo. **Filas 89 y 145:** `My sister and I work together in the garden` reaparece con el añadido superficial `on Saturdays`. **Cambio requerido:** reducir la repetición del mismo sujeto/acción y aportar tareas colaborativas distintas que practiquen `work together` con contextos autónomos. Las regresiones previas de `of course`, noticias y oficina de correos se observan mejor diversificadas.

14. **`frases_PF-A1-009_v1.csv`, filas 12, 52 y 84–86:** se repite `The baby is in bed` con distintos días/horas, incluso `después de clase`, sin un cambio comunicativo real. **Filas 102, 146 y 151–153:** se repite `My family watches TV in the living room` con marcos temporales añadidos. **Filas 80, 124, 125, 145 y 150:** se repite `We watch a TV show after dinner`, incluyendo `After work ... after dinner`, que acumula dos marcos temporales. **Cambio requerido:** dejar solo una progresión funcional por escena, quitar los marcos redundantes o incoherentes y cubrir `in bed`, `living room` y `TV show` con situaciones diferentes. Los problemas anteriores de `Good luck` (incluida la preposición del examen) y la variante `yourself` sí están corregidos.

## Regresión y sesiones para la siguiente revisión

Se corrigieron los nombres literales, los mínimos de cantidad, la equivalencia de `No hay de qué`, la preposición de `Good luck with your exam`, la inclusión de `take care of yourself` y varias construcciones complejas/repeticiones señaladas en el informe 18. Persisten los hallazgos enumerados; en particular, la variación superficial sigue siendo un patrón recurrente y no se considera resuelta por superar el mínimo de filas.

- **Sesiones completadas que pueden omitirse en la siguiente revisión:** ninguna de PF-A1-002 a PF-A1-009; todas conservan al menos una observación pendiente.
- **Sesiones pendientes de corrección y nueva validación:** PF-A1-002, PF-A1-003, PF-A1-004, PF-A1-005, PF-A1-006, PF-A1-007, PF-A1-008 y PF-A1-009.
- **PF-A1-001:** previamente aprobada, fuera de alcance y puede seguir omitiéndose.

## Indicación al orquestador

Informe: `loops_csv\20_loop\0_observaciones_a_las_sesiones.md`. **Se requiere otra iteración de corrección y posterior auditoría**, pero no se realiza en esta revisión; el loop20 es el máximo permitido. No modificar el plan aprobado, PF-A1-001 ni artefactos previos.
