from datetime import datetime
from sqlite3 import Connection, Cursor

class Employee:
    """Модель сотрудника."""
    def __init__(self, user_id: int, username: str, position: str, brigade_id: int = None):
        self.user_id = user_id
        self.username = username
        self.position = position
        self.brigade_id = brigade_id

    def save(self, conn: Connection) -> bool:
        """Сохраняет сотрудника в базу данных."""
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO employees (user_id, username, position, brigade_id)
                VALUES (?, ?, ?, ?)
                ''',
                (self.user_id, self.username, self.position, self.brigade_id)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка при сохранении сотрудника: {e}")
            return False

class Brigade:
    """Модель бригады."""
    def __init__(self, name: str, member_count: int = 0):
        self.name = name
        self.member_count = member_count

    def save(self, conn: Connection) -> bool:
        """Сохраняет бригаду в базу данных."""
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO brigades (name, member_count)
                VALUES (?, ?)
                ''',
                (self.name, self.member_count)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка при сохранении бригады: {e}")
            return False

class Tool:
    """Модель инструмента."""
    def __init__(self, name: str, quantity: int, in_repair: int = 0, photo_path: str = None):
        self.name = name
        self.quantity = quantity
        self.in_repair = in_repair
        self.photo_path = photo_path

    def save(self, conn: Connection) -> bool:
        """Сохраняет инструмент в базу данных."""
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO tools (name, quantity, in_repair, photo_path)
                VALUES (?, ?, ?, ?)
                ''',
                (self.name, self.quantity, self.in_repair, self.photo_path)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка при сохранении инструмента: {e}")
            return False

class MaterialRequest:
    """Модель заявки на материал."""
    def __init__(self, brigade_id: int, material_name: str, request_date: datetime = None, photo_path: str = None):
        self.brigade_id = brigade_id
        self.material_name = material_name
        self.request_date = request_date or datetime.now()
        self.photo_path = photo_path

    def save(self, conn: Connection) -> bool:
        """Сохраняет заявку на материал в базу данных."""
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO material_requests (brigade_id, material_name, request_date, photo_path)
                VALUES (?, ?, ?, ?)
                ''',
                (self.brigade_id, self.material_name, self.request_date, self.photo_path)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка при сохранении заявки на материал: {e}")
            return False

class Report:
    """Модель отчета."""
    def __init__(self, user_id: int, report_text: str, report_date: datetime = None, photo_path: str = None):
        self.user_id = user_id
        self.report_text = report_text
        self.report_date = report_date or datetime.now()
        self.photo_path = photo_path

    def save(self, conn: Connection) -> bool:
        """Сохраняет отчет в базу данных."""
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO reports (user_id, report_text, report_date, photo_path)
                VALUES (?, ?, ?, ?)
                ''',
                (self.user_id, self.report_text, self.report_date, self.photo_path)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка при сохранении отчета: {e}")
            return False

class Shift:
    """Модель смены."""
    def __init__(self, user_id: int, shift_start: datetime, shift_end: datetime = None):
        self.user_id = user_id
        self.shift_start = shift_start
        self.shift_end = shift_end

    def save(self, conn: Connection) -> bool:
        """Сохраняет смену в базу данных."""
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO shifts (user_id, shift_start, shift_end)
                VALUES (?, ?, ?)
                ''',
                (self.user_id, self.shift_start, self.shift_end)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка при сохранении смены: {e}")
            return False