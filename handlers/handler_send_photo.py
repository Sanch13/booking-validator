from settings import settings
from logic_server.middleware import check_subscribe, delete_user_message
from aiogram.types import Message
from init_bot import dispatcher, bot


@dispatcher.message_handler(content_types=['photo'])
@delete_user_message
@check_subscribe
async def send_photo_to_group(message: Message) -> None:
    image_id = message.photo[-1].file_id
    await bot.send_photo(chat_id=settings.CHANNEL_ID, photo=image_id)
