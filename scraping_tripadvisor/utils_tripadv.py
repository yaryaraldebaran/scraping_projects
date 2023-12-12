from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time

class TripAdvUtils:
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
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'pagination-navigation glyphicon pagination-navigation-next'))
        WebDriverWait(self.driver, 30).until(element_present)
        self.driver.click()

    def click_element(self,element_click):
        self.wait.until(EC.element_to_be_clickable((element_click)))
        if (element_click.is_enabled()):
            try:
                element_click.click()
            except Exception:
                print("Element is not clickable")

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
