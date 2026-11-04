# Generador de CSV para el aprendizaje de adjetivos por repetición

## Objetivo

Generar archivos CSV que ayuden a aprender adjetivos mediante recuperación activa, repetición espaciada dentro de la sesión y uso en contextos variados. Cada archivo debe centrarse en un adjetivo objetivo y enseñar cómo se usa en frases naturales, no solo su traducción aislada.

La prioridad es que el estudiante reconozca, comprenda y pueda usar el adjetivo en más de una estructura. Repetir el objetivo de forma intencional, pero cambiar gradualmente el sustantivo, la situación o la función gramatical para evitar que se memorice una única frase. No introducir variaciones gramaticales que no sean pertinentes para el adjetivo o el nivel.

## Alcance del aprendizaje

Antes de generar el archivo, identificar qué propiedades del adjetivo son relevantes en el idioma de origen y en el idioma de destino. Practicar solo las que ayuden a usarlo correctamente:

- **Significado y matiz:** precisar el sentido objetivo y evitar equivalentes que solo coincidan en ciertos contextos. Si una palabra tiene varios sentidos, seleccionar uno por archivo, salvo que el usuario solicite explícitamente compararlos.
- **Concordancia:** practicar género y número cuando el idioma los marque. En español, incluir las formas que correspondan (`pequeño`, `pequeña`, `pequeños`, `pequeñas`) con sustantivos y verbos correctamente concordados. No atribuir género gramatical de un idioma al otro.
- **Posición:** enseñar la posición natural del adjetivo en cada idioma. En español, muchos adjetivos aparecen después del sustantivo, pero algunos pueden ir antes y la posición puede cambiar el matiz. En inglés, el adjetivo suele preceder al sustantivo, pero puede aparecer después de verbos copulativos. No imponer el orden de un idioma al otro.
- **Función:** cuando sea apropiado, practicar el adjetivo junto a un sustantivo y como atributo con verbos como `ser`, `estar`, `parecer` o sus equivalentes. Elegir el verbo copulativo según el significado, no para crear una correspondencia mecánica entre idiomas.
- **Grado:** incluir formas comparativas o superlativas solo si son útiles, naturales y adecuadas al objetivo y nivel. Respetar las formas irregulares y las diferencias entre idiomas; no asumir que todo adjetivo admite todos los grados.
- **Uso y registro:** distinguir sentidos, colocaciones y restricciones de uso relevantes. Evitar sinónimos, derivados, adverbios u otras categorías gramaticales como sustitutos del adjetivo objetivo.

No intentar enseñar todas estas propiedades a la vez. Definir una progresión breve y priorizar el uso más frecuente del adjetivo.

## Formato del CSV

Cada fila debe tener exactamente dos columnas separadas por punto y coma (`;`), sin encabezado:

```text
Texto en idioma nativo;Texto en idioma destino
```

La primera fila presenta el adjetivo objetivo y su equivalente en forma de diccionario o forma de referencia adecuada a cada idioma:

```text
pequeño;small
```

Si una forma aislada resulta ambigua o poco útil, puede incluirse una pareja mínima con un sustantivo frecuente para dejar clara la concordancia o el uso:

```text
pequeño, pequeña;small
```

No incluir explicaciones, etiquetas gramaticales, encabezados, numeración ni comentarios en el CSV. Las explicaciones de este documento guían la generación; no deben agregarse como columnas o filas al archivo final. No usar punto y coma dentro de una frase.

## Parámetros de entrada

Usar los parámetros proporcionados por el usuario. Si falta el objetivo o alguno de los idiomas, pedir aclaración en vez de inventarlos:

```text
ADJETIVO = pequeño
IDIOMA_NATIVO = español
IDIOMA_DESTINO = inglés
NIVEL = principiante
FRASES = 15
TIPO = calidad
SENTIDO = de tamaño reducido
```

`NIVEL`: `principiante`, `intermedio` o `avanzado` (también se acepta `A1`–`C2`). `TIPO` es opcional. `SENTIDO` es opcional cuando el adjetivo tiene un significado claro en el contexto. Si el adjetivo es polisémico, confirmar o elegir el sentido explícitamente solicitado. Generar un archivo separado por adjetivo y sentido, salvo que el usuario pida comparar varios sentidos o adjetivos.

## Organización de la sesión

Presentar el adjetivo, modelar su uso y después espaciar las oportunidades para recuperarlo. Intercalar contextos y estructuras en lugar de agrupar todos los ejemplos de una sola forma.

### 1. Presentar el adjetivo

Comenzar con la forma de referencia y su equivalente. Si el idioma tiene flexión relevante, hacer evidente en los ejemplos posteriores cómo cambia la forma. No presentar una forma flexionada como si fuera otro adjetivo objetivo.

### 2. Asociarlo con un sustantivo familiar

Usar una combinación frecuente y fácil de imaginar. El sustantivo debe concordar con el adjetivo en cada idioma:

```text
una casa pequeña;a small house
un perro pequeño;a small dog
```

### 3. Practicar el adjetivo en una oración sencilla

Introducir el objetivo en una frase corta, con vocabulario conocido:

```text
La casa es pequeña.;The house is small.
El perro es pequeño.;The dog is small.
```

Traducir el significado de manera natural. No exigir que ambos idiomas usen la misma posición ni la misma estructura.

### 4. Reforzar las formas y funciones pertinentes

Variar género o número cuando corresponda y practicar tanto el uso junto al sustantivo como el predicativo, si son naturales:

```text
Las casas son pequeñas.;The houses are small.
Los perros son pequeños.;The dogs are small.
```

Incluir formas comparativas o superlativas únicamente cuando aporten valor pedagógico y el adjetivo lo permita:

```text
Esta casa es más pequeña.;This house is smaller.
Es la casa más pequeña.;It is the smallest house.
```

No forzar todas las formas en todos los archivos. Si la forma del adjetivo no cambia en un idioma, usar contextos que muestren el uso sin inventar flexiones.

### 5. Contextualizar y espaciar la recuperación

Avanzar desde frases simples hacia situaciones cotidianas. Reutilizar estructuras conocidas, alternar sustantivos y volver al adjetivo objetivo después de varias filas:

```text
La casa pequeña está al final de la calle.;The small house is at the end of the street.
Mi perro es pequeño, pero corre rápido.;My dog is small, but it runs fast.
¿Tienes una bolsa pequeña?;Do you have a small bag?
```

Las frases deben permitir inferir el uso, pero no depender de contextos tan rebuscados que distraigan del objetivo. Para fomentar el recuerdo, el sistema que presenta el CSV puede ocultar una columna; el archivo debe conservar ambas traducciones alineadas.

## Reglas de generación

### Repetición y variedad útil

- Mantener explícitamente el adjetivo objetivo en la mayoría de las frases.
- Repetirlo con sustantivos, sujetos y situaciones diferentes, usando vocabulario conocido.
- Alternar de forma deliberada entre uso atributivo y predicativo cuando ambos sean pertinentes.
- Reintroducir el objetivo a intervalos; no presentar todas sus formas en un único bloque.
- No sustituirlo sistemáticamente por pronombres, sinónimos, antónimos o adverbios.
- Evitar que las frases sean copias mecánicas. Cada cambio debe reforzar una combinación, función o contexto útil.

### Concordancia, posición y gramática

- Verificar género, número, orden de palabras y concordancia entre el adjetivo y el sustantivo en cada idioma.
- Usar las formas flexionadas necesarias sin tratar cada una como una palabra objetivo diferente.
- Respetar los adjetivos invariables y las reglas de posición propias de cada lengua.
- Si la posición del adjetivo altera el significado o el matiz, no mezclar los sentidos sin explicitarlo en los parámetros o separar los objetivos.
- Distinguir `ser` y `estar`, y sus equivalentes, por el significado de la frase; no afirmar que sus usos coinciden exactamente entre idiomas.
- No confundir un adjetivo con un adverbio. Si ambos se parecen formalmente, mantener el objetivo adjetival claro en la oración.
- No introducir errores deliberados como recurso de práctica. Las frases deben modelar usos correctos.

### Equivalencia y naturalidad

- Traducir el significado completo, no palabra por palabra.
- Usar el equivalente que corresponda al sentido y a la colocación de la frase.
- Comprobar que la traducción conserva el adjetivo objetivo o un equivalente funcional natural.
- Evitar frases que solo sean posibles mediante una traducción literal o que requieran un contexto improbable.
- No forzar equivalencias uno a uno cuando los idiomas expresan la idea de forma distinta.

### Progresión y nivel

- Empezar con combinaciones familiares y oraciones breves.
- Añadir solo uno o dos elementos nuevos por frase.
- Aumentar gradualmente la variedad y la longitud, sin saltar a estructuras avanzadas.
- Ajustar el vocabulario, los tiempos verbales y la gramática al nivel solicitado.
- Usar contextos concretos para principiantes; reservar sentidos abstractos, figurados o de registro especializado para niveles adecuados.

## Cantidad recomendada

Generar entre 10 y 20 frases por adjetivo, además de la fila inicial con el objetivo. Usar la cantidad solicitada si se proporcionó. No agregar filas vacías, duplicadas o variantes que solo cambien un detalle sin ofrecer una oportunidad útil de recuperación.

## Ejemplo de resultado

### Adjetivo: pequeño (tamaño reducido)

```text
pequeño;small
un perro pequeño;a small dog
El perro es pequeño.;The dog is small.
La casa es pequeña.;The house is small.
Tengo una bolsa pequeña.;I have a small bag.
Los perros pequeños juegan en el parque.;The small dogs play in the park.
La casa pequeña tiene una puerta azul.;The small house has a blue door.
Mi habitación es pequeña.;My room is small.
Estas cajas son pequeñas.;These boxes are small.
¿Es pequeño tu jardín?;Is your garden small?
La mesa pequeña está junto a la ventana.;The small table is next to the window.
Esta caja es más pequeña que la otra.;This box is smaller than the other one.
Es la habitación más pequeña de la casa.;It is the smallest room in the house.
```

## Revisión antes de entregar

Comprobar que:

1. El archivo trabaja un solo adjetivo y un sentido definido cuando sea necesario.
2. Todas las filas tienen exactamente dos campos separados por `;`, sin encabezado ni filas vacías.
3. La primera fila presenta el objetivo y un equivalente adecuado.
4. El adjetivo se repite en la mayoría de las frases y vuelve a aparecer en contextos intercalados.
5. Género, número, posición, concordancia y grados de comparación son correctos cuando aparecen.
6. Las frases distinguen correctamente el uso adjetival de otras categorías y no fuerzan estructuras entre idiomas.
7. Las traducciones son naturales y equivalentes en significado.
8. La progresión corresponde al nivel, y no hay duplicados ni complejidad innecesaria.

## Principio fundamental

El estudiante debe aprender a reconocer y recuperar el adjetivo en combinaciones y estructuras diferentes, y no solo recordar una traducción aislada. Para ello, combinar repetición espaciada, contextos variados pero familiares y modelos gramaticalmente correctos. La variedad debe reforzar el uso del objetivo, no competir con él.
