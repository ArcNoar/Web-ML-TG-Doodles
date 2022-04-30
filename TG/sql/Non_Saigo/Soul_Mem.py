import psycopg2
from datetime import date
from .conf import db_name,host,user,password
from Functional.EMR_Func import ETD_single, ETD_many


"""
Identity
Like_Dislike
Motives
postulates
Emote_Reg
"""

class Emote_Reg:
    def Em_Code_Create(self,em_dict):
        """
        Возвращает строку = '-Domin_Name-|Code|Code|Code -Sup_Name-|Code|Code|Code'
        """

       
        Code_Ref = {
            'СТРАХ' : {
                'Hrr' : 'Ужас',
                'Anx' : 'Тревога',
                'Crn' : 'Беспокойство',
                'Ast' : 'Удивление',
                'Cnf' : 'Замешательство', 
                'Tmd' : 'Робость',
                'Glt' : 'Вина', 
                'Emb' : 'Смущение', 
                'Dbt' : 'Сомнение'
            },
            'ГНЕВ' : {
                'Rge' : 'Ярость', 
                'Irr' : 'Раздражение', 
                'Rsn' : 'Обида',
                'Dgt' : 'Отвращение', 
                'Jls' : 'Ревность', 
                'Env' : 'Зависть',
                'Idn' : 'Негодование', 
                'Nrs' : 'Нервозность', 
                'Dsp' : 'Разочарование'
            },
            'ГРУСТЬ' : {
                'Idl' : 'Лень',
                'Dst' : 'Отчаяние',
                'Cmp' : 'Жалость',
                'Lns' : 'Отрешенность',
                'Hls' : 'Беспомощность',
                'Afs' : 'Отчужденность',
                'Rgt' : 'Сожаление',
                'Bdm' : 'Скука',
                'Sdn' : 'Печаль'
            },
            'РАДОСТЬ' : {
                'Hps' : 'Счастье',
                'Dlt' : 'Восторг',
                'Ist' : 'Интерес',
                'Ext' : 'Возбуждение',
                'Cty' : 'Любопытство',
                'Cfd' : 'Уверенность',
                'Hrn' : 'Влечение',
                'Lgh' : 'Смех',
                'Stf' : 'Удовлетворение'
            }
        }
    
        Sum_Of_aspects = {}
        sorted_sum_aspects = []
    
        def get_key(d, value):
            for k, v in d.items():
                if v == value:
                    return k
    
        # Получаем Доминирующую Эмоцию и Сопутствующую путем сравнения сум Эмоций.
        for emote in em_dict:
            em_value = sum(em_dict[f"{emote}"].values())
            em_value = f'{em_value:.1f}'
            #print(f' Балл эмоции -  {emote} : {em_value} \n' + ('-' * 10))
            Sum_Of_aspects[f'{emote}'] = float(em_value)
    
        sorted_sum_aspects = sorted((list(Sum_Of_aspects.values())))
        sorted_sum_aspects.reverse() # Сортируем и реверсим для удобства
    
        Domin_Emote = get_key(Sum_Of_aspects,max(sorted_sum_aspects))
        
        Sup_Emote = get_key(Sum_Of_aspects,sorted_sum_aspects[1])
    
        DE_dict = em_dict[f'{Domin_Emote}']
        
        SE_dict = em_dict[f'{Sup_Emote}']
        
        def Code_construct(domin_list,sup_list): # Конструируем код Эмоции
            DE_list = sorted(list(domin_list.values()))
            DE_list.reverse()
            SE_list = sorted(list(sup_list.values()))
            SE_list.reverse()
            
            def NM_Create(some_list,some_dict): # Создание упорядоченного списка Аспектов Эмоций
                Value_list = []
                Name_List = []
                for aspect in some_list:
                    if aspect < 0.5:
                        #print('Нулевой Аспект - прекращаем цикл')
                        break
                    else:
                        Value_list.append(aspect)
                for value in Value_list:
                    Name_List.append(get_key(some_dict,value))
    
                return Name_List
    
            Domin_NL = NM_Create(DE_list,DE_dict)
            Sup_NL = NM_Create(SE_list,SE_dict)
            Sum_NL = Domin_NL + Sup_NL
            
            """
            
            Это можно в теории улучшить по оптимизации.
            """
            def Code_Creating(name_list,Dom_Em,Sup_Em): # Сопоставляем с референсом кодировки и строим Код Эмоции
                Code_List = []
                Emote_Code = f'-{Dom_Em}-|'
                #print(name_list)
                #print(Code_Ref[f'{Dom_Em}'])
                for aspect_name in name_list:
                    #print(aspect_name)
                    key = get_key(Code_Ref[f'{Dom_Em}'],aspect_name)
                    if key != None:
                        Code_List.append(key)
                if sorted_sum_aspects[1] == 0.0:
                    pass
                else:
                    Code_List.append(f' -{Sup_Em}-')
                    for aspect_name in name_list:
                        key = get_key(Code_Ref[f'{Sup_Em}'],aspect_name)
                        if key != None:
                            Code_List.append(key)
                
                #print(Code_List)   
                Emote_Code = Emote_Code + '|'.join(Code_List)
                return Emote_Code
            return Code_Creating(Sum_NL,Domin_Emote,Sup_Emote)
        
        return Code_construct(DE_dict,SE_dict)
        


    """
    В шифровке имени эмоции прям большого смысла нет, потому что нейронка при подключении к дб
    сразу получит все значения и там нужна будет чисто фильтрация лишних значений по тому же принципу что я шифровал
    тип эта кодировка не несет за собой никаких значений в отличии от айдишников слов которые были.
    Это больше навигационная штука, чтоб отсеивать эмоции при поиске.
    """
    
    class New:
        def __init__(self,em_data):
            # 
            self.__Emote_Components = em_data['Эмоция']
            __code_func = Emote_Reg()

            self.Em_Code = __code_func.Em_Code_Create(self.__Emote_Components)
            self.EMT_id = em_data['Сущность-Триггер']
            self.Et_Type = em_data['Тип Триггера']
            self.Et_Descript = em_data['Описание']
            self.Et_Date = em_data['Дата']
            
            #General Emotes
            self.Fear = em_data['Эмоция']['СТРАХ']
            self.Anger = em_data['Эмоция']['ГНЕВ']
            self.Sorrow = em_data['Эмоция']['ГРУСТЬ']
            self.Joy = em_data['Эмоция']['РАДОСТЬ']

        def emote_reg(self):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()




                insert_query = f"""INSERT INTO public."Asiya_emote_reg" (
                                emote_name,emote_trigger_id, et_type, et_descript, et_date,

                                horror, anxiety, concern, astonishment, confusion, timidity, guilt, embarrassment, doubt,
                                rage, irritation, resentment, disgust, jealousy, envy, indignation, nervousness, disappointment, 
                                idleness, despait, compassion, loneliness, helplessness, aloofness, regret, boredom, sadness,
                                happiness, delight, interest, excitement, curiosity, confidence, horny, laugh, satisfaction)
                                VALUES (
                                '{self.Em_Code}'::character varying, '{self.EMT_id}'::character varying, '{self.Et_Type}'::character varying, '{self.Et_Descript}'::text, '{self.Et_Date}'::date,

                                '{self.Fear["Ужас"]}'::double precision, '{self.Fear["Тревога"]}'::double precision, '{self.Fear["Беспокойство"]}'::double precision, '{self.Fear["Удивление"]}'::double precision, '{self.Fear["Замешательство"]}'::double precision, '{self.Fear["Робость"]}'::double precision, '{self.Fear["Вина"]}'::double precision, '{self.Fear["Смущение"]}'::double precision, '{self.Fear["Сомнение"]}'::double precision,
                                '{self.Anger["Ярость"]}'::double precision, '{self.Anger["Раздражение"]}'::double precision, '{self.Anger["Обида"]}'::double precision, '{self.Anger["Отвращение"]}'::double precision, '{self.Anger["Ревность"]}'::double precision, '{self.Anger["Зависть"]}'::double precision, '{self.Anger["Негодование"]}'::double precision, '{self.Anger["Нервозность"]}'::double precision, '{self.Anger["Разочарование"]}'::double precision,
                                '{self.Sorrow["Лень"]}'::double precision, '{self.Sorrow["Отчаяние"]}'::double precision, '{self.Sorrow["Жалость"]}'::double precision, '{self.Sorrow["Отрешенность"]}'::double precision, '{self.Sorrow["Беспомощность"]}'::double precision, '{self.Sorrow["Отчужденность"]}'::double precision, '{self.Sorrow["Сожаление"]}'::double precision, '{self.Sorrow["Скука"]}'::double precision, '{self.Sorrow["Печаль"]}'::double precision,
                                '{self.Joy["Счастье"]}'::double precision, '{self.Joy["Восторг"]}'::double precision, '{self.Joy["Интерес"]}'::double precision, '{self.Joy["Возбуждение"]}'::double precision, '{self.Joy["Любопытство"]}'::double precision, '{self.Joy["Уверенность"]}'::double precision, '{self.Joy["Хорни"]}'::double precision, '{self.Joy["Смех"]}'::double precision, '{self.Joy["Удовлетворение"]}'::double precision)
                                 returning id;"""
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [EMOTE_REG [New - emote_reg]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
            

    class Get:
        def get_by_id(self,id):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Asiya_emote_reg" WHERE id = '{id}' ;"""
                cursor.execute(select_query)

                #print(f'Данные пользователя по ID - [{id}] . Получены. ')

                pulled_data = ETD_single(cursor.fetchall())
                
                return pulled_data

            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Emote_Reg [Get-get_by_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

        """
        Get by Emote_Code
        """
        def get_by_main_emote(self,main_emote):
            
            
          
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Asiya_emote_reg" WHERE emote_name LIKE '-{main_emote}-%' ;"""
                cursor.execute(select_query)

                #print(f'Данные пользователя по ID - [{id}] . Получены. ')

                pulled_data = ETD_many(cursor.fetchall())
                
                return pulled_data

            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Emote_Reg [Get-get_by_main_emote]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

        def get_by_code(self,full_code):
            
            
          
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Asiya_emote_reg" WHERE emote_name = '{full_code}' ;"""
                cursor.execute(select_query)

                #print(f'Данные пользователя по ID - [{id}] . Получены. ')

                pulled_data = ETD_single(cursor.fetchall())
                
                return pulled_data

            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Emote_Reg [Get-get_by_code]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')


    class Edit:
        """
        Не вижу необходимости в этом.
        """
        pass
    class Del:
        """
        Не вижу необходимости в этом.
        """
        pass
    




#Identity
class Identity:

    class New:
        def __init__(self,Info_list):
            self.Emo_State = Info_list['Эмоция']
            self.Motive = Info_list['Мотив']
            self.Note = Info_list['Комментарий']
            self.Note_date = Info_list['Дата']

        def Iden_infix(self):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                insert_query = f"""INSERT INTO public."Asiya_identity" (
                                      comment, reg_date, current_motive_id, emote_condition_id) VALUES (
                                      '{self.Note}'::text, '{self.Note_date}'::date, '{self.Motive}'::bigint, '{self.Emo_State}'::bigint)
                                       returning id;"""

                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Identity [New - Iden_infix ]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


    class Get:
        def all_Notes(self):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                insert_query = f"""SELECT * FROM public."Asiya_identity" """
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Identity [Get - All_Notes]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_note_id(self,id):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                insert_query = f"""SELECT * FROM public."Asiya_identity" WHERE id = '{id}' """
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Identity [Get - by_note_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_emote_state_id(self,id):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                insert_query = f"""SELECT * FROM public."Asiya_identity" WHERE emote_condition_id = '{id}' """
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Identity [Get - by_emote_state_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


        def by_motive_id(self,id):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                insert_query = f"""SELECT * FROM public."Asiya_identity" WHERE current_motive_id = '{id}' """
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Identity [Get - by_motive_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')



#Motives 
class Motives:

    class New:
        def will(self,content):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                reg_date = str(date.today())

                insert_query = f"""INSERT INTO public."Asiya_motives" (
                                    aspiration, reg_date) VALUES (
                                    '{content}'::text, '{reg_date}'::date)
                                     returning id;"""
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Motives [New - will]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

    
    class Get:
        def all_wishes(self):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                insert_query = f"""SELECT * FROM public."Asiya_motives" """
                cursor.execute(insert_query)
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Motives [Get - All_wishes]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_will_id(self,id):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                insert_query = f"""SELECT * FROM public."Asiya_motives" WHERE id = '{id}' """
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Motives [Get - by_will_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        

    class Forget:
        pass

#Like_Dislike
class Like_Dislike:

    class New:
        def rate_subject(self,subject,relation):
            """
            Relation = Like / Neutral / Dislike
            """
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                reg_date = str(date.today())

                insert_query = f"""INSERT INTO public."Asiya_like_dislike" (
                                        subject, reg_date, rel_to) VALUES (
                                        '{subject}'::text, '{reg_date}'::date, '{relation}'::character varying)
                                         returning id;"""
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Like_Dislike [New - Rate_Subject]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


    class Get:
        def all_Rates(self):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_like_dislike" """
                cursor.execute(select_query)
                raw_data = cursor.fetchall()

                pulled_data = []
                for rate in raw_data:
                    former = {}
                    former['ID'] = rate[0]
                    former['Subject'] = rate[1]
                    former['Date'] = rate[2]
                    former['Rate_Type'] = rate[3]
                    pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Like_Dislike [Get - All_Rates]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_rate_id(self,id):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_like_dislike" WHERE id = '{id}' """
                cursor.execute(select_query)
                raw_data = cursor.fetchone()

                pulled_data = []
                
                former = {}
                former['ID'] = raw_data[0]
                former['Subject'] = raw_data[1]
                former['Date'] = raw_data[2]
                former['Rate_Type'] = raw_data[3]
                pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Like_Dislike [Get - by_rate_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_subject(self,subject):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_like_dislike" WHERE subject = '{subject}' """
                cursor.execute(select_query)
                raw_data = cursor.fetchone()

                pulled_data = []
                
                former = {}
                former['ID'] = raw_data[0]
                former['Subject'] = raw_data[1]
                former['Date'] = raw_data[2]
                former['Rate_Type'] = raw_data[3]
                pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Like_Dislike [Get - by_rate_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_rate_type(self,relation):
            """
            Relation = Like Dislike Neutral
            """
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_like_dislike" WHERE rel_to = '{relation}' """
                cursor.execute(select_query)
                raw_data = cursor.fetchall()

                pulled_data = []
                for rate in raw_data:
                    former = {}
                    former['ID'] = rate[0]
                    former['Subject'] = rate[1]
                    former['Date'] = rate[2]
                    former['Rate_Type'] = rate[3]
                    pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Like_Dislike [Get - by_rate_type]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
        

    class Edit:
        def change_rate_by_id(self,id,new_relation):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                edit_query = f"""UPDATE public."Asiya_like_dislike" SET
                                    rel_to = '{new_relation}'::character varying WHERE
                                    id = '{id}';"""
                cursor.execute(edit_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Like_Dislike [Edit - By id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


        def change_rate_by_subject(self,subject,new_relation):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                edit_query = f"""UPDATE public."Asiya_like_dislike" SET
                                    rel_to = '{new_relation}'::character varying WHERE
                                    subject = '{subject}';"""
                cursor.execute(edit_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Like_Dislike [Edit - By subject]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


#Postulates
class Postulates:

    class New:
        def make_postule(self,postul):
            """
            Relation = Like / Neutral / Dislike
            """
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                reg_date = str(date.today())

                insert_query = f"""INSERT INTO public."Asiya_postulates" (
                                        postul, reg_date) VALUES (
                                        '{postul}'::text, '{reg_date}'::date)
                                         returning id;"""
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Postulates [New - make_postule]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


    class Get:
        def all_Postuls(self):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_postulates" """
                cursor.execute(select_query)
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Postulates [Get - All_Postuls]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_postul_id(self,id):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_postulates" WHERE id = '{id}' """
                cursor.execute(select_query)
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Postulates [Get - by_postul_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        
        

    class Edit:
        def change_postul_by_id(self,id,edited_postul):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                edit_query = f"""UPDATE public."Asiya_postulates" SET
                                    postul = '{edited_postul}'::character varying WHERE
                                    id = '{id}';"""
                cursor.execute(edit_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Postulates [Edit - By id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

