import sqlite3
from datetime import datetime
import os

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('reports.db')
    cursor = conn.cursor()

    # Создание таблицы сотрудников
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            user_id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            position TEXT,
            brigade_id INTEGER,
            FOREIGN KEY (brigade_id) REFERENCES brigades(id)
        )
    ''')

    # Создание таблицы бригад
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS brigades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            member_count INTEGER DEFAULT 0
        )
    ''')

    # Создание таблицы инструментов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tools (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER DEFAULT 0,
            in_repair INTEGER DEFAULT 0,
            photo_path TEXT
        )
    ''')

    # Создание таблицы заявок на материалы
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS material_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brigade_id INTEGER,
            material_name TEXT NOT NULL,
            request_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            photo_path TEXT,
            FOREIGN KEY (brigade_id) REFERENCES brigades(id)
        )
    ''')

    # Создание таблицы отчетов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            report_text TEXT NOT NULL,
            report_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            photo_path TEXT,
            FOREIGN KEY (user_id) REFERENCES employees(user_id)
        )
    ''')

    # Создание таблицы смен
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS shifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            shift_start DATETIME,
            shift_end DATETIME,
            FOREIGN KEY (user_id) REFERENCES employees(user_id)
        )
    ''')

    conn.commit()
    conn.close()

# Регистрация сотрудника
def register_employee(user_id, username, position):
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO employees (user_id, username, position) VALUES (?, ?, ?)', (user_id, username, position))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Ошибка при регистрации сотрудника: {e}")
        return False

# Добавление отчета
def add_report(user_id, report_text, photo_path=None):
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO reports (user_id, report_text, photo_path) VALUES (?, ?, ?)', (user_id, report_text, photo_path))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении отчета: {e}")
        return False

# Начало смены
def start_shift(user_id):
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO shifts (user_id, shift_start) VALUES (?, ?)', (user_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Ошибка при начале смены: {e}")
        return False

# Завершение смены
def end_shift(user_id):
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE shifts SET shift_end = ? WHERE user_id = ? AND shift_end IS NULL', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), user_id))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Ошибка при завершении смены: {e}")
        return False

# Получение смен сотрудника
def get_user_shifts(user_id):
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('SELECT shift_start, shift_end FROM shifts WHERE user_id = ?', (user_id,))
        shifts = cursor.fetchall()
        conn.close()
        return shifts
    except sqlite3.Error as e:
        print(f"Ошибка при получении смен: {e}")
        return []

# Создание бригады
def create_brigade_db(brigade_name):
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO brigades (name) VALUES (?)', (brigade_name,))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Ошибка при создании бригады: {e}")
        return False

# Получение списка бригад
def get_brigades():
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM brigades')
        brigades = cursor.fetchall()
        conn.close()
        return brigades
    except sqlite3.Error as e:
        print(f"Ошибка при получении списка бригад: {e}")
        return []

# Добавление инструмента
def add_tool_db(tool_name, quantity):
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tools (name, quantity) VALUES (?, ?)', (tool_name, quantity))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении инструмента: {e}")
        return False

# Получение списка инструментов
def get_tools():
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, quantity FROM tools')
        tools = cursor.fetchall()
        conn.close()
        return tools
    except sqlite3.Error as e:
        print(f"Ошибка при получении списка инструментов: {e}")
        return []

# Заявка на материал
def request_material_db(brigade_id, material_name):
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO material_requests (brigade_id, material_name) VALUES (?, ?)', (brigade_id, material_name))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Ошибка при отправке заявки на материал: {e}")
        return False

# Получение всех отчетов
def get_all_reports():
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, report_text FROM reports')
        reports = cursor.fetchall()
        conn.close()
        return reports
    except sqlite3.Error as e:
        print(f"Ошибка при получении отчетов: {e}")
        return []

# Получение всех смен
def get_all_shifts():
    try:
        conn = sqlite3.connect('reports.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, shift_start, shift_end FROM shifts')
        shifts = cursor.fetchall()
        conn.close()
        return shifts
    except sqlite3.Error as e:
        print(f"Ошибка при получении смен: {e}")
        return []

# Инициализация базы данных при первом запуске
if not os.path.exists('reports.db'):
    init_db()