from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime
import os
from ..database.db import add_report

def report(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /report. Позволяет пользователю отправить отчет.
    Если пользователь прикрепляет фото, оно сохраняется в папку photos/reports.
    """
    user_id = update.message.from_user.id
    report_text = ' '.join(context.args) if context.args else None

    if not report_text:
        update.message.reply_text("Пожалуйста, введите текст отчета после команды /report.")
        return

    # Обработка фото, если оно прикреплено
    photo_path = None
    if update.message.photo:
        # Скачиваем фото
        photo_file = update.message.photo[-1].get_file()
        photo_name = f"report_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        photo_path = os.path.join("photos", "reports", photo_name)

        # Создаем папку, если она не существует
        os.makedirs(os.path.dirname(photo_path), exist_ok=True)

        # Сохраняем фото
        photo_file.download(photo_path)

    # Добавляем отчет в базу данных
    if add_report(user_id, report_text, photo_path):
        update.message.reply_text("Ваш отчет успешно отправлен!")
    else:
        update.message.reply_text("Произошла ошибка при отправке отчета. Попробуйте снова.")