from aiogram.dispatcher.filters.state import StatesGroup, State


class AI_State(StatesGroup):
    Initial = State()
    Learning = State()
    Grading = State()