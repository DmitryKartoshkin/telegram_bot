import os

import asyncio
from dotenv import load_dotenv
from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config.config import BOT_TOKEN
from keyboards.keyboards import main_keybord
from servise.weather import get_weather


# load_dotenv()
# BOT_TOKEN = os.getenv('BOT_TOKEN')
# TOKEN = os.getenv('TOKEN_API')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class WeatherForm(StatesGroup):
    city = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=main_keybord)


@dp.message(Command("weather"))
async def cmd_weather(message: types.Message, state: FSMContext):
    await state.set_state(WeatherForm.city)
    await message.answer("Введите город")


@dp.message(WeatherForm.city)
async def form_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    data = await state.get_data()
    await state.clear()
    weather_forecast = await get_weather(data["city"])
    await message.answer(weather_forecast)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


