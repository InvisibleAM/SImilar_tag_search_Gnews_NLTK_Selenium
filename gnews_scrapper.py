# !pip install selenium
# !pip install webdriver_manager
# !apt install chromium-chromedriver

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from io import BytesIO

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

import warnings
warnings.filterwarnings('ignore')

def get_single_element(driver, xpath):
    '''
    Get single element by xpath in Selenium
    '''
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    return driver.find_element("xpath" , xpath)


def get_multiple_element(driver, xpath):
    '''
    Get multiple element by xpath in Selenium
    '''

    time.sleep(20)
    #WebDriverWait(driver, 10).until(
        #EC.presence_of_all_elements_located((By.XPATH, xpath)))
    return driver.find_elements(By.XPATH , xpath)


def get_text(driver, element):
    '''
    Extract text of an element in Selenium
    '''
    return driver.execute_script("return arguments[0].innerText;", element)


def get_content(xpath):
    '''
    Extract text of an element that is selected by xpath in Selenium
    '''
    return get_text(get_single_element(xpath))


def get_soup(url, verify=True):
    page = requests.get(url, verify=verify)
    soup = BeautifulSoup(page.content)
    return soup

def load_driver():
    op = webdriver.ChromeOptions()
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', options=op)
    return driver

def scrape_data(query):
        driver = load_driver()

        # Find query
        url = "https://www.google.com/search?q={}&hl=en-IN&gl=IN&source=lnms&tbm=nws".format(query)

        driver.get(url=url)

        xpath_next = '//*[@id="pnnext"]'
        xpath_div = '//*[@id="rso"]/div/div/div'

        df = pd.DataFrame({
            "media": [],
            "Title": [],
            "subtitle": [],
            "time": [],
            "link": []
        })

        while True and len(df)<400:
            driver.get(url)
            divs = get_multiple_element(driver, xpath_div)

            #divs = driver.find_elements(By.XPATH , xpath_div)
            for div in divs:
                text = div.text.split("\n")
                link = div.find_element(By.TAG_NAME,'a').get_attribute('href')
                data = {
                    "media": text[0],
                    "Title": text[1],
                    "subtitle": text[2],
                    "time": text[-1],
                    "link": link
                }
                df = df.append(data, ignore_index=True)
            try:
                url = get_single_element(driver, xpath_next).get_attribute("href")
            except:
                break

        driver.close()
        return df

scrape_data('Indian Agriculture')

driver = load_driver()

        # Find query
        url = "https://www.google.com/search?q={Indian Agriculture}&hl=en-IN&gl=IN&source=lnms&tbm=nws"

        driver.get(url=url)

        xpath_next = '//*[@id="pnnext"]'
        xpath_div = '//*[@id="rso"]/div/div/div'

        df = pd.DataFrame({
            "media": [],
            "Title": [],
            "subtitle": [],
            "time": [],
            "link": []
        })

        while True and len(df)<400:
            driver.get(url)
            divs = get_multiple_element(driver, xpath_div)

            #divs = driver.find_elements(By.XPATH , xpath_div)
            for div in divs:
                text = div.text.split("\n")
                link = div.find_element(By.TAG_NAME,'a').get_attribute('href')
                data = {
                    "media": text[0],
                    "Title": text[1],
                    "subtitle": text[2],
                    "time": text[-1],
                    "link": link
                }
                df = df.append(data, ignore_index=True)
            try:
                url = get_single_element(driver, xpath_next).get_attribute("href")
            except:
                break

        driver.close()
        df

df.to_excel('Indian Agricultre.xlsx', index=False)

df2 = pd.read_excel('Indian Agricultre.xlsx')
df2

df2["merged"]= df2["Title"] + df2["subtitle"]
print("\n".join(df2["merged"].to_list()))

with open('Indian AG.txt', 'w') as f:
    f.write("\n".join(df2["merged"].to_list()))

