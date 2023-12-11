from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException



service = Service(executable_path="scraping_projects/drivers/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
driver.set_window_size(1920,1080)
#urlk
url = "https://www.tripadvisor.com/"
xpath_restaurants_btn = "//a[text()='Restaurants' and @href='/Restaurants']"
xpath_search_field = "//input[@title='Search']"
xpath_to_all_results = "//div[contains(text(),'See all results')]"
xpath_result_title = "//div[@class='result-title']"
xpath_result_rating_count = "//a[@class='review_count']"
xpath_result_address = "//div[@class='address-text']"
xpath_mention_block = "//div[@class='review-mention-block']"
driver.get(url)
time.sleep(5)
element_restaurant_btn = driver.find_element(By.XPATH,xpath_restaurants_btn)
element_restaurant_btn.click()
driver.implicitly_wait(10)
element_search_field = driver.find_element(By.XPATH,xpath_search_field)
element_search_field.send_keys("Tangerang")
driver.implicitly_wait(10)
element_to_all_results = driver.find_element(By.XPATH,xpath_to_all_results)
element_to_all_results.click()
driver.implicitly_wait(10)

element_result_title = driver.find_elements(By.XPATH,xpath_result_title)
for x,place in enumerate(element_result_title):
    element_place = driver.find_element(By.XPATH,f"(//div[@class='result-title'])[{x+1}]")
    element_place.click()
    time.sleep(5)
    # driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    # Switch back to the first tab (index 0)
    driver.switch_to.window(driver.window_handles[0])



    # print("======================================")
    # element_result_rating_count = driver.find_element(By.XPATH,xpath_result_rating_count)
    # element_result_address = driver.find_element(By.XPATH,xpath_result_address)
    # element_mention_block = driver.find_element(By.XPATH,xpath_mention_block)
    # print(place.text)
    # print(element_result_rating_count.text)
    # print(element_result_address.text)
    # print(element_mention_block.text)
    # print("======================================")










driver.close()

