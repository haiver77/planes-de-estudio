# Auditoría integral A1 — generación 7

**Plan cotejado exclusivamente:** `c:\GIT\english-learning-program\planes_aprobados\oxford_phrase_list\plan_frases_oxford.md`  
**Lista de regresión consultada:** `loops_csv\7_loop\0_observaciones_a_las_sesiones.md`  
**Resultado:** requiere correcciones y otra iteración.

## Comprobaciones generales

- Cobertura correcta: están los nueve archivos previstos, exactamente una vez (`PF-A1-001` a `PF-A1-009`), sin IDs ausentes ni CSV adicionales.
- Conteos comprobados por lectura UTF-8 y análisis de registros: `001` 150; `002` 169; `003` 245; `004` 169; `005` 150; `006` 192; `007` 155; `008` 152; `009` 153. Todos alcanzan el mínimo explícito de 150 frases.
- Los nueve archivos decodifican como UTF-8 válido. Se comprobaron dos campos por fila, sin encabezado, separados por `;`; no hay filas vacías, campos extra, campos en blanco, comillas mal cerradas ni saltos de línea incrustados. Las columnas están en orden español–inglés. No se hallaron caracteres de reemplazo, patrones de mojibake ni preguntas en español sin `¿`.

## Regresión verificada

- **PF-A1-001, fila 135:** se corrigió `amigosí` por `amigos`.
- **PF-A1-004, filas 28–39:** se reemplazaron los imperfectos señalados por pasado simple y se eliminaron los marcos temporales incompatibles.
- **PF-A1-007:** están corregidos los imperfectos señalados (filas 2–4, 133 y 151), `inmediato` (136) y `estudian` (145).
- **PF-A1-008:** se corrigió la concordancia a `juntas` (filas 62–66) y se añadió la tilde de `Él` (filas 133 y 138).
- **PF-A1-009:** se corrigieron los errores anteriormente señalados en `hermano`, `televisión`, `estudia`, `niño` y `música`.
- Las correcciones puntuales anteriores no eliminan el patrón de variantes con prefijos contextuales arbitrarios que ya se había señalado: persiste de manera extensa en `PF-A1-002` a `PF-A1-009`, con nuevas frases que siguen siendo poco naturales, redundantes o incoherentes.

## Observaciones pendientes

### Prioridad alta — naturalidad, variedad y progresión

En las sesiones siguientes se replica sistemáticamente una frase base añadiendo `En casa`, `En el parque`, `Con mi familia` o `En la tienda`. En numerosos casos el prefijo no aporta una variación significativa ni una progresión, y algunas versiones resultan contradictorias o redundantes. Sustituir estos grupos por ejemplos realmente distintos, completos, naturales y utilizables por separado. Mantener al menos 150 filas válidas tras los cambios.

- **PF-A1-002 — `frases_PF-A1-002_v1.csv`:** 38 tríos de variantes con esos prefijos (114 filas). Ejemplo, filas 7–9: `Estoy un poco cansada` se repite como `En casa…`, `En el parque…` y `Con mi familia…` sin cambiar la situación ni practicar una función nueva. Revisar y sustituir todos los tríos, no solo el ejemplo.
- **PF-A1-003 — `frases_PF-A1-003_v1.csv`:** 51 tríos de variantes con esos prefijos (153 filas), además de una variante con `En la tienda`. Ejemplo, filas 120–122: `¿Hay otra persona en casa?` se antepone a `En el parque…`, que hace incoherente el lugar de la pregunta; filas 139–141 repiten la misma pregunta al médico con distintos prefijos sin aportar contexto. Rehacer los grupos de prefijos en toda la sesión.
- **PF-A1-004 — `frases_PF-A1-004_v1.csv`:** 36 tríos de variantes (108 filas). Ejemplo, filas 72–78: `Mi familia come en la playa` y `Vemos el mar desde la playa` se presentan también como `En casa…` y `En el parque…`; en la fila 74, `Con mi familia, mi familia…` es además redundante. Sustituir las variantes añadidas por frases pertinentes al foco.
- **PF-A1-005 — `frases_PF-A1-005_v1.csv`:** 32 tríos de variantes (96 filas) y otras tres filas con `En la tienda`. Ejemplo, filas 3–5: `En casa, llego a casa a las cinco` es redundante y `En el parque, llego a casa a las cinco` añade un marco que no ayuda a expresar el foco. Reformular estos grupos con contextos y situaciones diversos.
- **PF-A1-006 — `frases_PF-A1-006_v1.csv`:** 33 tríos con `En casa`/`En el parque`/`Con mi familia` y 35 añadidos con `En la tienda`. Ejemplo, filas 63–66: `En casa, ¡Oh, no! Mi libro está en casa` es redundante; la variante `En el parque… mi libro está en casa` introduce un contexto incongruente. Evitar también capitalización en minúscula de la exclamación autónoma de la fila 56 (`¡oh, no!;oh no!`); escribirla con mayúscula inicial en ambos idiomas.
- **PF-A1-007 — `frases_PF-A1-007_v1.csv`:** 63 filas con prefijos contextuales, muchos con `En la tienda`. Ejemplo, fila 29: `En la tienda, estoy en casa en este momento` se contradice directamente. Revisar todas las inserciones de ubicación, no solo esta fila.
- **PF-A1-008 — `frases_PF-A1-008_v1.csv`:** 85 filas con los mismos prefijos. Ejemplo, fila 82: `Con mi familia, quiero decir que la tienda está cerrada` carece de antecedente para `quiero decir`; las variantes de esta frase tampoco se vuelven autónomas por añadir un lugar. Reformular el grupo para que incluya un contexto aclaratorio natural en la propia frase o use una construcción independiente.
- **PF-A1-009 — `frases_PF-A1-009_v1.csv`:** 89 filas con prefijos contextuales. Ejemplos: filas 3–6 repiten `Es una buena idea llevar agua` con cuatro añadidos poco informativos; filas 124 y 126–129 aplican prefijos a `¡Qué pena! El parque está cerrado` o `Mi amigo no puede venir`, sin relación clara con el lugar y repitiendo el mismo esquema. Reemplazar los grupos por usos naturales y variados.

### Prioridad alta — ortografía y alcance gramatical

- **PF-A1-007 — `frases_PF-A1-007_v1.csv`, fila 129:** `Este año, estoy aprendiendo a cocinar` usa presente continuo, fuera de la gramática foco declarada para esta sesión (presente/pasado simple según el foco). Reformular con una estructura acorde al plan.
- **PF-A1-007 — `frases_PF-A1-007_v1.csv`, fila 145:** `El próximo año, mis amigos van a trabajar en otra ciudad` introduce `be going to`/`ir a + infinitivo`, estructura no incluida en la gramática foco declarada. Reformular conforme al plan aprobado.
- **PF-A1-009 — `frases_PF-A1-009_v1.csv`, fila 130:** `salir tempraño` contiene `ñ` en lugar de `n`. Corregir a `salir temprano`.

## Sesiones completas para omitir en la próxima validación

**PF-A1-001**. Las sesiones **PF-A1-002 a PF-A1-009** siguen pendientes de corrección y deben volver a validarse.

## Indicación al orquestador

Informe: `loops_csv\8_loop\0_observaciones_a_las_sesiones.md`. **Se requiere otra iteración** para corregir las observaciones pendientes de PF-A1-002 a PF-A1-009; PF-A1-001 puede omitirse en la siguiente validación.
