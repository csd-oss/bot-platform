async def send_message(task, bot):
    if task['channel'] == 'telegram':
        await bot.send_message(task['chat_id'], task['text'])
