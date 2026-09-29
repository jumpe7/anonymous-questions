import asyncio
from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("ПОКА НЕ РАБОТАЕТ!!!!!!!!!!!!!!!!!!!")

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print("DOT STARTING")
    asyncio.run(main())