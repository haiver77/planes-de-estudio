# Informe de auditoría - A1-S001 a A1-S005, iteración global 6

**Resultado:** requiere correcciones y una nueva iteración. Alcance limitado a los cinco CSV indicados, el plan aprobado, el catálogo y las 19 observaciones del informe de iteración 6. No se auditó ningún otro CSV ni `loops_csv_old`.

## Comprobaciones técnicas y de cobertura

- Existen los cinco archivos solicitados y sus IDs corresponden a las cinco sesiones revisadas.
- Validación de bytes y lectura mediante script: los cinco decodifican en UTF-8 estricto, sin BOM; tienen exactamente 150 líneas físicas y 150 registros CSV cada uno. El lector CSV estricto confirma dos campos por fila, sin encabezado, campos vacíos, filas en blanco, comillas mal cerradas ni saltos de línea incrustados. Cada línea contiene exactamente un `;`, por lo que no hay delimitadores dentro de frases ni comas usadas como separador.
- No se encontraron secuencias de mojibake ni caracteres de reemplazo. Los signos `?` ASCII de las muestras son cierres de pregunta válidos; las preguntas españolas tienen el signo de apertura. No se detectaron sustituciones de letras por `?` en los bytes revisados.
- Las filas 1-60 de cada archivo mantienen la organización de doce unidades nuevas, cinco pares por unidad, en orden de catálogo. Los lemas de las unidades nuevas se cotejaron con el catálogo.
- Se comprobaron los bloques de repaso planificados, lema por lema: S002 61-72 (+1 S001), S003 61-72 (+1 S002), S004 61-72 (+1 S003), S004 73-84 (+3 S001), S005 61-72 (+1 S004) y S005 73-84 (+3 S002). Los doce lemas de cada bloque son recuperables inequívocamente; no se exige solo una palabra relacionada.
- No hay pares duplicados exactos en los archivos. Las 19 observaciones del informe anterior se comprobaron contra esta versión y están corregidas; en particular, las filas de repaso, `A1-S005` 25/42/59/79, `A1-S004` 15/16/49/124, `A1-S003` 5/7/54/95/56/60 y `A1-S001` 15 ya no presentan los problemas allí señalados.

## Pendientes priorizados

### Prioridad alta - equivalencia o naturalidad

1. **`A1-S003.csv`, fila 17:** `Mi hermana conoce a sus amigas en la escuela.;My sister meets her friends at school.` *Conocer* expresa saber quiénes son o conocerlas, no encontrarse con ellas como el inglés *meets*. **Cambio requerido:** alinear acción y sentido en ambas columnas, por ejemplo `Mi hermana se encuentra con sus amigas en la escuela.;My sister meets her friends at school.`

2. **`A1-S004.csv`, filas 17-20:** `una mala cosa` es un calco poco idiomático de *a bad thing* en estos ejemplos (`Olvidar el pasaporte es una mala cosa`, `Es una mala cosa dejar la puerta abierta`, etc.). **Cambio requerido:** naturalizar las cuatro traducciones, por ejemplo usando `algo malo` y ajustando la sintaxis de cada oración, sin cambiar el sentido del inglés.

3. **`A1-S004.csv`, fila 22:** `Las cosas malas de ese autobús son que está lleno y que es lento.` La construcción hace que un plural concreto (`las cosas`) tenga como predicado dos cláusulas con `que`; resulta forzada. **Cambio requerido:** reformular con sintaxis natural manteniendo el concepto de *the bad things about*, por ejemplo `Entre las cosas malas de ese autobús están que va lleno y que es lento` o una formulación idiomática equivalente.

4. **`A1-S005.csv`, filas 26 y 28:** `Las diferencias ... están en el sabor` / `... están en el jardín` resulta poco natural y no explica con claridad en qué consisten las diferencias; las versiones inglesas también son rígidas. **Cambio requerido:** expresar que el sabor/jardín es una de las diferencias, por ejemplo `El sabor es una de las diferencias entre el té y el café.;Taste is one of the differences between tea and coffee.` y una reformulación paralela para casa/jardín.

### Prioridad media - gramática no prescrita o desajustes de frase

5. **`A1-S002.csv`, fila 5; `A1-S005.csv`, filas 1, 3 y 130:** aparecen imperativos (`Añade.../Add...`, `Mantén.../Keep...`, `Guarda.../Keep...`, `Ven.../Come...`) que no figuran entre los objetivos gramaticales de esas sesiones ni en su propósito comunicativo inmediato. **Cambio requerido:** sustituirlos por ejemplos afirmativos, negativos o interrogativos de gramática ya prescrita, conservando el lema de vocabulario correspondiente. No se consideran fallo por sí mismas las expresiones de vocabulario expresamente prescritas por el plan/catálogo.

6. **`A1-S001.csv`, fila 23:** `un abrigo abrigado` es redundante y poco natural. **Cambio requerido:** usar una colocación idiomática como `un abrigo cálido` y mantener `a warm coat` en inglés.

7. **`A1-S004.csv`, fila 108:** `¿La receta empieza con cebolla?;Does the recipe begin with an onion?` no conserva el número/cantidad: el inglés especifica una cebolla, mientras que `con cebolla` en español suele ser el ingrediente genérico. **Cambio requerido:** hacer explícita `una cebolla` en español o quitar el artículo unitario en inglés.

8. **`A1-S005.csv`, fila 136:** `¿Hay algún libro sobre la mesa?;Is there any book on the table?` La pregunta inglesa singular con *any* suena marcada en este contexto existencial neutro. **Cambio requerido:** usar `Is there a book on the table?` o pluralizar ambos lados (`Are there any books...? / ¿Hay libros...?`).

9. **`A1-S005.csv`, fila 142:** `No hay mucho tiempo antes del autobús.;There is not much time before the bus.` La versión inglesa queda incompleta/poco idiomática: *before the bus* no aclara el evento temporal. **Cambio requerido:** explicitar llegada o salida en ambas columnas, por ejemplo `No queda mucho tiempo antes de que llegue el autobús.;There isn't much time before the bus arrives.`

**Acción requerida:** corregir las filas señaladas, conservar el formato y las 150 filas por archivo, guardar en UTF-8 y entregar otra iteración para revisión.
