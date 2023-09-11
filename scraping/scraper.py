import aiohttp
import asyncio
from config import headers
from utilities import write_log as log, get_ip

            
async def fetch_url(session, url):
    async with session.get(url, headers=headers) as res:
        if res.status == 200:
            log(f"STATUS 200: {url}")
            return await res.json()
        elif res.status == 401:
            log(f"ERROR 401: Authentication error (run '/scraping/get_token.py' to update your token) {url}")
            raise aiohttp.ClientError
        elif res.status == 403:
            log(f"ERROR 403: Forbidden error (your IP '{get_ip()}' might be blocked) {url}")
            raise aiohttp.ClientError
        else:
            log(f"ERROR {res.status}: {url}")
            raise aiohttp.ClientError
        
async def get_responses(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)