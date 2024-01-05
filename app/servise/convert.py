from datetime import datetime

import requests

from config.config import config


async def _conversion(currency: str, TOKEN=config.YOUR_API_KEY):
    url = f'https://v6.exchangerate-api.com/v6/{TOKEN}/latest/{currency}'
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']


async def currency_convector(curr: str, numb: int):
    currency = config.DICT_CURRENCY_2.get(curr)
    res = await _conversion(currency)
    return f"Курс валюты на {datetime.today().strftime('%d-%m-%Y')} \n" \
           f"{numb} {config.DICT_CURRENCY_1.get(currency)}: {numb * res['USD']} {config.DICT_CURRENCY_1.get('USD')}\n" \
           f"{numb} {config.DICT_CURRENCY_1.get(currency)}: {numb * res['EUR']} {config.DICT_CURRENCY_1.get('EUR')}\n" \
           f"{numb} {config.DICT_CURRENCY_1.get(currency)}: {numb * res['RUB']} {config.DICT_CURRENCY_1.get('RUB')}"





# print(asyncio.run(currency_convector("Турецкая лира", 4)))
# currency_convector("EUR")



