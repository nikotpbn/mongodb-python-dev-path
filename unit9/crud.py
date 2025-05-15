import pprint


def print_result(cursor):
    result = [i for i in cursor]
    pprint.pp(result)

    return result


def unit9(client):
    db = client["sample_training"]

    """
    List all companies with music category in alphabetical order
    Capital letters are sorted first followed by lower case letters.
    It's possible to change this behavious by using the options param in sort method.
    """
    cursor = db.companies.find({"category_code": "music"}, {"name": 1}).sort(
        {"name": 1}
    )
    print_result(cursor)

    """
    List the top three  music companies that have the most number of employees
    In this case to also project the results
    """
    print("top three  music companies that have the most number of employees")
    cursor = (
        db.companies.find(
            {"category_code": "music"}, {"_id": 0, "name": 1, "number_of_employees": 1}
        )
        .sort({"number_of_employees": -1})
        .limit(3)
    )
    print_result(cursor)

    """
    Projection Examples: Including Fields
    """
    print("#### Projection ####")
    db = client["sample_training"]
    cursor = db.inspections.find(
        {"sector": "Restaurant - 818"}, {"_id": 0, "business_name": 1, "result": 1}
    )
    print_result(cursor)

    """
    Projection Examples: Excluding Fields
    """
    print("#### Projection Exclude ####")
    cursor = db.inspections.find(
        {"result": {"$in": ["Pass", "Warning"]}},
        {"_id": 0, "address.zip": 0, "date": 0},
    )
    print_result(cursor)
