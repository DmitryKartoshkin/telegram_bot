from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from servise.weather import get_weather

router = Router()


class WeatherForm(StatesGroup):
    city = State()


@router.message(Command("weather"))
async def cmd_weather(message: Message, state: FSMContext):
    await state.set_state(WeatherForm.city)
    await message.answer("Введите город")


@router.message(WeatherForm.city)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text.lower())
    data = await state.get_data()
    await state.clear()
    weather_forecast = await get_weather(data["city"])
    await message.answer(weather_forecast)
