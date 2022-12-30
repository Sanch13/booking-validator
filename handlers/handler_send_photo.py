from settings import settings
from logic_server.middleware import check_subscribe, message_del
from aiogram.types import Message
from init_bot import dispatcher, bot


@dispatcher.message_handler(content_types=['photo'])
@message_del
@check_subscribe
async def send_photo_to_group(message: Message) -> None:
    image_id = message.photo[-1].file_id
    await bot.send_photo(chat_id=settings.CHANNEL_ID, photo=image_id)
