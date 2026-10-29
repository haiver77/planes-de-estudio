# Auditoría A1 — generación de iteración 5

Fuente de verdad: `planes_aprobados/oxford_phrase_list/plan_frases_oxford.md` (plan aprobado indicado por el solicitante). Alcance: archivos de generación en `loops_csv/5_loop/A1/`. El informe previo en `loops_csv/5_loop/0_observaciones_a_las_sesiones.md` corresponde a la iteración 4; se consultó solo como regresión para PF-A1-001, no como resultado de esta auditoría.

## Resultado

Requiere correcciones y otra iteración. Se verificó el **mínimo explícito de 150 frases por CSV**: `frases_PF-A1-001_v1.csv` tiene 150 filas de frases y cumple el mínimo. No se editaron el CSV ni el plan.

## Observaciones priorizadas

### Prioridad alta — cobertura incompleta del nivel A1

El plan aprobado contiene nueve IDs de sesión A1 y define un CSV por cada uno. En `loops_csv/5_loop/A1/` solo existe `frases_PF-A1-001_v1.csv`. Faltan, por tanto, los siguientes archivos/IDs; generarlos con al menos 150 frases cada uno y conforme a sus objetivos del plan:

- `PF-A1-002` — `frases_PF-A1-002_v1.csv`
- `PF-A1-003` — `frases_PF-A1-003_v1.csv`
- `PF-A1-004` — `frases_PF-A1-004_v1.csv`
- `PF-A1-005` — `frases_PF-A1-005_v1.csv`
- `PF-A1-006` — `frases_PF-A1-006_v1.csv`
- `PF-A1-007` — `frases_PF-A1-007_v1.csv`
- `PF-A1-008` — `frases_PF-A1-008_v1.csv`
- `PF-A1-009` — `frases_PF-A1-009_v1.csv`

### Prioridad alta — gramática por encima del alcance A1

Archivo `frases_PF-A1-001_v1.csv`:

- **Fila 78:** «Asegúrate de que la puerta esté cerrada.» — `esté` es subjuntivo; excede el alcance de gramática declarado para esta sesión (verbos frecuentes en presente/pasado simple e imperativos cuando los requiera el foco). Reformular en español con gramática A1 y conservar la equivalencia con “Make sure the door is closed”; por ejemplo, usar una construcción con infinitivo y ajustar el inglés para que ambas frases expresen exactamente lo mismo.
- **Fila 84:** «Asegúrate de que el niño esté seguro.» — el subjuntivo `esté` queda fuera del alcance A1 declarado. Reformular ambos lados de la pareja con una construcción natural de nivel A1 que preserve el sentido y el foco `make sure`.
- **Fila 89:** «Asegúrate de que la ventana esté cerrada antes de salir.» — el subjuntivo `esté` queda fuera del alcance A1 declarado. Reformular la pareja con gramática A1 y preservar el sentido de comprobación antes de salir; revisar también que la versión inglesa siga correspondiendo.

## Comprobaciones aprobadas para PF-A1-001

- El nombre del archivo coincide con el plan y hay un CSV para ese ID.
- Lectura mediante script con decodificación UTF-8 estricta: válida; 150 filas, sin filas vacías, cada fila tiene exactamente dos campos no vacíos y un único `;`; sin encabezado, campos extra ni comillas mal cerradas. No se detectaron `;` dentro de frases, corrupción (`Ã¡`, `Ã±`, `�`) ni `?` sustituyendo `¿`. Las 20 preguntas en español tienen `¿` y `?`.
- Las columnas están en orden español; inglés. La revisión de los pares no encontró inversiones ni discrepancias de sentido que requieran observación.
- Los diez focos de PF-A1-001 están cubiertos en bloques de 15 frases cada uno (filas 1–150); las frases son independientes y el vocabulario se practica con distintos sujetos/contextos y longitudes crecientes en general.
- Regresión del informe previo de iteración 4: la fila 4 ahora dice «Mi inglés mejora con la práctica.» y la fila 53 conserva una redacción correcta; esas observaciones previas están resueltas. Las filas 78, 84 y 89 siguen pendientes de una solución que respete también el límite gramatical A1.

## Sesiones completadas para omitir en la siguiente validación

**Ninguna sesión está completa todavía.** PF-A1-001 cumple el formato y el mínimo de 150, pero requiere las tres correcciones gramaticales indicadas. PF-A1-002 a PF-A1-009 están ausentes y deben validarse cuando se generen.
