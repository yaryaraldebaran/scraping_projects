from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
from utils_sociolla import *
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils_sociolla import SociollaUtils
from selenium.common.exceptions import StaleElementReferenceException


service = Service(executable_path="scraping_projects/drivers/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)
soc_utils = SociollaUtils(driver=driver)
driver.set_window_size(1920,1080)
driver.get("https://www.sociolla.com/140-skin-care")
rentang = 500

wait = WebDriverWait(driver, 10)

content = driver.page_source
data = BeautifulSoup(content,'html.parser')
products_part = data.find_all('div',class_="product product--v3")
wait = WebDriverWait(driver,10)
if (soc_utils.verify_element_by_xpath("(//button[@class='ng-binding'])[1]")):
    notif_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@class='ng-binding'])[1]")))
    notif_btn.click()

list_prod = []
driver.implicitly_wait(10)

elements_prod = driver.find_elements(By.XPATH,"//a[@class='product__name']")
for page in range(1,2):
    element_next_page = driver.find_element(By.XPATH,"//a[@class='pagination-navigation glyphicon pagination-navigation-next']")
    element_next_page.click()
    time.sleep(3)
    for elmn, x in enumerate(elements_prod):
        print(elmn+1)
        element_click_init = driver.find_element(By.XPATH,f"(//a[@class='product__name'])[{elmn+1}]")
        product_name = element_click_init.text
        element_click = wait.until(EC.element_to_be_clickable((element_click_init)))
        element_click.click()
        time.sleep(5)
        driver.implicitly_wait(10)
        if (soc_utils.verify_element_by_xpath("//p[text()='Chat with Us ']")and soc_utils.verify_element_by_xpath("//button[@class='button-quick-tour']")):
            element_chat_us = driver.find_element(By.XPATH,"//p[text()='Chat with Us ']")
            element_ok = driver.find_element(By.XPATH,"//button[@class='button-quick-tour']")
            if(element_chat_us.is_displayed() and element_ok.is_enabled()):
                element_ok.click()
            else:
                pass
        else:
            pass
        if (soc_utils.verify_element_by_xpath("//li[@class='rating']")):
            rating = driver.find_element(By.XPATH,"//li[@class='rating']").text
            product_rating = rating
            print("rating : "+rating)
        
        if (soc_utils.verify_element_by_xpath("//li[@class='pricing hasdiscount']/*") == True):
            is_varian = driver.find_elements(By.XPATH,"//li[@class='pricing hasdiscount']/*")
            print(len(is_varian))
            #jika is_varian = 1 maka harga = is_varian.text
        if (soc_utils.verify_element_by_xpath("(//li[@class='pricing hasdiscount'])[1]/*[@class='ori']")):
            harga =[]
            harga_awal = driver.find_element(By.XPATH,"(//li[@class='pricing hasdiscount'])[1]/*[@class='ori']").text
            harga_post_disc=''
            if (soc_utils.verify_element_by_xpath("(//li[@class='pricing hasdiscount'])[1]/*[@class='after']")):
                harga_post_disc = driver.find_element(By.XPATH,"(//li[@class='pricing hasdiscount'])[1]/*[@class='after']").text    
            print("harga awal "+harga_awal)
            print("harga akhir "+harga_post_disc)
            harga.append(harga_awal)
            harga.append(harga_post_disc)
        product_price= harga


        # product_desc_tab = driver.find_element(By.XPATH,"//a[@title='INGREDIENTS']")
        if (soc_utils.verify_element_by_xpath("//a[@title='INGREDIENTS']")==True):
        # if (product_desc_tab.is_displayed()):
            product_desc_tab = driver.find_element(By.XPATH,"//a[@title='INGREDIENTS']")
            product_desc_tab.click()
            driver.implicitly_wait(10)
            element_present = EC.presence_of_element_located((By.XPATH,"//div[@id='ingredients']/*"))
            WebDriverWait(driver, 30).until(element_present)
            product_desc_text = driver.find_elements(By.XPATH,"//div[@id='ingredients']/*")
            driver.execute_script("arguments[0].scrollIntoView();", product_desc_text[0])
            ingredients = []
            for txt in product_desc_text:
                ingredients.append(txt.text)
        print("===============================")
        driver.implicitly_wait(10)
        product_name,product_rating,product_price,ingredients
        prod = {
            "product_name" : product_name,
            "product_rating" : product_rating,
            "product_price" : product_price,
            "ingredients" : ingredients
        }
        list_prod.append(prod)
        driver.back()
        time.sleep(5)
        

time.sleep(2)
driver.quit()
df = pd.DataFrame.from_dict(list_prod)
df.to_csv('scraping_projects/scraping_sociolla')
