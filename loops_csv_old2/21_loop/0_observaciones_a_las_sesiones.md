# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración global 20

**Resultado: requiere correcciones; se necesita otra iteración global.**

## Alcance y fuentes

Se auditaron exclusivamente `A1-S001.csv` a `A1-S005.csv` en `loops_csv/20_loop/A1/`, cotejándolos con `indicaciones_csv.md`, el plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv` y las observaciones históricas en `loops_csv/20_loop/0_observaciones_a_las_sesiones.md`. No se revisaron otros CSV ni `loops_csv_old`.

## Evidencia técnica y de cobertura

- La carpeta contiene exactamente los cinco IDs solicitados, sin faltantes ni CSV ajenos al alcance.
- Se comprobaron los bytes reales con decodificación UTF-8 estricta y parser CSV estricto. Los cinco archivos son UTF-8 válido, sin BOM, sin U+FFFD ni secuencias reales de mojibake `Ã`/`Â`. Tamaños: S001 12 984 bytes; S002 13 776; S003 12 651; S004 14 244; S005 13 521.
- Cada archivo tiene exactamente 150 líneas físicas y 150 registros: 750 pares en total. Cada registro tiene dos campos no vacíos, español primero e inglés después, delimitados por `;`; no hay encabezado, filas vacías, campos adicionales, comillas mal cerradas, saltos incrustados ni comas usadas como delimitador. Todas las preguntas españolas tienen apertura `¿` y cierre `?`; no se hallaron signos `?` sustituyendo letras ni errores en los caracteres acentuados inspeccionados.
- No se encontraron pares duplicados literalmente. Los defectos pendientes son de calidad, colocación, contexto y equivalencia (detallados abajo), no de estructura o cantidad.
- Las cinco sesiones tienen 60 ejemplos nuevos en bloques de 12 × 5 y cumplen el mínimo explícito de 150 pares. Los repasos previstos tienen 12 pares por cohorte/evento y las unidades sí son identificables: S003-61 y S005-73 recuperan `a little sugar` en contextos distintos de té/café; también se comprueban las demás colocaciones de las cohortes. La distribución respeta 30 posiciones gramaticales por sesión: S001-61–90 (G01), S002-73–102 (G02 y repaso previsto de G01), S003-73–102 (G03), S004-85–114 (G04) y S005-85–114 (G05). El resto completa las 60/48/48/36/36 posiciones de integración indicadas en el plan.
- La variedad léxica inglesa es predominantemente británica (`centre`, `colour`, `car park`, `mobile phone`, etc.). `Cell phone` está marcado explícitamente como uso estadounidense en S004-56–60 y S005-72; no obstante, las cinco líneas nuevas de S004 son casi todas metalingüísticas y repiten el contraste US/UK en vez de ofrecer situaciones de uso variadas.

## Observaciones históricas revalidadas

- **Corregido:** S002-36–40 contienen cinco ejemplos reconocibles de `anything else`.
- **Corregido:** S003-61 y S005-73 conservan `sugar` y cambian el contexto respecto de la introducción.
- **Corregido:** S005-16 y S005-25 hacen explícito el destino asociado al hablante/interlocutor; persiste ambigüedad en otras filas del mismo bloque (observación 3).
- **Corregido:** S004-124/125 ya no repiten la misma foto/periódico; ahora son escenas distintas. También se sustituyeron varios escenarios especializados señalados antes (entre ellos S003-61/62/66/72, S004-76, S005-61/77/78/84 y S002-124/125). Sin embargo, todavía hay contextos con carga técnica o vocabulario poco A1 en otras filas (observación 4).
- **Parcialmente corregido:** S002-73–98 tiene más variedad de objetos y propósitos que la plantilla anterior, pero sigue siendo mayoritariamente una secuencia de afirmaciones aisladas (solo seis preguntas y una negativa en 26 filas), con poca transferencia mediante intercambios o contraste de formas (observación 5).
- **Pendiente:** permanece la inserción rígida de `a period of time` en varias filas de S002, S003 y S005 (observación 1).

## Observaciones pendientes priorizadas

### Prioridad alta — fraseología artificial repetida

1. **A1-S002.csv, filas 46–50 y 110; A1-S003.csv, fila 70; A1-S005.csv, fila 82.** La expresión `a period of time` sigue utilizada como relleno o molde, en vez de una frase cotidiana idiomática. En S002-47, *I read before bed for a period of time* no suena natural; S002-48 define el recreo como *a period of time for a snack and a rest*; S002-50 usa *There is a period of time each afternoon when...*. S002-46/49 también repiten la construcción rígida, y S002-110 añade *after a short period of time* donde bastaría *after a short while*. S003-70 traduce *pasan un rato* mediante el poco idiomático *there is a period of time when*. S005-82 agrega la misma fórmula al reposo de la masa sin que el periodo se especifique. **Cambio requerido:** mantener la unidad objetivo en ejemplos naturales y variados, eliminando las definiciones/rellenos y ajustando la equivalencia española; no repetir cinco veces el mismo molde.

### Prioridad alta — equivalencia, gramática de uso y dirección

2. **A1-S001.csv, fila 13; fila 15.** S001-13 traduce *un par de veces* como *a few times*, que no conserva la cantidad (un par significa dos). S001-15, *a few times in summer*, es una colocación poco idiomática. **Cambio requerido:** usar *a couple of times* en inglés o cambiar el español a *unas cuantas veces* en la fila 13; en la fila 15 usar una formulación natural como *a few times each summer*.

3. **A1-S005.csv, filas 17, 19 y 24 — `come into` aún carece de perspectiva de llegada explícita.** A diferencia de S005-16/25, corregidas, estas líneas dicen que el gato, el hermano o la hermana “come into” un lugar sin establecer que el hablante/interlocutor esté allí. **Cambio requerido:** hacer explícita esa perspectiva en español/contexto o usar una forma neutral (`goes into`/`enters`) donde el movimiento no sea hacia el hablante.

4. **A1-S005.csv, fila 61; A1-S004.csv, fila 110.** S005-61 traduce *lejos de la cocina* como *away from the cooker*: *cocina* aquí puede significar habitación, mientras que *cooker* es el electrodoméstico. S004-110 usa *su abuela* sin antecedente que determine género, pero traduce *her grandmother*. **Cambio requerido:** alinear *kitchen/cooker* con *cocina/estufa* según el sentido pretendido y explicitar la persona en S004-110 (p. ej., “la abuela de Ana”) o neutralizar la referencia inglesa.

5. **A1-S002.csv, fila 130; fila 140; A1-S004.csv, fila 78.** S002-130, *Comemos todo el almuerzo*, suena a calco en español; usar *Nos comemos todo el almuerzo* o *Terminamos todo el almuerzo*. En S002-140, *some years older* es menos natural que *a few years older*. S004-78 traduce *el autobús nos deja cerca del museo* como *the bus takes us close to the museum*, que pierde el matiz de dejar/bajar pasajeros. **Cambio requerido:** naturalizar las formulaciones en ambos idiomas sin alterar el sentido.

### Prioridad alta — nivel A1 y contextos especializados

6. **A1-S001.csv, filas 96, 116, 125, 135, 137, 141, 147–148; A1-S002.csv, filas 64, 66, 68 y 103; A1-S003.csv, fila 71; A1-S004.csv, filas 72, 82 y 84; A1-S005.csv, filas 67, 70, 71 y 79.** Persisten ejemplos con vocabulario o situaciones que desplazan el foco A1: prueba de micrófono/presentación, sala de curas, auditorio/ensayo, guía de acuario, pinchazo/mecánico, ascensor de una compañía, pista de atletismo/copias digitales; beca de arte, entrada de museo/grupo escolar, club infantil y refugio; exposición de centro de ciencias; sesión de retratos de campaña, contrato y refugio; recorrido histórico de castillo, código QR/escáner, aparcamiento de hospital y código de seguridad de fábricas. **Cambio requerido:** sustituir los casos más cargados por situaciones familiares (casa, clase, comida, transporte, compras, familia o amistades), conservando el lema objetivo y la estructura de la fila con vocabulario de apoyo A1.

### Prioridad media — progresión y consistencia

7. **A1-S002.csv, filas 73–98 (bloque G02).** Se amplió la variedad de objetos y propósitos, pero el tramo sigue concentrado en afirmaciones de identificación/uso de objetos; de 26 filas, solo seis son preguntas y una es negativa. **Cambio requerido:** manteniendo las 30 posiciones gramaticales planificadas, convertir una parte de los ejemplos en preguntas/respuestas funcionales, negativas y mini-secuencias autónomas; distribuir mejor artículos, contables, plurales y demostrativos, sin volver a una plantilla repetida.

8. **A1-S004.csv, filas 56–60.** Los cinco ejemplos de `cell phone` reiteran casi la misma explicación comparativa US/UK (amigo estadounidense/británico, tienda, explicación de uso, forma de formulario). Aunque la etiqueta dialectal es correcta, la serie no ofrece cinco contextos de uso variados. **Cambio requerido:** mantener inequívoco que `cell phone` es estadounidense y `mobile phone` británico, pero diversificar la práctica y evitar repetir la explicación metalingüística.

## Acción requerida

Corregir únicamente los cinco CSV auditados en la siguiente iteración global. Mantener 150 pares por archivo, cinco ejemplos claros para cada una de las doce unidades nuevas, colocaciones objetivo en cada repaso 12/12, 30 posiciones gramaticales pertinentes y las proporciones de integración del plan. Revalidar desde los bytes UTF-8, estructura CSV, puntuación, equivalencia, naturalidad, progreso y repaso.