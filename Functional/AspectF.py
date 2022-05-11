import numpy as np
import csv
from random import randint

#from Functional.Prima_Func import Prima_sentence, Prima_word
from TG.sql.Prima_Mem import VM_Word # , VM_Sentence


VM_Get = VM_Word.Get()


def SC_Random(Generated_Sentence=None):
    
    
    if Generated_Sentence is None: 
        try:        
            sentence_lenght = randint(1,5)
        
            sentence_parts = []
            sent = ''
            s_components_id = []
            exception_counter = 0
            limiter = 0
            while limiter < sentence_lenght:
                try:
                    max_ID = VM_Get.max_id()
                    word_ident = str(randint(1,int(max_ID['ID'])))
                    pulled_word = VM_Get.word_by_id(word_ident)
                    sentence_parts.append(pulled_word['Слово'])
                    s_components_id.append(word_ident)
                    #print(word_ident)
                    limiter += 1
                except Exception as _ex:
                    #print('ОШИБКА БРАТАН. СЕНТЕНС КОНСТРУКТОР ХУЙНЯ',_ex)
                    if exception_counter < 10:
                        continue
                    else:
                        break
        
            sent = ' '.join(sentence_parts)
           

            return sent
            
        except Exception as _ex:
            print('При попытке спиздануть что то, возникла ошибка',_ex)
    else:
        return Generated_Sentence



#Grade CSV SAVE (Approved Sentences) GR = Good Responses

"""
-Надо огольвье доделать, тип категория и контекст- 

+ мб еще что то, но я сейчас сам не знаю и не помню
Потом проверишь норм оно закидывает или нет

US = User Sentence
AS = Actual Sentence (AR)

GR = Good Responses

G = Grade

"""


def CSV_Write(row):

    Header = ['US','AS','Category','Context','1G','2G','3G','4G','5G','6G','7G','7.5G']

    try:
        with open('GR.csv', 'a',encoding='UTF8',newline='') as f_object:
            # Pass the CSV  file object to the Dictwriter() function
            # Result - a DictWriter object
            Writer = csv.DictWriter(f_object, fieldnames=Header)
            #Writer.writeheader()
            
            Writer.writerow(row)
            
            f_object.close()
    except Exception as _ex:
        print(f'Возникла ошибка при записи CSV-Файла. -- {_ex}')





