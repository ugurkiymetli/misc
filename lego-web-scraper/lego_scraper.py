from bs4 import BeautifulSoup
import requests
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


url = 'https://lego.storeturkey.com.tr/yeni-urunler?stock=1'

# create a new instance of the Firefox driver
driver = webdriver.Chrome()

# navigate to the URL you want to scrape
driver.get(url)

# scroll to the bottom of the page
body = driver.find_element(By.TAG_NAME, 'body')
body_height = int(body.get_attribute('scrollHeight'))

print(body_height)

scroll_step = 1000  # adjust this value to suit your needs
for i in range(0, 35000, scroll_step):
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(1)  # wait for the page to load

# get the HTML of the page
html = driver.page_source

# close the driver
driver.quit()

# response = requests.get(url)
soup = BeautifulSoup(html, 'html.parser')


products_divs = soup.findAll('div', id=re.compile('^1003-product-detail-'))

for product_div in products_divs:
    name = product_div.find("span", itemprop="name").get('content')
    price = product_div.find(
        "div", class_="vitrin-current-price currentPrice").get_text(strip=True).replace('\nTL', '')

    print(name, '  ', price)
