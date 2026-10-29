# Revisión lingüística y técnica — A1, iteración 1

Fuente aprobada: `loops_plan/12_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
CSV revisados: `loops_csv/1_loop/A1/`  
Mínimo exigido: 150 pares por archivo

## Resultado

No cumple. Se requiere otra iteración y una revisión integral de los contenidos lingüísticos; no basta con corregir los ejemplos citados.

## Comprobaciones automáticas de cobertura y formato

- **Cobertura:** el plan contiene 107 ID A1 distintos y hay exactamente un archivo para cada uno (`A1-S001.csv`–`A1-S107.csv`), sin ID ausentes ni archivos ajenos.
- **Cantidad:** los 107 archivos tienen exactamente 150 filas.
- **Codificación y estructura:** los 107 archivos se decodifican como UTF-8 y el análisis estricto confirma dos campos por fila separados por `;`, sin errores de comillas CSV ni filas vacías. Las comas presentes en el texto no se usan como delimitador.
- Estos resultados técnicos no compensan los problemas sustanciales de equivalencia, naturalidad, fidelidad léxica y gramática descritos abajo.

## Observaciones priorizadas

### P1 — Pares incorrectos o no utilizables como modelos de inglés

1. **`A1-S007.csv`, filas 41–45 — equivalencia y situación incorrectas.** La secuencia española usa «¿Te va bien?» y «¿Estás progresando?» en escenas con un vecino, un cajero, una maestra y una llamada; todas se traducen como **“Are you getting on?”**. Esa traducción no conserva el sentido de las preguntas españolas en esos contextos y no es una pregunta natural para dirigirse a un cajero. Traducir de nuevo cada turno según la intención concreta (por ejemplo, preguntar si algo le parece bien, cómo está alguien o si está progresando); no reciclar una única traducción para todos.

2. **`A1-S031.csv`, primeras filas y bloque de “away” — vocabulario insertado en marcos incompatibles.** Ejemplos: **“The autumn is in the picture”** / «El otoño está en la foto»; **“I read about an autumn”** / «Leí sobre un otoño»; **“I see my friends away”** / «Veo a mis amigos lejos»; **“We meet at the café away”** / «Nos reunimos en el café de distancia». Son construcciones literales o no idiomáticas que no enseñan los sentidos ni colocaciones naturales de *autumn* y *away*. Sustituirlas por escenas plausibles y equivalentes, conservando el sentido y la categoría de cada unidad.

3. **`A1-S059.csv` — errores de traducción y frases incompletas.** Ejemplos: **“The room is small if comfortable”** para «La habitación es pequeña aunque cómoda» (invierte *aunque* por *if*); **“I buy bread if milk”** para «Compro pan si leche» (inglés incompleto); **“I imagine with my family”** para «Me imagino con mi familia» (marco verbal inadecuado para el sentido pretendido). Reescribir ambos lados como frases completas, naturales y equivalentes; comprobar especialmente conectores y complementos verbales.

4. **`A1-S107.csv` — errores en frases de práctica y en contexto temporal.** Ejemplos: **“In the evening, we ate lunch at home last Sunday”** emparejado con «Por la noche, el domingo pasado almorzamos en casa» mezcla noche y almuerzo y suena contradictorio; **“I see lot at the table”** («Veo mucho en la mesa») es agramatical y además no expresa una escena clara. Corregir tiempo, aspecto, artículos y contexto, y revisar todas las frases de integración con el mismo criterio.

### P1 — Las unidades del vocabulario foco se mencionan, pero no se practican en uso comunicativo

- **`A1-S021.csv`, filas 1–30**, repite para cada entrada marcos como “Leo la expresión «…» en la página”, “Mi profesor explica la expresión «…»” y “La expresión «…» está en mi cuaderno”. Incluso unidades comunicativas como *thank you* quedan reducidas a hablar de la expresión escrita, no a agradecer a alguien.
- **`A1-S007.csv`** repite el mismo patrón de cinco marcos metalingüísticos para entradas como *get home*, *get married*, *get off* y *get on*. El bloque siguiente vuelve a forzar preguntas sobre *get on* en escenas inadecuadas.
- Rehacer los pares para que cada unidad se use con su sentido y colocación propios en intercambios autónomos y realistas, como exige el plan. No presentar el lema/expresión como objeto de lectura o explicación salvo que esa sea realmente la situación comunicativa de la unidad.

### P1 — Plantillas repetidas y sustitución mecánica generan usos absurdos

- En **`A1-S031.csv`**, aparecen marcos casi idénticos para muchas entradas: “está en la foto”, “leí sobre…”, “oigo la expresión…”, “mi maestra habla de…” y “aprendo sobre…”. En **`A1-S059.csv`** se repiten series de cinco sujetos y momentos del día con construcciones defectuosas como *imagine with my family*, *improve with my family* e *include with my family*.
- Esa repetición no proporciona la variedad, transferencia contextual ni recuperación espaciada útil que pide el plan; cambia una palabra dejando intacto un marco que no siempre admite esa palabra. Revisar la distribución de los 150 pares de cada sesión, eliminar relleno de plantilla y dar a cada unidad un contexto y complementos compatibles. Mantener variedad de longitud y que cada fila funcione por separado.

### P2 — Gramática, artículos y naturalidad en los bloques de integración

- En **`A1-S059.csv`**: **“That is a important place for lunch”** requiere *an important place*; además, varios verbos se presentan sin el complemento necesario.
- En **`A1-S107.csv`**: **“I see lot at the table”** requiere una estructura completa (por ejemplo, un objeto y el cuantificador adecuado); no se debe conservar como modelo.
- Corregir de forma sistemática artículos, preposiciones, complementos, conectores, concordancia y orden de palabras, y cotejar cada bloque con el foco gramatical y el repaso de la sesión en el plan. Los ejemplos no deben introducir formas incorrectas como si fueran práctica válida.

## Cambio requerido para la siguiente iteración

Revisar y regenerar lingüísticamente los CSV de A1 afectados —con control explícito de cada par, no mediante sustitución mecánica de lemas— y volver a auditar los 107 archivos. Mantener exactamente un CSV por ID, UTF-8, dos columnas separadas por `;` y al menos 150 pares. Presentar los cambios con frases completas, idiomáticas y equivalentes, adecuadas al objetivo léxico y gramatical de cada sesión, sin duplicados de relleno ni plantillas reiteradas sin propósito.
