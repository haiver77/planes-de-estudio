# Reauditoría — Iteración 2, nivel A1

Alcance: `PF-A1-001`, `PF-A1-002` y `PF-A1-003`, en `loops_csv/2_loop/A1/`, contrastadas con el plan aprobado, `indicaciones_csv.md` y el informe anterior. Mínimo obligatorio: 150 pares por CSV.

## Comprobaciones de cobertura, formato y cantidad

- **Cobertura:** los tres ID solicitados están presentes, cada uno con un CSV. Se verificaron los focos del plan: 10 en `PF-A1-001`, 13 en `PF-A1-002` y 19 en `PF-A1-003`.
- **Formato y codificación:** los tres archivos se decodifican como UTF-8 válido y el análisis CSV estricto confirma dos columnas sin encabezado, separadas por `;`; no hay filas vacías, campos adicionales ni saltos de línea incrustados. No se detectaron caracteres de reemplazo ni texto corrupto. Las preguntas en español tienen `¿`.
- **Cantidad:** `PF-A1-001.csv`: 150 pares; `PF-A1-002.csv`: 156; `PF-A1-003.csv`: 152. Todos alcanzan el mínimo.

## PF-A1-001 — `PF-A1-001.csv`

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La observación anterior persiste: se mantienen bloques que repiten la misma oración cambiando solo el adverbio temporal, sin progresión suficiente ni variedad de contextos. Ejemplos: filas 006–015 («me siento mejor»), 026–030 («mi hermano se pierde en la ciudad»), 036–045 («me preparo»), 051–060 («me levanto»), 096–105 («recojo el libro»), 111–120 («me quito el abrigo»), 126–135 («mi prima participa en el juego») y 141–150 («el partido tiene lugar el sábado»). Reemplazar parte de esas variantes por ejemplos distintos, naturales y gradualmente más extensos que practiquen cada foco.

**Reglas incumplidas por línea**

- No se detectaron incumplimientos por línea en esta revisión.

**Regresión del informe anterior:** las observaciones de las filas 044, 086, 087, 088 y 090 están resueltas.

## PF-A1-002 — `PF-A1-002.csv`

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La observación anterior persiste: hay series que conservan la misma estructura y solo sustituyen el adverbio temporal. Ejemplos: filas 007–012 («estoy un poco cansado» / «hace un poco de frío»), 019–024 («quiero/necesito un poco más»), 031–036 («tengo unos pocos libros» / «veo unos pocos pájaros»), 043–048 («quiero un poco de leche»), 055–060 («estoy un poquito ocupado»), 067–072 («necesito un poco más de agua»), 079–084 («necesito mucho más tiempo»), 091–096 («la clase dura media hora»), 103–108 («hay demasiada agua»), 115–120 («quiero ganar dinero»), 127–132 («quiero/ella ahorra dinero»), 139–144 («me gusta mucho») y 151–156 («hay mucha leche» / «tenemos muchos libros»). Sustituir parte de las repeticiones por ejemplos variados y progresivamente más extensos que consoliden el foco.

**Reglas incumplidas por línea**

- **Fila 063 — Regla: Frase con sentido.** «¿Quieres un poco más de arroz?» no corresponde a “Would you like a little more rice?”: la traducción inglesa expresa una oferta cortés que el español no conserva. Reemplazar por: `¿Te gustaría un poco más de arroz?;Would you like a little more rice?`

**Regresión del informe anterior:** la observación de la fila 072 está resuelta.

## PF-A1-003 — `PF-A1-003.csv`

**Reglas generales por archivo incumplidas**

- **Regla: Progresion y repetición incremental.** La observación anterior persiste: se repiten oraciones casi idénticas con cambios de adverbio temporal, sin suficiente progresión ni variedad. Ejemplos: filas 007–008 («ella es mi mejor amiga»), 015–016 («ellos se ayudan el uno al otro»), 031–032 («ellos quieren casarse»), 055–056 («escucho música»), 063–064 («miro la foto»), 071–072 («busco mis llaves»), 087–088 («quiero hablar contigo»), 095–096 («hablamos de la escuela»), 103–106 («digo la verdad»), 119–120 («espero el autobús») y 135–136 («puedo nadar»). Reemplazar parte de esas variantes por ejemplos variados y gradualmente más largos que practiquen cada foco.

**Reglas incumplidas por línea**

- **Fila 137 — Regla: Frase con sentido.** “Would like something.” no es una oración independiente en inglés: falta el sujeto. Reemplazar por: `Me gustaría algo.;I would like something.`

**Regresión del informe anterior:** las observaciones de las filas 108 y 138–144 están resueltas. En la fila 137, la formulación española ya expresa el foco `would like`; el defecto señalado arriba es que la frase inglesa sigue incompleta.

## Sesiones para omitir en la siguiente iteración

Ninguna: las tres sesiones requieren correcciones y otra iteración.
