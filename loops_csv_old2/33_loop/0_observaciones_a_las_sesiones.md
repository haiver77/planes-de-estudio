# Informe de auditoría lingüística y técnica -- A1-S001 a A1-S005

**Iteración global auditada:** 32  
**Iteración de salida:** 33  
**Plan aprobado:** `C:\GIT\english-learning-program\loops_plan\11_loop\1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo cotejado:** `C:\GIT\english-learning-program\loops_plan\11_loop\2_catalogo_trazabilidad_fuentes.csv`  
**Alcance exclusivo:** `loops_csv/32_loop/A1/A1-S001.csv` a `A1-S005.csv`. No se revisó otro nivel ni `loops_csv_old/`.

## Evidencia técnica y de cobertura

- Se leyeron los bytes reales y se decodificaron con UTF-8 estricto. Los cinco archivos existen, sin BOM, y tienen 150 filas físicas/pares cada uno (750 pares en total). Tamaños observados: S001 13.914 bytes; S002 14.859; S003 14.457; S004 15.416; S005 15.639.
- `csv.reader` con `delimiter=';'`, `quotechar='"'` y `strict=True` parsea 150 registros de dos campos no vacíos en cada archivo, sin encabezado. Cada línea física tiene exactamente un `;`; no hay campos extra, filas vacías, separadores dentro de frases, comillas mal cerradas ni saltos de línea incrustados. No hay filas delimitadas solo por coma.
- No se detectaron U+FFFD, secuencias de mojibake ni preguntas españolas sin apertura `¿`. Los acentos y signos invertidos están presentes en Unicode; los signos `?` encontrados son cierres de pregunta. No hay `?` que sustituya letras.
- No hay pares duplicados, frases españolas duplicadas ni frases inglesas duplicadas dentro de un CSV o entre los cinco archivos.
- Distribución frente al plan: S001 = 60 vocabulario nuevo + 0 repaso + 30 gramática + 60 integración; S002 y S003 = 60 + 12 + 30 + 48; S004 y S005 = 60 + 24 + 30 + 36. Cada sesión dispone de 12 U con cinco ejemplos por U en las filas 1-60. Se comprobaron seis eventos de repaso de 12/12 unidades: S002 61-72 (S001); S003 61-72 (S002); S004 61-72 (S003) y 73-84 (S001); S005 61-72 (S004) y 73-84 (S002). Los bloques de 30 ejemplos gramaticales corresponden a G01-G05 y la cantidad de integración concuerda con el plan.
- Se mantiene en general el inglés británico (`centre`, `neighbour`, `film`, `car park`, `mobile phone`, `at the weekend`, `practise`, etc.). `cell phone` es el término estadounidense deliberado del catálogo de S004, y su aparición en el repaso de S005 es coherente con ese repaso. La cita fuente `He came into the room` de S005-21 es el único ejemplo en pasado de esa unidad; no se ha convertido en práctica productiva de un objetivo posterior.

## Cotejo de las ocho observaciones de entrada (línea por línea)

1. **S001-38-40:** corregidas. La progresión usa ahora `It's a good idea to call ...`, con invitación y ampliación comprensibles; no repite el giro forzado de dos puntos + gerundio.
2. **S004-14/15:** corregidas. La hora concreta de salida del autobús y la consecuencia para la familia forman una noticia clara y relacionada.
3. **S005-60:** la observación de entrada asigna aquí `cell phone`, pero esa asignación no coincide con el catálogo (véase la discrepancia documentada abajo). El contenido actual de S005-60 es correcto para `every week`.
4. **S003-23/25:** corregidas. La canción del evento escolar y el cumpleaños de Ana son contextos distintos; se eliminó el proyecto solidario.
5. **S005-29/30:** corregidas. `clear to the children` es idiomático y la segunda fila aporta una transferencia distinta mediante dibujos para las familias.
6. **S002-54/55:** corregidas. Se conserva una referencia temporal y la extensión añade el objetivo de visitar tres países, no otro marcador temporal redundante.
7. **S003-44/45:** corregidas. El orden inglés ahora es `arrive at the station at the same time`; la extensión de comprar billetes juntos es pertinente.
8. **S003-25 y S004-34/35:** los ejemplos antiguos de proyecto solidario, informe de progreso, cena de graduación y brindis se sustituyeron por cumpleaños, saludos de clase y una canción corta. Esas correcciones puntuales son adecuadas; persisten, sin embargo, problemas distintos de nivel A1 en otras filas indicadas a continuación.

## Discrepancia de asignación del teléfono -- cotejo informe/catálogo

La observación de entrada sitúa `cell phone` en **A1-S005-60**. El catálogo no lo asigna allí: `cell phone` es **A1-S004-U12**, fuente `OPL-A1-P01-L053`, ubicación `#A1-S004 -- Vocabulario Foco`; por tanto, corresponde al grupo **S004-56-60**, y S004-60 es su quinta frase. En cambio, **A1-S005-U12 es `every week`**, fuente `OPL-A1-P01-L065`, ubicación `#A1-S005 -- Vocabulario Foco`; S005-60 debe practicar esa unidad. El CSV actual sí respeta ambos lugares: S004-60 usa *cell phone* en un contexto autónomo, y S005-60 dice `Nos reunimos cada semana ... / We meet every week ...`. La asignación de la observación previa a S005-60 es una discrepancia del informe, no un defecto actual de esos dos renglones. La corrección del generador en S004-60 está justificada; corregir S005-60 para introducir allí *cell phone* no lo estaría.

## Observaciones pendientes -- se requiere otra iteración

### Prioridad alta

1. **A1-S003.csv, fila 126 -- posesión/adjunción ambigua.**  
   `Ana tiene un profesor con un coche azul.;Ana has got a teacher with a blue car.` En ambas columnas queda ambiguo quién tiene el coche: el lector puede interpretar que Ana tiene un profesor que lo tiene, pero el foco `have got` pretende expresar la posesión del profesor. **Cambio requerido:** identificar explícitamente al poseedor en español e inglés (por ejemplo, `El profesor de Ana tiene...` / `Ana's teacher has got...`), sin dejar la relación colgando del complemento `con/with`.

2. **A1-S002.csv, fila 147 -- equivalencia de intención.**  
   `¿Tienes un momento para darme un poco de ayuda con esta bolsa?;Are you free to give me a little help with this bag?` `Tienes un momento` pregunta si la otra persona puede dedicar tiempo; `Are you free` pregunta si está libre/disponible. Son cercanas, pero no equivalentes en intención. **Cambio requerido:** conservar la petición cortés y preguntar por un momento/tiempo disponible en ambas columnas, sin sustituirlo por disponibilidad general.

3. **A1-S004.csv, filas 57-58 -- origen convertido en ubicación actual.**  
   `Mi tía de Ohio ...` / `Mi amiga de Texas ...` se traduce como `My aunt in Ohio ...` / `My friend in Texas ...`. `De Ohio/Texas` expresa procedencia; `in Ohio/Texas` sitúa a las personas allí ahora. **Cambio requerido:** alinear el sentido en ambas columnas (cambiar el español a `en` si se trata de ubicación actual, o usar `from` si se trata de procedencia). La inclusión de *cell phone* sí es intencional según el catálogo, pero no justifica cambiar esta relación semántica.

### Prioridad media -- nivel A1 y progresión significativa

4. **A1-S003.csv, filas 28-30 -- vocabulario/escena demasiado avanzada y repetición estrecha.**  
   La respuesta al misterio, el último capítulo, la detective y la carta perdida (`mystery`, `final chapter`, `detective`, `missing letter`) se acumulan en una sola progresión. Las filas 28-30 siguen describiendo el mismo libro y la tercera añade una cláusula de trama compleja. **Cambio requerido:** conservar `at the end / at the end of` con objetos cotidianos y vocabulario A1; que las cinco frases añadan información útil sin depender de un misterio o de cláusulas subordinadas.

5. **A1-S003.csv, filas 34-35 y 38-40 -- densidad léxica y sintáctica superior a A1.**  
   En 34-35, `school concert`, `stage` y `audience` se combinan con una subordinada; en 38-40, `busy with my team ... checking the final report before the meeting` alarga la misma escena de oficina con léxico menos básico. **Cambio requerido:** mantener los focos `at the end of` y `at the moment`, pero usar escenas cotidianas, frases más cortas y extensiones que añadan una acción sencilla, no más cláusulas y nombres abstractos.

6. **A1-S003.csv, filas 49-50 -- la progresión ya añade información, pero sigue sobrecargada para A1.**  
   La disponibilidad del coche para una mudanza y el espacio para cajas grandes sí amplían el plan, pero `available`, `move` y la descripción de capacidad elevan la dificultad. **Cambio requerido:** mantener el contexto de fin de semana y una consecuencia clara con vocabulario básico; no sustituir la extensión significativa por un marcador temporal, pero sí simplificarla.

7. **A1-S004.csv, filas 23-25 -- persiste el problema de adecuación A1.**  
   Las frases sobre los aspectos negativos del invierno acumulan `icy roads`, `long journeys`, `nearest village`, `residents` y `before sunrise`, además de una explicación larga. La fila 25 añade una consecuencia, pero depende de vocabulario poco cotidiano para este nivel y el motivo de salir antes del amanecer no queda explicado. **Cambio requerido:** mantener `the bad things about ...` con elementos concretos y familiares de invierno, vocabulario A1 y una consecuencia explícita y breve.

8. **A1-S004.csv, filas 29-30 -- acumulación y circunstancia añadida sin progresión suficiente.**  
   `La calle está mojada por la lluvia esta mañana frente a la escuela cerca de mi casa después de la tormenta.` La fila 30 apila dos referencias locativas y dos referencias temporales; `after the storm` queda temporalmente suelto respecto de `this morning`, y la ampliación no aporta una acción nueva. **Cambio requerido:** reducir los complementos a un contexto claro y hacer que la segunda frase agregue una consecuencia o acción cotidiana relacionada.

9. **A1-S004.csv, filas 33, 45 y 50 -- léxico/contextos poco básicos.**  
   `ceremony / live traditional song`, `encourages me to apply for a summer job at the community centre` y `exhibition` son contextos y términos de nivel superior, especialmente en las frases largas de *begin with*, *best friend* y *black and white*. **Cambio requerido:** reemplazarlos por acciones familiares de aula, amigos o casa, conservando el vocabulario objetivo con frases más breves y transferibles.

10. **A1-S002.csv, filas 9-10 y 19-20 -- extensión mecánica.**  
    En 9-10 la visita familiar al museo solo gana `during our visit`; en 19-20 la lista de libros para la clase solo gana `this year`. Ambas extensiones repiten casi la misma escena y añaden un complemento temporal redundante o de poco valor. **Cambio requerido:** dejar una sola referencia temporal y hacer que la última frase aporte un uso, resultado o detalle distinto, sencillo y pertinente al contexto.

11. **A1-S002.csv, filas 49-50 -- progresión poco adecuada al nivel.**  
    `Workers remove the fallen branches` y `put up detour signs` describe una reparación plausible, pero introduce `fallen branches` y `detour signs` en una secuencia larga para practicar `a short period of time`. **Cambio requerido:** conservar la idea de cierre breve mientras alguien hace una tarea, con una tarea y vocabulario A1, y dar a la quinta frase una extensión útil en vez de más léxico especializado.

12. **A1-S001.csv, filas 138, 140 y 145; A1-S005.csv, filas 118 y 144 -- integración con léxico/contexto por encima de A1.**  
    `colleague`, `guide ... visitors`, `staff`, `manager ... budget` y `exhibition` elevan la carga léxica para estas frases de integración. **Cambio requerido:** reciclar las unidades con vocabulario de alta frecuencia y contextos inmediatos, manteniendo frases breves e independientes.

13. **A1-S005.csv, fila 127 -- contexto telefónico incompleto.**  
    `Mi teléfono móvil muestra el número de la plataforma.;My mobile phone shows the platform number.` La idea es posible si se refiere a una aplicación o pantalla de viaje, pero sin ese contexto parece que el teléfono muestra el número sin motivo. **Cambio requerido:** nombrar brevemente la aplicación/pantalla o usar un ejemplo más cotidiano, manteniendo el inglés británico.

## Resultado

Persisten observaciones de equivalencia, claridad, naturalidad, adecuación A1 y progresión. Corregirlas y volver a auditar únicamente A1-S001.csv a A1-S005.csv en `loops_csv/33_loop/`.
