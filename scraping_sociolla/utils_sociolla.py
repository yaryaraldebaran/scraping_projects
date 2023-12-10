from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time

class SociollaUtils:
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

                
        # print(len(product_list))


# for product in products_part:    
#     product_name = product.find('a',class_="product__name").get_text()
#     product_brand = product.find('a',class_="product__brand").get_text()
#     product_price = product.find('h2',class_="product__price").get_text()
#     dict_prod = {
#     "product_brand" : product_brand,
#     "product_name" : product_name,
#     "product_price": product_price
#     }
#     list_dict.append(dict_prod)    
# df = pd.DataFrame.from_dict(list_dict)
# df.to_csv('./output_csv/sociolla.csv')

# print(data)
# driver.find_elements(By.XPATH,"")


# for elmn,x in enumerate(elements_prod):
#     element_click = wait.until(EC.element_to_be_clickable((elements_prod[elmn])))
#     if (element_click.is_enabled()):
#         print(f"element {elmn} is clickable")
#         try:
#             driver.implicitly_wait(10)
#             element_click.click()
#         except exceptions.StaleElementReferenceException as e:
#             print("Element is not clickable")
#     driver.back()

# rating = driver.find_element(By.XPATH,"//li[@class='rating']").text
# print("rating : "+rating)

# harga_awal = driver.find_element(By.XPATH,"(//li[@class='pricing hasdiscount'])[1]/*[@class='ori']").text
# harga_post_disc = driver.find_element(By.XPATH,"(//li[@class='pricing hasdiscount'])[1]/*[@class='after']").text
# print("harga awal "+harga_awal)
# print("harga akhir "+harga_post_disc)

# element_present = EC.presence_of_element_located((By.XPATH,"//div[@id='ingredients']/*/p"))
# WebDriverWait(driver, 30).until(element_present)
# product_desc_text = driver.find_elements(By.XPATH,"//div[@id='ingredients']/*/p")
# driver.execute_script("arguments[0].scrollIntoView();", product_desc_text[0])
# for txt in product_desc_text:
#     print(txt.text)

    # if (element_click.is_enabled()):
    #     try:
    #         element_click.click()
    #         driver.back()
    #     except StaleElementReferenceException as e:
    #         print(e)
    #         driver.refresh()
