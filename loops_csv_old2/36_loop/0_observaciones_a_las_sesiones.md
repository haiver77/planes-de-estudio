# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración auditada:** `loops_csv/35_loop/A1/`  
**Informe de salida:** `loops_csv/36_loop/0_observaciones_a_las_sesiones.md`  
**Plan aprobado:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo cotejado:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Referencias revisadas:** `indicaciones_csv.md`, `contexto.md` y los informes de `loops_csv/33_loop/`, `34_loop/` y `35_loop/`.  
**Alcance exclusivo:** `A1-S001.csv` a `A1-S005.csv`. No se inspeccionaron ni modificaron otras iteraciones ni `loops_csv_old/`.

## Evidencia técnica, cobertura y fidelidad al plan

- En la carpeta auditada están exactamente los cinco archivos del alcance, uno por cada ID previsto: A1-S001 a A1-S005. Los cinco ID aparecen en el plan y cada catálogo asigna 12 unidades de introducción a su sesión.
- Se decodificaron los bytes de cada CSV con UTF-8 estricto y se analizaron con `csv.reader` en modo estricto. Los cinco contienen **150 registros válidos** (750 pares en total), sin encabezado; cada fila tiene exactamente dos campos no vacíos, en orden español–inglés, separados por un único `;`. No hay filas vacías, campos adicionales, comillas mal cerradas, saltos de línea incrustados ni archivos delimitados por comas. La cantidad de líneas físicas coincide con la de registros.
- No se detectaron BOM, U+FFFD (`�`), secuencias de mojibake (`Ã¡`, `Ã±`, etc.), `?` sustituyendo letras ni preguntas españolas sin `¿`. No hay duplicados exactos de frases españolas o inglesas dentro de estos archivos.
- Los bloques mantienen los tamaños del plan: S001 = 60 vocabulario nuevo + 0 repaso + 30 gramática + 60 integración; S002/S003 = 60 + 12 + 30 + 48; S004/S005 = 60 + 24 + 30 + 36. La revisión de los bloques confirma la secuencia de vocabulario, los repasos declarados y los bloques gramaticales G01–G05 en sus rangos. Cada sesión alcanza el mínimo obligatorio explícito de 150 pares.
- Comparé directamente `loops_csv/34_loop/A1/` con los CSV actuales y revisé las **20 filas modificadas**: S001-10/144; S002-25/60; S003-49/50; S004-18/20/129/131; S005-4/21/39/40/65/106/117/124/135/140. Las modificaciones de S001-10/144, S002-25/60, S003-49/50 y S005-4/21/39/40/65/106/117/124/135/140 son correctas en el contenido cotejado. S004-18 aclara la situación de las sillas y S004-20 es comprensible, pero no resuelven por completo la repetición de la secuencia S004-17/19. S004-129/131 conservan el problema de adecuación A1 indicado en el informe anterior. S005-4, aunque ahora es breve, deja sin resolver la progresión del bloque S005-1–5, porque S005-3 retiene la frase larga.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta: observaciones previas todavía pendientes

1. **A1-S004.csv, filas 129 y 131 — se mantienen los términos menos básicos señalados en el informe anterior.**  
   `Mis libros están en mi taquilla.;My books are in my locker.` y `Mi teléfono se queda sin batería en clase.;My phone runs out of battery in class.` La equivalencia es comprensible, pero `locker` y `runs out of battery` elevan la carga léxica de estas frases de integración A1. **Cambio requerido:** usar objetos y expresiones frecuentes sin esa formulación avanzada; por ejemplo, `Mis libros están en mi mochila.;My books are in my bag.` y `Mi teléfono está apagado en clase.;My phone is off in class.`

2. **A1-S005.csv, filas 3–5 — la progresión del bloque sigue siendo irregular pese a la corrección de la fila 4.**  
   La fila 3 aún dice `Después de llegar en tren, camino hasta el centro de la ciudad para visitar el mercado.;After arriving by train, I walk to the city centre to visit the market.` Acumula llegada, medio de transporte, desplazamiento y propósito, con una construcción inicial en gerundio. La fila 4 vuelve a `Voy al centro de la ciudad`, y la 5 añade solo comprar pan: la secuencia no crece gradualmente. **Cambio requerido:** simplificar la fila 3 a una acción/contexto A1 y ordenar las tres filas para que la información aumente de manera natural, sin reiniciar la progresión en la fila 4.

3. **A1-S004.csv, filas 17 y 19 (secuencia 17–20) — persiste la repetición semántica y de plantilla.**  
   La fila 17 dice `Dejar la puerta abierta es algo malo` y la 19 repite la misma idea con `durante la clase ... para todos`; la 20 vuelve a la estructura `Dejar la luz encendida ... puede ser algo malo`. Aunque la fila 18 ahora concreta el problema de las sillas, dos de las filas siguen repitiendo el motivo de dejar algo abierto/encendido y la misma plantilla. **Cambio requerido:** conservar una sola frase sobre la puerta y sustituir otra por un inconveniente cotidiano distinto, con una expansión que aporte información nueva.

### Prioridad media: naturalidad, autonomía y adecuación A1

4. **A1-S001.csv, fila 9 — escenario poco coherente.**  
   `Tenemos unos minutos antes de clase en la estación con mi madre.;We have a few minutes before class at the station with my mother.` No se explica por qué la clase ocurre en la estación ni qué hacen allí la persona y su madre. **Cambio requerido:** dar un contexto cotidiano que conecte el lugar con la espera, o eliminar la referencia a la estación; por ejemplo, `Tenemos unos minutos antes de que empiece la clase.;We have a few minutes before class starts.`

5. **A1-S001.csv, filas 19–20 — situación forzada y poco autónoma para practicar `a few years`.**  
   `Unos cuantos años son mucho tiempo para un niño en esta ciudad lejos de casa` y `... para un niño que vive lejos de su familia` describen a un niño apartado de su hogar/familia durante años, sin explicar la situación. **Cambio requerido:** cambiarlo por una relación temporal plausible y completa, por ejemplo `Unos cuantos años son mucho tiempo para vivir lejos de la familia.;A few years is a long time to live far from your family.`

6. **A1-S001.csv, fila 115 — traducción inglesa poco natural.**  
   `La leche que queda alcanza para mi té.;The milk left is enough for my tea.` `The milk left is enough` no es una formulación idiomática en inglés. **Cambio requerido:** conservar el español y usar `There is enough milk left for my tea.`

7. **A1-S002.csv, filas 14–15 — ampliación ambigua y mecánica.**  
   La fila 14 es `Tengo mucho que hacer hoy en casa antes de la cena`; la 15 repite la frase y añade `con mi hermana / with my sister` al final. No queda claro si la hermana ayuda o comparte la cena, y la extensión no añade una acción concreta. **Cambio requerido:** explicitar la relación y hacer que la segunda frase progrese; por ejemplo, `Tengo mucho que hacer antes de la cena, así que mi hermana me ayuda.;I have a lot to do before dinner, so my sister helps me.`

8. **A1-S003.csv, fila 23 — vocabulario/escena por encima de A1 en una secuencia de clase.**  
   `Al comienzo del evento escolar, los estudiantes presentan una canción para sus familias.;At the beginning of the school event, students perform a song for their families.` `Evento escolar` y especialmente `perform` son menos básicos que el resto del bloque, mientras que las filas 24–25 ya usan una escena sencilla de clase. **Cambio requerido:** mantener `at the beginning of` con personas y una acción cotidiana de alta frecuencia.

9. **A1-S004.csv, fila 10 — frase demasiado cargada para A1 y repetición del foco de humo.**  
   `La médica explica que el humo es malo para los pulmones, así que mi hermano evita fumar cerca de sus hijos.;The doctor explains that smoke is bad for the lungs, so my brother avoids smoking near his children.` La frase combina varias cláusulas y léxico menos básico (`explains`, `lungs`, `avoids smoking`), y vuelve al humo después de la fila 6 (`Smoke is bad for your health`). **Cambio requerido:** sustituirla por un ejemplo breve con `bad for` y vocabulario frecuente distinto, por ejemplo `El ruido es malo para dormir.;Noise is bad for sleep.`

10. **A1-S005.csv, filas 49–50 — cierre de la progresión más breve que la fila anterior.**  
    La fila 49 compara dos nombres y dos letras (`Megan ... pero Lucas ...`), mientras que la fila 50 se reduce a `La palabra cat termina en t.;The word cat ends in t.` La última frase no cierra con una ampliación y la anterior es más compleja que las demás. **Cambio requerido:** simplificar la fila 49 y hacer que la 50 añada un detalle sencillo al mismo foco `ends in`; por ejemplo, `La palabra cat termina en la letra t.;The word cat ends in the letter t.`

## Resultado

La cobertura, el formato, la codificación y el mínimo de 150 pares por CSV cumplen. Sin embargo, permanecen observaciones de adecuación A1, progresión, naturalidad, coherencia y variedad; además, las filas S004-129/131 siguen pendientes de la revisión anterior. **Se requiere otra iteración** y una nueva auditoría de estos cinco CSV.
