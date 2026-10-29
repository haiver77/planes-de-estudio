# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005, iteración global 15

**Resultado: requiere correcciones; se necesita otra iteración global (16).**

## Alcance y evidencia

Se auditaron exclusivamente `A1-S001.csv` a `A1-S005.csv` en `loops_csv/15_loop/A1/`, cotejándolos con el plan aprobado de la iteración 11, el catálogo de trazabilidad y todas las observaciones del informe de iteración 15. No se revisó el resto del nivel ni `loops_csv_old`.

Los cinco archivos requeridos están presentes, uno por cada ID dentro del alcance; no se extendió la búsqueda a otros IDs del nivel. La lectura desde bytes y validación con lector CSV estricto confirma en cada archivo UTF-8 válido, sin BOM, exactamente 150 registros, dos campos por registro, sin encabezado, filas vacías, campos vacíos, campos extra, comillas mal cerradas ni saltos de línea dentro de campos. No se detectaron secuencias de mojibake ni U+FFFD; las preguntas españolas revisadas llevan apertura `¿` y cierre `?`. No hay pares duplicados exactos dentro de los archivos ni entre ellos. Los cinco CSV alcanzan el mínimo de 150 pares.

El recuento y la correspondencia con el catálogo son: S001, 60 pares nuevos + 30 gramaticales + 60 de integración; S002 y S003, 60 nuevos + 12 de repaso + 30 gramaticales + 48 de integración; S004 y S005, 60 nuevos + 24 de repaso + 30 gramaticales + 36 de integración. Se verifican las 12 unidades nuevas × 5 ejemplos por sesión y los eventos de repaso de 12/12 unidades en cada CSV donde vencen. No se detectan IDs ausentes o ajenos.

Las correcciones previas de S002-61–72 para `Good idea!` y `That’s a good idea!` ya distinguen las dos expresiones y sus equivalencias son correctas: S002-66 usa `Good idea!` / `¡Buena idea!`; S002-68 usa `That’s a good idea!` / `¡Esa es una buena idea!`. El bloque G02 de S002-73–98 ya ofrece afirmaciones, negaciones, preguntas y contrastes de singular/plural y proximidad; no se observa adelanto de otro objetivo gramatical en ese bloque. También se corrigieron satisfactoriamente los contextos señalados en S003-61, 62, 66, 71 y 72, y en S005-61, 67, 70, 73, 74, 77, 78, 79 y 84, salvo las observaciones nuevas o persistentes que siguen.

## Observaciones pendientes priorizadas

### Prioridad alta — todavía hay repasos que solo cambian referentes o conservan el mismo marco

1. **A1-S003-63, -67 y -68 — transferencia insuficientemente nueva respecto de A1-S002.**
   - **S003-63** (`Él tiene mucho que hacer antes de que llegue el autobús.`) conserva casi literalmente el marco de S002-11 (`Tengo mucho que hacer antes de la cena`): “tener mucho que hacer antes de [un evento]”. Cambiar la cena por la llegada del autobús no crea una situación comunicativa suficientemente nueva.
   - **S003-67** (`La canción es popular en todo el mundo.`) vuelve al dominio musical de S002-32 (`La gente escucha la música de ese grupo en todo el mundo`); cambia la canción/el grupo, pero mantiene la misma idea de música conocida mundialmente.
   - **S003-68** pregunta si hace falta algo más para preparar la cena, y S002-36/37 ya practicaban `anything else` en el desayuno y al pedir del menú. Cambia la comida, pero permanece el contexto de comida/menú.

   **Cambio requerido:** sustituye estos tres ejemplos por contextos realmente distintos de los de introducción, manteniendo respectivamente `a lot to do`, `all over the world` y `anything else`. No basta con sustituir el acontecimiento, el referente musical o el momento de la comida.

2. **A1-S004-65–69 — persisten transferencias de superficie en el repaso de A1-S003.**
   - **S004-65/66** llevan `at the beginning` y `at the end` de una película a un concierto, pero reproducen la misma secuencia de evento de entretenimiento que empieza con una presentación y termina con una reacción/despedida del público.
   - **S004-67** cambia la farmacia al final de una calle por una puerta al final de un pasillo: ambos ejemplos solo ubican un objeto al final de un espacio.
   - **S004-68** cambia la biblioteca cerrada en ese momento por una sala de vacunación cerrada en ese momento; conserva la misma situación de establecimiento cerrado.
   - **S004-69** sustituye la alarma y el teléfono que suenan simultáneamente por dos altavoces que se encienden simultáneamente. Sigue siendo la misma escena de dispositivos electrónicos que coinciden en el tiempo.

   **Cambio requerido:** reescribe esos pares usando actividades, necesidades o escenarios distintos, no solo otro espectáculo, edificio, objeto o dispositivo. Conserva los objetivos léxicos respectivos (`at the beginning`, `at the end`, `at the end of`, `at the moment`, `at the same time`) y mantén cada fila autónoma.

### Prioridad alta — sigue sin quedar determinado el intervalo de S005-82

3. **A1-S005-82 — `a period of time` continúa siendo genérico.** El par actual dice que el ayuntamiento vigila el nivel del río “durante un período de tiempo” después de la crecida y termina los controles el viernes si el agua se mantiene bajo el límite. La condición y el viernes añaden información, pero no determinan cuánto dura el seguimiento desde la crecida; además, si no se cumple la condición, tampoco se indica el término. La expresión genérica que motivó la observación anterior permanece intacta.

   **Cambio requerido:** fija una duración plausible o una condición de término inequívoca vinculada al seguimiento (por ejemplo, hasta que el nivel baje del límite, con la frecuencia o el plazo que corresponda) y elimina `for a period of time` como intervalo inespecífico. Asegura que ambas versiones expresen la misma condición y duración.

### Prioridad media — carga léxica inadecuada para A1 en el bloque G02

4. **A1-S002-77–98 — la variedad gramatical mejoró, pero varios contextos exigen vocabulario especializado que no corresponde al nivel ni al objetivo comunicativo inmediato.** Ejemplos: `sendero accesible`, `documentos de registro`, `cascos de seguridad del equipo de rescate`, `copia legible del contrato`, `código de acceso`, `cajas de archivo`, `aviso de evacuación`, `solicitudes de empleo`, `jurado`, `coro infantil`, `frascos del laboratorio`, `sala de examen`, `planos del metro` y `facturas originales`. Esto desplaza la práctica de demostrativos y objetos inmediatos hacia escenarios y términos técnicos.

   **Cambio requerido:** conserva el contraste de demostrativos, número, distancia, preguntas y negaciones, pero sustituye la mayoría de esos escenarios por objetos y situaciones cotidianos de nivel A1. Mantén diversidad de intención y estructura; no vuelvas a una plantilla única de sustitución.

## Veredicto

No aprobar todavía. Aunque los cinco CSV cumplen el formato, la cantidad, la codificación, la cobertura de unidades y los conteos de repaso/gramática, quedan repasos con transferencia superficial, S005-82 sin intervalo suficientemente determinado y una carga léxica impropia en el bloque G02. Corregir únicamente estos cinco archivos para la iteración global 16 y volver a auditar.
