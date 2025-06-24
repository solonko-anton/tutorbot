from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def search_teacher_button() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(
        types.InlineKeyboardButton(text="Пошук вчителя", callback_data="search_teacher")
    )

    return builder.as_markup()
