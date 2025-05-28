from pymongoexplain import ExplainableCollection

import datetime
import pprint


def unit13(client):
    db = client.sample_analytics

    customers_collection = db.customers

    filter = {"birthdate": {"$lt": datetime.datetime(1966, 8, 2)}}

    sort = {"birthdate": 1}

    result = customers_collection.find(filter).sort(sort)
    # pprint.pp([i for i in result])

    result = customers_collection.create_index({"birthdate": 1})
    # print(result)

    """
    There is a duplicate on the sample database, so this does not work.
    Need change one of the documents first.
    """
    result = customers_collection.create_index({"email": 1}, unique=True)
    # print(result)

    result = customers_collection.list_indexes()
    # pprint.pp([x for x in result])

    # https://pypi.org/project/pymongoexplain/
    result = ExplainableCollection(customers_collection).find(
        {"birthdate": {"$gt": datetime.datetime(1995, 8, 1)}}
    )
    # pprint.pp(result)

    result = ExplainableCollection(customers_collection).find(
        {"birthdate": {"$gt": datetime.datetime(1995, 8, 1)}}, sort=[("email", 1)]
    )
    # pprint.pp(result)

    """
    Confirm that there no index in the accounts field, since the winning plan will be
    a COLLECTION SCAN
    """
    result = ExplainableCollection(customers_collection).find({"accounts": "871666"})
    # pprint.pp(result)

    result = customers_collection.create_index({"accounts": 1})
    # print(result)

    result = ExplainableCollection(customers_collection).find({"accounts": "871666"})
    # pprint.pp(result)

    """
    Find documents with filter and sorting and then
    confirm index scan on birthdate,
    fetch on active and
    sorting as last input stage
    """
    result = customers_collection.find(
        {"birthdate": {"$gte": datetime.datetime(1977, 1, 1)}, "active": True}
    ).sort({"birthdate": -1, "name": 1})
    # pprint.pp([x for x in result])

    result = ExplainableCollection(customers_collection).find(
        {"birthdate": {"$gte": datetime.datetime(1977, 1, 1)}, "active": True},
        sort=[("birthdate", -1), ("name", 1)],
    )
    # pprint.pp(result)

    """
    Improve performance by creating an index that
    better supports the query above
    """
    result = customers_collection.create_index(
        {"active": 1, "birthdate": -1, "name": 1}
    )
    # print(result)

    result = ExplainableCollection(customers_collection).find(
        {"birthdate": {"$gte": datetime.datetime(1977, 1, 1)}, "active": True},
        sort=[("birthdate", -1), ("name", 1)],
    )
    # pprint.pp(result)

    """
    Add projection to remove the FETCH stage
    """
    # result = customers_collection.find(
    #     {"birthdate": {"$gte": datetime.datetime(1977, 1, 1)}, "active": True},
    #     {"name": 1, "birthdate": 1, "_id": 0},
    # ).sort({"birthdate": -1, "name": 1})
    # pprint.pp([x for x in result])

    result = ExplainableCollection(customers_collection).find(
        {"birthdate": {"$gte": datetime.datetime(1977, 1, 1)}, "active": True},
        projection={"name": 1, "birthdate": 1, "_id": 0},
        sort=[("birthdate", -1), ("name", 1)],
    )
    # pprint.pp(result)