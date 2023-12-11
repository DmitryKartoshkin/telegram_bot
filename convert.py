from pprint import pprint

import requests

def conv():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    pprint(data)
# pprint(data['Valute']['USD'])


conv()