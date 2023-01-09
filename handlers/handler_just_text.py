from logic_server.middleware import check_subscribe, delete_user_message, get_all_bot_commands
from aiogram.types import Message
from init_bot import dispatcher


@dispatcher.message_handler()
@delete_user_message
@check_subscribe
async def reply_just_text(message: Message) -> None:
    text = f"Вы можете отправлять только изображения и команды :" \
           f"{get_all_bot_commands()}"
    await message.answer(text=text)
