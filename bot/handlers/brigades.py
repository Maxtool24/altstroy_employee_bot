from telegram import Update
from telegram.ext import CallbackContext
from ..database.db import create_brigade_db, get_brigades

def create_brigade(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /create_brigade.
    Создает новую бригаду с указанным названием.
    """
    brigade_name = ' '.join(context.args)  # Получаем название бригады из аргументов команды
    
    if brigade_name:  # Проверяем, что название не пустое
        if create_brigade_db(brigade_name):  # Пытаемся создать бригаду в базе данных
            update.message.reply_text(f"Бригада '{brigade_name}' успешно создана!")
        else:
            update.message.reply_text("Ошибка при создании бригады. Возможно, бригада с таким названием уже существует.")
    else:
        update.message.reply_text("Пожалуйста, укажите название бригады. Пример: /create_brigade Название_бригады")

def view_brigades(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /view_brigades.
    Показывает список всех зарегистрированных бригад.
    """
    brigades = get_brigades()  # Получаем список бригад из базы данных
    
    if brigades:  # Если бригады есть
        # Формируем сообщение с информацией о бригадах
        brigade_messages = "\n".join([f"ID: {id}, Название: {name}" for id, name in brigades])
        update.message.reply_text(f"Список бригад:\n{brigade_messages}")
    else:
        update.message.reply_text("Нет зарегистрированных бригад.")