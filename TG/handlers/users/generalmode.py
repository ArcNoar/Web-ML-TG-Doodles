from aiogram import types
from aiogram.dispatcher import FSMContext

from Functional.PM_Func import user_temp
from Functional.VMW_Func import word_temp
from Functional.VMS_Func import sentence_temp
from Functional.EMR_Func import Emote_Temp

from TG.sql.Person_Mem import Person_M
from TG.sql.Verbal_Mem import VM_Alph ,VM_Word , VM_Sentence , VM_Context
from TG.sql.Soul_Mem import Emote_Reg
from TG.sql.Fundametal_Mem import Ego



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

sent_template = sentence_temp() # Темплейт для запоминания предложения
sent_config = sent_template.create()

emote_template = Emote_Temp()
emote_shell = emote_template.create()

Alph_Get = VM_Alph.Get()


non_duple_counter = 0
ndc2 = 0

TEST_MOD = False

if TEST_MOD == True:
    try:
        for cst in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print(Alph_Get.get_by_construct(cst))

        print('Ебаная хуйня была исполнена брат.')
    except Exception as _ex:
        print('Опять? Только не снови все опять, ок?',_ex)

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    global non_duple_counter, ndc2

    current_user = message.from_user
    Noah = 340981880
    Artur = 743865349

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

    Alph_New = VM_Alph.New()

    Emote_Func = Emote_Reg()
    

    

    try:
        if str(current_user.id) in actual_UD['ID']:
            if non_duple_counter == 0:

                await dp.bot.send_message(current_user.id, f'Приветствую {current_user.first_name}.')
                non_duple_counter += 1
                
            if current_user.id == Noah:
                if message.text == 'Я состоятельный' :
                    await message.answer('К сожалению я не могу определить вашего состояния')
                
                elif (message.text).startswith('Напиши Артуру :') == True:
                    response = (message.text)[15:]
                    print(response)
                    await dp.bot.send_message(743865349, f"{response}")
                    await dp.bot.send_message(Noah, f"{response}")

                else:
                    """
                    try:
                        sentence = message.text

                        words = sentence.split(' ')

                        for word in words:
                            
                            for letter in word:
                                print(letter)
                                Alph_New.add_construct(letter.lower())
                                

                        await message.answer('Хм...')

                    except Exception as _ex:
                        print('Blyat',_ex)
                    """

                    
                    try:
                        bag_of_word = (message.text).split(' ')
                        #print(bag_of_word)
                        for word in bag_of_word: 
                            word_params['Слово'] = word.lower() 
                            #print(word_params)
                            
                            
                            Word_add = Word_func.New(word_params)
                            Word_add.learn_word()

                    except Exception as _ex:
                        print('Запоминание слов пошло пиздй братанчик.')


                    try:
                        sent_config['Предложение'] = (message.text).lower()
                        sent_config['От кого'] = current_user.id
                        Sentence_Func = VM_Sentence.New(sent_config)
                        Sentence_Func.sent_reg()
                    except Exception as _ex: 
                        print('Регистрация предложения провалилась. Ну или просто коряво прошла. Я хз ес чесна.',_ex)


                    """
                    try:
                        
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
                    """
                    
            elif current_user.id == Artur:
                print(message.text)

            else:
                print(message.text)
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

                
                user_data['Отношение от'] = 9
                
                
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
