# Auditoría lingüística y técnica — A1, iteración 14

**Plan aprobado e inmutable cotejado:** `planes_aprobados/oxford_phrase_list/plan_frases_oxford.md`  
**Lista de regresión revisada íntegramente:** `loops_csv/12_loop/0_observaciones_a_las_sesiones.md`  
**Alcance:** PF-A1-002 a PF-A1-009. PF-A1-001 queda excluida por estar previamente aprobada.

## Cobertura, nombres y comprobaciones técnicas

Se revisaron los ocho CSV de `loops_csv/13_loop/A1/`, comparando sus nombres con la columna `CSV planificado` del plan:

| Sesión | Archivo literal | Filas verificadas |
|---|---|---:|
| PF-A1-002 | `frases_PF-A1-002_v1.csv` | 173 |
| PF-A1-003 | `frases_PF-A1-003_v1.csv` | 249 |
| PF-A1-004 | `frases_PF-A1-004_v1.csv` | 172 |
| PF-A1-005 | `frases_PF-A1-005_v1.csv` | 153 |
| PF-A1-006 | `frases_PF-A1-006_v1.csv` | 194 |
| PF-A1-007 | `frases_PF-A1-007_v1.csv` | 158 |
| PF-A1-008 | `frases_PF-A1-008_v1.csv` | 155 |
| PF-A1-009 | `frases_PF-A1-009_v1.csv` | 156 |

- Hay exactamente un archivo para cada uno de los ocho IDs solicitados; no faltan IDs ni hay CSV adicionales en la carpeta revisada. Los ocho nombres coinciden literalmente con el plan.
- Se aplicó expresamente el mínimo de **150 frases a cada archivo**: los ocho lo cumplen; PF-A1-005 tiene el margen más estrecho, con 153.
- Se verificó cada archivo mediante decodificación UTF-8 estricta y parser CSV: dos campos no vacíos por fila, sin encabezado, separados por `;`; no hay filas vacías, campos adicionales, comillas mal cerradas, saltos de línea incrustados ni `;` dentro de campos. Cada línea física contiene exactamente un delimitador `;`.
- No se detectaron `Ã…`, `�` ni sustituciones por `?`; los signos diacríticos presentes se leen correctamente. Todas las preguntas en español incluyen `¿` y conservan el cierre `?`.

## Observaciones pendientes — se requiere corrección

### Prioridad alta — alcance A1 y coherencia semántica

1. **`frases_PF-A1-002_v1.csv`**
   - **Filas 129, 150 y 161:** `Mi tía gana dinero vendiendo flores`, `Ella gana dinero trabajando en una tienda` y `Mi hermano gana dinero reparando bicicletas`. Las construcciones con gerundio como complemento de actividad (`vendiendo/trabajando/reparando`) exceden la gramática A1 declarada. Reformular en dos acciones coordinadas y simples, por ejemplo: “Mi tía vende flores y gana dinero”, conservando `make money`.

2. **`frases_PF-A1-003_v1.csv`**
   - **Filas 152 y 179:** `Esta mañana/Por la tarde, mis padres se casaron en verano.;This morning/In the afternoon, my parents got married in summer.` Los marcos temporales se contradicen y hacen inverosímil cada frase. Dejar un único marco temporal coherente en ambos idiomas.
   - **Filas 66 y 78:** `Gracias por traerme una taza de té.;Thank you for bringing me a cup of tea.` y `Gracias por ayudarme con la tarea.;Thank you for helping me with my homework.` El uso de `por + infinitivo` y `for + gerundio` introduce una estructura por encima del alcance A1 indicado. Sustituirla por expresiones simples de agradecimiento adecuadas al objetivo de cortesía.

3. **`frases_PF-A1-006_v1.csv`**
   - **Fila 55:** `Los niños crecen rodeados de cariño y cuidado.;Children grow up surrounded by love and care.` `Rodeados de/surrounded by` añade vocabulario y una construcción participial no apropiados para A1. Usar una formulación directa con vocabulario elemental, por ejemplo, “Los niños crecen con amor y cariño”.
   - **Fila 156:** `Durante el viaje, ella anota la dirección antes de salir.;During the trip, she writes the address down before leaving.` “Durante el viaje” y “antes de salir” sitúan la acción a la vez dentro del viaje y antes de partir. Cambiar uno de los marcos para que la secuencia temporal sea posible y conserve el foco `write sth down`.

4. **`frases_PF-A1-008_v1.csv`**
   - **Fila 62:** `Durante el viaje, trabajo duro en la escuela.;During the trip, I work hard at school.` El viaje y trabajar en la escuela quedan en conflicto sin contexto explicativo. Sustituir el marco por una situación compatible o construir un contexto que justifique ambas partes.
   - **Fila 46:** `Las malas noticias entristecen a mi madre.;The bad news makes my mother sad.` `Entristecen` es un verbo poco frecuente y por encima del nivel A1. Reformular con vocabulario elemental y estructura A1, por ejemplo: “Mi madre está triste por las malas noticias”.

### Prioridad media — naturalidad, variedad, autonomía y repaso

5. **`frases_PF-A1-002_v1.csv`, filas 153, 155 y 156:** se repite exactamente `mi hermana ahorra dinero para una bicicleta` y solo se intercambian `A veces/Cada semana/Con frecuencia`. Sustituir al menos dos variantes por situaciones diferentes y naturales que practiquen `save money`; no repetir la misma frase añadiendo únicamente un adverbio de frecuencia.

6. **`frases_PF-A1-004_v1.csv`**
   - **Filas 30 y 35:** `Cada semana/Con frecuencia, la clase es el lunes.;Every week/Often, the class is on Monday.` Son variaciones mecánicas de una misma afirmación; además, “a menudo la clase es el lunes” resulta poco idiomático. Expresar una rutina real con una sola frecuencia clara o reemplazar las variantes por ejemplos distintos.
   - **Filas 157 y 160:** `Por la tarde/Antes de cenar, me gustan las frutas, por ejemplo, las manzanas.` Los marcos temporales no tienen relación con la preferencia expresada y parecen añadidos para variar la plantilla. Retirarlos o reemplazar cada frase por un contexto pertinente.

7. **`frases_PF-A1-005_v1.csv`, filas 10–12:** `A veces/En verano/Con frecuencia, estamos de vacaciones.` Se repite la misma oración con tres marcos; en particular, `Con frecuencia` (“often”) aplicado a estar de vacaciones resulta poco natural. Mantener, como máximo, la versión contextualizada y variar el resto con ejemplos autónomos y verosímiles para los focos de la sesión.

8. **`frases_PF-A1-007_v1.csv`**
   - **Filas 72 y 73:** `Por la tarde/Antes de cenar, voy a casa de inmediato.;In the afternoon/Before dinner, I go home at once.` `De inmediato/at once` queda sin acción o hecho desencadenante; ambos marcos son añadidos sin contexto. Precisar qué ocurre antes de irse (p. ej., termina la clase) y evitar la duplicación.
   - **Filas 44, 55, 62 y 68:** se repite `paso tiempo con mi familia` cambiando solo `A veces/En verano/Esta semana/Con frecuencia`. Crear contextos diferentes que usen `spend time` con naturalidad, en lugar de limitarse a rotar el marco temporal.
   - **Filas 122, 133, 141 y 146:** se repite `mis amigos pasan tiempo en el parque` con `En invierno/Por la noche/Después del trabajo/En días de lluvia`. La variedad es superficial y varios marcos no explican por qué se destaca ese momento. Reemplazar algunas filas por actividades o situaciones distintas y coherentes.

9. **`frases_PF-A1-008_v1.csv`**
   - **Fila 64:** `Durante el viaje, mi teléfono móvil es nuevo.;During the trip, my mobile phone is new.` El viaje no aporta contexto lógico a que el teléfono sea nuevo; parece un marco temporal insertado mecánicamente. Reformular con una situación pertinente o eliminar el marco.
   - **Filas 76 y 78:** `Cada semana/Con frecuencia, las malas noticias llegan por teléfono.` La noticia negativa repetida semanalmente/con frecuencia resulta poco verosímil y las dos filas duplican la misma idea. Reemplazarlas por situaciones plausibles y variadas para `bad news`.
   - **Fila 137:** `Antes de cenar, la oficina de correos abre a las nueve.;Before dinner, the post office opens at nine.` La relación entre “antes de cenar” y la hora de apertura no es clara; retirar el marco irrelevante o precisar un contexto natural.

10. **`frases_PF-A1-009_v1.csv`**
    - **Filas 96, 116 y 132:** `Hoy/En invierno/Por la noche, la sala de estar tiene una ventana grande.` Los marcos temporales no modifican una característica estática de la sala y no hacen las filas más naturales ni informativas. Eliminar estos añadidos y variar las frases con detalles o situaciones pertinentes.
    - **Filas 133, 147 y 149:** `Esta semana/Antes de cenar/Después de clase, mi hermana trabaja en casa el fin de semana.` Se superponen marcos temporales sin una relación comunicativa clara. Reescribir con un único marco coherente y diferenciar los ejemplos.

## Regresión y sesiones para la siguiente iteración

Se cotejaron las observaciones de la iteración 12. Se corrigieron, entre otros, los nombres literales y los problemas técnicos; también se mejoraron las filas de petición de respuesta `Creo que sí` en PF-A1-008, los marcos temporales citados para PF-A1-004/005/006 y la puntuación de la exclamación de PF-A1-009. No se repiten varios hallazgos lingüísticos previos; sin embargo, persisten los problemas enumerados arriba y se detectan ejemplos nuevos que todavía requieren corrección. La cobertura, la codificación y el mínimo de frases pasan, pero eso no compensa las observaciones de nivel, sentido y naturalidad.

- **Sesiones completadas que pueden omitirse en la siguiente iteración:** ninguna entre PF-A1-002 y PF-A1-009.
- **Sesiones que requieren otra iteración y validación:** PF-A1-002, PF-A1-003, PF-A1-004, PF-A1-005, PF-A1-006, PF-A1-007, PF-A1-008 y PF-A1-009.
- PF-A1-001 permanece previamente aprobada y fuera del alcance; puede seguir omitiéndose.

## Indicación al orquestador

Informe: `loops_csv/14_loop/0_observaciones_a_las_sesiones.md`. **Se requiere otra iteración** para corregir las observaciones y volver a validar las ocho sesiones indicadas. No modificar el plan aprobado, PF-A1-001 ni artefactos anteriores.
