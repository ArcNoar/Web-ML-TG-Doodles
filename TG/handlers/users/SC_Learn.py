from aiogram import types
from aiogram.dispatcher import FSMContext
from TG.loader import dp
import asyncio


import numpy as np
from random import randint


from TG.states.SCL_state import SC_State
from Functional.Prima_Func import Prima_sentence, Prima_word
from TG.sql.Prima_Mem import VM_Word , VM_Sentence

import csv


duple_counter = 0

Generated_Sentence = ''
GS_Components = [] # Список айдишников сгенерированного предложения.
S_Grade = 0
"""
Будущая теоритическая модель должна будет предсказывать значение оценки.
Основываясь на всех данных что мы ща сделаем.

"""


"""
Sentence Cord = sum of all words in sentence cords

Нужно создать цсвшник предложений. (Включить туда и провальные и одобренные предложения)
header = ['ID','Sentence','Sent_Dech','X_Cord','Y_Cord','Test_Result']
Взять мой 

# В основную дб пока ниче не заносить.
"""
#Get Template.
#    sent_template = Prima_sentence() # Темплейт для запоминания предложения
#    sent_config = sent_template.create()


# Добавляем хендлер оценки, и там уже закидываем его функциями редактирования координат. Ну и занесения дерьма в ЦСВ.
# Правда надо будет еще достать говно из рандом генератора.

VM_Get = VM_Word.Get()

VM_Edit = VM_Word.Edit()

#VMS_Edit = VM_Sentence.Edit()


def SC_Random():
    try:
                
        sentence_lenght = randint(2,10)
    
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
        
        return [sent, s_components_id]
        
    except Exception as _ex:
        print('При попытке спиздануть что то, возникла ошибка',_ex)

"""
У нас есть сгенерированное предложение, и айдишники компонент.
Нам нужно получить оценку, и на ее основании поменять оценку слов.
Our Values:
Grade = [-1 , -5], [1 , 5]
Indexes = GS_Components
Order = Порядок расположение индексов.

Пока вообще не думай о сходимости координат их значениях.
Наша задача научить ее правильно предложения составлять.

"""

"""
Меняем для начала значеник компонент и получаем значение порядка слов, а потом уже сделаем филлер предложения.
"""


def W_GC(Grade,Indexes):
    
    Components_Data = []
    

    for index in Indexes:
        current_word = VM_Get.word_by_id(index)

        Components_Data.append(current_word)

    def G_Change(G_Val,X_Cord,Y_Cord):

        X_New = X_Cord + (G_Val * 0.1)

        Y_New = Y_Cord + (G_Val * 0.1)

        #print(X_New)
        #print(Y_New)


        return [X_New,Y_New]


    for word_data in Components_Data:
        current_x = word_data['X_Cord']
        current_y = word_data['Y_Cord']


        New_Cords = G_Change(Grade,current_x,current_y)

        VM_Edit.X_Cord(word_data['ID'],New_Cords[0])
        VM_Edit.Y_Cord(word_data['ID'],New_Cords[1])

        #print(New_Cords)




def S_GS(Grade,W_Order): # Sentence Grade(Cord) Set

    Components_Data = [] # Данные компонент
    WX_List = [] # X Координаты компонент
    WY_List = [] # Y Координаты компонент
    

    for index in W_Order:
        current_word = VM_Get.word_by_id(index)
        Components_Data.append(current_word)

    for word_data in Components_Data:
        WX_List.append(word_data['X_Cord'])
        WY_List.append(word_data['Y_Cord'])

    def Loss(order_list): # Скаляр порядка компонент
        val_list = []
        for index in order_list:
            val_list.append(int(index))

        proc_result = val_list[0]
        for i in range(1,len(val_list)):
            proc_result -= val_list[i]
        
        if proc_result < 0:
            proc_result *= -1
        

        output = np.log(proc_result)
        
        output = round(output,2)

        return output

    def Cord_Calc(loss_val,X_Cord,Y_Cord):
        # Мы пока не закидываем в дб, а потом и нахуй нам це не надо.
        #sent_template = Prima_sentence() # Темплейт для запоминания предложения
        #sent_config = sent_template.create()

        X_Sum = sum(X_Cord)
        Y_Sum = sum(Y_Cord)

        neg_X = False
        neg_Y = False
        if X_Sum < 0:
            X_Sum *= -1
            neg_X = True
        elif Y_Sum < 0:
            Y_Sum *= -1
            neg_Y = True

        """

        Я вот бля не подумал насчет того что надо как то же взять эти координаты...
        Мы ща делаем темплейт, высчитываем сумму координат 

        крч
        примерно так я полагаю
        i_Scord = np.log(sum(i_cords) / np.exp(Loss))
        """

        X_Scord = (np.log(X_Sum / loss_val)) / (Grade * 0.1)
        X_Scord = round(X_Scord,2)
        Y_Scord = (np.log(Y_Sum / loss_val)) / (Grade * 0.1)
        Y_Scord = round(Y_Scord,2)
        
        if neg_X == True:
            X_Scord *= -1
        elif neg_Y == True:
            Y_Scord *= -1

        return [X_Scord,Y_Scord]

        
    
    

    return Cord_Calc(Loss(W_Order),WX_List,WY_List)

def D_Con(sent,grade,order,x_cord,y_cord): # Data Constructor
    Header = ['Sentence','WIO','X','Y','Test_Result']

    TR = ''

    if grade < 0:
        TR = 'FAIL'
    elif grade > 0:
        TR = 'SUCCESS'
    else:
        TR = f'ERROR-Result. Grade = {grade}'

    row = {'Sentence' : sent, 'WIO' : order, 'X' : x_cord, 'Y' : y_cord,'Test_Result' : TR}

    return [Header,row]

def CSV_Write(fieldnames,row):
    try:
        with open('Sentence.csv', 'a', newline='') as f_object:
            # Pass the CSV  file object to the Dictwriter() function
            # Result - a DictWriter object
            Writer = csv.DictWriter(f_object, fieldnames=fieldnames)
            Writer.writeheader()
            Writer.writerow(row)
            
            f_object.close()
    except Exception as _ex:
        print(f'Возникла ошибка при записи CSV-Файла. -- {_ex}')



























@dp.message_handler(commands="SC_Learn",state=None)
async def learn_init(message: types.Message):
    

    current_user = message.from_user
    Noah = 340981880
    Artur = 743865349

    

    #Word_func = VM_Word()
    #VM_Get = VM_Word.Get()
    #VM_Edit = VM_Word.Edit()

    #Alph_New = VM_Alph.New()

    
                
    if current_user.id == Noah:
    
        await SC_State.Initial.set()
        await message.answer('А, пора учиться?')
    
    else:
        await message.answer('А ты уверен что у тебя есть право обучать меня?')

duple_counter = 0

@dp.message_handler(state=SC_State.Initial)
async def learn_start(message: types.Message,state: FSMContext):
    global duple_counter
    current_user = message.from_user
    if message.text == 'Старт.':
        await message.answer('Оки, тогда я буду пытаться составлять предложения, а тебе нужно сказать, Верно ли оно.')
        await SC_State.Learning.set()

    else:
        if duple_counter == 0:
            await dp.bot.send_voice(current_user.id, open("TG/media/voice_msg/Ara_Ara.ogg","rb"))
            await asyncio.sleep(1)
            await dp.bot.send_message(current_user.id,'Чему же ты хочешь меня обучить~')
            duple_counter += 1
        elif duple_counter == 1:
            await message.reply('Чтобы начать обучение скажи "Старт.", и сука будь добр соблюдать регистр и в точности написать как это я сказала')
            duple_counter += 1    
        elif duple_counter == 2:
            await message.reply('Я неясно выразилась?')
            duple_counter += 1
        elif duple_counter == 3:
            await message.reply('Боже, да ты тупой, да?')
            duple_counter += 1
        else:
            await message.reply('Думаю стоит просто отобрать у тебя состояние')
            await state.finish()

@dp.message_handler(state=SC_State.Learning)
async def learn_proc(message: types.Message,state: FSMContext):
    global Generated_Sentence, GS_Components
    current_user = message.from_user
    
    SCR_Data = SC_Random()
    answer = SCR_Data[0]
    a_comp = SCR_Data[1]
    
    await dp.bot.send_message(current_user.id,answer)

    await asyncio.sleep(1)

    await dp.bot.send_message(current_user.id,'Я справилась? Оцените от -1 до -5 если результат плох, и от 1 до 5 если все хорошо.')

    Generated_Sentence = answer
    GS_Components = a_comp
    

    await SC_State.Grading.set()

@dp.message_handler(state=SC_State.Grading)
async def grading(message: types.Message, state: FSMContext):
    global Generated_Sentence, GS_Components, S_Grade
    current_user = message.from_user

    # Возможно стоит сменить оценку. Потому что 0 5 и 5 10 , немного несправдливо сильная разница. Надо отрицательно значение намутить.
    """
    Подсчет изначальных координат
    Смена системы оценки
    Функция которая меняет оценку каждому слову компоненте предложения.
    ЦСВ с предложениями
    Занесение измененных координат слов сразу в дб
    Возможен автоматический пересчет предолженний... (потому что слова могут быть  зайдествованы сразу в нескольких предложениях.)
    Т.е стоит еще учесть порядок расположения?
    Возможно координаты предложения будут более независимы от координат слов чем изначально планировалось.
    """

    #print(GS_Components)
    try:

        grade = int(message.text)

        S_Grade = grade

        if int(message.text) == 0:
            await message.answer('Так значит я провалилась...')
            S_Grade = 0.1
        else:
            await message.answer('Отлично.')

        W_GC(S_Grade,GS_Components)
        S_Cords = S_GS(S_Grade,GS_Components)

        CSV_Data = D_Con(Generated_Sentence,S_Grade,GS_Components,S_Cords[0],S_Cords[1])
        CSV_Write(CSV_Data[0],CSV_Data[1])

        await SC_State.Learning.set()

            
    except ValueError as _ex:
        print(_ex)
        await message.answer('Недопустимый формат оценки.')
    
    
