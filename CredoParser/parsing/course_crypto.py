import requests
import json


def get_course_crypto():  # Получение курса BTC
    url_ticker_crypto = 'https://api.binance.com/api/v3/ticker/price'
    BTC = {'symbol': 'BTCUSDT'}
    ETH = {'symbol': 'ETHUSDT'}
    BNB = {'symbol': 'BNBUSDT'}
    r1 = requests.get(url_ticker_crypto, BTC)
    r2 = requests.get(url_ticker_crypto, ETH)
    r3 = requests.get(url_ticker_crypto, BNB)
    data_str1 = json.dumps(r1.json())
    data_str2 = json.dumps(r2.json())
    data_str3 = json.dumps(r3.json())
    data1 = float(json.loads(data_str1)['price'])
    data2 = float(json.loads(data_str2)['price'])
    data3 = float(json.loads(data_str3)['price'])
    d = [data1, data2, data3]
    return d


courses = get_course_crypto()
