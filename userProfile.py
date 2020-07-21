from tinydb import TinyDB

db = TinyDB('data/db.json')


async def save_user(user):
    User = db.table('user')
    User.insert(user)
