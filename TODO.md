# course_vocabulary más completo

Modificar la lógica de los agentes "curso_ll_*" para que considere las siguientes actualizaciones:
1. Agregar al archivo "unit_details.json" que se está generando por cada unidad:
    - El campo "id", el cual contendrá el id de la unidad en este formato: "Unit_1", "Unit_2", "Unit_3", "Unit_n" (n el número de unidad).
    - El campo "category" el cual contendrá el nombre de la categoría (si existe) que proviene del archivo fuente con el vocabulario que fue usado para la creación del curso.

2. hacer que al finalizar al creación del curso, cuando se crean los archivos:
- course_vocabulary_focus_by_unit.csv
- course_vocabulary_complementary_by_unit.csv

Dichos archivos tengan los siguientes ajustes:
    - course_vocabulary_focus_by_unit.csv, invierte las columnas actuales y agrega la traducción al idioma nativo al final para que quede de la siguiente manera:
        - unit: Número de la unidad
        - vocabulary_focus: Vocabulario foco (Palabra o frase del vocabulario foco)
        - native: Traducción al lenguage nativo.
    - course_vocabulary_complementary_by_unit.csv, invierte las columnas actuales y agrega la traducción al idioma nativo para que quede de la siguiente manera:
        - unit: Número de la unidad
        - vocabulary_complementary: vocabulario supplementario usado para completar las oraciones que no hace parte del vocabulario foco.
        - native: Traducción al lenguage nativo.