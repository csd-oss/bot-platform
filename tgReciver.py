"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import re

from aiogram import Bot, Dispatcher, executor, types

from config import tgToken

API_TOKEN = tgToken

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def main(task):
    if task['event'] == 'start':
        print('Start')
    else:
        print('poshel nahui')

@dp.message_handler()
async def tg_reciver(message: types.Message):
    if  message['text'] == '/start':
        event = 'start'
    elif bool(re.search('^\/start\s\w+', message['text'])):
        event = 'context'
    elif bool(re.search('^\/\w+', message['text'])): 
         event = 'comand'
    else:
        event = 'text'
    task = {
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