import logging

from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    bahus = 736557383 # Не дееспособный айди
    Noah = 340981880
    try:
        #await dp.bot.send_message(bahus, "Давно не виделись, да?")
        await dp.bot.send_message(Noah, "Успешный Запуск.")

    except Exception as err:
        logging.exception(err)
