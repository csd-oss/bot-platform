from sendMessage import send_message

def save_user(user):
    """
    TO-DO:
    * Save users to db
    """
    return user


async def main(task, bot):
    if task['event'] == 'start':
        # await save_user(task['user'])
        task['text'] = 'Privet'
        await send_message(task, bot)
    else:
        print('poshel nahui')
