# Informe de revisión — Iteración 1, nivel A1

Alcance: `PF-A1-001`, `PF-A1-002` y `PF-A1-003`, contrastadas con el plan aprobado y `indicaciones_csv.md`.

## PF-A1-001 — `PF-A1-001.csv`

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** En varios focos se repite la misma oración cambiando únicamente el adverbio temporal, sin progresión suficiente de longitud ni variedad de contextos (por ejemplo, filas 006–015, 026–030, 036–045 y bloques posteriores). Sustituir parte de esas variantes por ejemplos distintos, naturales y gradualmente más extensos que consoliden el foco.

**Reglas incumplidas por línea**
- **Fila 044 — Regla: Frase con sentido.** «Por la mañana, ella se prepara por la mañana» repite innecesariamente la misma circunstancia. Reemplazar por: `Por la mañana, ella se prepara.;In the morning, she gets ready.`
- **Fila 086 — Regla: Frase con sentido.** «Me aseguro de llevar las llaves cuando salgo» no corresponde a «Today, I make sure I take the keys»: falta «cuando salgo» y se añade «Today». Reemplazar por: `Me aseguro de llevar las llaves cuando salgo.;I make sure I take the keys when I leave.`
- **Fila 087 — Regla: Frase con sentido.** «Siempre» y «guardar las llaves en mi bolso» no corresponden a «Sometimes» ni a «take the keys». Reemplazar por: `Siempre me aseguro de guardar las llaves en mi bolso.;I always make sure I keep the keys in my bag.`
- **Fila 088 — Regla: Frase con sentido.** El sujeto y la acción de «Mi padre se asegura de llevar las llaves del coche» no corresponden a «Usually, I make sure I take the keys». Reemplazar por: `Mi padre se asegura de llevar las llaves del coche.;My father makes sure he takes the car keys.`
- **Fila 090 — Regla: Frase con sentido.** «Ella se asegura de cerrar todas las ventanas» no corresponde a «This week, I make sure I take the keys». Reemplazar por: `Ella se asegura de cerrar todas las ventanas.;She makes sure she closes all the windows.`

## PF-A1-002 — `PF-A1-002.csv`

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** Se repite mecánicamente una oración base con cambios de adverbio temporal en varios focos, en lugar de una progresión de longitud y contextos variados (por ejemplo, filas 006–012, 018–024, 030–036 y bloques posteriores). Reemplazar parte de esas variantes con ejemplos nuevos, naturales y gradualmente más extensos que practiquen el vocabulario objetivo.

**Reglas incumplidas por línea**
- **Fila 072 — Regla: Frase con sentido.** «A veces, ¿quieres…?» / «Sometimes, would you like…?» resulta poco natural como pregunta. Reemplazar por: `¿A veces quieres un poco más de arroz?;Do you sometimes want a little more rice?`

## PF-A1-003 — `PF-A1-003.csv`

**Reglas generales por archivo incumplidas**
- **Regla: Progresion y repetición incremental.** Se repite mecánicamente la misma estructura con adverbios temporales en varios focos, sin progresión suficiente de longitud ni variedad de contextos (por ejemplo, filas 006–008, 014–016 y bloques posteriores). Reemplazar parte de esas variantes con ejemplos distintos, naturales y gradualmente más extensos que practiquen el vocabulario objetivo.

**Reglas incumplidas por línea**
- **Fila 108 — Regla: Frase con sentido.** «Ella dice gracias a su amiga» no es una formulación natural en español. Reemplazar por: `Ella le da las gracias a su amiga.;She thanks her friend.`
- **Fila 137 — Regla: Frase con sentido.** «Querer algo» expresa “to want something”, no el foco «would like». Reemplazar por: `Me gustaría algo.;Would like something.`
- **Fila 138 — Regla: Frase con sentido.** «Quiero» no expresa el matiz de cortesía de «would like». Reemplazar por: `Me gustaría un té.;I would like some tea.`
- **Fila 139 — Regla: Frase con sentido.** «Ella quiere» no expresa el matiz de cortesía de «would like». Reemplazar por: `A ella le gustaría un poco de agua.;She would like a little water.`
- **Fila 142 — Regla: Frase con sentido.** «Quiero» no corresponde al matiz de «would like». Reemplazar por: `Hoy, me gustaría tomar un té.;Today, I would like to have some tea.`
- **Fila 143 — Regla: Frase con sentido.** «Quiero» no corresponde al matiz de «would like». Reemplazar por: `A veces, me gustaría tomar un té.;Sometimes, I would like to have some tea.`
- **Fila 144 — Regla: Frase con sentido.** «Quiero» no corresponde al matiz de «would like». Reemplazar por: `Por la mañana, me gustaría tomar un té.;In the morning, I would like to have some tea.`

## Comprobaciones generales

- **Regla: Cobertura:** están los tres CSV solicitados, uno para cada ID auditado; no falta ninguno dentro del alcance.
- **Regla: Formato y codificación:** los tres archivos se decodifican como UTF-8 válido y contienen dos columnas separadas por `;`, sin encabezado. La lectura y el análisis estricto no encontraron filas vacías, campos adicionales, delimitadores incorrectos, comillas mal cerradas ni caracteres de reemplazo o texto corrupto.
- **Regla: Cantidad:** `PF-A1-001.csv` tiene 150 pares; `PF-A1-002.csv`, 156; `PF-A1-003.csv`, 152. Todos alcanzan el mínimo de 150.

**Sesiones completadas para omitir en la siguiente iteración:** ninguna. Las tres sesiones requieren correcciones y otra iteración.
