# Generador de CSV para el aprendizaje de sustantivos por repetición

## Objetivo

Generar archivos CSV para aprender sustantivos mediante repetición progresiva y uso contextualizado. Cada archivo debe centrarse en un solo sustantivo, objeto o concepto léxico concreto y presentar frases sencillas, naturales y fáciles de comprender.

La prioridad es que el estudiante reconozca y recuerde el sustantivo objetivo en distintos contextos. No se busca maximizar la variedad de vocabulario, sino repetir el objetivo de manera intencional sin producir frases mecánicas o artificiales.

La exposición repetida ayuda a aprender, pero no garantiza por sí sola la memorización. Ordenar las filas para que el estudiante pueda intentar recuperar el significado y la forma del sustantivo, comprobar la respuesta y volver a encontrarlo más adelante.

## Alcance: tipos de sustantivos

El procedimiento sirve para sustantivos de distintos tipos. Antes de generar el CSV, identificar las propiedades relevantes del objetivo y practicarlas solo cuando ayuden a aprenderlo:

- **Común o propio:** por ejemplo, `ciudad` o `London`. Usar nombres propios cuando sean el objetivo o resulten necesarios para un contexto natural.
- **Concreto o abstracto:** por ejemplo, `mesa` o `idea`. En niveles iniciales, priorizar referentes fáciles de imaginar. Para conceptos abstractos, usar situaciones claras que permitan entender el significado.
- **Contable o incontable:** por ejemplo, `book` o `water`. Respetar los artículos, plurales y cuantificadores propios de cada idioma. No forzar un plural ni usar `a/an` directamente con un sustantivo incontable.
- **Individual o colectivo:** por ejemplo, `bird` o `team`. Mantener la concordancia correcta en cada idioma.
- **Simple o compuesto:** por ejemplo, `tooth` o `toothbrush`. Tratar los compuestos frecuentes como una unidad léxica.
- **Género y número:** aprender el artículo y el plural cuando sean relevantes; incluir plurales irregulares si forman parte del objetivo.

Estas propiedades pueden cruzarse. No intentar enseñar todas a la vez: seleccionar únicamente las que sean necesarias para el sustantivo y el nivel solicitados. El género gramatical de un idioma no determina el del otro.

## Formato del CSV

Cada fila debe tener exactamente dos columnas separadas por punto y coma (`;`), sin encabezado:

```text
Texto en idioma nativo;Texto en idioma destino
```

La primera fila presenta el objetivo y su equivalente. Incluir el artículo si es una forma natural y útil de aprender el sustantivo en cada idioma:

```text
el libro;the book
```

Las filas restantes contienen frases emparejadas en ambos idiomas. No añadir columnas, comentarios, numeración, encabezados ni explicaciones gramaticales al archivo final. No usar punto y coma dentro de una frase.

## Parámetros de entrada

Usar los parámetros proporcionados por el usuario. Si no se indican, pedir aclaración en vez de inventar el objetivo o los idiomas:

```text
SUSTANTIVO = libro
IDIOMA_NATIVO = español
IDIOMA_DESTINO = inglés
NIVEL = principiante
FRASES = 15
TIPO = contable
SENTIDO = objeto para leer
```

- `NIVEL`: `principiante`, `intermedio` o `avanzado` (también se acepta `A1`–`C2`).
- `TIPO` y `SENTIDO` son opcionales. Usarlos si el sustantivo es polisémico o su categoría (contable, incontable, abstracto, etc.) requiere precisión.

Otros ejemplos de objetivos válidos:

```text
SUSTANTIVO = mesa
SUSTANTIVO = agua
SUSTANTIVO = familia
SUSTANTIVO = felicidad
SUSTANTIVO = toothbrush
```

Cada archivo debe trabajar un solo objetivo léxico. Si el usuario proporciona varios sustantivos, generar un archivo separado para cada uno, salvo que solicite explícitamente otro alcance.

## Organización de la sesión

Progresar desde el reconocimiento de la palabra hasta su recuperación en contextos variados. Mantener el sustantivo objetivo visible en la mayoría de las frases.

### 1. Presentar la forma objetivo

Comenzar con el sustantivo aislado o con su artículo, según lo que convenga al idioma y al nivel:

```text
libro;book
el libro;the book
```

No presentar dos variantes como objetivos distintos si solo se está enseñando una. Si el objetivo incluye una forma plural o irregular, mostrar claramente la relación con el singular.

### 2. Asociar el sustantivo con una frase básica

Usar estructuras conocidas y breves para que el contexto no distraiga del objetivo:

```text
Es un libro.;It is a book.
Veo el libro.;I see the book.
```

### 3. Reforzar la forma que corresponda

Practicar, cuando sea pertinente, artículo, singular/plural, contabilidad, género, posesión o cuantificadores. Introducir como máximo uno o dos elementos nuevos por frase.

```text
El libro es nuevo.;The book is new.
Los libros son nuevos.;The books are new.
```

No incluir variaciones que no apliquen al sustantivo. Para incontables, usar expresiones naturales de cantidad o medida:

```text
Necesito agua.;I need water.
Quiero un vaso de agua.;I want a glass of water.
```

### 4. Contextualizar de forma gradual

Ampliar las frases con situaciones familiares, ubicaciones, posesión y acciones comunes. Reutilizar estructuras y palabras ya introducidas:

```text
El libro está en la mesa.;The book is on the table.
Tengo el libro en mi mochila.;I have the book in my backpack.
Leo el libro en casa.;I read the book at home.
```

### 5. Recuperar y revisar

Intercalar frases del objetivo entre contextos distintos, en vez de presentar todas las frases de un patrón o contexto en un único bloque. Hacia el final, reutilizar el objetivo en ejemplos que no introduzcan vocabulario nuevo importante.

Si el sistema que consume el CSV permite ocultar una columna, usar las parejas para que el estudiante intente recordar la traducción antes de revelarla. No afirmar que memorizó el objetivo solo por haber completado la lista; la comprobación requiere recuperar la palabra sin verla.

## Reglas de generación

### Repetición dirigida

- El sustantivo objetivo debe aparecer explícitamente en la mayoría de las frases.
- Repetir la forma correcta, el artículo y el plural relevante de manera consistente.
- No sustituir el objetivo por sinónimos, pronombres o palabras relacionadas con tanta frecuencia que deje de practicarse.
- Variar el contexto, no la palabra que se está aprendiendo.

### Progresión y carga léxica

- Reutilizar vocabulario conocido y estructuras simples.
- Añadir solo uno o dos elementos nuevos por frase.
- Aumentar gradualmente la longitud; no saltar de una palabra aislada a frases complejas.
- Mantener cada frase comprensible por sí sola.

### Naturalidad y equivalencia

- Escribir frases que un hablante usaría realmente.
- Traducir el significado, no palabra por palabra.
- Verificar artículos, concordancia, orden de palabras, plural y cuantificadores en ambos idiomas.
- No crear frases absurdas solo para repetir el sustantivo.
- Evitar que una frase admita varias traducciones cuando se busca practicar una forma concreta.

### Dificultad

- Ajustar vocabulario y gramática al nivel proporcionado.
- Preferir contextos concretos, cotidianos y fáciles de imaginar para principiantes.
- Evitar tecnicismos, ambigüedad y subordinadas innecesarias.
- Introducir sustantivos abstractos con suficiente contexto para que el significado sea claro.

## Cantidad recomendada

Generar entre 10 y 20 frases por objetivo, además de la fila inicial de vocabulario. Usar la cantidad solicitada si se proporcionó. No agregar frases vacías, duplicadas ni variantes que solo cambien un marcador temporal sin aportar una oportunidad útil de recuperación.

## Ejemplo de resultado

### Sustantivo: libro

```text
libro;book
el libro;the book
Es un libro.;It is a book.
El libro es nuevo.;The book is new.
El libro es pequeño.;The book is small.
Mi libro está aquí.;My book is here.
Veo el libro en la mesa.;I see the book on the table.
Tengo un libro en mi mochila.;I have a book in my backpack.
Leo el libro en casa.;I read the book at home.
Ella lee el libro en la escuela.;She reads the book at school.
Los libros están en la mesa.;The books are on the table.
¿Dónde está mi libro?;Where is my book?
Necesito el libro para la clase.;I need the book for class.
Guardo el libro en mi mochila.;I put the book in my backpack.
El libro de mi hermana está aquí.;My sister's book is here.
Leo este libro con mi hermano.;I read this book with my brother.
```

## Revisión antes de entregar

Antes de guardar el CSV, comprobar que:

1. El archivo trata un solo sustantivo o concepto objetivo.
2. Todas las filas tienen exactamente dos campos separados por `;`.
3. La primera fila presenta el objetivo y su equivalente.
4. El sustantivo objetivo se repite en la mayoría de los ejemplos.
5. Artículos, plurales, contabilidad y concordancia son correctos cuando aparecen.
6. Las frases son naturales, comprensibles, progresivas y equivalentes en significado.
7. No hay filas vacías, encabezados, comentarios, duplicados ni complejidad innecesaria.

## Principio fundamental

El propósito es que el estudiante asocie la forma del sustantivo con su significado y pueda recuperarlo en más de un contexto. La repetición debe ser frecuente, comprensible y gradual; la variedad se limita a la necesaria para que el aprendizaje no dependa de una sola frase.
