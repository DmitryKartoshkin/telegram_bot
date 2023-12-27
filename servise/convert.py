from datetime import datetime

import requests

from config.config import YOUR_API_KEY, DICT_CURRENCY_1, DICT_CURRENCY_2


async def _conversion(currency: str, TOKEN=YOUR_API_KEY):
    url = f'https://v6.exchangerate-api.com/v6/{TOKEN}/latest/{currency}'
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']


async def currency_convector(curr: str, numb: int):
    currency = DICT_CURRENCY_2.get(curr)
    res = await _conversion(currency)
    return f"Курс валюты на {datetime.today().strftime('%d-%m-%Y')} \n" \
           f"{numb} {DICT_CURRENCY_1.get(currency)}: {numb * res['USD']} {DICT_CURRENCY_1.get('USD')} \n" \
           f"{numb} {DICT_CURRENCY_1.get(currency)}: {numb * res['EUR']} {DICT_CURRENCY_1.get('EUR')} \n" \
           f"{numb} {DICT_CURRENCY_1.get(currency)}: {numb * res['RUB']} {DICT_CURRENCY_1.get('RUB')}"





# print(asyncio.run(currency_convector("Турецкая лира", 4)))
# currency_convector("EUR")



