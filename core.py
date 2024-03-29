import asyncio
from aiogram import Bot, Dispatcher, Router

from settings import TOKEN
from utils.dbhelper import Database
from handlers import menu, fight

# Экземпляры bot, database, router для данного модуля
bot = Bot(token=TOKEN)
db = Database()
router = Router()

# Включение роутеров из модулей
router.include_router(menu.router)
router.include_router(fight.router)

async def run():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(run())
