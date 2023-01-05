import re
from aiogram.types import Message
from init_bot import bot
from settings import settings


def check_subscribe(func):
    """Checking user subscribing on the group or channel"""
    async def wrapper(message: Message):
        user_full_name = message.from_user.full_name
        user_id = message.from_user.id
        status = await bot.get_chat_member(chat_id=settings.CHANNEL_ID, user_id=user_id)
        if status.status != 'left':
            await func(message)
        else:
            text = f"Привет, {user_full_name or ''}." \
                   f"\nВы не подписаны на группу {settings.CHANNEL_LINK}." \
                   f"\nЧтобы пользоваться ботом подпишитесь!!!"
            await message.answer(text=text)
    return wrapper


def delete_user_message(func):
    """Delete message from user"""
    async def wrapper(message: Message):
        await func(message)
        await message.delete()
    return wrapper


def get_all_bot_commands() -> str:
    """Return all the bot commands"""
    path_to_file = "handlers/handler_commands.py"
    with open(path_to_file, 'r', encoding='utf-8') as file:
        text = file.read()
        list_commands = re.findall(r"""commands=\['([\D]*?)'\]""", text)
    return ''.join("\n/" + command for command in list_commands)
