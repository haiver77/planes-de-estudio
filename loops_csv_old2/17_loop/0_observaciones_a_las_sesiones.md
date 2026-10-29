# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración global 16

**Resultado: requiere correcciones; se necesita otra iteración global.**

## Alcance y referencias

Se revisaron exclusivamente `A1-S001.csv` a `A1-S005.csv` en `loops_csv/16_loop/A1/`, fila por fila. Referencias cotejadas: `indicaciones_csv.md`, el plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv` y las observaciones pendientes aplicables de los informes históricos, incluido el informe de `loops_csv/16_loop/0_observaciones_a_las_sesiones.md`, rotulado 15. No se auditó el resto del nivel ni se inspeccionó `loops_csv_old`.

## Evidencia técnica y de cobertura

- Los cinco IDs dentro del alcance están presentes. No falta ninguno de los IDs solicitados.
- Se verificaron los archivos desde sus bytes con decodificación UTF-8 estricta. Tamaños: S001 12 984 bytes; S002 13 941; S003 12 809; S004 13 857; S005 13 750.
- Cada CSV tiene exactamente 150 líneas y 150 registros: 750 pares en total. Cada línea se pudo leer con un parser CSV estricto y contiene dos campos no vacíos separados por un solo `;`, sin encabezado. No hay filas vacías, campos extra, comillas mal cerradas, saltos de línea incrustados ni `;` dentro de frases. La coma no se usa como delimitador.
- Los cinco archivos no tienen BOM y son UTF-8 válido en lectura de bytes. No se encontraron secuencias de mojibake, U+FFFD ni `?` sustituyendo letras. Las interrogaciones de las preguntas españolas están emparejadas con apertura `¿` y cierre `?`; los caracteres acentuados inspeccionados son correctos.
- No hay pares español–inglés duplicados literalmente ni campos completos duplicados dentro de estos cinco archivos. Sí queda una transferencia contextual demasiado próxima entre S004-69 y S003-43, detallada abajo.
- En las filas 1–60 de cada archivo se cotejaron las 12 unidades nuevas asignadas en el catálogo, con cinco ejemplos por unidad (12 × 5). Se mantienen diferenciadas las entradas cercanas *all over the world* y *around the world*.
- Los repasos programados cubren 12/12 unidades en cada evento: S002-61–72 recupera S001; S003-61–72 recupera S002; S004-61–72 recupera S003 y S004-73–84 recupera S001; S005-61–72 recupera S004 y S005-73–84 recupera S002.
- La distribución coincide con el plan y cada archivo suma 150: S001 = 60 nuevos + 0 repaso vencido + 30 G01 + 60 integración; S002 y S003 = 60 + 12 + 30 + 48; S004 y S005 = 60 + 24 + 30 + 36. Los bloques gramaticales asignados practican sus objetivos: G01 en S001-61–90; G02 en S002-73–102; G03 en S003-73–102; G04 en S004-85–114; y G05 en S005-85–114.

## Observaciones históricas revalidadas

- **Corregido:** S003-63, -67 y -68 ahora presentan una feria escolar, té conocido globalmente y una lista de tareas, respectivamente; ya no reproducen el marco de las tareas antes de la cena, la música mundialmente popular ni la comida/menú de las introducciones.
- **Corregido:** S004-65–68 usan el inicio de un viaje, el final de una clase, beber agua al final de un paseo y estar en la escuela en ese momento; no conservan los escenarios de entretenimiento, ubicación de objetos o establecimiento cerrado señalados anteriormente.
- **Corregido:** S005-82 especifica dos horas, de las tres a las cinco. La duración ya no queda indeterminada.
- **Corregido:** S002 G02-73–98 redujo el vocabulario técnico y ofrece contrastes variados de demostrativos, número, distancia, afirmación, negación y pregunta con objetos y lugares cotidianos. No se observa gramática posterior adelantada en ese tramo. Las filas 99–102 completan el bloque previsto de 30 pares con artículos, plural y estructuras be ya introducidas.
- **Corregido:** las transferencias de repaso verificadas mantienen 12/12 unidades en todos los eventos; las antiguas parejas de duplicación literal revisadas no reaparecen como pares exactos.

## Observaciones pendientes priorizadas

### Prioridad alta — transferencia repetida

1. **A1-S004.csv, fila 69, frente a A1-S003.csv, fila 43.** S004-69 dice `Mi hermana y yo salimos de casa al mismo tiempo cada mañana.;My sister and I leave home at the same time every morning.` S003-43 ya dice `Mi hermana y yo salimos al mismo tiempo cada mañana.;My sister and I leave at the same time every morning.` Añadir `de casa/home` no crea un contexto de repaso realmente nuevo: se repiten las mismas personas, la salida conjunta y el marco de cada mañana para practicar *at the same time*.

   **Cambio requerido:** sustituye S004-69 por un ejemplo autónomo de *at the same time* en una actividad y situación distintas, sin volver a una salida matinal ni a las escenas de coincidencia temporal ya usadas en S003-41–45. Mantén equivalencia entre ambos idiomas.

### Prioridad media — equivalencia y naturalidad

2. **A1-S003.csv, fila 119.** `Mi familia y yo cenamos juntos los fines de semana.;My family and I eat together at the weekend.` El español especifica que comen la cena; el inglés solo afirma que comen juntos y pierde esa información.

   **Cambio requerido:** conserva el sentido de cena en inglés, por ejemplo `My family and I have dinner together at the weekend` (o una variante regional coherente con el resto del archivo).

3. **A1-S005.csv, fila 61.** `El observatorio está apartado de las luces de la ciudad y los visitantes ven las estrellas con claridad.;The observatory is set away from the city lights, and visitors see the stars clearly.` `Is set away from` resulta poco idiomático para expresar la ubicación del observatorio.

   **Cambio requerido:** usa una construcción natural que conserve el sentido, como `The observatory is far from the city lights, so visitors can see the stars clearly`, ajustando también el español si se cambia la relación entre las dos ideas.

## Acción requerida

Corregir únicamente los cinco CSV auditados para la siguiente iteración global, manteniendo las cantidades, las unidades nuevas, los repasos 12/12, los bloques gramaticales y los totales previstos. Volver a validar el UTF-8 desde bytes y el formato de dos columnas, además de las filas modificadas y la transferencia contextual.
