from aiogram import executor

from TG.loader import dp
import TG.middlewares, TG.filters, TG.handlers
from TG.utils.notify_admins import on_startup_notify
from TG.utils.set_bot_commands import set_default_commands



async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    
    # Уведомляет про запуск
    #await on_startup_notify(dispatcher)

    # Дб по идее
    

def start():
    executor.start_polling(dp, on_startup=on_startup, skip_updates= False)




if __name__ == '__main__':
    start()

    