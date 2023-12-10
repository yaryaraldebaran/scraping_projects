from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains
# setup driver browser
opsi = webdriver.ChromeOptions()
# opsi.add_argument('--headless')
servis = Service('./chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=servis, options=opsi)

# setup link dan browser

base_url= "https://www.olx.co.id/bandung-kota_g4000018/properti_c88"

driver.set_window_size(1920,1080)
driver.get(base_url)
driver.save_screenshot("./homeolx.png")

# untuk scroll
rentang = 500
for i in range(1,10):
    time.sleep(0.5)
    akhir = rentang*i
    perintah = "window.scrollTo(0,"+str(akhir)+")"
    driver.execute_script(perintah)
    print("loading ke "+str(i))
    time.sleep(0.5)


# xpath = "//*[@data-aut-id="itemsList"]"
element = driver.find_element(By.XPATH,'//*[@data-aut-id="itemsList"]')
print (element.get_attribute)