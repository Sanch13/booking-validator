from aiogram import executor
from init_bot import dispatcher
import handlers


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
