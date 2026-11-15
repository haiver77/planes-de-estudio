# Generador de CSV para el aprendizaje de pronombres por repetición

## Objetivo

Generar sesiones en CSV para que el estudiante aprenda a reconocer y usar un pronombre en contexto. Cada archivo debe centrarse en un pronombre, una función y un sentido concretos. Repetir el objetivo en frases naturales para que el estudiante practique su forma, función y relación con el referente.

La prioridad es la repetición comprensible, no la variedad extrema. Cambiar gradualmente los verbos, referentes y situaciones, pero mantener el pronombre objetivo en el centro de cada frase.

## Elegir el tipo y el uso

Identificar qué tipo de pronombre y qué función se practicarán. Las categorías pueden variar entre idiomas; usarlas como guía y no asumir que las formas se corresponden palabra por palabra:

- **Personales de sujeto:** indican quién realiza la acción (`yo`, `ella`, `they`). Practicar persona, número y género cuando sean relevantes. En idiomas que suelen omitir el sujeto, incluirlo cuando sea natural y útil para practicar el contraste; no forzar su presencia si produce frases artificiales.
- **Personales de objeto directo o indirecto:** sustituyen a quien o a lo que recibe la acción (`lo`, `le`, `him`, `them`). Aclarar el tipo de complemento, el referente y las formas que deben practicarse.
- **Reflexivos y recíprocos:** relacionan la acción con quien la realiza o con los participantes entre sí (`me`, `se`, `each other`). Usar verbos y construcciones compatibles con el sentido elegido.
- **Posesivos:** expresan posesión como pronombres, sin acompañar directamente a un sustantivo (`el mío`, `hers`, `theirs`). No confundirlos con determinantes posesivos (`mi`, `her`) que preceden a un sustantivo.
- **Demostrativos:** sustituyen a un referente y señalan distancia o relación con el discurso (`este`, `those`). No confundirlos con demostrativos usados como determinantes delante de un sustantivo.
- **Relativos:** introducen una oración que se refiere a un antecedente (`que`, `who`, `which`). Mantener claro el antecedente y usar estructuras adecuadas al nivel.
- **Interrogativos y exclamativos:** preguntan o expresan énfasis en lugar de sustituir un referente conocido (`quién`, `what`). Usar preguntas o exclamaciones naturales y distinguir estos usos de los relativos.
- **Indefinidos:** se refieren a personas o cosas no identificadas con precisión (`alguien`, `something`). Mantener claro el sentido afirmativo, negativo o cuantitativo cuando corresponda.

Si una forma tiene varias funciones, escoger una por archivo, salvo que el usuario solicite compararlas explícitamente. Si una forma puede ser pronombre, determinante u otra categoría, asegurar que cada ejemplo use la función objetivo.

## Parámetros de entrada

Usar los parámetros proporcionados por el usuario. Si falta el pronombre objetivo o alguno de los idiomas, pedir aclaración:

```text
PRONOMBRE = lo
IDIOMA_NATIVO = español
IDIOMA_DESTINO = italiano
NIVEL = principiante
FRASES = 5
TIPO = personal de objeto directo
SENTIDO = sustituye un referente masculino singular
```

`NIVEL`: `principiante`, `intermedio` o `avanzado` (también se acepta `A1`–`C2`). `TIPO` y `SENTIDO` son opcionales si la función es inequívoca. `FRASES` indica la cantidad de frases emparejadas y no incluye la fila inicial del pronombre. Si el usuario proporciona varios pronombres o funciones, crear una sesión por objetivo, salvo que solicite una comparación.

## Formato del CSV

Cada fila debe tener exactamente dos columnas separadas por punto y coma (`;`), sin encabezado ni filas vacías:

```text
Texto en idioma nativo;Texto en idioma destino
```

La primera fila presenta el pronombre y su equivalente funcional de referencia:

```text
lo;lo
```

Las frases siguientes deben practicar el mismo pronombre objetivo, o su equivalente funcional natural, en ambas columnas:

```text
Veo el libro y lo leo.;Vedo il libro e lo leggo.
Lo compro hoy.;Lo compro oggi.
No lo encuentro.;Non lo trovo.
¿Lo quieres?;Lo vuoi?
```

En este ejemplo, `lo` es el pronombre de objeto directo en ambas lenguas. `el` e `il` acompañan al sustantivo `libro` y son artículos, no el objetivo de la sesión.

No añadir encabezados, etiquetas gramaticales, comentarios, numeración ni explicaciones al CSV. No usar punto y coma dentro de una frase.

## Organización de la sesión

### 1. Establecer claramente la función

Empezar con una frase corta donde se pueda identificar la función del pronombre. Cuando ayude a entender su referente, incluirlo en la misma frase junto con el pronombre:

```text
Veo el libro y lo leo.;Vedo il libro e lo leggo.
```

No presentar únicamente una frase con el referente nominal si esa frase no contiene el pronombre objetivo.

### 2. Repetir el pronombre con variación controlada

Mantener el pronombre en cada frase y variar gradualmente el verbo, el sujeto, el referente o la situación. Cambiar una dimensión a la vez y reutilizar vocabulario familiar:

```text
Lo compro hoy.;Lo compro oggi.
No lo encuentro.;Non lo trovo.
```

### 3. Espaciar la recuperación

Intercalar contextos diferentes y volver a presentar el pronombre después de otras frases. Se pueden usar afirmaciones, negaciones y preguntas cuando sean naturales para la función elegida.

### 4. Practicar contrastes solo cuando correspondan

Si la sesión enseña un paradigma o una comparación solicitada, cambiar una característica a la vez (por ejemplo, singular/plural o sujeto/objeto) y mantener explícito cuál forma se practica en cada frase. No introducir formas de otras funciones como si fueran variantes del mismo pronombre.

## Reglas de generación

### Repetición y función

- El pronombre objetivo debe aparecer explícitamente en todas las frases emparejadas siempre que la gramática de ambos idiomas lo permita.
- Cada columna debe contener el pronombre objetivo o su equivalente funcional natural. No sustituirlo por el sustantivo antecedente, un artículo, un determinante u otra categoría gramatical.
- Si una lengua normalmente omite el pronombre o usa una construcción distinta, elegir frases que permitan practicar el pronombre de forma natural. No conservar una frase si al traducirla desaparece el objetivo; reemplazarla por otra equivalente que sí lo practique.
- Puede variar la forma por concordancia, caso, persona o número solo cuando ese cambio forme parte del objetivo indicado. En ese caso, presentar claramente las formas del paradigma y no alternarlas sin propósito.
- Mantener claro el referente de los pronombres anafóricos. Si es necesario, incluir el antecedente en la misma frase, pero conservar también el pronombre objetivo.
- Distinguir pronombres de determinantes, artículos, adverbios y conjunciones, incluso cuando compartan la misma forma escrita.

### Traducción y progresión

- Traducir la función y el significado, no la forma palabra por palabra.
- Usar el equivalente natural del pronombre en cada idioma y respetar su posición, concordancia y forma.
- Mantener frases breves, naturales y adecuadas al nivel.
- Reutilizar vocabulario conocido y añadir como máximo uno o dos elementos nuevos por frase.
- Evitar frases ambiguas, artificiales o repetidas con cambios irrelevantes.

## Cantidad recomendada

Generar entre 4 y 7 frases por objetivo, además de la fila inicial. Usar la cantidad solicitada si se proporcionó. No incluir filas vacías ni duplicadas.

## Revisión final

Antes de entregar el CSV, comprobar que:

- Todas las filas tienen exactamente dos columnas y no contienen punto y coma dentro de las frases.
- Cada frase de ambas columnas practica el pronombre objetivo o su equivalente funcional.
- Ninguna frase usa solo el antecedente nominal, un artículo o un determinante en lugar del pronombre objetivo.
- La función y el referente son claros, y las traducciones son naturales y equivalentes.
- La cantidad de frases corresponde al parámetro solicitado, sin contar la fila inicial.
