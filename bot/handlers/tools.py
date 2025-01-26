from telegram import Update
from telegram.ext import CallbackContext
from ..database.db import add_tool_db, get_tools, update_tool_photo
import os

def add_tool(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /add_tool. Добавляет инструмент в базу данных.
    """
    try:
        # Получаем аргументы команды
        tool_name = ' '.join(context.args[:-1]) if context.args else None
        quantity = context.args[-1] if context.args and context.args[-1].isdigit() else None

        # Проверяем, что название и количество указаны
        if not tool_name or not quantity:
            update.message.reply_text("Пожалуйста, укажите название инструмента и его количество.\nПример: /add_tool Молоток 5")
            return

        # Добавляем инструмент в базу данных
        if add_tool_db(tool_name, int(quantity)):
            update.message.reply_text(f"Инструмент '{tool_name}' успешно добавлен с количеством {quantity}.")
        else:
            update.message.reply_text("Ошибка при добавлении инструмента.")
    except Exception as e:
        update.message.reply_text(f"Произошла ошибка: {e}")

def add_tool_photo(update: Update, context: CallbackContext) -> None:
    """
    Обработчик для добавления фотографии инструмента.
    """
    try:
        user_id = update.message.from_user.id
        tool_name = ' '.join(context.args) if context.args else None

        # Проверяем, что название инструмента указано
        if not tool_name:
            update.message.reply_text("Пожалуйста, укажите название инструмента.\nПример: /add_tool_photo Молоток")
            return

        # Проверяем, что пользователь отправил фото
        if update.message.photo:
            # Скачиваем фото
            photo_file = update.message.photo[-1].get_file()
            photo_path = f"photos/tools/{tool_name}_{user_id}.jpg"

            # Создаем папку, если она не существует
            os.makedirs(os.path.dirname(photo_path), exist_ok=True)

            # Сохраняем фото
            photo_file.download(photo_path)

            # Обновляем путь к фото в базе данных
            if update_tool_photo(tool_name, photo_path):
                update.message.reply_text(f"Фото для инструмента '{tool_name}' успешно добавлено.")
            else:
                update.message.reply_text("Ошибка при обновлении фото инструмента.")
        else:
            update.message.reply_text("Пожалуйста, отправьте фото инструмента.")
    except Exception as e:
        update.message.reply_text(f"Произошла ошибка: {e}")

def view_tools(update: Update, context: CallbackContext) -> None:
    """
    Обработчик команды /view_tools. Показывает список всех инструментов.
    """
    try:
        # Получаем список инструментов из базы данных
        tools = get_tools()

        if tools:
            # Формируем сообщение с информацией о каждом инструменте
            tool_messages = []
            for tool in tools:
                tool_id, name, quantity, in_repair, photo_path = tool
                tool_messages.append(
                    f"ID: {tool_id}, Название: {name}, Количество: {quantity}, "
                    f"В ремонте: {'Да' if in_repair else 'Нет'}, Фото: {photo_path if photo_path else 'Нет'}"
                )
            update.message.reply_text("\n".join(tool_messages))
        else:
            update.message.reply_text("Нет зарегистрированных инструментов.")
    except Exception as e:
        update.message.reply_text(f"Произошла ошибка: {e}")

def tools_menu(update: Update, context: CallbackContext) -> None:
    """
    Обработчик для меню инструментов.
    """
    update.message.reply_text(
        "Выберите действие:",
        reply_markup=ReplyKeyboardMarkup(
            [
                ['➕ Добавить инструмент', '📋 Список инструментов'],
                ['📸 Добавить фото инструмента', '🔙 Назад']
            ],
            resize_keyboard=True
        )
    )