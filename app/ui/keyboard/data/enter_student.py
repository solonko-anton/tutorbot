from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types
from aiogram.utils.i18n import gettext as _


def enter_student_data() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.add(
        types.KeyboardButton(
            text=_("Share contacts"),
            request_contact=True,
        )
    )
    return builder.as_markup(one_time_keyboard=True, resize_keyboard=True)
