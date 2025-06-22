from app.ui.start import user_router
from aiogram import F, types
from app.ui.keyboard.qualification import qualification_button
from app.ui.keyboard.search_teacher import search_teacher_button

@user_router.callback_query(F.data == 'role_student')
async def handle_student_role(callback: types.CallbackQuery):
    await callback.message.answer(
        text="""Будь ласка, введіть мінімальні дані для пошуку вчителя 👇"""
    )

@user_router.callback_query(F.data == 'role_teacher')
async def handle_teacher_role(callback: types.CallbackQuery):
    await callback.message.answer(
        text="""✅ Пройти кваліфікацію — надайте документи, що підтверджують ваші знання, та отримаєте статус «Кваліфікований».

⚠️ Продовжити без перевірки — ви зможете рухатись далі, але ваш статус буде встановлено як «Не кваліфікований».""",
        reply_markup=qualification_button()
    )
    await callback.answer()
    