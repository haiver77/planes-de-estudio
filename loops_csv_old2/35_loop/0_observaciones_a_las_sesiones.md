# Informe de auditoría A1-S001 a A1-S005

**Iteración auditada:** `loops_csv/34_loop/A1/`  
**Informe de salida:** `loops_csv/35_loop/0_observaciones_a_las_sesiones.md`  
**Plan:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Alcance exclusivo:** los cinco CSV `A1-S001.csv` a `A1-S005.csv`, más `indicaciones_csv.md`, `contexto.md` y los informes 33 y 34. No se auditaron ni modificaron otras iteraciones ni `loops_csv_old/`.

## Resultado técnico, cobertura y cotejo del plan

- Los cinco ID pedidos están en el plan y existe un CSV correspondiente a cada uno en la carpeta auditada. En cada archivo se comprobaron **150 pares** (750 en total), el mínimo obligatorio.
- Se leyeron los bytes y se decodificó cada archivo con UTF-8 estricto; el análisis con `csv.reader` estricto confirma 150 registros de dos campos no vacíos, sin encabezado. Cada fila física contiene un único `;`; no hay filas vacías, campos adicionales, comillas mal cerradas ni saltos de línea incrustados. No se usaron comas como delimitador.
- No se detectaron `Ã¡`, `Ã±`, `U+FFFD`, secuencias de mojibake ni preguntas españolas sin `¿`. Los `?` en las preguntas son cierres válidos. Columnas en orden español–inglés. No hay duplicados exactos de frases españolas ni inglesas dentro de cada archivo ni entre estos cinco CSV.
- En las filas 1–60 de cada CSV están las 12 unidades léxicas asignadas en el catálogo, con cinco ejemplos por unidad. Los bloques coinciden con el plan: S001 60 + 0 repaso + 30 gramática + 60 integración; S002/S003 60 + 12 + 30 + 48; S004/S005 60 + 24 + 30 + 36. Los repasos previstos y los bloques gramaticales G01–G05 están ubicados en sus rangos correspondientes.
- La mayor parte de las observaciones previas sí se corrigió: por ejemplo, S002-147 ahora pregunta `Do you have a moment…?`; S003-105, 119 y 127 están alineadas/naturales; S003-126 aclara quién tiene el coche; S004-57/58 usan `from`; S004-132 pregunta por carga; y las secuencias de S001-29/30 y S005-24/25, 34/35, 45 y 50 se reformularon. Sin embargo, persisten los problemas de A1 en S004-129/131 y hay nuevas observaciones abajo. La observación anterior sobre S005-5 se alivió en esa fila, pero la cuarta frase del mismo bloque sigue sobrecargada y rompe la progresión.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta: equivalencia, sentido y uso autónomo

1. **`A1-S003.csv`, filas 49–50 — referencia temporal no equivalente.**  
   Observado: `Estoy libre este fin de semana y puedo usar el coche.;I am free at the weekend, and I can use the car to take my sister to the park.` (la fila 50 añade el traslado). El español sitúa la disponibilidad en este fin de semana; `at the weekend` puede expresar una rutina o disponibilidad general, no necesariamente ese fin de semana. **Cambio requerido:** usar `this weekend` en inglés en ambas filas para conservar la referencia concreta, p. ej. `I am free this weekend...`.

2. **`A1-S004.csv`, filas 18–20 — frase vaga y paráfrasis repetida.**  
   Observado en la fila 18: `Es algo malo para el grupo en esta situación.;It is a bad thing for the group in this situation.` No se identifica la situación; aislada, la frase no comunica qué ocurre. Las filas 19–20 repiten casi el mismo ejemplo: dejar la puerta abierta/sin llave durante la clase es algo malo para todos/el grupo. **Cambio requerido:** hacer explícita una situación concreta en la fila 18 y sustituir una de las dos frases sobre la puerta por otro inconveniente cotidiano y distinto; conservar `bad thing` sin repetir plantilla y contenido.

3. **`A1-S004.csv`, filas 129 y 131 — sigue pendiente una observación A1 del informe 34.**  
   Observado: `Hay taquillas en mi escuela.;There are lockers at my school.` y `Mi teléfono se queda sin batería en el autobús.;My phone runs out of battery on the bus.` `Lockers` y `runs out of battery` añaden léxico/expresión menos básicos en integración. **Cambio requerido:** reemplazarlo por objetos y acciones familiares de nivel A1, p. ej. libros en la escuela y el teléfono apagado, o simplificar el mensaje manteniendo una idea cotidiana.

4. **`A1-S005.csv`, fila 4 (y secuencia 3–5) — frase de foco excesivamente cargada; la progresión se reinicia.**  
   Observado: `Después de llegar en tren, camino hasta el centro de la ciudad para visitar el mercado cubierto y comprar fruta fresca.;After arriving by train, I walk to the city centre to visit the covered market and buy fresh fruit.` Acumula llegada, medio, desplazamiento y dos acciones, con `covered market`; la fila 5 vuelve abruptamente a `Voy al centro de la ciudad y compro pan.` tras esa frase larga. **Cambio requerido:** acortar la fila 4 a una sola acción/contexto cotidiano y hacer que la fila 5 añada un detalle sencillo, de modo que el bloque crezca gradualmente sin introducir `covered market`.

### Prioridad media: progresión y adecuación A1

5. **`A1-S001.csv`, fila 10 — expansión demasiado larga y contexto poco inmediato.**  
   Observado: `Tenemos unos minutos antes de clase mientras esperamos el tren con mi madre en la estación.;We have a few minutes before class while we wait for the train with my mother at the main station.` La subordinada, varios complementos y la combinación de “antes de clase” con esperar un tren en la estación sobrecargan la quinta frase. **Cambio requerido:** conservar `a few minutes` en una escena A1 más directa, p. ej. `Tenemos unos minutos antes de que llegue el tren.;We have a few minutes before the train arrives.`

6. **`A1-S001.csv`, fila 144 — integración con léxico abstracto para A1.**  
   Observado: `El curso incluye ejercicios de conversación varias veces al mes.;The course includes speaking exercises several times a month.` `El curso incluye ejercicios de conversación` / `includes speaking exercises` convierte una frase de integración en una descripción abstracta. **Cambio requerido:** reciclar la unidad con hablantes y acción concreta, p. ej. `Hablamos inglés unas cuantas veces al mes.;We speak English a few times a month.`

7. **`A1-S002.csv`, fila 25 — extensión larga con vocabulario no básico.**  
   Observado: `La tienda está abierta todo el día hoy en el centro para los visitantes, así que los vecinos pueden comprar después del trabajo.;The shop is open all day today in the city for visitors, so local residents can shop after work.` La secuencia de circunstancias y la subordinada, junto con `visitors/local residents`, exceden lo necesario para practicar `all day`. **Cambio requerido:** dejar una escena corta con palabras de alta frecuencia, p. ej. `La tienda está abierta todo el día y la gente compra después del trabajo.;The shop is open all day, and people shop after work.`

8. **`A1-S002.csv`, fila 60 — repetición y regresión dentro de la progresión de `arrive at`.**  
   Observado: `Llegamos a la estación en autobús.;We arrive at the station by bus.` Repite casi literalmente la ruta de la fila 58 (`Es fácil llegar a la estación hoy en autobús / It is easy to arrive at the station today by bus`) y la quinta frase es más corta, no una ampliación final. **Cambio requerido:** usar otro destino o detalle sencillo y no repetido con `arrive at`, manteniendo una progresión creciente; p. ej. `Llegamos a la tienda antes del almuerzo.;We arrive at the shop before lunch.`

9. **`A1-S005.csv`, filas 39–40 — carga innecesaria y repetición mecánica.**  
   Observado: `Es difícil para mí nadar en invierno en el mar sin mis gafas.;It is difficult for me to swim in winter in the sea without my goggles.` La fila 40 repite toda la escena y solo añade `durante mucho tiempo / for a long time`. El conjunto resulta largo para A1 y la situación de nadar en el mar en invierno sin gafas no es inmediata. **Cambio requerido:** conservar `difficult for` con una actividad y marco familiares; que la quinta frase añada una consecuencia o detalle útil, no otro modificador temporal.

10. **`A1-S005.csv`, fila 65 — repaso con léxico por encima del nivel.**  
    Observado: `Las cosas malas de los viajes largos en coche son el cansancio y el tráfico.;The bad things about long car journeys are tiredness and traffic.` `Long car journeys` y `tiredness` son más avanzados de lo necesario para recuperar la unidad. **Cambio requerido:** usar inconvenientes concretos de un viaje corto con vocabulario frecuente, p. ej. `Lo malo del autobús es el ruido.;The bad thing about the bus is the noise.`

11. **`A1-S005.csv`, fila 124 — contexto de integración innecesariamente especializado.**  
    Observado: `La oficina de turismo está cerca del puente principal.;The tourist office is near the main bridge.` `Oficina de turismo / tourist office` no es vocabulario inmediato de supervivencia A1 y no se necesita para una oración de ubicación. **Cambio requerido:** conservar la estructura espacial con un lugar familiar, p. ej. `El café está cerca de la estación.;The café is near the station.`

## Veredicto

**VEREDICTO: NO COMPLETO.** La estructura, el recuento y la cobertura de las cinco sesiones cumplen, pero persisten observaciones previas y nuevas de equivalencia, naturalidad, variedad y nivel/progresión A1. Se requiere otra iteración: corregir únicamente los puntos enumerados en los CSV del siguiente ciclo y volver a auditarlos.