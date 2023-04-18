import requests
import time

from pprint import pprint

day_unix = 86400
month_unix = day_unix * 30
token = 'OAuth y0_AgAAAAAFwC2eAAYckQAAAADg1oFPTtP9p2KxS4KBeUKNBDhe6AgSL8U'
url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': token}
payload = {'from_date': (int(time.time()) - month_unix * 2)}

# Делаем GET-запрос к эндпоинту url с заголовком headers и параметрами params
homework_statuses = requests.get(url, headers=headers, params=payload)

# Печатаем ответ API в формате JSON
# print(homework_statuses.text)

# А можно ответ в формате JSON привести к типам данных Python и напечатать и его
pprint(homework_statuses.json())
print(int(time.time()))
