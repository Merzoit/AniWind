from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def get_start_menu_keyboard():
    """
    Кнопки стартового меню
    -Личный кабинет
    -Склад
    -Бой
    Отправляет меню в чат пользователю
    """
    button_lk = InlineKeyboardButton(
        text="🛡 Личный кабинет 🛡", 
        callback_data="button_lk"
    )
    button_storage = InlineKeyboardButton(
        text="📦 Склад 📦", 
        callback_data="button_storage"
    )
    button_fight = InlineKeyboardButton(
        text="⚔️ В бой ⚔️", 
        callback_data="button_queue"
    )
    # Регистрация кнопок
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_lk], 
            [button_storage], 
            [button_fight]
        ]
    )
    return keyboard

def get_back_keyboard():
    """
    Кнопка назад
    Удаляет сообщение
    """
    button_back = InlineKeyboardButton(
        text="Назад", 
        callback_data="button_back"
    )
    return InlineKeyboardMarkup(inline_keyboard=[[button_back]])

def get_fight_keyboard():
    """
    Боевая сетка кнопок
    Возвращает внутреннее боевое меню выбора карточек
    """
    fight_keyboard = ReplyKeyboardMarkup(
        keyboard=[], 
        resize_keyboard=True, 
        one_time_keyboard=True
    )

    # Первый ряд кнопок
    card_1_1 = KeyboardButton(text="Выбрать карточку")
    card_1_2 = KeyboardButton(text="Наруто(2)")
    card_1_3 = KeyboardButton(text="Выбрать карточку")
    fight_keyboard.keyboard.append(
        [
            card_1_1, 
            card_1_2, 
            card_1_3
        ]
    )
    # Второй ряд кнопок
    card_2_1 = KeyboardButton(text="Выбрать карточку")
    card_2_2 = KeyboardButton(text="Выбрать карточку")
    card_2_3 = KeyboardButton(text="Выбрать карточку")
    fight_keyboard.keyboard.append(
        [
            card_2_1, 
            card_2_2, 
            card_2_3
        ]
    )
    # Третий ряд кнопок
    card_3_1 = KeyboardButton(text="🃏 Колода 🃏")
    card_3_2 = KeyboardButton(text="🩸 Сдаться 🩸")
    fight_keyboard.keyboard.append(
        [
            card_3_1, 
            card_3_2
        ]
    )
    return fight_keyboard