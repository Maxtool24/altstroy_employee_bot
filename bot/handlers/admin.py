from telegram import Update
from telegram.ext import CallbackContext
from ..database.db import get_all_reports, get_all_shifts
from config import ADMIN_ID

def view_reports(update: Update, context: CallbackContext) -> None:
    """
    Показывает все отчеты сотрудников. Доступно только администратору.
    """
    if update.message.from_user.id == ADMIN_ID:
        reports = get_all_reports()
        if reports:
            # Формируем сообщение со всеми отчетами
            report_messages = []
            for report_id, user_id, report_text, report_date, photo_path in reports:
                message = f"📄 Отчет ID: {report_id}\n"
                message += f"👤 Сотрудник ID: {user_id}\n"
                message += f"📅 Дата: {report_date}\n"
                message += f"📝 Текст: {report_text}\n"
                if photo_path:
                    message += f"📸 Фото: {photo_path}\n"
                report_messages.append(message)
            
            # Отправляем сообщение с отчетами
            update.message.reply_text("\n".join(report_messages))
        else:
            update.message.reply_text("Нет отчетов.")
    else:
        update.message.reply_text("У вас нет доступа к этой команде.")

def view_all_shifts(update: Update, context: CallbackContext) -> None:
    """
    Показывает все смены сотрудников. Доступно только администратору.
    """
    if update.message.from_user.id == ADMIN_ID:
        shifts = get_all_shifts()
        if shifts:
            # Формируем сообщение со всеми сменами
            shift_messages = []
            for shift_id, user_id, shift_start, shift_end in shifts:
                message = f"⏳ Смена ID: {shift_id}\n"
                message += f"👤 Сотрудник ID: {user_id}\n"
                message += f"🕒 Начало: {shift_start}\n"
                message += f"🕔 Конец: {shift_end if shift_end else 'еще не завершена'}\n"
                shift_messages.append(message)
            
            # Отправляем сообщение со сменами
            update.message.reply_text("\n".join(shift_messages))
        else:
            update.message.reply_text("Нет смен.")
    else:
        update.message.reply_text("У вас нет доступа к этой команде.")