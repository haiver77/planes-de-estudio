# Auditoría del plan — `loops_plan_for_phrases/5_loop`

**Resultado: requiere otra iteración.**

## Comprobaciones verificadas

- `resources/Phrase List.txt` contiene 750 registros (A1 129, A2 379, B1 155, B2 57, C1 30; C2 0). Su SHA-256 de bytes es `1372473C7CD5CBD6A6A6FA30A7ACC63723562FDFA4D182362BC25B31987C8756`, igual al del plan.
- El manifiesto del plan tiene 750 IDs únicos. Los niveles y las huellas SHA-256 de las 750 expresiones coinciden con la fuente; las 750 expresiones son únicas tras normalizar Unicode, mayúsculas/minúsculas y espacios.
- La partición declarada suma 5 objetivos de propiedad general y 745 complementarios. Los cinco de propiedad general tienen tabla de evidencia por sesión y foco; los 745 complementarios están listados una vez en las tablas de sesión y tienen destino en el manifiesto. No hay IDs repetidos dentro de la lista complementaria del plan.
- Hay 54 sesiones y 54 nombres de CSV distintos, uno por sesión. Cada sesión define objetivo comunicativo, vocabulario foco, gramática foco, vocabulario en repaso y CSV planificado. El número de objetivos por sesión es de 8 a 20, inclusive; el inventario de expresiones está enumerado explícitamente. Las celdas de repaso indican que no se programa repaso.
- El plan reconoce que la fuente no contiene C2 y conserva las sesiones C2 del plan general sin atribuirles frases C2 nuevas. Indica que los CSV se producirán después, no en esta iteración de planificación; la ausencia de CSV generados aquí es coherente con ese alcance.
- `all over the world` aparece una vez en la fuente y una vez en las tablas/manifiesto de la iteración 5, como `PH-B1-006`, asignada a `PF-B1-003`.

## Observaciones priorizadas

### 1. Resolver el destino anterior de `all over the world`

- **Ubicación:** plan de esta iteración, fila `PF-B1-003` (línea 83); plan de `loops_plan_for_phrases/4_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, fila `PF-B1-018` (línea 122), y su informe de auditoría de la iteración 4.
- **Brecha:** la iteración 4 ya asigna `all over the world` a `PF-B1-018`; la iteración 5 lo asigna a `PF-B1-003`. La iteración 5 no declara que el destino anterior quede retirado o sustituido. Por tanto, aunque no hay duplicado dentro de la iteración 5, no queda demostrada la propiedad única sin repetición entre los destinos existentes que cita el historial de auditoría.
- **Cambio requerido:** identificar inequívocamente un único destino ejecutable para `PH-B1-006` y declarar explícitamente cancelado/sustituido el otro destino antes de producir CSV. No generar la frase en ambos CSV.

### 2. Alinear la cantidad planificada de líneas con el tamaño esperado del CSV

- **Ubicación:** alcance, línea 5, y las 54 filas de sesiones.
- **Brecha:** el plan promete exactamente una frase por expresión objetivo y descarta variantes/relleno. Con 8–20 objetivos por sesión, programa 8–20 líneas por CSV (745 líneas en total; promedio 13,8), muy por debajo de las aproximadamente 150 frases/líneas por sesión indicadas en `contexto.md`.
- **Cambio requerido:** reconciliar explícitamente el diseño de cada CSV con el tamaño esperado de unas 150 líneas, preservando la exclusión de repeticiones y repasos solicitada. Especificar cómo se completará ese volumen con frases naturales y distintas, o justificar/corregir el tamaño planificado; no mantener simultáneamente la promesa de una sola línea por objetivo y el tamaño esperado de 150.

### 3. Añadir criterios verificables de formato y aceptación para los CSV

- **Ubicación:** alcance y sección «Sesiones complementarias planificadas».
- **Brecha:** se nombran archivos futuros y se pide una frase autónoma y natural por objetivo, pero no se fija el contrato de salida ni una lista de aceptación que permita comprobarlos. En particular, el plan no explicita el orden de columnas español/inglés y el separador `;` descritos en `contexto.md`, ni convierte en control verificable la exigencia de `indicaciones_csv.md` de que el pronombre/referente español sea inequívoco cuando el inglés distingue, por ejemplo, `he` de `she`. Tampoco indica que se rechacen pares sin sentido lógico o traducciones no equivalentes.
- **Cambio requerido:** añadir criterios de aceptación explícitos para cada CSV: primera columna español, segunda inglés, separadas por `;`; pares autónomos, naturales, lógicamente coherentes y equivalentes; marcadores resueltos con argumentos concretos; y sujetos/pronombres explícitos o inequívocos en español cuando sean necesarios para determinar la traducción inglesa.

**Siguiente paso:** corregir las observaciones y solicitar otra auditoría de la iteración.
