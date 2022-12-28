from aiogram import Dispatcher, Bot
from settings import settings


bot = Bot(token=settings.API_TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot)
