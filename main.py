from util.connection import get_connection
from extra.dataset import post

from unit6.crud import create, read, update, delete

client = get_connection()


def unit6_crud():
    database = client["blog"]
    # collection = database["posts"]

    print(create(database, post))
    print(read(database, {"title": "Coffee"}))
    print(update(database, {'title': 'Coffee'}))
    print(delete(database, {'title': "A cup of Coffee"}))


unit6_crud()
