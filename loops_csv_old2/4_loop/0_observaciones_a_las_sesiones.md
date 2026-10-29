# Informe de revisión — A1-S001 a A1-S005 (iteración global 3)

**Resultado:** requiere correcciones y otra iteración. Se revisaron las cinco sesiones solicitadas, fila por fila, frente al plan aprobado y los 13 puntos del informe anterior. No se revisó ningún otro CSV ni `loops_csv_old`.

## Evidencia técnica y cobertura

- El plan incluye A1-S001, A1-S002, A1-S003, A1-S004 y A1-S005; los cinco archivos existen.
- Se leyeron los bytes y se decodificó cada archivo con UTF-8 estricto. Los cinco son UTF-8 válido y contienen 150 registros cada uno (750 pares).
- El parser CSV estricto confirmó dos campos por registro, sin encabezados, filas vacías, campos extra ni comillas mal cerradas. No hay saltos de línea dentro de registros. Las comas son puntuación de frases, no delimitadores; el separador es `;`.
- UTF-8 válido no impide caracteres sustituidos: hay cinco `?` ASCII dentro de `caf?` (ver punto 1). Los cierres de interrogación al final de frase son válidos; las preguntas españolas revisadas conservan el signo inicial.

## Observaciones pendientes, priorizadas

### Prioridad alta: caracteres, sentido y gramática

1. **Caracteres sustituidos en inglés:** reemplazar los cinco `?` de `caf?` por `é` o usar `cafe` consistentemente:
   - `A1-S002.csv`, filas 25 y 66.
   - `A1-S003.csv`, filas 13 y 20.
   - `A1-S004.csv`, fila 55.
   Verificar el carácter en los bytes finales; UTF-8 válido no corrige el `?` dentro de la palabra.

2. **Progresión gramatical: se adelantan objetivos no asignados a estas sesiones.**
   - `A1-S001.csv`, p. ej. fila 4, y `A1-S002.csv`, p. ej. filas 6, 13 y 16: uso de `there is/there are` y cuantificadores antes de G05. El plan introduce G05 en S005; en S001 corresponde G01 y en S002 G02. Cambiar estos ejemplos por práctica de la sesión o reservarlos para S005.
   - `A1-S004.csv`, filas 36–40, 111–115, 138, 143 y 148: futuro `going to` (`Voy a llamar`, `va a estudiar`, `¿Van a…?`). G04 de S004 es present simple con `do/does`; sustituir por estructuras de G04/instrucciones corteses o reservarlas para la sesión correspondiente.
   - `A1-S005.csv`, filas 21–24 y 131–132: pasado simple (`entró`, `llegué`, `did`, `came`, `arrived`); fila 37: present perfect (`have known`). S005 se centra en G05 y repasa G04. Sustituir por presente simple/G05 o posponer hasta que el plan introduzca esos tiempos.
   - `A1-S005.csv`, fila 66: `Nos quedamos dentro por la lluvia.;We stayed inside because of the rain` deja ambiguo el tiempo español y fuerza pasado en inglés; el marco `Cerca de la estación el viernes` no lo aclara. Alinear ambos idiomas en presente simple (por ejemplo, quedarse dentro cuando llueve) y quitar el prefijo irrelevante.

3. **Sujeto ambiguo en español respecto del inglés:** precisar el pronombre cuando la forma no distingue `ellos` de `ustedes`, según las indicaciones:
   - `A1-S001.csv`, fila 66: `¿Es mi hermano?;Is he my brother?` — escribir `¿Él es mi hermano?` o ajustar ambos lados.
   - `A1-S002.csv`, fila 59, y `A1-S003.csv`, fila 72: `Llegan a la escuela...;They arrive...` — usar `Ellos llegan...` o cambiar ambos sujetos.
   - `A1-S004.csv`, filas 85–87: `Ven televisión` / `No ven televisión` / `¿Ven televisión?`, traducidas con `They`; añadir `Ellos` en las tres.
   - `A1-S005.csv`, filas 51 y 58: `Juegan...;They play...` y `Nos visitan...;They visit us...`; añadir `Ellos` o reformular ambos lados.

4. **Equivalencia léxica:** `A1-S003.csv`, fila 125, traduce `una terraza pequeña` como `a small balcony`. Usar `a small terrace` o cambiar el español para que ambos lados nombren el mismo espacio.

### Prioridad media: contexto, naturalidad, repaso y duplicación

5. **Ubicaciones/días insertados sin relación o con marcos incompatibles.** Reescribir la frase completa; no basta con intercambiar el día:
   - `A1-S002.csv`, fila 64: `En casa el miércoles, esperar unos años es mucho tiempo` acumula lugar y fecha sin función para una duración general.
   - `A1-S003.csv`, fila 71: `En la escuela el sábado, el autobús recorre la ciudad` combina la escuela con una afirmación general del recorrido, sin situación comunicativa clara.
   - `A1-S004.csv`, filas 81–84: antepone `En el parque [día]` a estar de acuerdo con la profesora, tener comida para un viaje, necesitar ayuda en la cocina y dinero para el autobús. En particular, la cocina no corresponde al parque. Crear una secuencia realmente situada allí o quitar esos marcos.
   - `A1-S005.csv`, fila 72: `En la parada del autobús el lunes, en casa, mi teléfono móvil está en el bolso` sitúa la misma escena a la vez en la parada y en casa. Elegir un solo lugar y explicar su pertinencia.
   - `A1-S005.csv`, filas 107–109: huevos y paraguas se presentan como demostrativos en la cafetería sin contexto de señalamiento/compra. Filas 114–120 anteponen `En el parque` a acostarse, que el padre esté en el trabajo, olvidar llaves o hacer una valoración general de un alimento. Quitar prefijos gratuitos y construir mini-secuencias plausibles, autónomas y transferibles.

6. **Duplicación/repetición superficial:**
   - `A1-S001.csv`, filas 15 y 108, repite literalmente `En verano, ellos van al parque varias veces`, con traducción apenas reformulada. Sustituir una por una transferencia con otro propósito o contexto.
   - `A1-S003.csv`, filas 13/109, repite pedir el menú en el café; filas 20/116 repite que la cafetería está al final de la calle. Eliminar una ocurrencia o dar a la segunda una función contextual distinta.
   - `A1-S004.csv`, filas 55–60 y 130–135, vuelve a presentar el mismo bloque de aparcamiento/teléfono. Evitar la repetición literal o convertirla en transferencia real.
   - `A1-S005.csv`, filas 68 y 123, repite hacer la tarea después de cenar cambiando solo el día; además usa futuro adelantado. Sustituir por una frase del objetivo G05 con contexto nuevo.

7. **Naturalidad y uso independiente:** las filas afectadas deben tener una situación clara, poder practicarse por separado y formar mini-secuencias con continuidad. No añadir lugar/fecha para alargar una frase. La mezcla de tiempos y los escenarios artificiales citados impiden certificar progresión y fidelidad completa al plan.

## Seguimiento de las 13 observaciones anteriores

1. **Parcial:** la cita de S001 se reformuló (fila 101); permanecen los cinco `caf?` de los archivos indicados.
2. **Parcial:** varios ejemplos inverosímiles antiguos ya cambiaron; persisten marcos artificiales en S002-64, S003-71 y S005-72/114–120.
3. **Parcial:** los ejemplos semánticos antiguos de S003 ya no aparecen en esas filas; persiste el desajuste terraza/balcón de S003-125 y hay gramática adelantada en S005.
4. **Parcial:** no se conserva literalmente la antigua frase de S005-121; S005-66 vuelve a dejar ambiguo el tiempo español frente al inglés.
5. **Parcial:** se cambiaron los casos antiguos de lugares incompatibles; S005-72 aún mezcla parada y casa.
6. **Resuelto en los ejemplos citados:** los casos de habitación/casa de S004 ya no están en esas posiciones; persisten otros prefijos irrelevantes en S004-81–84.
7. **Parcial:** cambiaron las frases antiguas de S001, pero la ambigüedad reaparece en S001-66 y queda repetición en 15/108.
8. **Parcial:** S002-101 ahora explicita `él`; se mantienen omisiones de sujeto en S002-59 y los demás ejemplos citados.
9. **Resuelto en las filas antiguas; defecto nuevo:** no se repiten literalmente las frases de pasado antiguas de S003, pero S005-21–24 y 131–132 adelantan pasado simple.
10. **Parcial:** los ejemplos antiguos de S004-61–80 cambiaron; el patrón reaparece en S004-81–84 y S005-107–120.
11. **Resuelto en la frase citada:** S005 ya no contiene el presente continuo antiguo de la fila 138; ahora hay futuro adelantado en S004 y pasado/present perfect en S005.
12. **Resuelto en el ejemplo citado:** la frase ambigua antigua de S005-148 ya no aparece; siguen escenarios poco naturales en S005-107–120.
13. **Resuelto:** S005-28 ahora mantiene singular (`alguna tienda` / `a shop`).

**Límite de evidencia sobre vocabulario:** las filas del plan identifican U01–U12 y remiten los términos exactos a un catálogo CSV. Por el alcance indicado no se revisó ningún otro CSV; por tanto, no certifico esa correspondencia término por término. Las observaciones de gramática, equivalencia, sentido y progresión sí se basan en la lectura completa de las cinco sesiones.

**Acción requerida:** corregir las filas indicadas, volver a validar UTF-8 y estructura tras guardar, y entregar otra iteración de estos cinco archivos.
