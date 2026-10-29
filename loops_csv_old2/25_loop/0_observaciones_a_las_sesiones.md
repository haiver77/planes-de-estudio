# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración global 24

## Alcance y comprobaciones

Se auditaron exclusivamente `A1-S001.csv` a `A1-S005.csv` en `loops_csv/24_loop/A1/`, frente a `indicaciones_csv.md`, el plan aprobado de `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, el catálogo de trazabilidad y las observaciones históricas aplicables. No se revisaron otros CSV ni `loops_csv_old/`.

- **Cobertura y cantidad:** los cinco IDs están presentes, sin faltantes ni ajenos. Cada archivo contiene 150 pares (750 en total), cumple el mínimo y presenta 12 unidades nuevas × 5 pares. Los bloques de repaso de 12/12, 30 posiciones gramaticales por sesión y las cantidades de integración concuerdan con el plan.
- **Bytes y CSV:** se inspeccionaron los bytes y se decodificó cada archivo con UTF-8 estricto. Tamaños: S001 12.874; S002 13.106; S003 12.615; S004 13.780; S005 13.409 bytes. Cada uno tiene 150 líneas físicas y 150 registros CSV de dos campos no vacíos, sin encabezado ni BOM. No se detectaron campos extra, filas vacías, delimitadores incorrectos, punto y coma dentro de frases, comillas inválidas, saltos incrustados, signos de interrogación españoles sin `¿`, mojibake, U+FFFD ni `?` sustituyendo letras. Los caracteres acentuados inspeccionados son correctos.
- **Consistencia:** no hay pares duplicados ni frases españolas o inglesas idénticas dentro de los 750 registros. Los objetivos del catálogo aparecen en los grupos nuevos previstos y el inglés conserva mayoritariamente la variante británica; `cell phone` se contextualiza expresamente como variante estadounidense.
- **Observaciones históricas revalidadas:** S002-46–50 contiene la unidad exacta `a period of time` en los cinco pares y usa construcciones sintácticamente variadas; no se marca como incumplimiento de cobertura ni como plantilla. S005-23 ahora expresa la perspectiva de llegada en español e inglés. S004-104 (`for cleaning`) es natural y conserva el sentido. También están diferenciadas las causas de S004-27/28 y el repaso de S005-74–76 sigue el orden U02–U04 previsto. Persisten los defectos concretos siguientes.

## Observaciones pendientes priorizadas

### Prioridad alta

1. **A1-S002.csv, fila 48 — equivalencia semántica y naturalidad.** `El viaje de vuelta es un periodo de tiempo para que los niños descansen.;The journey home is a period of time for the children to rest.` Identifica el viaje mismo como un periodo de descanso, en vez de decir que los niños descansan durante el trayecto. **Cambio requerido:** conservar explícitamente `a period of time`, pero expresar la relación con sentido, por ejemplo: `Los niños descansan durante un periodo de tiempo en el viaje de vuelta.;The children rest for a period of time on the journey home.`

### Prioridad media

2. **A1-S003.csv, fila 70 — colocación poco idiomática.** `Mi abuelo necesita un periodo de tiempo para regar las plantas cada mañana.;My grandfather needs a period of time to water the plants each morning.` La construcción resulta rígida para una rutina diaria A1 y no delimita el intervalo. **Cambio requerido:** formular la acción de manera natural, manteniendo el objetivo explícito y un marco temporal concreto; por ejemplo: `Mi abuelo pasa un corto periodo de tiempo regando las plantas cada mañana.;My grandfather spends a short period of time watering the plants each morning.`

3. **A1-S005.csv, fila 82 — formulación redundante y genérica.** `Los niños tienen un periodo de tiempo para jugar con sus amigos durante el recreo.;The children have a period of time to play with their friends at break time.` La referencia a “un periodo de tiempo” queda vaga y se solapa con “durante el recreo / at break time”. **Cambio requerido:** precisar que es un intervalo breve y evitar la repetición temporal, por ejemplo: `Los niños tienen un corto periodo de tiempo para jugar con sus amigos durante el recreo.;The children have a short period of time to play with their friends at break.`

4. **A1-S003.csv, fila 149 — equivalencia incompleta para `ask for`.** `Mi hija pide un lápiz prestado en la escuela.;My daughter asks for a pencil at school.` El español afirma que pide el lápiz prestado; el inglés no expresa que lo solicita para tomarlo prestado. **Cambio requerido:** quitar `prestado` para conservar `ask for`, por ejemplo: `Mi hija pide un lápiz en la escuela.;My daughter asks for a pencil at school.`

## Acción requerida

Corregir las filas señaladas en una nueva iteración global y volver a revisar su naturalidad y equivalencia, manteniendo la cobertura del catálogo, el mínimo de 150 pares y el formato validado.
