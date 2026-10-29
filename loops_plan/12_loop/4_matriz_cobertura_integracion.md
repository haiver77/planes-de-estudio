# Matriz de cobertura e integración — Iteración 12
## Addendum de trazabilidad y corrección -- iteración 12

Se conserva la matriz y el análisis pedagógico heredado: 3.306 entradas Oxford 3000 (A1 900; A2 871; B1 809; B2 726), 301 sesiones de integración, más la línea base de 265 sesiones (566 en conjunto), secuencia CEFR A1--C2, calendario, repasos y carga oral. Las asignaciones, niveles, identificadores canónicos, deduplicación, cantidades de pares y tiempos de cada sesión se mantienen sin cambios.

La iteración restaura 26 formas con capitalización significativa en `entrada_normalizada`, conserva el literal fuente, separa `clave_comparacion_casefold` y añade página, ordinal visual por columna, caja en puntos PDF, hash y método de cotejo al catálogo. Las sesiones focales existentes reciben notas contextuales, sin crear ni reasignar unidades. La evidencia visual y el procedimiento reproducible se detallan en `5_registro_de_correcciones_y_evidencia.md`, `6_metodo_cotejo_y_localizadores.md` y `7_evidencia_visual_capitalizacion.pdf`.



## Cotejo de las 3.306 filas Oxford 3000



| Nivel | Registros fuente | Ya cubierto/reutilizado | Variante o sentido distinto | Nuevo | Introducción reutilizada | Repaso-only reutilizado |

|---|---:|---:|---:|---:|---:|---:|

| A1 | 900 | 0 | 11 | 889 | 75 | 6 |

| A2 | 871 | 0 | 75 | 796 | 73 | 6 |

| B1 | 809 | 0 | 113 | 696 | 68 | 6 |

| B2 | 726 | 0 | 128 | 598 | 61 | 6 |

| **Total** | **3306** | **0** | **327** | **2979** | **277** | **24** |



Variantes por nivel: A1 11, A2 75, B1 113, B2 128. De ellas, 304 son repeticiones del encabezado entre niveles con categorías disjuntas (A2 68, B1 110, B2 126); se conserva cada categoría como unidad diferente. Las otras 23 son candidatas frente a los catálogos heredados.

- En la comparación heredada: 19 candidatos con el mismo encabezado (18 de categoría diferente; `March` mes frente a `march` acción), un componente (`phone`) dentro de la expresión completa `phone number` y tres relaciones léxicas no flexivas (`sometimes`/`sometime`, `spelling`/`spell`, `shooting`/`shoot`). Ninguno autoriza fusionar unidades.

- Encabezados repetidos dentro del Oxford 3000: 304 filas posteriores a su primera aparición, sin ningún par con la misma categoría gramatical; por tanto, se marcan como variante/sentido distinto, no como una repetición que se enseñe dos veces.

- Equivalencias de unidad completa + categoría/sentido para deduplicar: 0. La evidencia por fila está en `evidencia_cotejo`.

- El informe loop10 informó 22 solapamientos parciales. El cotejo v11 registra 23 candidatos heredados y 304 repeticiones internas con categorías distintas; el subtotal 22 no se reproduce.



## Calendario y sesiones



| Nivel | Heredadas loop9 | Introducciones Oxford reutilizadas | Repaso final reutilizado | Total en v11 | Orden global |

|---|---:|---:|---:|---:|---|

| A1 | 26 | 75 | 6 | 107 | 1–107 |

| A2 | 19 | 73 | 6 | 98 | 108–205 |

| B1 | 20 | 68 | 6 | 94 | 206–299 |

| B2 | 71 | 61 | 6 | 138 | 300–437 |

| C1 | 117 | 0 | 0 | 117 | 438–554 |

| C2 | 12 | 0 | 0 | 12 | 555–566 |

| **Total** | **265** | **277** | **24** | **566** | **1–566** |



El mínimo de cohortes es `ceil(unidades del nivel / 12)`: A1 `ceil(900/12)=75`; A2 `ceil(871/12)=73`; B1 `ceil(809/12)=68`; B2 `ceil(726/12)=61`. La última cohorte es parcial en A2, B1 y B2. Seis sesiones de cierre por nivel cubren +1/+3/+6 de la cohorte final; las anteriores se repasan en sesiones posteriores del mismo nivel.



## Cobertura de intervalos y destinos



- 3.306/3.306 filas conservadas con sesión de foco y tres destinos; no hay destinos vacíos.

- Oxford 3000: 3.306 × 3 = **9.918 eventos**. Línea base: 3.012 unidades únicas × 3 = **9.036 eventos**. Total completo: **18.954** eventos, con destinos distintos, posteriores y existentes. Los repasos heredados desplazados a sesiones Oxford se incorporan a su carga y texto de repaso.

- Se reutilizan 301 IDs de sesión de `10_loop`; nuevas sesiones agregadas: **0**.



## Pares y carga oral: cálculo reproducible



| Componente de las sesiones Oxford | Cálculo | Pares |

|---|---:|---:|

| Introducción | 3.306 × 5 | 16.530 |

| Repaso en las sesiones Oxford | 9.918 Oxford 3000 + 414 heredados | 10,332 |

| Gramática | 301 × 30 | 9.030 |

| Integración acumulativa | residuo hasta 150/sesión | 9,258 |

| **Total** | **301 × 150** | **45.150** |



Modelo oral medio por par: pronunciación + reconocimiento/avance + promedio de 20 % de reintentos; se suman dos pausas de tres minutos por sesión (tres bloques de 50). La duración es estimada, no medida.



| Nivel | Sesiones Oxford | Centro por sesión | Rango con pausas | Oxford central | Oxford rango |

|---|---:|---:|---:|---:|---:|

| A1 | 81 | 26.0 min | 21.0–36.0 min | 35.10 h | 28.35–48.60 h |

| A2 | 79 | 28.5 min | 21.0–38.5 min | 37.52 h | 27.65–50.69 h |

| B1 | 74 | 31.0 min | 21.0–41.0 min | 38.23 h | 25.90–50.57 h |

| B2 | 67 | 36.0 min | 21.0–46.0 min | 40.20 h | 23.45–51.37 h |

| **Oxford A1–B2** | **301** | — | — | **151.06 h** | **105.35–201.22 h** |



**Suficiencia antes/después.** Antes: 265 × 150 = **39.750** pares de capacidad. Después: 566 × 150 = **84.900**; incremento 45.150. No se atribuye capacidad libre a las sesiones heredadas: las 301 sesiones de integración ya existentes se reutilizan y cada una respeta 150 pares. El incremento es suficiente por el máximo de cohorte, tres intervalos y carga oral estimada. Las 301 sesiones Oxford suman ≈151.1 h centrales y 105.3–201.2 h de rango. Para las 566 sesiones del programa completo, la estimación central es 307.6 h (rango 204.0–401.9 h). En la programación completa, los 84.900 pares se distribuyen en 31.590 de introducción, 18.954 de repaso espaciado, 16.980 gramaticales y 17.376 de integración. El máximo usado antes de integración es 126 pares por sesión (12 unidades × 5 + 36 eventos + 30 gramática). Se recomienda dividir cada sesión en tres bloques de 50 y pausar/reintentar sin superar el límite de generación.



## Criterio de naturalidad contextual



- Cada fila Oxford 3000 tiene `contexto_oral_sugerido` con escena CEFR y orientación ligada a su categoría. Las entradas heterogéneas por orden alfabético usan microescenas independientes.

- Sustantivos: referente, artículo/contabilidad y colocación plausibles; verbos: marco, complemento y preposición naturales; adjetivos: referente compatible; función/conectores: relación en frase completa; categorías múltiples: bloques de pares separados.

- Para los CSV futuros: cinco pares hablables por unidad; cada frase completa y autónoma; traducción española idiomática; colocación plausible; sin etiqueta/código como texto pronunciable.



## Archivos



- `1_plan_estudio_por_sesiones_de_repeticion.md`: orden global, sesiones por nivel y carga oral.

- `2_catalogo_trazabilidad_fuentes.csv`: 6.319 filas preservadas (3.013 heredadas + 3.306 Oxford 3000).

- `3_sesiones_oxford3000_integradas.csv`: 301 sesiones, orden CEFR, pares, cohortes y estimaciones.

- Esta matriz resume trazabilidad/capacidad; no es una revisión independiente ni declara completitud.
