# Generador de CSV para el aprendizaje de preposiciones por repetición

## Objetivo

Generar sesiones en CSV para que el estudiante aprenda el significado y el uso de una preposición o locución preposicional en contexto. Cada archivo debe centrarse en una preposición, un sentido o una construcción concreta. La práctica debe mostrar qué relación expresa y con qué complemento o estructura se usa.

Las preposiciones suelen tener varios sentidos y rara vez se traducen con una correspondencia exacta entre idiomas. Por ello, no enseñar una lista de equivalencias descontextualizadas. Repetir el objetivo en frases claras, variando gradualmente los objetos, lugares o situaciones, y separando los sentidos que podrían confundirse.

## Elegir el tipo y el sentido

Determinar qué relación expresa la preposición en los ejemplos. Las categorías siguientes son orientativas: una misma preposición puede cumplir varias funciones, y las lenguas no siempre las clasifican del mismo modo.

- **Lugar o ubicación:** expresa dónde ocurre algo o dónde está un referente (`en`, `under`, `between`). Usar objetos y lugares concretos, con relaciones espaciales fáciles de visualizar.
- **Dirección o destino:** expresa movimiento hacia un lugar o referente (`a`, `toward`, `into`). Diferenciar destino, dirección y entrada en un espacio cuando el idioma lo marque.
- **Origen o procedencia:** expresa desde dónde, de quién o de qué procede algo (`de`, `from`, `out of`). Usar contextos naturales de movimiento, origen o pertenencia y no confundirlos con otros sentidos.
- **Tiempo:** ubica una acción en el tiempo o expresa duración y límite (`a`, `durante`, `before`, `until`). Distinguir momento, duración, plazo y secuencia; no usar la misma equivalencia para todos.
- **Medio, instrumento o manera:** indica con qué o cómo se realiza una acción (`con`, `by`, `with`). Elegir verbos compatibles y evitar confundir instrumento, compañía y agente.
- **Causa, motivo o propósito:** expresa por qué o para qué ocurre algo (`por`, `para`, `because of`, `for`). Separar causa, destinatario y finalidad; en español, no mezclar los sentidos de `por` y `para` en un solo objetivo ambiguo.
- **Compañía o asociación:** indica con quién o junto a qué se realiza algo (`con`, `with`). Diferenciar compañía de instrumento según el contexto.
- **Pertenencia, relación o tema:** conecta referentes en una relación (`de`, `about`, `of`). Aclarar si expresa posesión, composición, tema u otra relación.
- **Agente o función en una construcción:** aparece en estructuras pasivas, complementos regidos u otros patrones (`por`, `by`, `a`). Enseñarlo dentro de una oración completa y adecuada al nivel.
- **Locuciones preposicionales y usos regidos:** tratar expresiones como una unidad cuando su sentido no se obtiene de cada palabra por separado. Practicar el complemento habitual y no desarmar una locución idiomática.

Si el objetivo tiene varios sentidos, seleccionar uno por archivo. Si el usuario pide comparar preposiciones cercanas, crear grupos de ejemplos paralelos que hagan visible el contraste sin enseñar varias reglas nuevas en cada frase.

## Parámetros de entrada

Usar los parámetros proporcionados por el usuario. Si no se indican el objetivo o los idiomas, pedir aclaración:

```text
PREPOSICION = en
IDIOMA_NATIVO = español
IDIOMA_DESTINO = inglés
NIVEL = principiante
FRASES = 15
TIPO = lugar
SENTIDO = ubicación dentro de un espacio
```

`NIVEL`: `principiante`, `intermedio` o `avanzado` (también se acepta `A1`–`C2`). `TIPO` y `SENTIDO` son opcionales si el uso es inequívoco. Si la preposición es polisémica o puede ser un falso amigo, precisar el sentido antes de generar la lista. Si se trabaja una locución, registrarla como unidad objetivo.

## Formato del CSV

Cada fila debe tener exactamente dos columnas separadas por punto y coma (`;`), sin encabezado:

```text
Texto en idioma nativo;Texto en idioma destino
```

La primera fila presenta la preposición o locución y un equivalente de referencia:

```text
debajo de;under
```

Cuando la preposición aislada no tenga una traducción fiable, puede usarse una frase breve de referencia:

```text
en la mesa;on the table
```

No incluir encabezados, etiquetas, comentarios, numeración ni explicaciones gramaticales en el CSV. No usar punto y coma dentro de una frase.

## Organización de la sesión

### 1. Presentar una relación clara

Empezar con una frase corta donde el contexto deje inequívoco el sentido de la preposición:

```text
El libro está en la mesa.;The book is on the table.
```

### 2. Repetir la misma relación con vocabulario familiar

Variar el sustantivo, sujeto o lugar sin cambiar el sentido que se enseña:

```text
La taza está en la mesa.;The cup is on the table.
El teléfono está en la bolsa.;The phone is in the bag.
```

### 3. Añadir contextos gradualmente

Introducir acciones, preguntas o tiempos verbales solo cuando ayuden a practicar la relación objetivo. Cambiar una dimensión a la vez y conservar frases comprensibles por sí solas.

### 4. Espaciar el objetivo y reforzar el complemento

Intercalar frases de distintas situaciones y volver a incluir la preposición objetivo después de varias filas. Practicar con los complementos que naturalmente la siguen; no presentar el objetivo como una palabra suelta si la construcción requiere una locución o una forma específica.

## Reglas de generación

### Sentido, complemento y estructura

- El sentido elegido debe aparecer explícitamente en la mayoría de las frases.
- Usar complementos y construcciones que sean gramaticales y naturales para esa preposición.
- Evitar mezclar sentidos diferentes de una misma preposición en un archivo, salvo que se solicite compararlos.
- Mantener claro qué elementos relaciona la preposición.
- Incluir las contracciones o cambios formales obligatorios, como `al` y `del` en español, cuando correspondan.
- Distinguir preposiciones de partículas verbales, adverbios y conjunciones. Enseñar verbos con preposición regida dentro de su construcción natural.
- Tratar una locución preposicional o expresión fija como unidad cuando su significado o uso no sea predecible palabra por palabra.

### Equivalencia entre idiomas

- Traducir la relación y la intención, no la preposición palabra por palabra.
- No exigir que ambos idiomas usen una preposición en la misma frase; pueden requerir una estructura distinta o ninguna preposición.
- Comprobar falsos amigos y contrastes frecuentes, como `en` frente a `in`/`on`, o `por` frente a `para`.
- Si una frase admite más de una lectura, agregar contexto suficiente o reemplazarla por un ejemplo más claro.
- Mantener la misma relación temporal, espacial, causal u otra en las dos columnas.

### Progresión y repetición

- Empezar con situaciones concretas, especialmente para principiantes.
- Reutilizar vocabulario conocido y añadir solo uno o dos elementos nuevos por frase.
- Variar sujetos, objetos y contextos sin perder de vista la preposición objetivo.
- Evitar repetir una misma oración con cambios irrelevantes.
- Incluir preguntas o afirmaciones solo cuando aporten práctica natural de la estructura.

## Cantidad recomendada

Generar entre 10 y 20 frases por objetivo, además de la fila inicial. Usar la cantidad solicitada si se proporcionó. No incluir filas vacías, duplicadas ni ejemplos que no ofrezcan una oportunidad útil de recuperación.

## Ejemplo de resultado

### Preposición de lugar: debajo de

```text
debajo de;under
El gato está debajo de la mesa.;The cat is under the table.
La pelota está debajo de la silla.;The ball is under the chair.
Mis zapatos están debajo de la cama.;My shoes are under the bed.
¿Está la caja debajo de la mesa?;Is the box under the table?
El perro busca su juguete debajo del sofá.;The dog looks for its toy under the sofa.
La mochila está debajo de mi escritorio.;The backpack is under my desk.
```

## Revisión antes de entregar

Comprobar que:

1. El archivo practica una preposición o locución con sentido y tipo de relación definidos.
2. Todas las filas tienen exactamente dos campos separados por `;`, sin encabezado ni filas vacías.
3. La primera fila presenta el objetivo o una referencia breve y comprensible.
4. La preposición aparece en la mayoría de los ejemplos y conserva el sentido seleccionado.
5. Complementos, contracciones, régimen y orden son correctos en ambos idiomas.
6. Las traducciones expresan la misma relación sin forzar equivalencias palabra por palabra.
7. Las frases son naturales, progresivas y adecuadas al nivel, sin duplicados ni ambigüedades innecesarias.

## Principio fundamental

El estudiante debe aprender qué relación expresa la preposición y cómo se integra con su complemento en una frase real. Practicar una relación por vez, repetirla en contextos variados y evitar asumir que una preposición tiene una traducción única.
