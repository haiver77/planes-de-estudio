# Informe de revisión lingüística y técnica — A1-S001 a A1-S005, iteración global 10

**Resultado: requiere correcciones; se necesita otra iteración.** Alcance exclusivo: `loops_csv/10_loop/A1/A1-S001.csv` a `A1-S005.csv`. Referencias: plan aprobado `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, catálogo `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`, `indicaciones_csv.md` e informe histórico `loops_csv/10_loop/0_observaciones_a_las_sesiones.md`. No se auditó el resto del nivel ni `loops_csv_old`.

## Comprobaciones que sí cumplen

- **Cobertura del alcance:** están los cinco archivos solicitados, sin faltantes ni IDs ajenos dentro de este alcance.
- **Formato y bytes:** lectura estricta de los bytes con UTF-8 real, sin BOM. Todos tienen 150 líneas físicas y 150 registros CSV; cada registro tiene exactamente dos campos separados por `;`, sin encabezado, campos vacíos, filas en blanco, comillas mal cerradas ni saltos de línea incrustados. No se encontró uso de comas como delimitador. Se revisaron `á é í ó ú ü ñ ¿ ¡`: no se detectó `Ã¡`, `Ã±`, U+FFFD ni `?` sustituyendo letras; las preguntas españolas observadas llevan apertura `¿` y cierre `?`.
- **Cantidad y reparto:** los cinco CSV tienen 150 pares cada uno (750 total), cumpliendo el mínimo. Cada sesión contiene 60 pares para 12 unidades nuevas ×5, 30 pares gramaticales, y las cantidades de integración/repaso previstas: S001 0 de repaso +60 de integración; S002 y S003 12 +48; S004 y S005 24 +36. Los cinco eventos de repaso del plan cubren 12/12 unidades cada uno (60 pares de repaso en total). El catálogo confirma 12 unidades nuevas asignadas a cada una de las cinco sesiones; los bloques 1–60 corresponden a esas 12 unidades en grupos de cinco.
- **Duplicados exactos:** la validación no encontró filas completas duplicadas dentro de ningún CSV. Sí hay repetición de frases/plantillas en los ejemplos señalados abajo.
- **Progresión histórica y gramática:** están corregidos los defectos n9 de `can`/`would`, do-support o existenciales adelantados en S001–S003, las pasivas de causa en S004 y S005, y la traducción de ayuda en S002-147. La voz activa actual de S004-26/28 y S005-66 ya no presenta el defecto pasivo anterior. El do-support de S004 está dentro de G04 y el de S005 repasa G04; `there is/are` en S005 corresponde a G05. El patrón `be going to` en S004 y el pasado de `He came into the room` en S005 corresponden a unidades léxicas explícitas del catálogo, por lo que no se marcan como adelantos ajenos. Las formas `is closed` detectadas son estados/adjetivos, no pasivas de evento.

## Observaciones pendientes priorizadas

### Prioridad alta — gramática fuera de la progresión y repetición contextual

1. **`A1-S004.csv`, filas 1, 3 y 54.** `Keep the children…`, `Keep the phone…` y `Leave the car…` son imperativos. La matriz del plan reserva los imperativos para G07 en A1-S007; S004 introduce G04. Aunque el objetivo comunicativo de S004 menciona instrucciones breves, la secuencia gramatical aún no ha introducido el imperativo. **Cambio requerido:** resuelve la discordancia con el plan: reescribe estas tres filas como enunciados no imperativos conservando el vocabulario (por ejemplo, “Los niños se mantienen lejos del fuego.;The children stay away from the fire.”; “Mi hermano guarda el teléfono lejos del agua.;My brother keeps the phone away from the water.”; y una oración declarativa sobre el coche en el aparcamiento), o ajusta explícitamente la secuencia del plan antes de mantener estos comandos.

2. **`A1-S003.csv`, fila 100.** `Estos son los libros que buscamos.;These are the books we are looking for.` El inglés usa presente continuo (`are looking for`), cuyo foco G06 está previsto para A1-S006; el español está en presente simple. **Cambio requerido:** cambia el par a una formulación natural de presente simple que conserve el sentido de búsqueda, o reserva este continuo para después de introducir G06; mantén ambas columnas equivalentes en aspecto.

3. **`A1-S004.csv`, filas 101 y 103.** Persisten dos ejemplos casi paralelos sobre el mismo partido afectado por el tiempo: cancelarlo por la tormenta frente a retrasar su inicio por la nieve. Esto mantiene la repetición contextual que ya se había señalado en n9; no son dos transferencias suficientemente distintas. **Cambio requerido:** sustituye una fila por otro contexto de `because of` (por ejemplo, el cierre temprano de un museo por nieve intensa), sin repetir el partido ni la misma plantilla de causa meteorológica.

### Prioridad media — equivalencia, naturalidad y variedad

4. **`A1-S003.csv`, filas 120 y 146.** En la 120, `Mi hermana estudia en la universidad.` se traduce como `My sister is at university`, que indica ubicación/condición de estudiante, no que esté estudiando; cambia a `My sister studies at university.` En la 146, `Compartimos el mismo libro de inglés.` se traduce como `We have got the same English book`, que sugiere que poseen libros iguales, no que comparten un ejemplar; cambia a `We share the same English book.` o modifica el español si se pretendía expresar posesión.

5. **`A1-S001.csv`, filas 125, 135, 137, 147 y 149.** Se repite cinco veces la fórmula editorial `Respondo: «…» / I reply, “…”`; además, los mensajes insertados reiteran casi literalmente ejemplos ya practicados (125 repite el mensaje de 37; 135 el de 30; 147 el de 29; 149 el de 36). Sin una intervención previa, “Respondo” tampoco aporta un contexto autónomo natural. **Cambio requerido:** sustituye al menos las repeticiones por situaciones/frases nuevas y autónomas, y diversifica la estructura de integración; no basta con envolver el mismo mensaje entre comillas.

6. **`A1-S002.csv`, fila 16.** `La cesta contiene mucha fruta.;A lot of fruit is in the basket.` La equivalencia básica se entiende, pero la construcción inglesa resulta menos idiomática que la española. **Cambio requerido:** usa `The basket contains a lot of fruit.`; mantiene el sentido, el nivel y la unidad léxica `a lot of sth`.

7. **`A1-S004.csv`, filas 2 y 5.** `My home is away from the station` y `We live away from our cousins` son formulaciones poco naturales en esos contextos. **Cambio requerido:** conserva `away from` con una colocación inglesa idiomática, por ejemplo `My home is a long way away from the station` y `We live far away from our cousins`.

8. **`A1-S005.csv`, fila 16.** `¿Te viene bien entrar en la sala, por favor?;Is it convenient for you to come into the living room, please?` La versión inglesa suena rígida para una petición cotidiana y concreta `living room` sin que el español especifique una sala de estar. **Cambio requerido:** usa una petición más natural y neutral respecto al tipo de habitación, alineando ambas columnas; por ejemplo, `¿Está bien entrar en la sala, por favor?;Is it all right to come into the room, please?`.

## Acción requerida

Corrige todas las observaciones, conserva el reparto de 150 pares, y vuelve a comprobar UTF-8 por bytes, estructura, objetivos gramaticales y equivalencia antes de solicitar otra auditoría. El informe está en `loops_csv/11_loop/0_observaciones_a_las_sesiones.md`; **se requiere otra iteración**.