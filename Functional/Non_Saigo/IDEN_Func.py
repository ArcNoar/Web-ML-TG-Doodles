from datetime import date



class Iden_Temp:
    def create():
        
        empty_emote = {
            
            'Эмоция' : 2,
            'Мотив' : 2,
            'Комментарий' : 'Нулевое Описание',
            'Дата' : str(date.today()),
            
            }
        return empty_emote