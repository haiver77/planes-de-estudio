# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración de entrada:** 29  
**Mínimo obligatorio:** 150 pares por CSV  
**Plan:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Alcance exclusivo:** `loops_csv/29_loop/A1/A1-S001.csv` a `A1-S005.csv`.

## Evidencia comprobada

- **Cobertura y cantidad:** existen los cinco archivos del alcance. Cada CSV contiene exactamente 150 pares, 750 en total. El catálogo asigna 12 unidades nuevas a cada sesión y se verificaron cinco pares por unidad (60 pares nuevos por CSV).
- **Validación desde bytes:** los cinco archivos decodifican con UTF-8 estricto, sin BOM. Tamaños: S001 13.865 bytes; S002 14.855; S003 14.201; S004 15.177; S005 15.566. Cada archivo tiene 150 líneas físicas y 150 registros CSV en modo estricto, sin encabezado y con dos campos no vacíos por registro; no hay filas vacías, campos adicionales, delimitadores por coma, puntos y coma dentro de frases, comillas mal cerradas ni saltos de línea incrustados. No se detectaron U+FFFD, secuencias de mojibake ni `?` sustituyendo letras. Todas las preguntas en español tienen `¿` de apertura.
- **Duplicados:** entre los 750 registros no hay pares repetidos ni frases españolas o inglesas duplicadas.
- **Repasos, gramática e integración:** se cotejaron los eventos con el plan, en orden U01–U12: S002 filas 61–72 (S001); S003 filas 61–72 (S002); S004 filas 61–72 (S003) y 73–84 (S001); S005 filas 61–72 (S004) y 73–84 (S002). Los seis eventos contienen 12/12 unidades. Se revisaron 30 pares gramaticales en cada sesión (S001 61–90; S002 y S003 73–102; S004 y S005 85–114), acordes con los focos G01–G05 del plan, y las cantidades planificadas de integración (60, 48, 48, 36 y 36).
- **Progresión de los grupos señalados:** los conteos de palabras crecen estrictamente en español e inglés en los grupos pedidos:

  | Archivo — filas | Español | Inglés |
  |---|---|---|
  | S001 — 21–25 | 8/9/10/12/19 | 7/9/10/12/19 |
  | S002 — 31–35 | 8/10/12/17/27 | 9/10/12/17/26 |
  | S002 — 46–50 | 8/10/14/17/26 | 9/10/13/16/24 |
  | S003 — 21–25 | 8/11/13/19/21 | 9/10/14/17/20 |
  | S004 — 6–10 | 7/8/13/14/21 | 6/9/11/14/18 |
  | S004 — 31–35 | 5/7/9/14/19 | 5/7/8/12/18 |
  | S004 — 41–45 | 7/8/9/12/15 | 7/8/9/11/15 |
  | S005 — 1–5 | 7/11/16/21/33 | 6/10/14/19/30 |
  | S005 — 21–25 | 5/6/12/15/21 | 5/6/11/14/21 |
  | S005 — 46–50 | 8/10/12/18/30 | 8/9/12/18/25 |
  | S005 — 56–60 | 5/8/11/13/17 | 5/6/10/12/14 |

  Las ampliaciones de estos grupos aportan acciones, participantes o circunstancias concretas; no se rechazan por el mero aumento de longitud. En S005, U05 (filas 21–25) conserva la frase fuente en pasado una sola vez en la fila 21 y usa presente simple en las cuatro siguientes, sin otros pasados.
- **Revalidación histórica:** se revisó línea por línea el informe guardado en `loops_csv/29_loop/0_observaciones_a_las_sesiones.md` (que audita la iteración 28) y las observaciones históricas aplicables. Sus puntos pendientes están corregidos en esta entrada: S001-24/25; S002-33–35 y 49/50; S003-23–25; S004-8–10, 34/35 y 44/45; S005-4/5, 48–50 y 57. También se confirmaron S001-13 (*a few times*), S003-126 (sujeto y posesión con *have got*), S002-48/49, S003-70/105/149, S004-27/28/104 y las correcciones de contexto de S005-18/19/23/82. La cuestión de inglés británico de S005-58 indicada abajo es nueva.

## Observaciones pendientes — se requiere otra iteración

### Prioridad alta

1. **A1-S005.csv, fila 50 — adelanta un objetivo gramatical posterior.**  
   `En el formulario, el nombre de Megan termina en la letra n, mientras que el de Lucas termina en la letra s. Revisa ambas terminaciones antes de copiar los datos.;On the form, Megan's name ends in the letter n, while Lucas's name ends in the letter s. Check both endings before copying the details.` La orden `Revisa / Check` introduce un imperativo, objetivo previsto para G07 en A1-S007; esta sesión introduce G05. **Cambio requerido:** mantener los ejemplos verificables de *end in* y el detalle contextual, pero reformular la instrucción sin imperativo ni adelanto de G07.

### Prioridad media

2. **A1-S002.csv, fila 30 — acumulación redundante y contexto débil.**  
   `La luz está encendida toda la noche en el pasillo hoy para el bebé durante el viaje.;The light is on all night in the hallway tonight for the baby during the trip.` `Toda la noche / all night` y `hoy / tonight` duplican la referencia temporal; además, no queda clara la relación entre dejar la luz encendida, el bebé y el viaje. **Cambio requerido:** sustituir la fila por una situación autónoma y verosímil que justifique por qué la luz queda encendida toda la noche, sin apilar marcadores temporales.

3. **A1-S005.csv, fila 58 — inconsistencia con la variedad británica.**  
   `Los vecinos juegan al fútbol juntos en el parque cada semana.;The neighbors play football together in the park every week.` El CSV usa repetidamente la forma británica `neighbour`; `neighbors` introduce la grafía estadounidense sin contexto que la justifique. **Cambio requerido:** escribir `neighbours` y mantener la convención británica.

### Prioridad baja

4. **A1-S005.csv, fila 20 — repetición poco natural en inglés.**  
   `Estoy en la cocina cuando mi hermano llega a casa del trabajo y entra para cenar.;I am in the kitchen when my brother gets home from work and comes into the kitchen for dinner.` El inglés repite `the kitchen` en la misma frase, mientras que el español expresa la ubicación una sola vez. **Cambio requerido:** reformular ambas columnas para conservar el regreso del trabajo y la entrada para cenar sin repetir el lugar, por ejemplo, indicar primero que quien habla está en casa y luego que el hermano entra en la cocina.

**Resultado:** permanecen observaciones lingüísticas y de fidelidad al plan. Corregirlas y volver a auditar únicamente estos cinco CSV en la siguiente iteración.
