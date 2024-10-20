#learn beautifulsoup
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import url_beautifulsoup1

from bs4 import BeautifulSoup
import requests
import re

url = url_beautifulsoup1
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
h3_elements = doc.find_all('h3')
prices = doc.find_all('p',class_='price-current')
names = [h3 for h3 in h3_elements if h3.find_parent(class_='content')]


for h3 in prices:
    clean_price = h3.text.replace('\n','').strip()
    numeric_part = re.sub(r'[^\d.]', '', clean_price)
    float_price = float(numeric_part.replace('.', ''))
    print(float_price)