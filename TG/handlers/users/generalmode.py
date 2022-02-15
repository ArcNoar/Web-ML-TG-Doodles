from aiogram import types
from aiogram.dispatcher import FSMContext

from Functional.PM_Func import data_temp, rep_refresh
from TG.sql.posql import PM_Sql

from TG.loader import dp

import asyncio
from time import sleep


# Общий хендлер
#340981880 Мой Айди
#Constant Var
recent_users = {}
admin_user = {}
template = data_temp()
user_data = template.create()



@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    current_user = message.from_user
    Noah = 340981880
    if current_user.id == Noah :
        if message.text == 'Я состоятельный' :
            await message.answer('К сожалению я не могу определить вашего состояния')
        elif message.text == 'Выдай мне список недавних пользователей.':
            await message.answer(f'Список недавних пользователей: \n {recent_users}')
        else:
            await dp.bot.send_message(Noah, f'Извините, {current_user.first_name}')
            await message.answer(f"Не поняла запроса\n"
                                 f"Ваше сообщение:\n"
                                 f"{message.text}")
        if current_user.first_name in recent_users or current_user.first_name in admin_user:
            pass
        else:
            recent_users[current_user.first_name] = current_user.id
            admin_user[current_user.first_name] = current_user.id
            try:
                
                user_data['ID'] = current_user.id
                user_data['Имя'] = current_user.first_name
                user_data['Фамилия'] = current_user.last_name
                
                user_data['Пол'] = 'male'
                user_data['День Рождения'] = '2003-10-18'
                
                
                Person_Memory = PM_Sql(user_data)
                
                Person_Memory.add_to()
            except:
                print('Возникла ошибка при запоминании данных')


            
                

    else:
        await dp.bot.send_message(Noah, current_user.id)
        if current_user.id not in recent_users:
            recent_users[current_user.first_name] = current_user.id
            try:
                user_data['ID'] = current_user.id
                user_data['Имя'] = current_user.first_name
                user_data['Фамилия'] = current_user.last_name
                
                Person_Memory = PM_Sql(user_data)
                Person_Memory.add_tp()
            except:
                print('Возникла ошибка при запоминании данных')
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
        if current_user.id not in recent_user:
            recent_user[current_user.id] = current_user.first_name
        else:
            pass
        await state.finish()
