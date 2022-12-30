from logic_server.middleware import check_subscribe, message_del
from aiogram.types import Message
from init_bot import dispatcher


@dispatcher.message_handler()
@message_del
@check_subscribe
async def reply_just_text(message: Message) -> None:
    text = f"Вы можете отправлять только изображения и команды :"
    # + get_all_bot_commands(commands=settings.COMMANDS)
    await message.answer(text=text)
