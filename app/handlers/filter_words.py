import string

from aiogram.types import Message
from aiogram import Router, F

from app.config.config import BAN_WORDS


router = Router()


@router.message(F.text)
async def filter_messages(message: Message):

    contains_ban_word = False
    if message.text:
        message_words = set(message.text.translate(str.maketrans('', '', string.punctuation)).split())
        print(message_words)
        filtered_message = message.text
        for word in message_words:
            if word.lower() in BAN_WORDS:
                filtered_message = filtered_message.replace(word, "*" * len(word))
                contains_ban_word = True

    if contains_ban_word:
        await message.delete()
        await message.answer_sticker('CAACAgIAAxkBAAEKbW1lGVW1I6zFVLyovwo2rSgIt1l35QADJQACYp0ISWYMy8-mubjIMAQ')
