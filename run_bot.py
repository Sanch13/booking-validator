from handlers.handler import dispatcher

from aiogram import executor


if __name__ == '__main__':
    executor.start_polling(dispatcher)
