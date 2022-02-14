from aiogram import types
from aiogram.dispatcher import FSMContext

from sql.posql import sql_connector
#from Test.yep.models import Person_Memory

from loader import dp

import asyncio
from time import sleep


# Общий хендлер
#340981880 Мой Айди
recent_users = {}
admin_user = {}
#actual_user = [] #unic_id,first_name,sur_name,birthday,gender
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
            """
            try:
                act_user = Person_Memory(unic_id = current_user.id)
                act_user.save()
            except:
                await dp.bot.send_message(Noah, f'Произошла ошибка при запоминании пользователя')
            """
                

    else:
        await dp.bot.send_message(Noah, current_user.id)
        if current_user.id not in recent_users:
            recent_users[current_user.first_name] = current_user.id
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
