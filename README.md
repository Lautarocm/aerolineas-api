# Aerolineas Argentinas - Buscador de Ofertas

Este proyecto permite al usuario ingresar un origen y destino y buscar ofertas de vuelos de todo el año, utilizando la API oficial de Aerolineas Argentinas.

## Contenido

- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Nota](#nota)

## Requisitos

- Python 3.x y pip
- Node.JS y npm
- Librerias de Python: `selenium`, `selenium-wire`, `webdriver-manager`, `requests`, `aiohttp`.
- Paquetes de Node: `express`, `cors`, kit de `fortawesome`, `nextui`, `autoprefixer`, `eslint`, `eslint-config-next`, `framer-motion`, `next`, `postcss`, `react`, `react-dom`, `tailwindcss`.

## Configuración

1. Clona este repositorio:

```sh
git clone https://github.com/Lautarocm/aerolineas-api.git
cd aerolineas-api
```

2. Crea y activa un entorno virtual en la raíz del proyecto:

```sh
virtualenv env
env\Scripts\activate
```

3. Instala las librerias necesarias:

```sh
pip install -r scraping/requirements.txt
```

4. Ejecuta `get_token.py`:

```sh
cd scraping
python get_token.py
```

5. Instala las dependencias del frontend (Next.JS):

```sh
cd ../client
npm install
```

6. Instala las dependencias del backend (Express.JS):

```sh
cd ../server
npm install
```

## Uso

1. Abre una terminal para el backend.
2. Corre el servidor en modo dev:

```sh
cd server
npm run dev
```

3. Abre una terminal para el frontend.
4. Corre el cliente en modo dev:

```sh
cd client
npm run dev
```

5. Abre un navegador y navega a `localhos:3000`:

[http://localhost:3000](http://localhost:3000)

A continuación, navega a la sección `Vuelos` y realiza una búsqueda. El programa buscará ofertas de vuelos y las mostrará en formato de tarjetas, puedes filtrar por meses y ordenar los precios en orden ascendente.

## Resultados

Los resultados incluyen toda la información de los vuelos como fechas, precio, aeropuertos, disponibilidad, entre otros.

## Estructura del proyecto

aerolineas-api/
|-- client/
|   |-- archivos de la aplicación Next.JS
|
|-- data/
|   |-- archivos JSON
|
|-- env/
|   |-- archivos del entorno virtual
|
|-- scraping/
|   |-- archivos de scraping
|
|-- server/
|   |-- archivos del servidor Express
|
|-- .gitignore
|-- README.md


## Nota

Este proyecto está diseñado para uso educativo y no comercial.
