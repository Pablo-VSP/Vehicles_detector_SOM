# Imagen ligera ARM64
FROM python:3.11-slim

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias mínimas del sistema
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio app
WORKDIR /app

# Copiar requirements primero (mejor cache)
COPY requirements.txt .

# Instalar solo numpy y opencv
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Variable importante para que Python encuentre libs del host
ENV LD_LIBRARY_PATH=/usr/lib:/lib:$LD_LIBRARY_PATH

CMD ["python3", "main.py"]