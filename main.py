from fastapi import FastAPI, Request

from app.bot import bot, dp
from aiogram.types import Update
from app.config.config import settings
from app.ui.start import user_router
from contextlib import asynccontextmanager
import app.utils.callbacks.role


@asynccontextmanager
async def lifespan(app: FastAPI):
    webhook_url = settings.get_webhook_url()
    dp.include_router(user_router)
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
    print(raw_update)
    update = Update(**raw_update)

    await dp.feed_update(bot, update)

