


class sentence_temp:
    """
        Sentence (Предложение) = None
        Sent_Dech (Дешифровка) = false
        Short_Mean (Краткая суть) = false

        From_Who_id (От кого) = false
        Sent_Context_id (Айди контекста) = NOUN
        
        
    """
    def create(self):
        Word_Template = {
            'Предложение' : 'Пустое предложение' ,
            'Дешифровка' : '91-92',
            'Краткая суть' : 'Смысл неопределен',
            'От кого' : '00000000',
            'Контекст' : '1',
            

            }
        return Word_Template