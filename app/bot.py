import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from app.config.config import settings

load_dotenv()

redis_url = os.getenv("REDIS_URL")

storage = RedisStorage.from_url(redis_url)

bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
i18n = I18n(path="app/locales", default_locale="en", domain="messages")
i18n_midllware = SimpleI18nMiddleware(i18n=i18n)
dp = Dispatcher(storage=storage)
dp.update.middleware(i18n_midllware)
dp.callback_query.middleware(i18n_midllware)