


class word_temp:
    """
        Word_Template = {
            'Слово' : None ,
            'Многозначность' : 'false',
            'Константность' : 'false',
            'Нарекающее' : 'false',
            
            'Тип' : 'NOUN',
            'Тип_2' : 'NONE_T',

            'Род' : 'NONE',
            'Множественное' : 'false',
            'Падеж' : 'None',
            'Собственное' : 'false'
            'Ст_Сравнения' : 'None',
            'Наклонение' : 'None',
            'Одушевленность' : 'None',
            'Время' : 'None',


            'Значение' : 'Смысл слова не известен.',
            'Ассоциация' : 'NULL',
            'Синоним' : 'NULL',
            'Антоним' : 'NULL',
            'Категория' : 'NULL',


            }
        
    """
    def create(self):
        Word_Template = {
            'Слово' : None ,
            'Многозначность' : 'false',
            'Константность' : 'false',
            'Нарекающее' : 'false',
            
            'Тип' : 'NOUN',
            'Тип_2' : 'NONE_T',

            'Род' : 'NONE',
            'Число' : 'None',
            'Падеж' : 'None',
            'Собственное' : 'false',
            'Ст_Сравнения' : 'None',
            'Наклонение' : 'None',
            'Одушевленность' : 'None',
            'Время' : 'None',
            'Лицо' : 'None',
            'Склонение' : 'None',


            'Значение' : 'Смысл слова не известен.',
            'Ассоциация' : 'NULL',
            'Синоним' : 'NULL',
            'Антоним' : 'NULL',
            'Категория' : 'NULL',


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
                'Многозначность' : data_list[0][2],
                'Константность' : str(data_list[0][3]),
                'Нарекающее' : data_list[0][4],
                'Тип' : data_list[0][5],
                'Род' : data_list[0][6],
                'Значение' : data_list[0][7],
                'Ассоциация' : data_list[0][8],
                'Синоним' : data_list[0][9],
                'Категория' : data_list[0][10],
                'Падеж' : data_list[0][11],
                'Собственное' : data_list[0][12],
                'Антоним' : data_list[0][13],
                'Степень Сравнения' : data_list[0][14],
                'Наклонение' : data_list[0][15],
                'Множественное' : data_list[0][16],
                'Одушевленность' : data_list[0][17],
                'Время' : data_list[0][18],
                'Тип_2' : data_list[0][19],
                'Лицо' : data_list[0][20],
                'Склонение' : data_list[0][21],
                
                

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
                    'Многозначность' : data_list[2],
                    'Константность' : str(data_list[3]),
                    'Нарекающее' : data_list[4],
                    'Тип' : data_list[5],
                    'Род' : data_list[6],
                    'Значение' : data_list[7],
                    'Ассоциация' : data_list[8],
                    'Синоним' : data_list[9],
                    'Категория' : data_list[10],
                    'Падеж' : data_list[11],
                    'Собственное' : data_list[12],
                    'Антоним' : data_list[13],
                    'Степень Сравнения' : data_list[14],
                    'Наклонение' : data_list[15],
                    'Множественное' : data_list[16],
                    'Одушевленность' : data_list[17],
                    'Время' : data_list[18],
                    'Тип_2' : data_list[19],
                    'Лицо' : data_list[20],
                    'Склонение' : data_list[21],
                    

                    }
            
            collected_users.append(converted_data)
        except Exception as _ex:
            print(_ex)
    return collected_users








