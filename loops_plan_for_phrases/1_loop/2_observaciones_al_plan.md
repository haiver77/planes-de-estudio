# Informe de revisión — `loops_plan_for_phrases/1_loop`

**Resultado: requiere otra iteración.** El plan identifica correctamente el alcance de `resources/Phrase List.txt`, pero aún no resuelve la incompatibilidad entre el límite de no repetición solicitado y la producción de unos 150 pares por sesión, ni demuestra cómo este bloque complementa el programa existente.

## Observaciones priorizadas

### 1. Crítica — La cuota de 150 pares exige repetir los objetivos

- **Ubicación:** «Producción de los CSV», puntos 2, 3 y 5; tablas de sesiones.
- **Brecha:** se pide al menos un par por cada expresión y completar hasta 150 con «variantes y contextos adicionales de esas mismas expresiones». Esto repite los objetivos léxicos dentro del CSV, aunque no los programe en otra sesión ni lo llame «repaso». Los propios cálculos lo hacen explícito: se requieren 21, 23, 24, 24, 72, 73, 93 y 120 líneas adicionales, respectivamente. En especial, C1-S01 tendría 120 pares adicionales para solo 30 expresiones objetivo. Además, `indicaciones_csv.md` propone explícitamente práctica progresiva con repetición, lo que no coincide con la petición de no incluir repeticiones ni repasos.
- **Cambio requerido:** definir «repetición» de manera inequívoca y hacer prevalecer la petición de esta iteración sobre las indicaciones generales incompatibles. Si no se permite reutilizar ningún objetivo, eliminar la cuota rígida de 150 y ajustar el tamaño del CSV al material único disponible; no completar el volumen repitiendo expresiones. Si se pretendía prohibir solo repasos entre sesiones, dejar esa excepción aprobada y explícita antes de generar los CSV. No presentar variantes de un mismo objetivo como ausencia de repetición.

### 2. Alta — La carga y la organización temática no son factibles para sesiones coherentes

- **Ubicación:** todas las tablas, sobre todo A1-S01 (129 expresiones), A2-S01–S03 (126–127 cada una), B1-S01–S02 (77–78), B2-S01 (57) y C1-S01 (30); «Alcance e identificación del vocabulario».
- **Brecha:** se asignan tramos consecutivos por orden de aparición, no por una secuencia comunicativa o gramatical demostrada. Así, cada sesión debe abordar decenas o más de cien expresiones, mientras su objetivo comunicativo es amplio y su gramática focal agrupa varios patrones. La instrucción de crear microescenas separadas cuando las expresiones no compartan contexto confirma que el foco de una misma sesión no necesariamente forma una unidad pedagógica. Para producir pares naturales y autónomos, cubrir cada expresión y mantener calidad, los CSV más cargados exigirían una gran cantidad de microescenas y objetivos distintos; en las sesiones con pocos objetivos, alcanzar 150 agravaría el problema mediante la reutilización señalada arriba.
- **Cambio requerido:** redistribuir las expresiones en grupos más pequeños y comunicativamente coherentes, relacionando cada grupo con su objetivo y gramática, y especificar los subobjetivos o tipos de enunciado que permitirán producir pares autónomos. Establecer el volumen después de respetar la regla de no repetición, no al revés. Si los rangos actuales se conservan, aportar una justificación y un método verificable que demuestren que cada sesión puede generar su volumen sin frases de relleno ni mezcla artificial de contextos.

### 3. Alta — Falta trazabilidad estable de cada expresión hasta el objetivo del CSV

- **Ubicación:** «Alcance e identificación del vocabulario» y rangos `PH-...` de las tablas.
- **Brecha:** el plan define códigos como ordinales dentro de las líneas de cada nivel y declara cobertura completa. El cotejo de la fuente confirma 750 entradas: A1 129, A2 379, B1 155, B2 57 y C1 30; los rangos propuestos suman esos totales sin solapamiento y C2 no aparece. Sin embargo, `Phrase List.txt` no contiene esos códigos y el plan no proporciona un índice que relacione cada código con su entrada fuente. La identificación depende de volver a contar el archivo y de que su orden no cambie; tampoco se especifica una versión o huella de la fuente. Esto dificulta auditar qué expresión debe aparecer en cada CSV y detectar omisiones o asignaciones incorrectas.
- **Cambio requerido:** añadir un manifiesto de trazabilidad verificable con nivel, ordinal estable, sesión asignada y referencia exacta a la entrada de origen; fijar la versión/huella del archivo. Usarlo para comprobar que cada entrada aparece exactamente en el objetivo previsto y en ningún otro CSV. No hace falta duplicar el manifiesto dentro de las frases generadas, pero sí que la generación pueda cotejarse contra él.

### 4. Alta — No se demuestra la integración como complemento del plan existente

- **Ubicación:** «Alcance e identificación del vocabulario», progresión A1–C1 y sección C2.
- **Brecha:** el documento define ocho sesiones propias, pero no identifica qué versión del plan existente complementa, cómo se ordenan sus sesiones respecto de este bloque, ni cómo se evita duplicar objetivos ya cubiertos. El plan base de `loops_plan/1_loop/1_plan_estudio_por_sesiones_de_repeticion.md` define una progresión A1–C2 y excluye expresamente el material de frases para que se incorpore por separado. Este plan reconoce correctamente que `Phrase List.txt` no tiene entradas C2, pero no enlaza esa carencia con la cobertura C2 del programa base. Por ello, aislado, no acredita una progresión completa A1–C2 ni su función concreta de complemento.
- **Cambio requerido:** nombrar y referenciar el plan base y la versión de sus sesiones; explicar si estos CSV son un bloque paralelo o una ampliación, dónde se insertan y qué mecanismo evita duplicaciones con el material ya asignado. Mantener C2 como límite de la fuente —sin inventar entradas—, pero indicar explícitamente cómo se conserva la cobertura C2 en el plan general.

### 5. Media — Las instrucciones de CSV necesitan criterios de validación y una regla de cantidad coherente

- **Ubicación:** «Producción de los CSV», puntos 1–5.
- **Brecha:** están definidos el par español–inglés, el separador `;`, UTF-8 y la ausencia de encabezado, además de un archivo por sesión. No se resuelve, sin embargo, la discrepancia entre «aproximadamente 150», el requisito de incluir cada objetivo y los totales orientativos exactos que suman 150; tampoco se fija un patrón de nombre de archivo ni controles de aceptación para cotejar líneas y objetivos. La regla de completar marcadores (`sb`, `sth`, `do sth`, `X` o puntos suspensivos) no exige registrar el referente elegido para comprobar que conserva el sentido de la expresión.
- **Cambio requerido:** una vez resuelta la observación 1, especificar si el volumen es un objetivo aproximado o una cantidad obligatoria, con una regla que no induzca repeticiones; fijar el nombre de cada CSV y un control de formato (dos campos, separador, codificación, sin encabezado) y de cobertura (objetivos requeridos presentes, sin objetivos ajenos ni repetidos, según la regla acordada). Incluir un criterio para verificar la naturalidad, equivalencia de sentido y resolución de marcadores en cada par.

**Siguiente paso:** corregir estas brechas en una nueva iteración y solicitar una nueva auditoría antes de generar o aprobar los CSV.
