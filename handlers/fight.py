from aiogram import types, Bot
from aiogram.dispatcher.router import Router
from aiomysql import IntegrityError

from utils.keyboards import get_fight_keyboard
from utils.dbhelper import Database
from settings import TOKEN
# Экземпляр Router для данного модуля
router = Router()
db = Database()
bot = Bot(token=TOKEN)
@router.callback_query(lambda c: c.data == 'button_queue')
async def handle_queue(query: types.CallbackQuery):
    """
    Обработчик события очереди
    Добавляет пользователя в очередь
    """
    user = query.from_user
    try:
        await db.queue_user_add(user.id)
        start_message = f'<b>🌎 Поиск соперника...</b>'
        await bot.send_message(user.id, start_message, parse_mode='HTML')
        await handle_fight(query)
    except IntegrityError as e:
        await bot.send_message(user.id, 'Вы уже в очереди.. Идёт поиск соперника.')
    # Запуск меню выбора карточек

@router.callback_query(lambda c: c.data == 'button_fight')
async def handle_fight(query: types.CallbackQuery):
    """
    Обработчик боевого события
    Начало боя, отправляет пустое поле и информацию о сопернике
    """
    start_message = f'<b>⚔️ Раунд 1 ⚔️</b>\nСоперник: RoxMaster(1)'
    start_photo = 'https://s3.timeweb.cloud/210a85b8-2790aa0e-77e8-4b85-92e6-2676c2ee4708/ui/empty_fields.png'

    # Запуск меню выбора карточек
    await query.bot.send_message(
        query.from_user.id,
        start_message,
        parse_mode='HTML',
        reply_markup=get_fight_keyboard()
    )
    # Отправка в чат стартовой позиции поля
    await query.bot.send_photo(
        query.from_user.id,
        photo=start_photo
    )
    # Удаленние стартового меню
    await query.message.delete()
