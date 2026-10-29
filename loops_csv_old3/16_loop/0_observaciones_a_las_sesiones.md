# Informe de auditoría lingüística y técnica — A1, iteración 15

**Plan aprobado e inmutable cotejado:** `c:\GIT\english-learning-program\planes_aprobados\oxford_phrase_list\plan_frases_oxford.md`  
**Lista de regresión revisada íntegramente:** `loops_csv\14_loop\0_observaciones_a_las_sesiones.md`  
**Alcance:** PF-A1-002 a PF-A1-009. PF-A1-001 queda excluida por aprobación previa.  
**Resultado:** quedan observaciones; se requiere otra iteración.

## Comprobaciones de cobertura y formato

Se cotejaron los nombres literales indicados por el plan y se validaron los ocho CSV con lectura UTF-8 estricta y parser CSV. No se modificaron los CSV ni los artefactos anteriores.

| Sesión | Archivo literal validado | Filas |
|---|---|---:|
| PF-A1-002 | `frases_PF-A1-002_v1.csv` | 173 |
| PF-A1-003 | `frases_PF-A1-003_v1.csv` | 249 |
| PF-A1-004 | `frases_PF-A1-004_v1.csv` | 172 |
| PF-A1-005 | `frases_PF-A1-005_v1.csv` | 153 |
| PF-A1-006 | `frases_PF-A1-006_v1.csv` | 194 |
| PF-A1-007 | `frases_PF-A1-007_v1.csv` | 158 |
| PF-A1-008 | `frases_PF-A1-008_v1.csv` | 155 |
| PF-A1-009 | `frases_PF-A1-009_v1.csv` | 156 |

- Hay exactamente un archivo por cada ID solicitado y los ocho nombres coinciden literalmente con el plan; no hay archivos adicionales en `15_loop\A1`.
- Se aplicó el mínimo de **150 frases a cada CSV individualmente**; todos lo cumplen.
- Los ocho archivos son UTF-8 válidos y tienen dos campos no vacíos por fila, sin encabezado y separados por `;`. No se detectaron filas vacías, campos adicionales, comillas mal cerradas, saltos de línea dentro de filas, delimitadores alternativos, `;` dentro de campos, caracteres corruptos (`Ã…`, `�`) ni sustituciones sospechosas por `?`. Las preguntas en español incluyen `¿`.
- Se comprobaron los focos léxicos del plan: aparecen en los CSV, con las variantes flexionadas correspondientes. Esto no subsana los problemas de sentido, gramática, naturalidad y variedad señalados abajo.

## Observaciones pendientes — se requiere corregir y volver a validar

### Prioridad alta — equivalencia, alcance A1 y coherencia

1. **`frases_PF-A1-003_v1.csv`**
   - **Fila 113:** `Gracias por esperar conmigo en la parada.;Thank you for waiting with me at the stop.` y **fila 246:** `Gracias por escucharme cuando estoy preocupado.;Thank you for listening to me when I am worried.` Mantienen la estructura `por + infinitivo / for + gerundio`, ya señalada en la iteración anterior como superior al alcance A1. Sustituir por expresiones breves de agradecimiento con estructuras A1, sin complemento verbal en gerundio.
   - **Fila 224:** `¿Quieres venir conmigo o prefieres hablar con Ana?;Would you like to come with me or would you rather speak to Ana?` `would rather` no corresponde al nivel declarado. Separar en dos preguntas con estructuras A1 y conservar la cortesía/deseo del foco.
   - **Fila 132:** `No hay de qué, fue un placer ayudarte.;You are welcome, it was a pleasure to help you.` La fórmula con pasado y `it was a pleasure` eleva innecesariamente la gramática respecto al foco de cortesía. Reescribir como respuesta simple de A1.

2. **`frases_PF-A1-004_v1.csv`**
   - **Filas 43, 110, 136 y 143:** ejemplos como `Camino todo el camino hasta la escuela.;I walk all the way to school.` calcan `all the way` como `todo el camino`, resultado redundante y poco idiomático en español. Usar una traducción natural que exprese el trayecto completo; además, en la **fila 143**, `Durante el viaje ... hasta la escuela` mezcla un viaje con un destino escolar sin contexto que lo justifique. Reformular esa fila con una situación coherente.

3. **`frases_PF-A1-005_v1.csv`**
   - **Filas 20, 24 y 139:** `después de hacer una compra / after shopping`, `después de visitar a mi abuela / after visiting my grandmother` y `después de leer un libro / after reading a book` usan gerundio inglés tras preposición. Ese patrón rebasa la gramática A1 priorizada en la sesión. Sustituirlo por complementos nominales o frases simples A1, manteniendo el foco temporal y el sentido.

4. **`frases_PF-A1-006_v1.csv`**
   - **Fila 162:** `Cuando entra la profesora, los alumnos se ponen de pie para saludarla.;When the teacher comes in, the students stand up to greet her.` Combina subordinada temporal con infinitivo de propósito y clítico, estructura demasiado compleja para los focos formulaicos A1 de la sesión. Simplificar en una frase de una sola estructura pertinente.
   - **Fila 59:** `Ella anota la dirección antes de salir.;She writes the address down before leaving.` El ejemplo conserva `before + gerundio` en inglés, por encima del alcance A1 aplicado en esta revisión. Reemplazar `before leaving` por una referencia nominal sencilla (por ejemplo, antes del viaje/salida), manteniendo `write sth down`.

5. **`frases_PF-A1-007_v1.csv`**
   - **Fila 131:** `Por la tarde, mi padre lee el periódico después del trabajo.;In the evening, my father reads the newspaper after work.` `Por la tarde` no equivale a `in the evening`; corregir ambos lados para que indiquen el mismo momento del día.
   - **Fila 40:** `Hace mucho tiempo, construyeron esta calle.;A long time ago, they built this street.` La traducción inglesa explicita `they`, pero el español omite el sujeto plural, contrario a la indicación de identificarlo. Añadir un sujeto explícito apropiado o reformular ambos idiomas.
   - **Fila 92:** `La próxima vez, lleva el paraguas grande porque el pequeño no te cubre.;Next time, take the big umbrella because the small one does not cover you.` La cláusula causal, la sustitución `the small one` y `cover you` exceden la sencillez A1. Rehacer con una instrucción y vocabulario básico, sin subordinación compleja.
   - **Fila 156:** `Hace mucho tiempo, mi abuelo vivía cerca del mar.;A long time ago, my grandfather lived near the sea.` El imperfecto `vivía` no es el pasado simple indicado por el plan para estos focos. Usar una estructura temporal A1 apropiada o un ejemplo sin ese aspecto verbal.

6. **`frases_PF-A1-008_v1.csv`**
   - **Fila 26:** `¿Está abierto el café ahora? Creo que sí, porque hay una luz encendida dentro.` / `Is the café open now? I think so, because there is a light on inside.` La justificación con `because` y la construcción `light on inside` exceden la estructura breve de pregunta/respuesta A1. Simplificar el indicio o expresar una respuesta directa.
   - **Fila 135:** `Suele llegar a las cuatro.;He usually gets home at four.` `soler + infinitivo` no corresponde a la gramática A1 declarada. Reformular con presente simple y un adverbio A1, sin perífrasis.

### Prioridad media — naturalidad, autonomía y variedad genuina

7. **`frases_PF-A1-002_v1.csv`**
   - **Filas 115, 125 y 148:** `Cada semana, la sopa está un poco caliente`, `Antes de cenar, tenemos muchos libros en casa` y `Durante el viaje, la tienda está un poquito lejos` añaden marcos temporales que no guardan relación natural con una propiedad estática o con el contenido principal. Retirar esos marcos o crear contextos verosímiles que los hagan pertinentes.
   - **Fila 124:** `Con frecuencia, ¿quieres un poco más de leche?;Often, would you like a bit more milk?` La frecuencia resulta extraña para una oferta puntual y la pregunta no suena natural. Convertirla en una petición/oferta situacional o usar una frase afirmativa que practique el foco.

8. **`frases_PF-A1-003_v1.csv`**
   - **Filas 134 y 152:** ambas repiten exactamente `Mis padres se casaron hace diez años.;My parents got married ten years ago.` Eliminar la duplicación exacta y reemplazar al menos una fila con otro uso autónomo de `get married`.
   - **Filas 115, 121, 161, 167, 170, 238, 239 y 244:** se mantiene `estar enamorado` cambiando solo el marco (`antes de cenar`, `después de clase`, `en verano`, `con frecuencia`, `por la noche`, `después del trabajo`, `en días de lluvia`). El estado no queda motivado por esos marcos y la variación es superficial. Crear situaciones distintas que den contexto real a `in love`.
   - **Filas 192 y 205:** `Después del trabajo / En días de lluvia, mi número de teléfono es nuevo` repite una propiedad estática con marcos temporales irrelevantes. Eliminar dichos añadidos o cambiar la situación para que el tiempo tenga sentido.

9. **`frases_PF-A1-004_v1.csv`**
   - **Filas 98, 127 y 132:** se repite `el café está allí, junto al banco` con `esta semana / antes de cenar / después de clase`; el tiempo no aporta información pertinente a una ubicación fija.
   - **Filas 33, 92, 128 y 134:** se repite que el mapa es gratis en la estación, cambiando solo a `en la estación / los lunes / antes de cenar / después de clase`. Hacer que la gratuidad o el momento de entrega tengan un motivo claro y variar los ejemplos con situaciones distintas.
   - **Filas 112, 162, 165 y 169:** se repite la plantilla `puedes tomar el autobús, por ejemplo, el número cinco` con marcos intercambiables. Sustituir varias por ejemplos diferentes de orientación/direcciones, útiles por separado.
   - **Filas 155, 156 y 163:** el autobús hace el mismo trayecto `todo el camino hasta el centro` y solo cambia el marco temporal. Variar la información del trayecto o retirar marcos que no cambian su sentido.
   - **Filas 145, 148 y 150:** `A veces / En verano / Esta semana hay muchos lugares cerca, por ejemplo, un parque` trata una ubicación como si dependiera de la frecuencia o la estación. Reformular con contextos donde `for example` aporte una ilustración natural.

10. **`frases_PF-A1-006_v1.csv`**
    - **Filas 48, 105, 111, 117, 129 y 135:** se repite que el centro de la ciudad está cerca, con añadidos como `los lunes`, `esta mañana`, `por la tarde` y `antes de cenar`; no cambian una relación espacial fija. Reemplazar varias filas por ejemplos distintos de `town centre` o darles una situación que justifique el marco.
    - **Filas 69, 131, 164 y 166:** se repite que el agente de policía está en la calle y se rotan marcos de tiempo (`en verano`, `antes de cenar`, `después de clase`, `en la calle`). Es variación superficial; hacer que cada fila practique el foco en una situación autónoma y natural.

11. **`frases_PF-A1-007_v1.csv`**
    - **Filas 135, 139, 149 y 150:** se repite `mi amiga tiene tiempo para visitar el museo` cambiando entre `los lunes / esta mañana / por la tarde / antes de cenar`. Variar la acción o el contexto real, en vez de rotar únicamente el marco temporal.
    - La revisión confirma que las repeticiones de `spend time` señaladas en la iteración 14 (familia y amigos en el parque) se diversificaron; no obstante, las filas anteriores muestran que persiste el patrón de variación mecánica en otros focos.

12. **`frases_PF-A1-008_v1.csv`**
    - **Filas 92 y 140:** duplicación exacta: `Voy a la oficina de correos después del trabajo.;I go to the post office after work.` Reemplazar una de ellas con otro ejemplo autónomo.
    - **Filas 44, 100, 105, 111 y 147:** se reitera `of course, I can help you with the book` y solo se alternan adverbios/marcos (`a veces`, `cada semana`, `con frecuencia`, `en días de lluvia`). La repetición no construye una progresión ni contextos genuinos; variar la acción y conservar `of course` en ejemplos naturales.
    - **Filas 12, 41 y 55:** `Hoy / En invierno / Por la noche, mi teléfono móvil es nuevo` impone marcos temporales irrelevantes a una propiedad estática. Retirarlos o cambiar el hecho descrito.

13. **`frases_PF-A1-009_v1.csv`**
    - **Filas 51, 53, 56 y 62:** se repite `leo un libro en la cama` con `a veces / en verano / cada semana / con frecuencia`. Sustituir varias por situaciones o actividades distintas relacionadas con `in bed`, no solo rotar la frecuencia.
    - **Filas 25, 29, 36 y 42:** se repite `mi familia está en casa` con `a veces / en verano / cada semana / con frecuencia`; en particular, `en verano` y `con frecuencia` no explican la afirmación. Variar con actividades domésticas concretas o un contexto pertinente.
    - **Filas 118, 120, 141 y 143:** se repite que el programa empieza a las ocho con marcos como `en verano`, `esta semana`, `antes de cenar` y `después de clase`. Diferenciar los ejemplos con información que aporte algo a la situación, no solo fechas o franjas horarias añadidas.
    - Se confirma que las observaciones anteriores sobre la ventana estática de la sala y los marcos temporales que se superponían al trabajo de la hermana se corrigieron; permanecen los nuevos grupos repetitivos descritos aquí.

## Regresión y sesiones para la siguiente iteración

La lectura del informe anterior se usó como lista de regresión. Se corrigieron varios hallazgos de la iteración 14: entre ellos, las construcciones sobre ganar dinero en PF-A1-002, las contradicciones temporales de PF-A1-003, la repetición de vacaciones en PF-A1-005, el contexto temporal de PF-A1-006, la repetición de `spend time` en PF-A1-007 y varios marcos de PF-A1-008/009. No obstante, persisten observaciones nuevas o patrones equivalentes de gramática, naturalidad y variedad en las ocho sesiones; por ello ninguna queda aprobada en esta revisión.

- **Sesiones completadas que pueden omitirse en la siguiente iteración:** ninguna entre PF-A1-002 y PF-A1-009.
- **Sesiones que requieren otra iteración y validación:** PF-A1-002, PF-A1-003, PF-A1-004, PF-A1-005, PF-A1-006, PF-A1-007, PF-A1-008 y PF-A1-009.
- **PF-A1-001:** previamente aprobada, fuera de este alcance y puede seguir omitiéndose.

## Indicación al orquestador

Informe: `loops_csv\16_loop\0_observaciones_a_las_sesiones.md`. **Se requiere otra iteración** para corregir y volver a validar las ocho sesiones listadas. No modificar el plan aprobado, PF-A1-001 ni artefactos anteriores.
