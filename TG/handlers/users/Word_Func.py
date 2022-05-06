from aiogram import types
from aiogram.dispatcher import FSMContext
from TG.loader import dp
from aiogram.dispatcher.filters import Text
import asyncio


from time import sleep
from random import randint

import csv
import numpy as np
import pandas as pd

import rusyllab as rl # Дробление на слоги.
#import nltk
#from nltk.stem.snowball import SnowballStemmer



from AI_Gen.MBoost.MB_Trees.Type_Trees import model_list
from AI_Gen.MBoost.MB_Grads.Type_Grad import Gmodel_list
from AI_Gen.Tools.Alpha_Calibrator import alpha_trainer

from Functional.Prima_Func import Prima_word, parse , G_Delay

from TG.sql.Prima_Mem import VM_Alph, VM_Word 

from TG.states.Grade_State import Word_Type


word_template = Prima_word() # Темплейт запоминания слов
word_params = word_template.create()

REM_STATE = False

def constuct_code(word):
        Alph_Get = VM_Alph.Get()

        some_word = word
        
        constr_id_list = []
        c_code = ''
        
        for constr in some_word:
            try:
                
                current_constr = Alph_Get.get_by_construct(constr)

                constr_id_list.append(str(current_constr['ID']))

            except Exception as _ex:
                #print('Ошибка в дешифраторе конструктов. [VM_Word - Construct Code]',_ex)
                constr_id_list.append('0')

        c_code = '-'.join(constr_id_list)
        return c_code

def CSV_Write(fieldnames,row):
    try:
        with open('Word_Data.csv','w',encoding='UTF8',newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(row)
            f.close()
    except Exception as _ex:
        print(f'Возникла ошибка при записи CSV-Файла.  {_ex}')



@dp.message_handler(commands="Word_Func",state=None)
async def WG_Init(message: types.Message):
    

    current_user = message.from_user
    Noah = 340981880
    Artur = 743865349

    

    #Word_func = VM_Word()
    #VM_Get = VM_Word.Get()
    #VM_Edit = VM_Word.Edit()

    #Alph_New = VM_Alph.New()

    
                
    if current_user.id == Noah:
    
        await Word_Type.Initial.set()
        await message.answer('Запускаю Фунциональное состояние - Слова')
        #await dp.bot.send_message(current_user.id,'В общем. Ты перенаправлен в состояние инструктажа. \n Если ты уже проходил этот гайд, то напиши "Пропустить."')

    
    else:
        await message.answer('А ты уверен что у тебя есть права?')

#Отмена.

@dp.message_handler(state='*', commands = 'закончили')
@dp.message_handler(Text(equals='закончили', ignore_case = True),state='*')
async def cancel_handler(message: types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ну окэ.')




@dp.message_handler(state=Word_Type.Initial)
async def Nav_State(message: types.Message,state: FSMContext):
    

    current_user = message.from_user
    Noah = 340981880
    Artur = 743865349

    

    Word_func = VM_Word()
    VM_Get = VM_Word.Get()
    #VM_Edit = VM_Word.Edit()

    

    
                
    if current_user.id == Noah:
        await dp.bot.send_message(Noah,"""Вы в функциональном состоянии. Доступные Функции. 
                                        F01 - Пул Слов. Формат - 1
                                        
                                        
                                        T01 - Поиск идеальной Альфы.
                                        T02 - Альтернативный Тест Слова.
                                        
                                        """)
    
        if message.text == 'Я состоятельный' :
    
            await message.answer('Ваше состояние : Функциональное - Слова')
        elif message.text == 'F01':
            """
            Создает ЦСВ ФАЙЛ данных слов для грамматической модели.
            """
            await message.answer('Как будете готовы. Напишите любое сообщение.')
            await Word_Type.Pulling.set()

        

        elif message.text == 'T01':
            await message.answer('Как будете готовы. Напишите любое сообщение.')
            await Word_Type.Alpha_Find.set()


        elif message.text == 'T02':
            await message.answer('Прошу вводить только одно слово, даже если ввёдете предложения, я учту только первое слово.')
            await Word_Type.ATT_Set.set()
        
            
            
    
        else:
            await message.answer('Неа, вы ошиблись.')
           

@dp.message_handler(state=Word_Type.Pulling)
async def word_pull(message: types.Message,state: FSMContext):
    #Word_func = VM_Word()
    VM_Get = VM_Word.Get()

    await message.answer('Пул слов начат.')
    data = VM_Get.all()
    fields = ['ID','Слово','Длина','Количество слогов.','Слоги','Код Слогов','Код','X_Cord','Y_Cord','SF','Категория','Тип']
    better_data = []
    for w_dict in data:
        #print(w_dict)
        w_dict['Слоги'] = rl.split_word(w_dict['Слово'])
        w_dict['Количество слогов.'] = len(w_dict['Слоги'])
        w_dict['Код Слогов'] = [[int(l) for l in j.split('-')] for j in [constuct_code(i) for i in w_dict['Слоги']]]
        w_dict['Длина'] = len(w_dict['Слово'])
        w_dict['Код'] = [int(i) for i in w_dict['Код'].split('-')]
        print(w_dict)
        better_data.append(w_dict)
    rows = better_data
    CSV_Write(fields,rows)
    await message.answer('Пул слов закончен.')

    await state.finish()



@dp.message_handler(state=Word_Type.ATT_Set)
async def WTS_Test(message: types.Message,state:FSMContext):
    global word_params
    raw_message = message.text

    message_list = raw_message.split(' ')

    word = message_list[0]

    template = word_params.copy()

    template['Слово'] = word.lower()

    template['Код'] = constuct_code(word)

    template['Слоги'] = rl.split_word(template['Слово'])
    template['Количество слогов.'] = len(template['Слоги']) #+
    template['Код Слогов'] = [[int(l) for l in j.split('-')] for j in [constuct_code(i) for i in template['Слоги']]]
    template['Длина'] = len(template['Слово']) #+
    template['Код'] = [int(i) for i in template['Код'].split('-')] #+
    #print(template)
    better_data = [template['Длина'],template['Количество слогов.'],template['Код Слогов'],template['Код']]

    data = better_data

    #code = data[3] # Забираем лист с индексами из массива данных

    w_part = data[2][len(data[2]) - 1]

    joined_part = int(''.join([str(i) for i in w_part]))
    data[2] = round(np.log(joined_part),3)
    
    Code_Columns = [] 
    Additional_Col = ['Lenght','P_Amount','Ending']
    
    def Column_Create():
        
        try:    
            for w_index in range(35):
                
                Code_Columns.append(f'Code_{w_index}')
        except Exception as _ex:
            print('ТЫ ДОЛБАЕБ')
                
    def data_trans(data_b):
        #collected_data = []
        
        
        new_data = []
        for i in data_b:
            #print(blyat)
            if type(i) == list:
                for c in i:
                    #print(c)
                    #print('МЫ ТУТ')
                    new_data.append(c)
            else:
                #print(blyat)
                new_data.append(i)
        while len(new_data) < 38:
            new_data.append(0)
        #collected_data.append(new_data)
            
    
    
        return new_data
    
    Column_Create()
    
    DF_Columns = Additional_Col + Code_Columns
    proc_data = data_trans(data)
    #print(proc_data)
    #print(f'Test Data : {proc_data}')
    testf = pd.DataFrame([proc_data], columns = DF_Columns) # X_DF
    #print(testf.head())
    #print(proc_data)
    #outpute_grade = Verb_Gmodel([proc_data])
    
    
    #print(outpute_grade)
    for i in Gmodel_list:
        cur_model = Gmodel_list[f'{i}']
        await message.answer(f'Дерево {i} Gmodel предсказало : {cur_model([proc_data])}')
    """
    for i in model_list:
        cur_model = model_list[f'{i}']
        await message.answer(f'Дерево {i} model предсказало : {cur_model(testf)}')
    """
    await message.answer('Продолжаем?')
    await Word_Type.Reset_Ask.set()
    

@dp.message_handler(state=Word_Type.Reset_Ask)
async def Asker(message: types.Message,state:FSMContext):
    if message.text == 'Да.':
        await message.answer('Следующее слово?')
        await Word_Type.ATT_Set.set()
        
    else:
        await state.finish()



@dp.message_handler(state=Word_Type.Alpha_Find)
async def Alpha_Search(message: types.Message,state:FSMContext):
    #print(model_list)
    for i in model_list:
        cur_model = model_list[f'{i}']
        await message.answer(f'Лучшая альфа для {i} model : {alpha_trainer(cur_model)}')

    await state.finish()










