# Informe de revisión independiente — Iteración 10

## VEREDICTO: NO COMPLETO

Se cotejaron los registros de Oxford 3000 con el PDF y el catálogo, las asignaciones y repasos con las 301 sesiones suplementarias, y la línea heredada con el catálogo de `9_loop`. La cobertura y la aritmética de capacidad son comprobables; sin embargo, la integración coloca las 3.306 entradas nuevas A1–B2 después de las doce sesiones C2, por lo que la secuencia completa no mantiene una progresión pedagógica A1–C2 coherente. Además, el límite de 150 pares está demostrado como volumen de archivo, pero no se justifica la carga temporal de práctica oral ni se operacionalizan los contextos naturales de cada grupo de vocabulario. Hace falta otra iteración.

## Conteos comprobados por nivel

Los conteos son **registros del PDF** (formas con nivel y categoría/acepción), no palabras ortográficas únicas. Las 22 coincidencias parciales se cuentan dentro de “nuevas asignadas”; no son aditivas ni se marcan como cubiertas.

| Nivel Oxford 3000 | Registros PDF | Cubiertos exactamente en la línea base | Solapamientos formales parciales | Nuevas unidades asignadas | Sesiones de introducción | Sesiones solo de repaso | Total de sesiones añadidas |
|---|---:|---:|---:|---:|---:|---:|---:|
| A1 | 900 | 0 | 9 | 900 | 75 | 6 | 81 |
| A2 | 871 | 0 | 9 | 871 | 73 | 6 | 79 |
| B1 | 809 | 0 | 3 | 809 | 68 | 6 | 74 |
| B2 | 726 | 0 | 1 | 726 | 61 | 6 | 67 |
| **Total** | **3.306** | **0** | **22** | **3.306** | **277** | **24** | **301** |

El PDF tiene 3.306 registros; el plan informa 2.990 encabezados distintos, pues hay encabezados repetidos entre niveles/acepciones y una etiqueta (`a, an`) contiene dos formas. No se han confundido esos registros con 3.306 formas ortográficas distintas. Los 22 solapamientos formales apuntan a unidades preexistentes y se distinguen por acepción/categoría o por ser un componente de una expresión: A1 8 con Oxford 5000 y `phone`/`phone number`; A2 9 con Oxford 5000; B1 3 con Oxford 5000; B2 1 con Oxford 5000. No se encontró coincidencia de entrada completa que el criterio de identidad del catálogo permita dar por cubierta. Los parciales permanecen como práctica nueva, lo cual evita atribuir equivalencia semántica solo por compartir grafía.

## Hallazgos priorizados

### P1 — Secuencia global invierte la progresión de niveles

- **Ubicación:** `1_plan_estudio_por_sesiones_de_repeticion.md`, sección “Orden global del suplemento” y tabla de sesiones de ampliación; `3_sesiones_oxford3000.csv`, órdenes globales 266–566.
- **Brecha:** las 265 sesiones heredadas terminan en C2-S012, orden 265. Las 301 sesiones nuevas empiezan en A1-S027, orden 266, y avanzan luego A2, B1 y B2. El alumno completa, por tanto, A1–C2 antes de estudiar las 3.306 unidades Oxford 3000 A1–B2. Mantener intactos los identificadores anteriores preserva trazabilidad, pero no resuelve este retroceso curricular.
- **Cambio requerido:** reubicar las cohortes nuevas dentro de sus tramos A1, A2, B1 y B2, o explicar y diseñar explícitamente el suplemento como curso separado que no se presenta como continuación cronológica del programa A1–C2. Al reordenar, recalcular y validar los destinos +1/+3/+6 de las unidades antiguas y nuevas para que sigan siendo sesiones posteriores reales y distintas. No basta con conservar los números actuales 266–566.

### P2 — Los objetivos genéricos no prueban todavía la naturalidad contextual de los pares

- **Ubicación:** `3_sesiones_oxford3000.csv`, campo `objetivo_comunicativo` de las 277 sesiones de introducción; textos fuente en `2_catalogo_trazabilidad_fuentes.csv`.
- **Brecha:** las sesiones reutilizan el mismo objetivo (“microintercambios inmediatos”, descripción/petición/pregunta/respuesta) para grupos de hasta 12 entradas heterogéneas. El PDF aporta principalmente lema y categoría gramatical, no traducción, definición ni contexto de uso. La instrucción de respetar sentido/categoría y producir cinco pares por unidad es útil, pero no especifica por sí sola el contexto que hará naturales y autónomos los pares de lemas polisémicos o con varias categorías. Por ello, la asignación es comprobable, pero la facilidad de convertir cada objetivo en pares naturales no queda demostrada para todo el inventario.
- **Cambio requerido:** concretar para cada cohorte (o cada unidad ambigua) situaciones, función comunicativa y sentidos/categorías que deben practicarse; conservar los cinco pares por unidad y permitir microcontextos separados cuando no haya un tema común natural. Añadir criterios verificables para que cada par español–inglés sea idiomático y utilizable por separado, sin leer etiquetas gramaticales o marcadores como parte de la frase.

### P2 — La carga oral está acotada por pares, no por tiempo ni reintentos

- **Ubicación:** sección “Cálculo verificable de capacidad” y reparto de pares de las sesiones suplementarias.
- **Brecha:** el volumen sí respeta el límite: cada una de las 301 sesiones contiene exactamente 150 pares; hasta 12 unidades nuevas × 5 pares = 60 pares nuevos, hasta 36 eventos de recuperación programada (máximo 12 unidades × +1/+3/+6), 30 pares gramaticales y al menos 24 de integración. En sesiones de introducción parcial o solo de repaso se destina el remanente a integración. Esto demuestra capacidad para generar el CSV de aproximadamente 150 líneas y evita excederla. No demuestra cuánto dura una sesión oral ni cómo influyen longitud, escucha, reconocimiento de voz, correcciones y reintentos, dado que el usuario debe pronunciar cada frase.
- **Cambio requerido:** declarar si 150 es un límite de generación o también una carga objetivo por sesión de estudio; incorporar una estimación o criterio de duración/segmentación que considere pronunciación y reintentos. Si 150 se mantiene como objetivo oral, justificarlo con la carga estimada y establecer cómo se evita que las frases largas y los errores de pronunciación vuelvan inviable el bloque.

## Evidencia de cobertura, asignación y repetición

- **Cotejo del PDF:** el archivo fuente tiene 12 páginas. Se validaron 3.306/3.306 registros de catálogo contra nivel, página, intervalo de línea y texto extraído del PDF; no hubo claves ausentes, textos discrepantes ni filas extra. Los conteos por nivel son A1 900, A2 871, B1 809 y B2 726; C1/C2 no están impresos en esta fuente.
- **Asignación:** las 3.306 filas tienen ID de unidad, sesión y ubicación de Vocabulario Foco; cada unidad figura en su sesión de introducción. No hay filas Oxford 3000 sin asignación.
- **Repasos nuevos:** para las 3.306 unidades, los destinos +1/+3/+6 existen y contienen el código de unidad en Vocabulario en repaso; no se detectaron errores de asignación. Los intervalos son sesiones posteriores y distintas dentro de cada bloque.
- **Conservación heredada:** las 3.013 filas de `9_loop/2_catalogo_trazabilidad_fuentes.csv` reaparecen con los mismos identificadores y campos en el catálogo v10 (3.013/3.013 idénticas). En particular, no se modificaron sus sesiones ni destinos de repaso.
- **Límite:** los 301 registros de `3_sesiones_oxford3000.csv` son únicos; los componentes de pares suman 150 en cada fila y ninguna sesión excede el máximo. Por nivel, las sesiones añadidas son A1 81, A2 79, B1 74 y B2 67. El plan reserva seis sesiones de cierre por nivel después de la última cohorte para completar los repasos de esa cohorte.

## Conclusión sobre suficiencia de sesiones

**En cantidad, la decisión de añadir sesiones es necesaria y el cálculo de capacidad está demostrado para el límite de pares:** las sesiones heredadas no se tratan como si tuvieran capacidad libre; con un máximo declarado de 12 unidades nuevas, hacen falta `ceil(900/12)=75` introducciones A1, `ceil(871/12)=73` A2, `ceil(809/12)=68` B1 y `ceil(726/12)=61` B2: **277 sesiones de introducción**. Añadir seis sesiones de cierre por cada nivel para los +1/+3/+6 de la cohorte final suma **24 sesiones más**, es decir **301 sesiones nuevas** y **566 en total**. El reparto de cada CSV respeta 150 pares. Por tanto, reducir la cantidad sin cambiar el tamaño de cohorte o sacrificar los repasos implicaría exceder el límite o dejar repasos pendientes.

**La suficiencia pedagógica global aún no está demostrada:** el calendario coloca esas 301 sesiones después de C2, invirtiendo la progresión A1–B2, y el límite de 150 pares no equivale por sí solo a una carga oral de duración validada. Corregir el orden y concretar contextos naturales y carga oral antes de declarar integración completa.
