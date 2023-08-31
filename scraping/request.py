import datetime
import asyncio
import aiohttp
from headers import headers
import json
import uuid



def read_json(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
    


def save_json(filename, dict):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(dict, json_file)



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
            if response.status == 200:
                print(response.status)
                return await response.json()
            else:
                print(f"error {response.status}")
    except aiohttp.ClientError as e:
        print(f"Error: {e}")
        return None
    


def get_city_name(city_code):
    json_destinations = read_json("./scraping/destinations.json")[0]["destinos"]
    for destination in json_destinations:
        if city_code.lower() == destination["id"].lower():
           return destination["cityName"]



async def clean_json(responses):
    offers_list = []
    
    for res in responses:
        empty_results = False
        messages = res["searchMetadata"]["infoMessages"]
        
        for msg in messages:
            if "gds.flights.info.emptyResults" in msg:
                empty_results = True

        if not empty_results:
            offers = res["calendarOffers"]["0"]
            
            for offer in offers:
                offer_exists = offer["offerDetails"] != None
                if offer_exists:
                    flight_data = offer["leg"]["segments"][0]
                    offer_data = offer["offerDetails"]

                    offer_dict = {
                        "id": f"{uuid.uuid4()}",
                        "flightNumber": f'{flight_data["flightNumber"]}',
                        "origin": flight_data["origin"],
                        "destination": flight_data["destination"],
                        "departure": flight_data["departure"],
                        "arrival": flight_data["arrival"],
                        "duration": flight_data["duration"],
                        "cabinClass": offer_data["cabinClass"],
                        "availability": offer_data["seatAvailability"]["seats"],
                        "price": offer_data["fare"]["total"],
                        "originCity": get_city_name(flight_data["origin"]),
                        "destinationCity": get_city_name(flight_data["destination"]),
                    }
                    offers_list.append(offer_dict)
                    
    return offers_list



def sort_offers(offers):
    return sorted(offers, key=lambda d: d['precio'])



def save_offers(sorted_offers):
    offers = open("./scraping/offers2.txt", 'w', encoding="utf-8")
    offers.write(str(sorted_offers).replace("}, ", "}\n").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("'", "").replace("precio: ", "precio: $"))



async def main():
    origin = input_origin()
    destinations = set_destination()
    dates = set_date()
    urls = set_url(origin, destinations, dates)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

    offers = await clean_json(responses)
    save_json("./data/offers.json", offers)

if __name__ == "__main__":
    asyncio.run(main())