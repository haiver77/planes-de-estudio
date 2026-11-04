# Generador de CSV para el aprendizaje de adverbios por repetición

## Objetivo

Generar archivos CSV para que un estudiante aprenda a comprender y usar un adverbio objetivo en contextos variados. Cada archivo debe centrarse en un adverbio o locución adverbial concreta, su sentido definido y, cuando sea útil, un tipo de uso. La sesión debe combinar recuperación activa, repetición espaciada dentro de la lista y frases naturales.

El objetivo no es memorizar una equivalencia aislada ni repetir una sola oración. Reutilizar el adverbio a intervalos, con verbos, sujetos o situaciones familiares diferentes. Variar lo suficiente para enseñar su uso, pero no añadir tantos elementos nuevos que el estudiante pierda de vista el objetivo.

## Elegir el tipo y el sentido

Antes de generar el archivo, determinar qué función cumple el adverbio en el uso objetivo. Las categorías siguientes ayudan a diseñar contextos y no siempre son excluyentes; algunos adverbios tienen más de una función o sentido. Elegir uno por archivo, salvo que el usuario solicite explícitamente una comparación.

- **Modo:** explica cómo ocurre una acción (`rápidamente`, `cuidadosamente`, `well`). Practicar con verbos compatibles y situaciones que hagan clara la manera de actuar. Distinguir adjetivos de adverbios (`rápido`/`rápidamente`, `good`/`well`) cuando sea relevante; no imponer una terminación adverbial que el idioma no use.
- **Tiempo:** indica cuándo o durante qué periodo ocurre algo (`hoy`, `pronto`, `recently`). Practicar con acciones y marcadores temporales naturales. Diferenciar sentidos que puedan confundirse, como `actualmente` y `actually`, o `lately` y `late`.
- **Frecuencia:** indica con qué regularidad ocurre algo (`siempre`, `a menudo`, `rarely`). Usar rutinas y verbos habituales. Practicar la posición típica en cada idioma y conservar el mismo sentido de frecuencia en la traducción, sin fingir que expresiones como `often` y `a menudo` siempre ocupan la misma posición.
- **Lugar o dirección:** indica dónde, hacia dónde o desde dónde (`aquí`, `afuera`, `nearby`). Asociar el adverbio con ubicaciones y movimientos comprensibles. No confundir un adverbio de lugar con una preposición o una frase preposicional.
- **Grado o cantidad:** modifica la intensidad o cantidad (`muy`, `bastante`, `almost`). Practicar con palabras o situaciones que acepte naturalmente. Mostrar su alcance: qué palabra o idea modifica. No usarlo con adjetivos, verbos o cuantificadores incompatibles.
- **Afirmación, negación o duda:** expresa polaridad o actitud (`sí`, `no`, `perhaps`). Usar diálogos o respuestas breves cuando ayuden a aclarar la función. Respetar la posición y las reglas de negación de cada lengua; evitar traducciones que cambien una posibilidad por una certeza.
- **Foco, inclusión o exclusión:** limita o destaca un elemento (`solo`, `también`, `even`). Usar frases con contexto suficiente para que se entienda qué elemento queda incluido, excluido o enfatizado. Si el foco cambia el significado al cambiar de posición, mantener un solo patrón por sesión o separarlo en archivos.
- **Conectores y adverbios oracionales:** relacionan ideas o expresan la postura del hablante (`however`, `fortunately`). Practicar solo si el nivel permite comprender las dos ideas relacionadas y los signos de puntuación correspondientes. No mezclarlos con adverbios de modo solo porque la palabra tenga terminación similar.
- **Interrogativos o relativos:** aparecen en preguntas o cláusulas (`dónde`, `when`). Incluirlos únicamente cuando ese sea el objetivo solicitado; diseñar preguntas o estructuras subordinadas adecuadas al nivel y distinguirlos de sus usos no interrogativos cuando la ortografía o el sentido cambien.

Un mismo adverbio puede pertenecer a más de una categoría según la frase. Confirmar el sentido previsto por el usuario; si no está claro y afecta significativamente la selección de ejemplos, pedir aclaración en vez de mezclar usos.

## Parámetros de entrada

Usar los parámetros proporcionados por el usuario. Si no se indican el objetivo o los idiomas, pedir aclaración:

```text
ADVERBIO = cuidadosamente
IDIOMA_NATIVO = español
IDIOMA_DESTINO = inglés
NIVEL = principiante
FRASES = 15
TIPO = modo
SENTIDO = con cuidado y atención
```

`NIVEL`: `principiante`, `intermedio` o `avanzado` (también se acepta `A1`–`C2`). `TIPO` y `SENTIDO` son opcionales si el uso es inequívoco. `FRASES` indica la cantidad de frases emparejadas, además de la fila inicial con el adverbio. Si el usuario proporciona varios adverbios, generar un archivo por cada uno y por cada sentido que requiera una sesión diferenciada, salvo que solicite explícitamente compararlos.

## Formato del CSV

Cada fila debe tener exactamente dos columnas separadas por punto y coma (`;`), sin encabezado:

```text
Texto en idioma nativo;Texto en idioma destino
```

La primera fila presenta el adverbio o locución objetivo y su equivalente de referencia:

```text
cuidadosamente;carefully
```

Usar la forma de referencia natural en cada idioma; no inventar una forma aislada si el objetivo suele usarse como parte de una locución. No incluir etiquetas de categoría, explicaciones, encabezados, numeración ni comentarios en el CSV. No usar punto y coma dentro de una frase.

## Organización de la sesión

Ordenar las frases desde un uso claro y sencillo hacia usos más variados, y volver a presentar el adverbio después de otras filas para favorecer su recuperación. La progresión concreta depende del tipo de adverbio.

### 1. Presentar y asociar

Comenzar con el adverbio y su equivalente. En las primeras frases, relacionarlo con un verbo o una situación familiar:

```text
cuidadosamente;carefully
Ella escribe cuidadosamente.;She writes carefully.
```

El primer contexto debe dejar claro qué modifica el adverbio. Evitar frases aisladas cuyo sentido dependa de información que el estudiante todavía no conoce.

### 2. Repetir con variación controlada

Reutilizar el adverbio con otros sujetos, verbos o complementos conocidos. Añadir uno o dos elementos nuevos por frase como máximo:

```text
Él abre la caja cuidadosamente.;He opens the box carefully.
Marta coloca cuidadosamente los vasos en la mesa.;Marta carefully puts the glasses on the table.
```

### 3. Enseñar posición y alcance

Mostrar la posición más natural del adverbio en cada idioma. Cuando la posición afecte el énfasis o el significado, mantener un uso consistente o aclarar el sentido antes de incluir otra construcción. No traducir conservando el orden de palabras si resulta antinatural.

### 4. Adaptar la práctica a la categoría

- **Modo:** repetir con acciones distintas que admitan esa manera de hacerlas; incluir verbos de habla, movimiento o trabajo solo cuando la combinación sea natural.
- **Tiempo:** alternar sujetos y acciones, conservando referencias temporales coherentes. Usar pasado, presente o futuro solo según el nivel y el sentido del adverbio.
- **Frecuencia:** practicar rutinas con sujetos y verbos familiares; alternar afirmaciones y preguntas cuando sea útil. Mantener el valor de frecuencia y la posición gramatical correcta.
- **Lugar o dirección:** cambiar el objeto o la ubicación de forma comprensible; diferenciar ubicación estática de movimiento si el idioma lo expresa de manera distinta.
- **Grado o cantidad:** cambiar gradualmente el elemento modificado y usar solo combinaciones gramaticales naturales. Hacer explícito el alcance mediante una oración sencilla.
- **Afirmación, negación o duda:** introducir respuestas o enunciados breves que permitan inferir la fuerza del adverbio; no cambiar el grado de certeza entre las traducciones.
- **Foco o inclusión/exclusión:** dar contexto suficiente para identificar qué se destaca. Evitar pares ambiguos en los que la ubicación del adverbio altere el foco sin una razón didáctica.
- **Conectores y adverbios oracionales:** emparejar ideas cortas, mantener la puntuación y mostrar claramente la relación lógica entre ellas.
- **Interrogativos o relativos:** practicar preguntas o cláusulas con estructuras conocidas y suficiente repetición del patrón; no elevar la dificultad gramatical sin necesidad.

### 5. Recuperar y revisar

Intercalar las frases del objetivo entre contextos distintos, en vez de presentar todos los ejemplos de una construcción seguidos. Cerca del final, volver a usarlo en una frase conocida y otra ligeramente nueva. Si el sistema permite ocultar una columna, animar al estudiante a recuperar la traducción antes de revelarla; completar la lista no demuestra por sí solo que el adverbio se haya aprendido.

## Reglas de generación

### Repetición dirigida y contexto

- El adverbio o la locución objetivo debe aparecer explícitamente en la mayoría de las frases.
- Repetir su sentido objetivo; no cambiar de significado sin indicarlo y separar esos usos en sesiones distintas cuando sea necesario.
- Reutilizar estructuras y vocabulario ya vistos para que la atención se concentre en el adverbio.
- Variar los contextos con intención y espaciar la reaparición del objetivo.
- No sustituir el objetivo por sinónimos, pronombres, adjetivos o frases adverbiales diferentes con tanta frecuencia que deje de practicarse.
- Usar suficiente contexto para que el estudiante comprenda qué palabra o idea modifica el adverbio.

### Gramática y contraste entre idiomas

- Comprobar la categoría gramatical: no confundir adverbios con adjetivos, preposiciones, conjunciones o locuciones de otra función.
- Verificar posición, alcance, negación, puntuación y compatibilidad con el verbo o modificador en cada idioma.
- No asumir que palabras parecidas tienen el mismo significado o función. Revisar especialmente falsos amigos y adverbios con varios sentidos.
- Respetar las formas irregulares y las diferencias morfológicas. Algunos adverbios no cambian de forma; otros tienen comparativos irregulares o coinciden formalmente con adjetivos.
- Incluir comparación de grado solo cuando el adverbio la admita y sea relevante al nivel. No forzar comparativos o superlativos.
- Traducir la intención y el uso de forma natural; las dos frases deben comunicar el mismo hecho, frecuencia, grado, lugar o actitud.

### Dificultad y naturalidad

- Ajustar vocabulario y estructuras al nivel indicado.
- Empezar con oraciones cortas y ampliar gradualmente, evitando subordinadas o tecnicismos innecesarios.
- Escribir frases que un hablante usaría realmente; no sacrificar naturalidad para repetir mecánicamente el objetivo.
- Evitar traducciones literales, contextos improbables y ejemplos que admitan varias interpretaciones si se busca practicar un sentido específico.

## Cantidad recomendada

Generar entre 10 y 20 frases por objetivo, además de la fila inicial. Usar la cantidad solicitada si se proporcionó. No agregar frases vacías, duplicadas ni variantes que solo cambien un detalle sin ofrecer una oportunidad útil de recuperación.

## Ejemplo de resultado

### Adverbio de frecuencia: a menudo

```text
a menudo;often
Leo a menudo antes de dormir.;I often read before bed.
Mi hermana visita a menudo a nuestros abuelos.;My sister often visits our grandparents.
¿Cocinas a menudo en casa?;Do you often cook at home?
Ellos caminan a menudo por el parque.;They often walk in the park.
A menudo escuchamos música en el autobús.;We often listen to music on the bus.
¿Vas a menudo a esa tienda?;Do you often go to that store?
Mi padre trabaja a menudo desde casa.;My father often works from home.
```

El ejemplo muestra una sola función: frecuencia. Mantener la cantidad indicada por el usuario; no considerar el tamaño breve del ejemplo como una excepción a ese parámetro.

## Revisión antes de entregar

Comprobar que:

1. El archivo practica un adverbio y un sentido definidos, con el tipo de uso identificado cuando haga falta.
2. Todas las filas tienen exactamente dos campos separados por `;`; no hay encabezado, comentarios ni filas vacías.
3. La primera fila presenta el objetivo y un equivalente natural.
4. El adverbio reaparece en la mayoría de los ejemplos y en contextos intercalados.
5. Las frases practican usos apropiados para su categoría y muestran con claridad qué modifica el adverbio.
6. Categoría, sentido, posición, alcance, negación y puntuación son correctos cuando correspondan.
7. Las traducciones son naturales y equivalentes, sin falsos amigos ni cambios de certeza, frecuencia o grado.
8. La progresión se ajusta al nivel y no hay duplicados ni complejidad innecesaria.

## Principio fundamental

El estudiante debe poder recuperar el adverbio y reconocer cómo modifica una acción, circunstancia o enunciado en más de un contexto. La sesión debe combinar repetición espaciada, significado claro y variedad acorde con el tipo de adverbio; la práctica gramatical sirve al uso del vocabulario, no lo reemplaza.
