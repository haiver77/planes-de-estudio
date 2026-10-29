# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración 19

**Resultado: requiere correcciones; se necesita otra iteración global.**

## Alcance y referencias

Se auditaron exclusivamente `A1-S001.csv` a `A1-S005.csv` de `loops_csv/19_loop/A1/`, fila por fila. Se cotejaron `indicaciones_csv.md`, el plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv` y las observaciones históricas aplicables, incluida la revisión de `loops_csv/19_loop/0_observaciones_a_las_sesiones.md`. No se revisaron otros CSV del nivel ni `loops_csv_old`.

## Evidencia técnica, cantidades y distribución

- En la carpeta están exactamente los cinco archivos solicitados: `A1-S001.csv` a `A1-S005.csv`; no faltan IDs ni hay CSV ajenos al alcance.
- Se leyeron los bytes reales con decodificación UTF-8 estricta y parser CSV estricto. Los cinco archivos son UTF-8 válido, sin BOM, sin secuencias de mojibake ni U+FFFD. Tamaños: S001 12 984 bytes; S002 13 609; S003 12 784; S004 14 167; S005 13 815.
- Cada archivo contiene exactamente 150 líneas físicas y 150 registros CSV válidos. Cada fila tiene dos campos no vacíos, español primero e inglés después, sin encabezado y separados por un solo `;`. No se encontraron filas vacías, campos adicionales, comillas mal cerradas, saltos incrustados, delimitadores alternativos ni `;` dentro de frases. Las preguntas españolas llevan `¿` y `?`; no se detectó `?` sustituyendo letras.
- No hay pares duplicados literalmente entre los cinco archivos. Sí hay una repetición contextual casi equivalente en S004-124/125, indicada abajo.
- El recuento satisface el mínimo explícito: 150 pares en cada archivo, 750 en total. La distribución coincide con el plan: S001 = 60 nuevos + 0 repaso programado + 30 G01 + 60 integración; S002 y S003 = 60 nuevos + 12 repaso + 30 gramática + 48 integración; S004 y S005 = 60 nuevos + 24 repaso + 30 gramática + 36 integración.
- Se cotejaron los bloques de gramática asignados G01–G05: S001-61–90, S002-73–102, S003-73–102, S004-85–114 y S005-85–114. No aparece `will` en los archivos revisados. No se detectó adelanto de una estructura gramatical posterior en esos bloques; los defectos restantes son de cobertura léxica, repetición, equivalencia/naturalidad y selección de contexto.
- Los eventos de repaso ocupan las posiciones previstas y contienen 12 filas por evento. Sin embargo, dos eventos sustituyen el referente explícito de la unidad S002-U01 (`a little sugar`) por otras colocaciones con `a little`; el recuento posicional 12/12 no basta para considerar recuperada esa unidad específica.

## Observaciones históricas revalidadas

- **Corregidos:** S002-6–10 practica `a lot` sin `of`; S002-11–15 separa `a lot to do`; S002-16–20 practica `a lot of`; S002-31–35 usa `all over the world` y S002-51–55 usa `around the world`. Se mantienen distinguidas las cinco unidades.
- **Corregido:** S002-120 dice que el pronóstico indica que hoy hace sol; no usa `will`.
- **Corregido:** S004-11 y S005-63 alinean `trae` con `brings`; donde el español expresa `tener` noticias, el inglés usa `have`.
- **Corregido:** el problema señalado históricamente para S003-121 ya no aparece: la fila actual compara una foto en blanco y negro en ambos idiomas y no añade una situación de trabajo/oficina.
- **Corregido:** la variación del inglés es predominantemente británica (`colour`, `neighbour`, `city centre`, `car park`, `mobile phone`, entre otras). `Cell phone` se presenta explícitamente como variante estadounidense en S004-56–60 y S005-72, con la alternativa británica `mobile phone`.
- **Corregido:** las observaciones previas sobre S004-69, S003-119 y la construcción inglesa de S005-61 ya no persisten: se usan un contexto distinto para `at the same time`, `have dinner` para `cenamos`, y `far away from` en una frase natural, respectivamente.
- **Pendiente:** continúan los usos rígidos de `a period of time` (véase observación 2); el intervalo definido en S005-82 resuelve la indeterminación anterior, pero no la repetición/torpeza de la formulación.

## Observaciones pendientes priorizadas

### Prioridad alta — cobertura léxica y repaso

1. **A1-S002.csv, filas 36–40 — la unidad `anything else` no tiene cinco ejemplos claros.** Solo las filas 36–37 contienen literalmente `anything else`. La fila 38 usa `nothing else`, la 39 `something else` y la 40 `nothing else`; son expresiones relacionadas, pero no ejemplos de la unidad asignada `anything else`.

   **Cambio requerido:** reescribe S002-38–40 para que cada par practique explícitamente `anything else`, con formulaciones naturales en inglés y equivalencia real en español (por ejemplo, preguntas o negativas dirigidas a una persona). Mantén cinco ejemplos reconocibles de la unidad en las filas 36–40.

2. **A1-S003.csv, fila 61; A1-S005.csv, fila 73 — el repaso de S002-U01 pierde la colocación objetivo.** S003-61 usa `a little blue paint` y S005-73 `a little ink`; ninguna fila recupera el vocabulario específico `a little sugar` del catálogo. Los dos eventos afectados no cubren fielmente esa unidad, aunque cada bloque conserve doce filas.

   **Cambio requerido:** conserva el referente `sugar` en ambas recuperaciones, con contextos nuevos y naturales que no repitan el té/café de la introducción S002-1–5. Revisa el contenido léxico de los eventos para que cada una de las doce unidades de la cohorte sea realmente identificable, no solo el patrón gramatical general.

### Prioridad alta — fraseología artificial repetida

3. **A1-S002.csv, filas 46–50; A1-S003.csv, fila 70; A1-S005.csv, fila 82 — `a period of time` sigue insertada como plantilla redundante.** S002-46–50 repite cinco veces el mismo molde explicativo: acción + `for a period of time: [duración]` + marcador temporal. S003-70 repite la misma fórmula para tocar el piano. S005-82, aunque ahora concreta dos horas (de las tres a las cinco), mantiene `for a fixed period of time: two hours, from three to five`, que duplica la misma información y suena didáctico/literal, no a una frase cotidiana autónoma. S002-110 (`a short period of time`) también debe revisarse por concisión.

   **Cambio requerido:** simplifica esas filas concretas, varía los marcos sintácticos y conserva duraciones o condiciones claras cuando correspondan. No añadas una etiqueta temporal redundante seguida de su paráfrasis; conserva la unidad de vocabulario de forma idiomática y sin convertirla en relleno.

### Prioridad alta — equivalencia y dirección de movimiento

4. **A1-S005.csv, filas 16 y 25 — `come into` no tiene una dirección deíctica suficientemente establecida.** En S005-16, `Entro en la habitación para buscar mi libro.` se traduce como `I come into the room to get my book`; sin un interlocutor dentro de la habitación, la formulación neutral sería de movimiento hacia otro lugar, no hacia el hablante. S005-25 (`No entramos en el parque por la entrada lateral, sino por la principal.` / `We come into the park...`) tiene la misma ambigüedad: no se indica que el hablante esté dentro del parque.

   **Cambio requerido:** conserva y practica `come into` en contextos donde el destino esté claramente asociado al hablante/interlocutor, o reformula el español para hacer explícita esa perspectiva. No uses `come` como sustituto automático de `go` o `enter`.

### Prioridad media — nivel A1, variedad y naturalidad

5. **A1-S003.csv, filas 61–62, 66 y 72; A1-S004.csv, fila 76; A1-S005.csv, filas 61, 77–78 y 84; también S002-124–125.** Persisten microcontextos con carga técnica o vocabulario poco cotidiano para los objetivos de supervivencia A1: restauración de murales y filtros, alarma defectuosa de un edificio, mercancía que llega a un puerto, garantía y equipo, observatorio, sistema eléctrico de hospital, faro y boletín meteorológico/radio. S002-124–125 añade laboratorio/guantes de seguridad y reducción de acidez. En estos ejemplos el contexto distrae del elemento lingüístico objetivo y algunos términos no se reciclan ni se apoyan de forma suficiente en la sesión.

   **Cambio requerido:** sustituye esos escenarios por situaciones familiares (casa, clase, comida, transporte local, compras, familia o amistades), manteniendo el lema requerido, la equivalencia y la estructura gramatical de la fila. Si una escena especializada es imprescindible, reduce el vocabulario no objetivo y deja claro el contexto con lenguaje básico.

6. **A1-S004.csv, filas 124–125 — repetición casi duplicada.** S004-124 presenta un periódico que muestra una foto del partido en blanco y negro; S004-125 vuelve a presentar el periódico con una foto en blanco y negro. No son pares literalmente idénticos, pero la segunda fila apenas cambia la misma escena y no aporta una transferencia contextual distinta.

   **Cambio requerido:** reescribe una de las dos filas con otro referente y propósito para practicar `black and white` (por ejemplo, una señal, una prenda o una imagen de otro medio), sin repetir el contexto del periódico/fotografía.

7. **A1-S002.csv, filas 73–98 — el bloque G02 sigue concentrado en una sola plantilla de identificación con demostrativos.** La mayoría de las 26 filas consecutivas son afirmaciones, negaciones o preguntas de señalar objetos (`this/that/these/those` + objeto). Aunque cambian los objetos y hay contraste de número/distancia, la progresión contextual y la transferencia son débiles frente al objetivo combinado de artículos, contables, plurales y demostrativos.

   **Cambio requerido:** conserva contrastes de singular/plural y proximidad, pero convierte parte de la secuencia en intercambios autónomos con propósito reconocible; distribuye mejor `a/an/the`, sustantivos contables y plurales en afirmaciones, negativas y preguntas, sin alterar las 30 filas del bloque G02.

## Acción requerida

Corregir únicamente los cinco CSV auditados en la siguiente iteración global. Mantener 150 pares por archivo, cinco ejemplos claros para cada una de las doce unidades nuevas, los repasos 12/12 con colocaciones objetivo y contextos de transferencia, y los bloques gramaticales asignados. Revalidar desde bytes UTF-8, estructura CSV, puntuación española, equivalencia y naturalidad de las filas señaladas.
