from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import os
from dotenv import load_dotenv


load_dotenv()

# Токе бота
TOKEN = os.getenv('HTTP_BOT_API')

# Створення екземпляра бота
bot = Bot(token=TOKEN)

# Диспетчер для обробки подій
dp = Dispatcher(bot)


# Опрацювання команди /start
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    menu_button = InlineKeyboardButton("\U0001F372 Menu", callback_data="menu")
    language_button = InlineKeyboardButton("\U0001F310 Język", callback_data="language")
    keyboard.row(menu_button, language_button)

    await message.reply("Dzień dobry! Ja jestem ZOLI Botem! Zobacz co my mamy!", reply_markup=keyboard)


# Запуск бота
if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(dp.start_polling())
        loop.run_forever()
    finally:
        loop.stop()
