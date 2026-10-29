# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración global 23

## Alcance y comprobaciones

Se revisaron exclusivamente `A1-S001.csv` a `A1-S005.csv` en `loops_csv/23_loop/A1/`, frente al plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`, `indicaciones_csv.md` y los informes históricos aplicables disponibles en `loops_csv/` (21 informes de las iteraciones 2–23; no hay informe en `5_loop`). No se auditó otro nivel ni se consultó `loops_csv_old/`.

- **Cobertura:** existen exactamente los cinco IDs solicitados, sin archivos de sesión faltantes ni ajenos en la carpeta A1 de la iteración 23.
- **Bytes y estructura:** se leyeron los bytes reales y se decodificó cada archivo con UTF-8 estricto. Tamaños: S001 12.874 bytes; S002 13.030; S003 12.567; S004 13.788; S005 13.348. Cada archivo tiene 150 líneas físicas y 150 registros CSV, dos campos por registro, sin encabezado ni BOM. No se hallaron campos vacíos o extra, delimitadores por coma, punto y coma dentro de frases, comillas inválidas, saltos de línea incrustados, mojibake, U+FFFD ni `?` sustituyendo letras. Las preguntas españolas llevan `¿` y las preguntas de cierre conservan `?`.
- **Cantidad y distribución:** hay 750 pares en total; cada CSV contiene exactamente 150. Se verificaron 12 unidades nuevas × 5 pares por sesión y 30 pares gramaticales en cada sesión. La distribución coincide con el plan: S001 = 60 nuevos + 0 repaso + 30 G01 + 60 integración; S002 y S003 = 60 + 12 + 30 + 48; S004 y S005 = 60 + 24 + 30 + 36. Los cinco totales son 150.
- **Repasos:** S005, filas 73–84, recupera las 12 unidades de S002 en orden exacto U01–U12: U01 *a little sugar*, U02 *a lot*, U03 *a lot to do*, U04 *a lot of sth*, U05 *all day*, U06 *all night*, U07 *all over the world*, U08 *anything else*, U09 *anyone else*, U10 *a period of time*, U11 *around the world*, U12 *arrive at*. No hay desplazamiento en 74–76. También se comprobaron los otros bloques de repaso según las posiciones del plan.
- **Duplicados:** no se encontraron pares idénticos ni frases españolas idénticas entre los 750 registros.
- **Observaciones históricas revalidadas:** S005-21–25 contiene solo una cita fuente en pasado (fila 21) y cuatro ejemplos de *come into* en presente simple (22–25), sin más pasado; S003-107 ya practica correctamente *ask for* sin añadir “prestado”; S004-27/28 ofrece causas diferentes (tráfico y viento fuerte). S004-102/104 ya no utiliza *roadworks* ni *maintenance*; queda una observación de naturalidad en 104 abajo. Los puntos históricos corregidos no se vuelven a marcar. La inspección de los demás pares no reveló otra observación accionable.

## Observaciones pendientes priorizadas

### Prioridad alta

1. **A1-S002.csv, filas 46–50; A1-S003.csv, fila 70; A1-S005.csv, fila 82 — persisten la cobertura incompleta y la formulación rígida de *a period of time*.** En S002-48, `A period without rain helps the garden` no contiene la unidad exacta *a period of time*; por tanto, el bloque de cinco no ofrece cinco realizaciones inequívocas del objetivo. Además, S002-46 (`For a period of time after lunch...`), 49 (`...for a period of time during a storm`) y 50 (`After a period of time...`), junto con S003-70 y S005-82, siguen apoyándose en el mismo intervalo genérico y en marcos temporales rígidos o poco naturales para A1. **Cambio requerido:** asegurar que S002-48 practique literalmente *a period of time* y revisar el bloque completo y los dos repasos para que todos los usos sean idiomáticos, concretos y variados, sin repetir como relleno el molde “for/after a period of time”; conservar la equivalencia española y las unidades del plan.

### Prioridad media

2. **A1-S005.csv, fila 23 (bloque de filas 21–25, *come into*) — destino deíctico no explícito.** `La profesora entra en el aula antes de la clase.;The teacher comes into the classroom before the lesson.` está en presente simple y mantiene *come into*, pero no sitúa al hablante o interlocutor en el aula. Sin ese anclaje, no se puede distinguir de forma clara la perspectiva de llegada que justifica *come* frente a *go*. **Cambio requerido:** hacer explícita la presencia del hablante/interlocutor en el destino en español e inglés, por ejemplo: `Estoy en el aula cuando la profesora entra antes de clase.;I am in the classroom when the teacher comes in before class.` Mantener la cita fuente pasada únicamente en la fila 21 y el presente simple en las otras cuatro.

3. **A1-S004.csv, fila 104 — colocación poco idiomática en una frase de nivel A1.** `La piscina cierra los lunes por la limpieza.;The pool closes on Mondays because of cleaning.` se entiende, pero `because of cleaning` suena rígido en este contexto cotidiano. **Cambio requerido:** usar una construcción natural y sencilla, por ejemplo `La piscina cierra los lunes para limpiarla.;The pool closes on Mondays for cleaning.`; mantener el significado y el presente simple.

## Acción requerida

Corregir únicamente las observaciones de los CSV A1-S001 a A1-S005 en la siguiente iteración global, conservar los 150 pares por archivo y volver a verificar desde los bytes la cobertura léxica, los repasos, la gramática, la estructura y la equivalencia.