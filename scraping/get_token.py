from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
import os
from utilities import get_script_directory as dir

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--headless')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://www.aerolineas.com.ar/")

url = "https://api.aerolineas.com.ar/v1/catalog/cabins"

current_dir = dir(__file__)
token_dir = os.path.join(current_dir, "token.txt")

for request in driver.requests:
    if url in request.url:
        with open(token_dir, "w") as file:
            file.write(request.headers["authorization"])