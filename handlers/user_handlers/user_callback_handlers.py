from aiogram import Router, F
from aiogram.types import CallbackQuery

from database import users_db
from keyboards import create_pagination_keyboard, create_editor_keyboard
from lexicon import LEXICON_RU
from services import book
from filters import PageNumberPressedFilter, DeleteBookmarksFilter, GoToThisPage


router: Router = Router()


@router.callback_query(F.data == LEXICON_RU['forward_cb'])
async def next_page_process(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] < len(book):
        users_db[callback.from_user.id]['page'] += 1
        await callback.message.edit_text(
            text=book[users_db[callback.from_user.id]['page']],
            reply_markup=create_pagination_keyboard(users_db[callback.from_user.id]['page'])
        )
    await callback.answer()


@router.callback_query(F.data == LEXICON_RU['backward_cb'])
async def previous_page_process(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        await callback.message.edit_text(
            text=book[users_db[callback.from_user.id]['page']],
            reply_markup=create_pagination_keyboard(users_db[callback.from_user.id]['page'])
        )
    await callback.answer()


@router.callback_query(PageNumberPressedFilter())
async def page_number_pressed_process(callback: CallbackQuery):
    page_number = int(callback.data.split('/')[0])
    if not (page_number in users_db[callback.from_user.id]['bookmarks']):
        users_db[callback.from_user.id]['bookmarks'].add(page_number)
        await callback.answer(
            text=LEXICON_RU['marks_added']
        )
    else:
        await callback.answer(
            text=LEXICON_RU['marks_not_added']
        )
    await callback.answer()


@router.callback_query(F.data == LEXICON_RU['edit_marks_cb'])
async def edit_button_pressed_process(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['edit_marks_text'],
        reply_markup=create_editor_keyboard(*users_db[callback.from_user.id]['bookmarks'])
    )
    await callback.answer()


@router.callback_query(F.data == LEXICON_RU['cancel_edition_cb'] or F.data == LEXICON_RU['close_marks_menu_cb'])
async def close_editor_process(callback: CallbackQuery):
    await callback.message.answer(
        text=LEXICON_RU['cancel_edition_text']
    )
    await callback.answer()


@router.callback_query(DeleteBookmarksFilter())
async def delete_bookmark_from_list_process(callback: CallbackQuery,
                                            page_number: int):
    users_db[callback.from_user.id]['bookmarks'].remove(page_number)
    await callback.message.edit_text(
        text=LEXICON_RU['edit_marks_text'],
        reply_markup=create_editor_keyboard(*users_db[callback.from_user.id]['bookmarks'])
    )
    await callback.answer()


@router.callback_query(GoToThisPage())
async def go_to_this_page_process(callback: CallbackQuery,
                                  page_number: int):
    users_db[callback.from_user.id]['page'] = page_number
    await callback.message.edit_text(
        text=book[page_number],
        reply_markup=create_pagination_keyboard(page_number)
    )
