#!/usr/bin/env python
# coding: utf-8


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from collections import OrderedDict
import sys
import html5lib


# In[3]:


# Define a function that retrieves information about currency.
# a dictionary form.
def extract_data_quote(quote_html):
    divs = quote_html.select('div', class_='col-md-2.col-xs-9')
    rate=[]
    for div in divs:
        content = div.text.strip()
        css_class = div.get('class')
        rate.append(content)
    return rate[:-2]


# Define a function that retrieves all the quotes on a single page.
def get_quotes_data(page_url):
    try:
        page = requests.get(page_url)
    except requests.exceptions.Timeout:
        print("The request timed out!")
        sys.exit(1)
    else:    
        if page.status_code == 200:
            print(f"Page {page_url} parsing.")
            pageParsed = BeautifulSoup(page.content, 'html5lib')
            quotes_html_page = pageParsed.find_all('div', {'class': "main-indicator_rate"})
            res = [extract_data_quote(quote_html) for quote_html in quotes_html_page]
            return res 
        else:
            print("Page was not parsed.")
            sys.exit(1)

# CBRF site
cbrf_url='https://www.cbr.ru/'

def currencies():
    # Retrieve data from the first page.
    data = get_quotes_data(cbrf_url)
    return data

