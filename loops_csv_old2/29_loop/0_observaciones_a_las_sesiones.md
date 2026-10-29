# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración revisada:** 28  
**Mínimo obligatorio:** 150 pares por CSV  
**Plan aprobado:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Alcance exclusivo:** `loops_csv/28_loop/A1/A1-S001.csv` a `A1-S005.csv`.

## Comprobaciones que cumplen

- Los cinco archivos solicitados existen y corresponden a los IDs del alcance. Cada CSV tiene exactamente 150 registros: 750 en total.
- Se leyeron los bytes y se validaron con decodificación UTF-8 estricta, sin BOM, y `csv.reader` en modo estricto con `;`. Hay 150 líneas físicas/registros por archivo, dos campos por registro, sin encabezado, campos vacíos, filas vacías, campos extra, comillas mal formadas, saltos incrustados ni líneas delimitadas solo por coma. Cada línea tiene exactamente un `;`.
- La inspección determinista no encontró U+FFFD, secuencias de mojibake ni `?` sustituyendo letras; las preguntas en español tienen `¿` de apertura.
- El catálogo asigna 12 unidades nuevas a cada sesión y se verificaron los bloques de 5 pares por unidad (60 pares nuevos por CSV). El conteo exacto de palabras confirma una progresión estrictamente creciente en español e inglés en los 60 grupos. No obstante, algunas frases alargan artificialmente el contexto o pierden naturalidad; véanse las observaciones.
- Los repasos conservan cantidad, posición y secuencia previstas: S002 filas 61–72 (S001); S003 filas 61–72 (S002); S004 filas 61–72 (S003) y 73–84 (S001); S005 filas 61–72 (S004) y 73–84 (S002). Cada bloque recorre las 12 unidades en orden y sus frases mantienen los contextos léxicos correspondientes.
- Se verificaron 30 frases gramaticales en cada bloque previsto: S001 filas 61–90 (G01), S002 y S003 filas 73–102 (G02/G03), S004 y S005 filas 85–114 (G04/G05). Las integraciones tienen 60, 48, 48, 36 y 36 pares, respectivamente, como establece el plan.
- No hay pares, frases españolas ni frases inglesas duplicados entre los 750 registros.
- Se revalidaron las correcciones históricas: S001-13 practica ahora *a few times*; S003-126 conserva correctamente la posesión de Ana con *have got*. También se mantienen las correcciones de S002-48/49, S003-70/105/149, S004-27/28/104, S005-18/19/23/82; en S005 algunas quedaron desplazadas de fila al reorganizarse el bloque, pero el sentido corregido sigue presente.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta

1. **A1-S005.csv, filas 21 y 24–25 — se adelanta el pasado simple.**  
   `Él entró en la habitación` / `He came into the room` y las variantes de las filas 24–25 practican pasado simple en una sesión cuyo objetivo gramatical es G05; el plan introduce el pasado simple más adelante, en A1-S009/G09. **Cambio requerido:** mantener *come into* y su perspectiva de movimiento, pero reformular estas frases en presente y con un contexto que justifique el punto de vista (por ejemplo, `En la historia, él entra en la habitación.;In the story, he comes into the room.`). Conservar la progresión sin adelantar la enseñanza del pasado simple prevista para A1-S009.

### Prioridad media

2. **A1-S001.csv, filas 24–25 — formulación incompleta y contexto añadido sin acción clara.**  
   `Es una buena idea para el viaje hoy con un mapa.` / `It is a good idea for the trip today with a map.` no expresa qué acción es buena idea; la fila 25 solo añade `antes de salir / before we leave` y sigue sin resolverlo. En el grupo completo (filas 21–25), las longitudes son 8/9/10/11/14 palabras en español y 7/9/10/12/15 en inglés: aumenta el tamaño, pero no la información útil en las dos últimas. **Cambio requerido:** expresar una acción concreta y extenderla con información útil, por ejemplo, `Es una buena idea llevar un mapa para el viaje de hoy.;It is a good idea to take a map for today's trip.`; hacer que la quinta frase añada un detalle lógico.

3. **A1-S002.csv, filas 33–35 — el grupo de *all over the world* usa relleno poco natural.**  
   La fila 33 acumula “por todo el mundo”, “muchas ciudades” y “distintos países”; la 34 afirma que hay tiendas “para los viajeros cada año”, relación poco lógica; la 35 repite la idea de viajar por todo el mundo y visitar cada país. En el grupo completo (filas 31–35), las longitudes aumentan de 8 a 24 palabras en español (8/9/12/14/24) y de 9 a 22 en inglés (9/11/13/14/22), pero las ampliaciones no aportan contexto natural. **Cambio requerido:** conservar la expresión objetivo, pero variar los contextos con situaciones plausibles y hacer que el aumento de longitud añada información significativa, no lugares o complementos redundantes.

4. **A1-S002.csv, filas 49–50 — colocación poco idiomática y expansión redundante de *a period of time*.**  
   `La espera es un período de tiempo corto para nosotros esta tarde en la clínica` / `The wait is a short period of time for us this afternoon at the clinic` suena forzado en español e inglés; la fila 50 solo agrega “antes de la cita / before the appointment”. En el grupo completo (filas 46–50), las longitudes son 9/12/13/15/19 palabras en español y 9/12/13/15/18 en inglés; las últimas dos amplían la misma idea sin volverla idiomática. **Cambio requerido:** reformular con una colocación natural manteniendo el objetivo, por ejemplo, `La espera en la clínica dura un corto período de tiempo.;The wait at the clinic lasts for a short period of time.` Si se amplía, añadir una consecuencia o detalle pertinente.

5. **A1-S003.csv, filas 23–25 — crecimiento por acumulación de detalles poco pertinentes.**  
   En la secuencia de *at the beginning*, la música suave al principio de la película termina situada “hoy en el cine para mi familia antes de la cena”. Es gramatical, pero los complementos agregados no enriquecen una microescena natural. En el grupo completo (filas 21–25), las longitudes son 8/9/13/16/20 palabras en español y 10/11/14/17/19 en inglés; el aumento de las tres últimas consiste en añadir contexto débil a la misma oración. **Cambio requerido:** reemplazar la extensión por ejemplos contextualizados y variados sobre el comienzo de una película, una clase o un evento; conservar el orden incremental con detalles que aporten sentido.

6. **A1-S004.csv, filas 8–10 — traducción poco natural del objetivo *bad for*.**  
   `El café es malo para dormir por la noche para mi hermano` / `Coffee is bad for sleep at night for my brother` repite complementos de manera poco idiomática; las ampliaciones de las filas 9–10 siguen esa construcción. En el grupo completo (filas 6–10), las longitudes son 7/8/12/13/17 palabras en español y 5/7/10/13/15 en inglés, pero el crecimiento reproduce la estructura forzada en vez de añadir variedad natural. **Cambio requerido:** expresar la idea con una colocación natural en ambos idiomas y mantener *bad for*, por ejemplo, `El café es malo para el sueño de mi hermano por la noche.;Coffee is bad for my brother's sleep at night.` Variar las demás frases del grupo sin reutilizar esa misma estructura forzada.

7. **A1-S004.csv, filas 34–35 — repetición tautológica en el grupo de *begin with*.**  
   `Empieza con una canción sencilla para la clase al comienzo de la actividad.` repite “empieza / al comienzo”; la fila 34 ya había añadido `al comienzo` a la misma frase de la fila 33. En el grupo completo (filas 31–35), las longitudes son 6/7/8/10/13 palabras en español y 6/7/8/11/14 en inglés, pero el alargamiento de las filas 34–35 es tautológico. **Cambio requerido:** mantener *begin with* en frases completas y aportar una circunstancia real distinta en cada ampliación, sin añadir un sinónimo redundante de “empezar”.

8. **A1-S004.csv, filas 44–45 — expresión redundante y plantilla repetida en *best friend*.**  
   `una buena vecina de al lado` / `a kind neighbor next door` duplica la idea de proximidad; la fila siguiente conserva casi la misma plantilla y solo cambia el complemento. En el grupo completo (filas 41–45), las longitudes son 7/8/9/12/13 palabras en español y 7/8/9/11/13 en inglés; las últimas frases priorizan sumar modificadores antes que ofrecer una transferencia contextual distinta. **Cambio requerido:** reemplazar la fila 44 por una formulación natural y usar la quinta frase para transferir *best friend* a otra situación, no solo para alargar la misma descripción.

9. **A1-S005.csv, filas 4–5 — contexto poco natural en *city centre*.**  
   `El centro de la ciudad está aquí hoy...` / `The city centre is here today...` atribuye al centro una presencia temporal (“hoy”) y la fila 5 añade “para los visitantes / for visitors” sin una relación clara. En el grupo completo (filas 1–5), las longitudes aumentan de 8 a 19 palabras en español (8/9/10/16/19) y de 6 a 14 en inglés (6/7/8/12/14), pero las dos frases más largas no aportan un contexto verosímil. **Cambio requerido:** reformular desde la perspectiva de una persona que está o trabaja en el centro, o que da indicaciones; ampliar con un destino o punto de referencia pertinente.

10. **A1-S005.csv, filas 48–50 — plantilla repetida sin ejemplo real en *end in*.**  
    Las tres frases repiten `La palabra termina en una vocal en español...`; “en este ejemplo” no identifica ninguna palabra, y la fila 50 solo añade “del libro de clase”. En el grupo completo (filas 46–50), las longitudes aumentan de 7 a 16 palabras en ambos idiomas (7/9/11/12/16); el orden numérico es correcto, pero no hay progresión de ejemplos ni de contexto. **Cambio requerido:** presentar palabras o nombres concretos que terminen en letras distintas y variar la situación; las extensiones deben aportar ejemplos verificables y contexto, no la misma plantilla con más palabras.

11. **A1-S005.csv, fila 57 — frecuencia semanal poco natural.**  
    `La biblioteca cierra temprano cada semana.;The library closes early every week.` sugiere que cierra temprano durante toda una semana, no en un momento recurrente de la semana. En el grupo completo (filas 56–60), las longitudes son 5/6/7/13/17 palabras en español y 5/6/7/12/14 en inglés; la fila 57 no comunica una frecuencia semanal idiomática. **Cambio requerido:** usar un evento que ocurra semanalmente o precisar el día de cierre, manteniendo el objetivo *every week* (por ejemplo, una actividad semanal de la biblioteca).

**Resultado:** quedan observaciones lingüísticas y de fidelidad/progresión accionables. Corregirlas en la siguiente iteración y volver a auditar únicamente los cinco CSV del alcance.
