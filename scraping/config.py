import datetime
from utilities import read_token as token

headers = {
    ':authority': 'api.aerolineas.com.ar',
    ':method': 'GET',
    ':scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-AR',
    'Authorization': token(),
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