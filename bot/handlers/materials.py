from telegram import Update
from telegram.ext import CallbackContext
from ..database.db import request_material_db

def request_material(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /request_material.
    Позволяет сотруднику отправить заявку на материал.
    """
    # Проверяем, переданы ли аргументы
    if not context.args or len(context.args) < 2:
        update.message.reply_text(
            "Пожалуйста, укажите ID бригады и название материала.\n"
            "Пример: /request_material 1 Цемент"
        )
        return

    # Извлекаем ID бригады и название материала
    brigade_id = context.args[0]
    material_name = ' '.join(context.args[1:])

    # Проверяем, что ID бригады является числом
    if not brigade_id.isdigit():
        update.message.reply_text("ID бригады должен быть числом.")
        return

    # Отправляем заявку в базу данных
    if request_material_db(brigade_id, material_name):
        update.message.reply_text(
            f"Заявка на материал '{material_name}' для бригады ID {brigade_id} успешно отправлена!"
        )
    else:
        update.message.reply_text("Ошибка при отправке заявки. Проверьте данные и попробуйте снова.")