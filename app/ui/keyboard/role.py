from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def get_role_choice_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(
        types.InlineKeyboardButton(
            text="Учень", callback_data="role_student"
        ),
        types.InlineKeyboardButton(
            text="Вчитель", callback_data="role_teacher"
        )
    )
    return builder.as_markup()