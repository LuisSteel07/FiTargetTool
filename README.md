# FiTargetTool
FiTargetTool es una herramienta para administrar una serie de clientes, donde de cada uno podremos ir administrando su progreso en los pesos de levantamiento y su peso, además de la rutina que este posee. También podremos crear nuestras rutinas personalizadas.

## Arquitectura MVC
El proyecto FiTargetTool posee una arquitectura MVC (Model, View, Controler) donde separamos por capas el código del mismo. En el modelo encontramos las clases que usamos para modelar los datos extraídos de la Base de Datos, usamos SQLite.

## Base de Datos

## Model
En la carpeta models, encontraremos todas las clases de cada tabla de la DB. Donde esto nos facilitara la manipulacion de los valores y objetos retornados para cada funcion.

| Clase      | Descripcion                                                                                                                                                   |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cliente    | Esta clase almacenara los datos de los clientes, con atributos: id, nombre, edad, rutina, progreso, pesos y foto para futura implementacion.                  |
| Dia        | Esta es una enumaracion que nos ayuda en la manipulacion de los dias para los demas modelos.                                                                  |
| Ejercicios | Esta clase usada para los ejercicios de las rutinas, posee: nombre del ejericio, lista de repeticiones y lista de pesos, estas dos listas deben de coincidir. |
| Peso       | Esta clase almacenara los pesos en forma de lista donde lo identificaremos con su id respectivo.                                                              |
| Progreso   | Esta clase tendra una lista de valores de PR (personal records) por cada grupo muscular.                                                                      |
| Rutina     | Esta clase tendra un nombre y almacenara por cada dia de la semana una lista de objetos de la clase Ejercicios.                                               |

## Funciones CRUD
Estas funciones se encuentran en la carpeta Controler, donde se podran apreciar archivos que contienen funciones para un destino determinado:

### Controler.py
Este archivo nos proporciona funciones que ayudaran a obtener u establecer valores de la DB.
Funciones como:

| Funcion             | Descripcion                                                                                                                                                                                            |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| get_rutine          | Esta funcion retornara un objeto de la clase Rutina, este tendra el id, el nombre de la rutina y luego para cada dia, su lista de ejercicios correspondientes.                                         |
| get_progress        | Esta extraera el progreso con un id en especifico y nos lo retornara en un objeto de la clase Progreso.                                                                                                |
| get_pesos           | Esta funcion retorna un objeto de la clase Peso, en donde almacena el id y lista de valores de los pesos almacenados.                                                                                  |
| get_client          | Esta funcion retorna un objeto de la clase Ciente, localizandolo con el nombre del mismo, estableciendo en ese objeto el id, nombre, edad, rutina y demas datos guardados acerca del usuario en la DB. |
| get_list_names      | Esta funcion nos retorna una lista de todos los nombres de los usuarios que estan en la DB.                                                                                                            |
| get_all_data        | Esta funcion nos retorna una lista con todos los clientes guardados en la base de datos.                                                                                                               |
| get_list_id_rutines | Esta funcion nos retornara una lista de todos los id de las rutinas almacenadas.                                                                                                                       |

### Delete.py
Esta archivo proporciona las funciones necesarias para eliminar cualquier dato en el momento propuesto, podemos encontrar funciones como:

| Funcion         | Descripcion                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------|
| delete_client   | Esta funcion elimina un cliente en espeifico.                                                   |
| delete_routine  | Esta funcion elimina una rutina en especifica.                                                  |
| delete_peso     | Esta funcion elimina un registro de pesos en especifico.                                        |
| delete_progress | Esta funcion elimina un registro de progresos en los pesos levantados por cada grupo muscular.  |

### Create.py
Este archivo proporciona las funciones necesarias para crear automaticamente un objeto y guardarlo en la DB, esto incluye convertirlo a un string en formato json para trabajar con ello.

| Funcion         | Descripcion                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------|
| create_client   | Esta funcion creara e insertara en la DB un nuevo objeto de la clase Cliente.                                   |
| create_pesos    | Esta funcion creara e insertara una lista con los registros de los pesos, teniendo en cuenta una lista inicial. |
| create_routine  | Esta funcion creara e insertara una nueva rutina con un nombre en espefifico.                                   |
| create_progress | Esta funcion creara e insertara un nuevo registro de progresos del cliente.                                     |

### Update.py
Este archivo proporciona funciones para actualizar los valores de cualquier campo requerido, en este tenemos funciones como:

| Funcion                 | Descripcion                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------|
| update_client           | Esta funcion actualiza los valores de un cliente en especifico.                               |
| update_rutina           | Esta funcion actualiza los valores de una rutina en especifico.                               |
| update_peso             | Esta funcion actualiza los valores de un registro de pesos.                                   |
| update_progress         | Esta funcion actualiza los valores de un registro de progresos de un cliente.                 |
| change_rutine           | Esta funcion cmabia cual sera la rutina de un cliente.                                        |
| update_client_data      | Esta funcion es similar a update_client, pero solo actualiza los campos de: nombre y edad.    |
| update_routine_full_day | Esta funcion actualiza la lista completa de ejercicios de un cliente en un dia en especifico. |
| update_full_routine     | Esta funcion actualiza los valores de una rutina a partir de otra.                            |

## Funciones Utils
En la carpeta Utils de podran encontrar archivos que proporcionen utilidades para funciones requeridas muy especificas.

| Funcion              | Descripcion                                                                                                                      |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| generate_models_json | Esta funcion crea un diccionario, compatible con la biblioteca JSON, en la misma se almacenan valores de la clase de ejercicios. |

## View
En la carpeta View encontraremos varias funciones que nos permitiran cargar determinados componentes o view completas para cada ruta del programa.

### AutoCompleteSuggestionData.py
En este archivo encontraremos funciones para el uso de los componentes "AutoCompleteSuggestion", los cuales son usados para tener ayuda a la hora de introducir valores y ir directo a los requeridos.

| Funcion                             | Descripcion                                                                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auto_complete_suggestion_data       | Esta funcion retorna un objeto de la clase AutoCompleteSuggestion, el cual contiene una lista de los posibles nombres de usuario que se pueden insertar para buscar. |
| auto_complete_suggestion_id_rutines | Esta funcion retorna un objeto de la clase AutoCompleteSuggestion, el cual contiene una lista de los posibles id de rutinas que se pueden insertar para buscar.      |

### ProgressGraphics.py
En este archivo estan las funciones que facilian el muestreo de los graficos de los registros de progresos de los clientes ingresados en la DB.

| Funcion                     | Descripcion                                                                                                                                           |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| open_graphic                | Esta funcion se encarga de cargar el grafico en un AlertDialog para poder ser visualizado.                                                            |
| show_graphic                | Esta funcion retorna el grafico totalmente construido.                                                                                                |
| create_linechartdata_points | Esta funcion crea la lista de valores que se van a ir viendo punto por punto.                                                                         |
| create_left_chart_axis      | Esta funcion retorna los elementos en la parte izquierda de la grafica.                                                                               |
| create_bottom_chart_axis    | Esta funcion retorna los elementos en la parte inferior de la grafica.                                                                                |
| collection_graphics_view    | Esta funcion muestra una seccion la cual muestra informacion de cada grupo muscular a traves de las graficas, ademas de poder editarlas directamente. |

### InfoClienteView.py
En este archivo se encontraran funciones las cual nos serviran para usar componentes para mostrar informacion de los clientes guardados en la DB.

| Funcion                  | Descripcion                                                                                                        |
|--------------------------|--------------------------------------------------------------------------------------------------------------------|
| info_cliente_view        | Funcion que retorna un componente el cual muestra el nombre y edad del cliente.                                    |
| create_datatable_clients | Funcion que crea una tabla donde muestra la informacion de los clientes.                                           |
| rows_table_clients       | Funcion que crea las filas de la tabla creada en la funcion "create_datatable_clients".                            |
| show_full_datatable      | Esta funcion muestra un AlertDialog, donde su contenido es la tabla retornada por la funcion "rows_table_clients". |

### EditData.py
Este archivo cuenta con funciones que ejecutan AlertDialogs los cuales ayudan a editar datos, ya sea de los clientes o de algun otro elemento.

| Funcion                       | Descripcion                                                                                                                                                                                                                                                                                   |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| alert_invalid_data            | Esta funcion retorna un AlertDialog el cual nos informa si se a insertado un valor invalido.                                                                                                                                                                                                  |
| create_client_view            | Esta funcion a traves de un componente AlertDialog, nos crea un usuario, donde se agregaran los primeros datos del mismo.                                                                                                                                                                     |
| list_edit_clients (en desuso) | Esta funcion nos retorna una lista detallada de informacion del cliente y formas para interactuar con esta informacion.                                                                                                                                                                       |
| add_peso                      | Esta funcion agrega un valor de peso a las estadisticas de un cliente.                                                                                                                                                                                                                        |
| add_progreso                  | Esta funcion agrega un valor de progreso a cada grupo muscular de un cliente.                                                                                                                                                                                                                 |
| create_routine_view           | Esta funcion crea una rutina.                                                                                                                                                                                                                                                                 |
| change_rutine_view            | Esta funcion cambia la rutina de un cliente por otra ya existente.                                                                                                                                                                                                                            |
| change_client_view            | Esta funcion nos permite modificar el nombre u edad de un cliente.                                                                                                                                                                                                                            |
| modify_rutine                 | Esta funcion, en conjunto con las siguientes, permiten la visualizacion y modificacion de los ejercicios de una rutina en forma de tabla.                                                                                                                                                     |
| list_textfields_rutine        | Esta funcion permite retornar una columna de la tabla dada en "modify_rutine", esta columna contiene el dia y luego los ejercicios de ese dia en forma de TextFields, osea que se pueden modificar ahi mismo, sino tiene ningun ejercicio ese dia, se agrega un texto unico diciendo "Vacio". |
| extract_routine_values        | Esta funcion extrae los valores de los TextFields de la tabla y los convierte en una instancia de la clase Rutina, donde ya en la funcion "modify_rutine" se hace uso de "update_full_routine" para actualizar la rutina por los nuevos valores.                                              |


