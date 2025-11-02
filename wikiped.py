from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import wikipedia
from dotenv import load_dotenv

import asyncio
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

db = Dispatcher()

@db.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Assalomu alaykum {message.from_user.first_name}! Wikipedia ga xush kelibsiz.")


@db.message()
async def how(message: Message):
    try:
        wikipedia.set_lang("uz")
        data = wikipedia.summary(message.text)
        await message.answer(data)
    except:
        await message.answer(f"""Siz izlagan malumot topilmadi""")


async def new():
    print("bot ishda")
    bot = Bot(TOKEN)
    await db.start_polling(bot)


asyncio.run(new())
