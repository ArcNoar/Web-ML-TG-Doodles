from datetime import date

class data_temp:
    """
            'ID' : None,
            'Внешность' : 'photo/unknown_user/default.png',
            'Имя' : None,
            'Фамилия' : None,
            'Пол' : 'None',
            'День Рождения' : '????-??-??',
            'Дата Знакомства' : str(date.today()),
            'Любовь' : 0.0,
            'Симпатия' : 0.0,
            'Дружба' : 0.0,
            'Восхищение' : 0.0,
            'Мания' : 0.0,
            'Ненависть' : 0.0,
            'Враждебность' : 1.0,
            'Неприязнь' : 0.0,
            'Страх' : 4.0,
            'Репутационный Бал' : -5.0,
            'Данные о Личности' : 'Нет информации',
            'Мнение о Личности' : 'Мнение не сформировано',
            'Черта Характера 1' : None,
            'Черта Характера 2' : None,
            'Черта Характера 3' : None,
            'Отношение от' : None,
            'Отношение к' : 1 , [1 - Незнакомец]

            }
    """
    def create(self):
        self.negative_affects = {
            'Ненависть' : 0.0,
            'Враждебность' : 1.0,
            'Неприязнь' : 0.0,
            'Страх' : 4.0
            }
        
        self.na_sum = sum(self.negative_affects.values())

        self.na_sum = float('{:.1f}'.format(self.na_sum))

        self.spec_affects = {
            'Мания' : 0.0,
            }

        self.positive_affects = {
            'Любовь' : 0.0,
            'Симпатия' : 0.0,
            'Дружба' : 0.0,
            'Восхищение' : 0.0
            }

        self.pa_sum = sum(self.positive_affects.values())
        self.pa_sum = float('{:.1f}'.format(self.pa_sum))
        
        def rep_sumarize(pas,nas,sa):
    
            if sa != 0.0 and sa != 0:
                return float('{:.1f}'.format(((pas + sa) - nas)))
            else:
                return float('{:.1f}'.format(pas - nas))

        self.Rep_SUM = rep_sumarize(self.pa_sum,self.na_sum,self.spec_affects.get('Мания'))
        self.raw_data = {
            'ID' : None,
            'Внешность' : 'photo/unknown_user/default.jpg',
            'Имя' : None,
            'Фамилия' : None,
            'Пол' : 'None',
            'День Рождения' : str(date.today()),
            'Дата Знакомства' : str(date.today()),
            'Любовь' : self.positive_affects['Любовь'],
            'Симпатия' : self.positive_affects['Симпатия'],
            'Дружба' : self.positive_affects['Дружба'],
            'Восхищение' : self.positive_affects['Восхищение'],
            'Мания' : self.spec_affects['Мания'],
            'Ненависть' : self.negative_affects['Ненависть'],
            'Враждебность' : self.negative_affects['Враждебность'],
            'Неприязнь' : self.negative_affects['Неприязнь'],
            'Страх' : self.negative_affects['Страх'],
            'Репутационный Бал' : self.Rep_SUM,
            'Данные о Личности' : 'Нет информации',
            'Мнение о Личности' : 'Мнение не сформировано',
            'Черта Характера 1' : None,
            'Черта Характера 2' : None,
            'Черта Характера 3' : None,
            'Отношение от' : 1,
            'Отношение к' : 1,

            }
        
        return self.raw_data
    def recreate(self,data):
        sample_data = data
        rep_val = float('{:.1f}'.format(((sample_data['Любовь'] + sample_data['Симпатия'] + sample_data['Дружба'] + sample_data['Восхищение']) + sample_data['Мания']) - (sample_data['Ненависть'] + sample_data['Враждебность'] + sample_data['Неприязнь'] + sample_data['Страх'])))
        sample_data['Репутационный Бал'] = rep_val

        return sample_data



def rep_refresh(pack):
    template = data_temp()
    temp = template.recreate(pack)
    return temp


def convert_to_dict(user_list):
    """
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    data_list = Pm_sql(user_data).get_user() => returns [(ID,first_name,sur_name,....,appearance)]
    
    covert_to_dict(data_list) => return dict = {
                                                'ID' : ID,
                                                'first_name' : first_name,
                                                 Key : Value,
                                                }

    """
    data_list = user_list
    try:
        converted_data = {
                'ID' : data_list[0][0],
                'Имя' : data_list[0][1],
                'Фамилия' : data_list[0][2],
                'День Рождения' : str(data_list[0][3]),
                'Пол' : data_list[0][4],
                'Любовь' : data_list[0][5],
                'Симпатия' : data_list[0][6],
                'Дружба' : data_list[0][7],
                'Восхищение' : data_list[0][8],
                'Мания' : data_list[0][9],
                'Ненависть' : data_list[0][10],
                'Враждебность' : data_list[0][11],
                'Неприязнь' : data_list[0][12],
                'Страх' : data_list[0][13],
                'Репутационный Бал' : data_list[0][14],
                'Дата Знакомства' : str(data_list[0][15]),
                'Данные о Личности' : data_list[0][16],
                'Мнение о Личности' : data_list[0][17],
                'Черта Характера 1' : data_list[0][18],
                'Черта Характера 2' : data_list[0][19],
                'Черта Характера 3' : data_list[0][20],
                'Отношение от' : data_list[0][21],
                'Отношение к' : data_list[0][22],
                'Внешность' : data_list[0][23],

                }
        
        return converted_data
    except Exception as _ex:
        print(_ex)