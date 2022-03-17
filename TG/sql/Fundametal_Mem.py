from logging import exception
import psycopg2
from datetime import date
from .conf import db_name,host,user,password


"""
Ego
Episode_Memory
Semantic_Memory
Constant_Expr
EM_Type (Это тип воспоминания эпизодического)
"""


class Ego:
    """
    С получением внешности пока отложим, пушо это довольно проблемно.
    """
    class Get:
        def personal(self):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f""" SELECT * FROM public."Asiya_ego" WHERE id = '1' """
                cursor.execute(select_query)

                raw_data = cursor.fetchone()
                
                name = raw_data[2]
                sur_name = raw_data[3]
                age = raw_data[4]
                birthday = str(raw_data[5])

                the_data = [name,sur_name,age,birthday]
                return the_data

                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Ego [Get - Personal]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
    class Edit:
        pass

class Const_Exp:
    class New:
        def constant(self,const,type):
            """
            type = 
                Very_Good
                Good
                Neutral
                Bad
                Very_Bad
            """
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                #reg_date = str(date.today())

                insert_query = f"""INSERT INTO public."Asiya_constant_expression" (
                                    const_expr, const_type) VALUES (
                                    '{const}'::text, '{type}'::character varying)
                                     returning id;"""
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Const_Expr [New - Constant]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
        
    class Get:
        def all_Constants(self):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_constant_expression" """
                cursor.execute(select_query)
                raw_data = cursor.fetchall()

                pulled_data = []
                for rate in raw_data:
                    former = {}
                    former['ID'] = rate[0]
                    former['Const'] = rate[1]
                    former['Const_Type'] = rate[2]
                    pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Const_Expr [Get - All_Constants]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_Const_id(self,id):
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_constant_expression" WHERE id = '{id}' """
                cursor.execute(select_query)

                raw_data = cursor.fetchone()
                pulled_data = []
                
                former = {}
                former['ID'] = raw_data[0]
                former['Const'] = raw_data[1]
                former['Const_Type'] = raw_data[2]

                pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Const_Expr [Get - by_const_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_rate_type(self,relation):
            """
            Relation = Very_Good 
                        Good
                        Neutral
                        Bad
                        Very_Bad
            """
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_constant_expression" WHERE const_type = '{relation}' """
                cursor.execute(select_query)

                raw_data = cursor.fetchall()

                pulled_data = []
                for rate in raw_data:
                    former = {}
                    former['ID'] = rate[0]
                    former['Const'] = rate[1]
                    former['Const_Type'] = rate[2]
                    pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Const_expr [Get - by_rate_type]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


        def by_name(self,name):
            """
            Relation = Very_Good 
                        Good
                        Neutral
                        Bad
                        Very_Bad
            """
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_constant_expression" WHERE const_expr = '{name}' """
                cursor.execute(select_query)

                raw_data = cursor.fetchone()
                pulled_data = []
                
                former = {}
                former['ID'] = raw_data[0]
                former['Const'] = raw_data[1]
                former['Const_Type'] = raw_data[2]

                pulled_data.append(former)

                return pulled_data
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Const_expr [Get - by_name]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

    class Edit:
        def change_type_by_id(self,id,new_relation):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                edit_query = f"""UPDATE public."Asiya_constant_expression" SET
                                    const_type = '{new_relation}'::character varying WHERE
                                    id = '{id}';"""
                cursor.execute(edit_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Const_Expr [Edit - By id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


        def change_type_by_const(self,const,new_relation):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                edit_query = f"""UPDATE public."Asiya_constant_expression" SET
                                    const_type = '{new_relation}'::character varying WHERE
                                    const_expr = '{const}';"""
                cursor.execute(edit_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Const_Expr [Edit - By Const]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
        

class EM_Type:
    class New:
        def Memory_Type(self,type):
            """
            
            """
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                #reg_date = str(date.today())

                insert_query = f"""INSERT INTO public."Asiya_em_type" (
                                        emt) VALUES (
                                        '{type}'::character varying)
                                         returning id;"""
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Em_Type [New - Memory_Type]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
    class Get:
        def by_id(self,id):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_em_type" WHERE id = '{id}' """
                cursor.execute(select_query)

                raw_data = cursor.fetchall()
                pulled_data = []
                
                former = {}
                former['ID'] = raw_data[0]
                former['Mtype'] = raw_data[1]
                

                pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Em_Type [Get - by_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def by_type(self,type):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                

                select_query = f"""SELECT * FROM public."Asiya_em_type" WHERE type = '{type}' """
                cursor.execute(select_query)

                raw_data = cursor.fetchall()
                pulled_data = []
                
                former = {}
                former['ID'] = raw_data[0]
                former['Mtype'] = raw_data[1]
                

                pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Em_Type [Get - by_type]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
        

class Episode_Memory:
    class New:
        def remember(self,episode,ems_id,emt,user_id=None):
            """
            episode = Содержание Воспоминания
            ems_id(Emote_Score_Id) = from Emote_Reg ID
            emt = from Em_Type Id
            user_id = (change only if required)*
            
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

                insert_query = f"""INSERT INTO public."Asiya_episode_memory" (
                                    episode, dor, emote_score_id, emote_type_id, share_with_id) VALUES (
                                    '{episode}'::text, '{reg_date}'::date, '{ems_id}'::bigint, '{emt}'::bigint, '{user_id}'::character varying)
                                     returning id;"""
                
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Episode_Memory [New - Remember]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
    class Get:
        """
        Вероятно придется делать больше, пушо в теории воспоминание может понадобится при оценке репутации
        """
        def get_all(self):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                #reg_date = str(date.today())

                select_query = f"""SELECT * FROM public."Asiya_episode_memory"
                                                            ORDER BY id ASC """
                
                cursor.execute(select_query)
                raw_data = cursor.fetchall()

                pulled_data = []
                for ep in raw_data:
                    former = {}
                    former['ID'] = ep[0]
                    former['Mem_Content'] = ep[1]
                    former['Date'] = ep[2]
                    former['Em_Score'] = ep[3]
                    former['Em_Type'] = ep[4]

                    try:
                        former['ShareWith'] = ep[5]
                    except Exception as _ex:
                        print('В данном воспоминание нет места для пользователя', _ex)
                    pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Episode_Memory [Get - All]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def get_by_id(self,id):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                #reg_date = str(date.today())

                select_query = f"""SELECT * FROM public."Asiya_episode_memory" WHERE id = '{id}'
                                                            ORDER BY id ASC """
                
                cursor.execute(select_query)
                raw_data = cursor.fetchone()

                pulled_data = []
                
                former = {}
                former['ID'] = ep[0]
                former['Mem_Content'] = ep[1]
                former['Date'] = ep[2]
                former['Em_Score'] = ep[3]
                former['Em_Type'] = ep[4]

                try:
                    former['ShareWith'] = ep[5]
                except Exception as _ex:
                    print('В данном воспоминание нет места для пользователя', _ex)
                pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Episode_Memory [Get - By_Id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def get_by_type(self,type):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                #reg_date = str(date.today())

                select_query = f"""SELECT * FROM public."Asiya_episode_memory" WHERE emote_type_id = '{type}'
                                                            ORDER BY id ASC """
                
                cursor.execute(select_query)
                raw_data = cursor.fetchall()

                pulled_data = []
                for ep in raw_data:
                    former = {}
                    former['ID'] = ep[0]
                    former['Mem_Content'] = ep[1]
                    former['Date'] = ep[2]
                    former['Em_Score'] = ep[3]
                    former['Em_Type'] = ep[4]

                    try:
                        former['ShareWith'] = ep[5]
                    except Exception as _ex:
                        print('В данном воспоминание нет места для пользователя', _ex)
                    pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Episode_Memory [Get - By_Type]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

    class Edit:
        def rewrite_episode_by_id(self,new_ep,id):
            
            
            
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                reg_date = str(date.today())

                insert_query = f"""UPDATE public."Asiya_episode_memory" SET
                                    episode = '{new_ep}'::text WHERE
                                        id = '{id}';"""
                
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Episode_Memory [Edit - Rewrite_Ep_by_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

       

class Semantic_Memory:
    class New:
        def learn(self,source=None,veracity,note):
            """
            Note = Содержание Воспоминания
            
            veracity = float value
            Source = (change to User_Id only if required)*
            
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

                insert_query = f"""INSERT INTO public."Asiya_semantic_memory" (
                                    don, von, note, son_id) VALUES (
                                    '{reg_date}'::date, 
                                    '{veracity}'::double precision, 
                                    '{note}'::text, 
                                    '{source}'::character varying)
                                    returning id;"""
                
                cursor.execute(insert_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Semantic_Memory [New - Learn]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
    class Get:
        def get_all(self):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                #reg_date = str(date.today())

                select_query = f"""SELECT * FROM public."Asiya_semantic_memory"
                                                            ORDER BY id ASC """
                
                cursor.execute(select_query)
                raw_data = cursor.fetchall()

                pulled_data = []
                for ep in raw_data:
                    former = {}
                    former['ID'] = ep[0]
                    former['Date'] = ep[1]
                    former['Veracity'] = ep[2]
                    former['Note'] = ep[3]
                    

                    try:
                        former['Source'] = ep[4]
                    except Exception as _ex:
                        print('В данном знании нет пользователя', _ex)
                    pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Semantic Memory [Get - All]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')


        def get_by_id(self,id):
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                #reg_date = str(date.today())

                select_query = f"""SELECT * FROM public."Asiya_semantic_memory"
                                                            ORDER BY id ASC """
                
                cursor.execute(select_query)
                raw_data = cursor.fetchone()

                pulled_data = []
                
                former = {}
                former['ID'] = ep[0]
                former['Date'] = ep[1]
                former['Veracity'] = ep[2]
                former['Note'] = ep[3]
                

                try:
                    former['Source'] = ep[4]
                except Exception as _ex:
                    print('В данном знании нет пользователя', _ex)
                pulled_data.append(former)

                return pulled_data
                #connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Semantic Memory [Get - By_Id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')
       

    class Edit:
        def change_veracity(self,new_vera,id):
            """
            id of knowledge
            """
       
            try:
            
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                #reg_date = str(date.today())

                update_query = f"""UPDATE public."Asiya_semantic_memory" SET
                                        von = '{new_vera}'::double precision WHERE
                                            id = '{id}';"""
                
                cursor.execute(update_query)
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Semantic [Edit - Veracity]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        
