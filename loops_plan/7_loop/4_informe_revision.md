# Informe de revisión independiente — Iteración 7

**Archivos cotejados**
- `loops_plan/7_loop/1_plan_estudio_por_sesiones_de_repeticion.md`
- `loops_plan/7_loop/2_catalogo_trazabilidad_fuentes.csv`
- `loops_plan/7_loop/3_trazabilidad_correccion_C2.md`
- `loops_plan/6_loop/3_informe_revision.md`
- `resources/Oxford 5000_by CEFR level.pdf`
- `resources/Oxford Phrase List.pdf`

## Veredicto

**NO COMPLETO — hace falta otra iteración.**

La observación de la iteración 6 sobre los repasos gramaticales C2 sí está corregida: las 18 recuperaciones tienen destinos en sesiones posteriores distintas, en los intervalos indicados, y las sesiones C2 conservan el reparto declarado de 150 pares. Sin embargo, el cotejo directo del Oxford Phrase List revela dos ejemplos completos que el catálogo dividió en unidades independientes. Por ello, la cobertura léxica y sus conteos no son íntegramente fieles a las entradas de la fuente.

## Observaciones prioritarias

### Alta — Dos ejemplos del Oxford Phrase List están divididos en fragmentos y contados como entradas independientes

**Ubicación y evidencia en la fuente** (`Oxford Phrase List.pdf`, página 3, líneas de texto extraído):

- Líneas 25–26: `They say you can’t buy ` + `happiness.`. El catálogo los registra por separado como `OPL-A2-P03-L025` (“They say you can’t buy”) y `OPL-A2-P03-L026` (“happiness.”), ambos como introducciones nuevas en `A2-S019` (`LEX-00520`/`A2-S019-U01` y `LEX-00521`/`A2-S019-U02`).
- Líneas 46–47: `I had a kind of feeling this ` + `might happen.`. El catálogo los registra por separado como `OPL-B1-P03-L046` (“I had a kind of feeling this”) y `OPL-B1-P03-L047` (“might happen.”), ambos como introducciones nuevas en `B1-S001` (`LEX-00540`/`B1-S001-U10` y `LEX-00541`/`B1-S001-U11`).

En ambos casos, las líneas contiguas forman una sola frase de ejemplo en la extracción del PDF; los fragmentos finales no son unidades léxicas autónomas ni pares español–inglés naturales por separado. El catálogo además marca cada fragmento como unidad nueva, lo que duplica artificialmente la asignación y no conserva la entrada fuente completa.

**Cambio requerido:** en una nueva iteración, representar cada ejemplo completo como un único registro, con el intervalo de líneas 25–26 y 46–47 respectivamente; actualizar el texto crudo/normalizado, la identidad canónica y los códigos de unidad. Revisar las asignaciones de sesión y los repasos del catálogo afectados, junto con los conteos de registros y unidades, y comprobar que los repartos de pares siguen siendo correctos. No contar los fragmentos como entradas independientes.

### Media — La afirmación de cobertura y los conteos del Phrase List deben recalcularse tras corregir los registros

**Ubicación:** plan, “Recuento verificable de extracción y asignación”, totales del Phrase List y totales globales; catálogo, filas `OPL-A2-P03-L025`–`L026` y `OPL-B1-P03-L046`–`L047`.

El plan informa 1.001 registros y 1.000 unidades únicas del Phrase List. Al menos dos pares de filas identificados arriba representan dos ejemplos partidos, no cuatro entradas independientes. Por tanto, los conteos actuales no describen fielmente el conjunto de frases completas de la fuente y deben actualizarse después de corregirlos. La diferencia editorial entre el prefacio de 750 frases y las 1.001 líneas catalogadas está explícitamente reconocida en el plan; esta revisión no la trata como una equivalencia demostrada ni puede usarla para validar esos conteos sin depurar primero las entradas partidas.

**Cambio requerido:** recalcular y documentar los totales por nivel y globales a partir de registros que correspondan a entradas completas del PDF. Mantener explícita la diferencia con el recuento editorial del prefacio, sin presentarla como cobertura reconciliada.

## Comprobaciones satisfactorias

- **Repasos gramaticales C2:** la matriz ICOG asigna C2-G01–G06 a introducción, +1, +3 y +6 en sesiones distintas. La secuencia está numerada de forma consecutiva: C2-S001–S012 ocupan los órdenes 254–265. Los destinos son, respectivamente, C2-S002/S004/S007; C2-S003/S005/S008; C2-S004/S006/S009; C2-S005/S007/S010; C2-S006/S008/S011; y C2-S007/S009/S012. No se cuentan bloques dentro de la misma sesión como repetición espaciada. Los campos de sesión y los repartos C2 consignan 150 pares por sesión.
- **Catálogo e identificadores de sesión:** contiene 3.015 filas de datos y 3.015 identificadores de registro distintos; los 3.014 identificadores canónicos son distintos salvo el duplicado exacto documentado. Las 3.015 referencias de sesión existen en el plan. Los destinos de repaso léxico existentes se separan de la sesión origen por +1, +3 y +6 posiciones.
- **Duplicado:** `all over the world` permanece señalado como duplicado y vinculado a su introducción original; no se presenta como unidad nueva.
- **Estructura y carga del plan:** las sesiones identificadas contienen los campos de objetivo comunicativo, vocabulario foco, gramática foco y vocabulario en repaso; el plan explicita una generación de 150 pares por sesión y la reutilización en contextos nuevos. Las sesiones añadidas de integración C2 no introducen vocabulario atribuido a una fuente C2 inexistente.
- **Observaciones previas conservadas:** el plan mantiene la introducción explícita de *must* en B1-S003 y su recuperación en B1-S004, y sitúa los cuantificadores de A1 después de A1-S002. La reserva del informe anterior sobre las diferencias entre conteos editoriales y texto extraído sigue declarada.

**Conclusión:** la corrección C2 de la iteración 6 está verificada, pero no procede declarar completitud mientras los dos ejemplos partidos sigan registrados como cuatro unidades nuevas y los totales derivados no se hayan corregido.
