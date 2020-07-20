"""
This is a echo bot.
It echoes any incoming text messages.
"""
import re
import logging

from aiogram import Bot, Dispatcher, executor, types

from main import main 
from config import tgToken



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=tgToken)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def tg_reciver(message: types.Message):
    # print(message)
    event = 'start'
    task = {
        'message_id':message['message_id'],
        'channel': 'telegram',
        'chat_id': message['from']['id'],
        'event': event,
        'message': {
            'type': 'text',
            'text': message['text']
        },
        'user': message['from']
    }
    await main(task)

@dp.message_handler(regexp='^\/start\s\w+')
async def tg_reciver(message: types.Message):
    event = 'context'
    task = {
        'message_id':message['message_id'],
        'channel': 'telegram',
        'chat_id': message['from']['id'],
        'event': event,
        'message': {
            'type': 'text',
            'text': message['text']
        }
    }
    main(task)

@dp.message_handler(regexp='^\/\w+')
async def tg_reciver(message: types.Message):
    event = 'comand'
    task = {
        'message_id':message['message_id'],
        'channel': 'telegram',
        'chat_id': message['from']['id'],
        'event': event,
        'message': {
            'type': 'text',
            'text': message['text']
        }
    }
    main(task)


@dp.message_handler()
async def tg_reciver(message: types.Message):
    event = 'text'
    task = {
        'message_id':message['message_id'],
        'channel': 'telegram',
        'chat_id': message['from']['id'],
        'event': event,
        'message': {
            'type': 'text',
            'text': message['text']
        }
    }
    main(task)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)