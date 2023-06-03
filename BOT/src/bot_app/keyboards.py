from aiogram import types


# ==== START MENU KEYBOARD ====
def create_start_buttons():
    start_keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_button = types.KeyboardButton('\U0001f9d1\u200D\U0001f373Menu')
    rules_button = types.KeyboardButton('\U0001f4d5Rules')
    start_keyboards.add(menu_button)
    start_keyboards.add(rules_button)
    return start_keyboards


# ====
def get_menu_keyboard(tags):
    menu_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    menu_keyboard.add(*tags)
    menu_keyboard.add(types.KeyboardButton("<<Back"))
    return menu_keyboard


def get_back_keyboard():
    back_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    back_button = types.KeyboardButton('<<Back')
    back_keyboard.add(back_button)
    return back_keyboard


def get_detail_dish_keyboard():
    detail_dish_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    photo_button = types.KeyboardButton('Photo')
    back_button = types.KeyboardButton('<<Back')
    detail_dish_keyboard.add(photo_button)
    detail_dish_keyboard.add(back_button)
