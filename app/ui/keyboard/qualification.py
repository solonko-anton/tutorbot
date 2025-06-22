from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def qualification_button() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(
        types.InlineKeyboardButton(
            text='Перевірити кваліфакацію',
            callback_data='check_qualification'
        ),
        types.InlineKeyboardButton(
            text='Продовжити без перевірки',
            callback_data='continue_without_qualification'
        )
    )
    builder.adjust(1)
    return builder.as_markup()