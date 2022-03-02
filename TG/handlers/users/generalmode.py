from aiogram import types
from aiogram.dispatcher import FSMContext

from Functional.PM_Func import user_temp
from Functional.VMW_Func import word_temp
from Functional.VMS_Func import sentence_temp

from TG.sql.Person_Mem import Person_M
from TG.sql.Verbal_Mem import VM_Word , VM_Sentence , VM_Context



from TG.loader import dp

import asyncio

from time import sleep
from random import randint


# TODO Это все потом в отчистку.

#340981880 Мой Айди



template = user_temp() # Это темплейт заполнения нового пользователя
user_data = template.create()

word_template = word_temp() # Темплейт запоминания слов
word_params = word_template.create()

sent_template = sentence_temp()
sent_config = sent_template.create()


non_duple_counter = 0

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    global non_duple_counter

    current_user = message.from_user
    Noah = 340981880

    user_data['ID'] = current_user.id
    user_data['Имя'] = current_user.first_name
    user_data['Фамилия'] = current_user.last_name

    P_Add = Person_M.New(user_data) # Занесение шаблона в Класс
    P_Get = Person_M.Get() # Инициализация класса получение данных о пользователе
    P_Editor = Person_M.Edit() # Инициализация класс редактирования данных пользователя
    actual_UD = P_Get.person(current_user.id) # Получение данных о пользователе, если таковой имеется.

    Word_func = VM_Word()
    VM_Get = VM_Word.Get()
    VM_Edit = VM_Word.Edit()

    

    try:
        if str(current_user.id) in actual_UD['ID']:
            if non_duple_counter == 0:

                await dp.bot.send_message(current_user.id, f'Приветствую {current_user.first_name}.')
                non_duple_counter += 1
                
            if current_user.id == Noah:
                if message.text == 'Я состоятельный' :
                    await message.answer('К сожалению я не могу определить вашего состояния')
                
                elif message.text == 'Мои Данные':
                    await message.answer(actual_UD)
                elif message.text == 'Го дружить.':
                    await message.answer(f'Теперь мы друзья?')
                    P_Editor.reputation('friendship',4,actual_UD)
                elif message.text == 'Топ Личностей.' :
                    await message.answer(f'Я пытаюсь но... \n по моему нихуя... {P_Get.top_persons()}')
                elif (message.text).startswith('Распознай предложение : ') == True:
                    sentence_to_proc = (message.text)[24:]
                    bag_of_word = (sentence_to_proc).split(' ')
                    try:
                        for word in bag_of_word:
                            VM_Get.one_word(word)
                        print('Вроде распознала')
                    except Exception as _ex:
                        print('Либо нет такого слова, либо какая то хуйня. [SENTENCE]', _ex)
                elif (message.text).startswith('Слово по номеру : ') == True:
                    
                    
                    wordId_to_proc = (message.text)[19:]
                    
                    try:
                        
                        pulled_word = VM_Get.word_by_id(wordId_to_proc)
                        print(f"Ты о [{pulled_word['Слово']}] ?")
                        await message.answer(f"""Ты о "{pulled_word['Слово']}" ?""")
                    except Exception as _ex:
                        print('Либо нет такого слова, либо какая то хуйня. [WORD_BY_ID]', _ex)
                    
                elif message.text == 'Обработчик говна':
                    try:
                        Sentence_Get = VM_Sentence.Get()
                        result = Sentence_Get.sentence_data('Мойсес')
                        await message.answer(result)
                        #print(result)
                    except Exception as _ex:
                        print('-Не братан, ты хуйню опять сделал, ошибка в обработчике говна',_ex)


                else:
                    try:
                        bag_of_word = (message.text).split(' ')
                        #print(bag_of_word)
                        for word in bag_of_word: 
                            word_params['Слово'] = word 
                            #print(word_params)
                            
                            
                            Word_add = Word_func.New(word_params)
                            Word_add.learn_word()

                    except Exception as _ex:
                        print('Запоминание слов пошло пиздй братанчик.')


                    try:
                        sent_config['Предложение'] = message.text
                        sent_config['От кого'] = current_user.id
                        Sentence_Func = VM_Sentence.New(sent_config)
                        Sentence_Func.sent_reg()
                    except Exception as _ex: 
                        print('Регистрация предложения провалилась. Ну или просто коряво прошла. Я хз ес чесна.',_ex)


                    
                    try:
                        VM_Get = VM_Word.Get()
                        sentence_lenght = randint(2,10)

                        sentence_parts = []
                        sent = ''
                        exception_counter = 0
                        limiter = 0
                        while limiter < sentence_lenght:
                            try:
                                max_ID = VM_Get.max_id()
                                word_ident = str(randint(1,int(max_ID['ID'])))
                                pulled_word = VM_Get.word_by_id(word_ident)
                                sentence_parts.append(pulled_word['Слово'])
                                limiter += 1
                            except Exception as _ex:
                                #print('ОШИБКА БРАТАН. СЕНТЕНС КОНСТРУКТОР ХУЙНЯ',_ex)
                                if exception_counter < 10:
                                    continue
                                else:
                                    break

                        sent = ' '.join(sentence_parts)
                        await message.answer(sent)
                    except Exception as _ex:
                        print('При попытке спиздануть что то, возникла ошибка',_ex)
                    

            else:
                pass

        else:
            await dp.bot.send_message(Noah,'Бред какой. По пользователю нет совпадений, но он есть???')

        
    except Exception as _ex:
        #
        print(f'[{_ex}] \n - Несуществующий пользователь? Проводим запоминание... ')
        try:
            if current_user.id == Noah:
                user_data['Внешность'] = 'photo/Noah_Photo/Noah.jpg' 
                user_data['Данные о Личности'] = 'Создатель Приюта. Администратор'
                
                user_data['Пол'] = 'male'
                user_data['День Рождения'] = '2003-10-18'
                user_data['Отношение от'] = 10
                
                
                P_Add = Person_M.New(user_data)
                
                P_Add.person()
            else:
                P_Add = Person_M.New(user_data)
                P_Add.person()
        except Exception as _ex:
            print(f'Возникла ошибка при запоминании данных [{_ex}]')   



# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    current_user = message.from_user
    Noah = 340981880
    if current_user.id == Noah:
        await message.answer("Обнаружено неизвестное состояние. Возвращаю состояние к изначальному.")
        
        await state.finish()
    else:
        await dp.bot.send_message(Noah, message.from_user.id)
        
        await state.finish()
