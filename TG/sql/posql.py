import psycopg2
from datetime import date
from .conf import db_name,host,user,password
from Functional.PM_Func import CTD_single,CTD_many, rep_refresh
"""
Нужно сделать связующую дб фукцию для каждого табла.
Ну скорее всего я потом буду объеденять эти три класс в один, ну если конечно в это есть необходимость
"""
#Person Memory

class Person_add:
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



    def person(self):
        # В случае возникновения проблем в этом классе, попробуй перенести переменные инита сюда
        """
        Person_Memory create data
        """
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



class Person_get:
    
    def person(self,id): # Person_Memory get data
        """
        Person_Memory get data
        return dict with data Where unic_id equal current_user.id
        """
        try:
            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()



            select_query = f"""SELECT * FROM public."Asiya_person_memory" WHERE unic_id = '{id}' ;"""
            cursor.execute(select_query)

            print(f'Данные пользователя по ID - [{id}] . Получены. ')

            pulled_data = CTD_single(cursor.fetchall())
            #print(f'Данные пользователя : {pulled_data}')
            return pulled_data

        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')
    
    def top_persons(self):
        """
        get 10 Persons with highest rep_sum
        """
        try:
            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()



            select_query = """SELECT * FROM public."Asiya_person_memory"
                                                    ORDER BY unic_id ASC LIMIT 10
                                                    """
            cursor.execute(select_query)

            pulled_data = CTD_many(cursor.fetchall())
            return pulled_data
            
            
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')
        

class Person_Edit:
    def __init__(self):
        self.__connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
        self.__cursor = self.__connection.cursor()


    def reputation(self,relate,value,user_data):
        """
        relate = 
        affection = Любовь
        sympathy = Симпатия
        friendship = Дружба
        admiration = Восхищение

        mania = Мания

        abhorrence = Ненависть
        spite = Враждебность
        disaffection = Неприязнь
        fright = Страх

        value = int
        user_data = dict

        """
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                               {relate} = '{value}'::double precision WHERE
                               unic_id = '{user_data['ID']}'; """

            self.__cursor.execute(update_query)
            self.__connection.commit()
            pull_data = Get_data()
            usr_data = pull_data.person(user_data['ID'])
            new_data = rep_refresh(usr_data)
            rep_sum_query  = f"""UPDATE public."Asiya_person_memory" SET
                               rep_sum = '{new_data['Репутационный Бал']}'::double precision WHERE
                               unic_id = '{new_data['ID']}'; """
            self.__cursor.execute(rep_sum_query)
            self.__connection.commit()


        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def gender(self,gen,id):
        """
        gen = 'male','None','female'
        """
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                gender = '{gen}'::character varying WHERE
                                unic_id = '{id}'; """
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def b_day(self,date,id):
        """
        date = 'YYYY-MM-DD'
        """
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                birthday = '{date}'::date WHERE
                                unic_id = '{id}';"""
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def fund_des(self,des,id):
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                fund_description = '{des}'::text WHERE
                                unic_id = '{id}';"""
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def local_des(self,des,id):
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                local_description = '{des}'::text WHERE
                                unic_id = '{id}';"""
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def relate_from(self,relate_id,id):
        """
        relate id:
            1 - Незнакомец
            2 - Дочь
        """
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                relation_from_id = '{relate_id}'::bigint WHERE
                                unic_id = '{id}';"""
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def relate_to(self,relate_id,id):
        """
        relate id:
            1 - Незнакомец
            2 - Дочь
        """
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                relation_to_id = '{relate_id}'::bigint WHERE
                                unic_id = '{id}';"""
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def char_tag_first(self,char_id,id):
        """
        char id:
            1 - Нарциссизм
        """
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                char_1_id = '{char_id}'::bigint WHERE
                                unic_id = '{id}';"""
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def char_tag_second(self,char_id,id):
        """
        char id:
            1 - Нарциссизм
        """
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                char_2_id = '{char_id}'::bigint WHERE
                                unic_id = '{id}';"""
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')


    def char_tag_third(self,char_id,id):
        """
        char id:
            1 - Нарциссизм
        """
        try:
            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                char_3_id = '{char_id}'::bigint WHERE
                                unic_id = '{id}';"""
            self.__cursor.execute(update_query)
            self.__connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ', _ex)
        
        finally:
            if self.__connection:
                self.__connection.close()
                print('Дб отключена')
        
        

        
class Person_Del:

    pass





#Verbal Memory
# Word Memory
class VM_Word:
    
    class New:

        def learn_word(self):
            pass

    class Get:
        pass
    class Edit:
        pass
    class Del:
        pass
