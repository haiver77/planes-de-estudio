# Generador de CSV para Aprendizaje de Vocabulario de Objetos por Repetición

## Objetivo

Generar archivos CSV para el aprendizaje de vocabulario relacionado con objetos mediante repetición progresiva y contextualizada.

Cada archivo debe enfocarse en un único objeto o concepto concreto y presentar frases simples, repetitivas y fáciles de comprender que permitan al estudiante adquirir el vocabulario de forma natural.

El objetivo principal no es la variedad de frases, sino la exposición repetida al mismo objeto en múltiples contextos sencillos.

---

# Formato del CSV

Cada fila debe contener exactamente dos columnas separadas por punto y coma (`;`):

```text
Frase en español;Frase en idioma destino
```

Ejemplo:

```text
el libro.;the book.
yo veo el libro.;I see the book.
yo tengo el libro.;I have the book.
```

---

# Enfoque Pedagógico

Las frases deben construirse de forma incremental.

Cada nueva frase debe reutilizar el objeto principal y la mayor cantidad posible de vocabulario previamente introducido, agregando únicamente uno o pocos elementos nuevos.

Esto permite que el estudiante:

- Memorice el nombre del objeto.
- Aprenda los artículos asociados.
- Aprenda adjetivos básicos.
- Aprenda vocabulario contextual relacionado.
- Vea el objeto en múltiples situaciones de uso.
- Refuerce naturalmente estructuras gramaticales simples.

---

# Principio Fundamental

La prioridad absoluta es la repetición controlada.

El mismo objeto debe aparecer constantemente a lo largo de todo el bloque.

Por ejemplo, si el objeto es:

```text
libro
```

la mayoría de las frases deben contener explícitamente la palabra:

```text
libro
```

No deben utilizarse numerosos sinónimos ni reemplazos que reduzcan la repetición.

---

# Estructura General

Cada archivo debe estar centrado en un único objeto.

Ejemplos:

```text
libro
mesa
silla
ventana
pelota
lápiz
cuaderno
mochila
cuchara
teléfono
```

---

# Progresión Recomendada

Las frases deben avanzar gradualmente siguiendo esta secuencia.

## Nivel 1: Objeto aislado

Presentar únicamente la palabra objetivo.

```text
libro
```

---

## Nivel 2: Artículo + Objeto

Introducir el artículo correspondiente.

```text
el libro
```

o

```text
la mesa
```

---

## Nivel 3: Identificación básica

Construcciones simples de reconocimiento.

```text
es un libro
es una mesa
```

---

## Nivel 4: Descripción simple

Agregar adjetivos de alta frecuencia.

```text
el libro es grande
el libro es pequeño
el libro es nuevo
el libro es viejo
```

---

## Nivel 5: Posesión

Introducir pronombres posesivos.

```text
mi libro
tu libro
su libro
nuestro libro
```

---

## Nivel 6: Ubicación

Introducir localización física.

```text
el libro está aquí
el libro está allí
el libro está sobre la mesa
el libro está en la mochila
```

---

## Nivel 7: Interacción con el objeto

Introducir acciones comunes asociadas al objeto.

```text
yo veo el libro
yo tengo el libro
yo uso el libro
yo llevo el libro
```

---

## Nivel 8: Contexto temporal

Agregar referencias temporales simples.

```text
hoy, yo uso el libro
mañana, yo uso el libro
```

---

## Nivel 9: Situaciones cotidianas

Utilizar contextos simples y familiares.

```text
yo uso el libro en la escuela
yo llevo el libro al parque
yo tengo el libro en mi mochila
```

---

# Selección de Verbos de Apoyo

Los verbos utilizados deben ser simples y de alta frecuencia.

Ejemplos:

```text
tener
ver
usar
llevar
abrir
cerrar
guardar
encontrar
mostrar
necesitar
```

No se deben utilizar verbos avanzados o poco frecuentes.

---

# Reglas de Generación

## Simplicidad

- Utilizar vocabulario cotidiano.
- Utilizar frases cortas.
- Evitar estructuras complejas.

## Repetición

- Mantener visible el objeto principal en la mayoría de las frases.
- Reutilizar palabras ya introducidas.
- Reforzar continuamente el vocabulario objetivo.

## Aprendizaje Progresivo

- Introducir solamente uno o dos conceptos nuevos por frase.
- Construir cada nueva frase a partir de frases anteriores.

## Contextualización

- Relacionar el objeto con situaciones reales y fáciles de visualizar.
- Utilizar ubicaciones comunes.
- Utilizar actividades cotidianas.

## Comprensibilidad

- Mantener nivel principiante.
- Evitar lenguaje abstracto.
- Priorizar conceptos concretos y visuales.

---

# Cantidad Recomendada

Generar entre 10 y 20 frases por objeto.

Ejemplo:

```text
1 objeto = 15 frases
```

o

```text
1 objeto = 20 frases
```

---

# Parámetros de Entrada

El generador debe aceptar parámetros similares a los siguientes:

```text
OBJETO = libro
IDIOMA_DESTINO = inglés
NIVEL = principiante
FRASES_POR_OBJETO = 15
```

Ejemplos válidos:

```text
OBJETO = libro
OBJETO = mesa
OBJETO = silla
OBJETO = teléfono
OBJETO = mochila
OBJETO = pelota
OBJETO = taza
OBJETO = cuchara
```

---

# Ejemplo de Resultado Esperado

## Objeto: libro

```text
libro;book

el libro.;the book.
es un libro.;it is a book.
el libro es grande.;the book is big.
el libro es pequeño.;the book is small.
mi libro.;my book.
tu libro.;your book.
el libro está aquí.;the book is here.
el libro está allí.;the book is there.
yo veo el libro.;I see the book.
yo tengo el libro.;I have the book.
yo uso el libro.;I use the book.
yo llevo el libro.;I carry the book.
hoy, yo uso el libro.;today, I use the book.
mañana, yo uso el libro.;tomorrow, I use the book.
yo uso el libro en la escuela.;I use the book at school.
```

---

# Objetivo Fundamental

La meta es que el estudiante adquiera el vocabulario mediante exposición repetida al mismo objeto en distintos contextos simples.

No intentar maximizar creatividad, variedad o complejidad.

La repetición debe ser intencional y sistemática.

El estudiante debe encontrar constantemente:

- El mismo objeto.
- Los mismos verbos frecuentes.
- Los mismos patrones de oración.
- Contextos fáciles de comprender.

Esto permite que la asociación entre la palabra, su significado y su uso se vuelva automática mediante repetición comprensible.