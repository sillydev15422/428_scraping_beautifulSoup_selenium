import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import requests
from importlib import reload
import time


import csv

with open('inspirational_quotes.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    data = []
    for row in csv_reader:
        if line_count == 0:
            print(f"")
            line_count += 1
        else:
            data = {}
            data[line_count] = f'{row[0]}{row[1]}'
            print(data[line_count])
            line_count += 1
