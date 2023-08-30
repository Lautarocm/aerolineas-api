import datetime
import asyncio
import aiohttp
from headers import headers
import json

def read_json(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

def input_origin():
    return input("Origen: ")

def set_destination():
    json_destinations = read_json("./scraping/destinations.json")[0]["destinos"]
    return [destination["id"].upper() for destination in json_destinations]

def set_date():
    dates_list = []
    today = datetime.datetime.now()
    year = today.year
    month = today.month
    day = today.day

    if day<=16:
        dates_list.append(f"{year:04}{month:02}16")
    else:
        dates_list.append(f"{year:04}{month:02}{day:02}")
    for i in range(1, 11):
        year = today.year
        month = today.month + i
        if month>12:
            month = today.month + i - 12
            year += 1

        dates_list.append(f"{year:04}{month:02}16")
    
    return dates_list

def set_url(origin, destinations, dates):
    urls_list = []
    endpoint = "https://api.aerolineas.com.ar/v1/flights/offers"
    adults = "1"
    children = "0"
    babies = "0"
    flex_dates = "true"
    cabin_class = "Economy"
    flight_type = "ONE_WAY"
    for date in dates:
                #Este bloque busca en un solo destino para evitar baneo de ip por exceso de peticiones, por eso uso {destinations[3]}, para buscar en un solo destino del JSON
        params = f"?adt={adults}&inf={babies}&chd={children}&flexDates={flex_dates}&cabinClass={cabin_class}&flightType={flight_type}&leg={origin}-{destinations[3]}-{date}"
        urls_list.append(endpoint + params)

            # Este bloque de codigo busca en multiples destinos. IMPORTANTE! ROTAR IPs PARA EVITAR BANEO
        # for destination in destinations:
        #     params = f"?adt={adults}&inf={babies}&chd={children}&flexDates={flex_dates}&cabinClass={cabin_class}&flightType={flight_type}&leg={origin}-{destination}-{date}"
        #     urls_list.append(endpoint + params)

    return urls_list

async def fetch_url(session, url):
    try:
        async with session.get(url, headers=headers) as response:
            print(response.status)
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Error: {e}")
        return None
        

async def clean_data(responses):
    offers_list = []

    for res in responses:
        if "calendarOffers" in res and "0" in res["calendarOffers"]:
            offers = res["calendarOffers"]["0"]
            for offer in offers:
                if offer.get("offerDetails"):
                    city_code = offer["leg"]["segments"][0]["destination"].lower()
                    json_destinations = read_json("./scraping/destinations.json")[0]["destinos"]
                    city_name = ""
                    for destination in json_destinations:
                        if city_code == destination["id"]:
                            city_name = destination["cityName"]

                    price = offer["offerDetails"]["fare"]["total"]
                    year, month, day = offer["departure"].split("-")
                    offer_dict = {
                        "fecha": f"{day:02}/{month:02}/{year:04}",
                        "destino": city_name,
                        "precio": price
                    }
                    offers_list.append(offer_dict)

    return offers_list

def sort_offers(offers):
    return sorted(offers, key=lambda d: d['precio'])

def save_offers(sorted_offers):
    offers = open("./scraping/offers.txt", 'w', encoding="utf-8")
    offers.write(str(sorted_offers).replace("}, ", "}\n").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace("precio: ", "precio: $"))

async def main():
    origin = input_origin()
    destinations = set_destination()
    dates = set_date()
    urls = set_url(origin, destinations, dates)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

    ofertas = await clean_data(responses)
    precios_ordenados = sort_offers(ofertas)
    save_offers(precios_ordenados)

if __name__ == "__main__":
    asyncio.run(main())