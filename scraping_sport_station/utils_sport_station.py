from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

class SportStatUtils:
    def __init__(self,driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def scroll_laman(self,limit):
        for i in range(1,limit):
            akhir = 300 * i 
            perintah = "window.scrollTo(0,"+str(akhir)+")"
            self.driver.execute_script(perintah)
            print("loading ke-"+str(i))
            time.sleep(1)
    
    def click_next_page(self):
        element_present = EC.presence_of_element_located((By.CLASS_NAME, "//li[@class='nextPage']"))
        WebDriverWait(self.driver, 30).until(element_present)
        self.driver.click()
    
    def zoom_in_out(self,zoom_size):
        self.driver.execute_script(f"document.body.style.zoom='{zoom_size}%'")

    def click_element_by_xpath(self,xpath):
        try:
            self.driver.implicitly_wait(10)
            element = self.driver.find_element(By.XPATH,xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except (NoSuchElementException, ElementClickInterceptedException):
            print(f"element {xpath} not found")
            print(ElementClickInterceptedException)
    
    def go_to_link_by_xpath(self,xpath):
        try:
            self.driver.implicitly_wait(10)
            element = self.driver.find_element(By.XPATH,xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.driver.get(element.get_attribute('href'))
        except (NoSuchElementException, ElementClickInterceptedException):
            print(f"element {xpath} not found")
            print(ElementClickInterceptedException)
            
    def verify_element_by_xpath(self,xpath):
        is_element_present = False
        try:
            self.driver.implicitly_wait(10)
            element = self.driver.find_element(By.XPATH,xpath)
            is_element_present = True
        except NoSuchElementException:
            print(f"element {xpath} not found")
            is_element_present = False
        return is_element_present

                
        # print(len(product_list))

