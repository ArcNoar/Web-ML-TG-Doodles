









class Prima_sentence:
    """
       Класс создающий темплейт заполнения данных в дб. 
    """
    def create(self):
        sent_Template = {
            'US' : 'Пустое предложение' ,
            'US_Dech' : '91-92',
            'AS' : 'Пустое предложение' ,
            'AS_Dech' : '91-92',
            'G1' : 1.0,
            'G2' : 1.0,
            'G3' : 1.0,
            'G4' : 1.0,
            'G5' : 1.0,
            'G6' : 1.0,
            'G7' : 1.0,
            'G8' : 1.0,
            'Категория' : '1',
            'Контекст' : '1',
            }
        # Тебе сейчас надо доделать хендлер положительной оценки и переделать сентенс класс в Прима Мем
        return sent_Template



def STD_Prima(sent_data):
    """
    STD = Sentence To Dict
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    Конвертирует Данные из дб в Словарь.
   

    """
    data_list = sent_data
    try:
        converted_data = {
                'ID' : data_list[0][0],
                'US' : data_list[0][1],
                'US_Dech' : data_list[0][2],
                'AS' : data_list[0][3],
                'AS_Dech' : data_list[0][4],
                'G1' : data_list[0][5],
                'G2' : data_list[0][6],
                'G3' : data_list[0][7],
                'G4' : data_list[0][8],
                'G5' : data_list[0][9],
                'G6' : data_list[0][10],
                'G7' : data_list[0][11],
                'G8' : data_list[0][12],
                'Категория' : data_list[0][13],
                'Контекст' : data_list[0][13]
                
                }
        
        return converted_data
    except Exception as _ex:
        print(_ex)




class Prima_word:
    """
    Шаблон заполнения данных в дб. 
    Word_Template = {
            'Слово' : None ,
            'Код' : '??',
            'X_Cord' : 1,
            'Y_Cord' : -1,
            'SF' : 'Empty',
            'Категория' : '1',
            'Тип' : 'NONE_T'

            }
        
    """
    def create(self):
        Word_Template = {
            'Слово' : None ,
            'Код' : '??',
            'X_Cord' : 1,
            'Y_Cord' : -1,
            'SF' : 'Empty',
            'Тип' : 'NONE_T'

            }
        return Word_Template







def WTD_Prima(pulled_word): 
    """
    WTD = Word To Dict
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    Достает слово из дб.
    Одно!.
   

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
                'Тип' : data_list[0][6]
                }
        
        return converted_data
    except Exception as _ex:
        pass
        #print(_ex)


def WTDM_Prima(word_list):
    """
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    Достает слово из дб.
    Много!.
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
                    'Тип' : data_list[6]


                    }
            
            collected_users.append(converted_data)
        except Exception as _ex:
            pass
            #print(_ex)
    return collected_users


# Грамматический пул (Парсер Частей речи.)

import requests



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



# Парсит полученные данные, доставая из них часть речи.
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