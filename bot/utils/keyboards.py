from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# Основное меню
def main_menu():
    return ReplyKeyboardMarkup(
        [
            ['📝 Отчет', '🛠 Инструменты'],
            ['👥 Бригады', '📦 Материалы'],
            ['⏳ Смены', '👤 Профиль']
        ],
        resize_keyboard=True
    )

# Меню инструментов
def tools_menu():
    return ReplyKeyboardMarkup(
        [
            ['➕ Добавить инструмент', '📋 Список инструментов'],
            ['🔙 Назад']
        ],
        resize_keyboard=True
    )

# Меню бригад
def brigades_menu():
    return ReplyKeyboardMarkup(
        [
            ['➕ Создать бригаду', '📋 Список бригад'],
            ['🔙 Назад']
        ],
        resize_keyboard=True
    )

# Меню смен
def shifts_menu():
    return ReplyKeyboardMarkup(
        [
            ['⏱ Начать смену', '🛑 Завершить смену'],
            ['📋 Мои смены', '🔙 Назад']
        ],
        resize_keyboard=True
    )

# Меню материалов
def materials_menu():
    return ReplyKeyboardMarkup(
        [
            ['📝 Заявка на материал', '📋 Список заявок'],
            ['🔙 Назад']
        ],
        resize_keyboard=True
    )

# Меню администратора
def admin_menu():
    return ReplyKeyboardMarkup(
        [
            ['📊 Все отчеты', '⏳ Все смены'],
            ['🔙 Назад']
        ],
        resize_keyboard=True
    )

# Кнопка "Назад"
def back_button():
    return ReplyKeyboardMarkup(
        [['🔙 Назад']],
        resize_keyboard=True
    )

# Инлайн-кнопки для подтверждения действий
def confirm_keyboard():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("✅ Да", callback_data="confirm_yes")],
            [InlineKeyboardButton("❌ Нет", callback_data="confirm_no")]
        ]
    )

# Инлайн-кнопки для выбора бригады
def brigade_selection_keyboard(brigades):
    buttons = [
        [InlineKeyboardButton(brigade['name'], callback_data=f"brigade_{brigade['id']}")]
        for brigade in brigades
    ]
    return InlineKeyboardMarkup(buttons)

# Инлайн-кнопки для выбора инструмента
def tool_selection_keyboard(tools):
    buttons = [
        [InlineKeyboardButton(tool['name'], callback_data=f"tool_{tool['id']}")]
        for tool in tools
    ]
    return InlineKeyboardMarkup(buttons)