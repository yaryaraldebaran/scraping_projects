from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains
from utils.util_web import *
# setup driver browser
opsi = webdriver.ChromeOptions()
servis = Service('./chromedriver_linux64/chromedriver')
opsi.add_argument('--headless')
driver = webdriver.Chrome(service=servis, options=opsi)
# setup link dan browser
base_url2= "https://www.airbnb.com/"
base_url="https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=2"

driver.set_window_size(1920,1080)
driver.get(base_url2)
scroll_with_increment(driver, interval=2)
card_elements = driver.find_elements(By.CLASS_NAME,"c4mnd7m")
location = driver.find_elements(By.CLASS_NAME,'t1jojoys')
place_name = driver.find_elements(By.CLASS_NAME,'fb4nyux')
price = driver.find_elements(By.CLASS_NAME,'pquyp1l')
rating = driver.find_elements(By.CLASS_NAME,'r1dxllyb')
for card in rating:
    print(card.text)
    print("===")
driver.close()