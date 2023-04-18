from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from handlers import start, attendance
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(start, commands=['start'])
dp.register_message_handler(attendance, commands=['attendance'])

if __name__ == '__main__':
    executor.start_polling(dp)

