# Plan complementario de expresiones por sesión — iteración 2

## Alcance, prioridad y fuente fijada

Este bloque convierte las entradas de `resources/Phrase List.txt` en objetivos para CSV, sin generar esos CSV aquí. Para esta iteración, la instrucción específica prevalece sobre cualquier pauta general incompatible: **no se repite ninguna expresión objetivo ni frase dentro de una sesión o entre sesiones, y no se programan repasos**. No se aplica una cuota de 150 líneas. Cada expresión fuente asignada genera exactamente una fila objetivo en su único CSV; no se añaden variantes ni líneas de relleno.

Fuente congelada para esta asignación:

- Ruta: `resources/Phrase List.txt`.
- Versión de referencia: **snapshot de 2026-10-27**.
- Huella SHA-256: `1372473C7CD5CBD6A6A6FA30A7ACC63723562FDFA4D182362BC25B31987C8756`.
- Alcance: 750 registros; A1 129, A2 379, B1 155, B2 57 y C1 30. La fuente no contiene C2.
- Clave estable de registro: `PH-{nivel}-{ordinal de tres dígitos}`. El ordinal es la posición de la entrada con ese nivel CEFR al recorrer la fuente, comenzando en 001. La forma inglesa fuente es el texto anterior a la etiqueta `CEFR`; se conserva exactamente para cotejo, sin normalizar mayúsculas, puntuación, elipsis ni marcadores.

El manifiesto de asignación es el conjunto de rangos de ID indicados en las tablas: cada ID dentro de un rango es un registro individual del manifiesto, con nivel, ordinal estable, sesión asignada y referencia exacta a la entrada correspondiente de la fuente fijada. Para materializar o auditar un registro, se busca su ordinal entre las entradas que llevan la etiqueta CEFR indicada; la huella evita que una reordenación o cambio de fuente altere silenciosamente esa referencia. Los rangos son inclusivos, disjuntos y particionan todos los ordinales de cada nivel.

## Relación con el plan base y orden de uso

El plan base es `loops_plan/1_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, con progresión A1–C2. Este documento es un **bloque complementario separado**, no reemplaza ni modifica el plan base. Se estudia después de completar las sesiones base del nivel correspondiente y antes de empezar el nivel siguiente; para C1, después de C1 base. Los CSV de este bloque contienen únicamente las expresiones asignadas aquí.

El plan base excluye el material de esta lista para incorporarlo por separado. La regla de no duplicación es comparar la forma inglesa objetivo exacta (incluidos marcadores y puntuación) y su ID de fuente: cada registro pertenece solo a una fila de este manifiesto y a un CSV. No se reutiliza como objetivo en el plan base, en otra sesión ni como línea adicional de contexto. Antes de producir los CSV se coteja que el plan base no haya asignado ninguna de estas entradas como objetivo; si apareciera una coincidencia, se conserva una sola asignación canónica y se corrige el plan de producción antes de exportar, sin duplicar la frase.

El programa general conserva su cobertura C2 mediante las sesiones y objetivos C2 propios del plan base. Esta fuente no aporta expresiones C2: no se crea una sesión de frases C2, no se elevan expresiones C1 a C2 ni se inventan entradas para cubrir el vacío.

## Secuencia de sesiones

Las tandas pequeñas respetan el orden y la identidad de la fuente, permiten generar una sola línea por objetivo y evitan forzar un CSV extenso con repeticiones. Los subobjetivos orientan la escena y la selección de referentes: cada línea debe sonar autónoma y mostrar la expresión asignada, no acumular objetivos distintos en una sola frase. La gramática indicada es el marco de producción pertinente a las formas del bloque; si una expresión necesita otro patrón para conservar su sentido, se usa su marco fuente sin añadir una estructura como objetivo nuevo.

### A1 — Expresiones inmediatas y concretas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| A1-S01 | Expresar cantidad, grado, capacidad y duración con enunciados breves. Subobjetivos: indicar cuánto/algo más y describir una capacidad o una referencia temporal sencilla. | PH-A1-001–026 (26 registros; fuente exacta por ID). | Cuantificadores y grupos nominales; `a bit/a lot`; `able to + infinitivo`; expresiones temporales. | Ninguno; no se programan repasos. |
| A1-S02 | Hablar de frecuencia, rutina y estados cotidianos; dar una respuesta social breve. Subobjetivos: decir cuándo ocurre algo y describir una situación personal sencilla. | PH-A1-027–052 (26 registros; fuente exacta por ID). | Presente simple; adverbiales de frecuencia y tiempo; `be` en presente; imperativos o fórmulas conversacionales cuando corresponda. | Ninguno; no se programan repasos. |
| A1-S03 | Comunicar bienestar, relaciones, preferencias y ubicación inmediata. Subobjetivos: preguntar/contestar con cortesía y situar una actividad o persona. | PH-A1-053–078 (26 registros; fuente exacta por ID). | Preguntas breves; pronombres y posesivos; `be`, `have` y preposiciones de lugar según la entrada. | Ninguno; no se programan repasos. |
| A1-S04 | Resolver intercambios sencillos en espacios públicos y por teléfono. Subobjetivos: identificar lugares, objetos o contactos y coordinar una acción inmediata. | PH-A1-079–104 (26 registros; fuente exacta por ID). | `there is/are`; imperativos; preposiciones de lugar; peticiones y respuestas corteses. | Ninguno; no se programan repasos. |
| A1-S05 | Expresar acciones, necesidades y cierres sociales de la vida diaria. Subobjetivos: pedir, ofrecer, relatar una acción breve o despedirse. | PH-A1-105–129 (25 registros; fuente exacta por ID). | Presente simple; `would like`; infinitivos y complementos; fórmulas afirmativas, negativas e interrogativas breves. | Ninguno; no se programan repasos. |

### A2 — Interacción cotidiana ampliada

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| A2-S01 | Describir tipos, cantidades, opciones y relaciones entre elementos. Subobjetivos: especificar una cantidad, categoría o alternativa en una situación concreta. | PH-A2-001–025 (25 registros; fuente exacta por ID). | Cuantificadores y determinantes; complementos nominales; `of`, `to` y patrones de comparación simples. | Ninguno; no se programan repasos. |
| A2-S02 | Solicitar, ubicar y describir estados, acceso o características de personas y cosas. Subobjetivos: formular una petición y añadir una condición o atributo. | PH-A2-026–050 (25 registros; fuente exacta por ID). | Infinitivo/gerundio tras verbo o preposición; `be + participio/adjetivo`; preguntas corteses. | Ninguno; no se programan repasos. |
| A2-S03 | Expresar relaciones personales, preferencias, obligaciones y cambios cotidianos. Subobjetivos: describir una relación o explicar qué se puede o debe hacer. | PH-A2-051–075 (25 registros; fuente exacta por ID). | Verbos de estado y patrones verbo + complemento; modales de obligación; pasado simple si lo exige el contexto. | Ninguno; no se programan repasos. |
| A2-S04 | Hablar de acciones, desplazamientos y organización práctica. Subobjetivos: indicar una acción concreta, su dirección o su resultado inmediato. | PH-A2-076–100 (25 registros; fuente exacta por ID). | Verbos con partícula y objeto; imperativos; presente/pasado simple; complementos de lugar. | Ninguno; no se programan repasos. |
| A2-S05 | Explicar causas, dificultades y respuestas en situaciones habituales. Subobjetivos: presentar un problema y una razón o reacción comprensible. | PH-A2-101–125 (25 registros; fuente exacta por ID). | `because`, `so`, `when`; adjetivos con complemento; preguntas y respuestas breves. | Ninguno; no se programan repasos. |
| A2-S06 | Describir experiencias, avances y límites en la vida diaria. Subobjetivos: expresar lo que se logra, cambia o resulta posible. | PH-A2-126–150 (25 registros; fuente exacta por ID). | Infinitivo y gerundio; pasado simple; presente perfecto solo cuando la expresión lo requiera. | Ninguno; no se programan repasos. |
| A2-S07 | Comunicar sentimientos, opiniones y expectativas en relaciones cercanas. Subobjetivos: decir qué se piensa, se siente o se espera con un motivo breve. | PH-A2-151–175 (25 registros; fuente exacta por ID). | `think/feel + complemento`; subordinación con `that/if`; adjetivos y preposiciones regidas. | Ninguno; no se programan repasos. |
| A2-S08 | Hablar de educación, personas y circunstancias; plantear preguntas y expresar opinión, necesidad o condición. Subobjetivos: pedir datos y describir una situación de estudio o convivencia. | PH-A2-176–200 (25 registros; fuente exacta por ID). | Preguntas con palabras interrogativas; pronombres; subordinación con `if/that`; expresiones de tiempo y lugar según cada entrada. | Ninguno; no se programan repasos. |
| A2-S09 | Describir lugares, posiciones y circunstancias de una actividad. Subobjetivos: localizar personas o cosas y especificar condiciones. | PH-A2-201–225 (25 registros; fuente exacta por ID). | Preposiciones y locuciones de lugar; `there is/are`; grupos nominales y complementos. | Ninguno; no se programan repasos. |
| A2-S10 | Explicar secuencias, propósitos y decisiones cotidianas. Subobjetivos: decir qué se hace, para qué y en qué orden. | PH-A2-226–250 (25 registros; fuente exacta por ID). | `to + infinitivo` de propósito; conectores de secuencia; patrones verbo + preposición. | Ninguno; no se programan repasos. |
| A2-S11 | Describir grados, emociones, salud y situaciones sociales; expresar reacción o limitación. Subobjetivos: valorar una circunstancia y decir qué se desea, necesita o rechaza. | PH-A2-251–275 (25 registros; fuente exacta por ID). | Cuantificadores y gradación; negación; modales y complementos verbales según la construcción asignada. | Ninguno; no se programan repasos. |
| A2-S12 | Comparar personas, cantidades y situaciones; comunicar semejanzas o diferencias. Subobjetivos: elegir entre opciones con una razón sencilla. | PH-A2-276–300 (25 registros; fuente exacta por ID). | Comparativos; cuantificadores; `as…as`; cláusulas de razón y contraste. | Ninguno; no se programan repasos. |
| A2-S13 | Resumir hechos y describir qué ocurre en distintos contextos sociales. Subobjetivos: identificar un tema o resultado y añadir una precisión relevante. | PH-A2-301–325 (25 registros; fuente exacta por ID). | Presente simple; pasiva básica; referencias anafóricas; conectores de adición. | Ninguno; no se programan repasos. |
| A2-S14 | Hablar de movimientos, resultados y respuestas ante una situación. Subobjetivos: relatar un cambio breve o explicar qué sigue. | PH-A2-326–350 (25 registros; fuente exacta por ID). | Verbos con partícula; pasado simple; secuencia temporal y resultado. | Ninguno; no se programan repasos. |
| A2-S15 | Cerrar intercambios y expresar elecciones, disponibilidad o reacción. Subobjetivos: responder, aceptar/rechazar y añadir una preferencia concreta. | PH-A2-351–379 (29 registros; fuente exacta por ID). | Preguntas y respuestas breves; `would`; modales; orden de adverbios y complementos. | Ninguno; no se programan repasos. |

### B1 — Comunicación independiente

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| B1-S01 | Explicar cambios, cantidades y relaciones en un relato o proceso cotidiano. Subobjetivos: presentar una circunstancia y describir su evolución. | PH-B1-001–026 (26 registros; fuente exacta por ID). | Complementación verbal; conectores temporales; voz pasiva y estructuras de resultado. | Ninguno; no se programan repasos. |
| B1-S02 | Describir procedimientos, decisiones y consecuencias con una secuencia clara. Subobjetivos: explicar qué se hizo y qué ocurrió después. | PH-B1-027–052 (26 registros; fuente exacta por ID). | Verbos con partícula; pasado simple; infinitivo/gerundio; causa y consecuencia. | Ninguno; no se programan repasos. |
| B1-S03 | Expresar experiencias, objetivos y condiciones personales. Subobjetivos: narrar un hecho y precisar intención, límite o condición. | PH-B1-053–078 (26 registros; fuente exacta por ID). | Pasado y presente perfecto según el marcador; condicionales; `to + infinitivo`. | Ninguno; no se programan repasos. |
| B1-S04 | Expresar una postura y explicar condiciones, relaciones o razones relevantes. Subobjetivos: plantear una posibilidad, aclarar una idea y justificar su alcance. | PH-B1-079–104 (26 registros; fuente exacta por ID). | Concesión y condición cuando correspondan; complementos preposicionales; subordinación y conectores discursivos. | Ninguno; no se programan repasos. |
| B1-S05 | Describir procesos, responsabilidades y resultados en ámbitos cotidianos. Subobjetivos: resumir un proceso y atribuir una acción o consecuencia. | PH-B1-105–130 (26 registros; fuente exacta por ID). | Pasiva; complementos preposicionales; cláusulas relativas y temporales. | Ninguno; no se programan repasos. |
| B1-S06 | Matizar una explicación y concluir con una valoración o posibilidad. Subobjetivos: reformular un punto y señalar su alcance. | PH-B1-131–155 (25 registros; fuente exacta por ID). | Modalidad; subordinación; conectores de conclusión y reformulación. | Ninguno; no se programan repasos. |

### B2 — Precisión y argumentación

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| B2-S01 | Exponer una postura y diferenciar evidencia, opinión y alcance. Subobjetivos: introducir una reserva y especificar el punto de vista. | PH-B2-001–019 (19 registros; fuente exacta por ID). | Concesión; cláusulas de opinión; modales de certeza y matización. | Ninguno; no se programan repasos. |
| B2-S02 | Contrastar alternativas y explicar consecuencias o condiciones. Subobjetivos: sostener una comparación y justificar su resultado. | PH-B2-020–038 (19 registros; fuente exacta por ID). | Condicionales; comparativas; estructuras de resultado y causa. | Ninguno; no se programan repasos. |
| B2-S03 | Evaluar propuestas, participación y resultados con precisión. Subobjetivos: expresar criterios, límites y conclusión. | PH-B2-039–057 (19 registros; fuente exacta por ID). | Infinitivo/gerundio; nominalización básica; pasiva y conectores argumentativos. | Ninguno; no se programan repasos. |

### C1 — Relaciones discursivas avanzadas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| C1-S01 | Atribuir información, explicar marcos de análisis y delimitar afirmaciones. Subobjetivos: identificar fuente, criterio o contexto sin sobreafirmar. | PH-C1-001–015 (15 registros; fuente exacta por ID). | Pasiva y atribución; nominalización; complementos preposicionales precisos. | Ninguno; no se programan repasos. |
| C1-S02 | Matizar relaciones, excepciones y consecuencias en una exposición formal. Subobjetivos: precisar alcance y enlazar una conclusión con sus condiciones. | PH-C1-016–030 (15 registros; fuente exacta por ID). | Subordinación compleja; concesión; relaciones de causa, marco y excepción; registro formal. | Ninguno; no se programan repasos. |

### C2 — Continuidad del programa general

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| C2 — fuera del bloque de frases | Mantener los objetivos C2 ya definidos por el plan base. Este bloque no crea sesión ni CSV C2 porque la fuente fijada no contiene entradas C2. | Ninguna entrada en `Phrase List.txt`; no inventar ni reasignar expresiones C1. | Según las sesiones C2 del plan base. | Según el calendario de repaso del plan base; no se añaden repasos de esta fuente. |

## Producción de los CSV y aceptación

### Nombre y contenido

- Un archivo por sesión con objetivos: `frases_{ID}_v1.csv` (por ejemplo, `frases_A1-S01_v1.csv`). No se crea CSV para C2 en este bloque.
- Una fila por cada ID del rango asignado a la sesión, en orden ordinal; ninguna otra fila. El número de filas es exactamente el número indicado en la tabla: no se busca llegar a 150.
- Dos columnas sin encabezado, `español;inglés`, UTF-8 y un único `;` separador. No añadir ID, nivel, notas ni columnas auxiliares al CSV.
- La columna inglesa realiza la entrada objetivo fuente una vez, resolviendo `sb`, `sth`, `do sth`, `X` o puntos suspensivos con referentes naturales cuando sea necesario. La traducción española debe corresponder al contexto elegido. Registrar fuera del CSV la resolución de cada marcador para auditar el sentido; no pronunciar ni copiar los marcadores literalmente.
- Crear una sola oración oral natural por expresión. No añadir reformulaciones, preguntas-respuestas de relleno, variantes ni ejemplos extra. No usar una misma frase española o inglesa para cubrir objetivos distintos.

### Lista de aceptación por sesión

1. **Cobertura exacta:** cada ID asignado aparece exactamente una vez; el total de filas es igual al total de IDs de la sesión.
2. **Sin ajenos ni duplicados:** ninguna fila representa un objetivo de otra sesión o de fuera de la fuente fijada; no hay expresiones objetivo ni frases duplicadas dentro del CSV ni entre los CSV del bloque.
3. **Formato:** dos campos por fila separados por `;`, UTF-8, sin encabezado y sin delimitadores o saltos de línea que creen campos o registros accidentales.
4. **Equivalencia y naturalidad:** un revisor confirma que el español y el inglés son idiomáticos en contexto y equivalentes en intención y sentido, no traducciones mecánicas.
5. **Marcadores:** cada marcador se resuelve con un referente inequívoco y natural, sin cambiar el significado, el patrón sintáctico o el registro de la entrada; se registra esa resolución para el cotejo.
6. **No duplicación con el plan base:** verificar que la forma inglesa exacta no esté asignada allí como objetivo; la lista fuente solo se produce mediante el ID canónico de este plan.

## Cotejo de cobertura y no repetición

| Nivel | Sesiones y partición de ordinales | Registros |
|---|---|---:|
| A1 | A1-S01 001–026; A1-S02 027–052; A1-S03 053–078; A1-S04 079–104; A1-S05 105–129 | 129/129 |
| A2 | A2-S01 001–025; S02 026–050; S03 051–075; S04 076–100; S05 101–125; S06 126–150; S07 151–175; S08 176–200; S09 201–225; S10 226–250; S11 251–275; S12 276–300; S13 301–325; S14 326–350; S15 351–379 | 379/379 |
| B1 | B1-S01 001–026; B1-S02 027–052; B1-S03 053–078; B1-S04 079–104; B1-S05 105–130; B1-S06 131–155 | 155/155 |
| B2 | B2-S01 001–019; B2-S02 020–038; B2-S03 039–057 | 57/57 |
| C1 | C1-S01 001–015; C1-S02 016–030 | 30/30 |
| C2 | No hay entradas en la fuente; continuidad mediante el plan base | 0 en este bloque |
| **Total fuente** | **31 sesiones con objetivos; rangos sin solapamiento dentro de cada nivel** | **750/750** |

El volumen de cada CSV queda fijado por sus objetivos únicos, no por una cuota. El campo «Vocabulario en repaso» se mantiene en «Ninguno» en todas las sesiones del bloque, conforme a la prohibición de repetir o repasar las entradas de la lista.
