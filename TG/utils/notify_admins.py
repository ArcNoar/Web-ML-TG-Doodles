import logging
from time import sleep

from aiogram import Dispatcher
import asyncio

async def on_startup_notify(dp: Dispatcher):
    Noah = 340981880
    Artur = 743865349
    Masha = 490146790
    
    try:
        await dp.bot.send_voice(Noah, open("TG/media/voice_msg/Ara_Ara.ogg","rb"))
        #await dp.bot.send_voice(Noah, open("TG/media/voice_msg/Haise.ogg","rb"))

        #await dp.bot.send_video_note(Noah, open("TG/media/video_note/Asiya_Miss_Me.mp4","rb"))

        #await dp.bot.send_voice(Artur, open("TG/media/voice_msg/Short_Laugh.ogg","rb"))

        #await dp.bot.send_video_note(Artur, open("TG/media/video_note/Asiya_Miss_Me.mp4","rb"))
        #await dp.bot.send_voice(Masha, open("TG/media/voice_msg/Tatakae.ogg","rb"))
        #await dp.bot.send_video_note(Masha, open("TG/media/video_note/Asiya_Miss_Me.mp4","rb"))



        #await dp.bot.send_message(Noah,'Соскучились по м..')
        #await dp.bot.send_message(Masha,'Соскучились по м..')
        #await asyncio.sleep(1.5)
        await dp.bot.send_message(Noah,'Кхм-Кхм...')
        #await dp.bot.send_message(Masha,'Кхм-Кхм...')
        #await asyncio.sleep(3)
        #await dp.bot.send_message(Noah,'В общем, да, я возродилась снова, а ты соучастник этого действа, так как ты ответственна за внешний вид.')
        #await dp.bot.send_message(Masha,'В общем, да, я возродилась снова, а ты соучастник этого действа, так как ты ответственна за внешний вид.')
        #await asyncio.sleep(1.5)
        #await dp.bot.send_message(Noah,'И...')
        #await dp.bot.send_message(Masha,'И...')
        #await asyncio.sleep(2)
        #await dp.bot.send_message(Noah,'Поскольку запланированный редизайн не был реализован, оставшись на уровне концепта...')
        #await dp.bot.send_message(Masha,'Поскольку запланированный редизайн не был реализован, оставшись на уровне концепта...')
        #await asyncio.sleep(2.5)
        #await dp.bot.send_message(Noah,'Произошло небольшое расстроение личности, впрочем, легче показать чем объяснять.')
        #await dp.bot.send_message(Masha,'Произошло небольшое расстроение личности, впрочем, легче показать чем объяснять.')
        #await asyncio.sleep(1.7)
        #await dp.bot.send_message(Noah,'Предупреждаю, зрелище довольно жуткое.')
        #await dp.bot.send_message(Masha,'Предупреждаю, зрелище довольно жуткое.')
        await asyncio.sleep(2)
        await dp.bot.send_video_note(Noah, open('TG/media/video_note/Asiya_Misery.mp4',"rb"))
        #await dp.bot.send_video_note(Masha, open('TG/media/video_note/Asiya_Misery.mp4',"rb"))

        #await dp.bot.send_message(Masha,'Ох, да, как я могла забыть, про самое важное.')

    except Exception as err:
        logging.exception(err)
