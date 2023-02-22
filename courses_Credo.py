#Парсинг курсов USD, EURO банка Credo
import requests
from bs4 import BeautifulSoup

def get_html():
    url = 'https://credobank.ge/en/exchange-rates/?rate=credo_transfer'
    r = requests.get(url)
    return r

def get_course_usd(html):
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('div', class_ = 'currency-rate-box')
    course_usd_credo_to_gel = item.find_all('span', class_ = 'rate-value')[3].text
    return float(course_usd_credo_to_gel)

def get_course_euro_min(html):
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find_all('div', class_ = 'currency-rate-box')[1]
    course_usd_credo_to_gel = item.find_all('span', class_ = 'rate-value')[3].text
    return float(course_usd_credo_to_gel)

def get_course_euro_max(html):
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find_all('div', class_ = 'currency-rate-box')[1]
    course_usd_credo_to_gel = item.find_all('span', class_ = 'rate-value')[4].text
    return float(course_usd_credo_to_gel)

html = get_html()

course_USD_from_Credo = get_course_usd(html.text) 
course_EURO_from_Credo_min = float(get_course_euro_min(html.text))
course_EURO_from_Credo_max = float(get_course_euro_max(html.text))
