# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración global 18

**Resultado: requiere correcciones; se necesita otra iteración global (19).**

## Alcance y referencias

Se revisaron exclusivamente `A1-S001.csv`, `A1-S002.csv`, `A1-S003.csv`, `A1-S004.csv` y `A1-S005.csv` en `loops_csv/18_loop/A1/`, fila por fila. Se cotejaron `indicaciones_csv.md`, el plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv` y las observaciones históricas aplicables, con especial atención a `loops_csv/18_loop/0_observaciones_a_las_sesiones.md`. No se auditó el resto del nivel ni se inspeccionó `loops_csv_old`.

## Evidencia técnica, cantidades y cobertura

- En la carpeta auditada están exactamente los cinco CSV solicitados: no falta ningún ID ni hay archivos CSV ajenos al alcance.
- Se leyeron los bytes y se validaron con decodificación UTF-8 estricta y un parser CSV estricto. Tamaños: S001 12 984 bytes; S002 13 941; S003 12 817; S004 13 842; S005 13 674. Ninguno tiene BOM.
- Cada archivo contiene 150 líneas físicas y 150 registros CSV: 750 pares en total. Cada registro tiene dos campos no vacíos, español primero e inglés después, delimitados por `;`, sin encabezado. No se hallaron comas usadas como delimitador, filas vacías, campos adicionales, comillas mal cerradas, saltos de línea incrustados ni `;` dentro de frases.
- No se detectaron secuencias de mojibake, U+FFFD ni signos `?` que sustituyan letras. Las preguntas españolas encontradas tienen apertura `¿` y cierre `?`. No hay pares duplicados literalmente dentro de estos cinco archivos.
- Cada sesión contiene 60 filas de presentación inicial (filas 1–60), 30 filas gramaticales en el bloque previsto y las cantidades planificadas de repaso e integración. Los totales son: S001 = 60 nuevas + 0 repaso vencido + 30 gramaticales + 60 integración; S002 y S003 = 60 + 12 + 30 + 48; S004 y S005 = 60 + 24 + 30 + 36. Todos suman 150.
- Los bloques gramaticales corresponden a G01 en S001-61–90, G02 en S002-73–102, G03 en S003-73–102, G04 en S004-85–114 y G05 en S005-85–114.
- Los repasos programados están presentes en los bloques previstos y cubren 12/12 unidades: S002-61–72; S003-61–72; S004-61–72 y 73–84; S005-61–72 y 73–84. En particular, S005-61–72 recupera las doce unidades de S004 y S005-73–84 las doce de S002.

## Observaciones históricas revalidadas

- **Corregido:** S005-73–84 incluye `a lot to do` (fila 74) y distingue `a lot` (fila 76) de `a lot of` (fila 75); el resto del bloque cubre las otras unidades de repaso de S002.
- **Corregido:** en S005-21–25 se conserva exactamente `He came into the room.` en la fila 21; las otras cuatro formas usan presente simple `come/comes into`. No se practica productivamente el pasado simple.
- **Corregido:** S005-118 alinea `anuncia` con `announces`.
- **Corregido:** S005-82 determina el período: dos horas, de las tres a las cinco.
- **Corregido:** S004-69 ofrece un contexto distinto para `at the same time`; S003-119 conserva `cenamos` como `have dinner`; S005-61 mantiene una traducción natural con `far away from`.

## Observaciones pendientes priorizadas

### Prioridad alta — no se mantienen cinco ejemplos inequívocos por cada unidad nueva

1. **A1-S002.csv, filas 6–10 y 51–55 — mezcla de unidades léxicas distintas.**
   - El bloque asignado a `a lot` (filas 6–10) solo practica claramente el adverbio `a lot` en las filas 6, 7 y 9. La fila 8 (`Tenemos mucho trabajo esta semana.;We have a lot of work this week.`) y la fila 10 (`Me parece mucho dinero.;That seems like a lot of money to me.`) usan `a lot of + sustantivo`, que corresponde a la unidad distinta `a lot of sth` de S002-U04. Así, U02 queda con tres ejemplos claros y se contaminan los cinco previstos para U04.
   - En el bloque de `around the world` (filas 51–55), la fila 55 dice `all over the world`, expresión asignada a otra unidad del mismo CSV; por tanto, U11 tiene cuatro ejemplos claros y se vuelve a mezclar con U07.

   **Cambio requerido:** reescribe S002-8 y S002-10 con `a lot` usado adverbialmente, sin `of`; reescribe S002-55 con `around the world`. Mantén cinco ejemplos reconocibles para cada una de las doce unidades y conserva separadas `a lot`, `a lot to do`, `a lot of sth`, `all over the world` y `around the world`.

### Prioridad alta — estructura gramatical no prevista para esta etapa

2. **A1-S002.csv, fila 120.** `El pronóstico anuncia sol, así que es una buena idea llevar gafas de sol.;The forecast says it will be sunny, so it is a good idea to wear sunglasses.` La versión inglesa introduce `will` para una predicción futura. S002 presenta G02 y el plan de A1 no asigna esta estructura a la sesión; el futuro no es necesario para practicar `a good idea`.

   **Cambio requerido:** evita `will` y conserva la equivalencia con una formulación natural en presente, por ejemplo, expresa que el pronóstico indica que hoy hace sol y que por eso es buena idea llevar gafas de sol.

### Prioridad media — equivalencia de la acción comunicativa

3. **A1-S004.csv, fila 11; A1-S005.csv, fila 63.** En ambos pares el español dice que alguien `trae malas noticias`, pero el inglés dice que alguien `has bad news`. Tener noticias no expresa exactamente traerlas/comunicarlas; es una diferencia de acción semejante a la que se corrigió en S005-118.

   **Cambio requerido:** alinea cada par: usa `brings bad news` si se mantiene la acción de traer/comunicar, o cambia el español a `tiene malas noticias` para conservar `has bad news`.

4. **A1-S003.csv, fila 121.** `Mi hermana está en su oficina ahora.;My sister is at work in her office now.` El inglés añade que está trabajando; el español solo indica que está en su oficina.

   **Cambio requerido:** elimina `at work` en inglés o explicita esa información en español, sin añadir un dato de situación en un solo idioma.

### Prioridad media — carga léxica y contextual demasiado especializada para los objetivos cotidianos A1

5. **A1-S002.csv, filas 47–50; A1-S003.csv, fila 70; A1-S004.csv, filas 61–64 y 75.** El contexto para practicar vocabulario básico depende de términos y situaciones especializados: seguro y equipo de feria, operación quirúrgica, prueba de motor y consumo de combustible, grabaciones de seguridad; investigadores que observan aves desde el amanecer; equipo que calibra sensores y mediciones; equipo de rescate tras un terremoto, factura desglosada, técnico de calefacción y reunión de admisión. La carga de vocabulario distrae del objetivo de la unidad y no corresponde bien al plan de intercambios cotidianos A1.

   **Cambio requerido:** reemplaza esos ejemplos por situaciones familiares y vocabulario básico, conservando el término objetivo de cada fila, la equivalencia y una duración/condición concreta cuando se practique `a period of time`.

### Prioridad baja — consistencia de variedad del inglés

6. **A1-S001 a A1-S005, varios ejemplos.** Se mezclan convenciones británicas y estadounidenses sin un patrón declarado: por ejemplo, `neighbour`, `colour`, `centre`, `car park`, `film` y `organise` junto a `yogurt`, `colored`, `color` y `cell phone`.

   **Cambio requerido:** aplica una variedad coherente a los cinco archivos —o señala explícitamente las variantes cuando sean pedagógicamente intencionales— y normaliza ortografía y vocabulario correspondientes.

## Acción requerida

Corregir únicamente los cinco CSV auditados para la iteración global 19. Mantener 150 pares por archivo, cinco ejemplos claros por cada una de las doce unidades nuevas, los repasos 12/12, 30 filas gramaticales y los totales de integración previstos. Volver a validar los bytes UTF-8, el formato CSV y las filas señaladas, además de verificar equivalencia y consistencia entre sesiones.
