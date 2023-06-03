from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_menu_keyboard():
    # Створюємо кнопки
    menu_button = KeyboardButton("\U0001F372 Menu")
    language_button = KeyboardButton("\U0001F310 Język")

    # Створюємо клавіатуру з кнопками
    start_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    start_menu_keyboard.row(menu_button)
    start_menu_keyboard.row(language_button)

    return start_menu_keyboard



