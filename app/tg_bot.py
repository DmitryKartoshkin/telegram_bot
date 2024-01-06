import asyncio
from aiogram import Bot, Dispatcher

from handlers import questions, weather, filter_words, currency
from config.config import config


# Запуск бота
async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    # Альтернативный вариант регистрации роутеров по одному на строку
    dp.include_router(questions.router)
    dp.include_router(weather.router)
    dp.include_router(currency.router)
    dp.include_router(filter_words.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
