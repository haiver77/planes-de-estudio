# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración de entrada:** 30  
**Mínimo obligatorio:** 150 pares por CSV  
**Plan aprobado:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Alcance exclusivo:** `loops_csv/30_loop/A1/A1-S001.csv` a `A1-S005.csv`.

## Evidencia comprobada

- **Cobertura y cantidad:** existen los cinco CSV del alcance y no falta ningún ID solicitado. Cada uno tiene exactamente 150 pares (750 en total), por lo que cumple el mínimo. Se cotejaron 12 unidades nuevas por sesión, con cinco ejemplos por unidad (60 filas nuevas en cada archivo).
- **Bytes, UTF-8 y parser:** se leyeron los bytes reales y se decodificaron con UTF-8 estricto. No hay BOM. Tamaños: S001 13.865 bytes; S002 14.863; S003 14.201; S004 15.177; S005 15.461. `csv.reader` con `;` y modo estricto devuelve 150 registros por archivo. Cada archivo tiene 150 líneas físicas, una sola separación `;` por línea y dos campos no vacíos; no hay encabezado, campos adicionales, filas vacías, comillas mal cerradas ni saltos incrustados. No aparecen mojibake ni U+FFFD; las interrogaciones españolas llevan `¿` y no se detectó `?` sustituyendo letras.
- **Duplicados:** no hay pares, frases en español ni frases en inglés repetidos en el conjunto de 750 filas.
- **Distribución del plan:** se cotejaron los bloques en orden con los IDs de unidad y las matrices del plan. S001: 30 pares de G01 y 60 de integración; S002/S003: 12 de repaso, 30 gramaticales y 48 de integración; S004/S005: 24 de repaso, 30 gramaticales y 36 de integración. Los cuatro repasos contienen 12/12 unidades: S002 recupera S001; S003 recupera S002; S004 recupera S003 y S001; S005 recupera S004 y S002. Los bloques gramaticales contienen 30 pares cada uno y corresponden a G01–G05.
- **Observaciones de la iteración 30:** S005-50 ya es declarativa; S002-30 ahora justifica de forma verosímil que la luz siga encendida toda la noche y no apila marcadores temporales; S005-58 usa correctamente *neighbours*; S005-20 evita repetir *the kitchen* y conserva el regreso del trabajo y la entrada para cenar. Esos cuatro cambios quedan resueltos.
- **Revalidación del informe histórico n29:** se comprobó cada punto aplicable. Se corrigieron S001-24/25; S002-33–35 y 49/50; S003-23–25; S004-8–10, 34–35 y 44–45; S005-4/5 y 48–50. S005-57 ya expresa una actividad semanal natural. También siguen corregidos los puntos históricos sobre *a few times*, posesión con *have got*, y los contextos de S002-48/49, S003-70/105/149, S004-27/28/104 y S005-18/19/23/82. Sin embargo, permanece el adelanto de pasado simple en S005-21 y se detectan las observaciones de progresión indicadas abajo.
- **Progresión de las 60 filas nuevas por sesión:** cada grupo de cinco tiene exactamente cinco ejemplos y aumenta estrictamente en longitud en ambos idiomas, salvo A1-S005-U10 (filas 46–50): el inglés queda en 18 palabras tanto en la fila 49 como en la 50 y repite los mismos datos de Megan y Lucas. Además, la progresión semántica y la naturalidad requieren los cambios detallados a continuación.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta

1. **A1-S005.csv, fila 21 — pasado simple adelantado, ya señalado en el informe histórico n29.**  
   `Él entró en la habitación.;He came into the room.` usa pasado simple, aunque esta sesión introduce G05 y el plan reserva el pasado simple para A1-S009/G09. Las filas 22–25 del mismo bloque ya usan presente. **Cambio requerido:** mantener el objetivo léxico *come into* y convertir esta línea en una frase declarativa natural en presente, sin introducir el pasado simple.

2. **A1-S004.csv, filas 4–5 — equivalencia ambigua de *away from*.**  
   `Vivimos lejos de la escuela...;We live away from school...` traduce una distancia explícita en español con *away from school*, que en inglés también puede entenderse como estar ausente de la escuela; no expresa inequívocamente «lejos». **Cambio requerido:** reformular ambas filas para indicar distancia de forma idiomática en inglés (por ejemplo, *far away from school*) y conservar la misma escena rural en español e inglés.

### Prioridad media

3. **A1-S005.csv, filas 49–50 — progresión plana y repetición en *end in*.**  
   Ambas filas enseñan con los mismos nombres y las mismas letras (`Megan` termina en *n* y `Lucas` en *s*). La versión inglesa tiene 18 palabras en cada fila; la 50 solo cambia «la lista» por «el formulario» y reformula la posesión, sin añadir un ejemplo ni información significativa. **Cambio requerido:** conservar la estructura *end in*, pero dar a la fila 50 otro ejemplo verificable o una ampliación útil; hacer que aumente también la información y longitud en inglés.

4. **A1-S001.csv, filas 38–40 — construcción poco natural y repetición de la misma idea.**  
   `¡Esa es una buena idea para el sábado para toda la familia!;That is a good idea for Saturday for the whole family!` acumula dos complementos con *for* y no concreta cuál es la idea. Las filas 39–40 vuelven a proponer pasar el sábado en el parque con la familia, con ampliaciones de escaso valor. **Cambio requerido:** expresar una acción concreta como idea en ambas columnas y hacer que la última frase añada un detalle lógico, sin repetir la misma propuesta con más complementos.

5. **A1-S002.csv, fila 25 — marcador temporal redundante en la progresión de *all day*.**  
   `La tienda está abierta todo el día hoy... hasta la noche.;The shop is open all day today... until the evening.` «Todo el día» ya cubre la jornada hasta la noche; la fila 25 repite ese límite en lugar de aportar contexto nuevo. **Cambio requerido:** eliminar la repetición temporal o sustituirla por un detalle pertinente que amplíe la escena sin contradecir ni duplicar *all day*.

6. **A1-S003.csv, filas 28–30 — ejemplo improbable y ampliaciones de relleno en el grupo de *at the end*.**  
   `El título está al final del libro en la última página...;The title is at the end of the book on the last page...` presenta como contexto ordinario un título al final del libro y luego solo añade «para los lectores/de la historia», que no explica ni enriquece la escena. **Cambio requerido:** reemplazar la secuencia por ejemplos verosímiles de algo situado al final de un libro u otro referente y hacer que las ampliaciones aporten información útil.

7. **A1-S003.csv, filas 33–35 — plantilla repetida en *at the end of*.**  
   Las tres filas mantienen el mismo dibujo, la última página y el título; las filas 34–35 agregan «para los niños/en la biblioteca» sin transferencia contextual ni avance de significado. **Cambio requerido:** variar la situación en las filas 34–35 (por ejemplo, otro objeto o un evento que termine) y evitar alargar la misma oración solo con destinatarios o lugares accesorios.

8. **A1-S003.csv, filas 38–40 — orden poco idiomático y acumulación de circunstancias.**  
   `Estoy ocupado en este momento en la oficina con mi equipo antes de la reunión de esta tarde.;I am busy at the moment at the office with my team before this afternoon's meeting.` El orden inglés *at the moment at the office* resulta forzado; las dos últimas filas repiten el mismo contexto y solo añaden la reunión. **Cambio requerido:** reordenar ambos idiomas con una secuencia natural (lugar/equipo y momento) y hacer que la extensión aporte una acción o consecuencia concreta.

9. **A1-S003.csv, filas 49–50 — redundancia entre *at the weekend* y *this Saturday*.**  
   `Estoy libre el fin de semana ... este sábado...;I am free at the weekend ... this Saturday...` expresa dos veces el mismo marco temporal; la fila 50 solo añade «antes del viaje». **Cambio requerido:** conservar un solo marcador temporal y ampliar con un detalle de disponibilidad o plan que aporte información nueva.

10. **A1-S004.csv, filas 23–25 — tres variaciones mecánicas de la misma frase sobre el invierno.**  
    Las filas repiten que el frío y la lluvia son lo malo del invierno para los niños de la ciudad y solo agregan «durante enero» y «cerca de la costa». La acumulación deja la última formulación poco natural y no amplía de forma significativa *the bad things about*. **Cambio requerido:** mantener el foco léxico, pero variar la situación o los aspectos negativos y usar las extensiones para añadir información pertinente, no una cadena de complementos geográficos y temporales.

**Resultado:** quedan observaciones lingüísticas, de equivalencia, fidelidad gramatical y progresión. Corregirlas y volver a auditar únicamente A1-S001.csv a A1-S005.csv en la iteración siguiente.
