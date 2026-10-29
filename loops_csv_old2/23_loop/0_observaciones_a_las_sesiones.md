# Informe de auditoría lingüística y técnica — A1, iteración 22

## Alcance y comprobaciones

Se auditaron exclusivamente `A1-S001.csv` a `A1-S005.csv` en `loops_csv/22_loop/A1/`, frente al plan aprobado, el catálogo de trazabilidad, `indicaciones_csv.md` y las observaciones históricas de `loops_csv/22_loop/0_observaciones_a_las_sesiones.md`.

- Los cinco IDs solicitados están presentes y son válidos; no hay IDs ausentes ni ajenos dentro del alcance.
- Los cinco archivos tienen 150 líneas físicas y 150 registros lógicos cada uno (750 pares en total). La decodificación estricta de los bytes confirma UTF-8 válido, sin BOM, mojibake ni U+FFFD. El parser CSV estricto confirma dos campos no vacíos por fila, español primero, separados por `;`; no hay encabezado, campos extra, filas vacías, punto y coma dentro de los campos, comillas mal cerradas ni saltos de línea incrustados. No se detectaron preguntas sin `¿`, pares literalmente duplicados ni signos `?` dentro de palabras.
- Cada sesión contiene 60 ejemplos nuevos en 12 grupos de cinco, correspondientes a las 12 unidades de su sesión en el catálogo. Se cumple el mínimo de 150 pares.
- La distribución global y las posiciones de los bloques gramaticales concuerdan con el plan: S001, 30 G01; S002, 26 G02 y 4 G01; S003, 30 G03; S004, 30 G04; S005, 30 G05, además de los repasos e integración previstos. En S002, las filas 73–98 muestran ya variedad contextual y funcional de G02 —identificación, disponibilidad, contraste y respuesta— con artículos, contables, plurales y demostrativos; no se mantiene el molde repetitivo señalado antes.
- Se revalidaron las observaciones históricas: S002-43 está reformulada con orden natural; S004-26/28/30 usan causas familiares (lluvia, tráfico y nieve); S002-36–40 y S003-61/S005-73 son usos adecuados de sus objetivos; la distinción dialectal de S004-56–60 y la perspectiva de llegada en S005-16/19/24 están presentes. También se revisaron las referencias históricas restantes de S001-13/15, 96, 116, 125, 135, 137, 141 y 147–148; S002-64, 66, 68 y 103; S003-71; S004-72, 78, 82, 84 y 110; y S005-61, 67, 70, 71 y 79. No se reabren como defectos los puntos corregidos; quedan las observaciones siguientes.

## Observaciones pendientes priorizadas

### Prioridad alta

1. **A1-S005.csv, filas 21–25 (unidad U05, `He came into the room.`): adelanto de gramática.** El bloque amplía el lema con pasado simple e imperfecto y varias acciones pasadas no previstas en G05: *was outside*, *was waiting*, *knocked*, *waited*, *arrived* y *came*. El pasado simple se introduce más adelante en A1-S009. **Cambio requerido:** mantener la unidad léxica fijada por el plan, pero evitar que sus cinco ejemplos enseñen además una secuencia de pasado; use marcos y cláusulas ya permitidos, o reserve la práctica gramatical ampliada para la sesión prevista.

2. **A1-S004.csv, fila 57: adelanto de tiempos.** *Mi amiga de Texas perdió su teléfono y lo busca… / My friend in Texas lost her cell phone and is looking…* combina pasado simple (`lost`) y presente continuo (`is looking`) antes de los bloques correspondientes del plan. **Cambio requerido:** conservar el ejemplo de `cell phone`, pero expresarlo con gramática ya introducida, por ejemplo, mediante una acción habitual en presente simple.

3. **A1-S002.csv, filas 46–50; A1-S003.csv, fila 70; A1-S005.csv, fila 82: el uso de `a period of time` sigue sin ser suficientemente natural y variado.** En S002 se repite cinco veces seguidas el mismo recurso; formulaciones como *The library is quiet for a period of time each day*, *My brother works at the café for a period of time each summer* y *For a period of time after school, I read in the park* suenan rígidas o forzadas para situaciones cotidianas A1. S003-70 (*stay at home for a period of time*) y S005-82 (*stays open for a period of time*) prolongan el mismo molde en los repasos. **Cambio requerido:** revisar el bloque completo y los dos repasos, conservando el objetivo explícito solo en ejemplos idiomáticos; variar situaciones y construcción, y ajustar el español para que mantenga exactamente el sentido.

### Prioridad media

4. **A1-S005.csv, filas 74–76: orden incorrecto del segundo repaso de A1-S002.** El bloque de 12 filas 73–84 contiene las 12 unidades y los contextos son nuevos, pero las tres primeras unidades tras `a little sugar` están desplazadas: fila 74 practica `a lot to do` (U03), fila 75 `a lot of sth` (U04) y fila 76 `a lot` (U02). **Cambio requerido:** respetar el orden de colocación del catálogo en las posiciones 74–76: U02 (`a lot`), U03 (`a lot to do`) y U04 (`a lot of sth`), usando contextos distintos de los de introducción.

5. **A1-S003.csv, fila 107: equivalencia imprecisa para `ask for`.** *Pido un bolígrafo prestado a mi compañero* significa que tomo prestado un bolígrafo; *I ask my classmate for a pen* solo expresa que se lo pido. **Cambio requerido:** si se mantiene el objetivo `ask for`, quitar `prestado` del español; si se conserva esa palabra, cambiar el inglés a *I borrow a pen from my classmate*.

6. **A1-S004.csv, filas 27–28 y 102/104: diversidad y adecuación léxica de las causas.** Las causas previstas en 26/28/30 ya son sencillas, pero 27 y 28 repiten casi el mismo ejemplo de llegar tarde por el tráfico, cambiando solo el sujeto. Además, `roadworks` (fila 102) y `maintenance` (fila 104) son menos básicos que las causas pedidas para A1. **Cambio requerido:** variar uno de los pares 27/28 con otra causa o consecuencia cotidiana, y simplificar el léxico de 102/104 para que la práctica siga siendo accesible a A1.

## Acción requerida

Corregir únicamente los ejemplos señalados en estos cinco CSV de A1 en la siguiente iteración global. Mantener los 150 pares por archivo, los 12 objetivos nuevos con cinco pares cada uno, los repasos en sus posiciones y los bloques gramaticales del plan; después, volver a revisar equivalencia, naturalidad y gramática desde los bytes.
