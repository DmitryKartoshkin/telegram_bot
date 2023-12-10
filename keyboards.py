from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/weather")]
    ],
    resize_keybord=True,
    one_time_keybord=True,
    input_field_placeholder="Команды запуска",
    selective=True
)
