# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración global 11

**Resultado: requiere correcciones; se necesita otra iteración.** Alcance auditado exclusivamente: `loops_csv/11_loop/A1/A1-S001.csv` a `A1-S005.csv`. Referencias: `indicaciones_csv.md`, plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv` y los informes históricos disponibles; en particular, las ocho observaciones de `loops_csv/11_loop/0_observaciones_a_las_sesiones.md`. No se inspeccionó ningún otro CSV ni `loops_csv_old`.

## Evidencia de comprobaciones

- Los cinco archivos solicitados existen y son los cinco IDs dentro del alcance. No se comprobó la cobertura del resto del nivel A1, por la limitación explícita de auditar únicamente estos archivos.
- Validación de bytes y lectura CSV estricta: los cinco se decodifican con UTF-8 real, sin BOM. Cada uno tiene 150 líneas físicas y 150 registros (750 pares en total), dos campos por registro, sin encabezado, campos vacíos, filas en blanco, comillas mal cerradas ni saltos de línea incrustados. Cada línea tiene exactamente un `;`; no se usa la coma como delimitador.
- No se detectaron `Ã¡`, `Ã±`, U+FFFD ni letras sustituidas por `?`. En todas las preguntas españolas coincide la cantidad de `¿` y `?`; los `?` ASCII son cierres de pregunta. Los caracteres acentuados y signos españoles presentes están correctamente codificados.
- En las filas 1–60 de cada archivo se cotejaron 12 unidades nuevas del catálogo, cinco pares por unidad (12 × 5). El registro fuente repetido de `all over the world` en el catálogo remite a la unidad A1-S002-U07; no se contó como unidad nueva adicional.
- Los eventos de repaso del plan cubren 12/12 unidades cada uno: S002 filas 61–72; S003 61–72; S004 61–72 y 73–84; S005 61–72 y 73–84. Reparto por sesión: S001 60 nuevas + 0 repaso + 30 gramaticales + 60 de integración; S002 y S003 60 + 12 + 30 + 48; S004 y S005 60 + 24 + 30 + 36. Todos suman 150.
- No hay pares completos duplicados dentro de un mismo CSV. Sí hay repeticiones literales entre sesiones y repeticiones contextuales muy próximas dentro de algunas sesiones; se detallan abajo. Los repasos previstos no eximen del requisito del plan de recuperar las unidades en un contexto nuevo.
- La búsqueda fila por fila no encontró imperativos en S004 ni `can/can’t` en los cinco CSV. El *do-support* aparece en S004, foco G04, y en S005 como repaso de G04; no se detectó fuera de esos ámbitos. Tampoco se encontró presente continuo ni pasiva de evento fuera de foco. `is open/closed` describe estados, no pasivas de evento. `be going to` en S004/S005 y el pasado de `He came into the room` en S005 corresponden a unidades léxicas explícitas del catálogo.
- Las ocho correcciones indicadas en el informe histórico de n11 están aplicadas: los imperativos de S004-1/3/54 son ahora declarativos; S003-100/120/146 y S002-16 ya están corregidas; S004-101 y S004-103 ahora describen situaciones distintas; S001-125/135/137/147/149 son ejemplos nuevos y autónomos; S004-2/5 y S005-16 también fueron reformuladas. Las observaciones históricas originales no se repiten como fallos; quedan los defectos nuevos/remanentes siguientes.

## Observaciones pendientes priorizadas

### Prioridad alta — duplicación literal o transferencia contextual insuficiente

1. **Pares idénticos entre sesiones pese a que el plan exige recuperar las unidades en contexto nuevo.** Se encontraron estas coincidencias exactas:
   - S001-6 / S002-62; S001-11 / S002-63; S001-146 / S002-65.
   - S001-64 / S002-99; S001-65 / S002-100; S001-67 / S002-102.
   - S001-7 / S004-74.
   - S002-31 / S005-79; S002-50 / S005-82.
   - S004-88 / S005-111; S004-90 / S005-113.
   
   Varias coincidencias están en bloques de repaso o de repaso gramatical, pero son traducciones copiadas literalmente, no recuperación contextual. **Cambio requerido:** reescribir uno de cada par con una situación y frase nuevas; conservar la unidad y, donde corresponda, la estructura gramatical repasada. Volver a cotejar las filas de repaso para mantener 12/12.

2. **`A1-S001.csv`, filas 2/130, 26/111, 40/113, 59/117 y 138/150.** Aunque no todas las parejas son duplicados literales completos, repiten prácticamente el mismo ejemplo: sillas para la clase; el mismo café cerca de casa (la frase española de 26 y 111 es idéntica); el mismo mensaje sobre el clima (40/113, con solo contracción distinta); dinero en la cartera/billetera (el inglés de 59 y 117 es idéntico); y el mismo acuerdo con el profesor sobre el viaje de estudios (138/150, cambiando solo el género en español). **Cambio requerido:** sustituir al menos una fila de cada grupo por una transferencia contextual distinta, no por una variante léxica o de contracción.

3. **`A1-S004.csv`, filas 52/129/140 y 54/126/145.** Se reiteran dos microcontextos: disponibilidad de plazas para bicicletas en el aparcamiento (52, 129, 140) y proximidad del aparcamiento/coche a la entrada (54, 126, 145). **Cambio requerido:** variar la situación de varias filas para que el vocabulario de *car park* y *away from* se recupere en contextos distintos; no limitarse a cambiar singular/plural o “by/beside/not far”.

4. **`A1-S004.csv`, filas 103–104.** Ambas repiten que un establecimiento cierra por un problema eléctrico: el museo cierra temprano por una avería eléctrica y la tienda cierra por un problema eléctrico. La corrección de S004-101/103 resolvió la repetición histórica del partido, pero quedó esta pareja casi calcada. **Cambio requerido:** conserva solo uno de los cierres eléctricos y sustituye el otro por otro contexto natural de causa con *because of*.

5. **`A1-S005.csv`, filas 21–25.** Cinco frases sucesivas repiten la misma escena y plantilla —él entra en la habitación—, añadiendo libros, silencio, propósito u hora. La entrada léxica de pasado está bien identificada, pero esta serie no ofrece cinco contextos diferenciados. **Cambio requerido:** conserva la unidad *He came into the room* y el nivel, pero diversifica sujetos, tipos de habitación y situaciones, evitando cinco variaciones del mismo acontecimiento.

6. **`A1-S005.csv`, filas 100–106 y 76/150.** Las filas 100–106 acumulan siete ejemplos con el marco “en casa” y alimentos/utensilios para *there is/are* y cuantificadores; 76 y 150 repiten, con otro marcador temporal, “hay mucho tráfico en el centro de la ciudad”. **Cambio requerido:** distribuye los ejemplos gramaticales entre lugares y situaciones diferentes, conservando el contraste de cantidad y singular/plural; sustituye una de las dos frases del tráfico por otro contexto.

7. **`A1-S002.csv`, filas 118, 120 y 144.** Se repite tres veces la plantilla editorial `Respondo: «…» / I reply, “…”`, sin que cada fila incluya la intervención que provoca la respuesta; los mensajes citados reciclan frases ya practicadas. **Cambio requerido:** elimina el marco “Respondo/I reply” sin contexto o construye intercambios autónomos y variados; no envuelvas frases ya vistas en comillas como si eso aportara una transferencia nueva.

### Prioridad media — equivalencia, naturalidad y consistencia

8. **`A1-S004.csv`, fila 1.** `Los niños se mantienen lejos del fuego.;The children stay away from fire.` La traducción omite el artículo definido exigido por `del fuego`. **Cambio requerido:** `The children stay away from the fire.`

9. **`A1-S004.csv`, fila 26.** `La lluvia cancela el partido por el campo inundado.;Rain cancels the match because of the flooded field.` La explicación repite prácticamente la misma causa (lluvia/campo inundado) y suena forzada. **Cambio requerido:** conserva *because of* y el presente simple, pero usa una causa no redundante y una frase idiomática en ambas columnas.

10. **`A1-S005.csv`, fila 80.** `¿Te apetece algo más para el desayuno?;Is anything else appealing for breakfast?` La traducción inglesa suena poco natural y cambia una pregunta dirigida al interlocutor por una valoración impersonal. **Cambio requerido:** usa una pregunta directa y coloquial con intención equivalente, por ejemplo `Do you fancy anything else for breakfast?`, manteniendo el nivel ya cubierto.

11. **`A1-S005.csv`, fila 123.** `Mi hermana repasa inglés durante veinte minutos antes del desayuno.;My sister reviews English for twenty minutes before breakfast.` *Reviews English* resulta poco idiomático en este contexto. **Cambio requerido:** emplea una colocación natural (`studies English`/`revises English`) y alinea el español con el matiz elegido.

12. **`A1-S003.csv`, filas 82–84.** La misma secuencia cambia de `teacher/profesor` en 82 a `teacher/maestro` en 83–84, sin cambio de referente que motive la alternancia. **Cambio requerido:** mantén un mismo término para el profesor a lo largo de las tres afirmaciones/preguntas.

13. **Consistencia de variante léxica inglesa.** `A1-S002.csv`, filas 27 y 140, alterna `neighbour` y `neighbor`; `A1-S004.csv`, filas 56–60 y 146, alterna `cell phone` con `mobile phone` aunque el catálogo fija `cell phone` para la unidad nueva. **Cambio requerido:** elige una variante ortográfica/terminológica coherente en cada sesión y mantén la forma de catálogo al recuperar la unidad.

14. **`A1-S001.csv`, fila 145.** `La escuela tiene varios años...;The school is a few years old...` `Varios años` no conserva con precisión el valor de *a few years*. **Cambio requerido:** cambia el español a `unos pocos años` o el inglés a `several years old`, manteniendo la unidad léxica prevista donde corresponda.

## Acción requerida

Corrige todas las observaciones, conserva los 150 pares por CSV, los bloques 12 × 5, los eventos de repaso 12/12 y el reparto gramatical/integración indicado por el plan. Después, vuelve a validar los bytes UTF-8 y la estructura con lectura estricta y revisa que cada recuperación use un contexto realmente nuevo.
