# Etapa 1: build
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix="/install" -r requirements.txt

# Etapa 2: Runtime - La imagen final distroless
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

#ruta de Python para que encuentre los paquetes instalados
ENV PYTHONPATH=/install/lib/python3.11/site-packages

# Copia las dependencias desde la etapa 'builder'
COPY --from=builder /install /install

# Copiar todo el código de la aplicación (src, config.py, run.py, etc.)
COPY . .

# Comando para ejecutar la aplicación con Gunicorn (servidor de producción)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]