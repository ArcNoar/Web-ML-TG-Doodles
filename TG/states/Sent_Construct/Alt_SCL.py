#from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class SC_Alt(StatesGroup):
    Initial = State()
    Learning = State()
    Grading = State()