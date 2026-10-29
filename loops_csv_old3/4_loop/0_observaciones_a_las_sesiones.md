# Auditoría de PF-A1-001 — iteración 3

Archivo: `loops_csv/3_loop/A1/frases_PF-A1-001_v1.csv`

Comprobación estructural: lectura UTF-8 estricta válida; 150 filas físicas no vacías, 150 pares parseados, dos campos por fila separados por un único `;`, sin encabezado, campos vacíos, filas multilínea ni texto corrupto. Se verifican 10 bloques de 15 frases. Se reexaminaron las observaciones previas: las filas 26 y 102 ya fueron corregidas.

## Observación pendiente

- **Media — fila 53:** `Mi hermana se levanta antes de la escuela.;My sister gets up before school.` La construcción española «antes de la escuela» resulta poco idiomática/ambigua como referencia a la hora de levantarse, y no explicita la acción que precede a la escuela. Cambiar a, por ejemplo: `Mi hermana se levanta antes de ir a la escuela.;My sister gets up before going to school.` Mantener el foco `get up` y una traducción natural equivalente.
