import datetime
import asyncio
import aiohttp
from headers import headers
import json

def ingresar_origen():
    return input("origen:")

def definir_destinos():
    with open("destinos_Argentina.json", "r") as destinos:
        json_destinos = json.load(destinos)
        return [destino["id"].upper() for destino in json_destinos]

def definir_fechas():
    arr_fechas = []
    hoy = datetime.datetime.now()
    anio = hoy.year
    mes = hoy.month
    dia = hoy.day

    if dia<=16:
        arr_fechas.append(f"{anio:04}{mes:02}16")
    else:
        arr_fechas.append(f"{anio:04}{mes:02}{dia:02}")
    for i in range(1, 11):
        nuevo_anio = hoy.year
        nuevo_mes = hoy.month + i
        if nuevo_mes>12:
            nuevo_mes = hoy.month + i - 12
            nuevo_anio += 1

        arr_fechas.append(f"{nuevo_anio:04}{nuevo_mes:02}16")
    
    return arr_fechas

def armar_url(origen, destinos, fechas):
    arr_urls = []
    endpoint = "https://api.aerolineas.com.ar/v1/flights/offers"
    adultos = "1"
    chicos = "0"
    bebes = "0"
    fechas_flexibles = "true"
    clase = "Economy"
    tramo = "ONE_WAY"
    for fecha in fechas:
                #Este bloque busca en un solo destinopara evitar baneo de ip, por eso uso {destinos[3]}, para buscar en el 4 destino del JSON
        params = f"?adt={adultos}&inf={bebes}&chd={chicos}&flexDates={fechas_flexibles}&cabinClass={clase}&flightType={tramo}&leg={origen}-{destinos[3]}-{fecha}"
        arr_urls.append(endpoint + params)

            # usar este bloque de codigo cuando se utilicen proxies para buscar en multiples destinos
        # for destino in destinos:
        #     params = f"?adt={adultos}&inf={bebes}&chd={chicos}&flexDates={fechas_flexibles}&cabinClass={clase}&flightType={tramo}&leg={origen}-{destino}-{fecha}"
        #     arr_urls.append(endpoint + params)

    return arr_urls

async def fetch_url(session, url):
    try:
        async with session.get(url, headers=headers) as response:
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Error: {e}")
        return None
        

async def limpiar_datos(respuestas):
    arr_ofertas = []

    for respuesta in respuestas:
        if respuesta is not None and "calendarOffers" in respuesta:
            ofertas = respuesta["calendarOffers"]["0"]
            for oferta in ofertas:
                if oferta.get("offerDetails"):
                    destino = oferta["leg"]["segments"][0]["destination"]
                    precio = oferta["offerDetails"]["fare"]["total"]
                    anio, mes, dia = oferta["departure"].split("-")
                    dict_oferta = {
                        "fecha": f"{dia:02}/{mes:02}/{anio:04}",
                        "destino": destino,
                        "precio": precio
                    }
                    arr_ofertas.append(dict_oferta)

    return arr_ofertas

def ordenar_precios(ofertas):
    return sorted(ofertas, key=lambda d: d['precio'])

def guardar_ofertas(precios_ordenados):
    ofertas = open("ofertas.txt", 'w')
    ofertas.write(str(precios_ordenados).replace("}, ", "}\n").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace("precio: ", "precio: $"))

async def main():
    origen = ingresar_origen()
    destinos = definir_destinos()
    fechas = definir_fechas()
    urls = armar_url(origen, destinos, fechas)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

    ofertas = await limpiar_datos(responses)
    precios_ordenados = ordenar_precios(ofertas)
    guardar_ofertas(precios_ordenados)

if __name__ == "__main__":
    asyncio.run(main())