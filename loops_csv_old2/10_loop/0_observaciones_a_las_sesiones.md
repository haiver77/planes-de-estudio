# Informe de auditoría — A1-S001 a A1-S005, iteración global 9

**Resultado: requiere correcciones; se necesita otra iteración.** Alcance exclusivo: `loops_csv/9_loop/A1/A1-S001.csv` a `A1-S005.csv`, plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`, `indicaciones_csv.md` y observaciones históricas pertinentes de `loops_csv/6_loop/`, `7_loop/`, `8_loop/` y el informe de n8 situado en `loops_csv/9_loop/0_observaciones_a_las_sesiones.md`. No se revisó el resto del nivel ni `loops_csv_old`.

## Evidencia técnica, cobertura y repasos

- Están presentes exactamente los cinco IDs pedidos, y concuerdan con las sesiones A1-S001–A1-S005 del plan. No hay ID faltante ni archivo ajeno dentro del alcance.
- Validación mediante lectura de bytes y `csv.reader` estricto: los cinco archivos decodifican con UTF-8 real (sin BOM), tienen exactamente 150 líneas físicas y 150 registros CSV cada uno (750 pares en total), dos campos por registro, sin encabezado, campos vacíos, filas en blanco, comillas mal cerradas, campos extra ni saltos de línea incrustados. El delimitador es `;`, no coma.
- No se detectaron `Ã¡`, `Ã±`, U+FFFD ni `?` sustituyendo letras. Los signos `?` detectados son cierres de pregunta; las preguntas en español conservan apertura `¿`. En particular, los bytes de `A1-S002.csv`, fila 67, contienen `está` codificado como `c3 a1` y no `est?`.
- En las filas 1–60 de cada archivo se verificaron las 12 unidades nuevas del catálogo, en bloques de cinco pares por unidad (12 × 5). Los lemas y sentidos se mantienen en general, incluido el lema de plantilla `He came into the room.` de S005-U05.
- Todos los eventos de repaso planificados cubren las 12 unidades respectivas: S002 61–72; S003 61–72; S004 61–72 y 73–84; S005 61–72 y 73–84. S002-67 recupera U07 con acento correcto y contexto coherente. La distribución y el total de 150 pares por sesión coinciden con el plan.
- No hay pares duplicados dentro de un CSV. Las coincidencias exactas entre archivos detectadas corresponden a los bloques de repaso léxico o gramatical previstos; no aparecen duplicados exactos fuera de esos repasos.

## Observaciones pendientes priorizadas

### Prioridad alta — construcciones gramaticales adelantadas

1. **`A1-S001.csv`, filas 8, 100 y 109.** La fila 8 usa `can` (`Puedo esperar… / I can wait…`); la 109 vuelve a usar `can` (`…puede ser… / …can be…`); y la 100 usa `Let’s meet…`, una petición imperativa. S001 introduce G01 y no G07 (modales/imperativos); el informe n8 ya había señalado que no se adelantaran `can` ni estructuras de G07. **Cambio requerido:** conservar los lemas de vocabulario con afirmaciones de `be` u otra formulación ya cubierta, sin `can` ni imperativo.

2. **`A1-S002.csv`, filas 3, 16, 32, 36–40, 43, 59, 109 y 147.** Persisten formas fuera de G02 y del repaso G01: `Would you like` (3), `There is` (16), pasiva `is heard` (32), preguntas/negaciones con `do/does` y `would` (36–38, 40, 43, 59 y 109), la estructura existencial `Is there…?` (39, G05) y `Can you…?` (147, G07). El informe n8 ya había requerido retirar el auxiliar `does` y `can` adelantados en S002; aunque se corrigieron las filas allí citadas, permanecen ejemplos del mismo tipo en estas filas. La fila 147, además, no expresa explícitamente “un poco de ayuda” en español. **Cambio requerido:** reescribir estas frases con la gramática introducida o repasada hasta S002; en la fila 32 usar voz activa (p. ej., `People hear that band’s music all over the world.`), y en la fila 147 alinear el sentido completo de “a little help” sin `can`.

3. **`A1-S003.csv`, filas 36, 110 y 124.** La 36 usa `cannot/can’t`, la 110 `Can you ask…?` y la 124 traduce `Veo…` como `I can see…`. S003 trabaja G03 y repasa G02; el modal G07 está adelantado. La fila 124 añade una modalidad no expresada en español. **Cambio requerido:** eliminar `can/cannot` y alinear ambas columnas, por ejemplo `Veo una taza azul junto al plato.;I see a blue cup next to the plate.`; reformular también 36 y 110 con gramática ya cubierta.

4. **`A1-S004.csv`, filas 26, 28 y 80.** Las filas 26 (`The match is cancelled…`) y 28 (`The flight is delayed…`) siguen usando pasiva, aunque el informe n8 ya pidió voz activa para practicar `because of` en S004. La 80 usa `can` (`Podemos comprar… / We can buy…`), modal G07 adelantado frente a G04. Las filas 101, 104 y 105 sí fueron corregidas, pero estas construcciones pendientes mantienen el mismo problema. **Cambio requerido:** cambiar 26 y 28 a presente simple activo y reformular 80 sin `can`, manteniendo el foco léxico.

5. **`A1-S005.csv`, filas 16, 27 y 66.** Las filas 16 (`Can you come into…?`) y 27 (`Can you see…?`) introducen `can`, no previsto hasta G07. En 27, además, el español pregunta si se ven diferencias, mientras que el inglés puede preguntar por capacidad; no queda idéntica la intención. La fila 66 (`The train is delayed…`) usa pasiva al repasar `because of`. **Cambio requerido:** reescribir 16 y 27 sin `can` y con intención paralela (p. ej., `¿Ves diferencias entre estas dos bolsas?;Do you see any differences between these two bags?`); convertir 66 a una formulación activa sencilla.

### Prioridad media — naturalidad y variedad

6. **`A1-S005.csv`, fila 45.** `Nosotros compartimos los gastos entre nosotros.;We share the costs with each other.` repite la reciprocidad en ambos idiomas y suena redundante. **Cambio requerido:** naturalizar, por ejemplo `Mi pareja y yo compartimos los gastos del viaje.;My partner and I share the travel costs.`

7. **`A1-S004.csv`, filas 101 y 103.** Ambas parejas repiten la misma plantilla y acción (`Cancelamos el partido… / We cancel the match because of…`), cambiando únicamente tormenta por nieve. No aportan dos contextos distintos de transferencia. **Cambio requerido:** sustituir una de las dos por un ejemplo contextual diferente que practique `because of`, sin duplicar la misma estructura y situación.

## Observaciones históricas verificadas

Se contrastaron las observaciones de los informes de las iteraciones 5, 6, 7 y 8 (este último alojado en `loops_csv/9_loop/0_observaciones_a_las_sesiones.md`). Están resueltos los errores de caracteres y equivalencia señalados (incluidos S005-25 y las filas citadas en n8: S001-74, S002-46/67, S003-89/90/96, S004-22/68 y S005-19/61/119); también están corregidas las observaciones anteriores de repaso incompleto, naturalidad de `arrive in`/`ask for`/`meet`, artículos, concordancia, traducciones de `bad thing` y duplicados exactos fuera de los repasos. Se comprobó que los cambios indicados expresamente en n8 para S001-44/52/102, S002-13/41/42/45, S003-4/8/45/48 y S004-101/104/105 sí están aplicados. No se repiten como fallos las observaciones históricas ya resueltas; sin embargo, hay ejemplos nuevos o remanentes del mismo tipo de gramática adelantada en las filas 1–5 señaladas arriba, por lo que la corrección histórica no está completa.

**Acción requerida:** corregir todas las filas enumeradas, mantener 150 registros por archivo y volver a validar bytes UTF-8, estructura, cobertura, repasos y equivalencia antes de solicitar otra auditoría.