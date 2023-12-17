from pprint import pprint

import requests

from config.config import YOUR_API_KEY


def conv():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    pprint(data)
# pprint(data['Valute']['USD'])


# conv()


def conversion(currency: str, TOKEN=YOUR_API_KEY):

    url = f'https://v6.exchangerate-api.com/v6/{TOKEN}/latest/{currency}'
    response = requests.get(url)
    data = response.json()
    pprint(data['conversion_rates'])


def currency_convector():
    pass
conversion("EUR")
