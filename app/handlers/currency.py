from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from keyboards.keyboards import currency_keyboard
from servise.convert import currency_convector

router = Router()


class CurrencyForm(StatesGroup):
    currency = State()
    count = State()


@router.message(Command("currency_convector"))
async def cmd_weather(message: Message, state: FSMContext):
    await state.set_state(CurrencyForm.currency)
    await message.answer(
        "Выберете валюту",
        reply_markup=currency_keyboard()
    )


@router.message(CurrencyForm.currency)
async def currency(message: Message, state: FSMContext):
    await state.update_data(currency=message.text)
    await state.set_state(CurrencyForm.count)
    await message.answer("Выберете количество для расчета")


@router.message(CurrencyForm.count)
async def currency(message: Message, state: FSMContext):
    await state.update_data(count=message.text)
    data = await state.get_data()
    await state.clear()
    cur = await currency_convector(data["currency"], int(data["count"]))
    await message.answer(cur)
