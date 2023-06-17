"""
Вспомогательные функции / методы, помогающие формировать клавиатуры.
"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon import LEXICON_RU
from services import book


def create_pagination_keyboard(page_number: int) -> InlineKeyboardMarkup:
    bd_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['backward_button'],
        callback_data=LEXICON_RU['backward_cb']
    )
    current_page_format = f'{page_number}/{len(book)}'
    page_number_button: InlineKeyboardButton = InlineKeyboardButton(
        text=current_page_format,
        callback_data=current_page_format
    )
    fd_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['forward_button'],
        callback_data=LEXICON_RU['forward_cb']
    )

    pagination_kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    pagination_kb_builder.row(*[bd_button, page_number_button, fd_button], width=3)
    return pagination_kb_builder.as_markup()


def create_bookmarks_keyboard(*marks: int) -> InlineKeyboardMarkup:
    bookmarks_buttons: list[InlineKeyboardButton] = []

    for mark in sorted(marks):
        mark_button: InlineKeyboardButton = InlineKeyboardButton(
            text=f'{mark} - {book[mark][:100]}',
            callback_data='go_to' + str(mark)
        )
        bookmarks_buttons.append(mark_button)

    edit_marks_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['edit_marks_button'],
        callback_data=LEXICON_RU['edit_marks_cb']
    )

    close_marks_menu_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['close_marks_menu_button'],
        callback_data=LEXICON_RU['close_marks_menu_cb']
    )

    bookmarks_menu_kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    bookmarks_menu_kb_builder.row(*bookmarks_buttons, width=1)
    bookmarks_menu_kb_builder.row(*[edit_marks_button, close_marks_menu_button],
                                  width=2)

    return bookmarks_menu_kb_builder.as_markup()


def create_editor_keyboard(*page_numbers: int) -> InlineKeyboardMarkup:
    editor_buttons: list[InlineKeyboardButton] = []

    for page_number in sorted(page_numbers):
        edit_mark_button: InlineKeyboardButton = InlineKeyboardButton(
            text=f'del {page_number} - {book[page_number][:100]}',
            callback_data='del' + str(page_number)
        )
        editor_buttons.append(edit_mark_button)

    cancel_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['cancel_edition'],
        callback_data=LEXICON_RU['cancel_edition_cb']
    )

    editor_marks_kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    editor_marks_kb_builder.row(*editor_buttons, width=1)
    editor_marks_kb_builder.row(cancel_button, width=1)

    return editor_marks_kb_builder.as_markup()
