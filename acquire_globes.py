from requests import get
from bs4 import BeautifulSoup
import os
import re

# get the year 
def get_year(url):
    headers = {'User-Agent':'Codeup Data Science Student'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    x = []
    for title in soup.title:
        x.append(title)
    return x


# get the category for each award
def get_category(url):
    headers = {'User-Agent':'Codeup Data Science Student'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    x = []
    for h2 in soup.find_all(class_='view-grouping-header'):
        x.append(h2.text)
    return x


# get the nominees for awards
def get_nominees(url):
    headers = {'User-Agent':'Codeup Data Science Student'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    x = []
    for h2 in soup.find_all(class_='primary-nominee'):
        x.append(re.sub(r'\s', ' ', h2.text))
    return x


# make a dictionary out of categories and nominees
def make_dict_from_page(url):
    headers = {'User-Agent':'Codeup Data Science Student'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    cat = get_category(url)
    nominee = get_nominees(url)
    return {'category': cat,
            'nominees': nominee
    }

# get multiple pages of data to then create a df
def get_nominations():
    urls = [
        "https://www.goldenglobes.com/winners-nominees/2019",
        "https://www.goldenglobes.com/winners-nominees/2019?page=1",
        "https://www.goldenglobes.com/winners-nominees/2018",
        "https://www.goldenglobes.com/winners-nominees/2018?page=1",
        "https://www.goldenglobes.com/winners-nominees/2017",
        "https://www.goldenglobes.com/winners-nominees/2017?page=1",
        "https://www.goldenglobes.com/winners-nominees/2016",
        "https://www.goldenglobes.com/winners-nominees/2016?page=1",
        "https://www.goldenglobes.com/winners-nominees/2015",
        "https://www.goldenglobes.com/winners-nominees/2015?page=1",
        "https://www.goldenglobes.com/winners-nominees/2014",
        "https://www.goldenglobes.com/winners-nominees/2014?page=1",
        "https://www.goldenglobes.com/winners-nominees/2013",
        "https://www.goldenglobes.com/winners-nominees/2013?page=1",
        "https://www.goldenglobes.com/winners-nominees/2012",
        "https://www.goldenglobes.com/winners-nominees/2012?page=1",
        "https://www.goldenglobes.com/winners-nominees/2011",
        "https://www.goldenglobes.com/winners-nominees/2011?page=1",
        "https://www.goldenglobes.com/winners-nominees/2010",
        "https://www.goldenglobes.com/winners-nominees/2010?page=1",
        "https://www.goldenglobes.com/winners-nominees/2009",
        "https://www.goldenglobes.com/winners-nominees/2009?page=1",
        "https://www.goldenglobes.com/winners-nominees/2008",
        "https://www.goldenglobes.com/winners-nominees/2008?page=1",
        "https://www.goldenglobes.com/winners-nominees/2007",
        "https://www.goldenglobes.com/winners-nominees/2007?page=1",
        "https://www.goldenglobes.com/winners-nominees/2006",
        "https://www.goldenglobes.com/winners-nominees/2006?page=1",
        "https://www.goldenglobes.com/winners-nominees/2005",
        "https://www.goldenglobes.com/winners-nominees/2005?page=1"
    ]
    x = []
    for url in urls:
        x.append(make_dict_from_page(url))
    return x


