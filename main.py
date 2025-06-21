from os import getenv
from fastapi import FastAPI, Request

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.config.config import settings
from contextlib import asynccontextmanager

TOKEN = getenv("TOKEN")

dp = Dispatcher()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@asynccontextmanager
async def lifespan(app: FastAPI):
    webhook_url = settings.get_webhook_url()
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True,
    )
    yield
    await bot.delete_webhook()

app = FastAPI(lifespan=lifespan)

@app.post("/webhook")
async def webhook(request: Request) -> None:
    update = await request.json()

    await dp.feed_update(bot, update)

async def start_bot():
    try:
        await bot.send_message(settings.ADMIN_ID, f'Я запущен🥳.')
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(settings.ADMIN_ID, 'Бот остановлен. За что?😔')
    except:
        pass