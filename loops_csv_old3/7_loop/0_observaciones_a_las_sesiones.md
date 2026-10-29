# Auditoría integral A1 — generación 6

**Plan cotejado exclusivamente:** `c:\GIT\english-learning-program\planes_aprobados\oxford_phrase_list\plan_frases_oxford.md`  
**Regresión consultada:** `loops_csv/6_loop/0_observaciones_a_las_sesiones.md`  
**Resultado:** requiere correcciones y otra iteración.

## Comprobaciones generales

- Los nueve IDs A1 del plan (`PF-A1-001` a `PF-A1-009`) tienen exactamente un CSV con el nombre esperado en `loops_csv/6_loop/A1/`; no faltan IDs ni hay CSV adicionales.
- Conteos comprobados por lectura y análisis de los archivos: `001` 150; `002` 169; `003` 245; `004` 169; `005` 150; `006` 192; `007` 155; `008` 152; `009` 153. Todos alcanzan el mínimo de 150 filas.
- Los nueve archivos se decodifican como UTF-8 válido y se analizan como CSV con dos campos no vacíos, sin encabezado, separados por un único `;`. No se detectaron filas vacías, campos extra, comillas mal cerradas ni saltos de línea incrustados en registros. Las columnas están en orden español–inglés. No se hallaron caracteres de reemplazo ni secuencias de mojibake; las preguntas en español revisadas llevan `¿` y `?`.
- Regresión: las tres frases señaladas para PF-A1-001 en el informe anterior (filas 78, 84 y 89) se reformularon sin subjuntivo y aquellas observaciones están resueltas. También se generaron los ocho CSV que faltaban en la iteración anterior. Se observa, no obstante, el error nuevo de la fila 135 indicado abajo.

## Observaciones priorizadas

### Prioridad alta — corrección lingüística y gramática A1

#### PF-A1-001 — `frases_PF-A1-001_v1.csv`

- **Fila 135:** «¿Por qué no participas en el partido con tus amigosí?» — `amigosí` contiene una tilde indebida y no es una forma correcta. Eliminar la `í` final; la frase debe terminar en «tus amigos?».

#### PF-A1-004 — `frases_PF-A1-004_v1.csv`

- **Filas 28, 32 y 36:** «En el pasado, vivíamos…», «…mi abuelo caminaba…», «…la tienda cerraba…» — se usa el imperfecto, que excede la gramática declarada para esta sesión y el alcance A1 solicitado. Reformular con estructuras de pasado simple de nivel A1, manteniendo el foco temporal.
- **Filas 29–31, 33–35 y 37–39:** ejemplos como «Hoy, en el pasado, vivíamos en un pueblo pequeño» y «Esta semana, en el pasado, la tienda cerraba temprano» — la inserción de hoy/fin de semana/esta semana contradice o vuelve incoherente el marco «en el pasado». Eliminar esas variantes o sustituirlas por contextos compatibles y naturales; no conservar el imperfecto fuera de nivel.

#### PF-A1-007 — `frases_PF-A1-007_v1.csv`

- **Filas 2–4, 133 y 151:** «Hace mucho tiempo, mi familia vivía…», «…esta calle era pequeña», «mi abuela vivía junto al mar» — el imperfecto no se ajusta al foco de presente/pasado simple indicado por el plan para A1. Cambiar a una formulación natural con pasado simple A1.
- **Fila 136:** «La enfermera viene de inmedíato.» — tilde incorrecta en `inmediato`; escribir «de inmediato».
- **Fila 145:** «…mis amigos estudían en otra ciudad.» — tilde indebida en `estudian`; escribir «estudian».

#### PF-A1-008 — `frases_PF-A1-008_v1.csv`

- **Filas 62–66:** «Mi hermana y yo trabajamos juntos en la cocina.» — el sujeto explícito es femenino plural, por lo que `juntos` no concuerda. Cambiar a «juntas» en las cinco parejas y conservar `work together` en inglés.
- **Filas 133 y 138:** «El come…» y «El trabaja…» — falta la tilde del pronombre sujeto y, sin ella, `El` se lee como artículo. Escribir «Él come…» y «Él trabaja…».

#### PF-A1-009 — `frases_PF-A1-009_v1.csv`

- **Fila 137:** «mi hermaño» — `hermaño` es una grafía incorrecta; escribir «mi hermano».
- **Filas 142–143:** «programa de television» — falta la tilde en `televisión`; corregir en ambas.
- **Fila 147:** «Mi hermaño estudía…» — corregir ambos errores: «Mi hermano estudia…».
- **Fila 148:** «El nino…» — `nino` no corresponde a “boy”; escribir «niño».
- **Fila 149:** «…escucha musica…» — falta la tilde en «música».

### Prioridad media — fidelidad a la consigna, naturalidad y progresión

El plan pide que cada foco se practique mediante una oración independiente y natural. En las siguientes sesiones se incluyen filas de glosario que solo traducen el foco, no una oración; esas filas también cuentan para el mínimo. Sustituirlas por frases completas que expresen el uso del foco y mantener al menos 150 filas utilizables:

- **PF-A1-002, fila 1 y comienzos de los demás bloques** (por ejemplo, fila 14 «un poco más; a bit more»): cambiar las entradas de vocabulario aisladas por oraciones completas.
- **PF-A1-003, filas 1 y 194** («mejor amigo; best friend», «de nada; you are welcome») y entradas equivalentes de los demás focos: practicar cada expresión en una oración natural.
- **PF-A1-004, filas 1, 14 y demás comienzos de bloque** (por ejemplo, «por ejemplo; for example»): sustituir los rótulos aislados por oraciones de uso.
- **PF-A1-005, fila 1 y comienzos de los bloques siguientes** (por ejemplo, «llegar a casa; get home»): sustituir los infinitivos/glosas aislados por oraciones completas.
- **PF-A1-006, fila 1 y entradas equivalentes** (por ejemplo, «quedarse dormido; fall asleep»): convertir las glosas en oraciones independientes.
- **PF-A1-007, fila 1 y comienzos de bloque** (por ejemplo, «hace mucho tiempo; a long time ago»): usar cada foco dentro de una oración, no como traducción aislada.
- **PF-A1-008, fila 1 y entradas equivalentes** (por ejemplo, «en la escuela; at school»): reemplazar los fragmentos de ubicación/actividad por oraciones completas.
- **PF-A1-009, fila 1 y comienzos de los bloques siguientes** (por ejemplo, «una buena idea; a good idea»): reemplazar las glosas nominales o verbales por oraciones de uso.

Se repite además un patrón de añadir mecánicamente «Hoy», «El sábado», «Esta semana» o «Por ejemplo» a una misma frase sin cambiar el contexto de forma significativa. Esto infla filas, hace algunas parejas poco naturales o incoherentes y reduce la progresión de frases cortas a más elaboradas. Sustituir esas variantes por usos distintos y pertinentes del vocabulario, manteniendo frases que funcionen por separado:

- **PF-A1-002, filas 2–5**: «Necesito un poco de agua» se repite con esos tres marcadores temporales; diversificar con situaciones sencillas de cantidad/petición en vez de calcar la misma frase.
- **PF-A1-003, filas 28–35 y 196–206**: se anteponen fechas a peticiones de cortesía y a «De nada» («Hoy, de nada»; «El sábado, de nada, aquí tienes el libro»). En particular, «Hoy, de nada» no funciona como respuesta autónoma natural. Reescribir con contextos de intercambio real y sin prefijos temporales arbitrarios.
- **PF-A1-004, filas 29–31, 33–35 y 37–39**: además de la incompatibilidad temporal indicada arriba, las variantes repiten la misma frase con marcadores que no aportan práctica distinta. Rehacerlas como ejemplos variados y coherentes.
- **PF-A1-005, filas 88–91**: «Los alumnos van a la escuela de lunes a viernes» se combina con «El sábado…» en la fila 90, que contradice el horario expresado. Eliminar esa combinación y revisar las demás variantes temporales para que concuerden con el contenido.
- **PF-A1-006, filas 57–61**: «¡Oh, no! El autobús llega tarde» recibe prefijos «Hoy», «El sábado», «Esta semana» y «Por ejemplo»; las inserciones producen ejemplos mecánicos y no una progresión contextual. Sustituirlas por situaciones autónomas y naturales para la interjección.
- **PF-A1-007, filas 54–58**: «Buenos días» se convierte en «Hoy, buenos días…», «El sábado, buenos días…» y «Por ejemplo, buenos días…». El saludo no queda natural ni autónomo con esos añadidos; crear intercambios o frases pertinentes. Revisar también las combinaciones repetidas de «este año» con «Hoy/El sábado/Esta semana» (filas 128–132).
- **PF-A1-008, filas 85–88**: «Hoy/El sábado/Esta semana, quiero decir que podemos ir mañana» antepone marcadores incongruentes a `quiero decir`, que además requiere un contexto previo para aclarar algo. Sustituir por usos naturales y autónomos de la expresión; revisar el mismo patrón repetido en los bloques.
- **PF-A1-009, filas 13–17**: «Me siento bien hoy» se duplica como «Hoy, me siento bien hoy» (redundante), «El sábado, me siento bien hoy» (contradicción temporal) y «Esta semana, me siento bien hoy» (marco poco natural). Corregir las tres variantes y eliminar las repeticiones mecánicas similares del archivo.

## Sesiones completas para omitir en la próxima validación

**Ninguna.** Los nueve CSV requieren al menos una corrección indicada en este informe.
