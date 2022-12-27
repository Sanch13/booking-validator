from aiogram import executor
from init_bot import dispatcher
from handlers import handler_just_text, handler_send_photo, handler_commands


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
