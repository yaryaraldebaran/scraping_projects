from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

class LinkedInUtils:
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