









class Prima_sentence:
    """
        Sentence (Предложение) = None
        Sent_Dech (Дешифровка) = false
        Short_Mean (Краткая суть) = false

        From_Who_id (От кого) = false
        Sent_Context_id (Айди контекста) = NOUN
        
        
    """
    def create(self):
        Word_Template = {
            'Предложение' : 'Пустое предложение' ,
            'Дешифровка' : '91-92',
            'X_Cord' : 1,
            'Y_Cord' : -1,
            'SF' : 'Empty',
            'Контекст' : '1',
            

            }
        return Word_Template



def STD_Prima(sent_data):
    """
    STD = Sentence To Dict
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    
    data_list = sql_pull_func(user_data).get_user() => returns [(ID,first_name,sur_name,....,appearance)]
    
    func(data_list) => return dict = {
                                                'ID' : ID,
                                                'first_name' : first_name,
                                                 Key : Value,
                                                }

    """
    data_list = sent_data
    try:
        converted_data = {
                'ID' : data_list[0][0],
                'Предложение' : data_list[0][1],
                'Дешифровка' : data_list[0][2],
                'X_Cord' : data_list[0][3],
                'Y_Cord' : data_list[0][4],
                'SF' : data_list[0][5],
                
                }
        
        return converted_data
    except Exception as _ex:
        print(_ex)




class Prima_word:
    """
        
        
    """
    def create(self):
        Word_Template = {
            'Слово' : None ,
            'Код' : '??',
            'X_Cord' : 1,
            'Y_Cord' : -1,
            'SF' : 'Empty',
            'Категория' : '1',
            'Тип' : 'NONE_T'

            }
        return Word_Template







def WTD_Prima(pulled_word): 
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
    #print(data_list)
    try:
        converted_data = {
                'ID' : data_list[0][0],
                'Слово' : data_list[0][1],
                'Код' : data_list[0][2],
                'X_Cord' : data_list[0][3],
                'Y_Cord' : data_list[0][4],
                'SF': data_list[0][5],
                'Категория' : data_list[0][6],
                'Тип' : data_list[0][7]
                }
        
        return converted_data
    except Exception as _ex:
        pass
        #print(_ex)


def WTDM_Prima(word_list):
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
                    'Код' : data_list[2],
                    'X_Cord' : data_list[3],
                    'Y_Cord' : data_list[4],
                    'SF' : data_list[5],
                    'Категория' : data_list[6],
                    'Тип' : data_list[7]


                    }
            
            collected_users.append(converted_data)
        except Exception as _ex:
            pass
            #print(_ex)
    return collected_users




import requests

#from TG.sql.Verbal_Mem import VM_Word 

from bs4 import BeautifulSoup

HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36','accept':'*/*'}


#VM_Get = VM_Word.Get()

def get_html(url,params=None):
    r = requests.get(url,headers=HEADERS,params=params)
    return r


def get_gramma(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div', class_= "morphology-analysis")

    gramma_text = (items[0].get_text())
    return gramma_text







def parse(word):
    html = get_html(f"https://wikislovo.ru/morphology/{word}")
    if html.status_code == 200:
        return get_gramma(html.text)
    else:
        pass
        #print('Oh no.')




def G_Delay(G_data):
    Data_String = G_data
    #print(G_data)
    Codes = {'имя существительное': 'NOUN',
              'глагол' : 'VERB',
              'имя прилагательное' : 'ADJECTIVE',
              'местоимение' : 'NOMIN',
              'междометие' : 'INTER',
              'наречие' : 'STATE',
              'союз' : 'UNION',
              'частица' : 'PTICK',
              'предлог' : 'PREPOS',
              'имя числительное' : 'NUMIN',
              'причастие' : 'PRICH',
              'деепричастие' : 'DEPRICH',
              'NONE_T' : 'NONE_T',
              }
    def SP(data):
        
        try:
            if data[data.find('Вариант'):8] == 'Вариант':
                #print('1')
                #print(data[data.find('Вариант'):])
                SP_Loc = data[len('Часть речи —  ') + 11:data.find('Морфологические') -1 ] # Часть речи.
                
                #print(SP_Loc)
                return SP_Loc
            elif data[data.find('Отвечает'):8] == 'Отвечает':
                SP_Loc = data[len('Часть речи —  ') + 1:data.find('Отвечает') -1 ]
                return SP_Loc
            else:
                SP_Loc = data[len('Часть речи —  ') + 1:data.find('Морфологические') -1 ] # Часть речи.
                #print('2')
                #print(data[data.find('Вариант'):8])
                #print(SP_Loc)
                return SP_Loc
        except Exception as _ex:
            #print('Нэ получилось дать тип.', _ex)
            SP_Loc = 'NONE_T'
            return SP_Loc
    Gramma = 'NONE_T'
    try:
        Gramma = Codes[f'{SP(Data_String)}']
    except Exception as _ex:
        Gramma = 'NONE_T'
    

    return Gramma

#result = G_Delay(output)
#print(result)