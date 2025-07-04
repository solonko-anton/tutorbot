from fastapi import FastAPI, Request

from app.bot import bot, dp
from aiogram.types import Update
from app.config.config import settings
from app.ui.user_router import user_router
from app.utils.fsm.user_states import registration_router
from app.utils.fsm.teacher_states import teacher_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    webhook_url = settings.get_webhook_url()
    dp.include_routers(user_router, 
                       registration_router,
                       teacher_router)
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=None,
        drop_pending_updates=True,
    )
    yield
    await bot.delete_webhook()
    await bot.session.close()


app = FastAPI(lifespan=lifespan)


@app.post("/webhook")
async def webhook(request: Request) -> None:
    raw_update = await request.json()
    update = Update(**raw_update)

    await dp.feed_update(bot, update)
