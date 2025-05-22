from pymongoexplain import ExplainableCollection

import datetime
import pprint


def unit13(client):
    db = client.sample_analytics

    customers_collection = db.customers

    # filter = { "birthdate": { "$lt": datetime.datetime(1966,8,2) } }

    # sort = {
    #     "birthdate": 1
    # }

    # result = customers_collection.find(filter).sort(sort)
    # x = [i for i in result]
    # pprint.pp(x)

    result = customers_collection.create_index({"birthdate": 1})
    # print(result)

    """
    There is a duplicate on the sample database, so this does not work.
    Need change one of the documents first.
    """
    result = customers_collection.create_index({"email": 1}, unique=True)
    print(result)

    result = customers_collection.list_indexes()
    pprint.pp([x for x in result])

    # https://pypi.org/project/pymongoexplain/
    # result = ExplainableCollection(customers_collection).find(
    #     {"birthdate": {"$gt": datetime.datetime(1995, 8, 1)}}
    # )
    # pprint.pp(result)

    # result = (
    #     ExplainableCollection(customers_collection)
    #     .find({"birthdate": {"$gt": datetime.datetime(1995, 8, 1)}}, sort=[("email", 1)])
    # )
    # pprint.pp(result)

    result = ExplainableCollection(customers_collection).find({ "accounts": "871666" })
    pprint.pp(result)