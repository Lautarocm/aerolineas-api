from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
from utilities import get_script_directory as directory

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get('https://www.aerolineas.com.ar/')

token = driver.execute_script('return window.__ACCESS_TOKEN__;')

current_dir = directory(__file__)
token_dir = os.path.join(current_dir, "token.txt")

with open(token_dir, "w") as file:
    file.write(f"Bearer {token}")