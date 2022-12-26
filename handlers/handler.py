from settings import config
from logic_server.middleware import check_sub_channel, get_all_bot_commands
from aiogram import Dispatcher, Bot, types


bot = Bot(token=config.API_TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot=bot)


@dispatcher.message_handler(commands=config.COMMANDS['START'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    if check_sub_channel(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)):
        text = f"Hello, {user_full_name or ''}.\nYou pushed the start button\n"
        await message.answer(text=text)
        await message.delete()
    else:
        text = config.ANSWER_NOT_SUB
        await message.answer(text=text)
        await message.delete()


@dispatcher.message_handler(commands=config.COMMANDS['HELP'])
async def help_handler(message: types.Message):
    user_full_name = message.from_user.full_name
    text = f"Привет, {user_full_name or ''}.\n" \
           f"Этот бот предназначен для отправки изображений в группу {config.CHANNEL_LINK}. \n" \
           f"Подпишись на группу и отправляй изображения!"
    await message.answer(text=text)
    await message.delete()


@dispatcher.message_handler(content_types=['photo'])
async def send_photo_to_group(message: types.Message):
    user_id = message.from_user.id
    if check_sub_channel(await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)):
        image_id = message.photo[-1].file_id
        await bot.send_photo(chat_id=config.CHANNEL_ID, photo=image_id)
    else:
        text = config.ANSWER_NOT_SUB
        await message.answer(text=text)
        await message.delete()


@dispatcher.message_handler()
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
