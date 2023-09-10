import requests
import json

token = ""
url = "https://api.aerolineas.com.ar/v1/catalog/airports"

with open("C:/Users/Usuario/Documents/proyectos/aerolineas-api/scraping/token.txt") as file:
    token = file.read()

headers = {
  'authority': 'api.aerolineas.com.ar',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'es-AR',
  'authorization': token,
  'cache-control': 'no-cache',
  'origin': 'https://www.aerolineas.com.ar',
  'pragma': 'no-cache',
  'referer': 'https://www.aerolineas.com.ar/',
  'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'traceparent': '00-d4f9640f06aad5c730b45d5351b07398-85efbd3f8bd83b2e-01',
  'tracestate': '2216741^@nr=0-1-2216741-326092031-85efbd3f8bd83b2e----1694305577591',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
  'x-channel-id': 'WEB_AR'
}
response = requests.request("GET", url, headers=headers)
with open("./data/airports.json", "w") as file:
    json.dump(response.json()["resources"], file)
