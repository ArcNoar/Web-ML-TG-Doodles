from aiogram.dispatcher.filters.state import StatesGroup, State


class Word_Type(StatesGroup):
    Initial = State()

    Pulling = State()

    
    ATT_Set = State()

    Alpha_Find = State()
    R_Find = State()
    Reset_Ask = State()
    #Learning = State()
    #Grading = State()