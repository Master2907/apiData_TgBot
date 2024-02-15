import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

import core.local_setting as st
from core.handlers import getMovie
from core.callback import getVideo

async def greeting(message: Message, bot: Bot):
    await message.answer("Welcome")

async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=st.TOKEN)
    dp = Dispatcher()

    dp.message.register(greeting, CommandStart())
    dp.message.register(getMovie)
    dp.callback_query.register(getVideo)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())