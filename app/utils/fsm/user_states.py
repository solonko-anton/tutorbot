from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters.command import CommandStart
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Router, types, F
from app.ui.keyboard.data.enter_student import enter_student_data
from app.bot import bot


class User(StatesGroup):
    first_name = State()
    last_name = State()
    patronymic = State()
    number = State()


registration_router = Router()

@registration_router.message(CommandStart())
async def start_registration(message: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(User.number)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await message.answer(
            text="Enter your phone number",
            reply_markup=enter_student_data()
        )

@registration_router.message(User.number, F.contact)
async def handle_number(message: types.Message, state: FSMContext):
    contact = message.contact
    number = contact.phone_number

    await state.update_data(number=number)
    await state.set_state(User.first_name)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await message.answer(
            text="Enter your first name"
        )

