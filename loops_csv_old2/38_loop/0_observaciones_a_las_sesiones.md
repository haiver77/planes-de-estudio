# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración auditada:** `loops_csv/37_loop/A1/`  
**Informe de salida:** `loops_csv/38_loop/0_observaciones_a_las_sesiones.md`  
**Plan:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Criterios auxiliares:** `indicaciones_csv.md`, `contexto.md` e informes de `loops_csv/33_loop/` a `37_loop/`.  
**Alcance:** solo `A1-S001.csv` a `A1-S005.csv` en `loops_csv/37_loop/A1/`. No se modificó ningún CSV ni archivo previo.

## Comprobaciones técnicas, cantidad y cobertura

- La carpeta contiene exactamente los cinco ID previstos (`A1-S001`–`A1-S005`), sin faltantes ni archivos ajenos en el alcance.
- Se leyeron los bytes y se validó UTF-8 estricto; un script de lectura CSV estricta confirmó **150 registros por archivo** y 150 líneas físicas por CSV (750 pares en total). Los cinco cumplen el mínimo explícito de 150.
- Todos los registros tienen dos campos no vacíos, sin encabezado, separados por un único `;`. No se detectaron filas vacías, campos adicionales, uso de comas como delimitador, comillas mal cerradas, saltos de línea incrustados, `;` dentro de frases, columnas invertidas, preguntas españolas sin `¿`, caracteres de reemplazo, mojibake ni `?` sustituyendo letras. No hay duplicados exactos de frases españolas o inglesas dentro de los archivos.
- Se cotejaron las unidades de vocabulario, los repasos y los objetivos de sesión con el catálogo y el plan. La cobertura general de los focos aparece; los hallazgos que afectan el uso de algunas filas se enumeran abajo.
- Se comprobaron expresamente observaciones anteriores: **S004-129/131** ahora dicen `Mis libros están en mi mochila.;My books are in my bag.` y `Mi teléfono está apagado en clase.;My phone is off in class.`, y corrigen las expresiones anteriormente señaladas. También están corregidas la redundancia de **S003-59/60**, la progresión de **S005-49/50**, la equivalencia temporal y el sujeto de **S001-44/45**, la secuencia **S003-22/25**, la intención de **S002-147** y la progresión de **S002-56/60**. La fila 45 de S001, no obstante, introduce un problema distinto de progresión (futuro) indicado abajo.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta: equivalencia y fidelidad gramatical

1. **`A1-S005.csv`, fila 94 — cambio de relación espacial.**  
   `¿Cuántas tazas hay sobre la mesa?;How many cups are there around the table?` «Sobre la mesa» indica que las tazas están encima de la superficie; `around the table` las sitúa alrededor de la mesa. **Cambio requerido:** usar `on the table` (`How many cups are there on the table?`) para conservar la ubicación española.

2. **`A1-S005.csv`, fila 99 — agente/acción no equivalente.**  
   `Hay mucho que hacer antes de abrir la tienda.;There is a lot to do before the shop opens.` El infinitivo español no especifica quién abre la tienda; el inglés atribuye la apertura a la tienda y cambia la relación. **Cambio requerido:** concretar una misma acción y agente, por ejemplo `Hay mucho que hacer antes de que abra la tienda.;There is a lot to do before the shop opens.` o `Tenemos mucho que hacer antes de abrir la tienda.;We have a lot to do before we open the shop.`

3. **`A1-S001.csv`, fila 45 — se adelanta una forma de futuro no prevista en el objetivo de esta sesión.**  
   `Hoy en clase, estoy de acuerdo con Ana sobre el viaje y yo hablaré con el profesor después de clase.;Today in class, I agree with Ana about the trip, and I will speak to the teacher after class.` El plan asigna S001 a pronombres y *be*; el uso de `hablaré / will speak` introduce futuro simple en esta sesión inicial (el plan posterior sí incluye objetivos futuros, entre ellos *be going to*). **Cambio requerido:** mantener *agree with*, pero sustituir la cláusula futura por una extensión con formas ya introducidas en el nivel/sesión, o trasladar la práctica del futuro a su bloque planificado.

### Prioridad media: naturalidad, nivel A1 y progresión

4. **`A1-S004.csv`, filas 4–5 — ubicación acumulada y equivalencia imprecisa en el cierre de *away from*.**  
   La fila 4 dice `Vivimos lejos de la escuela en el campo, cerca del río y del parque.`; la 5 repite todo y añade `a las afueras de nuestro pueblo / outside our town`. Se apilan «en el campo», «cerca del río y del parque» y «a las afueras» sin aportar una acción nueva; además, `outside our town` significa fuera del pueblo, no necesariamente en sus afueras. **Cambio requerido:** acortar las dos frases, conservar una sola relación espacial clara y hacer que la última añada un detalle sencillo, usando `on the edge of our town` solo si esa ubicación es la intención.

5. **`A1-S004.csv`, fila 31 — artículo y colocación del ingrediente.**  
   `La receta comienza con cebolla.;The recipe begins with onion.` En este ejemplo contable, el inglés singular requiere normalmente un determinante y la traducción suena incompleta. **Cambio requerido:** alinear ambas columnas, por ejemplo `La receta comienza con una cebolla.;The recipe begins with an onion.`

6. **`A1-S004.csv`, filas 53–55 — carga léxica innecesaria para A1.**  
   La secuencia incluye `car park exit`, `vending machine` y `hire car`: `La máquina expendedora está junto a la salida del aparcamiento.;The vending machine is beside the car park exit.` y `El coche de alquiler está en el aparcamiento...;The hire car is in the car park...`. Son nombres compuestos menos básicos y no se necesitan para reciclar *car park*. **Cambio requerido:** reemplazar esos objetos por referentes cotidianos (coche, puerta, tienda) y conservar frases breves e independientes.

7. **`A1-S002.csv`, fila 27 — repetición léxica poco natural.**  
   `El tren nocturno funciona toda la noche.;The night train runs all night.` `Night` aparece dos veces en inglés y «tren nocturno / toda la noche» repite la misma información en español. **Cambio requerido:** conservar el foco *all night* con un sujeto no redundante, por ejemplo `El tren funciona toda la noche.;The train runs all night.`

8. **`A1-S005.csv`, fila 20 — frase demasiado cargada para la progresión A1.**  
   `Estoy en casa cuando mi hermano vuelve del trabajo y entra en la cocina para cenar.;I am at home when my brother gets home from work and comes into the kitchen for dinner.` La subordinada acumula llegada del trabajo, entrada a la cocina y finalidad, antes de que el estudiante haya consolidado *come into*. **Cambio requerido:** conservar una sola acción/contexto, con una oración más corta y autónoma que contraste con las frases previas.

9. **`A1-S005.csv`, filas 29–30 — definiciones abstractas y cláusulas largas para *differences between*.**  
   La fila 29 (`Las diferencias entre el té y el café son claras para los niños de esta clase cuando prueban ambas bebidas.`) acumula una explicación abstracta y una subordinada; la 30 (`Los niños de esta clase usan dibujos sencillos para mostrar a sus familias las diferencias entre el té y el café.`) añade otra finalidad con varios complementos. **Cambio requerido:** practicar la comparación con dos objetos familiares y una frase corta por fila; que la última amplíe con una diferencia observable, no con explicaciones sobre qué tan claras son o para quién.

10. **`A1-S005.csv`, fila 90 — no practica el patrón de existencia previsto en el bloque gramatical.**  
    `¿Tenemos manzanas?;Do we have any apples?` Es una pregunta correcta, pero usa *do we have* en vez del objetivo de *there is/are* y cuantificadores de la sesión. **Cambio requerido:** convertirla en `¿Hay manzanas?;Are there any apples?` para mantener el cuantificador y practicar el patrón asignado.

## Conclusión

La estructura, codificación, cantidad y cobertura de ID cumplen, y varias observaciones de los ciclos anteriores están resueltas. Persisten defectos de equivalencia, avance gramatical, naturalidad y adecuación/progresión A1 que requieren cambios. **NO COMPLETO; se requiere otra iteración.**