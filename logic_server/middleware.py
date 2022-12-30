from aiogram.types import Message
from init_bot import bot
from settings import settings


def check_subscribe(func):

    async def wrapper(message: Message, *args, **kwargs):
        user_full_name = message.from_user.full_name
        user_id = message.from_user.id
        status = await bot.get_chat_member(chat_id=settings.CHANNEL_ID, user_id=user_id)
        print(status.status)
        if status.status != 'left':
            await func(message)
        else:
            text = f"Привет, {user_full_name or ''}." \
                   f"\nВы не подписаны на группу {settings.CHANNEL_LINK}." \
                   f"\nЧтобы пользоваться ботом подпишитесь!!!"
            await message.answer(text=text)
    return wrapper


def message_del(func):

    async def wrapper(message: Message):
        await func(message)
        await message.delete()
    return wrapper
