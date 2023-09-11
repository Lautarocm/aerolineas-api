import uuid

class FlightOffer:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.flights_numbers = []
        self.origin = ""
        self.destination = ""
        self.departures = []
        self.arrivals = []
        self.duration = 0
        self.cabin_class = ""
        self.availability = 0
        self.price = 0
        self.origin_city = ""
        self.destination_city = ""
        self.connections = 0
        self.connections_airports = []
    
    def to_dict(self):
        return{
            "id": self.id,
            "flights_numbers": self.flights_numbers,
            "origin": self.origin,
            "destination": self.destination,
            "departures": self.departures,
            "arrivals": self.arrivals,
            "duration": self.duration,
            "cabin_class": self.cabin_class,
            "availability": self.availability,
            "price": self.price,
            "origin_city": self.origin_city,
            "destination_city": self.destination_city,
            "connections": self.connections,
            "connections_airports": self.connections_airports
        }