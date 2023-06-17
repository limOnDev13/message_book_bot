from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class PageNumberPressedFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return ('/' in callback.data) and (callback.data.replace('/', '')).isdigit()


class DeleteBookmarksFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool | dict[str, int]:
        if callback.data[:3] == 'del' and callback.data[3:].isdigit():
            return {'page_number': int(callback.data.replace('del', ''))}
        else:
            return False


class GoToThisPage(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool | dict[str, int]:
        if callback.data[:5] == 'go_to' and callback.data[5:].isdigit():
            return {'page_number': int(callback.data.replace('go_to', ''))}
        else:
            return False
