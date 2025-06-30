from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types


def enter_student_data() -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.add(
        types.KeyboardButton(
            text="Register",
            request_contact=True,
        )
    )
    return builder.as_markup(one_time_keyboard=True, resize_keyboard=True)
