import requests
import pandas as pd
from headers import headers


    #Se puede obtener la lista de destinos de cualquier país pasando el nombre como argumento a la función get_destinations

def get_destinations(country):
    try:
        response = requests.get(f"https://api.aerolineas.com.ar/v1/suggest/suggestions/destinations?term={country}", headers=headers)
        print(response.status_code)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        df.to_json("./data/destinations.json", force_ascii=False, orient='records')
    except requests.RequestException as e:
        print(f"Error: {e}")
    

def main():
    country = input("Ingrese el país del cual quiera obtener los aeropuertos: ")
    get_destinations(country)
main()