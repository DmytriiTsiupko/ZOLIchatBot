import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import CommandStart

from handlers import start_menu_handler

load_dotenv()

# Отримуємо токен бота з оточення
TOKEN = os.getenv('BOT_TOKEN')

# Створюємо екземпляр бота та диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Зареєструвати хендлер
dp.register_message_handler(start_menu_handler, CommandStart())

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=False)