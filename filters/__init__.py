"""
Пакет с кастомными фильтрами (если не хватает встроенных фильтров
самого aiogram, или если при регистрации хэндлеров в диспетчере
анонимная функция получается слишком громоздкой)
"""
from .special_filters import PageNumberPressedFilter, DeleteBookmarksFilter, GoToThisPage
