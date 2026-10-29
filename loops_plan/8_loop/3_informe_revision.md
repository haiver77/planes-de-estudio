# Informe de revisión independiente — Iteración 8

**Alcance:** plan de sesiones, catálogo CSV, trazabilidad de correcciones, hallazgos de `loops_plan/7_loop/4_informe_revision.md` y cotejo con `resources/Oxford Phrase List.pdf` y `resources/Oxford 5000_by CEFR level.pdf`.

## Veredicto

**NO COMPLETO — hace falta otra iteración.**

La corrección de las dos continuaciones señaladas en la iteración 7 está bien aplicada y no encontré otras continuaciones mal segmentadas en el cotejo integral de las entradas del Phrase List. La extracción y la trazabilidad a líneas fuente son verificables. No obstante, sigue sin reconciliarse la diferencia entre el recuento editorial de los PDFs y las unidades que el plan afirma contabilizar; además, una entrada que se trasladaría a las frases de aprendizaje es gramaticalmente anómala.

## Hallazgos prioritarios

### Alta — El recuento del Oxford Phrase List no está reconciliado con el propio PDF

**Ubicación:** `resources/Oxford Phrase List.pdf`, página 1, prefacio; plan, «Recuento verificable de extracción y asignación»; catálogo CSV, registros `OPL-*`.

El prefacio describe una lista de **750 frases**. El catálogo de esta iteración contiene **999 registros completos y 998 unidades únicas**: A1 303/303, A2 227/226, B1 232/232, B2 148/148 y C1 89/89 (registros/unidades). La diferencia frente a 750 es de 249 registros y 248 unidades. El plan reconoce la discrepancia, pero no determina qué contabiliza el total editorial ni por qué se deben tratar todas las filas extraídas como unidades del inventario. Por ello, la correspondencia línea por línea no demuestra por sí sola que el catálogo contenga exactamente el conjunto de unidades que la fuente declara.

**Cambio requerido:** documentar y justificar la unidad de conteo del PDF (incluidos ejemplos, variantes y expresiones) y reconciliar el total editorial con los registros/unidades del catálogo; si el prefacio no corresponde al contenido incluido, explicitarlo con evidencia de fuente suficiente. No presentar el inventario como conteo reconciliado hasta resolverlo.

### Media — Una entrada fuente está registrada con una forma inglesa no natural

**Ubicación:** Phrase List, página 1, líneas de texto extraído 222–223; registro `OPL-A1-P01-L222`, normalizado como `What are you plans for next year?`.

La unión de línea está correctamente hecha, pero la secuencia `you plans` no es gramatical en inglés estándar. Tal como está normalizada, puede pasar a la futura generación de frases y enseñar una forma incorrecta.

**Cambio requerido:** cotejar visualmente la entrada con el PDF. Si la fuente dice *your*, corregir la normalización conservando el texto crudo y las líneas fuente; si el error está en la propia fuente, documentar la errata y evitar que la forma defectuosa se use como modelo de producción.

## Comprobaciones verificadas

- **Dos continuaciones de la iteración 7:**  
  - Página 3, líneas 25–26: `They say you can’t buy happiness.` queda en un registro, `OPL-A2-P03-L025-026`, A2-S019, unidad `A2-S019-U01`.  
  - Página 3, líneas 46–47: `I had a kind of feeling this might happen.` queda en un registro, `OPL-B1-P03-L046-047`, B1-S001, unidad `B1-S001-U10`.  
  Los cuatro fragmentos previos ya no aparecen como unidades independientes.
- **Revisión integral de continuidad del Phrase List:** las 1.001 filas del catálogo anterior se reducen a 999: 997 filas permanecen iguales y cuatro fragmentos se sustituyen por dos registros compuestos. Cada uno de los 999 registros actuales coincide con el texto de sus líneas y página del PDF; no hallé referencias de página/línea inválidas ni otras separaciones incorrectas. Las otras cuatro entradas que abarcan varias líneas —página 1, líneas 130–131, 166–167 y 222–223; página 2, líneas 269–270— están registradas como entradas completas. Se cubren 1.005 líneas fuente de contenido; la línea no catalogada de la página 1 es la continuación del texto introductorio, no una entrada del listado.
- **Conteos y duplicado:** el catálogo tiene 3.013 registros en total y 3.012 IDs canónicos consecutivos; conserva un duplicado exacto, `all over the world`, enlazado a la introducción original y sin crear una unidad nueva. La distribución por nivel coincide con la tabla precedente del informe.
- **Oxford 5000 preservado:** los 2.014 registros del catálogo actual (B2: 700; C1: 1.314) conservan íntegramente los 2.014 registros de la iteración 7: no hay filas fuente perdidas o agregadas ni diferencias en texto crudo, nivel, página o líneas. Los IDs/códigos se reindexaron tras las fusiones del Phrase List. El PDF presenta el contenido como 2.000 palabras adicionales, mientras el catálogo cuenta registros con etiquetas de categoría gramatical; hace falta aclarar esa base de conteo antes de equiparar ambos totales.
- **Asignación y repetición:** existen 265 sesiones del plan, incluidas las 12 sesiones de integración C2. Las 3.012 unidades nuevas tienen destinos de vocabulario +1/+3/+6 en sesiones reales y separadas, y las referencias coinciden con sus posiciones; no se detectaron destinos inexistentes ni intervalos incorrectos. Las seis recuperaciones gramaticales C2 tienen 18 destinos +1/+3/+6 correctos en sesiones posteriores distintas. Las 265 filas de sesión declaran un reparto de 150 pares.

## Conclusión para el orquestador

Persisten la reconciliación del recuento del Phrase List y la validación de la entrada anómala. **Hace falta otra iteración.**
