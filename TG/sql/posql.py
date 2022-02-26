import psycopg2
from datetime import date
from .conf import db_name,host,user,password
from Functional.PM_Func import CTD_single,CTD_many, rep_refresh
from Functional.VMW_Func import WTD_single, WTD_many
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
        



    def person(self):
        # В случае возникновения проблем в этом классе, попробуй перенести переменные инита сюда
        """
        Person_Memory create data
        """
        try:

            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()




            insert_query = """ INSERT INTO public."Asiya_person_memory" (unic_id,first_name,sur_name,appearance,gender,birthday,
                                                meet_date,affection,sympathy,friendship,admiration,mania,
                                                abhorrence,spite,disaffection,fright,
                                                rep_sum,fund_description,local_description,relation_from_id,relation_to_id) VALUES """ + f"""
                                              ({self.unic_id_d}, '{self.first_name_d}', '{self.sur_name_d}','{self.Appearance_d}','{self.gender_d}','{self.birthday_d}',
                                               '{self.Meet_Date_d}',{self.Affection_d},{self.Sympathy_d},{self.FriendShip_d},{self.Admiration_d},{self.Mania_d},
                                               {self.Abhorrence_d},{self.Spite_d},{self.DisAffection_d},{self.Fright_d},
                                               {self.Rep_SUM_d},'{self.Fund_Description_d}','{self.Local_Description_d}',{self.Relation_From_id_d},{self.Relation_To_id_d});"""
            cursor.execute(insert_query)
            connection.commit()
                    
        
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ. [Person_Memory [Add-Person]]', _ex)
        
        finally:
            if connection:
                connection.close()
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

            #print(f'Данные пользователя по ID - [{id}] . Получены. ')

            pulled_data = CTD_single(cursor.fetchall())
            #print(f'Данные пользователя : {pulled_data}')
            return pulled_data

        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ. [Person_Get [Get-Person]]', _ex)
        
        finally:
            if connection:
                connection.close()
                #print('Дб отключена')
    
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
            print('Ошибка в ходе чтения ДБ. [Person_Get [Get-Top_Person]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')
        

class Person_Edit:
    


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
            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()



            update_query = f"""UPDATE public."Asiya_person_memory" SET
                               {relate} = '{value}'::double precision WHERE
                               unic_id = '{user_data['ID']}'; """

            cursor.execute(update_query)
            connection.commit()
            pull_data = Person_get()
            usr_data = pull_data.person(user_data['ID'])
            new_data = rep_refresh(usr_data)
            rep_sum_query  = f"""UPDATE public."Asiya_person_memory" SET
                               rep_sum = '{new_data['Репутационный Бал']}'::double precision WHERE
                               unic_id = '{new_data['ID']}'; """
            cursor.execute(rep_sum_query)
            connection.commit()


        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[Person_Edit [Reputation]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def gender(self,gen,id):
        """
        gen = 'male','None','female'
        """
        try:
            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()




            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                gender = '{gen}'::character varying WHERE
                                unic_id = '{id}'; """
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[Person_Edit [Gender]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def b_day(self,date,id):
        """
        date = 'YYYY-MM-DD'
        """
        try:

            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()




            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                birthday = '{date}'::date WHERE
                                unic_id = '{id}';"""
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[Person_Edit [BirthDay]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def fund_des(self,des,id):
        try:

            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()



            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                fund_description = '{des}'::text WHERE
                                unic_id = '{id}';"""
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[Person_Edit [Fund_Des]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def local_des(self,des,id):
        try:

            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()


            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                local_description = '{des}'::text WHERE
                                unic_id = '{id}';"""
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[Person_Edit [Local_Des]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def relate_from(self,relate_id,id):
        """
        relate id:
            1 - Незнакомец
            2 - Дочь
        """
        try:
            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()

            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                relation_from_id = '{relate_id}'::bigint WHERE
                                unic_id = '{id}';"""
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[Person_Edit [Relate_From]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def relate_to(self,relate_id,id):
        """
        relate id:
            1 - Незнакомец
            2 - Дочь
        """
        try:


            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()



            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                relation_to_id = '{relate_id}'::bigint WHERE
                                unic_id = '{id}';"""
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[Person_Edit [Relate_To]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def char_tag_first(self,char_id,id):
        """
        char id:
            1 - Нарциссизм
        """
        try:

            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()



            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                char_1_id = '{char_id}'::bigint WHERE
                                unic_id = '{id}';"""
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[[Person_Edit [CharTagOne]]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def char_tag_second(self,char_id,id):
        """
        char id:
            1 - Нарциссизм
        """
        try:

            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()




            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                char_2_id = '{char_id}'::bigint WHERE
                                unic_id = '{id}';"""
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[[Person_Edit [CharTagSECOND]]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')


    def char_tag_third(self,char_id,id):
        """
        char id:
            1 - Нарциссизм
        """
        try:

            connection = psycopg2.connect(
            
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                    )
            
            cursor = connection.cursor()




            update_query = f"""UPDATE public."Asiya_person_memory" SET
                                char_3_id = '{char_id}'::bigint WHERE
                                unic_id = '{id}';"""
            cursor.execute(update_query)
            connection.commit()
        except Exception as _ex:
            print('Ошибка в ходе чтения ДБ.[[Person_Edit [CharTagTHIRD]]]', _ex)
        
        finally:
            if connection:
                connection.close()
                print('Дб отключена')
        
        

        
class Person_Del:

    pass





#Verbal Memory
# Word Memory
class VM_Word:
    
    class New:
        def __init__(self,template):
            self.Word = template['Слово']
            self.Polysemantic = template['Многозначность']
            self.Constant_W = template['Константность']

            self.Nomination = template['Нарекающее']
            self.Word_Type = template['Тип']
            self.Word_Gender = template['Род']

            self.Word_Des = template['Значение']
            self.Associated_W_id = template['Ассоциация']
            self.Group_Of_Word_id = template['Синоним']

            self.Synonym_W_id = template['Категория']

        def learn_word(self):
            #

            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                second_query = """INSERT INTO public."Asiya_vm_word" (
                                    word, polysemantic, constant_w, nomination, word_type, word_gender, word_des, associate_w_id, group_of_word_id, synonym_w_id) VALUES """ + f""" (
                                    '{self.Word}'::character varying, {self.Polysemantic}::boolean, {self.Constant_W}::boolean, {self.Nomination}::boolean, 
                                    '{self.Word_Type}'::character varying, '{self.Word_Gender}'::character varying, '{self.Word_Des}'::text, 
                                    {self.Associated_W_id}::bigint, {self.Group_Of_Word_id}::character varying, {self.Synonym_W_id}::bigint)
                                     returning word;"""
                cursor.execute(second_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_WORD-NEW[LEARN_NEW] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Get:

        def one_word(self,the_word):
            try:


                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                select_query = f"""SELECT * FROM public."Asiya_vm_word" WHERE word = '{the_word}'"""
                cursor.execute(select_query)
                pulled_data = WTD_single(cursor.fetchall())
                #print(pulled_data)
                return pulled_data
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[VM_WORD-GET [ONEWORD] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
        def word_by_id(self,word_id):
            try:


                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                select_query = f"""SELECT * FROM public."Asiya_vm_word" WHERE id = '{word_id}'"""
                cursor.execute(select_query)
                pulled_data = WTD_single(cursor.fetchall())
                
                return pulled_data
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[VM_WORD-GET [WORD_BY_ID] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

        def max_id(self):
            try:


                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                select_query = """SELECT * FROM public."Asiya_vm_word"
                                        ORDER BY id DESC LIMIT 1"""
                cursor.execute(select_query)
                pulled_data = WTD_single(cursor.fetchall())
                #print('ВОТ ОН ЭТО МАКСИМАЛЬНЫЙ АЙДИ БРАТ',pulled_data)
                
                return pulled_data
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[VM_WORD-GET [MAX_ID] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
        
    class Edit:
        def poly_type(self,the_word,value):
            """
            value = true/false
            """
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                polysemantic = {value}::boolean WHERE
                                word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-PolyType]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def const_type(self,the_word,value):
            """
            value = false/true
            """
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                constant_w = {value}::boolean WHERE
                                word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-ConstType]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def nomin_type(self,the_word,value):
            """
            value = false/true
            """
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                nomination = {value}::boolean WHERE
                                word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-NominType]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def word_type(self,the_word,type):
            """
            type:
                MOTION
                Descriptor
                NOUN
                STATE
                NOMIN
                SOUND
                PUNKT
                NUM
                UNION
            """
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                    word_type = '{type}'::character varying WHERE
                                    word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-WordType]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def word_gender(self,the_word,gen):
            """
            gen :
                male
                female
                neutral
                NONE
            """
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                    word_gender = '{gen}'::character varying WHERE
                                    word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-Gender]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def word_des(self,the_word,desc):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                    word_des = '{desc}'::text WHERE
                                    word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-Descript]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def associate_w(self,the_word,assoc_id):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                    associate_w_id = {assoc_id}::bigint WHERE
                                    word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-Associate]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def word_gow(self,the_word,gow):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                    group_of_word_id = '{gow}'::character varying WHERE
                                    word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-GOW]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def synonym_w(self,the_word,synon_id):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                    synonym_w_id = {synon_id}::bigint WHERE
                                    word = '{the_word}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-Synonym]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        
    class Del:
        pass


#SENTENCE MEMORY
class VM_Sentence:
    """
    Взять предложение вообще легко, по сути тупо инсертишь.
    Описание, ну пусть будет какое то стандартное я полагаю?
    А вот дешифровка это ептить проблема.
    Нужно же брать в учет фактор того что она не знает какого то слова.
    Ну наверное брать циклом с автозаполнением? Тип если нет результата = ставим Автозаполнение, если есть, ставим айдишник.
    Еще надо будет гет реализовать
    еще надо будет протестить дешифровку, т.е предложение со всеми известными словами как себя поведет,
    а вот эдит я хз че туда, только описание?
    Ну дешифровка это ыа наверное, мб даже не стоит делать автозаполнение??
    В общем, это не такой сложный пункт, но важный очень.
    Я на отпускной, тип увидимся 23-24 числа наверное.
    ____
    Ну теперь эдит контекста, эдит описания.
    Пул дешифвровки,
    пул всего предложения.
    и будет гатово.
    """
    def deschcode(self,sentence):
        Word_Func = VM_Word.Get()
        
        bag_of_word = (sentence).split(' ')
        words_id_list = []
        d_code = ''
        
        for wd in bag_of_word:
            try:
                current_word = Word_Func.one_word(wd)
                words_id_list.append(str(current_word['ID']))
            except Exception as _ex:
                print('Возникла ошиба при дешифрации предложения. [VM_Sentence - deschcode]',_ex)
                words_id_list.append('??')
        d_code = '-'.join(words_id_list)
        return d_code
    class New:
        def __init__(self,template):
            self.Sentence = template['Предложение']
            sent_func = VM_Sentence()
            self.Sent_Desch = sent_func.deschcode(self.Sentence)
            self.Short_Mean = template['Краткая суть']
            self.From_who = template['От кого']
            self.Context = template['Контекст']


        def sent_reg(self):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                add_query = f"""INSERT INTO public."Asiya_sentence_memory" (
                                sentence, sent_dech, short_mean, from_who_id, sent_context_id) VALUES (
                                '{self.Sentence}'::text, '{self.Sent_Desch}'::text, '{self.Short_Mean}'::text, 
                                '{self.From_who}'::character varying, '{self.Context}'::character varying)
                                 returning sentence;"""
                cursor.execute(add_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_Sentence-NEW[SENT_REG] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        
            

