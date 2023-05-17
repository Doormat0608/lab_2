import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from functions import welcome, help, get_student_grades
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(welcome, commands=['start'])
dp.register_message_handler(help, commands=['help'])
dp.register_message_handler(get_student_grades)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
