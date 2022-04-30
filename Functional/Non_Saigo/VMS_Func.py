


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



def STD_Single(sent_data):
    """
    STD = Sentence To Dict
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    
    data_list = sql_pull_func(user_data).get_user() => returns [(ID,first_name,sur_name,....,appearance)]
    
    func(data_list) => return dict = {
                                                'ID' : ID,
                                                'first_name' : first_name,
                                                 Key : Value,
                                                }

    """
    data_list = sent_data
    try:
        converted_data = {
                'ID' : data_list[0][0],
                'Предложение' : data_list[0][1],
                'Дешифровка' : data_list[0][2],
                'Краткая суть' : data_list[0][3],
                'От кого' : data_list[0][4],
                'Контекст' : data_list[0][5],
                }
        
        return converted_data
    except Exception as _ex:
        print(_ex)
