from bson.objectid import ObjectId


from util.connection import get_connection
from extra.dataset import post, grades

from unit6.crud import create, read, update, delete
from unit7.crud import insert, find

client = get_connection()


def unit6_crud():
    database = client["blog"]
    # collection = database["posts"]

    print(create(database, post))
    print(read(database, {"title": "Coffee"}))
    print(update(database, {"title": "Coffee"}))
    print(delete(database, {"title": "A cup of Coffee"}))


def unit7_crud():
    database = client["training"]
    insert(database, grades[0])
    insert(database, grades, many=True)

    database = client["sample_training"]
    collection = database["zips"]
    find(collection, {"_id": ObjectId("5c8eccc1caa187d17ca6ed16")})
    find(collection, {"city": {"$in": ["PHOENIX", "CHICAGO"]}})

    database = client["sample_supplies"]
    collection = database["sales"]
    find(collection, {"items.price": {"$gt": 50}})
    find(collection, {"items.price": {"$lt": 50}})
    find(collection, {"customer.age": {"$lte": 65}})
    find(collection, {"customer.age": {"$gte": 65}})

    database = client["sample_analytics"]
    collection = database["accounts"]
    find(collection, {"products": "InvestmentStock"})
    find(collection, {"products": {"$elemMatch": {"$eq": "InvestmentStock"}}})

    database = client["sample_supplies"]
    collection = database["sales"]
    find(
        collection,
        {
            "items": {
                "$elemMatch": {
                    "name": "laptop",
                    "price": {"$gt": 800},
                    "quantity": {"$gt": 1},
                }
            }
        },
    )


# unit6_crud()
unit7_crud()
