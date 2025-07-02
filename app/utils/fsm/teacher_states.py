from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, types


class TeacherStates(StatesGroup):
    user_id = State()
    verified = State()
    years_of_expiriens = State()
    description = State()

teacher_router = Router()

