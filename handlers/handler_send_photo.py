from settings import settings
from logic_server.middleware import check_sub_channel
from aiogram import types
from init_bot import bot, dispatcher


@dispatcher.message_handler(content_types=['photo'])
async def send_photo_to_group(message: types.Message):
    user_id = message.from_user.id
    if check_sub_channel(await bot.get_chat_member(chat_id=settings.CHANNEL_ID, user_id=user_id)):
        image_id = message.photo[-1].file_id
        await bot.send_photo(chat_id=settings.CHANNEL_ID, photo=image_id)
    else:
        text = settings.ANSWER_NOT_SUB
        await message.answer(text=text)
        await message.delete()
