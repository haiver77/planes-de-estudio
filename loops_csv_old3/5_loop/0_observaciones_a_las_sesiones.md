# Auditoría de PF-A1-001 — iteración 4

Archivo auditado: `loops_csv/4_loop/A1/frases_PF-A1-001_v1.csv`  
Plan: `planes_aprobados/oxford_phrase_list/plan_frases_oxford.md`  
Resultado: **requiere otra iteración**.

## Comprobaciones aprobadas

- El plan asigna a PF-A1-001 diez focos: `get better`, `get lost`, `get ready`, `get up`, `make a mistake`, `make sure`, `pick sb/sth up`, `take off`, `take part` y `take place`. El CSV contiene los diez, en bloques de 15 frases (150 filas en total), y satisface el mínimo explícito.
- Validación mediante script: decodificación UTF-8 estricta válida; 150 filas físicas; exactamente un `;` y dos campos no vacíos por fila; sin encabezado, filas vacías, campos adicionales, comas delimitadoras, comillas desbalanceadas, ni indicadores de texto corrupto (`Ã¡`, `Ã±`, `�`). Las 20 preguntas en español incluyen `¿` y el cierre `?`.
- Los sujetos y referentes se identifican en español mediante pronombres explícitos, nombres, grupos nominales o la flexión verbal pertinente; las formas imperativas no requieren pronombre sujeto expreso. Las traducciones son globalmente equivalentes y cada fila se entiende por separado. La longitud y variedad aumentan en general dentro de cada bloque.
- **Observación previa de fila 53 resuelta:** `Mi hermana se levanta antes de ir a la escuela.;My sister gets up before going to school.` La redacción actual es natural y conserva el sentido; no requiere cambio.

## Observaciones pendientes

1. **Prioridad media — filas 78, 84 y 89 (bloque `make sure`):** en las instrucciones afirmativas `Asegúrate de que…`, el indicativo `está` suena poco natural; el subjuntivo expresa correctamente el estado que se debe comprobar/garantizar. Cambiar, conservando el inglés, a:
   - Fila 78: `Asegúrate de que la puerta esté cerrada.;Make sure the door is closed.`
   - Fila 84: `Asegúrate de que el niño esté seguro.;Make sure the child is safe.`
   - Fila 89: `Asegúrate de que la ventana esté cerrada antes de salir.;Make sure the window is closed before you leave.`

2. **Prioridad baja — fila 4:** `Mi inglés mejora con práctica.;My English gets better with practice.` La frase española resulta poco idiomática sin artículo en este contexto. Cambiar a `Mi inglés mejora con la práctica.;My English gets better with practice.`

Corregir estas cuatro filas y solicitar nueva auditoría de la iteración siguiente.