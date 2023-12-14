from pprint import pprint

import requests


YOUR_API_KEY = "fe403357e740d588cde6a26f"

def conv():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    pprint(data)
# pprint(data['Valute']['USD'])


# conv()
DICT_CURRENCY = {'AED': "Дирхам ОАЭ", 'ARS': "Аргентинское пе́со", 'AUD': "Австралийский доллар",
                 'AMD': "Армянский драм", 'AZN': " Азербайджанский манат", 'BGN': "Болгарский лев",
                 'BRL': "Бразильский реал", 'BYN': "Белорусский рубль", 'CAD': "Канадский доллар",
                 'CHF': "Швейцарский франк", 'CNY': "Китайский юань", 'COP': "Колумбийское песо",
                 'CUP': "Кубинское песо", 'CZK': "Чешская крона", 'DKK': "Датская крона",
                 'EGP': "Египетский фунт", 'EUR': "евро", 'GBP': "фунт стерлинг", 'GEL': "Грузинский лари",
                 'HKD': "Гонконгский доллар", 'HUF': "Венгерский форинт", 'ILS': "шекель", 'INR': "Индийская рупия",
                 'JPY': "иена", 'KGS': "Киргизский сом", 'KRW': "Южнокорейская вона", 'KZT': "Казахстанский тенге",
                 'MDL': "Молдавский лей ", 'MXN': "Мексиканское песо", 'NOK': "Норвежская крона",
                 'PLN': "Польский злотый", 'RON': "Румынский лей", 'RSD': "Сербский динар", 'RUB': "рубль",
                 'SAR': "Саудовский риял", 'SEK': "шведская крона", 'SGD': "Сингапурский доллар",
                 'THB': "Таиландский бат", 'TJS': "Таджикский сомони", 'TMT': "Новый туркменский манат",
                 'TRY': "Турецкая лира", 'UAH': "Украинская гривна", 'USD': "доллар", 'UZS': "Узбекский су",
                 'VND': "Вьетнамский донг"}

LIST_COUNTRY = []
def conversion(currency: str):

    url = f'https://v6.exchangerate-api.com/v6/{YOUR_API_KEY}/latest/USD'
    response = requests.get(url)
    data = response.json()
    pprint(data)