import psycopg2

from .conf_Saigo import db_name,host,user,password

from Functional.Prima_Func import STD_Prima,MSTD_Prima, WTD_Prima, WTDM_Prima , parse, G_Delay, Prima_word

word_template = Prima_word() # Темплейт запоминания слов
word_params = word_template.create()



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
            #self.Group_Id = template['Категория']
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
                                word,word_code,x_cord,y_cord,special_field,word_type) VALUES (
                                '{self.Word}'::character varying, '{self.W_Code}'::character varying,
                                '{self.W_X}'::double precision,'{self.W_Y}'::double precision,
                                '{self.SpecF}'::character varying,
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




class VM_Correct_Answer:
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
                #print(current_word)
                words_id_list.append(str(current_word['ID']))
            except Exception as _ex:
                print('Возникла ошиба при дешифрации предложения. [VM_Sentence - deschcode]',_ex)

                word_params['Слово'] = wd
                word_params['Тип'] = G_Delay(parse(wd))
                Word_F = VM_Word()
                Word_add = Word_F.New(word_params)
                Word_add.learn_word()
                current_word = Word_Func.one_word(wd)
                #print(current_word)
                words_id_list.append(str(current_word['ID']))
        d_code = '-'.join(words_id_list)
        return d_code
    class New:
        def __init__(self,template):
            self.User_Sent = template['US']
            sent_func = VM_Correct_Answer()
            self.US_Desch = sent_func.deschcode(self.User_Sent)
            self.Answer_Sent = template['AS']
            self.AS_Desch = sent_func.deschcode(self.Answer_Sent)

            self.G1 = template['G1']
            self.G2 = template['G2']
            self.G3 = template['G3']
            self.G4 = template['G4']
            self.G5 = template['G5']
            self.G6 = template['G6']
            self.G7 = template['G7']
            self.G8 = template['G8']
            self.Category_id = template['Категория']
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
                
               


                add_query = f"""INSERT INTO public."Prima_Word_correct_answers" (
                                user_sent, us_dech, actual_resp, ar_dech,
                                g1, g2, g3, g4, g5, g6, g7, g8,
                                category_id, sent_context_id) VALUES (
                                '{self.User_Sent}'::text, '{self.US_Desch}'::text,
                                '{self.Answer_Sent}'::text, '{self.AS_Desch}'::text,
                                {self.G1}::double precision,{self.G2}::double precision,
                                {self.G3}::double precision,{self.G4}::double precision,
                                {self.G5}::double precision,{self.G6}::double precision,
                                {self.G7}::boolean,{self.G8}::boolean,
                                {self.Category_id}::bigint,
                                {self.Context_id}::bigint)
                                 returning id;"""
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
        Pull by User Message
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



                select_query = f"""SELECT * FROM public."Prima_Word_correct_answers" WHERE user_sent = '{proc_sent}' """
                cursor.execute(select_query)

                raw_data = cursor.fetchall().copy()
                if raw_data == []:
                    return False
                else:
                    pulled_data = MSTD_Prima(raw_data)
                    #print(pulled_data)
                    # 
                    return pulled_data
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_SENTENCE [Get-SENTENCE_DATA]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Edit:
        # Когда сможешь филлерить оценки, забьем эдитор.
        pass


class VM_InCorrect_Answer:
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
                #print(current_word)
                words_id_list.append(str(current_word['ID']))
            except Exception as _ex:
                print('Возникла ошиба при дешифрации предложения. [VM_Incor - deschcode]',_ex)
                word_params['Слово'] = wd
                word_params['Тип'] = G_Delay(parse(wd))
                Word_F = VM_Word()
                Word_add = Word_F.New(word_params)
                Word_add.learn_word()
                current_word = Word_Func.one_word(wd)
                #print(current_word)
                words_id_list.append(str(current_word['ID']))
        d_code = '-'.join(words_id_list)
        return d_code
    class New:
        def __init__(self,template):
            
            sent_func = VM_InCorrect_Answer()
           
            self.Answer_Sent = template['AS']
            self.AS_Desch = sent_func.deschcode(self.Answer_Sent)

            self.G1 = template['G1']
            self.G2 = template['G2']
            self.G3 = template['G3']
            self.G4 = template['G4']
            self.G5 = template['G5']
            self.G6 = template['G6']
            self.G7 = template['G7']
            self.G8 = template['G8']
            self.Category_id = template['Категория']
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
                
               


                add_query = f"""INSERT INTO public."Prima_Word_incorrect_answers" (
                                actual_resp, ar_dech,
                                g1, g2, g3, g4, g5, g6, g7, g8,
                                cat_id, sent_contex_id) VALUES (
                                
                                '{self.Answer_Sent}'::text, '{self.AS_Desch}'::text,
                                {self.G1}::double precision,{self.G2}::double precision,
                                {self.G3}::double precision,{self.G4}::double precision,
                                {self.G5}::double precision,{self.G6}::double precision,
                                {self.G7}::boolean,{self.G8}::boolean,
                                {self.Category_id}::bigint,
                                {self.Context_id}::bigint)
                                 returning id;"""
                cursor.execute(add_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[Prima_Incor-NEW[SENT_REG] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Get:
        """
        Pull by User Message
        """
        # Бесполезный Гет, нам нужно брать по айдишникам
        def sentence_data(self,proc_sent):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Prima_Word_incorrect_answers" WHERE actual_resp = '{proc_sent}' """
                

                cursor.execute(select_query)
                if cursor.fetchall() == []:
                    return False
                else:
                    pulled_data = STD_Prima(cursor.fetchall())
                    
                    # 
                    return pulled_data
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_Incor [Get-SENTENCE_DATA]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
        


        def by_id(self,S_id):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Prima_Word_incorrect_answers" WHERE id = '{S_id}' """
                

                cursor.execute(select_query)
                
                
                pulled_data = STD_Prima(cursor.fetchall())
                    
                    # 
                return pulled_data
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_Incor [Get-BY_ID_DATA]]', _ex)
            
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


                select_query = """SELECT * FROM public."Prima_Word_incorrect_answers"
                                        ORDER BY id DESC LIMIT 1"""
                cursor.execute(select_query)
                if cursor.fetchall() == []:

                    return False

                else:
                    pulled_data = STD_Prima(cursor.fetchall())
                    print(pulled_data)
                    limit_id = pulled_data['ID']
                    #print('ВОТ ОН ЭТО МАКСИМАЛЬНЫЙ АЙДИ БРАТ',pulled_data)
                    print(limit_id)
                    return limit_id
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[VM_WORD-GET [MAX_ID] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Edit:
        # Мы не редачить будем, а удалить и добавлять в кор дб
        pass

class VM_Trash_Answer:
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
                #print(current_word)
                words_id_list.append(str(current_word['ID']))
            except Exception as _ex:
                print('Возникла ошиба при дешифрации предложения. [VM_Sentence - deschcode]',_ex)
                word_params['Слово'] = wd
                word_params['Тип'] = G_Delay(parse(wd))
                Word_F = VM_Word()
                Word_add = Word_F.New(word_params)
                Word_add.learn_word()
                current_word = Word_Func.one_word(wd)
                #print(current_word)
                words_id_list.append(str(current_word['ID']))
        d_code = '-'.join(words_id_list)
        return d_code
    class New:
        def __init__(self,sentence):
            
            sent_func = VM_Trash_Answer()
            
            self.Answer_Sent = sentence
            self.AS_Desch = sent_func.deschcode(self.Answer_Sent)

           


        def sent_reg(self):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                add_query = f"""INSERT INTO public."Prima_Word_trash_answers" (
                                actual_resp, ar_dech) VALUES (
                                '{self.Answer_Sent}'::text, '{self.AS_Desch}'::text)
                                 returning id;"""
                cursor.execute(add_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[Prima_Trash-NEW[SENT_REG] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Get:
        """
        Pull by User Message
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



                select_query = f"""SELECT * FROM public."Prima_Word_trash_answers" WHERE actual_resp = '{proc_sent}' """
                cursor.execute(select_query)
                pulled_data = STD_Prima(cursor.fetchall())
                
                # 
                return pulled_data
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_Trash [Get-SENTENCE_DATA]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Edit:
        # Вот редачить сентенс мы будем, так что да, оставим. И как отредачим закинем в инкоррект.
        pass


class Prima_Contexts:
    class New:
        def context(self,cont_name):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                add_query = f"""INSERT INTO public."Prima_Word_context_table" (
                                    context) VALUES (
                                    '{cont_name}'::character varying)
                                     returning id;"""
                cursor.execute(add_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[Prima_Context-NEW[Context_REG] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')


    class Get:
        def check_for(self,proc_cont):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Prima_Word_context_table" WHERE context = '{proc_cont}' """
                cursor.execute(select_query)
                if cursor.fetchall() == []:
                    return False
                else:
                    return True
                #pulled_data = cursor.fetchall()
                
                # 
                #return pulled_data
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_CONTEXT [Get-CHECK FOR]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

        def get_id(self,cont):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Prima_Word_context_table" WHERE context = '{cont}' """
                cursor.execute(select_query)
                raw_data = cursor.fetchall()
                
                pulled_data = {}

                
                pulled_data['ID'] = raw_data[0][0]
                
                return pulled_data['ID']
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_CONTEXT [Get-ID]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

class Prima_Categories:
    class New:
        def category(self,cat_name):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                add_query = f"""INSERT INTO public."Prima_Word_gos" (
                                    cos) VALUES (
                                    '{cat_name}'::character varying)
                                     returning id;"""
                cursor.execute(add_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[Prima_Category-NEW[COS_REG] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')


    class Get:
        def check_for(self,proc_cat):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Prima_Word_gos" WHERE cos = '{proc_cat}' """
                
                cursor.execute(select_query)
                if cursor.fetchall() == []:
                    return False
                else:
                    return True
                
                #pulled_data = cursor.fetchall()
                
                # 
                #return pulled_data
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_Category [Get-CHECK FOR]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
        
        def get_id(self,cat):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Prima_Word_gos" WHERE cos = '{cat}' """
                cursor.execute(select_query)
                raw_data = cursor.fetchall()
                
                pulled_data = {}

                
                pulled_data['ID'] = raw_data[0][0]
                
                return pulled_data['ID']
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Prima_CAT [Get-ID]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')