import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from importlib import reload
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import csv
from datetime import datetime
import numpy as np
import sched

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 10)
browser = webdriver.Chrome()


# class Main():
# def __init__(self):

# self.getData()
# self.setup_method()
# self.teardown_method()
# self.wait_for_window()

def getData(scheduler):
    scheduler.enter(200, 1, getData, (scheduler,))
    print('123')
    with open('inspirational_quotes.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        datas = []
        for row in csv_reader:
            if line_count == 0:
                print(f"")
                line_count += 1
            else:
                data = {}
                data[line_count] = f'{row[0]}{row[1]}'
                line_count += 1
                datas.append(data)
        # print(datas)

    browser.get('https://www.bwsg.at/overview/?status_immediately=true&has_apartment=true&rent_exclusive=true&price-min=0&price-max=700&living_space-min=40&living_space-max=150&status_in_planning=false&status_under_contruction=false')

    # print('123')
    soup = BeautifulSoup(browser.page_source, "html.parser")
    quotes = []
    comQuotes = []
    result = soup.find_all(
        "div", {"class": "content-grid"})
    date = datetime.now()
    for item in result:
        quote = {}
        comQuoote = {}
        quote['address'] = item.h6.text
        quote['district'] = item.p.text
        quote['size'] = item.ul.text
        quote['rent'] = item.p.text
        quote['date'] = date
        quotes.append(quote)
        comQuoote['address'] = item.h6.text
        comQuoote['district'] = item.p.text
        comQuotes.append(comQuoote)
    diff = np.setdiff1d(quotes, datas)
    print('hihihi', diff)
    if diff:
        with open("inspirational_quotes.csv", "a")as infile:
            wrier = csv.writer(infile)
    print('hihihihihihihihihihihihihihihihihih')
    filename = 'inspirational_quotes.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(
            f, ['address', 'district', 'size', 'rent', 'date'])
        w.writeheader()
        for quote in quotes:
            print(quote)
            w.writerow(quote)


driver = webdriver.Chrome('./chromedriver')
driver.get("https://genossenschaften.immo/?cost=700&district=wien-1-innere-stadt&district=wien-2-leopoldstadt&district=wien-3-landstrasse&district=wien-4-wieden&district=wien-5-margareten&district=wien-6-mariahilf&district =wien-7-neubau&district=wien-8-josefstadt&district=wien-9-alsergrund&district=wien-10-favoriten&district=wien-11-simmering&district=wien-12-meidling&genossenschaft=bwsg&own_funds=15000&size=40")

time.sleep(10)
# print('driver.title')
# driver.set_window_size(945, 744)
# driver.find_element(
#     By.XPATH, '//*[@id="residence-teasers"]/div[1]/div').click()
print('123')
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# print(driver.current_url)
# driver.close()


# a = Main()
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(5, 1, getData, (my_scheduler,))
my_scheduler.run()
# a.getData()
