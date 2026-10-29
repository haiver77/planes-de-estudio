# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**CSV auditados exclusivamente:** `loops_csv/36_loop/A1/A1-S001.csv` a `A1-S005.csv`  
**Plan aprobado:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo cotejado:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Criterios auxiliares:** `indicaciones_csv.md`, `contexto.md` e informes de `loops_csv/33_loop/` a `36_loop/`.

## Verificaciones técnicas y cotejo del plan

- La carpeta auditada contiene exactamente los cinco ID previstos, sin faltantes ni CSV ajenos.
- Se leyeron los cinco archivos con decodificación UTF-8 estricta y análisis CSV estricto. Cada uno tiene **150 registros** y 150 líneas físicas; todas las filas tienen exactamente dos campos no vacíos, sin encabezado. No se encontraron delimitadores incorrectos, campos extra, filas vacías, comillas mal cerradas, saltos de línea incrustados, punto y coma dentro de frases, marcas de pregunta española ausentes, `?` sustituyendo letras, secuencias de mojibake ni carácter de reemplazo. No hay duplicados exactos de frases españolas o inglesas. Se cumple el mínimo obligatorio de 150 pares.
- El catálogo asigna 12 unidades léxicas a cada sesión y están representadas en sus bloques iniciales. Los bloques gramaticales corresponden a los objetivos previstos: *be* (S001), artículos/demostrativos (S002), *have got* (S003), *present simple* con *do/does* (S004) y *there is/are* con cuantificadores (S005). La distribución general de bloques y repasos coincide con la prevista.
- Se comprobaron directamente los hallazgos de los informes anteriores. Se corrigieron, entre otros, S001-9, S001-19/20 y S001-115; S002-14/15 y S002-147; S004-10, S004-17/20 y S004-129/131; y la progresión de S005-3/5. Sin embargo, persisten o se reformularon de manera incompleta los problemas de progresión en S002-56/60 y S005-49/50, y continúa la redundancia señalada para S003-59/60.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta: equivalencia, claridad y progresión

1. **`A1-S003.csv`, filas 59–60 — observación anterior aún pendiente: redundancia y ampliación poco natural.**  
   La fila 59 ya dice `Mi padre está en el trabajo hoy.;My father is at work today.` La fila 60 repite la misma afirmación y acumula `en la oficina / in the office` además de `con sus compañeros / with his colleagues`; “at work” e “in the office” duplican la ubicación, y la extensión suena mecánica. **Cambio requerido:** mantener solo una ubicación y ampliar con un detalle concreto y sencillo, sin repetir la misma idea ni añadir vocabulario menos básico innecesario.

2. **`A1-S005.csv`, filas 49–50 — progresión previa no resuelta en sentido pedagógico.**  
   La fila 50 es más larga que la 49, pero añade un dato desconectado: `La palabra pen termina en n y el bolígrafo está en la bolsa.;The word pen ends in n, and the pen is in the bag.` Que un bolígrafo esté en una bolsa no explica ni amplía la práctica de *ends in*; las dos cláusulas quedan unidas solo formalmente. **Cambio requerido:** sustituir la segunda cláusula por una extensión relacionada con la letra o la palabra (por ejemplo, una comparación sencilla con otra palabra), conservando el inglés natural y haciendo que la última frase avance la secuencia.

3. **`A1-S001.csv`, filas 44–45 — referencia temporal y sujeto de la ampliación ambiguos.**  
   `Estoy de acuerdo con Ana sobre el viaje hoy en clase...` puede leerse como si “hoy” describiera el viaje, en vez de indicar cuándo hablan. En la fila 45, `antes de hablar con el profesor` se traduce como `before we speak to the teacher`, que explicita un sujeto plural que el español no fija. **Cambio requerido:** reordenar para dejar claro que la conversación ocurre hoy en clase y especificar quién hablará con el profesor en ambas columnas; mantener la frase autónoma y el foco *agree with*.

### Prioridad media: naturalidad, variedad y nivel A1

4. **`A1-S002.csv`, filas 56–60 — la quinta frase reinicia la progresión de *arrive at*.**  
   Las filas 57–59 construyen una misma escena de llegada a la estación, añadiendo primero el autobús y luego el origen desde el centro. La fila 60 cambia de destino y vuelve a una frase más corta: `Llegamos a la tienda antes del almuerzo.;We arrive at the shop before lunch.` **Cambio requerido:** hacer que la fila 60 continúe la situación de la fila 59 con un único detalle A1 adicional, o reordenar el bloque para que la información aumente de manera gradual hasta el cierre.

5. **`A1-S003.csv`, filas 22–25 — repetición de la misma acción y secuencia poco natural.**  
   Las filas 22, 23, 24 y 25 repiten que la profesora saluda/dice hola al comienzo de la clase. En la 23, además, lee un libro antes de saludar, orden poco natural en esta microescena; la 25 vuelve a repetir el saludo para añadir que abre el libro. **Cambio requerido:** conservar *at the beginning of* y la dificultad A1, pero variar las acciones de las frases contiguas y ordenar la secuencia de clase de forma lógica, sin repetir el saludo como plantilla.

6. **`A1-S003.csv`, fila 55 — acumulación temporal poco natural.**  
   `Estudio en la universidad este año con mi amiga por la tarde antes de los exámenes.;I study at university this year with my friend in the afternoon before the exams.` Apila año, tarde y periodo previo a exámenes; el presente simple con `this year` suena poco idiomático para una situación temporal en curso. **Cambio requerido:** reducir los marcos temporales a uno o dos y expresar de modo natural el periodo de estudio en ambas columnas, manteniendo el foco *at university*.

7. **`A1-S001.csv`, fila 129 — detalle de integración innecesariamente especializado para A1.**  
   `El cocinero guarda un poco de comida en la nevera para el turno de noche.;The cook keeps a little food in the fridge for the night shift.` La expresión `turno de noche / night shift` introduce un contexto laboral específico que no se necesita para reciclar *a little food*. **Cambio requerido:** usar un contexto cotidiano y vocabulario más frecuente, manteniendo la unidad léxica objetivo.

8. **`A1-S002.csv`, fila 148 — léxico abstracto/especializado en integración A1.**  
   `El fondo vecinal tiene un poco de dinero para reparar el parque infantil.;The community fund has a little money to repair the playground.` `Fondo vecinal / community fund` y la finalidad de reparación elevan la carga léxica y abstracta para una frase de repaso de *a little money*. **Cambio requerido:** conservar el cuantificador en una situación concreta y familiar (por ejemplo, dinero para un libro o una comida), con una traducción sencilla y equivalente.

## Conclusión

La cobertura, codificación, estructura y cantidad cumplen. No obstante, persisten hallazgos lingüísticos y pedagógicos —incluidos dos problemas de progresión ya señalados previamente— que requieren cambios y una nueva revisión. **NO COMPLETO; se requiere otra iteración.**
