# What is special about ItWaC?
It was built by crawling Italian websites and collecting large amounts of Italian text.
It contains more than one billion words, making it one of the largest documented Italian language resources.
The texts were automatically processed with:
Part-of-speech tagging (identifying nouns, verbs, adjectives, etc.)
Lemmatization (reducing words to their base form)
Why is it used?

# Researchers and developers use ItWaC for:

# Word frequency analysis
Vocabulary extraction
Language learning resources
Lexicography (dictionary creation)
NLP model training and evaluation
Studying authentic Italian usage on the web

For example, if you want to know which Italian verbs are most common, a frequency list derived from ItWaC can provide statistically reliable counts based on billions of words.


# Propuesta de Distribución de los 12,000 Sustantivos Más Frecuentes del Italiano por Nivel CEFR

# Distribución Optimizada para una Aplicación de Aprendizaje

Si el objetivo es enseñar italiano progresivamente mediante frecuencia y utilidad práctica, una distribución más eficiente podría ser:

| Nivel | Sustantivos |
|---------|---------:|
| A1 | 500 |
| A2 | 500 |
| B1 | 1,000 |
| B2 | 2,000 |
| C1 | 3,000 |
| C2 | 5,000 |

Esta distribución refleja mejor cómo se adquiere el vocabulario en la práctica: una pequeña cantidad de palabras cubre gran parte de las conversaciones cotidianas, mientras que los niveles avanzados requieren miles de palabras adicionales para alcanzar una comprensión amplia de prensa, literatura y textos especializados.

---

# Propuesta Práctica Basada en el Ranking de Frecuencia

Si únicamente se dispone de una lista ordenada por frecuencia y se necesita una asignación automática por niveles CEFR, una aproximación razonable sería:

```text
A1: 1 - 500
A2: 501 - 1,000
B1: 1,001 - 2,000
B2: 3,001 - 6,000
C1: 6,001 - 9,000
C2: 9,001 - 12,000
```

Esta segmentación suele producir resultados bastante cercanos a los niveles CEFR observados en estudiantes de idiomas europeos y constituye un buen punto de partida para clasificar automáticamente un vocabulario basado en frecuencia.