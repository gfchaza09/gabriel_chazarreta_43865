# Proyecto de Videojuegos - README
Este proyecto tiene como objetivo crear un sitio web para administrar videojuegos, consolas y accesorios. A continuación, se detalla el orden en el que se probaron las funcionalidades y dónde se encuentran las diferentes partes del proyecto.

## Orden de pruebas de funcionalidades
1- Se probaron las vistas principales para verificar que se muestran correctamente y que los enlaces a las diferentes secciones funcionan adecuadamente.

2- Se probó la vista de "Lista de Videojuegos" para asegurarse de que los videojuegos se muestran correctamente en una lista y que cada uno de ellos tiene un enlace a su respectivo detalle. Para las vistas "Consolas" y "Accesorios" se procedió de igual manera.

3- Se probó la vista de "Detalle de Videojuego" para verificar que muestra correctamente los detalles de un videojuego específico. Lo mismo para el "Detalle de Consola y Accesorio"

4- Se probó la funcionalidad de búsqueda para asegurarse de que devuelve los resultados correctos según el término de búsqueda ingresado.

5- Se probó que los enlaces de cada resultado de búsqueda llevan al detalle correcto, ya sea de videojuego, consola o accesorio.

6- Se probó que el formulario de agregar un nuevo videojuego, consola o accesorio funciona correctamente y que los datos se guardan adecuadamente en la base de datos.

7- Se aplicaron estilos CSS para mejorar la apariencia general del sitio web y se verificó que los estilos se aplican correctamente en todas las páginas.

## Estructura del proyecto
El proyecto está estructurado de la siguiente manera:

- **tercera_preentrega_app**: Contiene las vistas, modelos, formularios y archivos relacionados con la aplicación principal del proyecto.
- **tercera_preentrega_chazarreta**: Configuración del proyecto Django y la URL principal.
- **static/tercera_preentrega_app**: Carpeta que contiene archivos estáticos, como hojas de estilo CSS, imágenes y scripts de JavaScript.
- **templates/tercera_preentrega_app**: Contiene los archivos HTML de las diferentes vistas del proyecto.
- **db.sqlite3**: Base de datos SQLite que almacena la información de videojuegos, consolas y accesorios.

## Ejecutar el proyecto
Para ejecutar el proyecto, asegúrate de tener Python y Django instalados. Luego, sigue los siguientes pasos:

Clona este repositorio en tu computadora.

Abre una terminal y navega hasta la carpeta del proyecto.

Ejecuta el siguiente comando para aplicar las migraciones de la base de datos:

``python manage.py migrate``

Luego, crea un superusuario para acceder al panel de administración de Django:

``python manage.py createsuperuser``

Inicia el servidor de desarrollo de Django:

``python manage.py runserver``

Abre tu navegador web y visita http://localhost:8000 para acceder al sitio web. Para acceder al panel de administración, ve a http://localhost:8000/admin e inicia sesión con el superusuario que creaste en el paso anterior.