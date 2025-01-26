from telegram import Update
from telegram.ext import CallbackContext
from ..database.db import start_shift, end_shift, get_user_shifts
from ..utils.keyboards import shifts_menu

def shift_start(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /shift_start. Начинает смену для пользователя.
    """
    user_id = update.message.from_user.id
    if start_shift(user_id):
        update.message.reply_text("Смена начата!", reply_markup=shifts_menu())
    else:
        update.message.reply_text("Ошибка при начале смены. Возможно, у вас уже есть активная смена.")

def shift_end(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /shift_end. Завершает смену для пользователя.
    """
    user_id = update.message.from_user.id
    if end_shift(user_id):
        update.message.reply_text("Смена завершена!", reply_markup=shifts_menu())
    else:
        update.message.reply_text("Ошибка при завершении смены. Возможно, у вас нет активной смены.")

def view_shifts(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /view_shifts. Показывает все смены пользователя.
    """
    user_id = update.message.from_user.id
    shifts = get_user_shifts(user_id)
    if shifts:
        shift_messages = []
        for shift in shifts:
            shift_start_time = shift[0]
            shift_end_time = shift[1] if shift[1] else "еще не завершена"
            shift_messages.append(f"Начало: {shift_start_time}, Конец: {shift_end_time}")
        update.message.reply_text("\n".join(shift_messages), reply_markup=shifts_menu())
    else:
        update.message.reply_text("У вас нет зарегистрированных смен.", reply_markup=shifts_menu())