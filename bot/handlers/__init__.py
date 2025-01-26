# Инициализация пакета handlers
from .start import start
from .register import register
from .report import report
from .shifts import shift_start, shift_end, view_shifts, view_all_shifts
from .brigades import create_brigade, view_brigades
from .tools import add_tool, view_tools, add_tool_photo
from .materials import request_material
from .admin import view_reports