# Usar una imagen base de Python
FROM python:3.11.2

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requerimientos y el código de la aplicación
COPY requirements.txt .
COPY app.py .

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
