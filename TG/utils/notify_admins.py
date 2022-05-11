import logging

from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    bahus = 736557383 # Не дееспособный айди
    Noah = 340981880
    Artur = 743865349
    Masha = 490146790
    
    try:
        #await dp.bot.send_voice(bahus, open("TG/media/voice_msg/Tatakae.ogg","rb"))
        await dp.bot.send_voice(Noah, open("TG/media/voice_msg/Ara_Ara.ogg","rb"))
        #await dp.bot.send_video_note(Noah, open("TG/media/video_note/Asiya_Miss_Me.mp4","rb"))
        #await dp.bot.send_voice(Artur, open("TG/media/voice_msg/Ara_Ara.ogg","rb"))
        #await dp.bot.send_video_note(Artur, open("TG/media/video_note/Asiya_Miss_Me.mp4","rb"))
        #await dp.bot.send_voice(Masha, open("TG/media/voice_msg/Haise.ogg","rb"))
        #await dp.bot.send_video_note(Masha, open("TG/media/video_note/Asiya_Miss_Me.mp4","rb"))

    except Exception as err:
        logging.exception(err)
