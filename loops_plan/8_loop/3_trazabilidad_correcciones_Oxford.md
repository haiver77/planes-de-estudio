# Trazabilidad de correcciones — Iteración 8

## Alcance

Se parte de los artefactos de `7_loop` y se escribe solo en `8_loop`. Se aplican los dos hallazgos concretos de `7_loop/4_informe_revision.md`. No se modifica el informe original ni ninguna iteracion anterior. No se declara completitud.

## Evidencia del PDF y correccion de registros

Cotejo del texto extraido de `resources/Oxford Phrase List.pdf`, pagina 3, con PyPDF:

| Líneas | Texto contiguo en el PDF | Registro corregido | Nivel / sesión; ID canónico / local |
|---|---|---|---|
| 25–26 | `They say you can’t buy ` + `happiness.` | `They say you can’t buy happiness.` — `OPL-A2-P03-L025-026` | A2 / A2-S019; `LEX-00520` / `A2-S019-U01` |
| 46–47 | `I had a kind of feeling this ` + `might happen.` | `I had a kind of feeling this might happen.` — `OPL-B1-P03-L046-047` | B1 / B1-S001; `LEX-00539` / `B1-S001-U10` |

Cada registro combina el intervalo completo en inicio/fin de linea y mantiene ambas lineas como texto crudo unido y normalizado. Los cuatro registros de fragmento se sustituyen por dos registros sin perder ninguna linea. `happiness.` y `might happen.` ya no tienen unidad ni asignacion independientes.

## Conteos antes/despues

| Nivel | Registros antes | Unidades antes | Registros despues | Unidades despues |
|---|---:|---:|---:|---:|
| A1 | 303 | 303 | 303 | 303 |
| A2 | 228 | 227 | 227 | 226 |
| B1 | 233 | 233 | 232 | 232 |
| B2 | 848 | 848 | 848 | 848 |
| C1 | 1403 | 1403 | 1403 | 1403 |
| **Total** | **3015** | **3014** | **3013** | **3012** |

Phrase List: 1001 registros / 1000 unidades únicas antes; 999 / 998 después. Oxford 5000 permanece en 2014 registros/unidades. Se conserva un duplicado exacto preexistente. El prefacio editorial “750 common phrases” no se reconcilia con el total extraído; el conteo actualizado se refiere a entradas completas del catálogo.

## IDs y asignaciones a sesiones existentes

- IDs canónicos reasignados de manera consecutiva por orden de primera introducción: `LEX-00001` a `LEX-03012`. El duplicado apunta al ID/código de introducción original y no crea unidad nueva.
- A2-S019 baja de 11 a 10 unidades (`U01-U10`). La frase compuesta ocupa U01; las restantes conservan su orden.
- B1-S001 baja de 12 a 11 unidades (`U01-U11`). La frase compuesta ocupa U10 y la entrada que seguia en U12 queda como U11.
- Se comprobó que cada nueva fila pertenece a la misma sesión y nivel que sus líneas origen, y que los destinos de repaso existentes siguen siendo válidos en el plan: frase A2 → B1-S001, B1-S003, B1-S006 (+1/+3/+6); frase B1 → B1-S002, B1-S004, B1-S007 (+1/+3/+6). No se movieron sesiones; solo baja en uno el tamaño de cada cohorte afectada.

## Reparto recalculado de pares

Regla aplicada: 5 pares por unidad nueva + 1 por evento de repaso de vocabulario + 30 gramaticales + integración hasta 150.

| Sesión | Unidades nuevas | Repasos | Gramática | Integración | Total |
|---|---:|---:|---:|---:|---:|
| A2-S019 | 10 (50 pares) | 36 | 30 | 34 | 150 |
| B1-S001 | 11 (55 pares) | 34 | 30 | 31 | 150 |
| B1-S002 | 12 (60 pares) | 35 | 30 | 25 | 150 |
| B1-S003 | 12 (60 pares) | 34 | 30 | 26 | 150 |
| B1-S004 | 12 (60 pares) | 35 | 30 | 25 | 150 |
| B1-S006 | 12 (60 pares) | 34 | 30 | 26 | 150 |
| B1-S007 | 12 (60 pares) | 35 | 30 | 25 | 150 |

C2 no cambia: los repasos gramaticales siguen en sesiones distintas y con los intervalos de la matriz ICOG de la iteración 7.
