from aiogram import executor
from init_bot import dispatcher
from handlers import handler_just_text, handler_send_photo, handler_commands


handler_commands.register_handler_commands(dispatcher)
handler_send_photo.register_handler_send_photo(dispatcher)
handler_just_text.register_handler_just_text(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
