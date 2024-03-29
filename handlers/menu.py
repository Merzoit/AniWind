from aiogram import types, Bot
from aiogram.dispatcher.router import Router
from utils.dbhelper import Database
from utils.keyboards import get_back_keyboard, get_start_menu_keyboard
import datetime
from aiogram.filters.command import CommandStart
from settings import TOKEN


# Экземпляр Router для данного модуля
router = Router()
# Экземпляр Database для данного модуля
db = Database()
# Экземпляр Bot для данного модуля
bot = Bot(token=TOKEN)
#Обработчики
@router.message(CommandStart())
async def start_command(message_or_query):
    """
    Обработчик стартового сообщения /start
    Отправляет в чат приветственное сообщение с меню
    """
    if isinstance(message_or_query, types.Message):
        user = message_or_query.from_user
    else:
        user = message_or_query.from_user
        message_or_query = message_or_query.message
    try:
        await bot.delete_message(user.id, message_or_query.message_id)
    except:
        pass

    start_photo = 'https://s3.timeweb.cloud/210a85b8-2790aa0e-77e8-4b85-92e6-2676c2ee4708/start'
    caption = (
        '⚔️<b> Привет воин! </b>⚔️\n\nЯ - <b>сержант Рокси</b>, я буду твоим наставником, '
        'пока ты не поймёшь что к чему..\n\n В меню ниже ты найдёшь всё что нужно, если нужна '
        'будет помощь, перейди в <b>раздел "Обучение"</b>'
    )
    # Регистрация нового пользователя
    await db.register_user(
        user.id,
        user.username, 
        user.first_name, 
        user.last_name, 
        datetime.datetime.now(),
        'В меню'
    )
    # Отправка ответа
    await message_or_query.answer_photo(
        photo=start_photo,
        caption=caption,
        parse_mode='HTML', reply_markup=get_start_menu_keyboard()
    )

@router.callback_query(lambda c: c.data == 'button_lk')
async def handle_lk_info(query: types.CallbackQuery):
    """
    Обработчик действия кнопки button_lk
    Отправляет в чат строку с информацие о пользвателе
    """
    user = query.from_user
    info_message = (
        '<b>🧾Общая информация🧾</b>\n'
        '<i>----🤵‍ Игровой ID: {}\n'
        '----🌕 Имя: {}\n'
        '----🌑 Фамилия: {}</i>\n\n'
        '<b>📖Прогресс📖</b>\n<i>----⭐️ Уровень: 1\n----💈 Опыт: 0/100</i>\n\n'
        '<b>📊Статистика📊</b>\n<i>----🥇 Побед: 0\n----🥈 Поражений: 0</i>'
    ).format(user.id, user.first_name, user.last_name)
    # Отправка ответа
    await query.message.answer(
        info_message, 
        parse_mode='HTML', 
        reply_markup=get_back_keyboard()
    )

    try:
        await bot.delete_message(user.id, query.message.message_id)
    except:
        pass

@router.callback_query(lambda c: c.data == 'button_back')
async def handle_back(query: types.CallbackQuery):
    """
    Обработчик действия кнопки button_back
    Возвращает стартовое меню
    """
    # Отправка ответа
    await start_command(query.message)
    await bot.delete_message(query.from_user.id, query.message.message_id)
