import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from .handlers import (
    start, register, report, shifts, brigades, tools, materials, admin
)
from .utils.keyboards import main_menu
from config import TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    # Инициализация бота
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Регистрация обработчиков команд
    dp.add_handler(CommandHandler("start", start.start))
    dp.add_handler(CommandHandler("register", register.register))
    dp.add_handler(CommandHandler("report", report.report))
    dp.add_handler(CommandHandler("shift_start", shifts.shift_start))
    dp.add_handler(CommandHandler("shift_end", shifts.shift_end))
    dp.add_handler(CommandHandler("view_shifts", shifts.view_shifts))
    dp.add_handler(CommandHandler("create_brigade", brigades.create_brigade))
    dp.add_handler(CommandHandler("view_brigades", brigades.view_brigades))
    dp.add_handler(CommandHandler("add_tool", tools.add_tool))
    dp.add_handler(CommandHandler("view_tools", tools.view_tools))
    dp.add_handler(CommandHandler("request_material", materials.request_material))
    dp.add_handler(CommandHandler("view_reports", admin.view_reports))
    dp.add_handler(CommandHandler("view_all_shifts", admin.view_all_shifts))

    # Обработка текстовых сообщений (кнопки)
    dp.add_handler(MessageHandler(Filters.text("📝 Отчет"), report.report))
    dp.add_handler(MessageHandler(Filters.text("🛠 Инструменты"), tools.view_tools))
    dp.add_handler(MessageHandler(Filters.text("👥 Бригады"), brigades.view_brigades))
    dp.add_handler(MessageHandler(Filters.text("⏳ Смены"), shifts.view_shifts))
    dp.add_handler(MessageHandler(Filters.text("🔙 Назад"), start.start))

    # Обработка фото (для отчетов и инструментов)
    dp.add_handler(MessageHandler(Filters.photo, report.handle_photo))

    # Запуск бота
    updater.start_polling()
    logger.info("Бот запущен и работает...")
    updater.idle()

if __name__ == '__main__':
    main()