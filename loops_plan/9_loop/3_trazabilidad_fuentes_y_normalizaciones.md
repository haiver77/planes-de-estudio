# Trazabilidad de cobertura y normalización — Iteración 9

## Alcance

Se parte únicamente de los artefactos de `8_loop`; esta iteración crea los artefactos bajo `9_loop` y no reescribe iteraciones anteriores. Se conservan las 265 sesiones, la cobertura de 2014 registros Oxford 5000 y todos los destinos de repaso léxico/gramatical C2. Esta trazabilidad documenta evidencia y transformaciones; no constituye una declaración de completitud ni una revisión independiente del plan.

## Reconciliación visual del Oxford Phrase List

**Fuente:** `resources/Oxford Phrase List.pdf`, 4 páginas. Se inspeccionó visualmente la página 1 en alta resolución: el prefacio declara “a list of 750 common phrases”; la lista muestra entradas principales en MyriadPro-Regular oscuro y líneas subordinadas indentadas en MyriadPro-Light. La jerarquía de estilos se cotejó en las cuatro páginas y sus registros se enlazaron por texto/página a las filas `OPL-*` del catálogo.

| Nivel impreso | Entrada principal (Regular, sin sangría) | Subentrada/apoyo (Light, sangría) | Registros completos | Unidades únicas |
|---|---:|---:|---:|---:|
| A1 | 200 | 103 | 303 | 303 |
| A2 | 175 | 52 | 227 | 226 |
| B1 | 175 | 57 | 232 | 232 |
| B2 | 125 | 23 | 148 | 148 |
| C1 | 75 | 14 | 89 | 89 |
| **Total** | **750** | **249** | **999** | **998** |

**Regla de conteo reproducible:** un registro fuente del catálogo equivale a una entrada lógica completa delimitada por su página y línea(s). La categoría visual se determina por la tipografía de la primera línea de la entrada en la página PDF: `MyriadPro-Regular` = principal; `MyriadPro-Light` más sangría = subordinada/apoyo. La suma visible por nivel es 750/249/999. De las 249 subordinadas, 36 terminan en puntuación terminal: 27 `.`, 6 `?`, 3 `!` (contando dos elementos terminados en `etc.`); se informa como proxy tipográfico y no como una partición semántica rígida. El documento no marca subtipos semánticos de modo consistente, así que variantes, ejemplos y expansiones se mantienen bajo la categoría reproducible “subentrada/apoyo”. Traducciones al español: 0.

**Líneas, exclusiones y unidades:** el texto extraído contiene 1017 líneas distribuidas en 4 páginas. Se excluyen del contenido léxico 12 líneas editoriales (1 título, 2 del prefacio, 5 encabezados de nivel, 4 pies de página), quedando 1005 líneas de cuerpo. Seis entradas se extienden a una línea física adicional y se unen según página/línea: p. 1, 130–131 (`It is important for sb/sth to do sth`), 166–167 (`What kind of music do you like?`) y 222–223 (entrada anotada más abajo); p. 2, 269–270 (`What sorts of things do you do?`); p. 3, 25–26 (`They say you can’t buy happiness.`) y 46–47 (`I had a kind of feeling this might happen.`). Las seis continuaciones son partes de esos registros, no unidades independientes: 1005−6=999 registros lógicos. Se incluyen las 750 entradas principales y las 249 subentradas/apoyos; todas están asignadas en sesiones. Se conserva un duplicado exacto, `OPL-A2-P02-L086` (`all over the world`), pero enlazado a la unidad original `A1-S002-U07`: el duplicado no crea unidad nueva. No se excluye ningún otro registro del cuerpo de la lista.

### Trazabilidad de continuaciones de línea

| Registro | Fuente, página/líneas | Texto normalizado como una unidad | Sesión / unidad | Repasos +1 / +3 / +6 |
|---|---|---|---|---|
| `OPL-A1-P01-L130` | Phrase List, p. 1, 130–131 | `It is important for sb/sth to do sth` | A1-S011 / A1-S011-U05 | A1-S012 / A1-S014 / A1-S017 |
| `OPL-A1-P01-L166` | Phrase List, p. 1, 166–167 | `What kind of music do you like?` | A1-S014 / A1-S014-U04 | A1-S015 / A1-S017 / A1-S020 |
| `OPL-A1-P01-L222` | Phrase List, p. 1, 222–223 | `What are your plans for next year?` (normalización de errata) | A1-S018 / A1-S018-U11 | A1-S019 / A1-S021 / A1-S024 |
| `OPL-A2-P02-L269` | Phrase List, p. 2, 269–270 | `What sorts of things do you do?` | A2-S016 / A2-S016-U12 | A2-S017 / A2-S019 / B1-S003 |
| `OPL-A2-P03-L025-026` | Phrase List, p. 3, 25–26 | `They say you can’t buy happiness.` | A2-S019 / A2-S019-U01 | B1-S001 / B1-S003 / B1-S006 |
| `OPL-B1-P03-L046-047` | Phrase List, p. 3, 46–47 | `I had a kind of feeling this might happen.` | B1-S001 / B1-S001-U10 | B1-S002 / B1-S004 / B1-S007 |

La fila `OPL-A1-P01-L222` conserva la lectura cruda distinta en el catálogo; las demás normalizaciones de esta tabla conservan el contenido de la unidad fuente. Los IDs, el calendario de repasos y las asignaciones se mantienen en `2_catalogo_trazabilidad_fuentes.csv`.

## Errata de la página 1

**ID y ubicación:** `OPL-A1-P01-L222`, página 1, líneas extraídas 222–223; A1-S018, `A1-S018-U11`; repasos léxicos ya programados A1-S019 (+1), A1-S021 (+3), A1-S024 (+6).

El cotejo visual del PDF muestra literalmente **“What are you plans for next year?”**. Por tanto, el error no es una sustitución OCR: la propia fuente imprime `you` donde la forma estándar exige `your`. Se conserva sin cambios esa lectura en `entrada_fuente_raw_pypdf`; la unidad normalizada para enseñanza y generación de frases pasa a **“What are your plans for next year?”**, con la anotación explícita en `nota_normalizacion_pedagogica`. En el plan se indica también un par natural de referencia: «¿Cuáles son tus planes para el próximo año?» / “What are your plans for next year?”. No se enseña la errata como modelo.

## Oxford 5000 y preservación

Se preservan íntegros los 2014 registros etiquetados del PDF Oxford 5000 (B2 700; C1 1314), con nivel, página, línea, ID de unidad y los repasos existentes. Las 2014 filas tienen etiquetas gramaticales distintas y no se deduplican entre categorías. Al retirar sufijos de categoría y comparar formas ortográficas se obtienen 1999 grafías distintas; 15 grafías aparecen en dos registros etiquetados: `acid`, `alien`, `bat`, `craft`, `deposit`, `dynamic`, `extract`, `hook`, `intellectual`, `principal`, `spare`, `tackle`, `terminal`, `trace`, `trigger`. El titular editorial dice 2000 palabras adicionales; se documenta como base distinta, sin descartar ninguna de las 2014 filas ni inventar una forma para forzar igualdad. No se atribuyen al documento secciones A1–B1 o C2.

## Continuidad de estudio

Las seis sesiones C2 de integración ya existentes se conservan dentro de C2-S001–C2-S012; se mantienen los repasos gramaticales de C2 en posiciones posteriores +1/+3/+6, en sesiones diferentes, y la recuperación léxica acumulativa. La modificación de `A1-S018-U11` no mueve su sesión, ID ni calendario de repaso. Las demás asignaciones y contenidos del plan se heredan sin cambios estructurales.
