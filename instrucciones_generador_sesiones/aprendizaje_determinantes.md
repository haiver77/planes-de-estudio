# Generador de CSV para el aprendizaje de determinantes por repetición

## Objetivo

Generar sesiones en CSV para que el estudiante aprenda a elegir y usar un determinante en contexto. Cada archivo debe centrarse en un determinante, una forma o una construcción determinativa y una función concreta. Repetir el objetivo en distintos grupos nominales para aprender cómo presenta, identifica, cuantifica o relaciona un sustantivo.

Los determinantes dependen del sustantivo y de las reglas de cada idioma. Por eso, la sesión debe practicar grupos nominales completos y no solo equivalencias aisladas. Repetir el determinante de manera espaciada, alternando sustantivos y contextos familiares, sin convertir la lista en un ejercicio de explicación gramatical.

## Elegir el tipo y el uso

Identificar qué tipo de determinante y qué función se practicarán. Las categorías pueden variar entre idiomas y marcos gramaticales; tratarlas como una guía para diseñar ejemplos, no como etiquetas universales:

- **Artículos definidos e indefinidos:** practicar identificación o presentación de referentes. Respetar género, número, sonido inicial, contabilidad y uso u omisión del artículo en cada idioma. No asumir correspondencias directas entre artículos de lenguas distintas.
- **Demostrativos:** señalar referentes según distancia, situación o discurso (`este`, `esa`, `those`). Practicar el sustantivo y la forma de número o género que corresponda. Distinguir su uso como determinante antes del sustantivo del uso pronominal cuando ambas formas puedan confundirse.
- **Posesivos:** expresar relación o pertenencia (`mi`, `their`). Usar poseedores y objetos variados; practicar concordancia con el poseedor o con el sustantivo según las reglas del idioma. No confundir formas determinativas con pronombres posesivos.
- **Cuantificadores y determinantes de cantidad:** expresar cantidad o proporción (`muchos`, `some`, `each`). Comprobar si el sustantivo es contable o incontable, singular o plural, y si la forma admite ese tipo de sustantivo.
- **Numerales:** practicar cantidades o posiciones con sustantivos naturales. Respetar concordancia, escritura, orden y formas ordinales o cardinales. No combinar demasiados números nuevos en una misma sesión.
- **Interrogativos y exclamativos:** practicar grupos nominales en preguntas o exclamaciones (`qué`, `which`). Incluir puntuación y orden propios de cada idioma; no mezclarlos con usos relativos o pronominales salvo que sean el objetivo.
- **Distributivos o selectivos:** practicar elementos como `cada`, `ambos`, `either` o `neither` con sustantivos y estructuras compatibles. Revisar número y concordancia verbal.

Si un determinante tiene usos diferentes o la categoría no coincide exactamente entre los idiomas, elegir un sentido y patrón por archivo. No incluir formas pronominales, adjetivos u otras categorías como si fueran el mismo objetivo.

## Parámetros de entrada

Usar los parámetros proporcionados por el usuario. Si no se indican el objetivo o los idiomas, pedir aclaración:

```text
DETERMINANTE = este
IDIOMA_NATIVO = español
IDIOMA_DESTINO = inglés
NIVEL = principiante
FRASES = 15
TIPO = demostrativo
USO = señalar objetos cercanos
```

`TIPO` y `USO` son opcionales cuando la función es inequívoca. Si el determinante cambia según género, número, sonido o clase del sustantivo, escoger las formas que el nivel requiera practicar. Si el usuario solicita varios objetivos, crear un archivo por objetivo o sentido, salvo que pida una comparación explícita.

## Formato del CSV

Cada fila debe tener exactamente dos columnas separadas por punto y coma (`;`), sin encabezado:

```text
Texto en idioma nativo;Texto en idioma destino
```

La primera fila presenta el determinante o construcción objetivo y un equivalente de referencia:

```text
este;this
```

Si una forma aislada no demuestra su función o requiere un sustantivo para quedar clara, puede presentarse como grupo nominal:

```text
este libro;this book
```

No añadir encabezados, etiquetas gramaticales, comentarios, numeración ni explicaciones al CSV. No usar punto y coma dentro de una frase.

## Organización de la sesión

### 1. Presentar la forma en un grupo nominal claro

Comenzar con una combinación frecuente y fácil de entender. Incluir el sustantivo para mostrar qué elemento determina la forma:

```text
este libro;this book
```

### 2. Repetir con sustantivos familiares

Cambiar gradualmente el sustantivo y conservar la misma función. Introducir como máximo uno o dos elementos nuevos por frase:

```text
Esta mesa es grande.;This table is big.
Estos libros son nuevos.;These books are new.
```

### 3. Practicar los contrastes pertinentes

Cuando el objetivo requiera alternar formas, contrastar solo una dimensión a la vez, como singular/plural, género, referente definido/indefinido o cercanía. No crear pares cuyo sentido dependa de un contexto que no se ha explicado.

### 4. Contextualizar y espaciar la recuperación

Intercalar los ejemplos para que el estudiante vuelva a recuperar la forma en diferentes frases. Usar preguntas, descripciones o situaciones cotidianas si corresponden al tipo de determinante:

```text
¿Dónde está este libro?;Where is this book?
Esos libros son para la clase.;Those books are for class.
```

La traducción debe ser natural en cada idioma; no es necesario conservar el mismo determinante si el uso idiomático difiere, pero sí el significado de la frase.

## Reglas de generación

### Uso y concordancia

- Repetir el determinante objetivo explícitamente en la mayoría de los grupos nominales.
- Comprobar concordancia de género y número cuando corresponda.
- Verificar compatibilidad con sustantivos contables, incontables, singulares y plurales.
- Respetar el orden de los determinantes y las reglas de artículos de cada idioma.
- Practicar solo las variantes relevantes; no presentar cada forma flexionada como un objetivo distinto.
- Distinguir determinantes de pronombres que aparecen sin sustantivo explícito.
- Considerar contracciones, omisiones y cambios de forma exigidos por el idioma, sin forzar una traducción palabra por palabra.

### Traducción y progresión

- Traducir la referencia y el sentido, no copiar la estructura del otro idioma.
- Mantener frases naturales, breves y equivalentes.
- Reutilizar vocabulario conocido y añadir solo uno o dos elementos nuevos por frase.
- Variar los sustantivos y las situaciones sin perder el determinante objetivo.
- Evitar ambigüedades, frases artificiales y cambios de función dentro de una misma sesión.

## Cantidad recomendada

Generar entre 10 y 20 frases por objetivo, además de la fila inicial. Usar la cantidad solicitada si se proporcionó. No incluir filas vacías, duplicadas ni cambios superficiales que no aporten una oportunidad de recuperación.

## Ejemplo de resultado

### Demostrativo: este/esta/estos/estas

```text
este;this
este libro;this book
Esta mesa es pequeña.;This table is small.
Este vaso está limpio.;This glass is clean.
Estos libros son nuevos.;These books are new.
¿Es esta tu mochila?;Is this your backpack?
Estas sillas están cerca de la ventana.;These chairs are near the window.
Quiero este cuaderno para la clase.;I want this notebook for class.
```

## Revisión antes de entregar

Comprobar que:

1. El archivo practica un determinante y una función definidos.
2. Todas las filas tienen exactamente dos campos separados por `;`, sin encabezado ni filas vacías.
3. La primera fila presenta el objetivo y un equivalente adecuado.
4. El determinante aparece en la mayoría de los ejemplos y acompaña a grupos nominales claros.
5. Concordancia, orden, número, género, contabilidad y puntuación son correctos cuando correspondan.
6. La traducción conserva la referencia y el significado sin forzar una correspondencia inexistente.
7. El nivel y la progresión son adecuados; no hay filas duplicadas ni cambios de categoría innecesarios.

## Principio fundamental

El estudiante debe aprender a elegir el determinante que funciona con el sustantivo y el contexto, no solo memorizar una equivalencia aislada. Repetirlo en grupos nominales variados, respetando las reglas propias de cada idioma y manteniendo cada sesión enfocada.
