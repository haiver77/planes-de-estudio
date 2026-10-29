# Informe de auditor?a ling??stica y t?cnica ? A1-S001 a A1-S005

**Iteraci?n auditada:** `loops_csv/38_loop/A1/` (solo los cinco CSV especificados).  
**Informe de salida:** `loops_csv/39_loop/0_observaciones_a_las_sesiones.md`  
**Referencias cotejadas:** plan aprobado y cat?logo de `loops_plan/11_loop/`, `indicaciones_csv.md`, `contexto.md` e informes `loops_csv/33_loop/` a `loops_csv/38_loop/`.

## Comprobaciones t?cnicas, cantidad y cobertura

- La carpeta auditada contiene exactamente `A1-S001.csv` a `A1-S005.csv`, sin IDs faltantes ni archivos ajenos.
- Se verificaron los bytes con decodificaci?n UTF-8 estricta y lectura CSV estricta. Cada archivo contiene **150 registros y 150 l?neas f?sicas**, sin encabezado; cumple el m?nimo obligatorio expl?cito de 150 pares.
- Todas las filas tienen dos campos no vac?os separados por `;`. No se detectaron filas vac?as, campos adicionales, delimitaci?n por comas, punto y coma dentro de campos, saltos de l?nea incrustados, comillas ASCII sin cerrar, columnas invertidas, preguntas espa?olas sin `?`, caracteres de reemplazo, mojibake ni `?` sustituyendo letras. Los signos diacr?ticos y de apertura aparecen correctamente. No hay duplicados exactos de pares ni de frases en espa?ol o ingl?s.
- El cat?logo asigna 12 unidades l?xicas foco a cada sesi?n y est?n representadas en sus bloques iniciales. Se cotejaron tambi?n los objetivos gramaticales, la distribuci?n de repaso y la integraci?n; los defectos pedag?gicos concretos que impiden aprobar se detallan abajo.
- Se revisaron las observaciones previas fila por fila. Entre otras correcciones verificadas: S003-126, S002-147, S004-57/58, S004-132, S001-20, S001-29/30, S002-49/50, S004-23/25, S004-29/30, S004-33/45/50, S001-138/140/145, S005-127, S003-59/60, S005-49/50, S001-44/45, S002-56/60, S003-22/25, S003-55, S001-129, S005-94/99/20/29/30/90 y S004-4/5/31/53?55 ya fueron modificadas o mejoradas. La secuencia de llegada de S002 y la de acuerdo de S001 a?n requieren los ajustes concretos anotados a continuaci?n.

## Observaciones pendientes ? se requiere otra iteraci?n

### Prioridad alta: progresi?n gramatical prevista

1. **`A1-S004.csv`, filas 9, 15, 18, 20, 40 y 49?50; `A1-S005.csv`, fila 144 ? se adelantan estructuras no previstas para estas sesiones.**  
   S004 introduce *can* (9: `can cause pain`; 20: `can fall`; 49?50: `can use`), *have to* (15: `has to get up early`), *there are* antes de la sesi?n G05 (18) y presente continuo (40: `my sister is setting the table`, objetivo de S006). S005-144 vuelve a usar *have to* (`Tenemos que ordenar...; We have to tidy...`), que no es el foco de G05 y aparece en objetivos posteriores. Estos usos no son necesarios para los objetivos de esas frases y s? hacen practicar anticipadamente gram?tica fuera de la progresi?n indicada. **Cambio requerido:** reescribir esas cl?usulas con vocabulario A1 y las formas ya introducidas en su sesi?n (S004: presente simple/`do`/`does`; S005: `there is/are` y cuantificadores), evitando *can*, *have to* y el presente continuo en las filas se?aladas. En S004, no eliminar la unidad de vocabulario `be going to do sth` asignada expresamente por el cat?logo; limitar el problema al material adicional no previsto.

### Prioridad media: equivalencia, claridad, naturalidad y nivel A1

2. **`A1-S002.csv`, fila 60 ? ambig?edad de sujeto en la progresi?n `arrive at` (seguimiento de la observaci?n previa sobre 56?60).**  
   `Llegamos a la estaci?n hoy en autob?s desde el centro con mi hermana.;We arrive at the station today by bus from the city centre with my sister.` La extensi?n conserva el destino, pero el sujeto plural de ?llegamos/we? no aclara si la hermana forma parte del grupo; ?con mi hermana/with my sister? resulta redundante o deja incierto qui?nes llegan. **Cambio requerido:** identificar claramente al grupo y ampliar con un detalle coherente, por ejemplo `Mi hermana y yo llegamos a la estaci?n hoy en autob?s desde el centro y compramos los billetes juntas.;My sister and I arrive at the station today by bus from the city centre, and we buy the tickets together.`

3. **`A1-S001.csv`, fila 45 ? ampliaci?n no queda bien enlazada con la idea anterior.**  
   La fila 44 trata de estar de acuerdo con Ana sobre el viaje; la 45 dice `Hoy en clase estoy de acuerdo con Ana y yo le pregunto al profesor despu?s de clase.` La relaci?n entre estar de acuerdo y preguntar al profesor no se expresa y, al quitar ?sobre el viaje?, la ampliaci?n deja de recuperar ese contexto. La observaci?n anterior de sujeto/tiempo s? qued? corregida, pero la secuencia contin?a d?bil. **Cambio requerido:** conservar expl?citamente el tema del viaje y vincularlo a la pregunta, por ejemplo `Hoy en clase estoy de acuerdo con Ana sobre el viaje y despu?s de clase le pregunto al profesor sobre el viaje.;Today in class, I agree with Ana about the trip, and after class I ask the teacher about the trip.`

4. **`A1-S005.csv`, fila 27 ? colocaci?n redundante.**  
   `Comparamos las diferencias entre el tren y el autob?s.;We compare the differences between the train and the bus.` ?Comparar diferencias? repite la noci?n de contraste y no es una formulaci?n natural para la escena. **Cambio requerido:** conservar la expresi?n foco con una construcci?n idiom?tica, por ejemplo `Vemos algunas diferencias entre el tren y el autob?s.;We see some differences between the train and the bus.`

5. **`A1-S005.csv`, fila 44 ? acumulaci?n l?xica menos b?sica para una frase de repaso A1.**  
   `Mi pareja y yo nos ayudamos mutuamente a preparar la mudanza.;My partner and I help each other prepare for the move.` ?Pareja/partner?, ?mudanza/move? y ?mutuamente? hacen la frase menos inmediata y m?s cargada que los ejemplos cercanos de *each other*. **Cambio requerido:** usar una relaci?n y tarea familiar de A1, por ejemplo `Mi hermana y yo nos ayudamos con la tarea.;My sister and I help each other with our homework.`

6. **`A1-S004.csv`, fila 79 ? l?xico/contexto por encima del nivel para integraci?n.**  
   `Es una buena idea etiquetar las cajas antes de la mudanza.;It?s a good idea to label the boxes before the move.` La colocaci?n es plausible, pero ?etiquetar/label? y ?mudanza/move? a?aden vocabulario menos b?sico que no hace falta para reciclar `It?s a good idea to?`. **Cambio requerido:** conservar el inicio objetivo en una escena cotidiana sencilla, por ejemplo `Es buena idea cerrar la puerta al salir.;It?s a good idea to close the door when you leave.`

7. **`A1-S002.csv`, filas 4?5 ? acumulaci?n y orden poco natural de complementos en la progresi?n de `a little sugar`.**  
   `Necesito un poco de az?car para el caf? hoy en la cocina antes del desayuno.;I need a little sugar for the coffee today in the kitchen before breakfast.` ?Hoy/en la cocina/antes del desayuno? acumula referencias temporales y locativas; en ingl?s el orden suena forzado y ?today? no aporta informaci?n ?til junto a ?before breakfast?. **Cambio requerido:** retirar el detalle redundante y ordenar la ampliaci?n con naturalidad, por ejemplo `Necesito un poco de az?car para el caf? en la cocina antes del desayuno.;I need a little sugar for my coffee in the kitchen before breakfast.`

## Resultado

La cobertura de IDs, codificaci?n, formato y m?nimo de pares s? cumplen. Persisten defectos ling??sticos y de fidelidad a la progresi?n (incluida una observaci?n anterior de secuencia a?n no resuelta del todo); corregir las filas indicadas y volver a auditar ?nicamente estos cinco CSV en la siguiente iteraci?n. **NO COMPLETO; se requiere otra iteraci?n.**
