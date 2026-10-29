# Informe de auditoría — `loops_plan_for_phrases/2_loop`

**Resultado: requiere otra iteración.** Se resolvieron la cuota forzada, el calendario de repasos y buena parte de la trazabilidad; sin embargo, quedan solapamientos comprobables con el plan base y las asignaciones siguen agrupando expresiones heterogéneas que no corresponden de forma consistente a los objetivos comunicativos declarados.

## Comprobaciones satisfactorias

- La huella SHA-256 de los bytes de `resources/Phrase List.txt` es `1372473C7CD5CBD6A6A6FA30A7ACC63723562FDFA4D182362BC25B31987C8756`, idéntica a la declarada en el plan. El archivo tiene 750 registros: A1 129, A2 379, B1 155, B2 57 y C1 30; no contiene C2 ni expresiones duplicadas exactas.
- Se cotejaron los rangos de las 31 sesiones con el número de registros por nivel. Cubren los 750 ordinales, sin huecos, solapamientos ni ordinales fuera de rango. El índice por nivel y ordinal, junto con la huella y la regla de orden, permite recuperar las entradas fuente asignadas.
- Las instrucciones fijan una fila única por objetivo, sin cuota de 150, sin repasos, sin variantes de relleno, y describen nombre de archivo, UTF-8, dos columnas sin encabezado, cobertura, duplicados, equivalencia y resolución registrada de marcadores. C2 se deja expresamente al plan base, que sí contiene sesiones C2-S01–C2-S06.

## Observaciones priorizadas

### 1. Alta — La regla de no duplicar con el plan base no se cumple en todas las asignaciones

- **Ubicación:** plan complementario, tablas A1-S01, A1-S05 y A2-S11; plan base, A1-S04, A2-S03 y C1-S03.
- **Evidencia:** el cotejo encontró coincidencias literales de expresiones asignadas: `would like` (PH-A1-127, A1-S05) está en la gramática foco de A2-S03 del plan base, y `not only` (PH-A2-264, A2-S11) está en la gramática foco de C1-S03. También hay solapamientos de construcción: el objetivo `there is` (PH-A1-114, A1-S05) frente a `there is/are` en A1-S04, y `a lot` (PH-A1-009, A1-S01) frente a `a lot of/much/many` en A2-S03. Por tanto, las formas/construcciones se trabajan también en la secuencia base, aunque el plan complementario diga que deben excluirse de allí y posponga el cotejo hasta antes de exportar.
- **Cambio requerido:** resolver ahora cada coincidencia en la asignación —no dejarlo como control futuro— y documentar el resultado canónico en el índice. Evitar que la misma expresión objetivo se produzca en los dos bloques; si se sostiene que una coincidencia gramatical del plan base no cuenta como objetivo repetido, distinguirlo explícitamente y delimitar qué se considera duplicación en la generación y aceptación de CSV.

### 2. Alta — La secuencia de rangos no forma grupos comunicativamente coherentes

- **Ubicación:** criterio de partición por ordinales y tablas de sesiones, en particular A1-S01–S03, A2-S01–S03 y B1-S01.
- **Evidencia:** la asignación sigue tramos consecutivos de la lista, pero los objetivos y subobjetivos no reflejan varios de sus elementos. A1-S01 promete cantidad, grado, capacidad y duración, pero agrupa, entre otros, `a good idea`, `at home`, `best friend`, `come on!` y `come true`; A1-S02 combina rutina/frecuencia con `each other`, `excuse me`, `for example`, `get married`, `good luck` y `good news`. A2-S01, cuyo foco es tipos, cantidades y opciones, incluye `accused of sth`, `aim to do sth`, `aimed at sb` y `all but`. B1-S01, sobre cambios, cantidades y relaciones en un proceso, reúne conectores temporales con `back sb/sth up`, `be charged with sth` y `break up`. En estos ejemplos, el rango por sí solo no permite inferir una escena común ni producir pares autónomos que practiquen el objetivo declarado.
- **Cambio requerido:** reorganizar los registros en grupos pequeños por función/escena real, o bien definir subobjetivos concretos que cubran cada grupo y reasignar expresamente cada expresión a uno de ellos. No basta con conservar un rango alfabético y añadir un objetivo general: cada sesión debe permitir producir una única frase natural por entrada sin mezclar artificialmente situaciones.

### 3. Media — Falta hacer explícito en la aceptación CSV el control de pronombres exigido por las indicaciones del proyecto

- **Ubicación:** «Lista de aceptación por sesión», especialmente el criterio 4, «Equivalencia y naturalidad».
- **Brecha:** `indicaciones_csv.md` exige que el español use el pronombre correcto y muestra como incorrectas las traducciones cuyo sujeto omitido hace ambiguo si se trata de «él» o «ella», o de quién realiza la acción. El plan comprueba naturalidad, equivalencia y referentes de marcadores, pero no nombra ni verifica expresamente esa condición. El control actual podría aprobar un par idiomático que no permite reconstruir el mismo sujeto que el inglés.
- **Cambio requerido:** añadir a la lista de aceptación una verificación explícita de que el sujeto y sus referentes quedan inequívocos en español y corresponden al inglés; exigir el pronombre explícito cuando su omisión cause ambigüedad, conforme a `indicaciones_csv.md`.

**Siguiente paso:** corregir las asignaciones duplicadas y la organización comunicativa, actualizar el control de pronombres y solicitar una nueva auditoría.
