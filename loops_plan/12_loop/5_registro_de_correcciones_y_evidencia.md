# Registro de correcciones y evidencia -- iteración 12

Este registro aplica los hallazgos de `loops_plan/11_loop/5_informe_revision.md`; no constituye una revisión independiente ni declara completa la iteración.

## Hallazgos aplicados

- **Capitalización (26 casos):** las formas visibles en el PDF se restauran en `entrada_normalizada`; `entrada_fuente_raw_pypdf` permanece literal. La clave de comparación `clave_comparacion_casefold` está separada y no reemplaza los campos fuente o legibles. Las asignaciones, IDs canónicos, niveles y estados de deduplicación no cambian. Las cajas y formas se comprobaron visualmente en la evidencia PDF.

- **Localizadores no reproducibles por línea extraída:** página + `elemento_pdf_estable` + `bbox_pdf_puntos` pasa a ser la referencia primaria para las 3.306 entradas O3K. Se conservan las líneas anteriores solo como información auxiliar. Cada localizador incluye el SHA-256 de la fuente.

## Evidencia de capitalización y asignación

| Registro | Forma fuente verificada | Forma legible restaurada | Página | Caja PDF (pt: x0,y0,x1,y1) | Elemento estable | Sesión conservada |
|---|---|---|---:|---|---|---|
| `O3K-A1-P01-L134` | `CD n.` | `CD n.` | 1 | `303.64,215.96,322.98,226.77` | `O3K-P01-E0129` | `A1-S037` |
| `O3K-A1-P01-L041` | `April n.` | `April n.` | 1 | `42.52,528.70,68.64,539.52` | `O3K-P01-E0036` | `A1-S029` |
| `O3K-A1-P01-L052` | `August n.` | `August n.` | 1 | `42.52,645.52,77.80,656.34` | `O3K-P01-E0047` | `A1-S030` |
| `O3K-A1-P01-L197` | `December n.` | `December n.` | 1 | `434.20,237.20,481.91,248.01` | `O3K-P01-E0192` | `A1-S042` |
| `O3K-A1-P01-L229` | `DVD n.` | `DVD n.` | 1 | `434.20,577.04,459.41,587.85` | `O3K-P01-E0224` | `A1-S045` |
| `O3K-A1-P02-L143` | `I pron.` | `I pron.` | 2 | `173.08,773.48,194.94,784.30` | `O3K-P02-E0140` | `A1-S058` |
| `O3K-A1-P02-L165` | `January n.` | `January n.` | 2 | `303.64,263.72,341.36,274.54` | `O3K-P02-E0162` | `A1-S060` |
| `O3K-A1-P02-L171` | `July n.` | `July n.` | 2 | `303.64,327.44,326.60,338.26` | `O3K-P02-E0168` | `A1-S061` |
| `O3K-A1-P02-L172` | `June n.` | `June n.` | 2 | `303.64,338.06,329.75,348.88` | `O3K-P02-E0169` | `A1-S061` |
| `O3K-A1-P02-L035` | `February n.` | `February n.` | 2 | `42.52,369.92,84.62,380.74` | `O3K-P02-E0032` | `A1-S049` |
| `O3K-A1-P02-L070` | `Friday n.` | `Friday n.` | 2 | `42.52,741.62,73.63,752.44` | `O3K-P02-E0067` | `A1-S052` |
| `O3K-A1-P02-L221` | `March n.` | `March n.` | 2 | `434.20,115.04,466.00,125.86` | `O3K-P02-E0217` | `A1-S065` |
| `O3K-A1-P02-L225` | `May n.` | `May n.` | 2 | `434.20,157.52,458.17,168.34` | `O3K-P02-E0221` | `A1-S065` |
| `O3K-A1-P02-L248` | `Monday n.` | `Monday n.` | 2 | `434.20,401.78,473.35,412.60` | `O3K-P02-E0244` | `A1-S067` |
| `O3K-A1-P03-L158` | `September n.` | `September n.` | 3 | `303.64,189.38,353.81,200.20` | `O3K-P03-E0154` | `A1-S083` |
| `O3K-A1-P03-L144` | `Saturday n.` | `Saturday n.` | 3 | `303.64,40.70,345.18,51.52` | `O3K-P03-E0141` | `A1-S082` |
| `O3K-A1-P03-L011` | `November n.` | `November n.` | 3 | `42.52,115.04,90.71,125.86` | `O3K-P03-E0008` | `A1-S071` |
| `O3K-A1-P03-L017` | `October n.` | `October n.` | 3 | `42.52,178.76,81.95,189.58` | `O3K-P03-E0014` | `A1-S071` |
| `O3K-A1-P03-L023` | `OK exclam., adj./adv.` | `OK exclam., adj./adv.` | 3 | `42.52,242.48,114.30,253.30` | `O3K-P03-E0020` | `A1-S072` |
| `O3K-A1-P03-L230` | `Sunday n.` | `Sunday n.` | 3 | `434.20,210.62,470.41,221.44` | `O3K-P03-E0226` | `A1-S089` |
| `O3K-A1-P03-L275` | `Thursday n.` | `Thursday n.` | 3 | `434.20,688.52,477.20,699.34` | `O3K-P03-E0271` | `A1-S092` |
| `O3K-A1-P04-L020` | `T-shirt n.` | `T-shirt n.` | 4 | `42.52,210.62,74.57,221.44` | `O3K-P04-E0017` | `A1-S095` |
| `O3K-A1-P04-L021` | `Tuesday n.` | `Tuesday n.` | 4 | `42.52,221.24,81.41,232.06` | `O3K-P04-E0018` | `A1-S095` |
| `O3K-A1-P04-L023` | `TV n.` | `TV n.` | 4 | `42.52,242.48,60.60,253.30` | `O3K-P04-E0020` | `A1-S095` |
| `O3K-A1-P04-L063` | `Wednesday n.` | `Wednesday n.` | 4 | `42.52,667.28,94.68,678.10` | `O3K-P04-E0060` | `A1-S098` |
| `O3K-B1-P08-L240` | `IT n.` | `IT n.` | 8 | `434.20,316.82,449.09,327.64` | `O3K-P08-E0237` | `B1-S052` |

La comprobación visual individual de las 26 entradas se conserva en `7_evidencia_visual_capitalizacion.pdf` (dos hojas de recortes); hash PDF de origen: `a1ccae422ddda0011e4783ce60a1d67c05a276a806dd07c2d3d887f4d97c5a8c`.

## Preservación de inventario y sesiones

- Filas del catálogo conservadas: **6.319**; entradas O3K: **3.306**.
- Distribución O3K conservada: **A1 900, A2 871, B1 809, B2 726**.
- Sesiones de integración conservadas: **301**; unidades nuevas: **3.306**; carga, pares, repasos y tiempos se heredan sin cambios.
- Sesiones base: **265**; programa total: **566**.
- Se preservan los campos de niveles, asignación, estado, `id_unidad_canonica`, `codigo_unidad_intro`, origen de duplicación, repasos +1/+3/+6, orden y focos.
- Se cotejó que cada registro del catálogo conserva una asignación cuyo ID corresponde a una sesión del plan base o del CSV de sesiones Oxford; el programa no crea ni reasigna sesiones.

Para reproducir el cotejo y los localizadores, consultar `6_metodo_cotejo_y_localizadores.md`. Esta actualización no añade una declaración de aprobación o cierre.
