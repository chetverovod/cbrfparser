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
            print(f"Page {page_url} lparsing.")
            pageParsed = BeautifulSoup(page.content, 'html5lib')
            quotes_html_page = pageParsed.find_all('div', {'class': "main-indicator_rate"})
            res = [extract_data_quote(quote_html) for quote_html in quotes_html_page]
            return res 
        else:
            print("Page was not parsed.")
            sys.exit(1)


# Retrieve data from the first page.
data = get_quotes_data('https://www.cbr.ru/')

for r in data:
    print('Валюта:', r[0], " Вчера:", r[1], " Сегодня:", r[2])



"""
# Retrieve data from all pages.
# for i in range(2, 101):
for i in range(2, 3):
    print(i)
    url = f'https://www.goodreads.com/quotes?page={i}'
    data_current_page = get_quotes_data(url)
    if data_current_page is None:
        continue
    data = data + data_current_page

data_df = pd.DataFrame.from_dict(data)
for i, row in data_df.iterrows():
    if row['tags'] is None:
        data_df = data_df.drop(i)

# Produce the data in a JSON format.
data_df.to_json('quotes.jsonl', orient="records", lines=True,
                force_ascii=False)
"""
