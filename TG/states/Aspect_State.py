from aiogram.dispatcher.filters.state import StatesGroup, State


class Aspect(StatesGroup):
    Initial = State() # получение предложения

    Pur_Find = State()

    Listen_Answer = State() # Ответ и уточнение корректности 

    Review = State() # Уточнение достоверности предложения пользователя (Опциольная функция.)

    Pos_Grading = State() # Успешная оценка.
    Neg_Grading = State() # Негативная оценка.


    Neg_Nav = State()
    Neg_Route_Nav = State()
    Correction = State()
    Fiction = State()

    ReCheck = State() # Подтверждение Оценки.

    Cat_Set = State() # Установка Категории.
    Context_Set = State() # Установка Контекста.


    TRASH = State()

    DB_Saving = State()
    Repeating = State()