import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from config.config import BOT_TOKEN
from keyboards.keyboards import main_keyboard, currency_keyboard
from servise.convert import currency_convector
from servise.weather import get_weather


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class WeatherForm(StatesGroup):
    city = State()


class CurrencyForm(StatesGroup):
    currency = State()
    count = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=main_keyboard)


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


@dp.message(Command("currency_convector"))
async def cmd_weather(message: types.Message, state: FSMContext):
    await state.set_state(CurrencyForm.currency)
    await message.answer("Выберете валюту", reply_markup=currency_keyboard().as_markup(resize_keyboard=True))


@dp.message(CurrencyForm.currency)
async def currency(message: types.Message, state: FSMContext):
    await state.update_data(currency=message.text)
    await state.set_state(CurrencyForm.count)
    await message.answer("Выберете количество для расчета")


@dp.message(CurrencyForm.count)
async def currency(message: types.Message, state: FSMContext):
    await state.update_data(count=message.text)
    data = await state.get_data()
    await state.clear()
    cur = await currency_convector(data["currency"], int(data["count"]))
    await message.answer(cur)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


