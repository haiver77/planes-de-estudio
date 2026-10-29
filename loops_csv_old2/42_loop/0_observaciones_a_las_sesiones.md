# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración auditada:** `loops_csv/41_loop/A1/`  
**Plan aprobado:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo cotejado:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Referencias adicionales:** `indicaciones_csv.md`, `contexto.md` e informes de `loops_csv/33_loop/` a `loops_csv/41_loop/`.  
**Alcance:** exclusivamente los cinco CSV A1-S001 a A1-S005.

## Comprobaciones

- La carpeta del nivel contiene exactamente `A1-S001.csv`, `A1-S002.csv`, `A1-S003.csv`, `A1-S004.csv` y `A1-S005.csv`: no hay ID faltante ni CSV ajeno dentro del alcance.
- Se leyeron los bytes y se validaron con UTF-8 estricto y análisis CSV estricto. Cada archivo tiene **150 líneas físicas y 150 registros** (750 pares en total), sin encabezado; todos satisfacen el mínimo obligatorio explícito de 150.
- Las 750 filas contienen exactamente dos campos no vacíos separados por `;`; no hay filas vacías, campos extra, comas usadas como delimitador, `;` dentro de campos, comillas mal cerradas ni saltos de línea incrustados. Las comas presentes dentro de algunas frases no funcionan como delimitador. No se hallaron columnas invertidas, preguntas españolas sin `¿`, caracteres de reemplazo, mojibake (`Ã...`) ni `?` sustituyendo letras. Los signos diacríticos y de apertura se leen correctamente. No hay duplicados exactos en español o inglés.
- Se cotejaron objetivos y unidades léxicas con el plan y el catálogo, y se revisaron las observaciones históricas contra las filas actuales. Los arreglos de n41 están aplicados: S002-43/61/116, S004-44/70/132 y S005-33 ya no presentan los problemas anotados; S001-59/60 ahora nombra el billete y hace explícito el uso del dinero.
- **S004, comprobación solicitada G04/G03:** el bloque ocupa exactamente las filas **85–114**. Las filas **85–102** son **18 pares G04** en seis series afirmativa/negativa/interrogativa de *present simple* con *do/does*; las filas **103–114** son **12 pares G03** en cuatro series de *have got/has got*. El orden G04→G03 y la cuenta **18 + 12** son correctos.

## Observaciones priorizadas — NO COMPLETO

### Prioridad alta: fidelidad al plan y consistencia del bloque gramatical

1. **`A1-S003.csv`, filas 73–102 — falta el repaso gramatical G02 previsto.** El plan asigna a S003 la introducción de G03 (*have got/has got* y posesivos) y el repaso de G02 (artículos, sustantivos contables, plurales y demostrativos). Sin embargo, las 30 filas 73–102 practican G03; las filas 61–72 son repaso léxico de S002, no una secuencia identificable de G02, y no practican demostrativos. **Cambio requerido:** incorporar en el bloque gramatical el repaso explícito de G02, incluidos los demostrativos y el contraste singular/plural, y mantener la práctica introductoria de G03 dentro del total previsto y en el orden del plan.

2. **`A1-S005.csv`, filas 85–114 — el bloque no evidencia el repaso G04 previsto.** Las 30 filas practican G05 (*there is/are*, *some/any*, *much/many* y *a lot of*). No se reserva en este bloque una secuencia de repaso de G04 (*present simple*, *do/does*, preguntas y negación); las frases de vocabulario de otras secciones no sustituyen ese repaso gramatical explícito. **Cambio requerido:** redistribuir el bloque, manteniendo el total de 30 pares, para incluir el repaso G04 planificado junto con la introducción de G05 y ordenar ambas partes de acuerdo con el plan.

3. **`A1-S004.csv`, fila 104 (secuencia 103–105) — el objeto cambia dentro de la práctica afirmativa/negativa/interrogativa de G03.** La fila 103 afirma que la hermana tiene su propio cuarto (`own room`); la 104 niega que tenga su propio escritorio (`own desk`); la 105 pregunta de nuevo por el cuarto. Aunque la fila 104 se traduce literalmente, la secuencia ya no transforma la misma proposición en afirmativa, negativa e interrogativa. **Cambio requerido:** mantener el mismo objeto en las tres filas (por ejemplo, `cuarto/room`) o reformular las tres para que la negación también se refiera al escritorio.

### Prioridad media: adecuación A1

4. **`A1-S005.csv`, fila 103 — léxico más avanzado de lo necesario para la práctica A1 de *any*.** `¿Hay sillas disponibles en la sala de espera?;Are there any chairs available in the waiting room?` es equivalente, pero *available* añade vocabulario menos básico sin ser necesario para practicar *are there any*. **Cambio requerido:** usar una formulación más simple, por ejemplo `¿Hay sillas libres en la sala?;Are there any free chairs in the room?`.

## Resultado

La cobertura, el mínimo de pares, la codificación y la estructura CSV cumplen; el bloque G04/G03 de S004 también cumple exactamente el orden y la cantidad solicitados. Persisten los incumplimientos gramaticales indicados para S003 y S005, una inconsistencia de secuencia en S004 y una frase de S005 que conviene simplificar para A1. **NO COMPLETO; se requiere otra iteración.**