from models import FlightOffer
from utilities import read_json
import os
from utilities import get_script_directory as dir

current_dir = dir(__file__)

def get_city_name(city_code):
    airports_dir = os.path.join(current_dir, "..", "data", "airports.json")
    airports_json = read_json(airports_dir)
    for destination in airports_json:
        if city_code.lower() == destination["iataCode"].lower():
           return destination["city"]["name"]

async def parse_data(responses):
    parsed_data = []
    filtered_empty_results = [offer["calendarOffers"]["0"] for offer in responses if len(offer["calendarOffers"]) > 0]
    for month_offers in filtered_empty_results:
        for offer in month_offers:
            if offer["offerDetails"] != None:
                parsed_data.append(offer)
    return parsed_data

def create_offers_list(parsed_data):
    flights_offers = []
    for offer in parsed_data:
        offer_details = offer["offerDetails"]
        segments = offer["leg"]["segments"]
        flight_offer = FlightOffer()
        
        flight_offer.flights_numbers = [f'{segment["flightNumber"]}' for segment in segments]
        flight_offer.origin = segments[0]["origin"]
        flight_offer.destination = segments[len(segments)-1]["destination"]
        flight_offer.departures = [segment["departure"] for segment in segments]
        flight_offer.arrivals = [segment["arrival"]for segment in segments]
        flight_offer.duration = offer["leg"]["totalDuration"]
        flight_offer.cabin_class = offer_details["cabinClass"]
        flight_offer.availability = offer_details["seatAvailability"]["seats"]
        flight_offer.price = offer_details["fare"]["total"]
        flight_offer.origin_city = get_city_name(segments[0]["origin"])
        flight_offer.destination_city = get_city_name(segments[len(segments)-1]["destination"])
        flight_offer.connections = offer["leg"]["stops"]
        flight_offer.connections_airports = [segment["destination"] for i, segment in enumerate(segments) if i < len(segments)-1]

        flights_offers.append(flight_offer.to_dict())
    return flights_offers