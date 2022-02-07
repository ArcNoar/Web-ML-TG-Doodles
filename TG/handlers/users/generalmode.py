from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

import asyncio
from time import sleep


# Общий хендлер
#340981880

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if message.from_user.id == 340981880 :
        if message.text == 'Я состоятельный' :
            await message.answer('К сожалению я не могу определить вашего состояния')
        else:
            await dp.bot.send_message(340981880, f'Извините, {message.from_user.first_name}')
            await message.answer(f"Не поняла запроса\n"
                                 f"Ваше сообщение:\n"
                                 f"{message.text}")
    
    else:
        pass



# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.from_user.id == 340981880:
        await message.answer("Обнаружено неизвестное состояние. Возвращаю состояние к изначальному.")
        await state.finish()
    else:
        await dp.bot.send_message(340981880, message.from_user.id)
        await state.finish()
