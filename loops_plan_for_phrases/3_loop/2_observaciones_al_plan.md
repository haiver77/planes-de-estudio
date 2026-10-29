# Informe de auditoría — `loops_plan_for_phrases/3_loop`

**Resultado: requiere otra iteración.** La trazabilidad de la fuente y varios controles formales están verificados, pero el plan deja de cumplir el propósito de crear sesiones complementarias para generar CSV y no resuelve los problemas de agrupación comunicativa ni la prohibición previa de repetir frases.

## Comprobaciones satisfactorias

- `resources/Phrase List.txt` contiene 750 registros: A1 129, A2 379, B1 155, B2 57 y C1 30; no hay C2. La SHA-256 calculada sobre los bytes coincide con la declarada: `1372473C7CD5CBD6A6A6FA30A7ACC63723562FDFA4D182362BC25B31987C8756`.
- El cotejo por normalización Unicode, mayúsculas/minúsculas y espacios confirma 739 coincidencias con `entrada_normalizada`. Las 11 restantes son exactamente las variantes listadas en la tabla de alias; sus IDs fuente, formas canónicas y sesiones indicadas coinciden con el catálogo de trazabilidad. El único registro repetido del catálogo que afecta a esta lista, `all over the world`, conserva A1-S002 como introducción y A2-S001 como repetición.
- Las diez entradas de la tabla de propiedad general corresponden a objetivos explícitos del plan general en las sesiones indicadas. El plan general conserva C2-S01–C2-S06, y la fuente no aporta entradas C2.
- El plan enuncia controles adecuados de dos columnas, `;`, UTF-8, sin encabezado, resolución de marcadores, equivalencia, pronombres explícitos cuando la omisión sea ambigua y ausencia de relleno. Sin embargo, son criterios escritos para futuros CSV, no evidencia de CSV complementarios efectivamente planificados.

## Observaciones priorizadas

### 1. Alta — La afirmación de propiedad del plan base sustituye el objetivo de crear sesiones complementarias

- **Ubicación:** «Decisión de alcance y resultado de la integración», «Cobertura íntegra por nivel» y «Verificación de cobertura».
- **Brecha:** el plan declara que no genera CSV, no crea sesiones complementarias y asigna **cero** CSV complementarios. La observación de la iteración 2 requería convertir las expresiones de la lista en objetivos de un bloque complementario, con una fila por expresión y un CSV propio; encontrar asignaciones previas en el catálogo evita duplicar propiedad, pero no satisface esa entrega. Además, el plan aprobado de Oxford es el propietario curricular de las expresiones que ya contiene, no prueba que exista un CSV complementario generado para ellas.
- **Cambio requerido:** conservar el cotejo y las exclusiones canónicas, pero definir sesiones complementarias que cubran las entradas que deben producirse y dejar explícita su generación CSV conforme a los controles. Si se propone retirar el objetivo de generar CSV y reutilizar los CSV base, debe solicitarse esa modificación de alcance; no presentarla como cumplimiento del pedido original.

### 2. Alta — No se demuestra una agrupación por escena/subobjetivo ni la naturalidad individual

- **Ubicación:** filas agregadas «A1 — base» a «C1 — base», y dependencia de `sesion_plan` en `loops_plan/12_loop/2_catalogo_trazabilidad_fuentes.csv` y de los tramos del plan aprobado `planes_aprobados/oxford_phrase_list/phrase_list.md`.
- **Evidencia:** las tablas de esta iteración no asignan escenas ni subobjetivos por expresión: remiten a sesiones heredadas y describen objetivos generales por nivel. La asignación heredada conserva tramos de la lista, no una organización nueva que demuestre coherencia. Por ejemplo, las entradas de `Phrase List.txt` que el catálogo asocia con B2-S004 incluyen `both sides`, `bound to do sth`, `bring sb up`, `by now`, `call for sth`, `case study`, `come across sb/sth` y `come true`, mientras que la sesión heredada promete informar, cuestionar o matizar afirmaciones ajenas. El plan no explica subobjetivos que hagan que cada expresión pertenezca a esa escena ni muestra cómo cada una producirá una frase autónoma natural. La advertencia general de que no se fuerce una escena no sustituye esa asignación.
- **Cambio requerido:** formar grupos complementarios por escena comunicativa real y declarar subobjetivos que cubran sus expresiones; comprobar que cada entrada permite una frase española e inglesa autónoma, natural y fiel a su acepción. No basta con heredar la sesión asociada a la forma en el catálogo.

### 3. Alta — Se conserva una repetición incompatible con la regla previa de no repetir frases

- **Ubicación:** «Decisión de alcance y resultado de la integración», nota sobre `all over the world`; catálogo de trazabilidad, introducción A1-S002 y fila de A2-S001.
- **Brecha:** el plan reconoce que `all over the world` vuelve a aparecer en A2-S001 como repaso. La observación de la iteración 2 fijó que no se repitiera ninguna expresión/frase entre sesiones y que no se programaran repasos. Llamar a la segunda aparición «repaso ya registrado» distingue propiedad de introducción, pero no elimina la repetición efectiva.
- **Cambio requerido:** eliminar esa segunda producción de los CSV/sesiones cubiertos por la restricción, o solicitar y documentar explícitamente una excepción al criterio de no repetición. Verificar la ausencia de repeticiones sobre las frases producidas, no solo sobre los propietarios canónicos.

### 4. Media — La declaración de 750 propietarios canónicos en Oxford contradice las diez excepciones

- **Ubicación:** primer párrafo de «Decisión de alcance y resultado de la integración» frente a «Propiedad canónica para solapamientos con el plan general».
- **Brecha:** el primer párrafo afirma que las 750 entradas tienen asignación canónica en el plan aprobado de Oxford; la tabla posterior asigna la propiedad exclusiva de diez entradas al plan general y dice que no deben tener una segunda introducción en Oxford. Por tanto, la cobertura total entre planes puede ser 750/750, pero no es correcto describir las 750 como propiedad canónica de Oxford.
- **Cambio requerido:** presentar la partición sin ambigüedad: 740 entradas con propiedad canónica Oxford y 10 con propiedad canónica general, y reconciliarla en el resumen y las tablas de cobertura. Para cada ID, mantener un único propietario y distinguir asignación de catálogo de producción efectiva.

**Siguiente paso:** corregir el alcance de generación complementaria, demostrar agrupación por escena y frase autónoma, resolver la repetición explícita y armonizar el recuento de propietarios antes de otra auditoría.
