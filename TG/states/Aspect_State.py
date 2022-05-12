from aiogram.dispatcher.filters.state import StatesGroup, State


class Aspect(StatesGroup):
    Initial = State() # ��������� �����������

    Pur_Find = State()

    Listen_Answer = State() # ����� � ��������� ������������ 

    Review = State() # ��������� ������������� ����������� ������������ (���������� �������.)

    Pos_Grading = State() # �������� ������.
    Neg_Grading = State() # ���������� ������.


    Neg_Nav = State()
    Neg_Route_Nav = State()
    Correction = State()
    Fiction = State()

    ReCheck = State() # ������������� ������.

    Cat_Set = State() # ��������� ���������.
    Context_Set = State() # ��������� ���������.


    TRASH = State()

    DB_Saving = State()
    Repeating = State()