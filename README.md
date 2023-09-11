# Aerolineas Argentinas - Buscador de Ofertas

Este proyecto permite al usuario ingresar un origen y destino y buscar ofertas de vuelos de todo el año, utilizando la API oficial de Aerolineas Argentinas.

## Contenido

- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura](#estructura)
- [Notas](#notas)

## Requisitos

- Python 3.x, pip y virtualenv
- Node.JS y npm
- Librerias de Python: `selenium`, `selenium-wire`, `webdriver-manager`, `requests`, `aiohttp`.
- Paquetes de Node: `express`, `cors`, kit de `fortawesome`, `nextui`, `autoprefixer`, `eslint`, `eslint-config-next`, `framer-motion`, `next`, `postcss`, `react`, `react-dom`, `tailwindcss`.

## Configuración

1. Clona este repositorio:

```sh
git clone https://github.com/Lautarocm/aerolineas-api.git
cd aerolineas-api
```

2. Instala la herramienta virtualenv:

```sh
pip install virtualenv
```

3. Crea y activa un entorno virtual en la raíz del proyecto:

```sh
virtualenv env
env\Scripts\activate
```

4. Instala las librerias necesarias de Python:

```sh
pip install -r scraping/requirements.txt
```

5. Ejecuta `get_token.py`: [Importante! ver notas](#notas)

```sh
cd scraping
python get_token.py
```

6. Ejecuta `get_airports.py`:

```sh
python get_airports.py
```

7. Instala las dependencias del frontend (Next.JS):

```sh
cd ../client
npm install
```

8. Instala las dependencias del backend (Express.JS):

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
Además se generará un log con información por cada request realizada. Incluye información de errores

## Estructura

- `aerolineas-api/`
  - `client/`
    - Archivos de la aplicación Next.js
  - `data/`
    - Archivos JSON
  - `env/`
    - Archivos del entorno virtual
  - `scraping/`
    - Archivos de scraping
  - `server/`
    - Archivos del servidor Express
  - `.gitignore`
  - `README.md`

## Notas

Al ejecutar `get_token.py` posiblemente aparezcan en la terminal errores de certificados SSL. Esto no interrumpe la ejecución, al terminar, el token estará en la carpeta `/scraping`

Este proyecto está diseñado para uso educativo y no comercial.
