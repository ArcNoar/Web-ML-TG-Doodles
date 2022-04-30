#from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class SC_State(StatesGroup):
    Guide = State()
    Initial = State()
    Learning = State()
    Grading = State()