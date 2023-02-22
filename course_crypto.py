import requests
import json

def get_course_btc():  # Получение курса BTC
    url_ticker_crypto = 'https://api.binance.com/api/v3/ticker/price'
    param = {
    'symbol': 'BTCUSDT',
    }
    r = requests.get(url_ticker_crypto, params = param)
    data_str = json.dumps(r.json())
    data = float(json.loads(data_str)['price'])
    return data