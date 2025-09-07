





### routes.py
Contendrá las rutas o endpoints de esta sección de la aplicación
* src/: Tu directorio de código fuente.
* main/: Un subdirectorio para agrupar la lógica principal o global. A medida que tu app crezca, podrías tener otros directorios aquí como users/ o products/.

Creamos una pieza de la aplicación (un Blueprint) que luego "enchufaremos" a la aplicación principal:

`main = Blueprint('main', __name__)`

La ruta ahora pertenece al Blueprint main:

`@main.route("/")`

Lógica de rutas y creación de la aplicación desacopladas. Este archivo es un componente reutilizable y organizado.

## config.py: El Panel de Ajustes ⚙️
Este archivo centraliza todas las variables de configuración de tu aplicación. Su propósito es separar los datos de configuración de la lógica del código.

¿Para qué sirve?

1. Seguridad: Guarda aquí información sensible como claves secretas (SECRET_KEY), contraseñas de bases de datos o credenciales de APIs. La buena práctica es cargar estos valores desde variables de entorno para no escribirlos directamente en el código.

2. Flexibilidad: Te permite crear diferentes configuraciones para distintos entornos. Por ejemplo, puedes usar una base de datos SQLite para desarrollo local y una PostgreSQL para producción, simplemente cambiando la configuración sin tocar una línea de la lógica de tu app.

3. Mantenimiento: Si necesitas cambiar una configuración, sabes exactamente a qué archivo ir, en lugar de buscarla por todo el código.

## run.py: La Llave de Arranque 🚀
Este es un script simple y limpio que se encuentra en la raíz de tu proyecto. Su única responsabilidad es crear una instancia de tu aplicación y ejecutarla.

¿Para qué sirve?

1. Punto de Entrada Claro: Sirve como el punto de entrada oficial para iniciar tu aplicación. Cualquiera que vea tu proyecto sabe que para arrancarlo, debe ejecutar python run.py.

2. Desacoplamiento: Desacopla el acto de ejecutar la aplicación de la lógica interna de la misma (que ahora vive en src). El run.py no sabe nada de tus rutas o modelos, solo sabe cómo usar la "fábrica" (create_app) que creaste.

3. Limpieza: Mantiene el código de arranque fuera del paquete principal de la aplicación (src), lo cual es una buena práctica de organización.

