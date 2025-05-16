from datetime import datetime

from bson.objectid import ObjectId

from util.connection import get_connection
from extra.dataset import post, grades, books, podcasts

from unit6.crud import create, read, update, delete
from unit7.crud import insert, find
from unit8.crud import replace, insert8, update8, find8
from unit9.crud import unit9
from unit10.crud import unit10
from unit11.crud import unit11

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

    database = client["sample_training"]
    collection = database["routes"]

    # AND operator
    explicit_and_query = {
        "$and": [{"airline.name": "Southwest Airlines"}, {"stops": {"$gte": 1}}]
    }
    implicit_and_query = {"airline.name": "Southwest Airlines", "stops": {"$gte": 1}}
    find(collection, implicit_and_query)

    # OR operator
    find(collection, {"$or": [{"dst_airport": "SEA"}, {"src_airport": "SEA"}]})

    # Nested logical
    find(
        collection,
        {
            "$and": [
                {"$or": [{"dst_airport": "SEA"}, {"src_airport": "SEA"}]},
                {"$or": [{"airline.name": "American Airlines"}, {"airplane": 320}]},
            ]
        },
    )


def unit8_crud():
    database = client["training"]
    collection = database["books"]

    result = collection.find_one({"_id": ObjectId("681df7ae0655443d693d1785")})

    if not result:
        data = {
            "_id": ObjectId("681df7ae0655443d693d1785"),
            "title": "Deep Dive Into React Hooks",
            "ISBN": "00000000",
            "thumbnailUrl": "",
            "publicationDate": datetime(2019, 1, 1),
            "authors": ["Ada Lovelace"],
        }

        insert8(collection, data)

    filter = {"_id": ObjectId("681df7ae0655443d693d1785")}
    data = {
        "title": "Deep Dive into React Hooks",
        "ISBN": "0-3182-1299-4",
        "thumbnailUrl": "http://via.placeholder.com/640x360",
        "publicationDate": datetime(2022, 7, 28),
        "authors": ["Ada Lovelace"],
    }

    replace(collection, filter, data)

    database = client["audio"]
    collection = database["podcasts"]

    result = collection.find_one({"_id": ObjectId("681dfe8cfaa229a6dc62f37c")})

    if not result:
        data = {
            "_id": ObjectId("681dfe8cfaa229a6dc62f37c"),
            "title": "The MongoDB Podcast",
            "year": "2022",
            "premium_subs": "",
            "downloads": 2,
            "podcasts_type": "audio",
        }

        insert8(collection, data)

    filter = {"_id": ObjectId("681dfe8cfaa229a6dc62f37c")}
    update8(collection, filter, {"$set": {"subscribers": 98562}}, upsert=False)
    update8(
        collection,
        {"title": "The Developer Hub"},
        {"$set": {"topics": ["databases", "MongoDB"]}},
        upsert=True,
    )
    update8(
        collection,
        {"title": "The MongoDB Podcast"},
        {"$push": {"hosts": "Nic Raboy"}},
        upsert=False,
    )

    print(
        collection.find_one_and_update(
            {"_id": ObjectId("681dfe8cfaa229a6dc62f37c")},
            {"$inc": {"downloads": 1}},
        )
    )

    database = client["training"]
    collection = database["books"]

    result = find8(collection, {"title": "MongoDB in Action"})
    if not result:
        result = collection.insert_many(books)

    # # Test to check if documents are inserted correctly
    # result = collection.find({"publishedDate": {"$lt": datetime(2019, 1, 1)}})
    # try:
    #     r = [x for x in result]
    #     pprint.pp(r)
    # except Exception as e:
    #     print(e)

    # result = collection.update_many(
    #     {"publishedDate": {"$lt": datetime(2019, 1, 1)}}, {"$set": {"status": "LEGACY"}}
    # )

    database = client["audio"]
    collection = database["podcasts"]

    # collection.insert_many(podcasts)

    result = collection.delete_one({"_id": ObjectId("68237ae23934ecd422a6dddd")})
    print(result)

    result = collection.delete_many({"category": "crime"})
    print(result)

# unit6_crud()
# unit7_crud()
# unit8_crud()
# unit9(client)
# unit10(client)
unit11(client)