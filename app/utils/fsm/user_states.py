from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters.command import CommandStart
from aiogram.utils.chat_action import ChatActionSender
from aiogram import Router, types, F
from aiogram.utils.i18n import gettext as _
from app.ui.keyboard.data.enter_student import enter_student_data
from app.bot import bot
from app.ui.keyboard.role import get_role_choice_keyboard


class User(StatesGroup):
    first_name = State()
    last_name = State()
    patronymic = State()
    number = State()


registration_router = Router()


@registration_router.message(CommandStart())
async def handle_number(message: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(User.number)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await message.answer(
            text=_("Enter your phone number"), reply_markup=enter_student_data()
        )


@registration_router.message(User.number, F.contact)
async def handle_first_name(message: types.Message, state: FSMContext):
    contact = message.contact
    number = contact.phone_number
    tg_id = contact.user_id

    await state.update_data(number=number)
    await state.set_state(User.first_name)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await message.answer(text=_("Enter your first name"))


@registration_router.message(User.first_name, F.text)
async def handle_last_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(User.last_name)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await message.answer(text=_("Enter your last name"))


@registration_router.message(User.last_name, F.text)
async def handle_patronymic(message: types.Message, state: FSMContext):
    await state.update_data(patronymic=message.text)
    await state.set_state(User.patronymic)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await message.answer(
            text=_("Enter your patronymic"),
        )


@registration_router.message(User.patronymic, F.text)
async def handle_role(message: types.Message):
    await message.answer(
        text=_("Choose your role: "),
        reply_markup=get_role_choice_keyboard(),
    )
