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
async def start_reciver(message: types.Message):
    # print(message)
    event = 'start'
    task = {
        'message_id': message['message_id'],
        'channel': 'telegram',
        'chat_id': message['from']['id'],
        'event': event,
        'message': {
            'type': 'text',
            'text': message['text']
        },
        'user': {
            'channel': 'telegram',
            'chat_id': message['from']['id'],
            'first_name': message['from']['first_name'],
            'username': message['from']['username']
        }
    }
    await main(task, bot)


@dp.message_handler(regexp=r'^\/start\s\w+')
async def start_with_contex_reciver(message: types.Message):
    event = 'context'
    task = {
        'message_id': message['message_id'],
        'channel': 'telegram',
        'chat_id': message['from']['id'],
        'event': event,
        'message': {
            'type': 'text',
            'text': message['text']
        }
    }
    await main(task, bot)


@dp.message_handler(regexp=r'^\/\w+')
async def command_reciver(message: types.Message):
    event = 'command'
    task = {
        'message_id': message['message_id'],
        'channel': 'telegram',
        'chat_id': message['from']['id'],
        'event': event,
        'message': {
            'type': 'text',
            'text': message['text']
        }
    }
    await main(task, bot)


@dp.message_handler()
async def tg_reciver(message: types.Message):
    event = 'text'
    task = {
        'message_id': message['message_id'],
        'channel': 'telegram',
        'chat_id': message['from']['id'],
        'event': event,
        'message': {
            'type': 'text',
            'text': message['text']
        }
    }
    await main(task, bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
