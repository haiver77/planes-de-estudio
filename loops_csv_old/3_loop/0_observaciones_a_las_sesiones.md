# Auditoría lingüística y técnica — A1, iteración 2

**Plan aprobado:** `loops_plan/12_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**CSV examinados:** `loops_csv/2_loop/A1/`  
**Mínimo:** 150 pares por archivo

## Resultado

**NO COMPLETO. Se requiere una nueva iteración y una revisión integral de los contenidos; no basta con corregir únicamente los ejemplos de este informe.** Hay problemas de equivalencia, gramática, uso contextual y duplicación en distintas sesiones, incluso en archivos no señalados anteriormente.

## Comprobaciones automáticas

- **Cobertura:** el plan contiene 107 ID A1 y hay 107 CSV válidos, exactamente uno por ID, sin faltantes ni ajenos.
- **Cantidad:** los 107 archivos tienen 150 filas cada uno; cumplen el mínimo numérico.
- **Formato:** los 107 se decodifican como UTF-8 y se analizaron con lector CSV estricto: dos campos por fila, separados por `;`; sin filas/campos vacíos, campos extra, comillas mal cerradas, saltos de línea incrustados ni `;` dentro de campos. No se detectaron CSV delimitados por coma.
- **Caracteres:** no se detectó texto corrupto (`Ã¡`, `Ã±`, `�`) ni preguntas españolas con `?` sin `¿`. Los caracteres acentuados y signos se conservan correctamente.
- **Comparación de iteraciones:** solo `A1-S007.csv`, `A1-S031.csv`, `A1-S059.csv` y `A1-S107.csv` difieren de sus homólogos de `1_loop`; los otros 103 son idénticos byte a byte a la iteración anterior. Esto no es por sí solo un defecto en cada archivo, pero confirma que no se aplicó una revisión amplia y que los problemas pendientes no se limitaron a los ejemplos anteriores.

## Observaciones priorizadas

### P1 — Sentido, colocaciones y naturalidad incorrectos; corregir todos los ejemplos de estos patrones

1. **`A1-S059.csv`, filas 31–35; `A1-S062.csv`, fila 79; `A1-S065.csv`, fila 91; `A1-S096.csv`, fila 148; `A1-S097.csv`, fila 141; `A1-S098.csv`, fila 134; `A1-S099.csv`, fila 127.** Se usa *include* con `with my family` como si significara “estar/incluirse con mi familia”: por ejemplo, S059 fila 31, «Me incluyo con mi familia todas las mañanas» / “I include with my family every morning”; S065 fila 91 incluso traduce «Los niños vienen con mi familia…» por “The children include with my family…”. Son construcciones incorrectas y, en un caso, no equivalentes. Reescribir con el sentido transitivo de *include* y un objeto apropiado (p. ej., incluir a alguien en una actividad/lista), o elegir otro verbo si el sentido previsto es pasar tiempo/ir con la familia. Revisar todas las apariciones, no solo S059.

2. **Adjetivos y artículos mal aplicados:**
   - `A1-S059.csv`, filas 46–55: “The room is interested today” (46), “My new bag is interested” (47), “That is a interested place…” (48), “My friend has a interested bicycle” (50) y “That is a interesting place…” (53), “a interesting bicycle” (55). Se atribuye interés a objetos y se usa *a* ante vocal. Corregir el sentido (persona interesada frente a cosa interesante), la concordancia semántica y *an*; no forzar el adjetivo sobre cualquier sustantivo.
   - Repetición fuera del archivo señalado: `A1-S060.csv`, fila 70, y `A1-S065.csv`, fila 94: “The room is interested today”. `A1-S062.csv`, filas 82–83, repite los errores “a interested” y “a interesting”. Corregir todas estas ubicaciones.
   - `A1-S034.csv`, filas 36 y 38: “The room is bored today” y “That is a bored place for lunch” traducen «aburrida/aburrido» como si el lugar experimentara aburrimiento; corresponde expresar que son aburridos (*boring*) o reformular. El error se repite en `A1-S035.csv` fila 68, `A1-S040.csv` fila 92 y “a bored place” en `A1-S037.csv` fila 80 y `A1-S053.csv`–`A1-S056.csv` (filas 150, 143, 136 y 129, respectivamente). Revisar todas las instancias y no cambiar únicamente la forma inglesa.

3. **Cuantificador y frase incompleta:** `A1-S064.csv` fila 22 y `A1-S102.csv` fila 104, `A1-S103.csv` fila 85, `A1-S104.csv` fila 78, `A1-S105.csv` fila 59 y `A1-S106.csv` fila 52: «Veo mucho en la mesa» / “I see lot at the table”. En inglés falta el determinante y *a lot* necesita un referente/complemento o una construcción existencial adecuada. Reformular ambos lados con un objeto/sentido claro y equivalente, por ejemplo especificando qué se ve sobre la mesa.

4. **Plantilla con alternativas incrustadas y uso no comunicativo:** `A1-S004.csv`, filas 1–5 y 123; `A1-S005.csv`, filas 61 y 116; `A1-S007.csv`, fila 73; `A1-S010.csv`, fila 85 contienen `away from my friend/the book` (y plantillas paralelas como `bad for my friend/the book`). La barra deja una frase sin decidir, no es una unidad usable como modelo; además, en S004/S007 se repiten marcos metalingüísticos de “leer/explicar/oír la expresión” en vez de practicar el sentido de las unidades. Reescribir cada fila como escena concreta, elegir un solo referente y emplear colocaciones naturales.

5. **`A1-S007.csv`, filas 1–40 y bloques posteriores de vocabulario, incluido 71–75:** aunque las traducciones de las filas 41–45 citadas previamente ahora son naturales, el archivo conserva una serie metalingüística masiva: ejemplos como fila 31 «Leo la expresión “get on” en la página» / “I read the phrase ‘get on’ on the page” no enseñan el sentido de *get on*. El patrón de cinco marcos repetidos por expresión ocupa 99 de las 150 filas según búsqueda automatizada; la fila 73 contiene además la alternativa inválida indicada arriba. Practicar cada unidad en su sentido/categoría y colocación propia, con contextos independientes y naturales; eliminar el relleno de plantilla de todo el CSV.

6. **`A1-S031.csv`, filas 31–60 y restantes bloques léxicos:** las frases vuelven al patrón mecánico «está en la foto / leí sobre… / oigo la expresión… / mi maestra habla… / aprendo sobre…». Ejemplo: fila 33 «Oigo la expresión “a ball” en una conversación en la tienda»; filas 46–50 fuerzan `bank (money)` en escenas de foto, lectura y conversación. Además, filas 51–60 repiten la misma frase española «El baño está en la foto» y «Leí sobre un baño…», traducidas una vez con *bath* y otra con *bathroom*, sin contexto que desambigüe el sentido. Aunque el bloque inicial de *autumn/away* citado anteriormente está corregido, el resto sigue sin cubrir el objetivo de cinco pares naturales por unidad. Sustituir estos marcos por microescenas adecuadas, distinguir sentidos con contexto y retirar traducciones dobles ambiguas.

7. **Errores de demostrativos y estructura:** `A1-S100.csv`, filas 117–120: «Cerca de la estación hay una manzana» / “Near the station, this is an apple” y sus variantes `that/these/those`. La estructura española es existencial, no demostrativa; no se corresponden los pares y se mezclan singular/plural y distancia sin apoyo contextual. Reformular cada fila como existencia (*There is/are…*) o como demostración (*This/That is…* / «Esta/Esa es…»), según el objetivo de la unidad.

8. **`A1-S021.csv`, filas 51–60:** las frases repiten “digo ‘hay’ al cajero” / “I say ‘there is/there are’ to the cashier” y no practican un intercambio real. Las filas 51 y 56 tienen español idéntico con traducciones distintas (*there is* frente a *there are*), y 53/58 repiten el mismo problema; «los hay/las hay» (57, 59) tampoco aporta un referente claro. Reformular enunciados con un sustantivo/contexto que determine singular o plural, y crear preguntas/respuestas realmente utilizables. Revisar las plantillas equivalentes de `A1-S022.csv`–`A1-S028.csv`.

### P2 — Duplicación, contradicciones y progresión insuficiente

- Se detectaron frases españolas repetidas con traducciones inglesas diferentes en **40 CSV**: `A1-S021`–`A1-S025`, `A1-S027`–`A1-S028`, `A1-S031`–`A1-S035`, `A1-S037`–`A1-S040`, `A1-S042`–`A1-S043`, `A1-S047`–`A1-S048`, `A1-S050`–`A1-S051`, `A1-S053`–`A1-S055`, `A1-S057`, `A1-S059`–`A1-S060`, `A1-S062`, `A1-S070`–`A1-S071`, `A1-S073`, `A1-S076`, `A1-S086`, `A1-S089`–`A1-S090`, `A1-S094`, `A1-S097`, `A1-S100` y `A1-S107`. Eliminar el duplicado o convertirlo en un contraste explícito en ambos idiomas; comprobar todas las filas repetidas, no solo los casos citados.
- Ejemplos: `A1-S033.csv` filas 11 y 16 repite «La habitación está mejor hoy» pero ofrece “The room is best today” frente a “The room is better today”; *best* no equivale a «mejor» en ese marco. `A1-S034.csv` filas 36/41 confunde *bored/boring*. `A1-S047.csv` fila 36 y `A1-S070.csv` fila 26 colocan a todos/nadie «en mi bolso» (“everyone/no one is in my bag”), contexto absurdo que revela sustitución mecánica. `A1-S100.csv` repite las estructuras demostrativas de filas 117–120 con cambio mínimo de pronombre.
- En distintos CSV se repiten cinco marcos casi idénticos por unidad sin progresión de longitud ni transferencia contextual. En particular S007 y S031 no respetan la exigencia del plan de microescenas independientes y naturales; además de reparar errores concretos, reconstruir los bloques para que haya recuperación espaciada útil, variedad, mini-secuencias y pares que funcionen por separado.
- `A1-S107.csv`: el ejemplo previo “I see lot…” y la contradicción de almuerzo nocturno citados para esa sesión ya no aparecen en las filas actuales; no obstante, filas 13 y 121 repiten «El domingo pasado cenamos en casa» con “We ate dinner…” / “We had dinner…”. Quitar redundancia o convertirla en contraste contextual real. El problema “I see lot” persiste en las seis sesiones indicadas en P1. No considerar el defecto resuelto globalmente mientras subsista en otros CSV.

## Cambio requerido

Revisar de nuevo **los 107 CSV**, no solo los cuatro que cambiaron respecto de la iteración anterior. Corregir todos los casos y patrones enumerados; validar cada par por sentido, situación, persona, tiempo, cortesía y naturalidad; comprobar los objetivos gramaticales y léxicos de cada sesión; retirar duplicados, alternativas con barra y marcos de relleno; preservar UTF-8, dos columnas separadas por `;` y al menos 150 pares. Después, volver a presentar A1 para auditoría integral. Se requiere otra iteración.
