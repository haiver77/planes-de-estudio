# Trazabilidad de la corrección C2 — Iteración 7

## Alcance del cambio

Se atiende el hallazgo del informe de revisión de `6_loop`: las diez recuperaciones gramaticales C2 que antes estaban asignadas intrasesión dejan de contarse como espaciadas. Se agregan seis sesiones terminales C2 de integración, sin nuevo vocabulario, y se actualizan en el plan la matriz ICOG, el conteo, la secuencia y las filas C2. No se modifica ningún archivo de iteraciones anteriores.

## Evidencia de separación entre sesiones

La secuencia global está fijada en el plan como A1 1–26, A2 27–45, B1 46–65, B2 66–136, C1 137–253 y C2 254–265. Cada número global corresponde a una sesión CSV distinta. C2-S001–C2-S006 ocupan los órdenes 254–259; C2-S007–C2-S012 ocupan los órdenes 260–265. El calendario no asigna fechas de calendario porque no se especificó la frecuencia diaria o semanal, pero los órdenes son inequívocos.

| Tema | Introducción | Repaso +1 | Repaso +3 | Repaso +6 |
|---|---:|---:|---:|---:|
| C2-G01 — Elipsis, sustitución y fragmentos discursivos | C2-S001 (254) | C2-S002 (255) | C2-S004 (257) | C2-S007 (260) |
| C2-G02 — Inversión y anteposición con foco pragmático | C2-S002 (255) | C2-S003 (256) | C2-S005 (258) | C2-S008 (261) |
| C2-G03 — Modalidad, evidencialidad y grados de compromiso | C2-S003 (256) | C2-S004 (257) | C2-S006 (259) | C2-S009 (262) |
| C2-G04 — Concesión, reformulación y rectificación | C2-S004 (257) | C2-S005 (258) | C2-S007 (260) | C2-S010 (263) |
| C2-G05 — Registro, información dada/nueva y ambigüedad | C2-S005 (258) | C2-S006 (259) | C2-S008 (261) | C2-S011 (264) |
| C2-G06 — Nominalización, densidad y alternancia de voz | C2-S006 (259) | C2-S007 (260) | C2-S009 (262) | C2-S012 (265) |

Las diferencias de orden son, en cada fila, exactamente +1, +3 y +6. La sesión terminal C2-S012 permite el último destino +6 de C2-G06. Ninguna celda remite a un bloque interno ni a la sesión de introducción. Los eventos C2 son 18 recuperaciones, las 18 posteriores a la introducción; el total ICOG permanece en 189 eventos (63 temas × 3 recuperaciones), ahora 189 posteriores y 0 intrasesión.

Las seis sesiones añadidas no agregan más de 150 pares: cada una asigna 30 pares al repaso gramatical (10 pares por tema si hay tres temas, 15 por tema si hay dos, o 30 al tema único) y 120 a integración/recuperación léxica acumulativa. Las sesiones iniciales de C2 también conservan su reparto de 150 pares declarado en la tabla del plan.

## Preservación y cotejo del catálogo Oxford de la iteración 6

`2_catalogo_trazabilidad_fuentes.csv` se copió a esta iteración sin alterar bytes. Verificación reproducible entre los archivos de 6_loop y 7_loop:

- Igualdad binaria: **sí**.
- SHA-256 en ambas iteraciones: `2b5426db80a0f7b4bc5393ff220a2e6cedf14465e3721d7a543b7747a3835953`.
- 3.015 filas de datos, 3.015 referencias de fuente distintas y 3.014 IDs léxicos canónicos distintos.
- Oxford 5000: B2 700 y C1 1.314 registros (2.014 en total).
- Oxford Phrase List: A1 303, A2 228, B1 233, B2 148 y C1 89 (1.001 en total).
- No hay entradas de fuente atribuidas a C2.
- Las 3.015 referencias de sesión del catálogo encuentran un ID de sesión en el plan actualizado. No se cambiaron IDs de sesiones léxicas; por ello no se editaron las asignaciones Oxford ni sus destinos +1/+3/+6.

## Referencias internas y límite de esta trazabilidad

El plan actualizado está en `1_plan_estudio_por_sesiones_de_repeticion.md`; el catálogo preservado está en `2_catalogo_trazabilidad_fuentes.csv`. No se declara aquí una revisión independiente ni un veredicto de completitud: se documentan los cambios y las comprobaciones específicas solicitadas.
