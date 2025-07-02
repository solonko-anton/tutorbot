from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from aiogram.utils.i18n import gettext as _


def get_role_choice_keyboard() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(
        types.InlineKeyboardButton(text=_("Student"), callback_data="role_student"),
        types.InlineKeyboardButton(text=_("Teacher"), callback_data="role_teacher"),
    )
    return builder.as_markup()
