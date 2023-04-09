# Ciomprix prueba tecnica

El siguiente proyecto contiene la solucion a la prueba tecnica de ciomprix

## Instalacion

Usar el manejador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar las dependencias del proyecto.

```bash
pip install -r requirements.txt
```
Configurar un archivo .env el cual contendra las variables de entorno del proyecto, se puede basar en el archivo .env.copy
```bash
cp .env.copy .env
```

## Uso
Par correr el proyecto sin instalacion local podemos usar docker compose para iniciarlo
```bash
docker-compose up -d --build
```
Actualmente el proyecto corre bajo el puerto 5000, asi que una vez se halla configurado abrir el endpoint en el puerto 5000

## Coleccion 

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/25189060-f11f4616-2219-43d5-afa9-86f98863ee70?action=collection%2Ffork&collection-url=entityId%3D25189060-f11f4616-2219-43d5-afa9-86f98863ee70%26entityType%3Dcollection%26workspaceId%3D7b14557c-ef23-44c5-92d1-05429f3e8bca)


