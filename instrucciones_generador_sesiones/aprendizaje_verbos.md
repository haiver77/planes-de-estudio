# Generador de CSV para Aprendizaje de Vocabulario por Repetición

## Objetivo

Generar archivos CSV para aprendizaje de idiomas mediante repetición progresiva. Cada archivo debe enfocarse en un único verbo y presentar frases simples y repetitivas que permitan al estudiante internalizar tanto el vocabulario como la conjugación de manera natural.

El objetivo principal no es la variedad de frases, sino la exposición repetida al mismo verbo en múltiples contextos sencillos.

---

## Formato del CSV

Cada fila debe contener exactamente dos columnas separadas por punto y coma (`;`), sin encabezado ni filas vacías. La primera columna contiene el texto en el idioma nativo y la segunda su traducción al idioma destino. No usar punto y coma dentro de una frase.

```text
Texto en idioma nativo;Texto en idioma destino
```

La primera fila presenta el verbo y su equivalente; las siguientes contienen frases emparejadas:

```text
yo corro.;I run.
yo corro rápido.;I run fast.
yo corro en el parque.;I run in the park.
```

---

## Enfoque Pedagógico

Las frases deben construirse de forma incremental.

Cada nueva frase debe reutilizar la mayor cantidad posible de vocabulario previamente introducido y agregar únicamente uno o pocos elementos nuevos.

Esto permite que el estudiante:

- Refuerce el verbo principal.
- Memorice las conjugaciones.
- Aprenda vocabulario por repetición.
- Identifique patrones gramaticales de forma natural.
- Desarrolle comprensión sin necesidad de explicaciones gramaticales complejas.

---

## Estructura General

Generar un bloque por cada conjugación que corresponda al idioma nativo. La cantidad indicada en `FRASES` se aplica a cada bloque y no incluye la fila inicial del verbo.

Cada bloque debe seguir exactamente el mismo patrón de complejidad.

### Conjugaciones de referencia

```text
yo
tú
él
ella
ellos
ellas
nosotros
nosotras
```

---

## Progresión Recomendada

Cada bloque debe avanzar gradualmente siguiendo una secuencia similar a la siguiente:

1. Verbo en infinitivo.
2. Sujeto + verbo.
3. Sujeto + verbo + adverbio.
4. Sujeto + verbo + complemento de lugar.
5. Sujeto + verbo + complemento temporal.
6. Sujeto + verbo + expresión de frecuencia.
7. Sujeto + verbo + objeto.
8. Sujeto + verbo + objeto + adjetivo.
9. Frases introducidas por marcadores temporales.
10. Frases contextualizadas.

---

## Ejemplo de Progresión

### Verbo: correr

```text
correr

yo corro.
yo corro rápido.
yo corro despacio.
yo corro en el parque.
yo corro en la mañana.
yo corro todos los días.
yo corro una carrera.
yo corro una carrera larga.
hoy, yo corro una carrera.
mañana, yo corro una carrera.
```

---

## Reglas de Generación

### Simplicidad

- Utilizar vocabulario de uso frecuente.
- Evitar tecnicismos.
- Utilizar estructuras comunes del lenguaje cotidiano.

### Repetición

- Repetir constantemente el verbo objetivo.
- Repetir estructuras previamente utilizadas.
- Priorizar refuerzo sobre variedad.

### Dificultad

- Mantener nivel principiante.
- Introducir vocabulario nuevo gradualmente.
- Agregar máximo uno o dos conceptos nuevos por frase.

### Longitud

- Mantener oraciones cortas.
- Evitar frases largas o complejas.
- Evitar subordinadas avanzadas.

### Consistencia

- Mantener el mismo tiempo verbal dentro de un bloque.
- Mantener el mismo sujeto durante todo el bloque.
- Mantener el mismo verbo objetivo durante todo el archivo.

### Naturalidad

- Las traducciones deben ser naturales para hablantes nativos.
- Evitar traducciones literales incorrectas.
- Mantener expresiones comunes y fáciles de recordar.

---

## Cantidad Recomendada

Generar entre 10 y 20 frases por cada conjugación.

Ejemplo:

```text
8 conjugaciones × 15 frases = 120 frases, más 1 fila inicial del verbo
```

---

## Parámetros de Entrada

Usar los parámetros proporcionados por el usuario. Si falta el objetivo o alguno de los idiomas, pedir aclaración en vez de inventarlos:

```text
VERBO = correr
IDIOMA_NATIVO = español
IDIOMA_DESTINO = inglés
NIVEL = principiante
FRASES = 15
TIPO = regular
SENTIDO = moverse rápidamente a pie
```

- `NIVEL`: `principiante`, `intermedio` o `avanzado` (también se acepta `A1`–`C2`).
- `FRASES`: cantidad de frases por cada conjugación.
- `TIPO` y `SENTIDO` son opcionales. Usarlos si el verbo es irregular, reflexivo o polisémico.

Ejemplos válidos:

```text
VERBO = comer
VERBO = beber
VERBO = leer
VERBO = escribir
VERBO = caminar
VERBO = hablar
VERBO = estudiar
VERBO = trabajar
```

---

## Ejemplo de Resultado Esperado

### Verbo: comer

```text
comer;to eat
yo como.;I eat.
yo como rápido.;I eat quickly.
yo como una manzana.;I eat an apple.
yo como en la cocina.;I eat in the kitchen.
yo como todos los días.;I eat every day.
hoy, yo como una manzana.;today, I eat an apple.
él come.;he eats.
él come rápido.;he eats quickly.
él come una manzana.;he eats an apple.
él come en la cocina.;he eats in the kitchen.
él come todos los días.;he eats every day.
hoy, él come una manzana.;today, he eats an apple.
```

---

## Objetivo Fundamental

La prioridad absoluta es la repetición controlada.

Las frases deben ser muy similares entre sí para que el estudiante vea repetidamente:

- El mismo verbo.
- Las mismas conjugaciones.
- El mismo vocabulario.
- Las mismas estructuras.

La repetición debe ser intencional y sistemática.

No intentar maximizar variedad, creatividad o complejidad.

La meta es que el estudiante adquiera el vocabulario y pueda usar el verbo objetivo en contextos sencillos con las conjugaciones pertinentes.