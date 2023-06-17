"""
Модуль с хэндлерами для пользователей с обычным статусом,
например, для тех, кто запустил бота в первый раз.
"""
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from copy import deepcopy

from database import users_db, user_dict_template
from keyboards import create_pagination_keyboard, create_bookmarks_keyboard
from lexicon import LEXICON_RU
from services import book


router: Router = Router()


@router.message(CommandStart())
async def start_command_process(message: Message):
    if not (message.from_user.id in users_db):
        users_db[message.from_user.id] = deepcopy(user_dict_template)

    await message.answer(text=LEXICON_RU['start'])


@router.message(Command(commands=['help']))
async def help_command_process(message: Message):
    await message.answer(text=LEXICON_RU['help'])


async def show_book(message: Message):
    await message.answer(
        text=book[users_db[message.from_user.id]['page']],
        reply_markup=create_pagination_keyboard(users_db[message.from_user.id]['page'])
    )


@router.message(Command(commands=['beginning']))
async def beginning_command_process(message: Message):
    users_db[message.from_user.id]['page'] = 1
    await show_book(message)


@router.message(Command(commands=['continue']))
async def continue_command_process(message: Message):
    await show_book(message)


@router.message(Command(commands=['bookmarks']))
async def bookmarks_command_process(message: Message):
    if users_db[message.from_user.id]['bookmarks']:
        await message.answer(
            text=LEXICON_RU['bookmarks_answer'],
            reply_markup=create_bookmarks_keyboard(*users_db[message.from_user.id]['bookmarks'])
        )
    else:
        await message.answer(text=LEXICON_RU['no_bookmarks'])
