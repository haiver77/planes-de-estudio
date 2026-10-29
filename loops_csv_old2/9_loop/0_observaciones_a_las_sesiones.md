# Informe de revisión — A1-S001 a A1-S005, iteración global 8

**Dictamen: requiere correcciones y otra iteración.** Alcance revisado exclusivamente: `loops_csv/8_loop/A1/A1-S001.csv` a `A1-S005.csv`, plan aprobado de `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`, catálogo de trazabilidad y los informes de `loops_csv/6_loop/`, `7_loop/` y `8_loop/`. No se revisó ningún otro CSV ni `loops_csv_old`.

## Evidencia de cobertura y validación técnica

- Los cinco archivos solicitados existen y corresponden a los IDs A1-S001–A1-S005 del plan.
- Script Python sobre los bytes y registros CSV: los cinco decodifican con UTF-8 estricto, sin BOM; cada archivo contiene exactamente 150 registros CSV y 150 líneas físicas, con dos campos por registro, sin encabezado, campos vacíos, filas en blanco, comillas mal cerradas ni saltos de línea incrustados. Cada línea física tiene un único `;` como separador. Se cumple el mínimo de 150 pares por archivo.
- No se detectaron secuencias de mojibake ni U+FFFD. Todas las preguntas españolas revisadas tienen `¿` y `?` de cierre válido, excepto la sustitución literal descrita en S002-67.
- Las filas 1–60 de cada archivo presentan las 12 unidades nuevas del catálogo, cinco pares por unidad y en el orden previsto. El reparto de filas corresponde al plan: S001 60 nuevas + 30 de gramática + 60 de integración; S002 y S003 60 + 12 de repaso + 30 + 48; S004 y S005 60 + 24 de repaso + 30 + 36.
- Los seis bloques de repaso previstos se cotejaron unidad por unidad. S003 61–72, S004 61–72 y 73–84, S005 61–72 y 73–84 cubren 12/12 unidades. S002 61–72 cubre 11/12: no queda demostrado el objetivo A1-S001-U07 (`It’s a good idea to…`), como se detalla abajo.
- No hay pares duplicados exactos dentro de los archivos. Las coincidencias literales entre sesiones se limitan a repasos léxicos planificados y a muestras de gramática retomadas expresamente por el plan (S001→S002 y S004→S005); no se detectó duplicación literal fuera de esos repasos.
- Se verificaron como corregidas las observaciones previas sobre S004-22, S005-119, S001-74, S002-46, S005-19/61, S004-68 y S003-89/96. Las repeticiones literales cruzadas observadas en el informe de loop 8 ya no aparecen fuera de los repasos planificados.

## Observaciones pendientes priorizadas

### Prioridad alta — integridad de caracteres y repaso incompleto

1. **`A1-S002.csv`, fila 67 — carácter sustituido y cobertura léxica insuficiente.**  
   Actual: `Un paraguas es una buena idea porque est? lloviendo.;An umbrella is a good idea because it is raining.` El `?` ASCII sustituye la `á` de `está`. Además, el par no practica inequívocamente la unidad A1-S001-U07 (`It’s a good idea to…`): formula que el paraguas es una buena idea, pero no la construcción «es buena idea hacer algo». Por eso el bloque 61–72 queda en 11/12.  
   **Cambio requerido:** sustituir la fila por una pareja que recupere U07 y corrija el carácter, por ejemplo: `Es buena idea llevar un paraguas cuando llueve.;It is a good idea to take an umbrella when it rains.` Después, volver a validar bytes y buscar sustituciones ASCII de letras.

### Prioridad alta — construcciones gramaticales adelantadas

2. **`A1-S001.csv`, filas 44 y 102; fila 52.** S001 introduce G01 (pronombres sujeto y *be*), no el auxiliar *do* ni el modal *can*. Las filas 44 y 102 usan preguntas con *Do you agree…?* (G04); la 52 usa *Can you give me…?* (G07). No se señala el vocabulario obligatorio `agree with` ni `a little help`, sino las construcciones interrogativas/modal no previstas para esta sesión.  
   **Cambio requerido:** retirar *do*-support y *can* de estas filas o trasladarlas a la sesión gramatical correspondiente. Mantener el vocabulario con afirmaciones sencillas, por ejemplo `Estoy de acuerdo con mi hermano sobre el juego.;I agree with my brother about the game.` y `Necesito un poco de ayuda con esta bolsa.;I need a little help with this bag.`

3. **`A1-S002.csv`, filas 13, 41–42 y 45.** La sesión trabaja G02 y repasa G01; *have got* (fila 13) se introduce en G03, el auxiliar *does* (filas 41–42) en G04 y *can* (fila 45) en G07. Son estructuras gramaticales adelantadas, no observaciones sobre los lemas obligatorios `a lot to do` o `anyone else`.  
   **Cambio requerido:** reformular sin esas construcciones o reservarlas para las sesiones que las introducen. Por ejemplo, usar `Tengo mucho que hacer hoy.;I have a lot to do today.` en la fila 13; convertir las preguntas con *does* en afirmaciones con `Someone else…`; y cambiar `Can anyone else help…?` por una afirmación sin modal que conserve `anyone else`.

4. **`A1-S003.csv`, filas 4, 8, 45 y 48.** S003 trabaja G03 y repasa G02; las preguntas con *does/do* de las filas 4, 45 y 48 anticipan G04, y *Can you ask…?* de la fila 8 anticipa G07. La unidad léxica `ask for` sí es obligatoria; el modal de la fila 8 no lo es.  
   **Cambio requerido:** sustituir esas preguntas por afirmaciones compatibles con los objetivos ya cubiertos, preservando los lemas donde corresponda. Ejemplos: `El vuelo llega a Roma al mediodía.;The flight arrives in Rome at noon.`; `Pido un mapa de la ciudad.;I ask for a city map.`

5. **`A1-S004.csv`, filas 101, 104 y 105.** S004 introduce G04 (present simple y *do/does*) y repasa G03. Las filas 101 y 104 usan pasiva en inglés (`The match is cancelled…`, `The shop is closed…`), y la fila 105 usa `cannot`, modal de G07. Estas construcciones no son necesarias para practicar `because of`.  
   **Cambio requerido:** reescribir en presente simple activo y sin modal, por ejemplo: `Cancelamos el partido por la tormenta.;We cancel the match because of the storm.`; `La tienda cierra por un problema eléctrico.;The shop closes because of an electrical problem.`; `Dormimos mal por el ruido de la calle.;We sleep badly because of the street noise.`

**Acción requerida:** corregir las filas señaladas, conservar el formato y las 150 parejas por archivo, guardar en UTF-8 y entregar otra iteración para revisión.
