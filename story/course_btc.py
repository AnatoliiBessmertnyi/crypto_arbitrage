import requests
import json
    
base = 'https://api.binance.com'
path =  '/api/v3/ticker/price'
url = base + path
param = {
    'symbol': 'BTCUSDT',
}
r = requests.get(url, params = param)
data_str = json.dumps(r.json())
data = float(json.loads(data_str)['price'])
print(data)