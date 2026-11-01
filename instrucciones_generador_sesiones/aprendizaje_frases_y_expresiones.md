# Generador de CSV para Sesiones de Aprendizaje de Frases y Expresiones

## Objetivo General

Generar archivos CSV para el aprendizaje de idiomas mediante repetición progresiva, comprensión contextual y exposición controlada.

El sistema debe ser independiente del idioma. Los idiomas, nivel de dificultad, cantidad de frases y demás parámetros serán proporcionados durante la ejecución.

Cada CSV debe ayudar al estudiante a:

- Comprender una expresión o estructura.
- Reconocer patrones de uso reales.
- Adquirir vocabulario de forma natural.
- Mejorar la fluidez mediante repetición.
- Practicar pronunciación.
- Internalizar expresiones completas en lugar de aprender palabras aisladas.

La prioridad es la repetición comprensible y gradual, no la creatividad ni la variedad extrema.

---

# Formato del CSV

Cada fila debe contener exactamente dos columnas separadas por punto y coma (`;`).

```text
Texto en idioma nativo;Texto en idioma objetivo
```

Ejemplo:

```text
Yo manejo el estrés.;I cope with stress.
```

```text
Me resulta difícil concentrarme.;I find it difficult to concentrate.
```

```text
Depende de la situación.;It depends on the situation.
```

---

# Parámetros de Entrada

Los siguientes parámetros serán proporcionados al agente durante la ejecución.

## Idiomas

```text
IDIOMA_NATIVO
IDIOMA_OBJETIVO
```

Ejemplos:

```text
IDIOMA_NATIVO = español
IDIOMA_OBJETIVO = inglés
```

```text
IDIOMA_NATIVO = español
IDIOMA_OBJETIVO = italiano
```

```text
IDIOMA_NATIVO = inglés
IDIOMA_OBJETIVO = francés
```

---

## Nivel

```text
NIVEL
```

Posibles valores:

```text
A1
A2
B1
B2
C1
C2
```

El vocabulario y complejidad gramatical deben ajustarse estrictamente al nivel solicitado.

---

## Tipo de Sesión

```text
TIPO_SESION
```

Posibles valores:

```text
verbo
objeto
phrasal_verb
grammar_pattern
quantity_expression
discourse_connector
fixed_expression
```

---

## Elemento Objetivo

```text
ELEMENTO
```

Ejemplos:

```text
run
book
cope with
because of
it depends
lots of
be supposed to
```

---

## Cantidad de Frases

```text
CANTIDAD_FRASES
```

El generador debe producir aproximadamente esta cantidad de frases.

---

# Reglas Generales

## Repetición Dirigida

La expresión objetivo debe aparecer repetidamente durante toda la sesión.

No sustituir constantemente la expresión por sinónimos.

La exposición repetida es obligatoria.

---

## Aprendizaje Incremental

Cada nueva frase debe introducir como máximo:

```text
1 concepto nuevo
```

o

```text
2 conceptos nuevos
```

Nunca introducir muchos conceptos nuevos en la misma frase.

---

## Comprensibilidad

Las frases deben ser:

- Claras.
- Naturales.
- Fáciles de imaginar.
- Fáciles de pronunciar.
- Adecuadas para el nivel solicitado.

---

## Longitud

Preferir:

```text
frases cortas
```

o

```text
frases medianas
```

Evitar oraciones innecesariamente complejas.

---

## Naturalidad

Las frases deben sonar naturales para hablantes nativos.

No generar ejemplos artificiales únicamente para cumplir una estructura.

---

## Traducción

La traducción debe:

- Conservar el significado completo.
- Utilizar equivalentes naturales.
- Respetar el nivel lingüístico solicitado.
- Mantener el mismo registro comunicativo.
- Evitar traducciones literales incorrectas.
- Preservar la intención original de la frase.

---

## Temáticas Preferidas

Priorizar contextos relacionados con:

```text
vida diaria
familia
hogar
escuela
universidad
trabajo
tecnología
amistades
compras
viajes
salud
ocio
```

---

# FAMILIA 1: PHRASAL VERBS Y EXPRESIONES VERBALES

## Descripción

Expresiones centradas en acciones.

Normalmente contienen un verbo acompañado por una preposición o partícula que modifica el significado.

Ejemplos:

```text
cope with sth
deal with sth
focus on sth
search for sth
get rid of sth
get over sth
figure out sth
come across sth
participate in sth
rely on sth
respond to sth
```

## Objetivo de Aprendizaje

El estudiante debe aprender la expresión como una unidad indivisible.

No debe intentar traducir cada palabra por separado.

Debe reconocer automáticamente el significado general y el contexto adecuado para utilizarla.

## Patrón de Generación

### Etapa 1

Presentación de la expresión.

```text
Expresión
Traducción
```

### Etapa 2

Frases mínimas.

```text
Frase simple 1
Frase simple 2
Frase simple 3
```

### Etapa 3

Variaciones controladas.

Modificar únicamente:

```text
objeto
lugar
persona
tiempo
```

manteniendo la expresión principal.

### Etapa 4

Contextos cotidianos.

```text
hogar
escuela
trabajo
```

### Etapa 5

Situaciones reales.

### Etapa 6

Pregunta y respuesta.

## Cantidad Recomendada

```text
12 a 18 frases
```

---

# FAMILIA 2: PATRONES GRAMATICALES

## Descripción

Estructuras reutilizables con componentes variables.

Ejemplos:

```text
be allowed to do sth
be expected to do sth
be supposed to do sth
would rather
be about to do sth
manage to do sth
learn how to do sth
prepared to do sth
seek to do sth
tend to do sth
```

## Objetivo de Aprendizaje

El estudiante debe dominar la estructura completa y reutilizarla con diferentes verbos y sujetos.

## Patrón de Generación

### Etapa 1

Presentación del patrón.

```text
Patrón
Significado
```

### Etapa 2

Misma estructura con verbos diferentes.

### Etapa 3

Misma estructura con sujetos diferentes.

```text
I
You
He
She
We
They
```

### Etapa 4

Aplicación en situaciones reales.

### Etapa 5

Pregunta y respuesta.

## Cantidad Recomendada

```text
15 a 20 frases
```

---

# FAMILIA 3: EXPRESIONES DE CANTIDAD Y FRECUENCIA

## Descripción

Expresiones relacionadas con cantidad, frecuencia o intensidad.

Ejemplos:

```text
lots of
loads of
a bit of
millions of
quite a lot
more than
less than
far too
x times a week
```

## Objetivo de Aprendizaje

Asociar la expresión con cantidades reales y usos frecuentes.

## Patrón de Generación

### Etapa 1

Presentación de la expresión.

### Etapa 2

Expresión más sustantivo.

```text
lots of people
lots of books
lots of students
```

### Etapa 3

Oraciones simples.

### Etapa 4

Contextos cotidianos.

### Etapa 5

Comparaciones simples.

## Cantidad Recomendada

```text
12 a 15 frases
```

---

# FAMILIA 4: CONECTORES Y MARCADORES DISCURSIVOS

## Descripción

Expresiones utilizadas para conectar ideas o expresar relaciones lógicas.

Ejemplos:

```text
because of
as a result
in contrast
on the other hand
in addition
instead of
in my opinion
```

## Objetivo de Aprendizaje

Comprender la función comunicativa del conector y aplicarlo correctamente.

## Patrón de Generación

### Etapa 1

Presentación del conector.

### Etapa 2

Dos ideas relacionadas mediante el conector.

```text
Idea A
Conector
Idea B
```

### Etapa 3

Oraciones completas.

### Etapa 4

Contextos progresivamente más complejos.

### Etapa 5

Mini situaciones.

Ejemplos:

```text
problema → causa → resultado
```

o

```text
idea → contraste
```

según corresponda.

## Cantidad Recomendada

```text
10 a 15 frases
```

---

# FAMILIA 5: EXPRESIONES FIJAS Y BLOQUES CONVERSACIONALES

## Descripción

Expresiones utilizadas como unidades completas dentro de conversaciones cotidianas.

Ejemplos:

```text
it depends
i guess
oh well
oh dear
you see
have a look
have no idea
how about...?
what about...?
```

## Objetivo de Aprendizaje

Desarrollar respuestas automáticas y naturales en conversaciones.

## Patrón de Generación

### Etapa 1

Presentación de la expresión.

### Etapa 2

Uso mínimo.

```text
It depends.
```

### Etapa 3

Uso contextual.

### Etapa 4

Mini diálogos.

### Etapa 5

Conversaciones cotidianas.

## Cantidad Recomendada

```text
10 a 15 frases
```

---

# Patrón Universal de Respaldo

Cuando una expresión no encaje claramente en una familia específica, utilizar el siguiente patrón universal.

```text
1. Expresión

2. Traducción

3. Frase mínima

4. Variación simple 1

5. Variación simple 2

6. Variación simple 3

7. Contexto cotidiano

8. Contexto académico

9. Contexto laboral

10. Situación real

11. Pregunta

12. Respuesta usando la expresión
```

---

# Principio Fundamental

El objetivo principal no es que el estudiante vea muchas frases diferentes.

El objetivo principal es que el estudiante vea repetidamente la misma expresión en múltiples contextos comprensibles hasta que pueda reconocerla, comprenderla y utilizarla automáticamente.

La repetición debe ser:

```text
intencional
sistemática
progresiva
comprensible
natural
```

Cada nueva frase debe reforzar lo aprendido en las frases anteriores mientras añade únicamente una pequeña cantidad de información nueva.