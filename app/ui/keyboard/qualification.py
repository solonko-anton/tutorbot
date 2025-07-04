from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from aiogram.utils.i18n import gettext as _


def qualification_button() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(
        types.InlineKeyboardButton(
            text=_("Confirm qualification"), callback_data="check_qualification"
        ),
        types.InlineKeyboardButton(
            text=_("Continue without confirming"),
            callback_data="continue_without_qualification",
        ),
    )
    builder.adjust(1)
    return builder.as_markup()
