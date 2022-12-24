from aiogram import executor
from handlers.handler import dispatcher

if __name__ == '__main__':
    executor.start_polling(dispatcher)
