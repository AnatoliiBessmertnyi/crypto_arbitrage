import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def count():
    session = requests.Session()
    return cfscrape.create_scraper(sess=session)
session = get_session() # Дальше работать как с обычной requests.Session
header = {
    'Request URL': 'https://koronapay.com/transfers/online/?locale=ru&paidNotification=false&holdOnCalculator=true&receivingAmount=1500&receivingCountryId=GEO&receivingCurrencyId=981&sendingCountryId=RUS',
    'Request Method': 'GET',
    'Status Code': '200 OK',
    'Remote Address': '194.85.18.32:443',
    'Referrer Policy': 'strict-origin-when-cross-origin',
    'cache-control': 'private, no-cache, no-store, must-revalidate',
    'content-encoding': 'gzip',
    'content-type': 'text/html; charset=utf-8',
    'date': 'Thu, 16 Feb 2023 16:41:08 GMT',
    'expires': '-1',
    'pragma': 'no-cache',
    'samesite': 'None',
    'set-cookie': 'qpay-web/3.0_locale=ru; Path=/',
    'set-cookie': 'ROUTEID=29f5eaf1148ee63a|Y+5cp; path=/',
    'strict-transport-security': 'max-age=16000000',
    'transfer-encoding': 'chunked',
    'vary': 'Accept-Encoding',
    'x-content-type-options': 'nosniff',
    'x-xss-protection': '1; mode=block',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en-GB;q=0.9,en;q=0.8,ru;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.1.1490510052.1676113636; _gcl_au=1.1.459106353.1676113660; tmr_lvid=240de717cc13e2a4a9864b2f5a25faba; tmr_lvidTS=1676113661361; _ga_X0B8K32217=GS1.1.1676299513.2.0.1676299517.56.0.0; client-id=8d10fa6e-31da-4ead-afce-fe5114e0f153; qpay-web/3.0_locale=ru; qpay-web/3.0_is-toggle-locale-cookie=true; qpay-web/3.0_csrf-token-v2=a8fc22b1a9bdb20b5639f879e4328417; _ga_H68H5PL1N6=GS1.1.1676565505.4.1.1676565538.27.0.0; tmr_detect=1%7C1676565540262; ROUTEID=29f5eaf1148ee63a|Y+5co',
    'Host': 'koronapay.com',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
url = 'https://koronapay.com'
json_url = 'https://koronapay.com/transfers/online/?locale=ru&paidNotification=false&holdOnCalculator=true&receivingAmount=1500&receivingCountryId=GEO&receivingCurrencyId=981&sendingCountryId=RUS'
session = requests.Session()
r = session.get(url, headers=header)
json_r = session.get(json_url, headers=header)

print(json_r)