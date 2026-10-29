# Informe de auditoría — `loops_plan_for_phrases/4_loop`

**Resultado: requiere otra iteración.** El manifiesto de la fuente es íntegro y el plan contiene varios controles CSV pertinentes, pero hay brechas de propiedad efectiva, agrupación pedagógica, carga por sesión y repetición espaciada. Además, no existen CSV en esta iteración que permitan verificar los objetivos en su uso real.

## Comprobaciones satisfactorias

- `resources/Phrase List.txt` contiene 750 entradas: A1 129, A2 379, B1 155, B2 57 y C1 30; no hay entradas C2. Su SHA-256 es `1372473C7CD5CBD6A6A6FA30A7ACC63723562FDFA4D182362BC25B31987C8756`, igual al declarado en el plan.
- El manifiesto tiene 750 filas. Los IDs siguen el orden y nivel de la fuente; las 750 formas cotejan con las expresiones de origen tras normalizar Unicode, mayúsculas/minúsculas y espacios, y sus 750 hashes normalizados coinciden. No hay IDs ni expresiones duplicados.
- La tabla asigna una sola fila de propietario/destino a cada ID. La lista de vocabulario foco de las 87 sesiones complementarias contiene 740 objetivos distintos, sin duplicados internos; los otros 10 registros aparecen como propiedad general. Los recuentos por nivel de entradas y sesiones también suman correctamente.
- La fuente contiene una sola entrada `all over the world` y el manifiesto la asigna una vez, a `PF-B1-018`. El plan general conserva C2-S01–C2-S06 y el complemento no inventa unidades C2.
- El contrato futuro recoge UTF-8, dos columnas español;inglés, `;`, ausencia de encabezado, resolución de marcadores, equivalencia de sentido y control de pronombres/sujetos. Son especificaciones, no comprobaciones de CSV generado.

## Observaciones priorizadas

### 1. Organizar y limpiar el plan
- **Cambio requerido:** Manten el plan puntual. El objetivo es que estén claramente definas las sesiones de las que se compondrá el plan, que cada sesión maneje una cantidad apropiada de frases nuevas (no menos de 8  no más de 20) y tener claridad de qué frases están incluidas en cada sesion.


### 2. no se necesita repaso ni repetición.


**Siguiente paso:** corregir
