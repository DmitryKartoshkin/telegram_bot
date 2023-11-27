import os

import asyncio
import requests
from dotenv import load_dotenv
from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command
from aiogram.dispatcher.filters.state import State, StatesGroup

from main import get_weather

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
TOKEN = os.getenv('TOKEN_API')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class WeatherForm(StatesGroup):
    city = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# Начинаем наш диалог
@dp.message_handler(commands=['weather'])
async def cmd_start(message: types.Message):
    await WeatherForm.name.set()
    await message.reply("Привет! Введите название города, в котором хотите узнать погоду")



# @dp.message(F.text, Command("weather"))
# async def get_weather_city(message: types.Message):
#     print(s)
    # s = await get_weather()



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


