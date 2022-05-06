import psycopg2

from .conf_Saigo import db_name,host,user,password

from Functional.Prima_Func import STD_Prima, WTD_Prima, WTDM_Prima





class VM_Alph:
    class New:
        def add_construct(self,cstr,type='NUM'):
            try:

                connection = psycopg2.connect(
        
                                host = host,
                                user = user,
                                password = password,
                                database = db_name
                                )
                
                cursor = connection.cursor()


                second_query = f"""INSERT INTO public."Prima_Word_vm_alph" (
                                    construct, alp_t) VALUES (
                                    '{cstr}'::character varying, '{type}'::character varying)
                                     returning id;"""

                cursor.execute(second_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                #print('Ошибка в ходе чтения ДБ.[[Prima_ALPH-NEW[NEW_CONSTRUCT] ]', _ex)
                pass

            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
            
            

    class Get:
        
        def get_by_construct(self,cstr):
            try:

                connection = psycopg2.connect(
        
                            host = host,
                            user = user,
                            password = password,
                            database = db_name
                            )
                
                
                cursor = connection.cursor()


                select_query = f"""SELECT * FROM public."Prima_Word_vm_alph" WHERE construct = '{cstr}' """
                cursor.execute(select_query)
                raw_data = cursor.fetchall()
                
                #print(raw_data)
                data_dict = {}

                pulled_data = []
                
                for elem in raw_data:
                    data_dict['ID'] = elem[0]
                    data_dict['Конструкт'] = elem[1]
                    data_dict['Тип'] = elem[2]
                    
                    pulled_data.append(data_dict)
                
                return pulled_data[0]
                
                        
            
            except Exception as _ex:
                #print('Ошибка в ходе чтения ДБ.[[PRIMA_ALPH-GET[BY CONSTRUCT] ]', _ex)
                pass
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')


class VM_Word:
    def constuct_code(self,word):
        Alph_Get = VM_Alph.Get()

        some_word = word
        
        constr_id_list = []
        c_code = ''
        
        for constr in some_word:
            try:
                
                current_constr = Alph_Get.get_by_construct(constr)

                constr_id_list.append(str(current_constr['ID']))

            except Exception as _ex:
                pass
                #print('Ошибка в дешифраторе конструктов. [VM_Word - Construct Code]',_ex)
                #constr_id_list.append('0')

        c_code = '-'.join(constr_id_list)
        return c_code



    class New:
        def __init__(self,template):
            self.Word = template['Слово']
            self.W_X = template['X_Cord']
            self.W_Y = template['Y_Cord']
            self.Group_Id = template['Категория']
            self.SpecF = template['SF']
            self.W_Type = template['Тип']
            constr_func = VM_Word()
            self.W_Code = constr_func.constuct_code(self.Word)
            

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


                second_query = f"""INSERT INTO public."Prima_Word_vm_word" (
                                word,word_code,x_cord,y_cord,special_field, group_of_word_id,word_type) VALUES (
                                '{self.Word}'::character varying, '{self.W_Code}'::character varying,
                                '{self.W_X}'::double precision,'{self.W_Y}'::double precision,
                                '{self.SpecF}'::character varying,
                                 '{self.Group_Id}'::bigint,
                                 '{self.W_Type}'::character varying)
                                 returning id;"""
                cursor.execute(second_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_WORD-NEW[LEARN_NEW] ]', _ex)
                pass
            
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


                select_query = f""" SELECT * FROM public."Prima_Word_vm_word" WHERE word = '{the_word}' """
                cursor.execute(select_query)
                raw_data = cursor.fetchall()
                #print(raw_data)
                pulled_data = WTD_Prima(raw_data)
                #print(pulled_data)
                #print(pulled_data)
                return pulled_data
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[VM_WORD-GET [ONEWORD] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')


        def word_by_id(self,id):
            try:


                connection = psycopg2.connect(

                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                select_query = f""" SELECT * FROM public."Prima_Word_vm_word" WHERE id = '{id}' """
                cursor.execute(select_query)
                raw_data = cursor.fetchall()
                #print(raw_data)
                pulled_data = WTD_Prima(raw_data)
                #print(pulled_data)
                #print(pulled_data)
                return pulled_data
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[VM_WORD-GET [ONEWORD] ]', _ex)
            
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


                select_query = """SELECT * FROM public."Prima_Word_vm_word"
                                        ORDER BY id DESC LIMIT 1"""
                cursor.execute(select_query)
                pulled_data = WTD_Prima(cursor.fetchall())
                #print('ВОТ ОН ЭТО МАКСИМАЛЬНЫЙ АЙДИ БРАТ',pulled_data)
                
                return pulled_data
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[VM_WORD-GET [MAX_ID] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

        def all(self):
            try:


                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                select_query = """SELECT * FROM public."Prima_Word_vm_word"
                                        ORDER BY id ASC """
                cursor.execute(select_query)
                pulled_data = WTDM_Prima(cursor.fetchall())
                #print('ВОТ ОН ЭТО МАКСИМАЛЬНЫЙ АЙДИ БРАТ',pulled_data)
                
                return pulled_data
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[VM_WORD-GET [ALL] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Edit:
        def X_Cord(self,id,new_x):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Prima_Word_vm_word" SET
                                    x_cord = '{new_x}'::Double Precision WHERE
                                    id = '{id}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-X_CORD]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')


        def Y_Cord(self,id,new_y):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Prima_Word_vm_word" SET
                                    y_cord = '{new_y}'::Double Precision WHERE
                                    id = '{id}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Word_Edit-X_CORD]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')




class VM_Sentence:
    """
    
    """
    def deschcode(self,sentence):
        Word_Func = VM_Word.Get()
        
        bag_of_word = (sentence).split(' ')
        words_id_list = []
        d_code = ''
        
        for wd in bag_of_word:
            try:
                current_word = Word_Func.one_word(wd)
                print(current_word)
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
            self.S_X = template['X_Cord']
            self.S_Y = template['Y_Cord']
            self.Spec_F = template['SF']
            self.Context_id = template['Контекст']


        def sent_reg(self):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                add_query = f"""INSERT INTO public."Prima_Word_sentence_memory" (
                                sentence, sent_dech, x_cord, y_cord,special_field, sent_context_id) VALUES (
                                '{self.Sentence}'::text, '{self.Sent_Desch}'::text,
                                '{self.S_X}'::double precision,'{self.S_Y}'::double precision,
                                '{self.Spec_F}'::character varying,
                                 {self.Context_id}::bigint)
                                 returning sentence;"""
                cursor.execute(add_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[Prima_Sentence-NEW[SENT_REG] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Get:
        """
        Зачем ей доставать предложения если предложения добавляется всегда? Тип слова, потом предложения.
        Что даст сопоставление? (Наверное тогда и париться не буду кек.)
        Мб конечно в будушем при поиске схожих предложений, тип пусть будет ок, но хз.
        """

        def sentence_data(self,proc_sent):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Prima_Word_sentence_memory" WHERE sentence = '{proc_sent}' """
                cursor.execute(select_query)
                pulled_data = STD_Prima(cursor.fetchall())
                
                # 
                return pulled_data
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_SENTENCE [Get-SENTENCE_DATA]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Edit:
        def X_Cord(self,id,new_x):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Prima_Word_sentence_memory" SET
                                    x_cord = '{new_x}'::Double Precision WHERE
                                    id = '{id}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Sent_Edit-X_CORD]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')


        def Y_Cord(self,id,new_y):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Prima_Word_sentence_memory" SET
                                    y_cord = '{new_y}'::Double Precision WHERE
                                    id = '{id}';"""
                cursor.execute(Edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ[Sent_Edit-X_CORD]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')