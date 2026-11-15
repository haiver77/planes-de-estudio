# course_vocabulary más completo

Modificar la lógica de los agentes "curso_ll_*" para que considere las siguientes actualizaciones:
que al finalizar al creación del curso, cuando se crean los archivos:
- course_vocabulary_focus_by_unit.csv
- course_vocabulary_complementary_by_unit.csv

Tengan las siguientes carácteristicas:
    - course_vocabulary_focus_by_unit.csv, tendrá 4 columnas:
        - Unit Number: Número de la unidad
        - Unit Title: El título de la unidad (Campo title del json de unit_details.json).
        - Category: La categoría de la unidad si existe, caso contrario quedará vacio.
        - chunk: Vocabulario foco (Palabra o frase del vocabulario foco)
        - native: Traducción en el lenguage nativo.
    - course_vocabulary_complementary_by_unit.csv, tendrá 2 columnas:
        - Unit: El nombre de la unidad (Unit_1, Unit_2, Unit_*).
        - Word: vocabulario supplementario usado para completar las oraciones que no hace parte del vocabulario foco.




