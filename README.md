 # Gestor de Clases en Django

Este es un proyecto de gestión de alumnos y otras funcionalidades construido con Django. Proporciona un sistema básico de CRUD (Crear, Leer, Actualizar, Eliminar) para alumnos y tendrá características adicionales para profesores, materias y notas en futuras versiones.

## Configuración del Entorno

Antes de comenzar, asegúrate de haber creado un entorno virtual y de haber instalado las dependencias del proyecto utilizando el archivo `requirements.txt`.

```bash
# Crear y activar el entorno virtual (ejemplo en Unix-like)
python3 -m venv venv
source venv/bin/activate

```

# Instalar las dependencias
```
pip install -r requirements.txt
```

# Ejecución del Proyecto
Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1. Asegúrate de tener activado tu entorno virtual:

```
source venv/bin/activate
```

2. Navega a la carpeta del proyecto
```
cd path/al/proyecto
```

3. Realiza las migraciones de la base de datos:
```
python manage.py migrate
```

4. Inicia el servidor de desarrollo:
```
python manage.py runserver
```

5. Abre tu navegador y visita http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

## Estructura de Carpetas

- `gestion_alumnos/`: Directorio principal de la aplicación Django.
  - `settings.py`: Configuración de la aplicación.
  - `urls.py`: Definición de las rutas (URLs) de la aplicación.
  - `models.py`: Definición de los modelos de la base de datos.
  - `views.py`: Definición de las vistas y controladores.
- `venv/`: Directorio del entorno virtual (ignorado por Git).
- `requirements.txt`: Lista de dependencias del proyecto.
- `manage.py`: Punto de entrada para comandos de gestión de Django.

## Estructura de la Aplicación `gestion_alumnos`

- `models.py`: Define los modelos de la base de datos, como Alumno, Profesor, Materia, Nota, etc.
- `views.py`: Define las vistas y controladores para gestionar las interacciones del usuario.
- `urls.py`: Define las rutas (URLs) y mapeos a las vistas.
- `templates/`: Carpeta para plantillas HTML utilizadas en las vistas.
- `static/`: Carpeta para archivos estáticos como CSS, JavaScript, imágenes, etc.

## Estructura de Archivos

- `requirements.txt`: Lista de dependencias del proyecto que se pueden instalar con `pip`.
- `README.md`: Documento principal que proporciona información general sobre el proyecto.
- `LICENSE`: Archivo que describe los términos de la licencia del proyecto.
- `STRUCTURE.md`: Este documento que describe la estructura del proyecto.


Contribuciones
¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, asegúrate de seguir las mejores prácticas y abrir un pull request con tus cambios.

Futuras Funcionalidades
Este proyecto está en constante desarrollo. Próximamente se agregarán las siguientes características:

CRUD de profesores.
Sistema de gestión de materias.
Registro y seguimiento de notas.
Funcionalidades adicionales.
¡Mantente atento a las actualizaciones!

Licencia
Este proyecto está bajo la Licencia XYZ. Consulta el archivo LICENSE para más información.