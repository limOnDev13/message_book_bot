"""
Модуль с хэндлерами, которые не попали в ругие модули с хэндлерами
"""
from aiogram import Router
from aiogram.types import Message

from lexicon import LEXICON_RU


router: Router = Router()


@router.message()
async def other_answers_process(message: Message):
    await message.answer(
        text=LEXICON_RU['other_answers']
    )
