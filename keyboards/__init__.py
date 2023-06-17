"""
Пакет с модулями, в которых хранятся и/или динамически формируются
клавиатуры, отправляемые пользователем ботом, в процессе взаимодействия
"""
from .set_menu import set_main_menu
from .keyboard_utils import create_pagination_keyboard, \
    create_bookmarks_keyboard, create_editor_keyboard
