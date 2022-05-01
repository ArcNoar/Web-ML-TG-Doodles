from aiogram import types
from aiogram.dispatcher import FSMContext
from TG.loader import dp
from aiogram.dispatcher.filters import Text


import asyncio
import csv
from time import sleep
from random import randint
import rusyllab as rl # Дробление на слоги.
import numpy as np
import pandas as pd

from AI_Gen.Gramm_Set import model

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
        await dp.bot.send_message(Noah,'Вы в функциональном состоянии. Доступные Функции. \n (Пул Слов.) \n T01 \n T02')
    
        if message.text == 'Я состоятельный' :
    
            await message.answer('Ваше состояние : Функциональное - Слова')
        elif message.text == 'Пул Слов.':
            """
            Создает ЦСВ ФАЙЛ данных слов для грамматической модели.
            """
            await message.answer('Как будете готовы. Напишите любое сообщение.')
            await Word_Type.Pulling.set()

           
        elif message.text == 'T01':
            await message.answer('Как будете готовы. Напишите любое сообщение.')
            await Word_Type.Testing.set()

        elif message.text == 'T02':
            await message.answer('Прошу вводить только одно слово, даже если ввёдете предложения, я учту только первое слово.')
            await Word_Type.TT_Set.set()
        
            
            
    
        else:
            await message.answer('Неа, вы ошиблись.')
            # Запоминание Слов
            """
            if REM_STATE == True:
                try:
                    
                    
                    lines = (message.text).splitlines()
                    bag_of_word = []

                    for line in lines:
                        for w in line.split():
                            except_symbol = ['.','?',',','(',')','!',"'",'"','-']

                            word = [i for i in w if i not in except_symbol]
                            #symbols = [i for i in w if i in except_symbol]
                            word = ''.join(word)
                            
                            bag_of_word.append(word)
                    print(bag_of_word)
                    for word in bag_of_word:
                        if word == '':
                            word = 'пустота'
                        else:
                            #print(word)
                            word = word.lower()
                            #print(normal_word)
                            word_params['Слово'] = word
                            word_params['Тип'] = G_Delay(parse(word))
                            #print(word_params)
                            
                            #print(word)
                            Word_add = Word_func.New(word_params)
                            Word_add.learn_word()
                    #await message.answer('Оке...')
                except Exception as _ex:
                    print('Запоминание слов пошло пиздй братанчик.',_ex)
            """

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


@dp.message_handler(state=Word_Type.Testing)
async def model_test(message: types.Message,state: FSMContext):
    await message.answer('Ок, запускаю модель.')

    await message.answer(model())

    await state.finish()


@dp.message_handler(state=Word_Type.TT_Set)
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
    better_data = [template['Длина'],template['Количество слогов.'],template['Код']]

    data = better_data

    code = data[2] # Забираем лист с индексами из массива данных

    
    Code_Columns = [] 
    Additional_Col = ['Lenght','P_Amount']
    
    def Column_Create(d):
        
        try:    
            for w_index in range(40):
                
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
        while len(new_data) < 42:
            new_data.append(0)
        #collected_data.append(new_data)
            
    
    
        return new_data
    
    Column_Create(code)
    
    DF_Columns = Additional_Col + Code_Columns
    proc_data = data_trans(data)
    #print(f'Test Data : {proc_data}')
    testf = pd.DataFrame([proc_data], columns = DF_Columns) # X_DF
    #print(DF_Columns)

    await message.answer(model(testf))
    await message.answer('Продолжаем?')
    await Word_Type.Reset_Ask.set()

    #await state.finish()

@dp.message_handler(state=Word_Type.Reset_Ask)
async def WTS_Test(message: types.Message,state:FSMContext):
    if message.text == 'Да.':
        await message.answer('Следующее слово?')
        await Word_Type.TT_Set.set()
        
    else:
        await state.finish()




