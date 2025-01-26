from telegram import Update
from telegram.ext import CallbackContext
from ..utils.keyboards import main_menu

def start(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /start. Отправляет приветственное сообщение и основное меню.
    
    :param update: Объект Update от Telegram.
    :param context: Объект CallbackContext для передачи данных между обработчиками.
    """
    # Получаем информацию о пользователе
    user = update.message.from_user

    # Отправляем приветственное сообщение с основным меню
    update.message.reply_text(
        f"Привет, {user.first_name}! Я бот для управления отчетами и сменами.\n\n"
        "Выберите одну из команд ниже:",
        reply_markup=main_menu()  # Основное меню с кнопками
    )