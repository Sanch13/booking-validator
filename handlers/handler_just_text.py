from settings import config
from logic_server.middleware import check_sub_channel, get_all_bot_commands
from aiogram import types, Dispatcher
from init_bot import bot


async def reply_just_text(message: types.Message):
    user_id = message.from_user.id
    if check_sub_channel(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)):
        text = f"Вы можете отправлять только изображения и команды :" \
               + get_all_bot_commands(commands=config.COMMANDS)
        await message.answer(text=text)
    else:
        text = config.ANSWER_NOT_SUB
        await message.answer(text=text)
        await message.delete()


def register_handler_just_text(dispatcher: Dispatcher):
    dispatcher.register_message_handler(reply_just_text)
