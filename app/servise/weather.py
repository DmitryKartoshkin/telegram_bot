from datetime import datetime

import requests
from app.config.config import TOKEN_API, BAN_WORDS

DICT_ICON_WEATHER = {
    "Clear": "Ясно \U00002680",
    "Clouds": "Облачно \U00002601",
    "Rain": "Дождь \U00002614",
    "Drizzle": "Дождь \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Снег \U0001F328",
    "Mist": "Туман \U00002601"
}


async def get_weather(city: str, key=TOKEN_API):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={key}&units=metric"
    try:

        response = requests.get(URL)
        result = response.json()
        weather_description = DICT_ICON_WEATHER.get(result['weather'][0]['main'],
                                                    "Посмотри в окно, не пойму что там за погода")
        sunrise = datetime.fromtimestamp(result['sys']['sunrise'])
        sunset = datetime.fromtimestamp(result['sys']['sunset'])
        return f"Дата {datetime.fromtimestamp(result['dt']).strftime('%d.%m.%Y')} \n" \
               f"Город: {result['name']} \n" \
               f"Температура воздуха: {result['main']['temp']} C {weather_description}\n" \
               f"Влажность: {result['main']['humidity']} % \n" \
               f"Давление: {result['main']['pressure']} мм.рт.ст. \n" \
               f"Ветер: {result['wind']['speed']} м/с\n" \
               f"Восход: {sunrise.strftime('%H:%M:%S')} \n" \
               f"Закат: {sunset.strftime('%H:%M:%S')} \n" \
               f"Продолжительность дня: {sunset - sunrise}"
    except:
        return "\U00002620 Проверь название города \U00002620"


# if __name__ == "__main__":
#     print(get_weather("сочи", key=TOKEN))
