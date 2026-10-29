# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración auditada:** `loops_csv/39_loop/A1/`  
**Informe de salida:** `loops_csv/40_loop/0_observaciones_a_las_sesiones.md`  
**Referencias cotejadas:** plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`, `indicaciones_csv.md`, `contexto.md` e informes `loops_csv/33_loop/` a `loops_csv/39_loop/`.  
**Alcance:** exclusivamente los cinco CSV A1 indicados.

## Comprobaciones técnicas, cobertura y cambios previos

- La carpeta contiene exactamente `A1-S001.csv`, `A1-S002.csv`, `A1-S003.csv`, `A1-S004.csv` y `A1-S005.csv`: coincide con los cinco ID previstos y no hay CSV ajenos en el alcance.
- Se leyeron los archivos con decodificación UTF-8 estricta y análisis CSV estricto. Cada uno tiene **150 registros y 150 líneas físicas**, sin encabezado. Todas las filas tienen exactamente dos campos no vacíos y un `;` delimitador. No hay filas vacías, campos extra, comas como delimitador, punto y coma dentro de las frases, comillas mal cerradas ni saltos de línea incrustados. Todas las preguntas españolas tienen `¿` y `?` de cierre. No se hallaron caracteres de reemplazo, mojibake ni `?` sustituyendo letras. No hay duplicados exactos de frases en español o inglés.
- Se cotejaron las 12 unidades léxicas asignadas a cada sesión y los bloques de repaso e integración. Se compararon además las filas de esta iteración con `38_loop` para revisar directamente todos los cambios. Varias observaciones anteriores ya están corregidas: entre otras, S001-45; S002-4/5 y 60; S003-37/40 y 49/50; S004-9/15/18; y S005-27/44/144. Los cambios previos sobre `have to`, `can`, el presente continuo anticipado y la pregunta de S005-90 también están resueltos en los archivos actuales. Las observaciones que siguen persisten o son defectos nuevos comprobados directamente.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta: fidelidad al plan y equivalencia

1. **`A1-S004.csv`, bloque gramatical, filas 85–114 — falta el repaso G03 previsto en el plan.**  
   El plan de S004 asigna G04 (*present simple*, *do/does*, preguntas y negación) y explícitamente repasa G03 (*have got/has got* y adjetivos posesivos, de S003). Las 30 filas del bloque gramatical actual practican present simple, pero en todo el CSV no aparece `have got` ni `has got` (tampoco sus formas negativas o interrogativas). **Cambio requerido:** incorporar en el bloque la práctica de repaso de G03 —formas afirmativas, negativas e interrogativas de *have got/has got* con posesivos correctos— y mantener también la práctica prevista de G04, sin adelantar gramática posterior.

2. **`A1-S002.csv`, fila 60 — el español añade el género femenino de quien habla.**  
   `Mi hermana y yo ... compramos los billetes juntas.` / `My sister and I ... buy the tickets together.` El inglés no especifica el género de la primera persona; `juntas` presupone que quien habla es mujer. **Cambio requerido:** retirar el adverbio con marca de género (por ejemplo, terminar en `... y compramos los billetes / ... and we buy the tickets together`) para conservar la equivalencia sin imponer información no expresada.

### Prioridad media: coherencia, naturalidad, progresión y nivel A1

3. **`A1-S004.csv`, filas 19–20 — persiste la repetición semántica observada en informes anteriores.**  
   La fila 19 dice que el suelo mojado es algo malo para los niños; la 20 vuelve a presentar el suelo mojado como algo malo y solo agrega que está en la entrada y que los niños caminan despacio. La segunda frase repite la misma escena y el mismo juicio en vez de avanzar con una idea distinta. **Cambio requerido:** conservar una sola frase sobre el suelo mojado y sustituir la otra por un inconveniente cotidiano diferente, con una consecuencia clara y breve.

4. **`A1-S001.csv`, filas 59–60 — orden poco natural en inglés y extensión que conserva la torpeza.**  
   `I have a little money for the bus today in my pocket.` La secuencia `for the bus today in my pocket` coloca los complementos de forma forzada; la fila 60 repite ese orden y solo añade `before I leave home`. **Cambio requerido:** reordenar ambos pares con naturalidad y hacer que la última frase amplíe la primera. Por ejemplo, usar `in my pocket` antes de `for the bus` y precisar que el dinero es para el billete.

5. **`A1-S001.csv`, fila 27 — relación lógica insuficiente en el bloque de `Good idea!`.**  
   `¡Buena idea! Mi hermana está en casa.;Good idea! My sister is at home.` La información de que la hermana está en casa no explica ni desarrolla qué idea se acepta, así que las dos cláusulas quedan yuxtapuestas sin nexo contextual claro. **Cambio requerido:** sustituir la afirmación por una acción o detalle que conecte explícitamente con la idea aceptada, manteniendo una intervención autónoma y vocabulario A1.

6. **`A1-S002.csv`, fila 24 — acumulación y complemento final poco natural para practicar `all day`.**  
   `La tienda está abierta todo el día hoy en el centro para los visitantes.;The shop is open all day today in the city for visitors.` Se apilan tiempo y lugar, y `for visitors` no aclara qué actividad se realiza en la tienda; el inglés suena poco idiomático. La fila 25 ya ofrece una continuación más clara con la gente que compra después del trabajo. **Cambio requerido:** simplificar la fila 24 a una escena breve (por ejemplo, la tienda está abierta todo el día) y dejar que la fila 25 aporte la ampliación relacionada.

7. **`A1-S005.csv`, fila 66 — colocación inglesa poco natural.**  
   `El tren llega tarde por la nieve que cubre las vías.;The train is late because of snow covering the tracks.` La construcción inglesa `because of snow covering the tracks` es pesada para este ejemplo y no reproduce con naturalidad el complemento español. **Cambio requerido:** emplear una colocación sencilla, como `because of snow on the tracks`, y ajustar el español a `por la nieve en las vías` para que ambos pares mantengan la misma formulación.

8. **`A1-S004.csv`, filas 145 y 150 — vocabulario de integración más específico de lo necesario para A1.**  
   `centro histórico / historic centre` y `plantas de interior / houseplants` añaden léxico menos inmediato que no hace falta para practicar `far from` y `bad for`. **Cambio requerido:** conservar las estructuras objetivo con sustantivos más frecuentes, por ejemplo `centro de la ciudad / city centre` y `plantas / plants`.

## Resultado

La cobertura de archivos, codificación, formato y mínimo de 150 pares cumple. Sin embargo, persisten una omisión del repaso gramatical prescrito y defectos de equivalencia, coherencia, naturalidad y progresión A1. Corregir los puntos indicados y solicitar una nueva revisión de estos cinco CSV en la iteración 41. **NO COMPLETO; se requiere otra iteración.**
