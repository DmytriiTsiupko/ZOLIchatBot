from aiogram import types
from aiogram.dispatcher.filters import Text, CommandStart
from aiogram.dispatcher import FSMContext

from .bot import dp
from .states import States
from .data_fetcher import get_dishes, get_dishes_by_tag, get_dish_info, get_photo_from_url

from .messages_ENG import WELCOME_MASSAGE, MANE_MANU_MASSAGE, RULES
from .keyboards import create_start_buttons, get_menu_keyboard, get_back_keyboard


# ==== START COMMAND HANDLER ====

@dp.message_handler(CommandStart(), state="*")
async def start_menu_handler(massage: types.Message, state: FSMContext):

    await States.start_command_state.set()

    await massage.answer(WELCOME_MASSAGE, reply_markup=create_start_buttons())


# ==== STAR MENU HANDLERS ==== start_command_state

@dp.message_handler(Text(equals='\U0001f9d1\u200D\U0001f373Menu'), state="*")
async def menu_handler(massage: types.Message, state: FSMContext):

    await States.menu_state.set()

    dishes = await get_dishes()
    tags = set(dish.get('tag') for dish in dishes)

    unique_tags = []
    for tag in tags:
        if ' ' in tag:
            splited_tag = tag.split()
            unique_tags.append(splited_tag[0])
        else:
            unique_tags.append(tag)

    menu_keyboard = get_menu_keyboard(set(unique_tags))

    await massage.answer(MANE_MANU_MASSAGE, reply_markup=menu_keyboard)


@dp.message_handler(Text(equals="\U0001f4d5Rules"), state="*")
async def get_rules(massage: types.Message, state: FSMContext):

    await state.reset_state(with_data=False)
    await States.rules_state.set()

    await massage.answer(RULES, reply_markup=get_back_keyboard())


# ==== DISH HANDLERS ==== menu_state

@dp.message_handler(Text(equals='<<Back'), state=States.menu_state)
@dp.message_handler(state=States.menu_state)
async def tag_handler(message: types.Message, state: FSMContext):

    if message.text == '<<Back':
        # Обробка кнопки "<<Back"
        await start_menu_handler(message, state)

    elif message.text.startswith('/'):
        # Обробка інших повідомлень у стані "menu_state"
        await detail_dish_handler(message, state)

    else:

        tag = message.text  # Отримуємо текст кнопки, яку натиснув користувач
        dishes = await get_dishes_by_tag(tag)  # Отримуємо список страв з обраним тегом

        if dishes:
            # Формуємо повідомлення зі списком страв
            dish_list = [f"{tag.upper()}:\n\n"]
            for dish in dishes:
                dish_name = dish['name'].replace(' ', '_')
                price = dish['price']
                description = dish['description']
                emoji = ""

                if dish['is_vegan'] == 'vegetarian':
                    emoji = "\U0001f96c"
                elif dish['spiciness'] != 'mild':
                    emoji = "\U0001f336\uFE0F"

                dish_item = f"- {emoji} /{dish_name} ({price} zł): {description}\n\n"
                dish_list.append(dish_item)

            await message.answer("".join(dish_list))
        else:
            await menu_handler(message, state)


@dp.message_handler(lambda message: message.text.startswith('/'), state=States.menu_state)
async def detail_dish_handler(message: types.Message, state: FSMContext):

    dish_name = message.text[1:].replace('_', ' ')
    dish_info = await get_dish_info(dish_name)

    if dish_info:

        dish = dish_info[0]
        name = dish.get('name')
        detail_description = dish.get('detail_description')
        photo_url = dish.get('photo')

        if photo_url:
            photo = await get_photo_from_url(photo_url)

            await message.answer_photo(photo, caption=f"{name.upper()}\n\n{detail_description}")

        else:
            await message.answer(f"{name.upper()}:\n\n{detail_description}")
    else:
        await message.answer("Dish not found")


# ==== BACK BUTTON HANDLER ====

@dp.message_handler(Text(equals='<<Back'), state=[States.menu_state, States.rules_state, States.detail_dish_state])
async def go_back_handler(message: types.Message, state: FSMContext):

    current_state = await state.get_state()

    if current_state is States.detail_dish_state:
        await state.reset_state(with_data=False)
        await menu_handler(message, state)

    elif current_state is States.menu_state or States.rules_state:
        await state.reset_state(with_data=False)
        await start_menu_handler(message, state)

    elif current_state is States.type_dish_state:
        await state.reset_state(with_data=False)
        await menu_handler(message, state)

    else:
        await state.reset_state(with_data=False)
        await start_menu_handler(message, state)


