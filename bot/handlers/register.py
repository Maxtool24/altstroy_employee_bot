from telegram import Update
from telegram.ext import CallbackContext
from ..database.db import register_employee

def register(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /register.
    Регистрирует сотрудника в базе данных.
    """
    # Получаем данные пользователя
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    position = ' '.join(context.args) if context.args else 'Рабочий'  # Должность (если указана)

    # Регистрируем сотрудника в базе данных
    if register_employee(user_id, username, position):
        update.message.reply_text("Вы успешно зарегистрированы!")
    else:
        update.message.reply_text("Ошибка при регистрации. Возможно, вы уже зарегистрированы.")