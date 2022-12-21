from settings import config
from logic_server.middleware import check_sub_channel
from aiogram import Bot, Dispatcher, types


bot = Bot(token=config.API_TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot)


@dispatcher.message_handler(commands=config.COMMANDS['START'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    if check_sub_channel(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)):
        text = f"Hello, {user_full_name or ''}.\nYou pushed the start button\n"
        await message.answer(text=text)
    else:
        text = f"Вы не подписаны на группу {config.CHANNEL_LINK}. Подпишитесь!!!"
        await message.answer(text=text)


@dispatcher.message_handler(commands=config.COMMANDS['HELP'])
async def help_handler(message: types.Message):
    user_full_name = message.from_user.full_name
    text = f'Hi, {user_full_name}.\nYou pushed the help button'
    await message.answer(text=text)
