









class Prima_sentence:
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
            'X_Cord' : 1,
            'Y_Cord' : -1,
            'SF' : 'Empty',
            'Контекст' : '1',
            

            }
        return Word_Template



def STD_Prima(sent_data):
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
                'X_Cord' : data_list[0][3],
                'Y_Cord' : data_list[0][4],
                'SF' : data_list[0][5],
                'Контекст' : data_list[0][6]
                }
        
        return converted_data
    except Exception as _ex:
        print(_ex)




class Prima_word:
    """
        
        
    """
    def create(self):
        Word_Template = {
            'Слово' : None ,
            'Код' : '??',
            'X_Cord' : 1,
            'Y_Cord' : -1,
            'SF' : 'Empty',
            'Категория' : '1',

            }
        return Word_Template







def WTD_Prima(pulled_word): 
    """
    CTD = Conver To Dict
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    
    data_list = Pm_sql(user_data).get_user() => returns [(ID,first_name,sur_name,....,appearance)]
    
    covert_to_dict(data_list) => return dict = {
                                                'ID' : ID,
                                                'first_name' : first_name,
                                                 Key : Value,
                                                }

    """
    data_list = pulled_word
    #print(data_list)
    try:
        converted_data = {
                'ID' : data_list[0][0],
                'Слово' : data_list[0][1],
                'Код' : data_list[0][2],
                'X_Cord' : data_list[0][3],
                'Y_Cord' : data_list[0][4],
                'SF': data_list[0][5],
                'Категория' : data_list[0][6],
                }
        
        return converted_data
    except Exception as _ex:
        pass
        #print(_ex)


def WTDM_Prima(word_list):
    """
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    CTD = Conver To Dict
    data_list = Pm_sql(user_data).get_user() => returns [(ID,first_name,sur_name,....,appearance)]
    # Это можно по сути сделать основной функцией пушо что один что много, норм буит
    """
    dt_list = word_list
    collected_users = []
    for data_list in dt_list:
        
        try:
            converted_data = {
                    'ID' : data_list[0],
                    'Слово' : data_list[1],
                    'Код' : data_list[2],
                    'X_Cord' : data_list[3],
                    'Y_Cord' : data_list[4],
                    'SF' : data_list[5],
                    'Категория' : data_list[6],


                    }
            
            collected_users.append(converted_data)
        except Exception as _ex:
            pass
            #print(_ex)
    return collected_users