# Informe de auditoría lingüística y técnica — A1, iteración 21

## Alcance y fuentes

Se auditaron exclusivamente `loops_csv/21_loop/A1/A1-S001.csv` a `A1-S005.csv`, cotejándolos con `indicaciones_csv.md`, el plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv` y todos los contextos y observaciones de `loops_csv/21_loop/0_observaciones_a_las_sesiones.md`. No se revisó ningún otro nivel ni archivo CSV.

## Evidencia técnica, cobertura y distribución

- Los cinco IDs previstos para este alcance están presentes: A1-S001 a A1-S005. No se detectaron IDs faltantes o inválidos entre los cinco solicitados.
- Se verificaron los bytes con decodificación UTF-8 estricta y los registros con parser CSV estricto. Cada archivo contiene 150 líneas físicas y 150 registros lógicos; 750 pares en total. Los 750 registros tienen dos campos no vacíos, español primero e inglés después, delimitados por `;`; no hay encabezado, campos extra, filas vacías, comas usadas como delimitador, punto y coma dentro de frases, comillas mal cerradas ni saltos de línea incrustados. No hay BOM, secuencias de mojibake ni U+FFFD. Las preguntas españolas llevan `¿` y `?` de cierre; no se observó `?` sustituyendo letras ni errores en los caracteres acentuados requeridos.
- Cada sesión contiene 60 ejemplos nuevos en 12 bloques de cinco, de acuerdo con las 12 unidades U del catálogo, y cumple el mínimo obligatorio de 150 pares. No se hallaron pares literalmente duplicados.
- La distribución corresponde al plan: S001, 30 posiciones G01 en filas 61–90 y 60 de integración; S002, 12 de repaso en 61–72, bloque G02 y repaso G01 en 73–102, y 48 de integración; S003, 12 de repaso en 61–72, G03 en 73–102 y 48 de integración; S004, dos cohortes de repaso (61–72 y 73–84), G04 en 85–114 y 36 de integración; S005, dos cohortes de repaso (61–72 y 73–84), G05 en 85–114 y 36 de integración. Los repasos conservan las colocaciones de las unidades previstas.
- Se revisaron expresamente los ejemplos históricos: S002-36–40 son cinco usos reconocibles de `anything else`; S003-61 y S005-73 conservan `sugar` en contextos distintos de las presentaciones de té/café; S005-16–25 establece la perspectiva de llegada para `come into`; S004-56–60 identifica inequívocamente `cell phone` como estadounidense y contrasta con `mobile phone` británico mediante situaciones variadas. Estos puntos están corregidos.
- El inglés mantiene en general la variedad británica (`city centre`, `car park`, `mobile phone`, `neighbour`, `colour`, `film`, `holiday`, entre otros). No se detectó una contradicción dialectal pendiente.
- En S002-73–98 hay 11 preguntas y 6 negativas, además de pares/respuestas breves; por tanto, la variedad de formas señalada en la iteración anterior mejoró y no consiste únicamente en contar preguntas y negativas. Aun así, persiste repetición de un mismo molde, indicada abajo.

## Observaciones pendientes priorizadas

### Prioridad alta — naturalidad y repetición de `a period of time`

1. **A1-S002.csv, filas 46–50; A1-S003.csv, fila 70; A1-S005.csv, fila 82.** La práctica de `a period of time` vuelve a apoyarse en formulaciones rígidas o demasiado formales para intercambios A1. En S002-47, *After a period of time, the children knew the new game well*; S002-48, *My aunt spent a period of time with her sister at home*; y S002-49, *The paint needs a period of time to dry* repiten la misma construcción, con naturalidad desigual. S003-70, *The children spent a period of time indoors...*, no suena idiomático para “pasaron un rato”. S005-82, *The dough needs a longer period of time to rise...*, también puede simplificarse y conserva una inserción formulaica del lema. **Cambio requerido:** mantener explícita la unidad objetivo en ejemplos naturales y variados, usando situaciones cotidianas y ajustando la equivalencia española; no resolverlo repitiendo el mismo molde en las cinco frases.

### Prioridad media — naturalidad del español

2. **A1-S002.csv, fila 43.** *¿Le resulta conocida la dirección del hotel a alguien más?* conserva la idea de *Is the hotel address familiar to anyone else?*, pero el orden resulta forzado en español. **Cambio requerido:** reformular con orden idiomático, por ejemplo, *¿A alguien más le resulta familiar la dirección del hotel?*, sin cambiar el sentido ni la unidad `anyone else`.

### Prioridad media — variedad de estructuras en G02

3. **A1-S002.csv, filas 73–98.** La variedad de preguntas y negativas mejoró (11 preguntas, 6 negativas) y hay pequeñas secuencias autónomas, pero gran parte del bloque sigue organizada alrededor del patrón repetido «este/ese objeto es/son para…» (por ejemplo, filas 73–76, 80–85, 89–95 y 96–98). **Cambio requerido:** conservar las 26 posiciones de G02 y su práctica de artículos, contables, plurales y demostrativos, pero diversificar la función comunicativa y los predicados en algunas frases (identificar, preguntar por disponibilidad o pertenencia, contrastar y responder), evitando que casi toda la transferencia dependa de `for`.

### Prioridad media — vocabulario/contexto por encima del foco A1

4. **A1-S004.csv, filas 26, 28 y 30 (bloque `because of`).** *a safety inspection*, *an airline ... a pilots’ strike* y *construction work* introducen vocabulario o situaciones más especializados de lo necesario para practicar `because of`; en particular, la fila 28 acumula *airline*, *pilots* y *strike*. **Cambio requerido:** sustituir estos motivos por causas familiares y léxico A1 (p. ej., lluvia, nieve, tráfico, una tienda cerrada), manteniendo `because of` y una relación causal clara.

## Elementos revalidados sin observación pendiente

- S001-13 conserva “un par de veces” con *a couple of times*; S001-15 usa *a few times each summer*.
- Las observaciones de contextos especializados citadas para S001-96/116/125/135/137/141/147–148, S002-64/66/68/103, S003-71, S004-72/78/82/84/110 y S005-61/67/70/71/79 se comprobaron en esta iteración y no permanecen como los casos señalados previamente.
- S005-17/19/24 explicitan la perspectiva de llegada para `come into`; S004-78 usa *drops us off* para “nos deja”; S004-110 identifica a la abuela de Ana. S004-56–60 no se limita a repetir una explicación metalingüística: tras la línea de identificación dialectal, presenta situaciones distintas en Texas, California, Ohio y un viaje por Estados Unidos.

## Acción requerida

Corregir únicamente los ejemplos indicados en los cinco CSV de A1 en la siguiente iteración global. Mantener 150 pares por archivo, los 12 objetivos nuevos con cinco pares cada uno, los repasos y su colocación, los bloques gramaticales previstos y las cantidades de integración. Después, volver a revisar naturalidad, equivalencia, nivel léxico, progresión y estructura directamente desde los bytes.
