# ClassManager

ClassManager es una aplicación web desarrollada en Django que facilita la gestión de información de profesores, alumnos, materias y horarios. Proporciona una interfaz intuitiva y funcionalidades robustas para administrar y organizar eficientemente los datos relacionados con la gestión académica.

## Características principales

- Gestión de profesores: Agrega, edita y elimina información de profesores, incluyendo su nombre, correo electrónico, especialidad, etc.
- Gestión de alumnos: Administra datos de alumnos, como nombres, apellidos, número de matrícula, etc.
- Gestión de materias: Permite el registro y mantenimiento de información sobre las materias ofrecidas, como nombre, código, descripción, etc.
- Gestión de horarios: Organiza y visualiza los horarios de clases para un mejor seguimiento y organización.

## Requisitos de instalación

Asegúrate de tener los siguientes requisitos previos antes de instalar y ejecutar el proyecto:

- Python 3.x: https://www.python.org/downloads/
- Django: Instalable a través de pip, puedes ejecutar `pip install Django` en tu entorno virtual.

### Como instalar django
Fuera del repositorio del proyecto crear una máquina virtual.
` -py -m venv venv`

Puedes remplazar el último venv con el nombre que deseas agregar a la máquina virtual.
Luego ingresar a la carpeta venv, Scripts y ejecutar el siguiente comando
`activate`

Esto te indicará que estas dentro de la máquina virtual.
Luego volver a la carpeta raíz de este proyecto e instalar django con el siguiente comando:
`pip install Django`



## Instalación y configuración

1. Clona este repositorio en tu máquina local utilizando el siguiente comando:
`git clone https://github.com/tu_usuario/ClassManager.git`

2. Accede al directorio del proyecto:
`cd ClassManager`

3. Instala las dependencias necesarias:
`pip install -r requirements.txt`

4. Realiza las migraciones de la base de datos:
`python manage.py migrate`

5. Inicia el servidor de desarrollo:
`python manage.py runserver`


7. Abre tu navegador web y accede a `http://localhost:8000` para ver la aplicación en funcionamiento.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar en el desarrollo de ClassManager, asegúrate de seguir los pasos:

1. Crea un fork de este repositorio.
2. Crea una rama para tu función o corrección de error: `git checkout -b nombre-de-la-rama`.
3. Realiza los cambios y realiza confirmaciones significativas.
4. Envía tus cambios al repositorio remoto: `git push origin nombre-de-la-rama`.
5. Envía una solicitud de extracción (Pull Request) describiendo los cambios realizados.

## Contacto

Si tienes alguna pregunta, sugerencia o problema relacionado con ClassManager, no dudes en contactarnos a través de la sección de "Issues" de este repositorio.

Esperamos que disfrutes utilizando ClassManager y que sea de gran utilidad para la gestión académica en tu institución.

¡Gracias por usar ClassManager!





