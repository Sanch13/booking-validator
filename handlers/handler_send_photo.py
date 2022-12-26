from settings import config
from logic_server.middleware import check_sub_channel
from aiogram import types, Dispatcher
from init_bot import bot


async def send_photo_to_group(message: types.Message):
    user_id = message.from_user.id
    if check_sub_channel(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)):
        image_id = message.photo[-1].file_id
        await bot.send_photo(chat_id=config.CHANNEL_ID, photo=image_id)
    else:
        text = config.ANSWER_NOT_SUB
        await message.answer(text=text)
        await message.delete()


def register_handler_send_photo(dispatcher: Dispatcher):
    dispatcher.register_message_handler(send_photo_to_group, content_types=['photo'])
