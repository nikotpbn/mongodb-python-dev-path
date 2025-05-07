def insert(database, data, many=False):
    print(data)

    try:
        if many:
            result = database.grades.insert_many(data)
            return "grades list sucessfully inserted"
        else:
            result = database.grades.insert_one(data)
            return "grade sucessfully inserted"


    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)