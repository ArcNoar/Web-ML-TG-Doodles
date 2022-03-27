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
    print(gramma_text)

        
        
            

  
    
def parse(word):
    html = get_html(f"https://wikislovo.ru/morphology/{word}")
    if html.status_code == 200:
        return get_gramma(html.text)
    else:
        print('Oh no.')

parse('интеллект')

"""

def gramma_fill(word_dict):
    # word_dict - словарь слова
    g_gramma = parse(word_dict['Слово']) #Грамматика
    print(f'Прикол прикольный: {g_gramma}')

    gramma_output = {}

    gramma_key = {
        'имя существительное' : 'NOUN',

        'неодушевлённое' : 'INANIMA',
        'одушевлённое' : 'ANIMA',

        'мужской' : 'Male',
        'женский' : 'Female',
        'средний' : 'Neutral',

        'именительный' : 'IMP',
        'родительный' : 'RP',
        'дательный' : 'DP',
        'винительный' : 'VP',
        'творительный' : 'TP',
        'предложный' : 'PP',

        'единственное' : 'SINGULAR',
        'множественное' : 'PLURAL',
        }

    for gg in g_gramma.keys():
        
        cur_gv = g_gramma[f'{gg}'] # cur_gram value
        if gg == ' падеж':
            cur_gv = ((cur_gv).split(','))[0]
        if gg == ' отвечает на вопрос':
            continue
        if cur_gv in gramma_key.keys():
            if gg == 'часть речи':
                pass
            else:
                gg = gg[1:]
            gramma_output[gg] = cur_gv
        else:
            print(f" что это за хуйня???  {cur_gv}")
            
    word_dict['Тип'] = gramma_key[gramma_output['часть речи']]
    word_dict['Род'] = gramma_key[gramma_output['род']]
    word_dict['Число'] = gramma_key[gramma_output['число']]
    word_dict['Падеж'] = gramma_key[gramma_output['падеж']]
    word_dict['Одушевленность'] = gramma_key[gramma_output['одушевлённость']]
    print(f'С заполненной грамматикой {word_dict}')

        
"""



    

    



