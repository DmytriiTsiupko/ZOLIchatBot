from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher import Dispatcher

from keyboards import start_menu_keyboard
from lexicon_pl import LEXICON_PL

async def start_menu_handler(message: types.Message):
    # Отримати клавіатуру стартового меню
    keyboard = start_menu_keyboard()

    # Відправити повідомлення зі стартовим меню
    await message.answer(LEXICON_PL['/start'], reply_markup=keyboard)
