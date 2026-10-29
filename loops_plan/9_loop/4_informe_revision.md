# Informe de revisión independiente — Iteración 9

## VEREDICTO: COMPLETO

Se cotejaron el plan, el catálogo y la trazabilidad de la iteración 9 con los PDFs originales `resources/Oxford Phrase List.pdf` y `resources/Oxford 5000_by CEFR level.pdf`, además de revisar los hallazgos del informe de la iteración 8. No se editaron el plan ni el catálogo. La evidencia confirma que se preservan y asignan todas las entradas léxicas reales de ambos documentos; las dos observaciones pendientes de la iteración 8 están resueltas. No hace falta otra iteración.

## Evidencias y comprobaciones

### 1. Oxford Phrase List: cobertura completa y jerarquía visual

- Revisé visualmente las cuatro páginas renderizadas del PDF original. La página 1 declara “a list of 750 common phrases”. En todo el documento, la tipografía y la sangría distinguen las entradas principales (`MyriadPro-Regular`) de las líneas subordinadas (`MyriadPro-Light`).
- El catálogo contiene **999 registros completos**: **750 entradas principales y 249 subentradas/apoyos**. Verifiqué la asignación visual de cada registro contra el texto y la fuente tipográfica de la primera línea en el PDF: **999/999 coincidencias**, sin discrepancias de categoría. La distribución por nivel coincide con el documento: A1 200/103, A2 175/52, B1 175/57, B2 125/23 y C1 75/14 (principales/apoyos).
- El recuento de extracción es consistente: 1.017 líneas en las cuatro páginas, menos 12 líneas editoriales, deja 1.005 líneas de contenido. El catálogo cubre esas 1.005 líneas; seis continuaciones físicas se combinan con sus respectivas entradas, resultando en 999 registros lógicos. Cada texto bruto de catálogo coincide con las líneas fuente indicadas (**999/999**, sin ubicaciones inválidas ni fragmentos añadidos).
- Las seis continuaciones se conservan como entradas completas y con asignación real: `OPL-A1-P01-L130` (A1-S011-U05), `OPL-A1-P01-L166` (A1-S014-U04), `OPL-A1-P01-L222` (A1-S018-U11), `OPL-A2-P02-L269` (A2-S016-U12), `OPL-A2-P03-L025-026` (A2-S019-U01) y `OPL-B1-P03-L046-047` (B1-S001-U10). No se contabilizan sus líneas de continuación como unidades independientes.
- El duplicado `all over the world`, `OPL-A2-P02-L086`, se conserva como registro de fuente y repaso explícito en A2-S001. Enlaza a su unidad original A1-S002-U07; no crea una unidad nueva ni altera los 998 textos únicos del Phrase List.
- Por tanto, la discrepancia editorial del hallazgo alto de la iteración 8 queda reconciliada: 750 es el número de entradas principales que declara el prefacio, no el total de líneas subordinadas del listado. Los 249 apoyos adicionales se identifican por una regla visual reproducible, se preservan y no se presentan como parte de las 750 principales.

### 2. Errata “What are you plans for next year?”

- El cotejo visual de la página 1 confirma que el PDF imprime literalmente **“What are you plans for next year?”**; no es un error de OCR.
- El catálogo mantiene esa forma en `entrada_fuente_raw_pypdf` y normaliza la unidad `OPL-A1-P01-L222` como **“What are your plans for next year?”**, con explicación pedagógica. El plan la asigna a A1-S018, unidad A1-S018-U11, y muestra el par natural «¿Cuáles son tus planes para el próximo año?» / “What are your plans for next year?”.
- Los repasos de esa unidad permanecen en A1-S019, A1-S021 y A1-S024 (+1/+3/+6). La forma defectuosa no se enseña como modelo. Se resuelve así la observación media del informe de la iteración 8 sin ocultar la forma fuente.

### 3. Oxford 5000: cotejo, preservación y diferencia editorial

- Revisé visualmente las ocho páginas del PDF original. El catálogo conserva **2.014 registros con etiqueta gramatical**, B2: 700 y C1: 1.314. Los 2.014 textos brutos coinciden con las líneas y páginas citadas del PDF (**2.014/2.014 coincidencias**); no hay referencias inválidas, omisiones ni registros añadidos en el cotejo.
- No se eliminan entradas con categorías gramaticales distintas. Al retirar las etiquetas, quedan 1.999 grafías distintas; las 15 grafías duplicadas entre registros son `acid`, `alien`, `bat`, `craft`, `deposit`, `dynamic`, `extract`, `hook`, `intellectual`, `principal`, `spare`, `tackle`, `terminal`, `trace` y `trigger`.
- El titular del PDF habla de “additional 2000 words”. La diferencia entre ese titular editorial y los 2.014 registros etiquetados (o las 1.999 grafías distintas tras retirar etiquetas) está declarada en la trazabilidad: son bases de conteo distintas. Se conservan todas las filas reales del PDF sin inventar una entrada para forzar la cifra editorial. No se atribuyen niveles A1–B1 ni C2 a este documento.

### 4. Asignación a sesiones, repetición espaciada y límite de pares

- El catálogo reúne **3.013 registros fuente** (2.014 Oxford 5000 + 999 Phrase List) y **3.012 unidades únicas**. Las filas de unidades nuevas enlazan a una sesión real y a un código local cuyo número queda dentro del intervalo de Vocabulario Foco de esa sesión. La fila duplicada queda enlazada a la unidad original y a su repaso explícito.
- Comprobé los destinos léxicos +1/+3/+6 de las 3.012 unidades únicas: todos existen, están en sesiones posteriores distintas y corresponden a las posiciones indicadas; no encontré errores de asignación ni de intervalo.
- El plan presenta 265 sesiones consecutivas: A1 (26), A2 (19), B1 (20), B2 (71), C1 (117) y C2 (12). Cada fila incluye Objetivo Comunicativo, Vocabulario Foco, Gramática foco, Vocabulario en repaso y reparto de pares. Los objetivos dan contextos comunicativos para producir afirmaciones, preguntas, respuestas y negaciones autónomas; las plantillas `sb/sth`, `X` y `…` se explican como marcadores que deben sustituirse por elementos naturales, no leerse literalmente. Esto permite convertir los focos en pares español-inglés utilizables por separado.
- Las **265 sesiones** declaran un total exacto de **150 pares** y sus componentes permanecen dentro de ese límite. El criterio de producción reserva pares para unidades nuevas y repasos, mantiene el bloque gramatical de 30 pares e integra el remanente hasta 150; las sesiones de integración C2 distribuyen 30 pares gramaticales y 120 de integración/recuperación léxica.
- C2 no atribuye vocabulario nuevo a una fuente que no tiene sección C2. Sus seis focos gramaticales se introducen en C2-S001–C2-S006 y se recuperan con intervalos +1/+3/+6 en sesiones posteriores reales; la matriz identifica los 18 destinos hasta C2-S012. La recuperación léxica acumulativa B2–C1 continúa también en este tramo, incluidas las entradas C1 finales.

**Conclusión:** la cobertura fuente, la asignación, los repasos y la corrección pedagógica cuentan con evidencia suficiente. Las observaciones pendientes de la iteración 8 se resolvieron y no se requieren cambios adicionales para declarar completo el plan de la iteración 9.
