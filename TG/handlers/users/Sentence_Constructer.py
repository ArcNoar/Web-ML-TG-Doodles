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

from TG.states.Sent_Construct.Senco import Senco
from Functional.Prima_Func import Prima_SENT
from TG.sql.Prima_Mem import VM_Sentence

"""
1. Вписывать предложения для Асии и сразу присваивать значения правильного или нет
2. Получать дешифровку предложения (У нас уже где то валяется дешифровщик, так что нужно просто разбить его)
3. Заполнять пустые столбцы нулями (Мы зададим определенный предел длины предложения)
4. Создать CSV файл этого дерьма.
"""

sent_template = Prima_SENT() # Темплейт для запоминания предложения
sent_config = sent_template.create()

def random_SENT():
    Sent_GET = VM_Sentence.Get()
    try:
        id_limit = Sent_GET.max_id()
        sentence_id = randint(2,id_limit)

        output_sent = Sent_GET.get_by_id(sentence_id)
        if output_sent['SENT'] != None:
            return output_sent['SENT']
        else:
            print(sentence_id)
            random_SENT()

    except:
        print('Возникла ошибка при пуле предложения')
        

def INCOR_Pull():
    Incor_Get = VM_Sentence.Get()
    try:
        pulled_sentences = Incor_Get.get_all()
        #print(pulled_sentences)
        
        word_bag = []

        for bag in pulled_sentences:
            local_bag = [int(i) for i in bag['SENT_Dech'].split('-')]

            word_bag += local_bag
        
        normal_bog = set(word_bag) # BAG OF WORDS !!!
        
        


        
    except:
        print('Возникла ошибка при пуле предложения')




@dp.message_handler(commands="Senco",state=None)
async def Senco_Init(message: types.Message):
    

    current_user = message.from_user
    Noah = 340981880
    
                
    if current_user.id == Noah:
    
        await Senco.Initial.set()
        await message.answer('Запускаю Фунциональное состояние - SENCO')
        #await dp.bot.send_message(current_user.id,'В общем. Ты перенаправлен в состояние инструктажа. \n Если ты уже проходил этот гайд, то напиши "Пропустить."')

    
    else:
        await message.answer('А ты уверен что у тебя есть права?')


@dp.message_handler(state='*', commands = 'закончили')
@dp.message_handler(Text(equals='закончили', ignore_case = True),state='*')
async def cancel_handler(message: types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ну окэ.')


@dp.message_handler(state=Senco.Initial)
async def Nav_State(message: types.Message,state: FSMContext):
    

    current_user = message.from_user
    Noah = 340981880


    
                
    if current_user.id == Noah:
        await dp.bot.send_message(Noah,"""Вы в функциональном состоянии. Доступные Функции. 
                                        F01 - Занесение правильных предложений.
                                        
                                        
                                        """)
    
        if message.text == 'Я состоятельный' :
    
            await message.answer('Ваше состояние : Функциональное - Внесение корректных предложений')
        elif message.text == 'F01':
            """
            Вносим в дб правильные предложения.
            """
            await message.answer('Как будете готовы. Напишите корректное предложение')
            await Senco.Filling_COR.set()
        
        elif message.text == 'F02':
            """
            Вносим в дб правильные предложения.
            """
            await message.answer('Как будете готовы. Пишите что угодно, и начнется автопул неверных предложений')
            await Senco.Filling_INCOR.set()

        elif message.text == 'Fun_Mode':
            """
            For Fun.
            """
            await message.answer('Это шуточное состояние. Я просто буду вбрасывать случайное предложение.')
            await Senco.Fun_Mode.set()
    
        else:
            await message.answer('Неа, вы ошиблись.')



@dp.message_handler(state=Senco.Filling_COR)
async def Nav_State(message: types.Message,state: FSMContext):
    

    current_user = message.from_user
    Noah = 340981880


    if current_user.id == Noah:
        try:
         
            sent_config['SENT'] = (message.text).lower()
            sent_config['GRADE'] = True
            Sentence_Func = VM_Sentence.New(sent_config)
            Sentence_Func.sent_reg()

            await message.answer('Предложение успешно занесено.')

        except Exception as _ex: 
            print('Регистрация предложения провалилась. Ну или просто коряво прошла. Я хз ес чесна.',_ex)


@dp.message_handler(state=Senco.Filling_INCOR)
async def Nav_State(message: types.Message,state: FSMContext):
    

    current_user = message.from_user
    Noah = 340981880


    if current_user.id == Noah:
        try:

            data_bag = INCOR_Pull()

            #await message.answer('Заебал лови :')

            #await message.answer(f'{data_bag}')
            """
            sent_config['SENT'] = (message.text).lower()
            sent_config['GRADE'] = True
            Sentence_Func = VM_Sentence.New(sent_config)
            Sentence_Func.sent_reg()

            await message.answer('Предложение успешно занесено.')
            """
        except Exception as _ex: 
            print('Регистрация предложения провалилась. Ну или просто коряво прошла. Я хз ес чесна.',_ex)


@dp.message_handler(state=Senco.Fun_Mode)
async def Nav_State(message: types.Message,state: FSMContext):
    

    current_user = message.from_user
    Noah = 340981880


    if current_user.id == Noah:
        try:
            await message.answer(f'{random_SENT()}')

            sent_config['SENT'] = (message.text).lower()
            sent_config['GRADE'] = True
            Sentence_Func = VM_Sentence.New(sent_config)
            Sentence_Func.sent_reg()

            #await message.answer('Предложение успешно занесено.')

        except Exception as _ex: 
            print('Регистрация предложения провалилась. Ну или просто коряво прошла. Я хз ес чесна.',_ex)