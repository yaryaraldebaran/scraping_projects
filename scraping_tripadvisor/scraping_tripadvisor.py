from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utils_tripadv import TripAdvUtils
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
utils_trip = TripAdvUtils(driver)
#urlk
url = "https://www.tripadvisor.com/"
xpath_restaurants_btn = "//a[text()='Restaurants' and @href='/Restaurants']"
xpath_search_field = "//input[@title='Search']"
xpath_to_all_results = "//div[contains(text(),'See all results')]"
xpath_result_title = "//div[@class='result-title']"
xpath_result_rating_count = "//a[@class='review_count']"
xpath_result_address = "//div[@class='address-text']"
xpath_mention_block = "//div[@class='review-mention-block']"


xpath_restaurant_name ="//h1[@class='HjBfq']"
xpath_restaurant_rating = "//span[@class='ZDEqb']"
xpath_restaurant_review_count = "//a[@class='IcelI']"
xpath_restaurant_details = "//div[@class='BMlpu']/div"
xpath_restaurant_gmaps_address = "(//div[@class='kDZhm IdiaP']/*)[2]"
xpath_restaurant_website = "(//a[@class='YnKZo Ci Wc _S C FPPgD'])[2]"
xpath_restaurant_phone = "//div[@class='IdiaP']/*/*/span[@class='yEWoV']"

list_restaurant = []
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
for x,elmn in enumerate(element_result_title):#enumerate(element_result_title):
    element_place = driver.find_element(By.XPATH,f"(//div[@class='result-title'])[{x+1}]")
    element_place.click()
    time.sleep(5)
    
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)
    driver.implicitly_wait(10)
    element_restaurant_name = driver.find_element(By.XPATH,xpath_restaurant_name).text
    element_restaurant_rating = driver.find_element(By.XPATH,xpath_restaurant_rating).text
    element_restaurant_review_count = driver.find_element(By.XPATH,xpath_restaurant_review_count).text
    element_restaurant_details = driver.find_elements(By.XPATH,xpath_restaurant_details)
    element_restaurant_gmaps_address = driver.find_element(By.XPATH,xpath_restaurant_gmaps_address).text
    if (utils_trip.verify_element_by_xpath(xpath_restaurant_website)):
        element_restaurant_website = driver.find_element(By.XPATH,xpath_restaurant_website).get_attribute('href')
    if (utils_trip.verify_element_by_xpath(xpath_restaurant_phone)):
        element_restaurant_phone = driver.find_element(By.XPATH,xpath_restaurant_phone).text
    restaurant_data = {
        "element_restaurant_name":element_restaurant_name,
        "element_restaurant_rating":element_restaurant_rating,
        "element_restaurant_review_count":element_restaurant_review_count,
        "element_restaurant_gmaps_address":element_restaurant_gmaps_address,
        "element_restaurant_website":element_restaurant_website,
        "element_restaurant_phone":element_restaurant_phone
    }
    list_restaurant.append(restaurant_data)

    # print(element_restaurant_details.get_attribute("innerHTML"))
    # print(element_restaurant_name)
    # print(element_restaurant_rating)
    # print(element_restaurant_review_count)
    # print(element_restaurant_gmaps_address)
    # print(element_restaurant_website)
    # print(element_restaurant_phone)

    print("================")
    driver.close()
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



df = pd.DataFrame.from_dict(list_restaurant)
df.to_csv('scraping_projects/scraping_tripadvisor/tripadvisor.csv')
driver.close()

