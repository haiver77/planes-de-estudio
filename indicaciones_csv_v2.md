# Indicaciones para diseñar las sesiones CSV para vocabulario foco que son frases

## Progresión del vocabulario

- Introduce un solo elemento de vocabulario foco a la vez.
- Si el foco es una frase, preséntala primero por separado cuando sea gramaticalmente posible.
- Después, úsala en ejemplos que aumenten gradualmente en extensión o complejidad. Puedes variar los contextos.
- Consolida el foco con varios ejemplos antes de introducir el siguiente.

**Ejemplo: foco «get up»**

```csv
Levantarse;Get up
Me levanto a las siete.;I get up at seven.
yo me levanto temprano,I get up early
Mi padre se levanta temprano.;My father gets up early.
Ellos se levantan antes del desayuno.;They get up before breakfast.
Ella se levantó tarde el domingo.;She got up late on Sunday.
El bebé se levanta cuando oye a su madre.;The baby gets up when he hears his mother.
Me levanto y abro las cortinas.;I get up and open the curtains.
Mi hermano se levanta para preparar el desayuno.;My brother gets up to make breakfast.
¿A qué hora te levantas para ir a la escuela?;What time do you get up for school?
Los sábados, mi familia se levanta tarde y desayuna junta.;On Saturdays, my family gets up late and has breakfast together.
```

## Frases naturales y coherentes

Cada frase debe tener sentido y sonar como algo que una persona diría. Evita mezclar elementos o contextos sin una relación lógica.

**Evita ejemplos como estos:**

```csv
En casa el jueves, ¿quién es tu maestro?;At home on Thursday, who is your teacher?
En el mercado el jueves, el tráfico está en la imagen.;At the market on Thursday, the traffic is in the picture.
En la parada del autobús el viernes, en casa ya está listo para clase.;At the bus stop on Friday, at home, it is ready for class.
```

## Pronombres claros en español

Cuando el sujeto en inglés sea *he*, *she* o *they*, incluye en español un pronombre o sujeto explícito que permita identificarlo. No omitas el sujeto si eso hace ambigua la traducción.

**Claro:**

```csv
Ella no tiene una familia grande.;She has not got a big family.
El jueves por la noche, ellos llegan al mismo tiempo.;On Thursday evening, they arrive at the same time.
```

**Ambiguo:**

```csv
Tiene una familia grande.;She has got a big family.
El jueves por la noche, llegan al mismo tiempo.;On Thursday evening, they arrive at the same time.
```

## Construcción gradual de ejemplos

Empieza con el vocabulario foco y añade información poco a poco, sin perder naturalidad.

**Ejemplo: foco «a bit»**

```csv
Un poco;A bit
Estoy un poco cansado.;I am a bit tired.
Hace un poco de frío.;It is a bit cold.
La tienda está un poco lejos.;The shop is a bit far away.
```

## No mezcles inglés en la frase en español

La columna en español debe expresar el significado, no mencionar ni citar la frase inglesa foco.

**Evita:**

```csv
Leo la expresión «at home» en la página.;I read the phrase “at home” on the page.
Mi profesor explica la expresión «at school» después de clase.;My teacher explains the phrase “at school” after class.
```

# Reglas para el validador

A continuación, las reglas que debe aplicar el agente validador.

Reglas generales por archivo csv:
- **Regla: Progresion y repetición incremental:** Inserta el vocabulario foco comenzando con ejemplos simples e independientes cuando sea gramaticalmente apropiado, y lo refuerza mediante repeticiones graduales en distintos contextos antes de introducir un nuevo vocabulario foco.
- **Regla: Cobertura:** exactamente un CSV por cada ID del nivel en el plan.
- **Regla: Formato y codificación:** UTF-8 válido; dos columnas sin encabezado (español; inglés) separadas por `;`
- **Regla: Cantidad:** cada CSV tiene al menos el mínimo de frases indicado.

Reglas por linea:
- **Regla: Frase con sentido:** Salvo la primera aparición del vocabulario objetivo, que puede mostrarse de forma aislada cuando resulte natural, para todas las demás asegurate que la frase tenga sentido completo y pueda utilizarse de forma independiente. En caso de no cumplir con la regla, sugerir la nueva frase con sentido con la que debería reemplazarse, asegurate de no sugerir una frase que ya existe.
- **Regla: Sin caracteres extraños** Rechaza comas como delimitador, `;`, filas vacías, campos extra, comillas mal cerradas, columnas invertidas y saltos de línea dentro de filas. Revisa que `á é í ó ú ü ñ ¿ ¡` estén correctos; señala `?` sustituyendo.letras y texto corrupto (`Ã¡`, `Ã±`, `�`). Las preguntas en español exigen `¿`; el `?` de cierre es válido.
- **Regla: Desambiguación de sujeto** Detecta casos donde el sujeto en español no permite identificar inequívocamente el pronombre utilizado en inglés. 