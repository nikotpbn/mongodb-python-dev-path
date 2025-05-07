from extra.dataset import grades

def insert(data, many=False):
    try:
        if many:
            print(data)
            # result = collection.insert_one(data)
            # return result
        else:
            print(data)
            # result = collection.insert_many(data)
            # return result.inserted_ids


    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

insert(grades[0])
insert(grades, many=True)