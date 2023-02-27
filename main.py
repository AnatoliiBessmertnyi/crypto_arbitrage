import re
from bs4 import BeautifulSoup
import urllib.request

def get_corona_gel():
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    url = "https://koronapay.com/transfers/online/?locale=ru&paidNotification=false&holdOnCalculator=true&receivingAmount=1000&receivingCountryId=GEO&receivingCurrencyId=981&sendingCountryId=RUS"
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

print(get_corona_gel())
print(get_corona_usd())
