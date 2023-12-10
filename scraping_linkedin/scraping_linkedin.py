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


url = "https://www.linkedin.com/"
email ="kiranadewa97@gmail.com"
password = "kiranadewi97"
xpath_username = "//input[@id='session_key']"
xpath_password = "//input[@id='session_password']"
xpath_button_login = "//button[@type='submit']"
driver.get(url)

element_username = driver.find_element(By.XPATH,xpath_username)
element_username.send_keys(email)
element_password = driver.find_element(By.XPATH,xpath_password)
element_password.send_keys(password)
element_button_login = driver.find_element(By.XPATH,xpath_button_login)
element_button_login.click()

time.sleep(5)