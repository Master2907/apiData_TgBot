import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import core.local_setting as st
from core.handlers import getMovie
from core.callback import getVideo

async def startup(bot: Bot):
    await bot.send_message(5811454533, 'Started')

async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=st.TOKEN)
    dp = Dispatcher()

    dp.startup.register(startup)
    dp.message.register(getMovie    )
    dp.callback_query.register(getVideo)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())