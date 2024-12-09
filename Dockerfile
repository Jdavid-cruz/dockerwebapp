# Usamos la imagen base de Nginx
FROM nginx:alpine

# Copiamos los archivos HTML y CSS al contenedor
COPY ./html /usr/share/nginx/html

# Copiamos el archivo de la base de datos y el script al contenedor
COPY ./data /data

# Exponemos el puerto 80 para acceder al servidor Nginx
EXPOSE 80
