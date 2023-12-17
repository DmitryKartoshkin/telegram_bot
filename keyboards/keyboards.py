from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config.config import DICT_CURRENCY

main_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/weather"),
            KeyboardButton(text="/currency_convector"),
         ]
    ],
    resize_keybord=True,
    one_time_keybord=True,
    input_field_placeholder="Команды запуска",
    selective=True
)


def currency_keybord():
    builder = ReplyKeyboardBuilder()
    for i in [*DICT_CURRENCY.values()]:
        builder.add(KeyboardButton(text=str(i)))
    return builder.adjust(4)


