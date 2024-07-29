#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from collections import OrderedDict
import sys
import html5lib

# CBRF site
cbrf_url='https://www.cbr.ru/'

# Define a function that retrieves information about currency.
# a dictionary form.
def extract_data_currency(currency_html):
    divs = currency_html.select('div', class_='col-md-2.col-xs-9')
    rate=[]
    for div in divs:
        content = div.text.strip()
        css_class = div.get('class')
        rate.append(content)
    return rate[:-2]


# Define a function that retrieves all the currencies.
def get_currencies_data(page_url):
    try:
        page = requests.get(page_url)
    except requests.exceptions.Timeout:
        print("The request timed out!")
        sys.exit(1)
    else:    
        if page.status_code == 200:
            pageParsed = BeautifulSoup(page.content, 'html5lib')
            currencys_html_page = pageParsed.find_all('div', {'class': "main-indicator_rate"})
            res = [extract_data_currency(currency_html) for currency_html in currencys_html_page]
            return res 
        else:
            print("Page was not parsed.")
            sys.exit(1)


def currencies():
    # Retrieve data from the first page.
    data = get_currencies_data(cbrf_url)
    return data

