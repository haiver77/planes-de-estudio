# Generador de CSV para el aprendizaje de conjunciones por repetición

## Objetivo

Generar sesiones en CSV para que el estudiante aprenda a conectar palabras, grupos de palabras u oraciones mediante una conjunción. Cada archivo debe centrarse en una conjunción o construcción conjuntiva y una función definida. Las frases deben mostrar qué relación lógica o gramatical establece el objetivo.

Las conjunciones conectan elementos, por lo que aprenderlas requiere ejemplos con suficiente estructura a ambos lados. Evitar listas de traducciones aisladas: repetir la conjunción en frases naturales y progresivas, variando las ideas conectadas sin perder de vista la relación.

## Elegir el tipo y la función

Determinar qué relación expresa la conjunción en las frases. Las categorías y etiquetas pueden variar entre idiomas; usarlas como guía pedagógica:

- **Coordinantes de adición:** agregan información o elementos (`y`, `and`, `nor`). Conectar palabras, grupos o cláusulas paralelas y mantener estructuras compatibles.
- **Coordinantes de alternativa:** presentan opciones (`o`, `or`, `either...or`). Practicar opciones reales con elementos de la misma clase cuando sea posible; considerar las construcciones correlativas como unidad.
- **Coordinantes de contraste:** oponen o limitan ideas (`pero`, `but`, `yet`). Usar dos ideas claras y evitar que el contraste dependa de vocabulario desconocido.
- **Coordinantes de consecuencia o explicación:** conectan ideas mediante resultado o razón (`así que`, `so`, `for`). Distinguir causa de consecuencia; no confundir el uso conjuntivo con otros sentidos de la misma palabra.
- **Subordinantes de causa o concesión:** introducen razones o contrastes (`porque`, `although`). Mostrar claramente la cláusula principal y la subordinada; mantener natural el orden de las cláusulas.
- **Subordinantes condicionales:** expresan condiciones (`si`, `unless`). Usar situaciones comprensibles y respetar los tiempos y modos verbales requeridos, incluido el subjuntivo cuando corresponda.
- **Subordinantes temporales:** expresan tiempo o secuencia (`cuando`, `before`, `until`). Practicar eventos relacionados y revisar las diferencias de tiempo verbal entre los idiomas.
- **Subordinantes de propósito o resultado:** expresan finalidad o consecuencia (`para que`, `so that`). Elegir estructuras adecuadas al nivel y mantener explícita la relación entre las cláusulas.
- **Subordinantes completivas o de contenido:** introducen una cláusula que funciona como complemento (`que`, `that`, `if/whether`). Practicar con verbos y marcos frecuentes; no incluirlas si requieren estructuras demasiado avanzadas.
- **Correlativas:** aparecen como pares (`tanto...como`, `either...or`, `neither...nor`, `not only...but also`). Tratar el par completo como objetivo, conservar el paralelismo y comprobar concordancia.

Conjunciones como `cuando`, `si` o `que` pueden tener usos distintos. Seleccionar una sola función por archivo. Distinguir conjunciones de adverbios conectores, preposiciones y pronombres relativos aunque en ciertos idiomas compartan formas.

## Parámetros de entrada

Usar los parámetros proporcionados por el usuario. Si no se indican el objetivo o los idiomas, pedir aclaración:

```text
CONJUNCION = aunque
IDIOMA_NATIVO = español
IDIOMA_DESTINO = inglés
NIVEL = intermedio
FRASES = 15
TIPO = subordinante concesiva
FUNCION = introducir una idea que contrasta con la principal
```

`TIPO` y `FUNCION` son opcionales si el uso es inequívoco. Para construcciones correlativas, especificar el par completo. Si una forma tiene múltiples funciones, definir el sentido antes de crear los ejemplos; separar los usos en archivos distintos, salvo que el usuario solicite compararlos.

## Formato del CSV

Cada fila debe tener exactamente dos columnas separadas por punto y coma (`;`), sin encabezado:

```text
Texto en idioma nativo;Texto en idioma destino
```

La primera fila presenta la conjunción o construcción y un equivalente de referencia:

```text
aunque;although
```

Para una construcción correlativa, incluir ambos componentes como una sola unidad:

```text
o... o;either...or
```

No añadir encabezados, etiquetas gramaticales, comentarios, numeración ni explicaciones al CSV. No usar punto y coma dentro de una frase.

## Organización de la sesión

### 1. Presentar la relación entre ideas

Comenzar con una frase sencilla que haga evidente la relación expresada. Incluir ideas familiares a ambos lados de la conjunción:

```text
Quiero salir, aunque está lloviendo.;I want to go out, although it is raining.
```

### 2. Mantener el patrón y variar el contenido

Repetir la conjunción con pares de ideas diferentes pero estructuras conocidas:

```text
Ella está cansada, aunque sigue estudiando.;She is tired, although she keeps studying.
```

### 3. Practicar estructuras propias del tipo

- **Coordinantes:** alternar elementos o cláusulas paralelas; incluir puntuación correcta.
- **Subordinantes:** variar gradualmente el orden de la cláusula subordinada, cuando ambas posiciones sean naturales; conservar la relación lógica.
- **Condicionales y temporales:** introducir cambios de tiempo verbal o modo solo cuando el nivel y la regla objetivo lo requieran.
- **Correlativas:** mantener los dos componentes y el paralelismo gramatical; no dejar un miembro del par sin su correspondiente elemento.
- **Conjunciones de causa o consecuencia:** asegurarse de que la secuencia de ideas refleje la causalidad correcta, no solo una conexión aproximada.

### 4. Espaciar la recuperación

Intercalar ejemplos con distintos sujetos y situaciones, y volver a presentar la conjunción después de otras filas. Hacia el final, usar una frase algo nueva sin añadir vocabulario o gramática innecesarios.

## Reglas de generación

### Estructura y función

- El objetivo debe aparecer explícitamente en la mayoría de las frases.
- Cada ejemplo debe mostrar con claridad qué elementos conecta y qué relación establece.
- Mantener las dos partes de la oración comprensibles; no practicar la conjunción mediante fragmentos incompletos.
- Usar construcciones paralelas cuando la conjunción lo requiera.
- Tratar las construcciones correlativas como una unidad y conservar todos sus componentes.
- Verificar orden, puntuación, modo y tiempos verbales, especialmente en subordinadas condicionales y temporales.
- No mezclar funciones diferentes de una misma forma dentro de un archivo sin una petición explícita.
- Distinguir conjunciones de adverbios conectores y de otras palabras con forma similar.

### Traducción y progresión

- Mantener la misma relación lógica en ambas columnas, aunque cambie la estructura.
- No asumir equivalencia palabra por palabra: una lengua puede omitir la conjunción, elegir otra o requerir una construcción distinta.
- Evitar traducciones que conviertan posibilidad en certeza, causa en consecuencia, o contraste en adición.
- Empezar con cláusulas breves y vocabulario frecuente; aumentar la complejidad gradualmente.
- Introducir como máximo uno o dos elementos nuevos por frase.
- Evitar ejemplos cuya interpretación dependa de una situación poco clara.

## Cantidad recomendada

Generar entre 10 y 20 frases por objetivo, además de la fila inicial. Usar la cantidad solicitada si se proporcionó. No incluir filas vacías, duplicadas ni variantes que solo cambien un nombre sin aportar práctica útil.

## Ejemplo de resultado

### Conjunción coordinante de contraste: pero

```text
pero;but
Quiero caminar, pero está lloviendo.;I want to walk, but it is raining.
La comida es sencilla, pero está rica.;The food is simple, but it is tasty.
Él tiene poco tiempo, pero ayuda a su amigo.;He has little time, but he helps his friend.
La tienda es pequeña, pero vende muchas cosas.;The store is small, but it sells many things.
Queríamos salir, pero empezó a llover.;We wanted to go out, but it started to rain.
```

## Revisión antes de entregar

Comprobar que:

1. El archivo practica una conjunción o construcción y una función definidas.
2. Todas las filas tienen exactamente dos campos separados por `;`, sin encabezado ni filas vacías.
3. La primera fila presenta la conjunción y un equivalente de referencia adecuado.
4. La conjunción aparece en la mayoría de las frases y conecta elementos completos y comprensibles.
5. La relación lógica, el paralelismo, el orden, la puntuación y los tiempos o modos son correctos.
6. Las traducciones naturales conservan la relación sin forzar estructuras idénticas.
7. Las frases son progresivas, apropiadas al nivel y no mezclan funciones sin propósito.

## Principio fundamental

El estudiante debe poder recuperar la conjunción y entender cómo conecta ideas. Repetirla en contextos variados, manteniendo clara su relación lógica y la estructura que exige; no reducir su aprendizaje a una traducción aislada.
