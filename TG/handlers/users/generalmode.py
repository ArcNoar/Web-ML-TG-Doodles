from aiogram import types
from aiogram.dispatcher import FSMContext

from Functional.PM_Func import data_temp, rep_refresh
from TG.sql.posql import New_data, Get_data, Edit_data

from TG.loader import dp

import asyncio
from time import sleep


# TO DO этот хендлер убогий, пушо он неправильно прописан структурно, проверка на наличие в бд? Так если в бд нет будет ошибка.

#340981880 Мой Айди

recent_users = {} # Два бесполезных словаря но пусть пока что будут
admin_user = {}


template = data_temp() # Это темплейт заполнения нового пользователя
user_data = template.create()




@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    current_user = message.from_user
    Noah = 340981880

    user_data['ID'] = current_user.id
    user_data['Имя'] = current_user.first_name
    user_data['Фамилия'] = current_user.last_name

    Person_Add = New_data(user_data)
    Person_Get = Get_data()
    Person_Editor = Edit_data()
    actual_UD = Person_Get.person(current_user.id)

    if current_user.id == Noah :
        if message.text == 'Я состоятельный' :
            await message.answer('К сожалению я не могу определить вашего состояния')
        elif message.text == 'Выдай мне список недавних пользователей.':
            await message.answer(f'Список недавних пользователей: \n {recent_users}')
        elif message.text == 'Мои Данные':
            await message.answer(actual_UD)
        elif message.text == 'Го дружить.':
            await message.answer(f'Теперь мы друзья?')
            Person_Editor.reputation('friendship',4,actual_UD)
            
        if str(current_user.id) in actual_UD['ID']:
            await dp.bot.send_message(Noah, f'Приветствую {current_user.first_name}.')
        else:
            recent_users[current_user.first_name] = current_user.id
            admin_user[current_user.first_name] = current_user.id
            try:
                

                user_data['Внешность'] = 'photo/Noah_Photo/Noah.jpg' 
                user_data['Данные о Личности'] = 'Создатель Приюта. Администратор'
                
                user_data['Пол'] = 'male'
                user_data['День Рождения'] = '2003-10-18'
                
                
                Person_Add = New_data(user_data)
                
                Person_Add.person()
            except Exception as _ex:
                print(f'Возникла ошибка при запоминании данных [{_ex}]')


            
                

    else:
        await dp.bot.send_message(Noah, current_user.id)
        if current_user.id not in recent_users:
            recent_users[current_user.first_name] = current_user.id
            try:
                Person_Add = New_data(user_data)
                Person_Add.person()
            except Exception as _ex:
                print(f'Возникла ошибка при запоминании данных [{_ex}]')
        else:
            pass
        



# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    current_user = message.from_user
    Noah = 340981880
    if current_user.id == Noah:
        await message.answer("Обнаружено неизвестное состояние. Возвращаю состояние к изначальному.")
        if current_user.id not in recent_users and current_user.id not in admin_user:
            recent_users[current_user.first_name] = current_user.id
            admin_user[current_user.first_name] = current_user.id
        else:
            pass
        await state.finish()
    else:
        await dp.bot.send_message(Noah, message.from_user.id)
        if current_user.id not in recent_users:
            recent_users[current_user.id] = current_user.first_name
        else:
            pass
        await state.finish()
