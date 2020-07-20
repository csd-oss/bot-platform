
def save_user(user):
    """
    TO-DO:
    * Save users to db
    """
    return user


async def main(task):
    if task['event'] == 'start':
        save_user(task['user'])
        await bot.send_message(task.chat_id, 'Privet')
    else:
        print('poshel nahui')
