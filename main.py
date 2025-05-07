from util.connection import get_connection
from extra.dataset import post, grades

from unit6.crud import create, read, update, delete
from unit7.crud import insert

client = get_connection()


def unit6_crud():
    database = client["blog"]
    # collection = database["posts"]

    print(create(database, post))
    print(read(database, {"title": "Coffee"}))
    print(update(database, {'title': 'Coffee'}))
    print(delete(database, {'title': "A cup of Coffee"}))

def unit7_crud():
    database = client["training"]

    # insert(database, grades[0])
    insert(database, grades, many=True)

# unit6_crud()
unit7_crud()