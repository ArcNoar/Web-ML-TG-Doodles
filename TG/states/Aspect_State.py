from aiogram.dispatcher.filters.state import StatesGroup, State


class Aspect(StatesGroup):
    Initial = State() # получение предложения

    Listen_Answer = State() # Ответ и уточнение корректности 

    Review = State() # Уточнение достоверности предложения пользователя

    Pos_Grading = State() # Успешная оценка.
    Neg_Grading = State() # Негативная оценка.

    ReCheck = State() # Подтверждение Оценки.

    Cat_Set = State() # Установка Категории.
    Context_Set = State() # Установка Контекста.

    Repeating = State()