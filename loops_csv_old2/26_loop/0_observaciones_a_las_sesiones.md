# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración de entrada:** 25  
**Informe:** `loops_csv/26_loop/0_observaciones_a_las_sesiones.md`  
**Alcance:** exclusivamente `loops_csv/25_loop/A1/A1-S001.csv` a `A1-S005.csv`, frente al plan aprobado y el catálogo indicados. No se revisaron otros niveles ni `loops_csv_old/`. No se modificó ningún CSV.

## Evidencia y comprobaciones

- **Cobertura:** están los cinco IDs esperados, sin archivos faltantes ni ajenos. El catálogo contiene 12 unidades nuevas para cada sesión; cada una aparece en su bloque previsto de cinco pares.
- **Cantidad y parser:** los cinco CSV tienen exactamente 150 líneas físicas y 150 registros parseados con un lector CSV estricto, delimitador `;`, sin encabezado y con exactamente dos campos no vacíos por registro. Bytes por archivo: S001 12.874; S002 13.102; S003 12.608; S004 13.780; S005 13.407. Se cumple el mínimo de 150 pares en cada archivo.
- **Bytes, codificación y forma:** los cinco archivos se decodificaron desde bytes con UTF-8 estricto. No tienen BOM, filas vacías, campos adicionales, punto y coma dentro de frases, comillas mal formadas ni saltos de línea incrustados. No se detectaron `Ã...`, U+FFFD ni signos `?` sustituyendo letras; las preguntas en español llevan apertura `¿`. No se encontraron frases con comas usadas como delimitador.
- **Duplicación:** entre los 750 registros hay 750 pares distintos, 750 frases españolas distintas y 750 frases inglesas distintas. No se detectó duplicación literal.
- **Fidelidad de cantidades y colocación:**
  - S001: 60 nuevos (U01–U12 ×5), 30 gramaticales (filas 61–90) y 60 de integración (91–150); sin bloque de repaso por ser la primera sesión.
  - S002: 60 nuevos, 12 de repaso de S001 (61–72), 30 gramaticales (73–102) y 48 de integración (103–150).
  - S003: 60 nuevos, 12 de repaso de S002 (61–72), 30 gramaticales (73–102) y 48 de integración (103–150).
  - S004: 60 nuevos, 12 de repaso de S003 (61–72) y 12 de S001 (73–84), 30 gramaticales (85–114) y 36 de integración (115–150).
  - S005: 60 nuevos, 12 de repaso de S004 (61–72) y 12 de S002 (73–84), 30 gramaticales (85–114) y 36 de integración (115–150).
- **Repasos:** se cotejaron los 12 elementos de cada bloque con el orden previsto en el plan/catálogo; no se observan omisiones ni desplazamientos. En S005, filas 73–76 corresponden correctamente a S002-U01–U04, como se había indicado en el historial.
- **Objetivos y dialecto:** los bloques de gramática corresponden a G01–G05 por sesión. La alternancia `cell phone`/`mobile phone` está explicada y contextualizada como variante estadounidense/británica; el resto del inglés mantiene mayoritariamente el uso británico. No se detectó una contradicción de dialecto que requiera cambio.

## Revalidación de las cuatro observaciones anteriores

1. **A1-S002.csv, fila 48:** `Los niños descansan durante un periodo de tiempo en el viaje de vuelta.;The children rest for a period of time on the journey home.` La relación temporal queda explícita en ambos idiomas; equivalencia e idiomaticidad aceptables. La corrección no introduce otro defecto.
2. **A1-S003.csv, fila 70:** `Mi abuelo riega las plantas durante un corto periodo de tiempo cada mañana.;My grandfather waters the plants for a short period of time each morning.` La duración y la rutina se conservan; la colocación es aceptable y la corrección no crea un defecto nuevo.
3. **A1-S003.csv, fila 149:** `Mi hija pide un lápiz en la escuela.;My daughter asks for a pencil at school.` Ambas frases expresan la solicitud de un lápiz, sin añadir que se pide prestado. Equivalencia correcta.
4. **A1-S005.csv, fila 82:** `Durante el recreo, los niños tienen un breve periodo para jugar con sus amigos.;The children have a short period of time to play with their friends at break.` El intervalo breve y el recreo se conservan; la formulación es idiomática en español y equivalente al inglés. La omisión de «de tiempo» no cambia aquí el sentido de «breve periodo».

## Observaciones pendientes — requieren otra iteración

### Prioridad media

1. **A1-S002.csv, fila 49 — naturalidad y precisión.**  
   `El corte de electricidad dura un periodo de tiempo durante la tormenta.;The power cut lasts for a period of time during the storm.` La idea se entiende y las dos columnas concuerdan, pero «dura un periodo de tiempo / lasts for a period of time» resulta tautológico y no precisa el intervalo. **Cambio requerido:** especificar la duración sin perder el objetivo léxico, por ejemplo: `El corte de electricidad dura un corto periodo de tiempo durante la tormenta.;The power cut lasts for a short period of time during the storm.`

### Prioridad baja

2. **A1-S005.csv, fila 23 — repetición que resta naturalidad.**  
   `Estoy en el aula cuando la profesora entra en el aula antes de la clase.;I am in the classroom when the teacher comes into the classroom before the lesson.` La repetición de «el aula / the classroom» en ambas columnas hace que la frase suene poco natural, aunque comunica la perspectiva de llegada. **Cambio requerido:** eliminar la repetición conservando el sentido y el objetivo `come into`; por ejemplo: `Antes de la clase, la profesora entra en el aula donde estoy.;Before the lesson, the teacher comes into the classroom where I am.`

3. **A1-S003.csv, fila 105 — contexto sin motivación.**  
   `Tú llegas a la escuela el fin de semana.;You arrive at school at the weekend.` La traducción es equivalente, pero sin una actividad o motivo la llegada a la escuela durante el fin de semana queda poco contextualizada. **Cambio requerido:** añadir una razón breve que haga verosímil la visita (por ejemplo, un partido o un club escolar) en ambos idiomas, o cambiar el momento a un día lectivo.

**Resultado:** permanecen observaciones lingüísticas accionables; no se aprueba esta iteración. Se requiere corregir las filas 49 de S002, 23 de S005 y 105 de S003 y repetir la auditoría.
