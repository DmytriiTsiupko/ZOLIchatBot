from aiogram import types
from aiogram.dispatcher.filters import Text, CommandStart
from aiogram.dispatcher import FSMContext

from .bot import dp
from .states import States
from .data_fetcher import get_dishes, get_dishes_by_tag

from .massages_ENG import WELCOME_MASSAGE, MANE_MANU_MASSAGE, RULES
from .keyboards import create_start_buttons, get_menu_keyboard, get_back_keyboard


# ==== START COMMAND HANDLER ====

@dp.message_handler(CommandStart(), state="*")
async def start_menu_handler(massage: types.Message, state: FSMContext):
    await States.start_command_state.set()
    await massage.answer(WELCOME_MASSAGE, reply_markup=create_start_buttons())


# ==== STAR MENU HANDLERS ====

@dp.message_handler(Text(equals='Menu'), state=States.start_command_state)
async def menu_handler(massage: types.Message, state: FSMContext):
    await States.menu_state.set()
    dishes = await get_dishes()
    dishes_by_tag = {}

    for dish in dishes:
        tag = dish.get('tag')
        name = dish.get('name')
        description = dish.get('description')

        if tag and name:
            if tag in dishes_by_tag:
                dishes_by_tag[tag].append({"name": name, "description": description})
            else:
                dishes_by_tag[tag] = [{"name": name, "description": description}]

    tags = list(dishes_by_tag.keys())
    menu_keyboard = get_menu_keyboard(tags)

    await massage.answer(MANE_MANU_MASSAGE, reply_markup=menu_keyboard)


@dp.message_handler(Text(equals="Rules"), state=States.start_command_state)
async def get_rules(massage: types.Message, state: FSMContext):
    await States.rules_state.set()
    await massage.answer(RULES, reply_markup=get_back_keyboard())


# ==== DISH HANDLERS ====

@dp.message_handler(state=States.menu_state)
async def tag_handler(message: types.Message, state: FSMContext):
    await state.reset_state()
    await States.detail_dish_state.set()
    tag = message.text  # Отримуємо текст кнопки, яку натиснув користувач
    dishes = await get_dishes_by_tag(tag)  # Отримуємо список страв з обраним тегом

    if dishes:
        # Формуємо повідомлення зі списком страв
        dish_list = f"{tag}:\n"
        for dish in dishes:
            dish_list += f"- /{dish['name'].replace(' ', '_')}: {dish['description']}\n"

        await message.answer(dish_list)
    else:
        await message.answer("На жаль, для цього тегу немає страв.")
        await start_menu_handler(message, state=States.start_command_state)


@dp.message_handler(lambda message: message.text.startswith('/'))
async def dish_handler(message: types.Message):
    dish_name = message.text[1:]  # Видаляємо знак "/" з початку назви страви
    dish_info = await get_dish_info(dish_name)  # Отримуємо інформацію про страву з сервера

    if dish_info:
        # Отримання інформації про страву
        name = dish_info.get('name')
        description = dish_info.get('description')
        photo_url = dish_info.get('photo_url')

        # Відправка повідомлення з інформацією про страву
        await message.answer(f"Name: {name}\nDescription: {description}")
        if photo_url:
            await message.answer_photo(photo_url)
    else:
        await message.answer("Dish not found")  # В разі, якщо страву не знайдено

# ==== BACK BUTTON HANDLER ====

@dp.message_handler(Text(equals='<<Back'), state=[States.menu_state, States.rules_state])
async def back_handler(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)
    await start_menu_handler(message, state=States.start_command_state)


