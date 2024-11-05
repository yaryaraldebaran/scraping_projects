import sys
import csv
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import requests
import re
#get url 
from config import url_beautifulsoup2

opsi = webdriver.ChromeOptions()
# opsi.add_argument('--headless')
servis = Service('./drivers/chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

# setup link dan browser

base_url= url_beautifulsoup2

driver.set_window_size(1920,1080)
driver.get(base_url)
wait = WebDriverWait(driver, 120)

with open('output_bs4.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['event name','event date','event_venue'])
    for page in range(6):
        element_current_page = wait.until(EC.presence_of_element_located((By.XPATH, "(//a[@class='paginate_button current'])[1]")))

        print("page :",element_current_page.text)
        element =  wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class ='paginate_button next'])[2]")))
        print("element found!")
        page_source = driver.page_source
        doc = BeautifulSoup(page_source,"html.parser")
        items = doc.find('table',id='DataTables_Table_0').find_all('tr')
        for item in items :
            list_info = item.find('div', class_='list-info')        
            if list_info:
                event_name = list_info.find('a', class_='list-view-title')
                event_date = list_info.find('div',class_='list-view-date')
                event_venue = list_info.find('div',class_='list-view-venue')
                if event_name:
                    writer.writerow([event_name.text, event_date.text, event_venue.text])
                else:
                    print("No event name found in 'list-view-detail'.")
            else:
                print("No 'list-info' found in this item.")
        
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        driver.implicitly_wait(10)
        
        try:
            element.click()
        except ElementClickInterceptedException:
            print("element tidak bisa diklik")
    input("Press Enter to close the browser...")