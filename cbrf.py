"""Module provides functions for metal, currencies courses reading from site
https://www.cbr.ru/."""

import sys

import requests
from bs4 import BeautifulSoup
from lxml import etree

# Timeout for site access.
TIMEOUT = 10

# CBRF site pages.
CBRF_URL = "https://www.cbr.ru/"
CBRF_INDICATORS_URL = "https://www.cbr.ru/key-indicators/"

cn = ["name_ru", "name", "yesterday_rate", "today_rate"]


def get_currencies_data(page_url) -> dict:
    """
    Function retrieves the currencies courses.

    returns data in dictionary form.
    """

    try:
        page = requests.get(page_url, timeout=TIMEOUT)
    except requests.exceptions.Timeout as exc:
        msg = "The request timed out!"
        raise ValueError(msg) from exc

    if page.status_code == 200:
        page_parsed = BeautifulSoup(page.content, 'html5lib')
        dom = etree.HTML(str(page_parsed))

        currency_locators = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[2]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[2]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[2]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[2]/td[3]'
        }
        cny = {}
        for key, locator in currency_locators.items():
            cny[key] = (dom.xpath(locator)[0].text).strip()

        currency_locators = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[3]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[3]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[3]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[3]/td[3]'
        }
        usd = {}
        for key, locator in currency_locators.items():
            usd[key] = (dom.xpath(locator)[0].text).strip()

        currency_locators = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[4]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[4]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[4]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[4] \
                /div/div/table/tbody/tr[4]/td[3]'
        }
        eur = {}
        for key, locator in currency_locators.items():
            eur[key] = (dom.xpath(locator)[0].text).strip()

        res = [cny, usd, eur]
        return res
    else:
        msg = "Page was not parsed."
        raise ValueError(msg)


def currencies() -> dict:
    """
    Function retrieves information about currency.

    returns data in dictionary form.
    """

    # Retrieve data from the first page.
    data = get_currencies_data(CBRF_INDICATORS_URL)
    return data


def get_metals_data(page_url) -> list:
    """
    Function that retrieves prices of metals.

    returns data in list of dictionary form.
    """

    try:
        page = requests.get(page_url, timeout=TIMEOUT)
    except requests.exceptions.Timeout as exc:
        msg = "The request timed out!"
        raise ValueError(msg) from exc

    if page.status_code == 200:
        page_parsed = BeautifulSoup(page.content, 'html5lib')
        dom = etree.HTML(str(page_parsed))

        metal_locators = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[2]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[2]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[2]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[2]/td[3]'
        }
        aurum = {}
        for key, locator in metal_locators.items():
            aurum[key] = (dom.xpath(locator)[0].text).strip()

        metal_locators = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[3]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[3]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[3]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[3]/td[3]'
        }
        argentum = {}
        for key, locator in metal_locators.items():
            argentum[key] = (dom.xpath(locator)[0].text).strip()

        metal_locators = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[4]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[4]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[4]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[4]/td[3]'
        }
        platinum = {}
        for key, locator in metal_locators.items():
            platinum[key] = (dom.xpath(locator)[0].text).strip()

        metal_locators = {
            cn[0]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[5]/td[1]/div/div[1]',
            cn[1]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[5]/td[1]/div/div[2]',
            cn[2]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[5]/td[2]',
            cn[3]: '//*[@id="content"]/div/div/div/div[2]/div[2]/div[6] \
                /div/div/table/tbody/tr[5]/td[3]'
        }
        palladium = {}
        for key, locator in metal_locators.items():
            palladium[key] = (dom.xpath(locator)[0].text).strip()

        res = [aurum, argentum, platinum, palladium]
        return res
    else:
        msg = "Page was not parsed."
        raise ValueError(msg)


def metals():
    """
    Function that retrieves information about metals.
    a dictionary form.
    """

    # Retrieve data from the first page.
    data = get_metals_data(CBRF_INDICATORS_URL)
    return data
