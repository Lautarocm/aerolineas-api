from scraper import get_responses
from parsers import parse_data, create_offers_list
from config import set_date, set_url
import asyncio
import json
import sys


async def main(origin, destination):
    dates = set_date()
    urls = set_url(origin, destination, dates)
    responses = await get_responses(urls)
    parsed_data = await parse_data(responses)
    final_offers = create_offers_list(parsed_data)
    return final_offers


final_offers = asyncio.run(main(sys.argv[1], sys.argv[2]))
print(json.dumps(final_offers))