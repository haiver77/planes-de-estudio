# Informe de revisión lingüística y técnica — A1-S001 a A1-S005

**Iteración de entrada:** 27  
**Mínimo obligatorio:** 150 pares por CSV  
**Plan:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Alcance:** exclusivamente `loops_csv/27_loop/A1/A1-S001.csv` a `A1-S005.csv`. No se revisó otro nivel ni `loops_csv_old/`. No se modificó ningún CSV.

## Evidencia comprobada

- **Cobertura y cantidad:** los cinco IDs del alcance están presentes y son válidos. El catálogo asigna 12 unidades nuevas a cada sesión; se verificaron cinco pares por unidad (60 nuevos por CSV). Cada archivo contiene exactamente 150 pares, 750 en total; cumple el mínimo.
- **Codificación y parser desde bytes:** los cinco archivos decodifican con UTF-8 estricto y no tienen BOM. Se parsearon con `csv.reader` estricto, delimitador `;`: cada fichero tiene 150 líneas físicas y 150 registros, dos campos por registro, sin encabezado, campos vacíos, filas vacías, campos extra, comillas mal formadas ni saltos de línea incrustados. Cada línea física contiene exactamente un `;`; no hay líneas delimitadas solo por coma. No se hallaron U+FFFD, secuencias de mojibake ni `?` sustituyendo letras. Todas las preguntas españolas detectadas tienen `¿` de apertura.
- **Evidencia de archivos:** S001 12.874 bytes; S002 13.114; S003 12.669; S004 13.780; S005 13.443.
- **Duplicados:** entre los 750 registros hay 750 pares distintos, 750 frases españolas distintas y 750 frases inglesas distintas.
- **Repasos:** se cotejaron los seis bloques, en su posición y orden U01–U12: S002 filas 61–72 (S001); S003 filas 61–72 (S002); S004 filas 61–72 (S003) y 73–84 (S001); S005 filas 61–72 (S004) y 73–84 (S002). Los seis bloques tienen 12/12 unidades y los ejemplos conservan contextos diferenciados.
- **Gramática e integración:** se revisaron las 30 frases gramaticales de cada sesión: S001 filas 61–90 (G01), S002 y S003 filas 73–102 (G02/G03), y S004 y S005 filas 85–114 (G04/G05). Los objetivos corresponden al plan. Las cantidades de integración son, respectivamente, 60, 48, 48, 36 y 36 pares. Se revisó el contenido de las 750 frases; las observaciones que siguen son pendientes.
- **Observaciones históricas revalidadas:** S002-49 mantiene la corrección del periodo breve; S005-23 conserva la perspectiva de llegada y `come into`; S003-105 incluye el motivo del partido; S002-48, S003-70, S003-149 y S005-82 resuelven los problemas históricos de sentido/naturalidad. S004-27/28 usa causas diferenciadas y S004-104 mantiene una formulación natural. En particular, S005-18 incluye la puerta principal en español e inglés, y S005-19 expresa claramente que el hermano llega del trabajo y entra para cenar, manteniendo `comes into the kitchen`; ambas correcciones son adecuadas y no introducen un error nuevo.

## Observaciones pendientes — requieren otra iteración

### Prioridad alta

1. **A1-S003.csv, fila 126 — sujeto y posesión no equivalentes.**  
   `Ana tiene un profesor con un coche azul.;Ana’s teacher has got a blue car.` En español, Ana es quien tiene un profesor que tiene un coche azul; en inglés, el profesor es el sujeto de `has got` y Ana solo aparece en el posesivo. **Cambio requerido:** conservar el sentido y el objetivo `have got`, por ejemplo: `Ana tiene un profesor con un coche azul.;Ana has got a teacher with a blue car.`

### Prioridad media

2. **A1-S001.csv, fila 13 — el ejemplo no practica la unidad asignada.**  
   `Él me llama un par de veces después del trabajo.;He calls me a couple of times after work.` Las columnas concuerdan entre sí, pero el catálogo asigna `a few times`; `un par de veces / a couple of times` suele indicar dos veces y no conserva con precisión “unas cuantas veces”. **Cambio requerido:** mantener el objetivo léxico de la sesión, por ejemplo: `Él me llama unas cuantas veces después del trabajo.;He calls me a few times after work.`

### Prioridad baja

3. **A1-S001.csv, filas 1–5 — falta progresión de frases cortas a largas dentro de la unidad U01 (`a few`).**  
   El bloque presenta longitudes de 7, 6, 8, 8 y 7 palabras, respectivamente; por tanto, no progresa de forma incremental, aunque las cinco frases sean comprensibles. **Cambio requerido:** ordenar los ejemplos de cada grupo de cinco desde la formulación más breve hacia las más largas y conservar la variedad contextual; aplicar el mismo criterio a los bloques nuevos de las cinco sesiones.

**Resultado:** permanecen observaciones lingüísticas y pedagógicas accionables. Corregirlas y repetir la auditoría de A1-S001 a A1-S005 en la siguiente iteración global.
