# Usa una imagen base de Ubuntu 24.04
FROM ubuntu:24.04

# Establece el directorio de trabajo
WORKDIR /app

# Actualiza el sistema e instala dependencias necesarias
RUN apt-get update && \
    apt-get install -y \
    python3.12 \
    python3-pip \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia los archivos de requisitos al contenedor
COPY requirements.txt /app/requirements.txt

# Instala las dependencias de Python
RUN pip3 install --upgrade pip \
    && pip3 install -r /app/requirements.txt

# Crea los directorios en el contenedor
RUN mkdir -p /var/server_api /var/server_web

# Copia las carpetas de tus aplicaciones al contenedor
COPY server_api/ /var/server_api/
COPY server_web/ /var/server_web/
COPY .env /var/

# Expone los puertos que usarán tus aplicaciones
EXPOSE 5000  
EXPOSE 8000  

# Define el comando por defecto para ejecutar las aplicaciones
CMD ["sh", "-c", "python3 /var/server_api/app.py & python3 /var/server_web/app.py"]
