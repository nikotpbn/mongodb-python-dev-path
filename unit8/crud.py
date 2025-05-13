def find8(collection, filter):
    try:
            cursor = collection.find(filter)
            result = []
            for item in cursor:
                result.append(item)
            return result

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)



def insert8(collection, data):
    try:
            result = collection.insert_one(data)
            return "sucessfully inserted"
    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def replace(collection, filter, data, many=False):
    try:
        if many:
            result = collection.replace_many(filter, data)
            return "grades list sucessfully inserted"
        else:
            result = collection.replace_one(filter, data)
            return "data sucessfully updated"


    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def update8(collection, filter, data, upsert):
    try:
        result = collection.update_one(filter, data, upsert)
        return "data sucessfully updated"


    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)