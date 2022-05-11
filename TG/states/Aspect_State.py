from aiogram.dispatcher.filters.state import StatesGroup, State


class Aspect(StatesGroup):
    Initial = State() # ��������� �����������

    Listen_Answer = State() # ����� � ��������� ������������ 

    Review = State() # ��������� ������������� ����������� ������������

    Pos_Grading = State() # �������� ������.
    Neg_Grading = State() # ���������� ������.

    ReCheck = State() # ������������� ������.

    Cat_Set = State() # ��������� ���������.
    Context_Set = State() # ��������� ���������.

    Repeating = State()