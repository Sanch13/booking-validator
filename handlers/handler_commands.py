from settings import settings
from logic_server.middleware import check_subscribe, message_del
from init_bot import dispatcher
from aiogram.types import Message


@dispatcher.message_handler(commands=['start'])
@message_del
@check_subscribe
async def start_handler(message: Message) -> None:
    user_full_name = message.from_user.full_name
    text = f"Привет, {user_full_name or ''}.\nВы нажали на кнопку /start\n"
    await message.answer(text=text)


@dispatcher.message_handler(commands=['help'])
@message_del
async def help_handler(message: Message) -> None:
    user_full_name = message.from_user.full_name
    text = f"Привет, {user_full_name or ''}.\n" \
           f"Этот бот предназначен для отправки изображений в группу {settings.CHANNEL_LINK}. \n" \
           f"Подпишись на группу и отправляй изображения!"
    await message.answer(text=text)
