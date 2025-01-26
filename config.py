# Конфигурация бота

# Токен вашего Telegram-бота (получите у @BotFather)
TOKEN = "ВАШ_ТОКЕН"

# ID администратора (ваш Telegram ID)
# Узнать свой ID можно через бота @userinfobot
ADMIN_ID = 123456789  # Замените на ваш ID

# Путь к базе данных SQLite
DATABASE_PATH = "reports.db"

# Путь к папке для хранения фотографий
PHOTOS_DIR = "photos"

# Подпапки для фотографий
TOOLS_PHOTOS_DIR = f"{PHOTOS_DIR}/tools"  # Фото инструментов
REPORTS_PHOTOS_DIR = f"{PHOTOS_DIR}/reports"  # Фото отчетов

# Настройки логирования
LOGGING_CONFIG = {
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "level": "INFO",  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    "filename": "bot.log",  # Файл для записи логов
}