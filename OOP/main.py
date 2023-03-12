import requests

class A:
    headers = {
            'authority': 'p2p.binance.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9',
            'c2ctype': 'c2c_merchant',
            'clienttype': 'web',
            'content-type': 'application/json',
            'lang': 'ru',
            'origin': 'https://p2p.binance.com',
            # 'referer': 'https://p2p.binance.com/ru/trade/TinkoffNew/USDT?fiat=RUB', #тут тоже нужно изменить Тинькофф на нужный вам банк, ну или оставить
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
            'rows': 20,
            'payTypes': [
                'TinkoffNew',
                # тут указываете название вашего банка. Узнать можно тут https://p2p.binance.com/ru/trade/all-payments/USDT, all-payments поменяется на ваш банк.
            ],
            'countries': [],
            'publisherType': None,
            'asset': 'USDT',
            'fiat': 'RUB',  # смена валюты
            'tradeType': 'BUY',  # тип сделки
        }
    
    response = requests.post(
            'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
            headers=headers,
            json=json_data,
        )
          

    def parse(self, response):
        all_data_1 = response.json() # от сюда начали магию творить
        all_data_2 = all_data_1['data']
        prices = []
        min_transfers = []
        amounts = []
        for i in all_data_2:
            price = float(i['adv']['price'])
            min_singl_transfer = float(i['adv']['minSingleTransAmount'])
            amount = float(i['adv']['surplusAmount'])
            #print(price,'', min_singl_transfer, '', amount)  # проверка
            prices.append(price)
            min_transfers.append(min_singl_transfer)
            amounts.append(amount)
            if min_singl_transfer <= 5000 and amount >= 150:
                break
        return max(prices)

class B(A):
    a = 2
    
print(A)  
