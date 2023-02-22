import requests
from courses_Credo import course_USD_from_Credo, course_EURO_from_Credo_min, \
    course_EURO_from_Credo_max
from course_GEL import course_buy_GEL_for_USDT, course_sell_GEL_for_USDT, \
    course_sell_EUR_for_USDT


def get_course_tinkoff():  # Функция парсинга ордеров p2p
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/TinkoffNew/USDT?fiat=RUB', #тут тоже нужно изменить Тинькофф на нужный вам банк, ну или оставить
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
        if min_singl_transfer <= 5000 and amount >= 200:
            break

    return max(prices)

def get_course_raif():  # Функция парсинга ордеров p2p
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/RaiffeisenBank/USDT?fiat=RUB', #тут тоже нужно изменить Тинькофф на нужный вам банк, ну или оставить
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
            'RaiffeisenBank',
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
        if min_singl_transfer <= 5000 and amount >= 100:
            break

    return max(prices)

# Функции расчета прибылей
sum_to_send_USD = 1000 # Оборот в $
course_sell_USDT_for_RUB = max(get_course_tinkoff(), get_course_raif()) # курс продажи USDT за фиат
sum_to_send_in_RUB = sum_to_send_USD * course_sell_USDT_for_RUB  # Сумма отправления в рублях

course_USD_from_corona = 76.4562  # курс USD ЗК
course_EURO_from_corona = 81.2112  # курс EURO ЗК
course_GEL_from_corona = 28.827  # курс GEL ЗК

course_USD_from_unistream = 76.2048  # курс USD юнистрим
course_EURO_from_unistream = 80.98255  # курс EURP юнистрим #
course_GEL_from_unistream = 29.44473  # курс GEL Unistream

def unistream_usd():
    profit = (
        sum_to_send_in_RUB / course_USD_from_unistream
        * course_USD_from_Credo / course_sell_GEL_for_USDT 
        * course_sell_USDT_for_RUB * 0.999) - (sum_to_send_in_RUB * 1.005)
    return profit

def corona_usd():
    corona_USD_profit_rub = (
        (sum_to_send_in_RUB / course_USD_from_corona
        * course_USD_from_Credo / course_sell_GEL_for_USDT 
        * course_sell_USDT_for_RUB * 0.999) - (sum_to_send_in_RUB * 1.005)
    )
    return corona_USD_profit_rub


def corona_gel():  # Функция подсчета прибыли через отправку GEL по ЗК
    corona_profit_RUB = (
        (sum_to_send_in_RUB / course_GEL_from_corona
         / course_sell_GEL_for_USDT * course_sell_USDT_for_RUB * 0.999) 
         - (sum_to_send_in_RUB * 1.005)
    )
    return corona_profit_RUB

def unistream_gel():  # Функция подсчета прибыли через отправку GEL по ЗК
    unistream_profit_RUB = (
        (sum_to_send_in_RUB / course_GEL_from_unistream
        / course_sell_GEL_for_USDT * course_sell_USDT_for_RUB * 0.999) 
        - (sum_to_send_in_RUB * 1.005)
        )
    return unistream_profit_RUB


def corona_euro():
    corona_EURO_profit_rub = (
        (sum_to_send_in_RUB / course_EURO_from_corona
        * course_EURO_from_Credo_min / course_sell_GEL_for_USDT 
        * course_sell_USDT_for_RUB * 0.999) - (sum_to_send_in_RUB * 1.005)
    )
    return corona_EURO_profit_rub

def unistream_euro():
    unistream_EURO_profit_rub = (
        (sum_to_send_in_RUB / course_EURO_from_unistream
        * course_EURO_from_Credo_min / course_sell_GEL_for_USDT 
        * course_sell_USDT_for_RUB * 0.999) - (sum_to_send_in_RUB * 1.005)
    )
    return unistream_EURO_profit_rub

def euro_classic():
    profit = (
        (sum_to_send_USD / course_sell_EUR_for_USDT * course_buy_GEL_for_USDT)
        - (sum_to_send_USD * course_EURO_from_Credo_max) 
    )
    spred = profit / (sum_to_send_USD * course_EURO_from_Credo_max) * 100
    return spred

if unistream_usd() > corona_usd():
    print(
        f'\nПрибыль по Unistream USD c {sum_to_send_USD}$ '
        f'составит: {unistream_usd():.2f} рублей \n'
        f'Спред: {unistream_usd() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
    )
elif unistream_usd() < corona_usd():
    print(
        f'\nПрибыль по Золотой короне USD c {sum_to_send_USD}$ '
        f'составит: {corona_usd():.2f} рублей \n'
        f'Спред: {corona_usd() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
    )

if unistream_euro() > corona_euro():
    print(    
        f'Прибыль по Unistream EURO c {sum_to_send_USD}$ '
        f'составит: {unistream_euro():.2f} рублей\n'
        f'Спред: {unistream_euro() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
    )
elif unistream_euro() < corona_euro():
    print(    
        f'Прибыль по Золотой короне EURO c {sum_to_send_USD}$ '
        f'составит: {corona_euro():.2f} рублей \n'
        f'Спред: {corona_euro() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
        )

if corona_gel() > unistream_gel():
    print(    
        f'Прибыль по Золотой короне GEL c {sum_to_send_USD}$ '
        f'составит: {corona_gel():.2f} рублей \n'
        f'Спред: {corona_gel() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
    )
elif corona_gel() < unistream_gel():
    print(    
        f'Прибыль по Unistream GEL c {sum_to_send_USD}$ '
        f'составит: {unistream_gel():.2f} рублей \n'
        f'Спред: {unistream_gel() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
        )

# Проверка
print(
    f'Продажа USDT за RUB: {course_sell_USDT_for_RUB} | '
    f'Курс конвертации EURO/GEL: {course_EURO_from_Credo_max}'
    f'\nКурс USD/GEL Credo: {course_USD_from_Credo}  | '
    f'Курс EURO/GEL Credo: {course_EURO_from_Credo_min}'
    f'\nПокупка GEL за USDT: {course_buy_GEL_for_USDT}  | '
    f'Покупка USDT за GEL: {course_sell_GEL_for_USDT}'
    f'\nСпред классики: {course_buy_GEL_for_USDT / course_sell_GEL_for_USDT * 100 - 100:.2f}%      | '
    f'Спред EURO/USDT: {euro_classic():.2f}%\n'
#    f'\nПрибыль по Unistream USD c {sum_to_send_USD}$ '
 #   f'составит: {unistream_usd():.2f} рублей \n'
  #  f'Спред: {unistream_usd() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
#    f'Прибыль по Unistream EURO c {sum_to_send_USD}$ '
#    f'составит: {unistream_euro():.2f} рублей \n'
#    f'Спред: {unistream_euro() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
#    f'Прибыль по Unistream GEL c {sum_to_send_USD}$ '
#    f'составит: {unistream_gel():.2f} рублей \n'
#    f'Спред: {unistream_gel() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'

#    f'\nПрибыль по Золотой короне USD c {sum_to_send_USD}$ '
#    f'составит: {corona_usd():.2f} рублей \n'
 #   f'Спред: {corona_usd() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
 #   f'Прибыль по Золотой короне EURO c {sum_to_send_USD}$ '
#    f'составит: {corona_euro():.2f} рублей \n'
#    f'Спред: {corona_euro() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
#    f'Прибыль по Золотой короне GEL c {sum_to_send_USD}$ '
#    f'составит: {corona_gel():.2f} рублей \n'
#    f'Спред: {corona_gel() / (sum_to_send_USD * course_sell_USDT_for_RUB) * 100:.2f}%\n'
)
