#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
# import pandas as pd
import json
# from collections import OrderedDict
import sys
import html5lib
from lxml import etree 

# CBRF site pages.
cbrf_url = 'https://www.cbr.ru/'
cbrf_indicators_url = 'https://www.cbr.ru/key-indicators/'

cn = ['name_ru', 'name', 'yesterday_rate', 'today_rate']


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
            dom = etree.HTML(str(pageParsed)) 

            curr = {
            cn[0]:'//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[2]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[2]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[2]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[2]/td[3]'
            }  
            cny = {}
            for k in curr.keys():
                cny[k] = (dom.xpath(curr[k])[0].text).strip()

            curr = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[3]/td[1]/div/div[1]', 
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[3]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[3]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[3]/td[3]'
            }  
            usd = {}
            for k in curr.keys():
                usd[k] = (dom.xpath(curr[k])[0].text).strip() 

            curr = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[4]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[4]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[4]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[4]/td[3]'
            }  
            eur = {}
            for k in curr.keys():
                eur[k] = (dom.xpath(curr[k])[0].text).strip() 
            
            res = [cny, usd, eur]
            return res 
        else:
            print("Page was not parsed.")
            sys.exit(1)


# Define a function that retrieves information about currency.
# a dictionary form.
def currencies():
    # Retrieve data from the first page.
    data = get_currencies_data(cbrf_indicators_url)
    return data


# Define a function that retrieves all the metals.
def get_metals_data(page_url):
    try:
        page = requests.get(page_url)
    except requests.exceptions.Timeout:
        print("The request timed out!")
        sys.exit(1)
    else:    
        if page.status_code == 200:
            pageParsed = BeautifulSoup(page.content, 'html5lib')
            dom = etree.HTML(str(pageParsed)) 

            metal = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[2]/td[1]/div/div[1]', 
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[2]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[2]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[2]/td[3]'
            }  
            Au={}
            for k in metal.keys():
                Au[k] = (dom.xpath(metal[k])[0].text).strip() 

            metal = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[3]/td[1]/div/div[1]', 
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[3]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[3]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[3]/td[3]'
            }  
            Ag={}
            for k in metal.keys():
                Ag[k] = (dom.xpath(metal[k])[0].text).strip() 

            metal = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[4]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[4]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[4]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[4]/td[3]'
            }  
            Pl={}
            for k in metal.keys():
                Pl[k] = (dom.xpath(metal[k])[0].text).strip() 
            
            metal = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[5]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[5]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[5]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[5]/td[3]'
            }  
            Pd={}
            for k in metal.keys():
                Pd[k] = (dom.xpath(metal[k])[0].text).strip() 

            res = [Au, Ag, Pl, Pd]
            return res 
        else:
            print("Page was not parsed.")
            sys.exit(1)


# Define a function that retrieves information about metals.
# a dictionary form.
def metals():
    # Retrieve data from the first page.
    data = get_metals_data(cbrf_indicators_url)
    return data

