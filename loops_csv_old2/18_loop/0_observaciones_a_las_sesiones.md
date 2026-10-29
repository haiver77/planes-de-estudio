# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración global 17

**Resultado: requiere correcciones; se necesita otra iteración global (18).**

## Alcance y referencias

Auditoría exclusiva de `A1-S001.csv` a `A1-S005.csv` en `loops_csv/17_loop/A1/`. Cotejo con `indicaciones_csv.md`, el plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv` y los informes aplicables previos, en particular `loops_csv/16_loop/0_observaciones_a_las_sesiones.md` y `loops_csv/17_loop/0_observaciones_a_las_sesiones.md`. No se auditó el resto del nivel ni se inspeccionó `loops_csv_old`.

## Evidencia técnica y cobertura

- Los cinco IDs solicitados están presentes, uno por archivo; no hay faltantes ni archivos ajenos entre los cinco examinados.
- Se validaron los bytes y el contenido con lectura UTF-8 estricta y un parser CSV estricto. Tamaños: S001 12 984 bytes; S002 13 941; S003 12 817; S004 13 842; S005 13 769. No hay BOM.
- Cada CSV tiene exactamente 150 líneas físicas y 150 registros: 750 pares en total. Todas las filas tienen dos campos no vacíos, sin encabezado, separados por `;`; no hay filas vacías, campos adicionales, `;` dentro de campos, comillas mal cerradas ni saltos de línea incrustados. La coma no se usa como delimitador.
- No se detectaron `Ã¡`, `Ã±`, U+FFFD ni otros marcadores de mojibake. Las preguntas españolas llevan `¿` y cierre `?`; los caracteres acentuados verificados se leen correctamente.
- No hay filas duplicadas literalmente dentro de un CSV ni entre los cinco archivos.
- Las filas 1–60 de cada sesión cubren las 12 unidades nuevas del catálogo con cinco pares por unidad (12 × 5). Los bloques de 30 pares gramaticales están en las posiciones previstas: S001-61–90 (G01), S002-73–102 (G02), S003-73–102 (G03), S004-85–114 (G04) y S005-85–114 (G05). El bloque G02 de S002 mantiene variedad de demostrativos, número, afirmación, negación y pregunta; no repite la plantilla superficial señalada en auditorías anteriores.
- Los bloques de repaso S002-61–72, S003-61–72, S004-61–72 y S004-73–84 cubren las 12 unidades previstas. S005-61–72 también recupera las 12 unidades de S004. **S005-73–84 no cubre las 12 unidades de S002**, según se detalla abajo.

## Observaciones históricas revalidadas

- **Corregido — A1-S004.csv, fila 69.** `Los dos semáforos se ponen en verde al mismo tiempo.;The two traffic lights turn green at the same time.` presenta una actividad/situación distinta de la salida matinal de S003-43, conserva equivalencia y utiliza *at the same time*.
- **Corregido — A1-S003.csv, fila 119.** `Mi familia y yo cenamos juntos los fines de semana.;My family and I have dinner together at the weekend.` conserva explícitamente la cena.
- **Corregido — A1-S005.csv, fila 61.** La traducción `far away from the city lights` es idiomática, incluye exactamente la secuencia *away from* y conserva el sentido del español.
- **Corregido — A1-S005.csv, fila 82.** El período de *a period of time* queda determinado: dos horas, de las tres a las cinco.

## Observaciones pendientes priorizadas

### Prioridad alta — cobertura incompleta del repaso

1. **A1-S005.csv, filas 73–84 — repaso de A1-S002 incompleto (11/12 unidades).** El bloque recupera *a little*, *a lot*, *a lot of sth*, *all day*, *all night*, *all over the world*, *anything else*, *anyone else*, *a period of time*, *around the world* y *arrive at*. No hay ningún par que practique **A1-S002-U03, *a lot to do***. En cambio, S005-74 (`...reduces ... energy a lot`) y S005-75/76 (`a lot of events/traffic`) vuelven a cubrir *a lot* o *a lot of sth*.

   **Cambio requerido:** sustituye una de las filas que duplica esas unidades por una frase autónoma y natural que use *a lot to do*, con traducción equivalente; conserva una recuperación distinta para cada una de las 12 unidades de S002 y verifica el reparto completo 12/12.

### Prioridad alta — adelanto gramatical

2. **A1-S005.csv, filas 21–25 — generalización del pasado simple antes de su introducción.** Las cinco filas usan *came into* en pasado simple: `He came into the room`, `The librarian came into the reading room`, `The students came into the classroom`, `The doctor came into the examination room` y `The owner came into the restaurant`. El plan de S005 introduce G05 y repasa G04; el pasado simple no se introduce hasta A1-S009 (G09). Aunque el catálogo incluye U05 como la frase fuente fija `He came into the room.`, cuatro ejemplos adicionales extienden el patrón a sujetos y contextos nuevos y lo convierten en práctica productiva anticipada.

   **Cambio requerido:** no generalices el pasado simple en este bloque; conserva, como máximo, la expresión fuente como unidad lexicalizada y reformula los otros ejemplos con objetivos ya introducidos. Si no puede respetarse la entrada del catálogo sin enseñar el objetivo posterior, señala y resuelve primero esa incompatibilidad de plan/catálogo; no des por cubierto el requisito gramatical con adelanto.

### Prioridad media — equivalencia

3. **A1-S005.csv, fila 118.** `El gerente anuncia malas noticias sobre el presupuesto del club.;The manager has bad news about the club budget.` El español afirma que el gerente **anuncia** la noticia; el inglés solo dice que **tiene** malas noticias, con cambio de acción/intención.

   **Cambio requerido:** alinea ambas versiones, por ejemplo, `The manager announces bad news about the club budget` o modifica el español para que exprese que el gerente tiene esas noticias.

## Conclusión

No aprobar todavía. La estructura, UTF-8, cantidad y cobertura de vocabulario nuevo cumplen; las tres correcciones específicas del informe anterior también quedaron resueltas. Quedan pendientes el repaso 12/12 de S005 y el adelanto del pasado simple, además de la equivalencia de S005-118. Corregir únicamente estos cinco CSV para la iteración global 18 y volver a auditar.
