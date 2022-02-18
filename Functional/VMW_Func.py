


class word_temp:
    """
        Word (Слово) = None
        Polysemantic (Многозначное) = false
        Constant_W (Константа) = false

        Nomination (Наименование) = false
        Word_Type (Тип) = NOUN
        Word_Gender (Род) = Neutral

        Word_Des (Значение) = Смысл слова не известен.
        Associated_W_id = None
        Group_Of_Word_id = None

        Synonym_W_id = None
        
    """
    def create(self):
        Word_Template = {
            'Слово' : None ,
            'Многозначность' : 'false',
            'Константность' : 'false',
            'Нарекающее' : 'false',
            'Тип' : 'NOUN',
            'Род' : 'Neutral',
            'Значение' : 'Смысл слова не известен.',
            'Ассоциация' : 'NULL',
            'Синоним' : 'NULL',
            'Категория' : 'NULL',

            }
        return Word_Template







