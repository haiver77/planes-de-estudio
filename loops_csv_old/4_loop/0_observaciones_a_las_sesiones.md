# Auditoría lingüística y técnica — A1, iteración 3

**Plan aprobado:** `loops_plan/12_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**CSV revisados:** `loops_csv/3_loop/A1/`  
**Mínimo exigido:** 150 pares por CSV  
**Informes previos consultados:** `loops_csv/2_loop/0_observaciones_a_las_sesiones.md` y `loops_csv/3_loop/0_observaciones_a_las_sesiones.md`

## Resultado

**NO COMPLETO. Se requiere otra iteración.** La cobertura y los controles técnicos básicos cumplen, y varios errores puntuales de iteraciones anteriores se corrigieron. Sin embargo, persisten defectos de fidelidad al plan, práctica no comunicativa y repetición masiva de frases genéricas. Por eso no se aprueba el conjunto.

## Comprobaciones automáticas

- **Cobertura:** el plan contiene 107 ID A1 y hay exactamente 107 CSV, uno por ID; no hay IDs ausentes ni archivos ajenos.
- **Cantidad:** los 107 archivos contienen exactamente 150 filas cada uno.
- **Formato/codificación:** lectura UTF-8 y análisis CSV estricto correctos en los 107 archivos; dos columnas separadas por `;`, sin filas vacías, campos extra, comillas mal cerradas, saltos de línea incrustados ni `;` dentro de campos. No se encontraron archivos delimitados por comas.
- **Caracteres:** no se detectó texto corrupto (`Ã¡`, `Ã±`, `�`), preguntas españolas sin `¿` ni signos de interrogación usados como sustitutos de letras.
- **Duplicación:** no se detectaron frases españolas idénticas con traducciones inglesas diferentes dentro de un mismo CSV. Sí hay repetición idéntica entre sesiones, señalada abajo.

## Observaciones priorizadas

### P1 — Las unidades de vocabulario se practican como “frases” escritas, no en uso comunicativo

En **101 de los 107 CSV** hay **2.927 filas** que presentan la unidad como “expresión/frase” para leer, explicar, oír, escribir o guardar en un cuaderno. Este patrón no cumple el objetivo recurrente del plan: cinco pares naturales por unidad, en microescenas independientes, con sentido, colocación y categoría propios; tampoco proporciona transferencia contextual ni práctica autónoma.

Ejemplos:

- **`A1-S002.csv`, filas 21–25:** para *all day*, se repiten marcos como «Leo la expresión “all day” en la página» / “I read the phrase ‘all day’ on the page” y «Mi profesor explica la expresión…» / “My teacher explains the phrase…”. Practicar *all day* en situaciones reales, no explicar el rótulo de la unidad.
- **`A1-S003.csv`, filas 1–5:** el mismo molde se aplica a *arrive in after class*; aparte de ser metalingüístico, el ejemplo no da el complemento de lugar que requiere *arrive in*. Redactar frases completas y naturales que practiquen el sentido previsto; no usar la unidad incompleta como si fuera una expresión autónoma.
- **`A1-S031.csv`, filas 34–35, 44–45, 49–50, 54–55 y 59:** “Mi maestra habla de…” / “Aprendo sobre…” ocupan repetidamente pares de *ball*, *band*, *bank*, *bath* y *bathroom*. Sustituir estos rellenos por microescenas que enseñen cada unidad. Por ejemplo, contextualizar *bank* como entidad financiera con una acción o necesidad concreta y distinguir *bath* de *bathroom* sin traducir ambos como «baño» en escenas indistintas.

La observación es transversal: revisar y reconstruir las filas de práctica léxica de todos los archivos afectados, no limitarse a estos ejemplos. Mantener el vocabulario de la sesión, pero convertirlo en frases comunicativas, variadas y completas; comprobar también que los 60 pares previstos para las 12 unidades nuevas (cinco por unidad) realmente practiquen esas unidades.

### P1 — Se mantienen bloques mecánicos y situaciones sin propósito comunicativo

**`A1-S031.csv`, filas 31–55**, conserva bloques de cinco marcos casi calcados: la unidad “está en la foto”, aparece en una explicación escolar o se menciona como tema de aprendizaje. Ejemplos: filas 31 y 34–35 para *ball*; 41 y 44–45 para *band*; 46 y 49–50 para *bank*; 51 y 54–55 para *bath*. Aunque algunas frases aisladas son gramaticales, la secuencia no enseña los usos previstos con variedad ni refuerza vocabulario de forma espaciada útil. Reemplazar los pares repetidos con contextos adecuados a cada lema y con longitud/progresión variadas.

Este defecto continúa la observación previa sobre S031: las primeras frases sobre *autumn/away* sí se corrigieron, pero persisten las plantillas en los bloques siguientes. La corrección parcial no resuelve el incumplimiento del objetivo completo de la sesión.

### P1 — Relleno idéntico reutilizado masivamente entre sesiones

La frase **«Tengo unas cuantas manzanas para el almuerzo» / “I have a few apples for lunch”** aparece idéntica en **53 CSV**, por ejemplo `A1-S001.csv:1`, `A1-S002.csv:61`, `A1-S004.csv:2`, `A1-S005.csv:8` y `A1-S007.csv:85`. **«Necesitamos algunas sillas para la clase» / “We need a few chairs for the class”** aparece idéntica en 30 CSV; por ejemplo, `A1-S001.csv:2`, `A1-S004.csv:3`, `A1-S005.csv:13` y `A1-S008.csv:130`.

Eliminar la reutilización como relleno y reemplazarla por ejemplos pertinentes a las unidades, la gramática, el repaso y la situación comunicativa de cada sesión. La repetición de recuperación debe ser intencional y contextualizada, no una copia literal que ocupa filas de práctica de varias sesiones.

### P2 — Duplicación local y frase redundante en integración final

En **`A1-S107.csv`, filas 127 y 144**, se repite exactamente “I only need one cup today.”; la fila 144 añade además **“hoy”** redundante en «Hoy solo necesito una taza hoy». Eliminar la duplicación o convertirla en un contraste comunicativo real, y corregir la frase española. El antiguo ejemplo de cena duplicado de las filas 13/121 ya no aparece, pero este nuevo caso sigue pendiente.

## Resolución de observaciones anteriores

Se corrigieron varios ejemplos concretos: en `A1-S007.csv`, filas 41–45, las preguntas ya tienen traducciones diferenciadas y naturales; en `A1-S031.csv` se corrigieron los ejemplos iniciales de *autumn/away*; en `A1-S059.csv` ya no aparecen *include with my family*, *a interested place* ni los ejemplos incompletos previamente citados; también se corrigieron los casos de *I see lot* en los archivos señalados, los demostrativos de `A1-S100.csv` y las frases de existencia de `A1-S021.csv`.

No obstante, no se resolvió la observación de fondo de ambos informes previos: revisar integralmente el material, retirar las plantillas y asegurar que cada unidad se practique en contexto. Las 2.927 filas metalingüísticas, las plantillas aún presentes en S031 y el relleno copiado entre decenas de CSV son defectos sustanciales pendientes.

## Cambio requerido

Revisar de nuevo los 107 CSV frente a la unidad, gramática y repaso asignados en el plan; regenerar los pares metalingüísticos o de plantilla con escenas naturales; retirar relleno idéntico entre sesiones; resolver la duplicación de S107; y volver a validar la equivalencia, naturalidad, progresión, transferencia contextual y consistencia global. Conservar UTF-8, dos columnas sin encabezado y al menos 150 filas por archivo.
