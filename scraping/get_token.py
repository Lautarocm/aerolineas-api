from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--headless')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://www.aerolineas.com.ar/")

url = "https://api.aerolineas.com.ar/v1/catalog/cabins"

for request in driver.requests:
    if url in request.url:
        with open("C:/Users/Usuario/Documents/proyectos/aerolineas-api/scraping/token.txt", "w") as file:
            file.write(request.headers["authorization"])