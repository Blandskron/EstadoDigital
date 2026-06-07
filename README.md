# EstadoDigital - Plataforma de Registro de Eventos

Este es un proyecto profesional avanzado basado en **Django 5.1.1** diseñado para gestionar el registro de asistentes para el evento **UN ESTADO DIGITAL**. El sistema está completamente preparado para entornos de producción, incorporando altos estándares de seguridad y facilidades de despliegue automatizado mediante contenedores Docker.

---

## 🛠️ Arquitectura y Tecnologías
- **Core**: Django 5.1.1 (Python 3.11/3.12)
- **Base de Datos**: PostgreSQL para producción y SQLite para desarrollo local (adaptable mediante `DATABASE_URL`).
- **Servidor de Producción**: Gunicorn.
- **Gestión de Estáticos**: WhiteNoise (compresión y almacenamiento optimizado en caché).
- **Contenedores**: Docker & Docker Compose.
- **Variables de Entorno**: `python-dotenv` y `dj-database-url`.

---

## 🔒 Mejoras de Seguridad Implementadas

1. **Variables de Entorno Estrictas**:
   - Se eliminaron las credenciales y llaves secretas del archivo de configuración `settings.py`. Ahora toda la información sensible (contraseñas de correo, claves secretas, hosts permitidos) se administra mediante un archivo `.env`.
2. **Encabezados de Seguridad HTTP**:
   - En entornos de producción (`DJANGO_DEBUG=False`), se habilitan automáticamente políticas estrictas:
     - Redirección HTTPS forzada (`SECURE_SSL_REDIRECT`).
     - HSTS (HTTP Strict Transport Security) configurado a 1 año (`SECURE_HSTS_SECONDS=31536000`), incluyendo subdominios y precarga.
     - Cookies de sesión y CSRF protegidas con el flag `Secure` (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`).
     - Protección contra rastreo de tipo MIME (`SECURE_CONTENT_TYPE_NOSNIFF`).
     - Protección contra ataques XSS en navegadores antiguos (`SECURE_BROWSER_XSS_FILTER`).
     - Prevención de clickjacking configurando `X_FRAME_OPTIONS` a `DENY`.
3. **Contenedorización Segura (No-Root)**:
   - El contenedor Docker no se ejecuta con privilegios de administrador (`root`). Se creó un usuario del sistema `django` y se le asignaron permisos explícitos sobre el directorio de trabajo, reduciendo drásticamente la superficie de ataque del host ante posibles vulnerabilidades.
4. **Validaciones Avanzadas de Formulario**:
   - Validación personalizada del campo RUT chileno e imposibilidad de agendar tracks del evento que colisionen en el mismo bloque horario (definido en `forms.py`).

---

## 🚀 Despliegue con Docker Compose (Automático e Instantáneo)

El proyecto incluye soporte listo para usar para levantar tanto el servidor web como una base de datos PostgreSQL de forma aislada.

### Requisitos previos
- Docker y Docker Compose instalados.

### Instrucciones de Despliegue

1. **Crear archivo de configuración `.env`**:
   Copia la plantilla de ejemplo:
   ```bash
   cp .env.example .env
   ```
   *Nota: Ajusta los valores de las variables en tu archivo `.env` según tus necesidades de seguridad.*

2. **Levantar los servicios**:
   Ejecuta el siguiente comando para construir la imagen y levantar los contenedores en segundo plano:
   ```bash
   docker compose up --build -d
   ```

3. **Acciones Automatizadas en el Inicio**:
   El script de punto de entrada (`docker-entrypoint.sh`) se encarga automáticamente de:
   - Esperar a que la base de datos PostgreSQL esté lista para aceptar conexiones.
   - Ejecutar las migraciones pendientes en la base de datos (`python manage.py migrate`).
   - Recolectar todos los archivos estáticos (`python manage.py collectstatic`).
   - Crear un superusuario administrativo por defecto si no existe (usando las credenciales especificadas en `.env` mediante `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, y `DJANGO_SUPERUSER_PASSWORD`).

4. **Acceder a la aplicación**:
   - Sitio principal: [http://localhost:8000](http://localhost:8000)
   - Panel de Administración de Django: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 💻 Desarrollo Local (Sin Docker)

Si prefieres ejecutar el proyecto de forma local utilizando SQLite:

1. Crea y activa tu entorno virtual:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Genera un archivo `.env` con `DJANGO_DEBUG=True`. Al no especificar la variable `DATABASE_URL`, el sistema utilizará SQLite (`db.sqlite3`) de manera automática.

4. Corre las migraciones y levanta el servidor:
   ```bash
   python unestadodigital/manage.py migrate
   python unestadodigital/manage.py runserver
   ```
