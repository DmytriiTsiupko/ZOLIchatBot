from aiogram import executor
from src.bot_app import dp


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, reset_webhook=True)
