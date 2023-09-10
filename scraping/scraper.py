import datetime
import asyncio
import aiohttp
from headers import headers
import json
import uuid
import sys


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


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


def set_url(origin, destination, dates):
    urls_list = []
    endpoint = "https://api.aerolineas.com.ar/v1/flights/offers"
    adults = "1"
    children = "0"
    babies = "0"
    flex_dates = "true"
    cabin_class = "Economy"
    flight_type = "ONE_WAY"
    for date in dates:
        params = f"?adt={adults}&inf={babies}&chd={children}&flexDates={flex_dates}&cabinClass={cabin_class}&flightType={flight_type}&leg={origin}-{destination}-{date}"
        urls_list.append(endpoint + params)
    return urls_list


            #el código comentado en esta función es para que no salga en la salida del child_proccess en Node
async def fetch_url(session, url):
    try:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                # print(response.status)
                return await response.json()
            # else:
            #     print(f"error {response.status}") 
    except aiohttp.ClientError as e:
        # print(f"Error: {e}")
        return None
   

def get_city_name(city_code):
    json_destinations = read_json("C:/Users/Usuario/Documents/proyectos/aerolineas-api/data/airports.json")
    for destination in json_destinations:
        if city_code.lower() == destination["iataCode"].lower():
           return destination["city"]["name"]


async def clean_offers(responses):
    filtered_empty_results = [offer["calendarOffers"]["0"] for offer in responses if len(offer["calendarOffers"]) > 0]
    filtered_offers = []
    for month_offers in filtered_empty_results:
        for offer in month_offers:
            if offer["offerDetails"] != None:
                filtered_offers.append(offer)
    return filtered_offers


def create_json_offers(cleaned_offers):
    offers_list = []
    for offer in cleaned_offers:
        offer_data = offer["offerDetails"]
        segments = offer["leg"]["segments"]
        offer_dict = {
                "id": f"{uuid.uuid4()}",
                "flightsNumbers": [f'{segment["flightNumber"]}' for segment in segments],
                "origin": segments[0]["origin"],
                "destination": segments[len(segments)-1]["destination"],
                "departures": [segment["departure"] for segment in segments],
                "arrivals": [segment["arrival"]for segment in segments],
                "duration": offer["leg"]["totalDuration"],
                "cabinClass": offer_data["cabinClass"],
                "availability": offer_data["seatAvailability"]["seats"],
                "price": offer_data["fare"]["total"],
                "originCity": get_city_name(segments[0]["origin"]),
                "destinationCity": get_city_name(segments[len(segments)-1]["destination"]),
                "connections": offer["leg"]["stops"],
                "connectionsAirports": [segment["destination"] for i, segment in enumerate(segments) if i < len(segments)-1]
            }
        offers_list.append(offer_dict)
    return offers_list


async def main(origin, destination):
    dates = set_date()
    urls = set_url(origin, destination, dates)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
    cleaned_offers = await clean_offers(responses)
    final_offers = create_json_offers(cleaned_offers)
    return final_offers


final_offers = asyncio.run(main(sys.argv[1], sys.argv[2]))
print(json.dumps(final_offers))