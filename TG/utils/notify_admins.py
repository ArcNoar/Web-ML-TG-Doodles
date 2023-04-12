import logging
from time import sleep

from aiogram import Dispatcher
import asyncio

async def on_startup_notify(dp: Dispatcher):
    Noah = 340981880
    Artur = 743865349
    Masha = 490146790
    
    try:
        #await dp.bot.send_voice(Noah, open("TG/media/voice_msg/Ara_Ara.ogg","rb"))
    
        #await dp.bot.send_message(Noah,'Кхм-Кхм...')

        print('Симулякрум Запущен.')
      

    except Exception as err:
        logging.exception(err)
