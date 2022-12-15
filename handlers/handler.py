from settings import config

from aiogram import Bot, Dispatcher, types


bot = Bot(token=config.API_TELEGRAM_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=config.COMMANDS['START'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id                  # for logging in the future
    user_name = message.from_user.first_name        # for logging in the future
    user_full_name = message.from_user.full_name
    await message.answer(text=f"Hello, {user_full_name}.\nYou pushed the start button")


@dp.message_handler(commands=config.COMMANDS['HELP'])
async def help_handler(message: types.Message):
    user_full_name = message.from_user.full_name
    await message.answer(text=f'Hi, {user_full_name}.\nYou pushed the help button')
