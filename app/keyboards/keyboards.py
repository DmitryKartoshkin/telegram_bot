from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config.config import config


def get_start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="/weather")
    kb.button(text="/currency_convector")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)


def currency_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for i in [*config.DICT_CURRENCY_2.keys()]:
        builder.add(KeyboardButton(text=str(i)))
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True)

