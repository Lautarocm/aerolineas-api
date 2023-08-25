import requests
import datetime
from destinos import destinos_argentina_filtrados

from headers import headers

def ingresar_origen():
    return input("origen:")

def definir_destinos(destinos):
    arr_destinos = []
    for destino in destinos:
        arr_destinos.append(destino["codigo"])
    return arr_destinos

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
        for destino in destinos:
            params = f"?adt={adultos}&inf={bebes}&chd={chicos}&flexDates={fechas_flexibles}&cabinClass={clase}&flightType={tramo}&leg={origen}-{destino}-{fecha}"
            arr_urls.append(endpoint + params)
    return arr_urls

def consumir_api(urls, headers):
    arr_respuestas = []
    for url in urls:
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            arr_respuestas.append(respuesta.json()["calendarOffers"])
        else:
            print(f"Error: {respuesta.status_code}")
    return  arr_respuestas

def limpiar_datos(respuestas):
    arr_ofertas = []

    for respuesta in respuestas:
        ofertas = respuesta["0"]
        for oferta in ofertas:
            if oferta["offerDetails"]:
                destino = oferta["leg"]["segments"][0]["destination"]
                precio = oferta["offerDetails"]["fare"]["total"]
                anio, mes, dia = oferta["departure"].split("-")
                piripipi = {
                    "fecha": f"{dia:02}/{mes:02}/{anio:04}",
                    "destino": destino,
                    "precio": precio
                }
                arr_ofertas.append(piripipi)
    

    return arr_ofertas

def ordenar_precios(ofertas):
    precios_ordenados = sorted(ofertas, key=lambda d: d['precio'])

    return precios_ordenados

def guardar_ofertas(precios_ordenados):
    ofertas = open("ofertas.txt", 'w')
    ofertas.write(str(precios_ordenados).replace("}, ", "}\n").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace("precio: ", "precio: $"))

def main():
    origen = ingresar_origen()
    destinos = definir_destinos(destinos_argentina_filtrados)
    fechas = definir_fechas()
    urls = armar_url(origen, destinos, fechas)
    respuestas = consumir_api(urls, headers)
    ofertas = limpiar_datos(respuestas)
    precios_ordenados = ordenar_precios(ofertas)
    guardar_ofertas(precios_ordenados)

main()