# Informe de auditoría — A1, iteración 1

**Alcance:** únicamente `A1-S001.csv` a `A1-S005.csv`, cotejados con las sesiones A1-S001–A1-S005 del plan aprobado de la iteración 11. No se revisaron otros archivos del nivel.

**Resultado:** requiere correcciones y otra iteración. Los problemas lingüísticos, de sentido y de progresión que siguen impiden aprobar estos CSV.

## Comprobaciones automáticas y cobertura

- En la carpeta revisada están exactamente los cinco archivos solicitados; corresponden a los cinco IDs del plan, sin faltantes ni archivos ajenos.
- Los cinco archivos tienen **150 filas cada uno** (150 pares por CSV).
- La lectura estricta UTF-8 fue válida. Los cinco se interpretan como CSV sin encabezado: dos campos por fila, separados por `;`; no se encontraron filas vacías, filas con campos adicionales, delimitadores alternativos, comillas desbalanceadas, mojibake ni signos de interrogación españoles sin apertura. No hay pares duplicados exactos.
- Las unidades léxicas previstas aparecen representadas, y hay muestras de los focos gramaticales programados. Esto no subsana los ejemplos defectuosos ni las secuencias artificiales descritas a continuación.

## Observaciones prioritarias

### Prioridad alta — corregir sentido, equivalencia y naturalidad

1. **A1-S002.csv, filas 46–50, 110 y 134 — uso literal e inverosímil de “a period of time”.** Ejemplos: `Ella trae un período de tiempo al picnic.;She brings a period of time to the picnic.` (48), `Mi familia compra un tiempo en la tienda.;My family buys a period of time at the shop.` (49) y `We take a period of time to school` (110). El giro se trata como objeto que se trae o compra y varias traducciones no son inglés natural. Sustituir estos pares por situaciones en que el lapso temporal sea realmente la duración o el tiempo disponible; traducir con una construcción idiomática y mantener el sentido de la frase española.

2. **A1-S003.csv, fila 28 — traducción incorrecta.** `En casa el sábado, lo veo en la mesa.;At home on Saturday, I see its at the table.` “Its” no puede funcionar como objeto directo aquí. Precisar el referente (persona u objeto) en español y traducirlo con el pronombre inglés correcto; por ejemplo, nombrar un objeto y usar “I see it on the table”.

3. **A1-S003.csv, fila 26 — frase incompleta/ambigua.** `Veo pocos en la mesa.;I see few at the table.` “Pocos/few” necesita un referente contable explícito en este contexto. Indicar qué se ve (por ejemplo, “Veo pocos platos en la mesa / I see few plates on the table”) o rehacer el par con un sustantivo coherente en ambos idiomas.

4. **A1-S004.csv, filas 21–25 — ejemplos semánticamente absurdos para “the bad things about sth”.** Entre ellos: `Lo malo del libro lo tenemos para almorzar.;We have the bad things about the book for lunch.` (22), traer “las cosas malas del libro” a un picnic (23) y comprarlas en una tienda (24). No son usos naturales de la expresión y algunos traducen literalmente una combinación sin sentido. Reescribir la serie con situaciones plausibles sobre aspectos negativos de un libro/plan/producto y traducciones idiomáticas; no presentar esos “bad things” como comida u objetos comprables.

5. **A1-S005.csv, fila 12 — cambio de perspectiva en la traducción.** `Puedo ir a la fiesta.;I can come to the party.` Sin un contexto que sitúe al hablante en el destino, “ir” corresponde a “go”, no “come”. Cambiar el inglés a “I can go to the party” o establecer explícitamente un contexto que justifique “come”.

6. **A1-S005.csv, fila 24 — acto de habla poco natural para una pregunta.** `En la escuela, le pregunto a mi maestro: “Entró al salón”.;At school, I ask my teacher, “He came into the room.”` La cita es una afirmación, no una pregunta que normalmente se haría al maestro; además, el ejemplo fuerza una situación poco verosímil. Crear un intercambio natural que use la expresión objetivo y conserve claramente quién pregunta y qué quiere saber.

### Prioridad media — realinear el contexto, la progresión y el repaso

7. **A1-S003.csv, fila 5 — contradicción temporal:** `El viernes por la tarde, llego a la escuela todas las mañanas.` La circunstancia puntual de viernes por la tarde no concuerda con “todas las mañanas”. Corregir el marco temporal o reformular la oración para que ambas partes sean compatibles.

8. **A1-S003.csv, filas 6–10 — tiempo verbal adelantado y repetición mecánica.** `Pedí un vaso de agua` se traduce con pasado simple (`I asked`) aunque el foco de esta sesión es *have got/has got* y posesivos; las filas siguientes repiten casi la misma petición añadiendo días u horas. Mantener el ejemplo dentro de los objetivos ya introducidos —o justificarlo como expresión memorizada si el plan lo prevé— y convertir la serie en práctica variada con propósito, no en copias con marcas horarias.

9. **A1-S002.csv, fila 27 — contexto contradictorio:** `En casa, comemos todo nuestro almuerzo en la escuela.;At home, we eat all our lunch at school.` Corregir el lugar o la acción para que casa y escuela no se contradigan. La fila 30 vuelve a combinar “en casa” con comer en la escuela; revisar también esa variante.

10. **A1-S002.csv, fila 21 — inglés poco idiomático:** `Ella conoce a toda mi familia.;She knows all my family.` Cambiar a “She knows my whole family” (o una formulación natural equivalente).

11. **A1-S005.csv, filas 4–5 — acumulación temporal confusa y duplicación.** Las dos filas anteponen “El lunes por la mañana/tarde” a `hoy vivo lejos del centro de la ciudad` y repiten la misma afirmación. Eliminar el choque entre “hoy” y el marco añadido o rehacer ambas como ejemplos distintos y contextualizados.

12. **Patrón de progresión y transferencia — A1-S001.csv, fila 97; A1-S002.csv, filas 29–30; A1-S005.csv, filas 26–30.** Se añaden lugares, días u horas a una oración ya completa sin que aporten una situación comunicativa clara; algunos insertos vuelven la frase extraña (por ejemplo, `En casa, los años pasan rápidamente.`) y otros repiten la misma oración con otro día. Sustituir estas variantes por mini-secuencias con continuidad lógica, longitud progresiva y transferencia a contextos diferentes; cada fila debe seguir siendo natural y comprensible por separado.

Antes de volver a solicitar aprobación, corregir las filas señaladas, comprobar que el foco de cada sesión no se desplace por ejemplos fuera de progresión y repetir la validación de los cinco CSV.
