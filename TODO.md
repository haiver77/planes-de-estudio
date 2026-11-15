# Contexto de interface gráfica para funcionalidad de cursos en la aplicación.


## Definiciones:
 - `pantalla cursos`: Pantalla que presenta la lista de cursos disponibles, en cada curso se visualiza el nombre del curso, la cantidad de `vocabulario foco` y la cantidad de `vocabulario complementario`del curso. Si hay un curso actualmente selecconado, se muestra al principio, con alguna marca o tag de 'Current'. Si hay progreso registrado para el curso, se visualiza en una barra de progreso. También cada curso contiene un botón de "Select", si el usuario lo marca y no tiene registrado ningún progreso anterior para el curso, entonces se selecciona la primera unidad del curso, si tiene progreso, entonces se selecciona la última unidad que registra algún progreso.
 - `pantalla detalles de curso`: Pantalla que presenta los detalles de un curso, se muestra el título de curso, una breve descripción en la parte superior y luego una lista de unidades. La lista de unidades también son cajas verticales donde está el nombre de la unidad, descripción, cantidad de `vocabulario foco`, cantidad de `vocabulario complementario` y progreso de la unidad. También tiene un botón "Select", que en caso de ser seleccionado, el sistema registra que es la unidad seleccionada actual para el usuario.

 ## Navegación
 
Crea prototipos de navegación que puedan soportar la siguiente nueva funcionalidad que quiero implementar en esta aplicación:

* Adicional a las opciones actuales que están disponible en la pantalla "Load Phrases" (Prompt, Load from file, Predefined Sets), existirá una opción adicional llamada "Cursos".
* Cuando el usuario ingresa a esa opción de "Cursos" el sistema mostrará la Pantalla "Cursos".
La pantalla "Cursos" tiene una lista de cursos, donde se muestran los cursos en cajas horizontales, donde cada caja contiene el nombre del curso, una descripción breve del curso, la cantidad de vocabulario foco y cantidad de vocabulario complementario.
* Estando en la pantalla "Cursos"
* Cuando el usuario da click en un curso, el objetivo es que el sistema lo lleve a una nueva "pantalla principal de detalles del curso" con los detalles del curso.
* Pantalla "pantalla principal de detalles del curso" mostrará el título de curso, una breve descripción en la parte superior y luego una lista de unidades.