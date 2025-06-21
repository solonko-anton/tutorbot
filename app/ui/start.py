from main import dp
from aiogram import types
from aiogram.filters.command import Command

@dp.message(Command('start'))
async def startbot(message: types.Message):
    pass