import datetime
import asyncio
import aiohttp
from headers import headers
import json

def leer_json(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

def ingresar_origen():
    return input("Origen: ")

def definir_destinos():
    json_destinos = leer_json("destinos_argentina.json")[0]["destinos"]
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
                #Este bloque busca en un solo destino para evitar baneo de ip por exceso de peticiones, por eso uso {destinos[3]}, para buscar en un solo destino del JSON
        params = f"?adt={adultos}&inf={bebes}&chd={chicos}&flexDates={fechas_flexibles}&cabinClass={clase}&flightType={tramo}&leg={origen}-{destinos[3]}-{fecha}"
        arr_urls.append(endpoint + params)

            # Este bloque de codigo busca en multiples destinos. iMPORTANTE! ROTAR IPs PARA EVITAR BANEO
        # for destino in destinos:
        #     params = f"?adt={adultos}&inf={bebes}&chd={chicos}&flexDates={fechas_flexibles}&cabinClass={clase}&flightType={tramo}&leg={origen}-{destino}-{fecha}"
        #     arr_urls.append(endpoint + params)

    return arr_urls

async def fetch_url(session, url):
    try:
        async with session.get(url, headers=headers) as response:
            print(response.status)
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Error: {e}")
        return None
        

async def limpiar_datos(respuestas):
    arr_ofertas = []

    for respuesta in respuestas:
        if "calendarOffers" in respuesta and "0" in respuesta["calendarOffers"]:
            ofertas = respuesta["calendarOffers"]["0"]
            for oferta in ofertas:
                if oferta.get("offerDetails"):
                    codigo_ciudad = oferta["leg"]["segments"][0]["destination"].lower()
                    json_destinos = leer_json("destinos_argentina.json")[0]["destinos"]
                    nombre_ciudad = ""
                    for destino in json_destinos:
                        if codigo_ciudad == destino["id"]:
                            nombre_ciudad = destino["cityName"]

                    precio = oferta["offerDetails"]["fare"]["total"]
                    anio, mes, dia = oferta["departure"].split("-")
                    dict_oferta = {
                        "fecha": f"{dia:02}/{mes:02}/{anio:04}",
                        "destino": nombre_ciudad,
                        "precio": precio
                    }
                    arr_ofertas.append(dict_oferta)

    return arr_ofertas

def ordenar_precios(ofertas):
    return sorted(ofertas, key=lambda d: d['precio'])

def guardar_ofertas(precios_ordenados):
    ofertas = open("ofertas.txt", 'w', encoding="utf-8")
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