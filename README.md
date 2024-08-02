# FiTargetTool

FiTargetTool es una herramienta para administrar una serie de clientes, donde de cada uno podremos ir administrando su progreso en los pesos de levantamiento y su peso, además de la rutina que este posee. También podremos crear nuestras rutinas personalizadas.

## Arquitectura MVC

El proyecto FiTargetTool posee una arquitectura MVC (Model, View, Controler) donde separamos por capas el código del mismo. En el modelo encontramos las clases que usamos para modelar los datos extraídos de la Base de Datos, usamos SQLite.

#### Diagrama UML

<img src="./docs/UML FiTargetTool.png" width="800"/>

## Documentación del Código

En la capa Controler encontraremos los scrips necesarios para la: optención, actualización y eliminación de la información de la Base de Datos.

### Controler.py

- **get_rutine(id)**: Función que se encargará de obtener una rutina según su id.
- **get_progress(id)**: Función que se encargará de obtener un progrso según su id.
- **get_pesos(id)**: Función que se encargará de obtener una lista de pesos según su id.
- **get_client(name)**: Función que se encargará de obtener un cliente según su nombre.
- **get_list_names():** Función que se encargará de obtener una lista de nombres de todos los clientes.
- **get_all_data():** Función que se encargará de obtener toda la lista de clientes.
- **get_list_id_rutines():** Función que se encargará de obtener una la lista de los id de las rutinas.

### Create.py

