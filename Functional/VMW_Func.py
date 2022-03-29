


class word_temp:
    """
        
        
    """
    def create(self):
        Word_Template = {
            'Слово' : None ,
            'Код' : '??',
            'Тип' : 'NOUN',
            'Значение' : 'Смысл слова не известен.',
            'Категория' : '1',

            }
        return Word_Template







def WTD_single(pulled_word): 
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
    try:
        converted_data = {
                'ID' : data_list[0][0],
                'Слово' : data_list[0][1],
                'Тип' : data_list[0][2],
                'Значение' : data_list[0][3],
                'Категория' : data_list[0][4],
                'Код' : data_list[0][5],
                }
        
        return converted_data
    except Exception as _ex:
        print(_ex)


def WTD_many(word_list):
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
                    'Тип' : data_list[2],
                    'Значение' : data_list[3],
                    'Категория' : data_list[4],
                    'Код' : data_list[5],


                    }
            
            collected_users.append(converted_data)
        except Exception as _ex:
            print(_ex)
    return collected_users








