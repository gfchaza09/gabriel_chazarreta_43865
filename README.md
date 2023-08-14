# Proyecto Final Python Coderhouse

## Descripción

Este proyecto es parte de la tercera presentación de mi curso y se enfoca en el desarrollo de un sitio web para gestionar videojuegos, consolas, accesorios y reseñas relacionadas. Es la culminación de aquel proyecto que inicie como tercera presentación, el sitio web "El Rincon del Gamer", como lo titulé es el proyecto final del curso de Python de Coderhouse.

## Funcionalidades

El sitio web permite a los usuarios:

- Registrar y autenticarse en el sistema. El usuario tiene un campo opcional para agregar un avatar, en caso de no subir ninguno se utilizará una imagen por defecto desde la carpeta static/assets.
- Agregar, editar y eliminar videojuegos, consolas y accesorios.
- Dejar reseñas en los elementos (videojuegos, consolas, accesorios).
- Realizar búsquedas de elementos por nombre.
- Acceder a la página "Acerca de mí" para conocer más sobre el desarrollador. El acceso a la página se encuentra en el footer del sitio web.

Se utilizaron 4 modelos principales para la creación del proyecto los cuales son:

1. Videojuego: Este modelo representa la información de un videojuego, incluyendo su título, género, desarrollador y año de lanzamiento. Además, se establece una relación con el modelo de Reseña para permitir que los usuarios dejen comentarios sobre los videojuegos.

2. Consola: Este modelo almacena los detalles de una consola, como su nombre, fabricante y año de lanzamiento. Al igual que en el modelo de Videojuego, se establece una relación con el modelo de Reseña para que los usuarios puedan dejar comentarios sobre las consolas.

3. Accesorio: Este modelo guarda información sobre un accesorio, incluyendo su nombre y tipo. Nuevamente, se crea una relación con el modelo de Reseña para permitir comentarios de los usuarios.

4. Review (Reseña): Este modelo almacena las reseñas dejadas por los usuarios en los videojuegos, consolas y accesorios. Cada reseña incluye la calificación, el comentario, la fecha de creación y la relación con el usuario que la dejó y el elemento sobre el que se hizo la reseña.

## Credenciales de Administrador

- Usuario: gabriel
- Contraseña: 123456

## Tecnologías Utilizadas

- Django (versión 4.2.3)
- HTML5, CSS3
- Font Awesome (versión 5.8.2)

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta las migraciones con `python manage.py migrate`.
4. Crea un superusuario administrador con `python manage.py createsuperuser`.
5. Inicia el servidor con `python manage.py runserver`.

## Casos de Test Unitarios

El proyecto incluye un archivo Excel llamado `pruebas_proyecto_python_chazarreta.xls` que contiene 10 casos de pruebas unitarias relevantes. Estos casos han sido diseñados para verificar el funcionamiento correcto de las principales funcionalidades del proyecto.

## Video de Funcionamiento

También se ha preparado un video de demostración que muestra el funcionamiento del sitio web, el cual se encuentra en el repositorio: `proyecto_final_chazarreta.webm`

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

- Nombre: Gabriel Chazarreta
- Email: gfchazarreta@gmail.com
- LinkedIn: https://www.linkedin.com/in/gabriel-chazarreta/