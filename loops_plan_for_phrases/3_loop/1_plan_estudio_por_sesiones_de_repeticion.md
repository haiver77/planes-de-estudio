# Plan de asignación de expresiones — iteración 3

## Decisión de alcance y resultado de la integración

Esta iteración fija la propiedad de las 750 entradas de `resources/Phrase List.txt`; no genera CSV. El cotejo con los planes disponibles muestra que **las 750 entradas ya tienen una asignación canónica en el plan aprobado de Oxford Phrase List** (`planes_aprobados/oxford_phrase_list/phrase_list.md`), localizable por expresión y sesión en `loops_plan/12_loop/2_catalogo_trazabilidad_fuentes.csv`. Por ello, no se crea un segundo objetivo ni un CSV complementario para ninguna entrada. El destino de cada ID `PH` es el plan base indicado en el registro de cobertura que sigue; no queda ninguna entrada pendiente de un cotejo futuro.

La asignación del catálogo conserva la sesión de introducción de la unidad principal. Cuando el texto de `Phrase List.txt` es una variante de escritura o plantilla de la forma del catálogo, el registro de variantes de este plan resuelve el destino. Si una frase también está trabajada explícitamente en el plan general, prevalece la sesión general indicada en la tabla de propiedad canónica y no se produce esa frase como objetivo en otra sesión base ni en CSV. Las entradas repetidas del catálogo que son repasos no crean una segunda propiedad: por ejemplo, `all over the world` conserva como única introducción `A1-S002`; su aparición posterior en `A2-S001` es solo el repaso ya registrado.

## Fuente y clave de cobertura

- Fuente: `resources/Phrase List.txt`, snapshot consultado el 27-10-2026.
- SHA-256 de los bytes de la fuente: `1372473C7CD5CBD6A6A6FA30A7ACC63723562FDFA4D182362BC25B31987C8756`.
- Total: 750 registros: A1 129, A2 379, B1 155, B2 57, C1 30; no hay entradas C2.
- Clave: `PH-{nivel}-{ordinal de tres dígitos}`. El ordinal es la posición dentro del nivel en la fuente fijada; así se recupera una sola expresión fuente sin depender de un rango temático ni de normalizar el texto.
- Cotejo materializado: 739 formas coinciden literalmente tras normalizar Unicode, mayúsculas/minúsculas y espacios; 11 variantes de puntuación, marcadores o forma se resuelven de modo explícito en la tabla de alias. Las 750 tienen destino base. El catálogo registra para las coincidencias exactas `entrada_normalizada`, `id_unidad_canonica` y `sesion_plan`.

### Regla de identidad y duplicación

Se considera duplicado cuando dos filas futuras tienen la misma expresión objetivo/collocation, incluidos cambios meramente ortográficos o la misma plantilla con marcadores completados; también cuando la misma construcción está explícitamente asignada como objetivo de frase en ambos planes. Se fija una única propiedad canónica y una sola introducción. Una frase que usa gramática relacionada **no** es duplicada por ese solo hecho: la construcción debe aparecer efectivamente como objetivo explícito. No se cuenta como duplicado el uso incidental de una palabra funcional o estructura general que no enseñe el objetivo fuente.

## Propiedad canónica para solapamientos con el plan general

El plan general prevalece para estas entradas porque las asigna expresamente como foco léxico o construcción objetivo. Se excluyen de cualquier objetivo complementario y de cualquier segunda introducción del plan Oxford. Las unidades y el resto de vocabulario de sus sesiones generales no se eliminan.

| ID fuente | Expresión objetivo | Única propiedad canónica | Decisión |
|---|---|---|---|
| PH-A1-009 | `a lot` | Plan general A2-S03: cuantificadores `a lot of/much/many` | Cubierta; no CSV complementario. |
| PH-A1-011 | `a lot of sth` | Plan general A2-S03: cuantificadores `a lot of/much/many` | Misma colocación cuantificadora; no segunda propiedad. |
| PH-A1-056 | `have got` | Plan general A1-S02: `have/has got` | Cubierta como objetivo explícito de gramática; no CSV complementario. |
| PH-A1-114 | `there is` | Plan general A1-S04: `there is/are` | Misma construcción existencial; no CSV complementario. |
| PH-A1-127 | `would like` | Plan general A2-S03: `prefer/would like` | Cubierta; no CSV complementario. |
| PH-A2-182 | `how many…?` | Plan general A1-S05: preguntas `how many/how much` | Cubierta; no CSV complementario. |
| PH-A2-183 | `how much…?` | Plan general A1-S05: preguntas `how many/how much` | Cubierta; no CSV complementario. |
| PH-A2-264 | `not only` | Plan general C1-S06: inversión enfática `not only… but also` | Misma colocación; no CSV complementario. |
| PH-A2-289 | `ought to` | Plan general C1-S02: modalidad de recomendación/obligación `ought to` | Cubierta; no CSV complementario. |
| PH-A2-372 | `would you like…?` | Plan general A2-S04: invitaciones y ofrecimientos con `would you like to` | Misma fórmula de invitación; no CSV complementario. |

### Casos cercanos que no se declaran duplicados por gramática general

- PH-A2-371 `would rather` no se absorbe por el mero hecho de que B2-S04 trate `would + verbo base`: el plan general no asigna explícitamente la colocación `would rather` como objetivo.
- PH-B1-007 `as long as…` no se absorbe por el foco general de primer condicional/`unless`: no es la misma expresión objetivo.
- PH-A2-235 `instead of` no se absorbe por un foco general de contraste sin asignación explícita de esa colocación.
- La coincidencia contextual de un sustantivo, verbo o marcador no equivale por sí misma a duplicar el objetivo fuente.

Estos casos permanecen bajo la propiedad única del plan aprobado de Oxford Phrase List, identificada por el cotejo del catálogo; no se convierten en CSV de este bloque.

## Cobertura íntegra por nivel

En cada tabla, los IDs PH se resuelven individualmente contra la fuente fija por su nivel y ordinal. El destino base de cada uno es la sesión que figura en `sesion_plan` para la forma exacta del catálogo, con los alias explícitos descritos más abajo. Estas filas declaran propiedad de cobertura; no son nuevas sesiones ni autorizan generar CSV. No hay repasos ni asignaciones de vocabulario complementario.

### A1 — 129/129 entradas cubiertas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| A1 — base | Mantener intercambios inmediatos y cotidianos en las escenas específicas de las sesiones base. | PH-A1-001–129; sesión base individual por cotejo fuente→`entrada_normalizada`→`sesion_plan`, excepto las propiedades canónicas generales ya enumeradas. | La de cada sesión base propietaria; este bloque no añade gramática objetivo. | Ninguno añadido; se conserva solo el calendario base. |

### A2 — 379/379 entradas cubiertas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| A2 — base | Resolver interacciones cotidianas, necesidades, decisiones y relaciones según la microescena de la sesión base asignada a cada expresión. | PH-A2-001–379; sesión base individual por cotejo del catálogo, excepto las propiedades canónicas generales ya enumeradas. | La de cada sesión base propietaria; no se reutiliza una construcción como objetivo nuevo aquí. | Ninguno añadido; se conserva solo el calendario base. |

### B1 — 155/155 entradas cubiertas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| B1 — base | Explicar actividades, procesos, experiencias y relaciones según la microescena de la sesión base asignada a cada expresión. | PH-B1-001–155; la forma fuente exacta determina la sesión base propietaria. | La de cada sesión base propietaria. | Ninguno añadido; se conserva solo el calendario base. |

### B2 — 57/57 entradas cubiertas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| B2 — base | Expresar matices, razones, condiciones y valoraciones en la microescena propia de la sesión base. | PH-B2-001–057; la forma fuente exacta determina la sesión base propietaria. | La de cada sesión base propietaria. | Ninguno añadido; se conserva solo el calendario base. |

### C1 — 30/30 entradas cubiertas

| ID | Objetivo Comunicativo | Vocabulario Foco | Gramática foco | Vocabulario en repaso |
|---|---|---|---|---|
| C1 — base | Desarrollar comunicación discursiva y formal en la microescena asignada por el plan base. | PH-C1-001–030; la forma fuente exacta determina la sesión base propietaria. | La de cada sesión base propietaria. | Ninguno añadido; se conserva solo el calendario base. |

La resolución por forma, y no por un tramo alfabético que suponga una escena compartida, conserva la asignación contextual de cada unidad en su sesión base. Al producir material de esas sesiones, cada objetivo se realiza una sola vez, en una oración autónoma que use su sentido y marco naturales; las expresiones heterogéneas no se acumulan en una misma oración ni se fuerza una escena común.

## Alias y variantes que completan la trazabilidad

Estas 11 formas no coinciden literalmente con la escritura del catálogo tras normalización, pero son variantes de su objetivo y ya tienen una asignación concreta en el plan Oxford. Por ello, tampoco se exportan como objetivos nuevos. La convención de marcadores y los registros de origen del catálogo permiten comprobar cada equivalencia.

| ID fuente | Forma en `Phrase List.txt` | Forma canónica en catálogo | Sesión base única |
|---|---|---|---|
| PH-A2-046 | `as to` | `as to sth` | C1-S001 |
| PH-A2-090 | `can't afford sth` | `can’t afford sth` | B1-S004 |
| PH-A2-131 | `ever since` | `ever since(…)` | B2-S006 |
| PH-B2-013 | `get over sb/sth` | `get over sth/sb` | B2-S006 |
| PH-A2-187 | `i don't care` | `I don’t care` | A2-S010 |
| PH-A2-191 | `i'm afraid…` | `I’m afraid…` | A2-S010 |
| PH-A1-061 | `i'm sorry` | `I’m sorry` | A1-S011 |
| PH-A2-237 | `it takes…` | `It takes…` | A1-S014 |
| PH-B1-139 | `take sth/sb on` | `take sb/sth on` | B1-S017 |
| PH-A1-113 | `that's it` | `That’s it` | B1-S018 |
| PH-A1-129 | `you're welcome` | `You’re welcome` | A1-S026 |

## C2 — continuidad del plan general

`Phrase List.txt` no contiene registros C2. Se conservan las sesiones y objetivos C2 del plan general; este bloque no crea sesiones C2, no eleva expresiones C1 ni inventa frases. Los repasos C2 siguen exclusivamente el calendario del plan general.

## Convención de producción y aceptación

**No se programa ningún CSV complementario de frases.** Para conservar la convención cuando se generen CSV del plan base:

- Nombre: `frases_{ID}_v1.csv`, un archivo por sesión base que tenga objetivos; dos columnas sin encabezado, `español;inglés`, UTF-8 y `;` como separador.
- Solo se incluyen los objetivos de esa sesión base y cada objetivo se produce una vez; no se agregan filas de relleno, variantes ni repasos de estas 750 entradas.
- Antes de exportar, se resuelven los marcadores `sb`, `sth`, `do sth`, `X` y puntos suspensivos con referentes naturales; se registra la resolución fuera del CSV.
- Aceptación: cobertura exacta de objetivos asignados, sin ajenos, omisiones o repeticiones; formato correcto; pares idiomáticos y equivalentes en sentido e intención; una sola frase autónoma por objetivo.
- **Equivalencia de sujeto/pronombres:** comprobar explícitamente que sujeto y referentes sean inequívocos y coincidan en inglés y español. Incluir el pronombre explícito en español cuando omitirlo pudiera volver ambiguo quién actúa (por ejemplo, él/ella/ellos), conforme a `indicaciones_csv.md`.
- **No duplicación:** comparar expresión objetivo/collocation y construcción focal efectivamente asignada, no la mera presencia de gramática relacionada. Aplicar las propiedades canónicas de esta iteración y no duplicar entre sesiones base ni en un CSV complementario.
- **Volumen:** no se fija cuota de 150 filas. No crear pares adicionales para alcanzar una cantidad.

## Verificación de cobertura

| Nivel | Registros fuente | Propiedad en plan base | CSV complementario | C2 |
|---|---:|---|---:|---|
| A1 | 129 | 129/129; destino de cada ID recuperable por expresión y sesión base | 0 | — |
| A2 | 379 | 379/379; destino de cada ID recuperable por expresión y sesión base | 0 | — |
| B1 | 155 | 155/155; destino de cada ID recuperable por expresión y sesión base | 0 | — |
| B2 | 57 | 57/57; destino de cada ID recuperable por expresión y sesión base | 0 | — |
| C1 | 30 | 30/30; destino de cada ID recuperable por expresión y sesión base | 0 | — |
| **Total** | **750** | **750/750** | **0** | **Conservado en el plan general** |

La observación de reorganizar las expresiones en nuevos grupos complementarios no se aplica como una reasignación aquí: el cotejo resolvió que las 750 entradas ya tienen una sesión propietaria en los planes base, así que moverlas a nuevas sesiones o a CSV complementarios volvería a asignar objetivos existentes. Se conserva la microescena y el destino por expresión del plan Oxford propietario; C2 permanece exclusivamente en el plan general.
