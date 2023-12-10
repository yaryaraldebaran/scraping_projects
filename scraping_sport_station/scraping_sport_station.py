from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
from utils_sport_station import SportStatUtils 
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException



service = Service(executable_path="scraping_projects/drivers/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)
sportst_utils = SportStatUtils(driver=driver)
wait = WebDriverWait(driver, 10)
driver.set_window_size(1920,1080)
#urlk
url = "https://www.sportsstation.id/men-footwear.html"

driver.get(url)
list_prod_scrape=[]
sportst_utils.zoom_in_out(70)
driver.implicitly_wait(10)
element_prods = driver.find_elements(By.XPATH,"//a[@class='product-details']")
for product, x in enumerate(element_prods):
    sportst_utils.go_to_link_by_xpath(f"(//a[@class='product-details'])[{product+1}]")
    rentang = 500
    
    sizes = driver.find_elements(By.XPATH,"//section[@class='product-attr_item'][1]/ul/li[@class = 'attr-item active' or @class='attr-item']")
    prod_brand = driver.find_element(By.XPATH,"//span[@class='brand']").text
    prod_name = driver.find_element(By.XPATH,"//h1[@class='product-name']").text
    prod_price = driver.find_element(By.XPATH,"//span[@class='current-price']").text
    prod_url = driver.current_url
    prod_pict = driver.find_element(By.XPATH,"(//img[@class='el-image__inner el-image__preview'])[1]").get_attribute('src')
    daftar_size =[]
    for size in sizes:
        daftar_size.append(size.text)
    print("daftar ukuran : ",daftar_size)
    prod_data = {
        "product_brand" : prod_brand,
        "product_name" : prod_name,
        "product_price" : prod_price,
        "availabel_sizes":daftar_size,
        "prod_url" : prod_url,
        "prod_pict" : prod_pict
    }
    list_prod_scrape.append(prod_data)
    time.sleep(3)
    driver.back()
driver.close()

df = pd.DataFrame.from_dict(list_prod_scrape)
df.to_csv('scraping_projects/scraping_sport_station/output_file/output_sport_station.csv')
