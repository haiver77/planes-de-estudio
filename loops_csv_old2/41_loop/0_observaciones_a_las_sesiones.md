# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración auditada:** `loops_csv/40_loop/A1/`  
**Plan:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Criterios cotejados:** `indicaciones_csv.md`, `contexto.md` e informes de `loops_csv/33_loop/` a `loops_csv/40_loop/`.  
**Alcance:** exclusivamente los cinco CSV solicitados. No se modificaron CSV ni archivos previos.

## Comprobaciones

- Los cinco archivos previstos existen, sin faltantes ni CSV ajenos en el directorio A1 auditado. Se validaron directamente sus bytes con UTF-8 estricto y lectura CSV estricta: **150 registros por archivo** (750 pares en total), sin encabezado, dos campos no vacíos por fila y una línea física por par. Todos cumplen el mínimo explícito de 150.
- No se encontraron separadores de comas, campos extra, filas vacías, comillas mal cerradas, saltos de línea incrustados, `;` dentro de campos, columnas invertidas, preguntas españolas sin `¿`, mojibake ni `�`. No hay duplicados exactos de frases españolas o inglesas.
- Se cotejaron los objetivos y las cohortes de vocabulario con el plan y el catálogo, así como las observaciones pendientes de los ciclos anteriores. Varias correcciones previas sí están aplicadas: entre ellas S002-60 ya no contiene `juntas`, S004-19/20 ya no repite la misma escena, S002-24/25 y S005-66 se reformularon, y se resolvieron las filas previamente señaladas de S004-145/150.
- **Comprobación específica S004:** el bloque gramatical ocupa exactamente las filas **85–114 (30 pares)**. Las filas **85–102** contienen **18 prácticas G04** (seis series de afirmativa, negativa e interrogativa de *present simple/do/does*). Las filas **103–114** contienen **12 repasos G03** (cuatro series de afirmativa, negativa e interrogativa de *have got/has got*, con posesivos congruentes: *her, his, our, your*). La ubicación, el orden y las cantidades están correctos; no se observa omisión de esas prácticas.

## Observaciones — NO COMPLETO

### Prioridad alta: equivalencia y naturalidad

1. **`A1-S001.csv`, filas 59–60 — seguimiento de la observación pendiente del informe 40; progresión y propósito aún poco claros.**  
   La fila 59 dice `Tengo un poco de dinero en el bolsillo para el autobús.;I have a little money in my pocket for the bus.` La fila 60 repite la idea de llevar dinero en el bolsillo: `El billete del autobús cuesta dos libras, así que llevo un poco de dinero en el bolsillo.;The bus ticket costs two pounds, so I have a little money in my pocket.` La segunda frase añade el precio, pero la relación causal suena forzada y no expresa claramente que el dinero es para pagar el billete; el bloque no progresa de forma suficientemente natural. **Cambio requerido:** reordenar y aclarar el uso del dinero, nombrando explícitamente el billete en la relación de finalidad, y hacer que la fila 60 amplíe la 59 sin limitarse a repetir “dinero en el bolsillo”.

2. **`A1-S004.csv`, fila 44 — información de género no equivalente.**  
   `Mi mejor amiga y yo estudiamos juntas para el examen de ciencias.;My best friend and I study together for the science test.` El español marca explícitamente como femenino al grupo mediante `juntas`; el inglés no determina el género de quien habla. **Cambio requerido:** reformular el español sin imponer el género del hablante y mantener en ambas columnas la idea de que estudian juntas (por ejemplo, indicar que estudian en la misma mesa).

3. **`A1-S005.csv`, fila 33 — colocación poco idiomática.**  
   `El horario temprano es difícil para mi hermano.;The early schedule is difficult for my brother.` `Early schedule` no es una colocación natural en inglés y `horario temprano` también resulta poco idiomático en este contexto. **Cambio requerido:** expresar la idea con una acción cotidiana, por ejemplo `Empezar temprano es difícil para mi hermano.;It is difficult for my brother to start early.`

4. **`A1-S004.csv`, fila 132 — pregunta inglesa poco natural y significado incompleto.**  
   `¿Tu teléfono móvil tiene carga?;Does your mobile phone have any charge?` La intención es preguntar si queda carga, pero `have any charge` suena incompleto sin indicar que se trata de carga restante. **Cambio requerido:** expresar explícitamente la carga que queda en ambas columnas, por ejemplo `¿Le queda batería a tu teléfono móvil?;Does your mobile phone have any charge left?`

### Prioridad media: nivel A1 y adecuación léxica

5. **`A1-S002.csv`, filas 43, 61 y 116 — léxico innecesariamente avanzado para las frases de recuperación/integración.**
   - **Fila 43:** `¿A alguien más le resulta familiar la dirección del hotel?;Is the hotel address familiar to anyone else?` `familiar` y la construcción resultan más complejos que lo necesario para practicar `anyone else`. **Cambio requerido:** usar una pregunta más directa, como `¿Alguien más conoce la dirección del hotel?;Does anyone else know the hotel address?`
   - **Fila 61:** `Todavía quedan unas cuantas entradas para la función.;A few tickets are still available for the show.` `available` añade una palabra menos básica sin ser necesaria para practicar `a few`. **Cambio requerido:** simplificar, por ejemplo `Todavía quedan unas cuantas entradas para la función.;There are still a few tickets for the show.`
   - **Fila 116:** `La biblioteca renueva sus estanterías cada pocos años.;The library replaces its shelves every few years.` La renovación de estanterías y `replaces its shelves` cargan la frase con vocabulario y una situación poco inmediata para A1. **Cambio requerido:** conservar `every few years` con un objeto o actividad cotidiana y palabras más frecuentes.

6. **`A1-S004.csv`, fila 70 — contexto de repaso menos cotidiano y léxico por encima de lo necesario.**  
   `Los voluntarios limpian la playa el fin de semana después de las tormentas.;The volunteers clean the beach at the weekend after storms.` La acción es comprensible, pero `voluntarios/volunteers` y la referencia a tormentas no son necesarios para recuperar `at the weekend` y hacen menos inmediata la escena A1. **Cambio requerido:** mantener el marco de fin de semana en una actividad familiar con vocabulario frecuente.

## Resultado

La cobertura de archivos, cantidad, formato y codificación cumple. El bloque G04/G03 de S004 también cumple exactamente las cantidades y posiciones comprobadas. Persisten, sin embargo, observaciones de equivalencia, naturalidad y adecuación A1 que requieren corrección y otra iteración. **NO COMPLETO; se requiere iteración 42.**
