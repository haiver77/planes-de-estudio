# Informe de auditoría lingüística y técnica — A1-S001 a A1-S005

**Iteración revisada:** 26  
**Mínimo exigido:** 150 pares por CSV  
**Plan:** `loops_plan/11_loop/1_plan_estudio_por_sesiones_de_repeticion.md`  
**Catálogo:** `loops_plan/11_loop/2_catalogo_trazabilidad_fuentes.csv`  
**Alcance:** solo `loops_csv/26_loop/A1/A1-S001.csv` a `A1-S005.csv`. No se modificó ningún CSV.

## Evidencia de las comprobaciones

- **Cobertura:** el directorio contiene exactamente los cinco CSV esperados; no faltan IDs ni hay archivos ajenos. El plan contiene las cinco sesiones y el catálogo asigna 12 códigos de unidad únicos a cada sesión.
- **Cantidad y bloques:** cada archivo tiene 150 registros. En cada uno, las filas 1–60 corresponden a 12 unidades nuevas, cinco pares por unidad; las filas y cantidades restantes coinciden con la estructura del plan:

  | Sesión | Nuevas | Repaso | Gramática | Integración |
  |---|---:|---:|---:|---:|
  | A1-S001 | 60 | 0 | 30 | 60 |
  | A1-S002 | 60 | 12 | 30 | 48 |
  | A1-S003 | 60 | 12 | 30 | 48 |
  | A1-S004 | 60 | 24 (12 + 12) | 30 | 36 |
  | A1-S005 | 60 | 24 (12 + 12) | 30 | 36 |

- **Validación programática desde bytes:** los cinco archivos decodifican con UTF-8 estricto, sin BOM; cada uno tiene 150 líneas físicas y 150 registros CSV estrictos, dos campos por registro, sin encabezado, campos vacíos, filas vacías, campos adicionales, punto y coma dentro de campos ni saltos de línea incrustados. No se hallaron comillas mal formadas, U+FFFD ni los marcadores `Ã¡`/`Ã±`. Las preguntas españolas detectadas tienen `¿` de apertura; los `?` de cierre están presentes. Las comas detectadas están dentro de frases, no se usan como delimitador.
- **Duplicados:** en los 750 pares no hay pares repetidos ni frases españolas o inglesas duplicadas.
- **Cotejo de contenido:** se revisaron las 12 unidades nuevas de cada sesión y los bloques de repaso previstos (12/12 por evento), además de los 30 pares gramaticales y los pares de integración. Los objetivos gramaticales coinciden con G01–G05 del plan; no se detecta adelanto de los objetivos posteriores.
- **Revalidación de observaciones anteriores:**
  - **A1-S002, fila 49:** `El corte de electricidad dura un corto periodo de tiempo durante la tormenta.;The power cut lasts for a short period of time during the storm.` La corrección es natural, equivalente y conserva el vocabulario objetivo.
  - **A1-S005, fila 23:** `Antes de la clase, la profesora entra en el aula donde estoy.;Before the lesson, the teacher comes into the classroom where I am.` La corrección elimina la repetición y conserva el sentido y el objetivo `come into`.
  - **A1-S003, fila 105:** `Tú llegas a la escuela el fin de semana para jugar un partido de fútbol.;You arrive at school at the weekend to play in a football match.` El motivo hace verosímil la llegada en fin de semana y se conserva en ambos idiomas.

## Observaciones pendientes — requieren otra iteración

### Prioridad media

1. **A1-S005.csv, fila 19 — equivalencia incompleta y ambigüedad temporal.**  
   `Estoy en la cocina cuando mi hermano llega del trabajo y entra para cenar.;My brother comes into the kitchen while I am there after work.` La traducción omite que el hermano llega del trabajo y entra para cenar; además, `after work` puede interpretarse como referido a quien habla. **Cambio requerido:** restituir claramente ambos detalles, por ejemplo: `I am in the kitchen when my brother gets home from work and comes in for dinner.`

### Prioridad baja

2. **A1-S005.csv, fila 18 — detalle de situación omitido.**  
   `Estoy dentro de la tienda cuando los clientes entran por la puerta principal.;Customers come into the shop while I am inside.` La versión inglesa no conserva que los clientes entran por la puerta principal. **Cambio requerido:** incorporar el punto de entrada, por ejemplo: `I am inside the shop when the customers come in through the main door.`

**Resultado:** permanecen dos observaciones lingüísticas accionables. Se requiere corregir las filas 19 y 18 de A1-S005.csv y repetir la auditoría.
