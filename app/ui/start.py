from aiogram import Router, types
from aiogram.filters.command import CommandStart

from app.ui.keyboard.role import get_role_choice_keyboard

user_router = Router()


@user_router.message(CommandStart())
async def startbot(message: types.Message):
    await message.answer(
        text="Вітаю! Оберіть вашу роль:", reply_markup=get_role_choice_keyboard()
    )
