# Use official slim Python runtime
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system dependencies (including pg_config/libpq for psycopg2 if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Copy and install python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Copy entrypoint script and make it executable
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && \
    sed -i 's/\r$//g' /usr/local/bin/docker-entrypoint.sh

# Create a non-root system user and adjust permissions
RUN useradd -m -u 1000 django && \
    chown -R django:django /app
USER django

# Expose port
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["docker-entrypoint.sh"]

# Start production server using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "/app/unestadodigital", "unestadodigital.wsgi:application"]
