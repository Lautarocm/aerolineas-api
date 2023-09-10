token = ""

with open("C:/Users/Usuario/Documents/proyectos/aerolineas-api/scraping/token.txt") as file:
    token = file.read()

headers = {
    ':authority': 'api.aerolineas.com.ar',
    ':method': 'GET',
    ':scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-AR',
    'Authorization': token,
    'Cache-Control': 'no-cache',
    'Origin': 'https://www.aerolineas.com.ar',
    'Pragma': 'no-cache',
    'Referer': 'https://www.aerolineas.com.ar/',
    'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Traceparent': '00-e767befcd4ff25e93ea38ccc889b6c38-4eb17e7a8bef3661-01',
    'Tracestate': '2216741@nr=0-1-2216741-326092031-4eb17e7a8bef3661----1693853030827',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Channel-Id': 'WEB_AR'
}