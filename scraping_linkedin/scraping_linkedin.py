from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from utils_linkedin import LinkedInUtils



service = Service(executable_path="scraping_projects/drivers/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
driver.set_window_size(1920,1080)
linkedin_utils = LinkedInUtils(driver=driver)
actions = ActionChains(driver)

url = "https://www.linkedin.com/"
email ="kiranadewa97@gmail.com"
password = "kiranadewi97"
xpath_username = "//input[@id='session_key']"
xpath_password = "//input[@id='session_password']"
xpath_button_login = "//button[@type='submit']"
xpath_field_search = "//input[@class='search-global-typeahead__input']"
keyword_to_search = "talent acquisition specialist"
xpath_search_res = "//div[@id='triggered-expanded-ember10']/*"
xpath_search_click = "(//div[@class='ivm-image-view-model    search-global-typeahead-hit__image'])[1]"
xpath_pekerjaan_filter = "//button[contains(@class,'artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2') and (text()='Pekerjaan' or text()='Jobs')]"
xpath_job_cards = "//div[contains(@class,'job-card-container relative job-card-list')]"
xpath_job_01 = "(//div[contains(@class,'job-card-container relative job-card-list')])[5]"
driver.get(url)

element_username = driver.find_element(By.XPATH,xpath_username)
element_username.send_keys(email)
element_password = driver.find_element(By.XPATH,xpath_password)
element_password.send_keys(password)
element_button_login = driver.find_element(By.XPATH,xpath_button_login)
element_button_login.click()
element_search_field = driver.find_element(By.XPATH,xpath_field_search)
element_search_field.click()
element_search_field.send_keys(keyword_to_search)
driver.implicitly_wait(10)
element_search_res = driver.find_element(By.XPATH,xpath_search_click)
element_search_res.click()
element_filter_job_btn = driver.find_element(By.XPATH,xpath_pekerjaan_filter)
element_filter_job_btn.click()
element_job_1 = driver.find_element(By.XPATH,xpath_job_01)
element_job_1.click()
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'job-card-container relative job-card-list')])[5]"))
)

# Click the element
element.click()

print("element_job_1 clicked")
time.sleep(5)

# element_job_cards = driver.find_elements(By.XPATH,xpath_job_cards)
# print(len(element_job_cards))
time.sleep(5)

