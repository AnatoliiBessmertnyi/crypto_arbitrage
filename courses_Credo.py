#Парсинг курсов USD, EURO банка Credo
import requests
from bs4 import BeautifulSoup
import urllib.request
import re

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

def get_corona_gel():
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    url = "https://koronapay.com/transfers/online/?locale=ru&paidNotification=false&holdOnCalculator=true&receivingAmount=1700&receivingCountryId=GEO&receivingCurrencyId=981&sendingCountryId=RUS"
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response, 'html.parser')
    course_str = soup.find('span', {'id': 'static-text-calculatorExchangeRate'}).text
    course = re.findall(r"[-+]?\d*\.?\d+|\d+", course_str)
    return float(course[1])

def get_corona_usd():
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    url = 'https://koronapay.com/transfers/online/?locale=ru&paidNotification=false&holdOnCalculator=true&receivingAmount=700&receivingCountryId=GEO&receivingCurrencyId=840&sendingCountryId=RUS'
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response, 'html.parser')
    course_str = soup.find('span', {'id': 'static-text-calculatorExchangeRate'}).text
    course = re.findall(r"[-+]?\d*\.?\d+|\d+", course_str)
    return float(course[1])

course_USD_from_Credo = get_course_usd(html.text)  # Курсы банка Credo
course_EURO_from_Credo_min = float(get_course_euro_min(html.text))
course_EURO_from_Credo_max = float(get_course_euro_max(html.text))

course_corona_gel = get_corona_gel()  # Курс золотой короны GEL
course_corona_usd = get_corona_usd()
