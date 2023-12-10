# to be added

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select

def scroll_with_increment(driver, step=500, interval=1.5):
    initial_scroll_position = driver.execute_script("return window.scrollY;")    
    while True:
        new_scroll_position = initial_scroll_position + step
        driver.execute_script(f"window.scrollTo(0, {new_scroll_position});")
        time.sleep(interval)
        initial_scroll_position = new_scroll_position
        if new_scroll_position >= driver.execute_script("return document.body.scrollHeight - window.innerHeight;"):
            break

def verify_and_click_element(driver, by, value):
    try:
        element = driver.find_element(by, value)
        if element.is_displayed() and element.is_enabled():
            element.click()
            return True
    except NoSuchElementException:
        return False
    

def verify_and_type_element(driver, by, value, text):
    try:
        element = driver.find_element(by, value)
        if element.is_displayed() and element.is_enabled():
            try:
                element.clear()  # Clear any existing text
                element.send_keys(text)
                return True
            except ElementNotInteractableException:
                return False
    except NoSuchElementException:
        return False


def verify_and_click_dropdown_option(driver, dropdown_by, dropdown_value, option_text):
    try:
        dropdown = Select(driver.find_element(dropdown_by, dropdown_value))
        if dropdown.first_selected_option.text != option_text:
            dropdown.select_by_visible_text(option_text)
            return True
    except NoSuchElementException:
        return False


def verify_and_get_element_text(driver, by, value):
    try:
        element = driver.find_element(by, value)
        if element.is_displayed():
            return element.text
    except NoSuchElementException:
        return None


def verify_and_click_radio_button(driver, by, value):
    try:
        radio_button = driver.find_element(by, value)
        if radio_button.is_displayed() and radio_button.is_enabled():
            if not radio_button.is_selected():
                radio_button.click()
                return True
    except NoSuchElementException:
        return False