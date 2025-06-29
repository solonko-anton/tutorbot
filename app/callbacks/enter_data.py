from app.ui.user_router import user_router
from aiogram import F, types
from app.ui.keyboard.data.enter_student import enter_student_data

@user_router.callback_query(F.data == "role_student")
async def handle_student_data(callback: types.CallbackQuery):
    await callback.message.answer(
        text="Share number",
        reply_markup=enter_student_data()
    )


@user_router.callback_query(F.data == "role_teacher")
async def handle_teacher_data(callback: types.CallbackQuery):
    await callback.message.answer(
    )
    await callback.answer()
