from aiogram.dispatcher.filters.state import StatesGroup, State


class Senco(StatesGroup):
    Initial = State()
    Filling_COR = State()
    Filling_INCOR = State()
    Pulling = State()
    Fun_Mode = State()
    