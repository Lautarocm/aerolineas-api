import requests
import pandas as pd
from headers import headers



def get_destinos(pais):
    try:
        response = requests.get(f"https://api.aerolineas.com.ar/v1/suggest/suggestions/destinations?term={pais}", headers=headers)
        print(response.status_code)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        df.to_json("destinos_argentina.json", force_ascii=False, orient='records')
    except requests.RequestException as e:
        print(f"Error: {e}")
    

def main():
    pais = input("Ingrese el país del cual quiera obtener los aeropuertos: ")
    get_destinos(pais)
main()