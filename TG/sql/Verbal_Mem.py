import psycopg2
#from datetime import date
from .conf import db_name,host,user,password
from Functional.VMW_Func import WTD_single #WTD_many
from Functional.VMS_Func import STD_Single




class VM_Alph:
    class New:
        def add_construct(self,cstr,type='LETTER',type_2 = 'NONE_T'):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                second_query = f"""INSERT INTO public."Asiya_vm_alph" (
                                    construct, alp_t, alp_t2) VALUES (
                                    '{cstr}'::character varying, '{type}'::character varying, '{type_2}'::character varying)
                                     returning id;"""
                cursor.execute(second_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_ALPH-NEW[NEW_CONSTRUCT] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Get:
        pass

# --Word Memory
class VM_Word:
    
    class New:
        def __init__(self,template):
            self.Word = template['Слово']
            self.Word_Type = template['Тип']
            self.Word_Des = template['Значение']
            self.Group_Id = template['Категория']
            self.W_Code = template['Код']
            

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


                second_query = f"""INSERT INTO public."Asiya_vm_word" (
                                word, word_type, word_des, group_of_word_id, word_code) VALUES (
                                '{self.Word}'::character varying, '{self.Word_Type}'::character varying, '{self.Word_Des}'::text,
                                 '{self.Group_Id}'::bigint, '??'::character varying)
                                 returning id;"""
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


        def word_gow(self,the_word,gow_id):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()


                Edit_query = f"""UPDATE public."Asiya_vm_word" SET
                                    group_of_word_id = '{gow_id}'::bigint WHERE
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

        

        
    class Del:
        pass


#---SENTENCE MEMORY
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
                
               


                add_query = f"""INSERT INTO public."Asiya_sentence_memory" (
                                sentence, sent_dech, short_mean, from_who_id, sent_context_id) VALUES (
                                '{self.Sentence}'::text, '{self.Sent_Desch}'::text, '{self.Short_Mean}'::text, 
                                '{self.From_who}'::character varying, {self.Context_id}::bigint)
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

        
    class Edit:
        def short_mean(self,new_mean,sentence_to_edit):
            """
            new_mean = str
            sentence_to_edit = str
            """
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                edit_query = f"""UPDATE public."Asiya_sentence_memory" SET
                                short_mean = '{new_mean}'::text WHERE
                                            sentence = '{sentence_to_edit}';"""
                cursor.execute(edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_Sentence-EDIT[SHORT_Mean] ]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

        def sent_context(self,new_context,sentence_to_edit):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                edit_query = f"""UPDATE public."Asiya_sentence_memory" SET
                                sent_context_id = {new_context}::bigint WHERE
                                            sentence = '{sentence_to_edit}';"""
                cursor.execute(edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_Sentence-EDIT[SHORT_Mean] ]', _ex)
            
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



                select_query = f"""SELECT * FROM public."Asiya_sentence_memory" WHERE sentence = '{proc_sent}' """
                cursor.execute(select_query)
                pulled_data = STD_Single(cursor.fetchall())
                
                # 
                return pulled_data
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [VM_SENTENCE [Get-SENTENCE_DATA]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
            








#NON FUND VERBAL MEMORY
class VM_Context:

    class New:
        def context_reg(self,Context_name,Context_content):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                add_query = f"""INSERT INTO public."Asiya_context_table" (
                                    "context", "context_desc") VALUES (
                                    '{Context_name}'::character varying, 
                                    '{Context_content}'::text)
                                     returning "Context";"""
                cursor.execute(add_query)

                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_Context-NEW [CONTEXT_REG]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
        


    class Edit:
        
        def content(self,new_content,context_tag):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                edit_query = f"""UPDATE public."Asiya_context_table" SET
                            "Context_Desc" = '{new_content}'::text WHERE
                            "Context" = '{context_tag}';"""
                cursor.execute(edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_Context-EDIT [CONTENT]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

        def name_tag(self,new_tag,context_tag):
            try:

                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()
                
               


                edit_query = f"""UPDATE public."Asiya_context_table" SET
                            "context" = '{new_tag}'::text WHERE
                            "context" = '{context_tag}';"""
                cursor.execute(edit_query)
                #СУКА КТО КОМИТ СПИЗДИЛ
                connection.commit()
                        
            
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ.[[VM_Context-EDIT [NAME]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')


    class Get:
        
        def all(self):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = """SELECT * FROM public."Asiya_context_table" """
                cursor.execute(select_query)
                pulled_data = cursor.fetchall()
                context_dict = {}
                pulled_contexts = []
                for context in pulled_data:
                    context_dict['ID'] = context[0]
                    context_dict['Context_Name'] = context[1]
                    context_dict['Descript'] = context[2]
                    pulled_contexts.append(context_dict)
                return pulled_contexts
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [VM_CONTEXT [Get-ALL]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

        def one_by_id(self,id):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                select_query = f"""SELECT * FROM public."Asiya_context_table" WHERE id = '{id}' """
                cursor.execute(select_query)
                pulled_data = cursor.fetchall()
                context_dict = {}
                
                for context in pulled_data:
                    context_dict['ID'] = context[0]
                    context_dict['Context_Name'] = context[1]
                    context_dict['Descript'] = context[2]
                    
                return context_dict
                
                
                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [VM_CONTEXT [Get-BY ID]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    print('Дб отключена')

#GROUP OF WORDS
class GOW:
    """
    Group of Words
    """
    class New:
        def new_group(self,group_name):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                add_query = f"""INSERT INTO public."Asiya_gow" (
                                                    char_tag) VALUES (
                                                    '{group_name}'::character varying)
                                                     returning id;"""
                cursor.execute(add_query)
                connection.commit()
                

            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [GOW [New-new_group]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
    
    class Edit:
        def group_by_id(self,new_name,group_id):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                edit_query = f"""UPDATE public."Asiya_gow" SET
                                    cow = '{new_name}'::character varying WHERE
                                                        id = '{group_id}';"""
                cursor.execute(edit_query)
                connection.commit()
                

            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [GOW [EDIT-edit_Group_by_id]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

        def group_by_name(self,new_name,relate_group):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                edit_query = f"""UPDATE public."Asiya_gow" SET
                                    cow = '{new_name}'::character varying WHERE
                                                        cow = '{relate_group}';"""
                cursor.execute(edit_query)
                connection.commit()
                

            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [Char_Tag [EDIT-edit_tag_by_name]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')
        

    class Get:
        def get_groups(self):
            try:
                connection = psycopg2.connect(
                
                        host = host,
                        user = user,
                        password = password,
                        database = db_name
                        )
                
                cursor = connection.cursor()



                edit_query = f"""SELECT * FROM public."Asiya_gow" 
                                                        ORDER BY id ASC """
                cursor.execute(edit_query)
                pulled_data = cursor.fetchall()
                group_dict = {}
                group_list = []
                for group in pulled_data:
                    group_dict['ID'] = group[0]
                    group_dict['Tag'] = group[0]
                    group_list.append(group_dict)
                return group_list

                
            except Exception as _ex:
                print('Ошибка в ходе чтения ДБ. [GOW [GET-Get_groups]]', _ex)
            
            finally:
                if connection:
                    connection.close()
                    #print('Дб отключена')

    class Del:
        pass

