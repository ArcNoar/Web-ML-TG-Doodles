from aiogram import types
from aiogram.dispatcher import FSMContext
from TG.loader import dp
import asyncio
from aiogram.dispatcher.filters import Text


import numpy as np
from random import randint


from TG.states.SC_AI import AI_State
from Functional.Prima_Func import Prima_sentence, Prima_word
from TG.sql.Prima_Mem import VM_Word , VM_Sentence

import csv
import pandas as pd


from AI_Gen.CG_Data_Prep import Test_X
from AI_Gen.Construct_Grade import Construct_Grader

#duple_counter = 0

Generated_Sentence = ''
GS_Components = [] # Список айдишников сгенерированного предложения.
S_Grade = 0
# НУЖНО ПЕРЕДЕЛЫВАТЬ ВАЩЕ ВСЕ Я ПОМЕНЯЛ ВСЕ ФОРМУЛЫ И РАССЧЕТЫ


VM_Get = VM_Word.Get()

VM_Edit = VM_Word.Edit()


def SC_Random():
    try:
                
        sentence_lenght = randint(1,7)
    
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

# Cord Set
def W_GC(Indexes):
    
    Components_Data = []
    
    X = None
    Y = None
    for index in Indexes:
        current_word = VM_Get.word_by_id(index)

        Components_Data.append(current_word)

    
    for word_data in Components_Data:
        X = word_data['X_Cord']
        Y = word_data['Y_Cord']

        

    return [X,Y]

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


# DATA PROC

def D_Con(sent,grade,order,x_cord,y_cord): # Data Constructor
    Header = ['Sentence','Order_Val','X','Y','Grade','Test_Result']

    TR = ''

    val_list = []
    for index in order:
        val_list.append(int(index))

    proc_result = val_list[0]
    for i in range(1,len(val_list)):
        proc_result -= val_list[i]
    
    if proc_result < 0:
        proc_result *= -1
    

    output = np.log(proc_result)
    
    Order_Val = round(output,2)

    
    
    if grade < 2:
        TR = 'FAIL'
    elif grade > 2:
        TR = 'SUCCESS'
    else:
        TR = f'ERROR-Result. Grade = {grade}'
    
    row = {'Sentence' : sent, 'Order_Val' : Order_Val, 'X' : x_cord, 'Y' : y_cord,'Grade' : grade,'Test_Result' : TR}

    return [Header,row]


def CSV_Write(fieldnames,row):
    try:
        with open('Pred_S.csv', 'a',encoding='UTF8',newline='') as f_object:
            # Pass the CSV  file object to the Dictwriter() function
            # Result - a DictWriter object
            Writer = csv.DictWriter(f_object, fieldnames=fieldnames)
            #Writer.writeheader()
            if row['Test_Result'] == 'SUCCESS':
                Writer.writerow(row)
            
            f_object.close()
    except Exception as _ex:
        print(f'Возникла ошибка при записи CSV-Файла. -- {_ex}')




@dp.message_handler(commands="SC_AI",state=None)
async def learn_init(message: types.Message):
    

    current_user = message.from_user
    Noah = 340981880
    Artur = 743865349

    

    #Word_func = VM_Word()
    #VM_Get = VM_Word.Get()
    #VM_Edit = VM_Word.Edit()

    #Alph_New = VM_Alph.New()

    
                
    if current_user.id == Noah:
    
        await AI_State.Initial.set()
        await message.answer('Самообучение, да?')
        #await dp.bot.send_message(current_user.id,'В общем. Ты перенаправлен в состояние инструктажа. \n Если ты уже проходил этот гайд, то напиши "Пропустить."')

    
    else:
        await message.answer('А ты уверен что у тебя есть право обучать меня?')

@dp.message_handler(state='*', commands = 'закончили')
@dp.message_handler(Text(equals='закончили', ignore_case = True),state='*')
async def cancel_handler(message: types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ну окэ.')


duple_counter = 0



@dp.message_handler(state=AI_State.Initial)
async def learn_start(message: types.Message,state: FSMContext):
    global duple_counter
    current_user = message.from_user
    if message.text == 'Старт.':
        await message.answer('Штош. Ща попробуем.')
        await AI_State.Learning.set()

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

@dp.message_handler(state=AI_State.Learning)
async def learn_proc(message: types.Message,state: FSMContext):
    global Generated_Sentence, GS_Components
    current_user = message.from_user
    for i in range(1000):
        SCR_Data = SC_Random()
        answer = SCR_Data[0]
        a_comp = SCR_Data[1]
        Generated_Sentence = answer
        GS_Components = a_comp

        try:

            

            

            Cords = W_GC(GS_Components)
            #S_Cords = S_GS(S_Grade,GS_Components)

            #CSV_Data = D_Con(Generated_Sentence,S_Grade,GS_Components,S_Cords[0],S_Cords[1])
            val_list = []
            for index in GS_Components:
                val_list.append(int(index))

            proc_result = val_list[0]
            for i in range(1,len(val_list)):
                proc_result -= val_list[i]
            
            if proc_result < 0:
                proc_result *= -1
            

            output = np.log(proc_result)
            
            Order_Val = round(output,2)

            
            X_Data = Test_X(Order_Val,Cords[0],Cords[1])
            
            prediction = Construct_Grader.predict(X_Data)
            
            CSV_Data = D_Con(Generated_Sentence,prediction[0],GS_Components,Cords[0],Cords[1])
            

            CSV_Write(CSV_Data[0],CSV_Data[1])
            

            #await message.answer(f'Я полагаю что оценка этого предложения будет {prediction}')

            #await AI_State.Learning.set()

                
        except ValueError as _ex:
            print(_ex)
            await message.answer('Недопустимый формат оценки.')
    
    await dp.bot.send_message(current_user.id,'Я завершила свои предсказания.')
    await state.finish()
    #await asyncio.sleep(1)

    

    #await AI_State.Grading.set()
"""
@dp.message_handler(state=AI_State.Grading)
async def grading(message: types.Message, state: FSMContext):
    global Generated_Sentence, GS_Components, S_Grade
    current_user = message.from_user

    try:

        S_Grade = None

        

        Cords = W_GC(GS_Components)
        #S_Cords = S_GS(S_Grade,GS_Components)

        #CSV_Data = D_Con(Generated_Sentence,S_Grade,GS_Components,S_Cords[0],S_Cords[1])
        

        
        X_Data = Test_X(GS_Components,Cords[0],Cords[1])

        prediction = Construct_Grader.predict(X_Data)

        await message.answer(f'Я полагаю что оценка этого предложения будет {prediction}')

        

            
    except ValueError as _ex:
        print(_ex)
        await message.answer('Недопустимый формат оценки.')

"""

"""
Нужно найти константу предсказания. (Резидуал?)
Нужно перезаполнить дб, потому что ГРЭЙД ПИЗДЕЦКИ ВАЖЕН
Нужно доработать данные координат слов
Нужно Почистить немного это все, а то мусора пизда
А да, еще этот твой альт лерн не работает правильно потому что класс состояни одноименный)
"""