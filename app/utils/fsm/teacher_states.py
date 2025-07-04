from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.utils.i18n import gettext as _
from aiogram.utils.chat_action import ChatActionSender
from app.bot import bot
from app.ui.keyboard.qualification import qualification_button


class TeacherStates(StatesGroup):
    user_id = State()
    verified = State()
    years_of_expiriens = State()
    description = State()


teacher_router = Router()

@teacher_router.callback_query(F.data == "role_teacher")
async def handle_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(TeacherStates.years_of_expiriens)

    async with ChatActionSender.typing(bot=bot, chat_id=callback.message.chat.id):
        await callback.message.answer(
            text=_("""How many years of experience do you have in your field?
(Only numbers are accepted, e.g. 3.5)""")
        )

@teacher_router.message(TeacherStates.years_of_expiriens, F.text)
async def handle_years_of_exp(message: types.Message, state: FSMContext):
    years = message.text.strip()
    await state.update_data(years_of_expiriens=years)
    await state.set_state(TeacherStates.description)

    await message.answer(
        text=_("Describe your expirience")
    )

@teacher_router.message(TeacherStates.description, F.text)
async def handle_years_of_exp(message: types.Message, state: FSMContext):
    desc = message.text
    await state.update_data(description=desc)

    await message.answer(
        text=_("For a successful student search, you should confirm your qualifications"),
        reply_markup=qualification_button()
    )