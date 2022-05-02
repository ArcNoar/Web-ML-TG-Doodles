from aiogram.dispatcher.filters.state import StatesGroup, State


class Word_Type(StatesGroup):
    Initial = State()
    Pulling = State()
    Testing = State()
    TT_Set = State() # Test - Typeset
    Alpha_Find = State()
    Reset_Ask = State()
    #Learning = State()
    #Grading = State()