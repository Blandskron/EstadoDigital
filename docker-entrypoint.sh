#!/bin/sh
set -e

# Wait for database if PostgreSQL is used
if [ -n "$DATABASE_URL" ]; then
  # Parse host and port from DATABASE_URL if PostgreSQL is used
  # Example URL: postgres://user:pass@host:5432/dbname
  DB_HOST=$(echo "$DATABASE_URL" | sed -n 's/.*@\(.*\):.*/\1/p')
  DB_PORT=$(echo "$DATABASE_URL" | sed -n 's/.*:\([0-9]*\)\/.*/\1/p')
  
  if [ -n "$DB_HOST" ] && [ -n "$DB_PORT" ]; then
    echo "Waiting for database at $DB_HOST:$DB_PORT..."
    # Loop until PostgreSQL port is open
    while ! curl -s --connect-timeout 2 http://$DB_HOST:$DB_PORT > /dev/null 2>&1; do
      # Since we don't have pg_isready/nc installed on the slim image, we can try to use a quick python check
      if python -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
try:
    s.connect(('$DB_HOST', int('$DB_PORT')))
    s.close()
    exit(0)
except Exception:
    exit(1)
" > /dev/null 2>&1; then
        break
      fi
      sleep 1
    done
    echo "Database is up and running!"
  fi
fi

echo "Applying database migrations..."
python /app/unestadodigital/manage.py migrate --noinput

echo "Collecting static files..."
python /app/unestadodigital/manage.py collectstatic --noinput

echo "Checking superuser creation..."
python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unestadodigital.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@unestadodigital.cl')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print('Superuser successfully created!')
    else:
        print('Superuser already exists. Skipping creation.')
else:
    print('Superuser environment variables not set. Skipping creation.')
"

# Execute the CMD passed to Docker
exec "$@"
