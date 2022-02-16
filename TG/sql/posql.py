import psycopg2
from datetime import date
from .conf import db_name,host,user,password
from Functional.PM_Func import convert_to_dict
"""
Нужно сделать связующую дб фукцию для каждого табла.
Социальная Память:
    Person_Memory
    Возможно нам не пригодится писать триллиард дб, если мне сейчас удастся прикрутить сюда джангу

Класс с функцией занесения, взятия данных, редактирования | удаления? (честно не уверен ибо это стоит поручить уже мне)

"""
class PM_Sql:

    def __init__(self,data_dict):
        self.unic_id_d = data_dict['ID']
        
        self.Appearance_d = data_dict['Внешность']
        self.first_name_d = data_dict['Имя']
        self.sur_name_d = data_dict['Фамилия']
        self.gender_d = data_dict['Пол']
        
        self.birthday_d = data_dict['День Рождения']
        self.Meet_Date_d = data_dict['Дата Знакомства']
        
        self.Affection_d = data_dict['Любовь']
        self.Sympathy_d = data_dict['Симпатия']
        self.FriendShip_d = data_dict['Дружба']
        self.Admiration_d = data_dict['Восхищение']
        
        self.Mania_d= data_dict['Мания']
        
        self.Abhorrence_d = data_dict['Ненависть']
        self.Spite_d = data_dict['Враждебность']
        self.DisAffection_d = data_dict['Неприязнь']
        self.Fright_d = data_dict['Страх']
        
        self.Rep_SUM_d = data_dict['Репутационный Бал']
        
        self.Fund_Description_d = data_dict['Данные о Личности']
        self.Local_Description_d = data_dict['Мнение о Личности']
        
        self.Char_1_id_d = data_dict['Черта Характера 1']
        self.Char_2_id_d = data_dict['Черта Характера 2']
        self.Char_3_id_d = data_dict['Черта Характера 3']
        
        self.Relation_From_id_d = data_dict['Отношение от']
        self.Relation_To_id_d = data_dict['Отношение к']
        
        
        self.__connection = psycopg2.connect(
        
                host = host,
                user = user,
                password = password,
                database = db_name
                )
        
        self.__cursor = self.__connection.cursor()# Можно перенести функцию сюда



    def new_user(self):

        try:
            insert_query = """ INSERT INTO public."Asiya_person_memory" (unic_id,first_name,sur_name,appearance,gender,birthday,
                                                meet_date,affection,sympathy,friendship,admiration,mania,
                                                abhorrence,spite,disaffection,fright,
                                                rep_sum,fund_description,local_description,relation_from_id,relation_to_id) VALUES """ + f"""
                                              ({self.unic_id_d}, '{self.first_name_d}', '{self.sur_name_d}','{self.Appearance_d}','{self.gender_d}','{self.birthday_d}',
                                               '{self.Meet_Date_d}',{self.Affection_d},{self.Sympathy_d},{self.FriendShip_d},{self.Admiration_d},{self.Mania_d},
                                               {self.Abhorrence_d},{self.Spite_d},{self.DisAffection_d},{self.Fright_d},
                                               {self.Rep_SUM_d},'{self.Fund_Description_d}','{self.Local_Description_d}',{self.Relation_From_id_d},{self.Relation_To_id_d});"""
            self.__cursor.execute(insert_query)
            self.__connection.commit()
                    
        
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')

    
    def get_user(self):
        """
        return dict with data Where unic_id equal current_user.id
        """
        try:
            select_query = f"""SELECT * FROM public."Asiya_person_memory" WHERE unic_id = '{self.unic_id_d}' ;"""
            self.__cursor.execute(select_query)

            print(f'Данные пользователя по ID - [{self.unic_id_d}] . Получены. ')

            pulled_data = convert_to_dict(self.__cursor.fetchall())
            #print(f'Данные пользователя : {pulled_data}')
            return pulled_data

        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')

    
