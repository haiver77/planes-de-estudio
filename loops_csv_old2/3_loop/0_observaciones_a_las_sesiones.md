# Informe de auditor?a ? A1, iteraci?n 2

**Alcance:** exclusivamente `A1-S001.csv` a `A1-S005.csv` en `loops_csv/2_loop/A1`, cotejados con las cinco sesiones A1-S001?A1-S005 del plan aprobado y con las observaciones pendientes de la iteraci?n anterior. No se revisaron otros CSV ni `loops_csv_old`.

**Resultado:** requiere correcciones y otra iteraci?n. Aunque las cantidades y la estructura b?sica cumplen, quedan errores de caracteres, equivalencia, gram?tica, sentido, progresi?n y uso de contextos.

## Comprobaciones autom?ticas y cobertura

- La carpeta revisada contiene exactamente los cinco IDs solicitados, sin faltantes ni archivos ajenos.
- Cada archivo tiene **150 l?neas/pares**, cumpliendo el m?nimo obligatorio de 150.
- Los cinco archivos se decodifican estrictamente como UTF-8. La lectura con parser CSV en cada l?nea confirma dos campos separados por un ?nico `;`, sin encabezado, filas vac?as, campos adicionales ni comillas mal cerradas. No hay pares exactos duplicados.
- Sin embargo, existen signos ASCII `?` que sustituyen caracteres o puntuaci?n, detallados abajo. Por tanto, que la secuencia de bytes sea UTF-8 v?lida no significa que todo el texto est? correctamente codificado.

## Observaciones prioritarias

### Prioridad alta ? corregir caracteres, sentido y traducci?n

1. **Caracteres sustituidos y puntuaci?n corrompida ? varios archivos.** Reemplazar los `?` literales que no son signos de cierre v?lidos y verificar el car?cter exacto en el CSV guardado:
   - `A1-S001.csv`, fila 101: `??Buena idea! ...?` / `?Good idea! ...?`. Los signos rodean una exclamaci?n/afirmaci?n como si fuera pregunta y no son delimitadores adecuados. Reescribir la cita con comillas y puntuaci?n natural en ambos idiomas (por ejemplo, `En casa respondo: ??Buena idea! El parque est? cerca de aqu?.?;At home, I reply, ?Good idea! The park is nearby.?`).
   - `A1-S002.csv`, filas 25 y 66: `caf?`; corregir a `caf?` en ingl?s (`caf?` o `cafe`, sin sustituir la vocal por `?`).
   - `A1-S003.csv`, filas 13, 20 y 110: `caf?`; corregir a `caf?`/`cafe`.
   - `A1-S004.csv`, fila 55: `caf?`; corregir a `caf?`/`cafe`. Fila 140: `??Buena idea!...?` y su traducci?n `?Good idea!...?`; reformular con comillas y puntuaci?n de afirmaci?n/exclamaci?n, no con interrogaciones.

2. **A1-S002.csv, filas 103, 125, 127?128 y 138 ? significado inveros?mil y mezcla de contextos.** `En casa, trae mucho que hacer al picnic.;At home, she brings a lot to do to the picnic` trata ?mucho que hacer? como objeto que se lleva; `En casa eso es un poco de az?car para mi cuarto.;At home, that is a little sugar for my room` carece de situaci?n l?gica; `compartimos muchas cosas que hacer` (127) y `guarda gran parte del libro en su bolso` (128) son construcciones literales/ambiguas. Adem?s, 138 acumula ?Cerca de la estaci?n? y ?en la escuela? sin relaci?n clara. Reescribir esos pares con acciones plausibles, referente expl?cito y contexto ?nico; no basta con cambiar el d?a o el lugar.

3. **A1-S003.csv, filas 108?115, 131, 133, 139, 144?145 y 149 ? errores sem?nticos o traducciones inadecuadas.** En 108, `Lo usamos en casa.;We use him at home` asigna a `lo` un referente humano no indicado; en 144, `We use its at home` usa incorrectamente el posesivo `its` como objeto. Especificar el referente y usar `it/him` seg?n corresponda. En 109 y 145, `esto/esa es clave` significa ?this/that is key?, no `a key`; corregir traducci?n o cambiar el espa?ol si se habla de una llave f?sica. La fila 111, `Nos reunimos en el caf? justo.;We meet at the caf? just`, es una traducci?n literal no natural: rehacer con un sentido definido. La 112, `Veo a mi hombre...;I see my man...`, resulta impropia/ambigua sin contexto; usar una relaci?n o persona concreta natural. La 115 (`El fin de semana es una bolsa.;At the weekend, this is a bag`) no conserva el sentido y cambia el sujeto: sustituir el par completo. En 131 falta sujeto espa?ol para el `he` ingl?s (`mete mucho`); en 133 `eso es mucho libro` es poco idiom?tico y no aclara la cantidad. En 139, `veo un periodo de tiempo sobre la mesa`, vuelve a tratar un lapso temporal como objeto visible. En 149, `Veo suficiente en la mesa.;I see enough at the table` no identifica qu? es suficiente. Reescribir estas frases con sujetos y referentes expl?citos, significado coherente e ingl?s idiom?tico.

4. **A1-S005.csv, fila 121 ? contradicci?n de tiempo verbal.** `Nos quedamos dentro por la lluvia.;We stayed inside because of the rain` presenta pasado en ingl?s y presente en espa?ol. Alinear ambos tiempos (`We stay inside...` o expresar el pasado en espa?ol).

5. **A1-S005.csv, filas 135, 137?139, 142?145 ? combinaci?n incompatible de lugares.** Ejemplos: `En nuestra ciudad..., en casa necesitamos...` (135), `En el autob?s, en casa veo...` (137), y `En el autob?s..., en casa...` en 138?145. Se atribuye una acci?n simult?neamente al autob?s y a casa, o se acumulan marcos sin continuidad. Eliminar el lugar sobrante y construir una secuencia l?gica; cada fila debe tener sentido por s? sola.

6. **A1-S004.csv, filas 63, 71 y 107?109 ? contexto sin sentido o referente ausente.** `En la parada del autob?s..., est?s en casa` (63) y `En la cafeter?a..., ?est?s en casa?` (71) contraponen sin motivo el lugar de la escena y estar en casa. Las filas 107?109 dicen que ?es una habitaci?n peque?a? en el parque/en el trabajo, sin antecedente que identifique la habitaci?n. Cambiar a una situaci?n comunicativa plausible, con referente expl?cito y sin a?adir lugares arbitrarios.

### Prioridad media ? gram?tica, naturalidad, progresi?n y repaso

7. **A1-S001.csv, filas 103, 107 y 109, y filas 143?145 ? sujeto omitido, concordancia y repetici?n mec?nica.** En 103 (`En casa tiene...;...he has...`) y 107 (`En casa, habla...;...she talks...`) el espa?ol omite el pronombre y no permite identificar la persona, pese a que el ingl?s la fija; a?adir `?l`/`Ella` seg?n el sentido. En 109, `unos a?os es mucho tiempo` tiene discordancia entre sujeto plural y verbo singular y la construcci?n es poco natural; reformular, por ejemplo, como `Esperar unos a?os es mucho tiempo`. En 143, `Despu?s del almuerzo, necesitamos unos minutos para terminar el almuerzo` repite innecesariamente la misma idea; variar el objetivo o expresar una acci?n distinta.

8. **A1-S002.csv, filas 101, 113, 141 y 145 ? antecedentes y sujetos insuficientes.** La pregunta `?es mi hermano?` (101) no identifica qui?n se pregunta si es hermano de qui?n; la frase en casa sobre que ?es una buena idea? (141) no tiene antecedente claro. En 145 se omite en espa?ol el sujeto que el ingl?s traduce como `they`; en 113, aunque el sujeto aparece, la visita ?despu?s de la escuela? estando ?en casa? necesita un contexto m?s claro. Explicitar qui?n hace la acci?n y evitar una secuencia de frases independientes conectadas solo por una ubicaci?n.

9. **A1-S003.csv, filas 107 y 143 ? pasado simple y repetici?n con cambio superficial.** Ambas repiten `Ped? un vaso de agua, por favor` / `I asked for a glass of water, please`, cambiando solo el d?a. El plan para S003 introduce *have got/has got* y posesivos, con repaso de S002; no se?ala una pr?ctica de pasado simple. Sustituirlas por pr?ctica alineada con esos objetivos o justificar una expresi?n memorizada y cambiar la segunda por transferencia contextual real, no por una fecha intercambiada.

10. **A1-S004.csv ? contextos insertados sin prop?sito (filas 61?80 y varios ejemplos posteriores).** Varias oraciones completas reciben prefijos de lugar/d?a que no contribuyen al significado: adem?s de los casos se?alados en el punto 6, 73 pone amigos que visitan ?despu?s de la escuela? en una cafeter?a; 76 habla de la edad de un libro en la cafeter?a; 77 da un consejo sobre abrigo all?; 78 combina ?En el parque? con una respuesta y una hermana en casa. Rehacer como mini-secuencias con continuidad y transferencia; no crear pr?ctica a?adiendo mec?nicamente d?as/lugares.

11. **A1-S005.csv, fila 138 ? adelanto y falta de equivalencia de aspecto.** `Ahora camino a la escuela, pero normalmente camino todos los d?as.;I am walking to school now, but I usually walk every day` usa presente continuo en ingl?s antes del objetivo G06 del plan y no lo expresa en espa?ol. Cambiarlo por presente simple en ambos idiomas para G05, o reservarlo para la sesi?n donde se introduce el contraste present continuous/present simple.

12. **A1-S005.csv, fila 148 ? frase ambigua y poco natural.** `En casa, eso es mucho para mi habitaci?n.;At home, that is a lot for my room` no aclara qu? cantidad/objeto es ?mucho? ni por qu? se destina a la habitaci?n. Nombrar la cantidad o el objeto y usar una situaci?n natural, o reemplazar el par.

13. **A1-S005.csv, fila 28 ? singular/plural no equivalente.** `?Hay alguna tienda abierta ahora?;Are there any shops open now?` pasa de una tienda singular a varias tiendas. Hacer coincidir n?mero y construcci?n, por ejemplo `Is there any shop/store open now?` o cambiar el espa?ol al plural.

## Seguimiento de las observaciones de la iteraci?n anterior

Se verificaron individualmente los ejemplos se?alados anteriormente:

- **Corregidos en las frases indicadas:** A1-S002, filas antiguas 46?50, 110 y 134, ahora expresan duraciones; A1-S003, filas antiguas 26 y 28, ya especifican platos y una taza; A1-S004, antiguas 21?25, ahora describen aspectos negativos plausibles de libros/planes/productos; A1-S005, antiguas 12 y 24, ahora usan `go` y una pregunta natural sobre qui?n entr?; A1-S003, antigua fila 5, ya no combina viernes por la tarde con ?todas las ma?anas?; A1-S002, antiguas filas 27 y 30, ya no combinan estar en casa con almorzar en la escuela; A1-S005, antiguas filas 4?5, ya no repiten ?hoy vivo lejos? bajo marcos temporales incompatibles. La traducci?n anterior `She knows all my family` y los ejemplos anteriores de ?bad things about the book? ya no aparecen.
- **No se repiten literalmente las filas antiguas 6?10 de S003**, pero el pasado simple vuelve en las filas actuales 107 y 143, se?alado en el punto 9.
- **La progresi?n/contextos criticados en A1-S001, antigua fila 97; A1-S002, antiguas 29?30; y A1-S005, antiguas 26?30**, fueron reformulados en esas posiciones; no obstante, la inserci?n mec?nica de ubicaciones/fechas y la falta de transferencia natural persisten en otras filas de S001, S002, S004 y S005, seg?n los puntos anteriores.

**Acci?n requerida:** corregir las filas y rangos indicados, conservar los objetivos gramaticales asignados por el plan, y volver a validar las cinco sesiones antes de una nueva auditor?a. **Se requiere otra iteraci?n: s?.**
