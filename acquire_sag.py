from requests import get
from bs4 import BeautifulSoup
import os
import re

# get categories
def get_category(url):
    headers = {'User-Agent':'Codeup Data Science Student'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    x = []
    for h3 in soup.find_all('h3')[:5]:
        x.append(h3.text)
    return x

# get film titles
def get_film(url):
    headers = {'User-Agent':'Codeup Data Science Student'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    x = []
    for h3 in soup.find_all(class_='movie-title-group')[:5]:
        x.append(h3.text)
    return x


# get nominee names
def get_nominee(url):
    headers = {'User-Agent':'Codeup Data Science Student'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    x = []
    for h3 in soup.find_all(class_='nominee-name')[:20]:
        x.append(h3.text)
    return x


# turn into a dictionary
def make_dict_from_page(url):
    headers = {'User-Agent':'Codeup Data Science Student'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    year = soup.title.string
    cat = get_category(url)
    film = get_film(url)
    nominee = get_nominee(url)
    return {'year': year,
            'category': cat,
            'film': film,
            'nominees': nominee
    }