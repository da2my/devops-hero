# Etapa 1: build
FROM python:3.11-slim-bookworm AS builder

# Evita bytecode y buffers en logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema mínimas (por si algunas libs lo requieren)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix="/install" -r requirements.txt

# Etapa 2: Runtime - La imagen final distroless
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/install/lib/python3.11/site-packages

# Copia las dependencias desde la etapa 'builder'
COPY --from=builder /install /install

# Copiar todo el código de la aplicación (src, config.py, run.py, etc.)
COPY . .

# Comando para ejecutar la aplicación con Gunicorn (servidor de producción)
#binario directo en caso de fallback
# CMD ["/install/bin/gunicorn", "--bind", "0.0.0.0:5000", "run:app"]

#usa ENTRYPOINT de distroless
# CMD ["-m", "gunicorn", "--bind", "0.0.0.0:5000", "run:app"]

# ENTRYPOINT explícito → controlamos siempre qué binario se arranca
ENTRYPOINT ["/usr/bin/python3.11"]
# CMD → lo que se pasa al intérprete Python
CMD ["-m", "gunicorn", "--bind", "0.0.0.0:5000", "run:app"]




