from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    start_command_state = State()
    menu_state = State()
    rules_state = State()
    detail_dish_state = State()
    prev_handler = {}
