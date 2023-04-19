import requests

headers = {
    'authority': 'p2p.binance.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'c2ctype': 'c2c_merchant',
    'clienttype': 'web',
    'content-type': 'application/json',
    'lang': 'ru',
    'origin': 'https://p2p.binance.com',
    'sec-ch-ua':
    '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


def get_btc_buy():  # Функция парсинга ордеров p2p
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': ['CREDOBANK'],  # наименование банка
        'countries': [],
        'publisherType': None,
        'asset': 'BTC',
        'fiat': 'GEL',  # валюта
        'tradeType': 'BUY',  # тип сделки
    }
    response = requests.post(
        'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
        headers=headers,
        json=json_data,
    )
    items = response.json().get('data')
    prices = []

    for i in items:
        price = float(i['adv']['price'])
        # print(price)  # проверка
        prices.append(price)

    return prices[0]


def get_eth_buy():
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': ['CREDOBANK'],
        'countries': [],
        'publisherType': None,
        'asset': 'ETH',
        'fiat': 'GEL',
        'tradeType': 'BUY',
    }
    response = requests.post(
        'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
        headers=headers,
        json=json_data,
    )
    items = response.json().get('data')
    prices = []

    for i in items:
        price = float(i['adv']['price'])
        # print(price)  # проверка
        prices.append(price)

    return prices[0]


def get_btc_sell():  # Функция парсинга ордеров p2p
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': ['CREDOBANK'],
        'countries': [],
        'publisherType': None,
        'asset': 'BTC',
        'fiat': 'GEL',
        'tradeType': 'SELL',
    }
    response = requests.post(
        'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
        headers=headers,
        json=json_data,
    )
    items = response.json().get('data')
    prices = []

    for i in items:
        price = float(i['adv']['price'])
        # print(price) # проверка
        prices.append(price)
    return prices[0]


def get_eth_sell():
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': ['CREDOBANK'],
        'countries': [],
        'publisherType': None,
        'asset': 'ETH',
        'fiat': 'GEL',
        'tradeType': 'SELL',
    }
    response = requests.post(
        'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
        headers=headers,
        json=json_data,
    )
    items = response.json().get('data')
    prices = []

    for i in items:
        price = float(i['adv']['price'])
        # print(price) # проверка
        prices.append(price)
    return prices[0]


def get_bnb_sell():
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': ['CREDOBANK'],
        'countries': [],
        'publisherType': None,
        'asset': 'BNB',
        'fiat': 'GEL',
        'tradeType': 'SELL',
    }
    response = requests.post(
        'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
        headers=headers,
        json=json_data,
    )
    items = response.json().get('data')
    prices = []

    for i in items:
        price = float(i['adv']['price'])
        # print(price) # проверка
        prices.append(price)
    return prices[0]


course_sell_GEL_for_BTC = get_btc_sell()
course_sell_GEL_for_ETH = get_eth_sell()
course_sell_GEL_for_BNB = get_bnb_sell()
course_buy_GEL_for_BTC = get_btc_buy()
course_buy_GEL_for_ETH = get_eth_buy()

# print(course_sell_GEL_for_BTC)
# print(course_sell_GEL_for_ETH)
# print(course_sell_GEL_for_BNB)
# print(course_buy_GEL_for_BTC)
# print(course_buy_GEL_for_ETH)
