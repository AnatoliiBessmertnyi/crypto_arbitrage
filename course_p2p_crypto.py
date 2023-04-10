import requests


def get_btc_buy():  # Функция парсинга ордеров p2p
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': [
            'CREDOBANK',
            # тут указываете название вашего банка. Узнать можно тут https://p2p.binance.com/ru/trade/all-payments/USDT, all-payments поменяется на ваш банк.
        ],
        'countries': [],
        'publisherType': None,
        'asset': 'BTC',
        'fiat': 'GEL',  # смена валюты
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


def get_eth_buy():  # Функция парсинга ордеров p2p
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': [
            'CREDOBANK',
            # тут указываете название вашего банка. Узнать можно тут https://p2p.binance.com/ru/trade/all-payments/USDT, all-payments поменяется на ваш банк.
        ],
        'countries': [],
        'publisherType': None,
        'asset': 'ETH',
        'fiat': 'GEL',  # смена валюты
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


def get_btc_sell():  # Функция парсинга ордеров p2p
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': [
            'CREDOBANK',
            # тут указываете название вашего банка. Узнать можно тут https://p2p.binance.com/ru/trade/all-payments/USDT, all-payments поменяется на ваш банк.
        ],
        'countries': [],
        'publisherType': None,
        'asset': 'BTC',
        'fiat': 'GEL',  # смена валюты
        'tradeType': 'SELL',  # тип сделки
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


def get_eth_sell():  # Функция парсинга ордеров p2p
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/sell/BTC?fiat=GEL&payment=CREDOBANK', #тут тоже нужно изменить Тинькофф на нужный вам банк, ну или оставить
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': [
            'CREDOBANK',
            # тут указываете название вашего банка. Узнать можно тут https://p2p.binance.com/ru/trade/all-payments/USDT, all-payments поменяется на ваш банк.
        ],
        'countries': [],
        'publisherType': None,
        'asset': 'ETH',
        'fiat': 'GEL',  # смена валюты
        'tradeType': 'SELL',  # тип сделки
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


def get_bnb_sell():  # Функция парсинга ордеров p2p
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/sell/BTC?fiat=GEL&payment=CREDOBANK', #тут тоже нужно изменить Тинькофф на нужный вам банк, ну или оставить
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': [
            'CREDOBANK',
            # тут указываете название вашего банка. Узнать можно тут https://p2p.binance.com/ru/trade/all-payments/USDT, all-payments поменяется на ваш банк.
        ],
        'countries': [],
        'publisherType': None,
        'asset': 'BNB',
        'fiat': 'GEL',  # смена валюты
        'tradeType': 'SELL',  # тип сделки
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
