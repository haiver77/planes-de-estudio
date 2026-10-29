# Informe de revisión - A1-S001 a A1-S005, iteración global 7

**Resultado: requiere correcciones y otra iteración.** Alcance exclusivo: los cinco CSV indicados en `loops_csv/7_loop/A1/`, el plan aprobado de `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo de trazabilidad y los informes de observaciones de los loops 6 y 7. No se revisaron otros CSV ni `loops_csv_old`.

## Evidencia de comprobaciones

- Existen exactamente los cinco IDs del alcance en la carpeta revisada. Los cinco archivos se decodifican desde bytes con UTF-8 estricto (sin BOM), y cada uno tiene exactamente 150 líneas/registros CSV y dos campos por registro, sin encabezado. La lectura CSV estricta no detecta filas vacías, campos vacíos/extra ni comillas mal cerradas; cada línea física contiene un solo `;` y no hay saltos de línea incrustados. Cumplen el mínimo obligatorio de 150 pares.
- La verificación de bytes y caracteres no detecta mojibake ni U+FFFD ni letras sustituidas por `?`; los signos ASCII `?` son cierres de pregunta y las preguntas españolas revisadas llevan `¿`. Los caracteres `á é í ó ú ü ñ ¿ ¡` están correctamente codificados.
- El catálogo contiene 12 U por sesión y el bloque 1-60 de cada archivo tiene cinco pares consecutivos por U, siguiendo el orden de las entradas. Se distingue este vocabulario léxicamente requerido de la gramática objetivo de cada sesión.
- Los repasos previstos sí recuperan 12/12 unidades: S003 filas 61-72 (+1 S002), S004 filas 61-72 (+1 S003) y 73-84 (+3 S001), S005 filas 61-72 (+1 S004) y 73-84 (+3 S002). Se mantiene una unidad por fila en esos bloques.
- Se comprobaron fila por fila las observaciones del informe guardado en `loops_csv/6_loop/0_observaciones_a_las_sesiones.md` y las pendientes del informe en `loops_csv/7_loop/0_observaciones_a_las_sesiones.md`. Los problemas de los bloques de repaso anteriores y las correcciones señaladas allí (incluidas las filas S003 5/7/17/54/95, S004 15-20/49/108/124 y S005 25/26/28/42/59/79/136/142, así como las filas de imperativos expresamente señaladas) están corregidos en esta versión, salvo S004 fila 22, que sigue requiriendo cambio. Las observaciones nuevas pendientes se detallan abajo.
- No se detectaron duplicados exactos dentro de un mismo archivo. Sí aparecen pares completos idénticos entre sesiones fuera de los bloques de repaso programados; se enumeran abajo porque no aportan transferencia contextual.

## Observaciones pendientes priorizadas

### Prioridad alta - equivalencia, construcción o contexto

1. **`A1-S004.csv`, fila 22:** `Lo malo de ese autobús es que va lleno y es lento.;The bad things about that bus are that it is crowded and slow.` El español presenta una construcción singular y el inglés mantiene el plural; además, las cláusulas con `que` hacen forzada la versión española para el patrón léxico plural. **Cambio requerido:** usar una estructura paralela y natural en ambos idiomas, por ejemplo `Las cosas malas de ese autobús son el ruido y los asientos incómodos.;The bad things about that bus are the noise and the uncomfortable seats.`

2. **`A1-S005.csv`, fila 119:** `Olvidar las llaves es una mala idea.;Forgetting your keys is a bad thing.` `Una mala idea` no equivale a `a bad thing`. **Cambio requerido:** alinear el concepto en ambas columnas, por ejemplo `Olvidar las llaves es algo malo.;Forgetting your keys is a bad thing.`

3. **`A1-S001.csv`, fila 74:** `No llegamos a tiempo.;We are not on time.` El español usa `llegar` (no alcanzar/llegar a tiempo), mientras que el inglés expresa estado con `be`; no conserva la misma estructura ni sentido fino. **Cambio requerido:** `No estamos a tiempo.;We are not on time.` (o reformular ambos lados como acción de llegar).

4. **`A1-S002.csv`, fila 46:** `Necesitamos un período de tiempo para estudiar con calma.;We need a period of time to study quietly.` `Con calma` significa sin prisa/tranquilamente, no necesariamente en silencio (`quietly`). **Cambio requerido:** alinear el matiz, por ejemplo cambiar inglés a `to study at a relaxed pace` o español a `para estudiar en silencio`.

5. **`A1-S002.csv`, fila 67:** `En casa el sábado, es una buena idea llevar un paraguas.;At home on Saturday, it's a good idea to take an umbrella.` El marco espacial/temporal queda desconectado del consejo y produce una escena arbitraria en ambos idiomas. **Cambio requerido:** quitar ese marco o dar una razón contextual clara y coherente para llevar paraguas, manteniendo el nivel gramatical de la sesión.

### Prioridad media - gramática no prescrita, naturalidad y consistencia

6. **`A1-S005.csv`, fila 19:** `Entra en la oficina y deja tu abrigo aquí.;Come into the office and leave your coat here.` Es un imperativo, objetivo gramatical posterior (A1-G07), y S005 trabaja G05; el propósito comunicativo de S005 no es dar instrucciones. **Cambio requerido:** convertirlo en frase autónoma con gramática ya cubierta, conservando `come into` (p. ej., una afirmación o pregunta en presente simple).

7. **`A1-S005.csv`, fila 61:** `La bicicleta debe mantenerse alejada del tráfico.;The bicycle should be kept away from traffic.` El repaso léxico de `away from` se presenta con `should` y pasiva, estructuras no prescritas en S005 ni necesarias para practicar la unidad. **Cambio requerido:** reformular con una estructura sencilla ya cubierta, por ejemplo una afirmación con `estar/is ... away from`.

8. **`A1-S004.csv`, fila 68:** `No puedo hablar en este momento porque estoy en una reunión.;I cannot talk at the moment because I am in a meeting.` Introduce `can/cannot`, objetivo posterior A1-G07, mientras S004 introduce G04. **Cambio requerido:** mantener `at the moment` con una estructura gramatical ya prescrita, sin la forma modal adelantada.

9. **`A1-S003.csv`, filas 89-90:** fila 89 `Nuestra maestra no tiene sombrero verde` omite el artículo de `a green hat` y puede leerse como `no lleva sombrero`; fila 90 cambia a `Nuestro maestro` dentro de la misma secuencia, mientras que las filas 88-89 identifican a `Nuestra maestra`. **Cambio requerido:** usar `un sombrero verde` en la fila 89 y conservar el mismo referente/género de profesor en las tres filas (88-90).

10. **`A1-S003.csv`, fila 96:** `¿En casa tengo una bolsa azul?;At home, have I got a blue bag?` La inversión y el marco antepuesto resultan poco idiomáticos en ambas preguntas. **Cambio requerido:** reformular naturalmente, por ejemplo `¿Tengo una bolsa azul en casa?;Have I got a blue bag at home?`.

11. **Repetición exacta no programada entre sesiones:** se encontraron pares idénticos fuera de los bloques explícitos de repaso: `A1-S001` filas 2, 3, 9, 10, 14, 20, 41, 46, 53, 56 y 124 reaparecen literalmente en `A1-S002` filas 137, 113, 114, `A1-S005` 116, `A1-S002` 139, 140, 121, 146, 123, 148 y 143, respectivamente; además, `A1-S002` fila 112 se repite en `A1-S003` fila 106. **Cambio requerido:** conservar el repaso previsto, pero sustituir las copias literales fuera de esos bloques por ejemplos contextuales distintos que recuperen la unidad sin repetir el mismo par palabra por palabra.

**Acción requerida:** corregir las filas y repeticiones enumeradas, mantener el formato y 150 pares por archivo, guardar en UTF-8 y entregar otra iteración para revisión.
