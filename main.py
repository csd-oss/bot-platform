from sendMessage import send_message
from userProfile import save_user


async def question(task, bot):
    task['text'] = 'Привет, как тебя зовут?'
    await send_message(task, bot)


async def test(task, bot):
    task['text'] = 'Test удачи'
    await send_message(task, bot)


async def main(task, bot):
    # print(task)
    if task['event'] == 'start':
        user = task['user']
        await save_user(user)
        task['text'] = 'Privet, напиши что-то'
        await send_message(task, bot)
