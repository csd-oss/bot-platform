"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from config import tgToken

API_TOKEN = tgToken

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends anything to bot
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)