from sendMessage import send_message
from time import sleep

def save_user(user):
    """
    TO-DO:
    * Save users to db
    """
    return user

async def question(task, bot):
    task['text'] = 'Привет, как тебя зовут?'
    await send_message(task, bot)


async def test(task, bot):
    task['text'] = 'Test удачи'
    await send_message(task, bot)

async def main(task, bot):
    print(task)
    if task['event'] == 'start':
        # await save_user(task['user'])
        task['text'] = 'Privet, напиши что-то'
        await send_message(task, bot)
    # elif task['event'] == 'command':
    #     func = task['message']['text'][1:]
    #     print(func)
    #     task['message']['text'][1:](task, bot)
    # DOESEN'T work
    else: 
        if task['message']['text'] == 'хуй':
            task['text'] = 'Сук, у тебя хуй'
            await send_message(task, bot)
            sleep(3)
            await  question(task, bot)
        else: 
            await  question(task, bot)
