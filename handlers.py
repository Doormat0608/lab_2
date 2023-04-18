from aiogram.types import Message

async def start(message: Message):
    await message.answer("Добро пожаловать в чат-бот для родителей! Вы можете проверить успеваемость вашего ребенка, используя следующую команду:\n\n"
                          "/attendance - Посмотреть запись о посещаемости вашего ребенка\n")

async def attendance(message: Message):
    await message.answer("Ваш ребенок посещал школу в следующие дни:\n\n"
                          "Вторник, 10 марта\n"
                          "Среда, 11 марта\n"
                          "Вторник, 17 марта\n"
                          "Вторник, 4 апреля\n"
                          "Пятница, 7 апреля\n"
                          "Понедельник, 10 апреля\n"
                          "Среда, 12 апреля\n")
