# Usar una imagen base de Python
FROM python:3.11.2

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /website

# Copiar los archivos de requerimientos, la aplicación y el archivo mysqlconnection.py
COPY requirements.txt .
COPY app.py .
COPY mysqlconnection.py .
COPY . /website

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 4000

# Ejecutar la aplicación
CMD ["python", "app.py"]