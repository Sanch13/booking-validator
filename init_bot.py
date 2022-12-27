from aiogram import Dispatcher, Bot
from settings import config


bot = Bot(token=config.API_TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot)
