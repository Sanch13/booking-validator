from settings import config
from logic_server.middleware import check_sub_channel
from init_bot import bot
from aiogram import types, Dispatcher


async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    if check_sub_channel(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)):
        text = f"Привет, {user_full_name or ''}.\nВы нажали на кнопку /start\n"
        await message.answer(text=text)
        await message.delete()
    else:
        text = config.ANSWER_NOT_SUB
        await message.answer(text=text)
        await message.delete()


async def help_handler(message: types.Message):
    user_full_name = message.from_user.full_name
    text = f"Привет, {user_full_name or ''}.\n" \
           f"Этот бот предназначен для отправки изображений в группу {config.CHANNEL_LINK}. \n" \
           f"Подпишись на группу и отправляй изображения!"
    await message.answer(text=text)
    await message.delete()


def register_handler_commands(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start_handler, commands=config.COMMANDS['START'])
    dispatcher.register_message_handler(help_handler, commands=config.COMMANDS['HELP'])
