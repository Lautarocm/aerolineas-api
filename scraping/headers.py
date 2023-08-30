from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-AR",
    "Authorization": api_key,
    "Origin": "https://www.aerolineas.com.ar",
    "Referer": "https://www.aerolineas.com.ar/",
    "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Traceparent": "00-e42ed516d431d90c8326aef0b55bb46c-5c2f11ce9b6e91aa-01",
    "Tracestate": "2216741@nr=0-1-2216741-326092031-5c2f11ce9b6e91aa----1692909310970",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "X-Channel-Id": "WEB_AR"
}