import os
from pprint import pprint
from datetime import datetime

import requests
from dotenv import load_dotenv
from translate import Translator


load_dotenv()
TOKEN = os.getenv('TOKEN_API')

translator = Translator(from_lang="English", to_lang="russian")

DICT_ICON_WEATHER = {
    "Clear": "Ясно \U00002680",
    "Clouds": "Облачно \U00002601",
    "Rain": "Дождь \U00002614",
    "Drizzle": "Дождь \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Снег \U0001F328",
    "Mist": "Туман \U00002601"
}


async def get_weather(city: str, key=TOKEN):

    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric")
        result = response.json()
        name_city = translator.translate(result['name'])
        weather_description = DICT_ICON_WEATHER.get(result['weather'][0]['main'],
                                                    "Посмотри в окно, не пойму что там за погода")
        sunrise = datetime.fromtimestamp(result['sys']['sunrise'])
        sunset = datetime.fromtimestamp(result['sys']['sunset'])
        return f"Дата {datetime.fromtimestamp(result['dt']).strftime('%d.%m.%Y')} \n" \
               f"Город: {name_city} \n" \
               f"Температура воздуха: {result['main']['temp']} C {weather_description}\n" \
               f"Влажность: {result['main']['humidity']} % \n" \
               f"Давление: {result['main']['pressure']} мм.рт.ст. \n" \
               f"Ветер: {result['wind']['speed']} м/с\n" \
               f"Восход: {sunrise.strftime('%H:%M:%S')} \n" \
               f"Закат: {sunset.strftime('%H:%M:%S')} \n" \
               f"Продолжительность дня: {sunset - sunrise}"
    except:
        return "\U00002620 Проверь название города \U00002620"
