# Aerolineas Argentinas - Buscador de Ofertas

Este proyecto permite al usuario ingresar un origen y buscar ofertas de vuelos a distintos destinos, utilizando la API oficial de Aerolineas Argentinas.

## Contenido

- `destinations.json`: Contiene destinos de vuelo en Argentina.
- `get_destinations.py`: Contiene las funciones para obtener el archivo JSON con los posibles destinos.
- `headers.py`: Define los headers para hacer las solicitudes a la API, incluida la autenticación.
- `request.py`: Contiene las funciones necesarias para interactuar con el usuario, definir los parámetros de búsqueda, consumir la API, procesar y almacenar los datos en un JSON.
- `requiriments.txt`: Contiene las librerias necesarias para correr el proyecto.

## Pre-requisitos

- Python 3.x
- Bibliotecas `requests`, `asyncio`, `aiohttp`, `json`,  `dotenv` y `uuid`, `datetime`, `json` de Python.

## Configuración

1. Clona este repositorio.
2. Crea un entorno virtual en la raíz del proyecto.
3. Crea un archivo `.env` en la raíz del proyecto.
4. En el archivo `.env`, establece tu clave de API:

```sh
API_KEY=tu_clave_de_api_aqui
```

5. Instala las librerias necesarias:

```sh
pip install -r scraping/requirements.txt
```

## Uso

Ejecuta `request.py`:

```sh
python request.py
```

A continuación, introduce el código de ciudad de origen cuando se te solicite. El programa buscará ofertas de vuelos desde esa ciudad a los destinos elegidos para las próximas fechas y guardará los resultados en `/scraping/offers.json`.

## Resultados

Los resultados incluyen toda la información de los vuelos como fechas, precio, aeropuertos, disponibilidad, entre otros.

## Nota

Este proyecto está diseñado para uso educativo y no comercial.
