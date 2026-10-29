# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración auditada:** `loops_csv/33_loop/`  
**Iteración de salida:** `loops_csv/34_loop/`  
**Plan aprobado:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo cotejado:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Criterios auxiliares:** `indicaciones_csv.md`, `contexto.md` y el informe completo de `loops_csv/33_loop/0_observaciones_a_las_sesiones.md`  
**Alcance exclusivo:** `A1-S001.csv` a `A1-S005.csv`. No se inspeccionaron ni modificaron otras iteraciones o `loops_csv_old/`.

## Evidencia técnica, cobertura y plan

- Los cinco archivos solicitados existen y corresponden a los cinco IDs del alcance en el plan; no hay ID faltante ni CSV ajeno dentro de ese conjunto.
- Se decodificaron los bytes con UTF-8 estricto y se analizaron con lector CSV estricto. Cada archivo tiene **150 registros** (750 pares en total), sin encabezado, dos campos no vacíos por registro, un `;` delimitador, una fila física por par y sin filas vacías, campos adicionales, comillas mal cerradas ni saltos de línea incrustados. No se usaron comas como delimitador.
- No se detectaron `�`, secuencias de mojibake ni `?` sustituyendo letras. Las preguntas españolas llevan `¿`; los signos `?` comprobados son cierres de pregunta válidos. Las columnas están en el orden español–inglés.
- No hay duplicados exactos de frase española ni inglesa dentro de un CSV o entre los cinco archivos.
- Cada sesión contiene las 12 unidades de vocabulario de introducción que le corresponden en el catálogo, con cinco ejemplos por unidad en las filas 1–60. Los bloques de repaso, gramática e integración tienen las cantidades y posiciones previstas: S001 60+0+30+60; S002/S003 60+12+30+48; S004/S005 60+24+30+36. Los eventos de repaso examinados corresponden a las unidades de las sesiones fuente indicadas en el plan. La práctica gramatical dedicada está en los bloques previstos: G01 (S001, 61–90), G02 (S002, 73–102), G03 (S003, 73–102), G04 (S004, 85–114) y G05 (S005, 85–114).
- La mayoría de las correcciones señaladas en el informe anterior sí aparecen resueltas: entre ellas S003-126, S004-57/58, S005-60 y las secuencias previamente observadas de S003/S004. **S002-147 conserva un problema de equivalencia**, descrito abajo. La revisión de esta iteración también encontró otros problemas que no estaban en el informe anterior.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta: equivalencia, naturalidad y claridad

1. **A1-S002.csv, fila 147 — no conserva exactamente la intención de la petición.**  
   `¿Tienes un momento para ayudarme con esta bolsa?;Is this a good time to help me with this bag?` La frase española pregunta si la otra persona puede dedicar un momento; la inglesa pregunta si el momento actual es oportuno. Son intenciones cercanas, pero no iguales, y esta diferencia ya se había señalado en el informe anterior. **Cambio requerido:** alinear las dos preguntas. Por ejemplo, conservar el español y usar `Do you have a moment to help me with this bag?`, con una petición igualmente cortés.

2. **A1-S003.csv, fila 119 — diferencia entre hábito y ocasión concreta.**  
   `Mi familia y yo cenamos juntos los fines de semana.;My family and I have dinner together at the weekend.` El plural español expresa una rutina; en inglés británico `at the weekend` suele apuntar a un fin de semana concreto. **Cambio requerido:** traducir el hábito como `at weekends` o cambiar el español a `este fin de semana` si se quiere hablar de una ocasión concreta.

3. **A1-S003.csv, fila 127 — colocación inglesa poco natural.**  
   `Tengo un paraguas azul para la lluvia.;I have got a blue umbrella for the rain.` `For the rain` no es una forma natural de expresar el uso previsto del paraguas. **Cambio requerido:** formularlo como paraguas para días lluviosos, por ejemplo `Tengo un paraguas azul para los días de lluvia.;I have a blue umbrella for rainy days.`

4. **A1-S003.csv, fila 105 — construcción inglesa torpe y contexto poco claro.**  
   `Tú llegas a la escuela el fin de semana para jugar un partido de fútbol.;You arrive at school at the weekend to play in a football match.` `Arrive at school ... to play in a football match` resulta forzado y deja sin aclarar por qué se va a la escuela el fin de semana. **Cambio requerido:** dar una escena cotidiana clara y reformular la finalidad de forma idiomática (por ejemplo, `to play a football match` o `for a football match`), manteniendo el foco léxico que corresponda.

5. **A1-S004.csv, fila 132 — pregunta sobre batería ambigua en inglés.**  
   `¿Tu teléfono móvil tiene batería?;Does your mobile phone have a battery?` La pregunta inglesa consulta si el aparato incorpora una batería; el español normalmente pregunta si todavía tiene carga. **Cambio requerido:** expresar carga disponible en ambas columnas, por ejemplo `¿Tu teléfono móvil tiene carga?;Does your mobile phone have any charge?`

6. **A1-S004.csv, filas 8–9 — colocación poco idiomática y repetición del mismo razonamiento.**  
   La secuencia `...es malo para el sueño de mi hermano / ...because it is bad for his sleep` fuerza una combinación poco natural y repite la misma explicación en dos frases contiguas. **Cambio requerido:** conservar el objetivo `bad for`, pero elegir una consecuencia o un complemento natural en inglés y hacer que la segunda frase aporte un ejemplo o resultado distinto, no una paráfrasis casi idéntica.

7. **A1-S001.csv, fila 20 — relación espacial poco clara.**  
   `Unos cuantos años son mucho tiempo para un niño en esta ciudad lejos de casa sin su familia.;A few years is a long time for a child in this town away from home without his family.` La acumulación `in this town / away from home / without his family` deja sin explicar dónde vive o está el niño y hace que la escena resulte contradictoria o ambigua. **Cambio requerido:** aclarar la situación con un contexto sencillo y coherente; conservar el objetivo `a few years` sin apilar referencias espaciales redundantes.

### Prioridad media: progresión A1, carga y frases autónomas

8. **A1-S001.csv, filas 29–30 — fragmentos y progresión débil.**  
   `¡Buena idea para la cena con mis amigos hoy en el parque!` / `¡Buena idea para la cena ... antes del partido!` y sus traducciones son fragmentos que presuponen una propuesta previa; la segunda añade solo otro marcador circunstancial. **Cambio requerido:** conservar `Good idea!` pero hacer que cada par funcione como intervención autónoma (por ejemplo, aceptar una propuesta y añadir una acción sencilla); que la segunda frase aporte información relacionada, no solo una circunstancia adicional.

9. **A1-S001.csv, fila 132 — léxico/contexto por encima del nivel y de la escena inmediata.**  
   `Mi grupo de teatro actúa en el centro comunitario unas cuantas veces al año.;My theatre group performs at the community centre a few times a year.` `Theatre group`, `performs` y `community centre` elevan la carga léxica de una frase de integración A1. **Cambio requerido:** reciclar la unidad con una actividad y un lugar familiares, usando vocabulario frecuente y una estructura breve.

10. **A1-S002.csv, fila 35 — progresión excesivamente larga y léxico abstracto.**  
    `Familias de todo el mundo ven el concierto en línea desde casa y animan a los músicos y envían mensajes de apoyo cuando termina la última canción.` / `Families ... cheer for the musicians, and send messages of support when the final song ends.` La frase acumula acciones, una subordinada y expresiones menos básicas (`messages of support`, `final song`). **Cambio requerido:** conservar `all over the world` con una escena cotidiana y limitar la extensión a una acción adicional sencilla.

11. **A1-S002.csv, fila 60 — densidad y vocabulario poco básicos para la quinta frase de la unidad.**  
    `Es fácil llegar a la estación hoy en autobús desde el centro antes del anochecer.;It is easy to arrive at the station today by bus from the city centre before nightfall.` La sucesión de tiempo, medio, origen y límite temporal, junto con `nightfall`, sobrecarga el ejemplo. **Cambio requerido:** reducir los complementos a una ruta clara y usar vocabulario A1 frecuente, manteniendo `arrive at`.

12. **A1-S003.csv, fila 37 — expresión de nivel superior para el foco y el nivel.**  
    `No estoy disponible para hablar en este momento.;I am not available to talk at the moment.` `Disponible / available` es más avanzado que el foco temporal y no se necesita para practicarlo. **Cambio requerido:** expresar la misma situación con una forma cotidiana y breve, como “no puedo hablar ahora”, conservando `at the moment` en el inglés.

13. **A1-S003.csv, fila 59 — redundancia y carga innecesaria.**  
    `Mi padre está en el trabajo hoy en la oficina con sus compañeros.;My father is at work today in the office with his colleagues.` `At work` e `in the office` repiten la ubicación, y `colleagues` añade léxico menos básico. **Cambio requerido:** quitar una de las dos ubicaciones y usar un referente familiar, manteniendo una oración natural.

14. **A1-S003.csv, filas 24–25 — frases largas para practicar una expresión espacial básica.**  
    La fila 24 combina clase de ciencias, explicación de un experimento y materiales para cada grupo; la fila 25 añade una fiesta, regalo y reacción. La extensión supera lo necesario para A1 y la primera introduce varias acciones en una sola frase. **Cambio requerido:** acortar ambas, usar una microescena familiar y progresar con un solo detalle útil por fila.

15. **A1-S003.csv, filas 138 y 145 — vocabulario de integración más avanzado que A1.**  
    Fila 138: `la banda saluda al público / the band waves to the audience`; fila 145: `el mostrador de devoluciones ... al final del pasillo / the returns desk ... at the end of the aisle`. `Audience`, `returns desk` y `aisle` son términos poco frecuentes para estas frases de integración. **Cambio requerido:** conservar la estructura espacial/temporal practicada con objetos y lugares cotidianos.

16. **A1-S004.csv, fila 22 — vocabulario abstracto y poco inmediato para `the bad things about`.**  
    `Las cosas malas de vivir lejos son los viajes largos y el gasto de transporte.;The bad things about living far away are the long journeys and transport costs.` `Long journeys` y especialmente `transport costs` aumentan la carga léxica y la abstracción. **Cambio requerido:** listar inconvenientes concretos y familiares con palabras A1.

17. **A1-S004.csv, fila 32 — contexto y vocabulario por encima de A1.**  
    `El taller comienza con una breve presentación.;The workshop begins with a short introduction.` `Workshop` e `introduction` son menos básicos y el contexto no es tan inmediato como los ejemplos de aula/casa de la misma unidad. **Cambio requerido:** conservar `begins with` en una escena cotidiana y sencilla, por ejemplo una clase que comienza con un saludo o una pregunta.

18. **A1-S004.csv, filas 71, 74, 129 y 131 — integración/repaso con carga léxica elevada.**  
    Fila 71: `run a book club at university`; fila 74: `dough ... before it goes in the oven`; fila 129: `lockers ... showers`; fila 131: `runs out of battery`. Son expresiones y objetos menos básicos que los necesarios para recuperar las unidades previstas. **Cambio requerido:** sustituirlas por microescenas familiares y verbos frecuentes, manteniendo el elemento de vocabulario que se está repasando en cada fila.

19. **A1-S005.csv, fila 5 — frase demasiado extensa para el foco `city centre`.**  
    `Después de llegar en tren, camino hasta el centro de la ciudad para visitar el mercado cubierto, comprar fruta fresca y tomar un café en la plaza antes de volver a la estación.` La quinta frase apila llegada, desplazamiento, tres acciones y regreso; además, `covered market` añade un término menos básico. **Cambio requerido:** dejar una escena breve con una o dos acciones cotidianas y cerrar la progresión sin una cadena de actividades.

20. **A1-S005.csv, filas 24–25 — escenarios y sintaxis demasiado complejos para `come into`.**  
    La fila 24 combina consulta, enfermera, temperatura y paciente; la fila 25 añade encargado, sala de reuniones, presentación e informe. La última frase introduce varios nombres menos básicos y dos acciones coordinadas. **Cambio requerido:** practicar `come into` con lugares y personas familiares, frases cortas y una sola acción clara por ejemplo.

21. **A1-S005.csv, filas 34–35 — repetición mecánica y complementos temporales acumulados.**  
    La frase sobre el ejercicio difícil para Ana en clase se amplía con `today`, `without the teacher's help` y `before the test`. La fila 35 añade un marcador temporal sin aportar una acción o consecuencia nueva. **Cambio requerido:** conservar `difficult for`, eliminar el detalle temporal redundante y hacer que la quinta frase amplíe el contexto de forma útil y sencilla.

22. **A1-S005.csv, fila 45 — frase de integración sobrecargada y con tiempos apilados.**  
    `Nos ayudamos unos a otros en clase con los deberes cada semana antes de los exámenes.;We help each other in class with homework every week before the exams.` `Every week` y `before the exams` se acumulan y no queda clara la relación temporal; la frase además contiene varios complementos. **Cambio requerido:** dejar un único marco temporal y una escena clara de ayuda mutua, manteniendo `each other`.

23. **A1-S005.csv, fila 50 — ejemplo de `ends in` innecesariamente complejo.**  
    La frase sobre las palabras `garden` y `ticket` termina explicando que el profesor las coloca en grupos distintos; la clasificación no se justifica y añade una cláusula prescindible. **Cambio requerido:** usar una frase más corta y autónoma sobre una sola palabra que termine en una letra, o explicar explícitamente una actividad sencilla de clasificación.

24. **A1-S005.csv, fila 83 — escena y léxico poco básicos en integración.**  
    `Los chefs comparten recetas de todo el mundo en el programa.;The chefs share recipes from around the world on the show.` `Chefs`, `recipes` y `on the show` introducen un contexto más especializado de lo necesario. **Cambio requerido:** reciclar la expresión con personas y una actividad cotidiana de casa/comida, en una oración A1 breve.

## Resultado

La estructura técnica, el mínimo de 150 pares, la cobertura de los cinco IDs y la distribución léxica/gramatical y de repaso coinciden con el plan en el alcance revisado. Sin embargo, persisten observaciones de equivalencia, naturalidad, claridad y adecuación/progresión A1; en particular, la diferencia de intención de A1-S002 fila 147 sigue pendiente. Corregir los puntos enumerados y volver a auditar únicamente A1-S001.csv a A1-S005.csv en `loops_csv/34_loop/`.
