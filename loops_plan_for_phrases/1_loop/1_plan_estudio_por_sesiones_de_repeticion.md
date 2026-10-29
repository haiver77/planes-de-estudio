# Plan de estudio oral por sesiones — Phrase List (iteración 1)

## Alcance e identificación del vocabulario

- La fuente complementaria es `resources/Phrase List.txt`. Contiene 750 expresiones con nivel CEFR: 129 A1, 379 A2, 155 B1, 57 B2 y 30 C1. No contiene entradas C2.
- Los códigos `PH-A2-001`, `PH-B1-023`, etc. identifican la expresión del nivel indicado por su orden de aparición entre las líneas que llevan esa etiqueta `CEFR` en la fuente. La numeración comienza en 001 para cada nivel. Los rangos de las tablas son inclusivos y cubren cada entrada una sola vez. La expresión inglesa de la fuente es la forma objetivo; completa `sb`, `sth`, `do sth`, `X` o puntos suspensivos con referentes naturales, sin pronunciar los marcadores literalmente.
- La progresión va de expresiones concretas de uso cotidiano a colocaciones, verbos con partícula y relaciones discursivas más abstractas. Dentro de cada nivel, las expresiones se identifican en el orden de la fuente para asegurar cobertura; cada una se practica en una microescena propia cuando no comparte contexto lógico con las demás.
- El plan comprende ocho sesiones y ocho CSV, uno por sesión. No incluye repasos, recuperación espaciada ni sesiones de revisión. Ninguna expresión objetivo se asigna a más de una sesión. El campo «Vocabulario en repaso» queda explícitamente en «Ninguno».

## A1 — Expresiones inmediatas y concretas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| A1-S01 | Expresar cantidad, disponibilidad, tiempo, ubicación y cortesía en intercambios cotidianos breves. | PH-A1-001–129 (129 expresiones, en orden de la fuente). | Cuantificadores y expresiones de cantidad; grupos nominales; preposiciones y expresiones de lugar/tiempo; pronombres y formas simples de afirmación, negación y pregunta dentro de ejemplos naturales. | Ninguno. |

## A2 — Interacción cotidiana ampliada

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| A2-S01 | Pedir, ofrecer y describir opciones y necesidades en situaciones familiares con expresiones más precisas. | PH-A2-001–127 (127 expresiones, en orden de la fuente). | Patrones de verbo + complemento; infinitivo y gerundio en expresiones frecuentes; cuantificadores y determinantes; preguntas y peticiones corteses. | Ninguno. |
| A2-S02 | Explicar relaciones, cambios, obligaciones y resultados sencillos en contextos cotidianos. | PH-A2-128–253 (126 expresiones, en orden de la fuente). | Verbos con partícula; pasiva y formas con *be*; causa, contraste y secuencia; obligación, permiso y necesidad en estructuras breves. | Ninguno. |
| A2-S03 | Comunicar experiencias, preferencias y situaciones prácticas enlazando una idea con su razón o consecuencia. | PH-A2-254–379 (126 expresiones, en orden de la fuente). | Comparación; subordinación temporal y condicional básica; patrones de verbo + preposición; conectores de causa, propósito y resultado. | Ninguno. |

## B1 — Comunicación independiente y matizada

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| B1-S01 | Relatar y explicar situaciones, procesos y decisiones con expresiones precisas de nivel intermedio. | PH-B1-001–078 (78 expresiones, en orden de la fuente). | Verbos con partícula y complementación; cláusulas temporales y causales; contraste entre acciones, estados y resultados. | Ninguno. |
| B1-S02 | Plantear posibilidades, contrastar puntos de vista y justificar una conclusión en intercambios autónomos. | PH-B1-079–155 (77 expresiones, en orden de la fuente). | Condicionales; concesión y contraste; estilo indirecto introductorio; conectores para desarrollar y cerrar una explicación. | Ninguno. |

## B2 — Precisión y argumentación

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| B2-S01 | Presentar una postura, ponderar evidencia y expresar condiciones, consecuencias o reservas con precisión. | PH-B2-001–057 (57 expresiones, en orden de la fuente). | Subordinación concesiva y condicional; estructuras de resultado; modales para expresar grado de certeza; énfasis y matización en el orden de la oración. | Ninguno. |

## C1 — Expresión idiomática y relaciones discursivas avanzadas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| C1-S01 | Atribuir, delimitar y matizar afirmaciones complejas en un registro adecuado y natural. | PH-C1-001–030 (30 expresiones, en orden de la fuente). | Atribución y modalidad epistémica; subordinación y nominalización; construcciones pasivas; precisión de complementos y registro. | Ninguno. |

## C2 — Límite de cobertura de la fuente

`Phrase List.txt` no asigna expresiones al nivel C2. Por tanto, esta iteración no inventa vocabulario, no etiqueta expresiones C1 como C2 y no añade una sesión C2 sin material objetivo verificable. Para planificar C2 hará falta una fuente con expresiones o criterios de ese nivel; no se reutilizarán expresiones de sesiones anteriores como supuesto sustituto.

## Producción de los CSV

1. Crear un CSV por cada ID de sesión, con aproximadamente 150 líneas. Cada línea es un par natural español-inglés, separado por un único punto y coma (`español;English`), codificado en UTF-8 y sin encabezado. Mantener el sentido de la expresión inglesa objetivo, no una traducción palabra por palabra.
2. Incluir al menos una línea que enseñe cada expresión del rango asignado a esa sesión. Completar el volumen con variantes y contextos adicionales de esas mismas expresiones, sin incorporar expresiones objetivo de otra sesión ni convertir las líneas adicionales en un plan de repaso. Volumen orientativo exacto para llegar a 150 líneas: A1-S01 129 líneas objetivo + 21 ejemplos adicionales; A2-S01 127 + 23; A2-S02 y A2-S03 126 + 24 cada una; B1-S01 78 + 72; B1-S02 77 + 73; B2-S01 57 + 93; C1-S01 30 + 120.
3. Las líneas adicionales deben desarrollar las expresiones foco con cambios naturales de sujeto, número, tiempo, polaridad, pregunta/respuesta, cortesía o complemento, según la estructura que enseñe la sesión. No añadir frases de relleno: cada línea debe enseñar el uso de una expresión o practicar su patrón gramatical.
4. Construir microescenas breves y lógicamente coherentes. No combinar expresiones solo porque estén próximas en la lista. Si una plantilla de la fuente requiere completar un referente, especificarlo de forma inequívoca. Escribir explícitamente el sujeto en español cuando el inglés exija distinguir pronombres como *he/she/they*. Comprobar equivalencia de sentido, naturalidad oral y concordancia antes de exportar.
5. Mantener una expresión como objetivo de su única sesión asignada. La práctica adicional ocurre dentro de ese mismo CSV y no se programa como repetición espaciada ni como sesión posterior de recuperación.

## Cotejo de cobertura

- A1: 129/129 expresiones asignadas a A1-S01.
- A2: 127 + 126 + 126 = 379/379 expresiones asignadas a A2-S01–A2-S03.
- B1: 78 + 77 = 155/155 expresiones asignadas a B1-S01–B1-S02.
- B2: 57/57 expresiones asignadas a B2-S01.
- C1: 30/30 expresiones asignadas a C1-S01.
- Total de la fuente asignado: 750/750 entradas A1–C1; C2 queda señalado como carencia de fuente, no como una sesión de revisión.
