def create(database, data):
    try:
        result = read(database, {'title': data['title']})
        if result:
            return "A post with this title already exists"

        result = database.posts.insert_one(data)
        return "Post successfully created."

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def read(database, filter=None):
    try:
        result = database.posts.find_one(filter)
        # print(result.acknowledged)
        return result

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def update(database, filter):
    try:
        update_operation = { "$set" :
            { "title" : "A cup of Coffee",
             "url": "https://media.istockphoto.com/id/1152767411/pt/foto/cup-of-coffee-latte-isolated-on-white-background-with-clipping-path.jpg?s=1024x1024&w=is&k=20&c=qOJvxun-Uth21sKX1U7cgbZI6E440V19rZsimeFwKtw=" }
        }
        result = database.posts.update_one(filter, update_operation)

        return read(database, {"title": "A cup of Coffee"})

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def delete(database, filter):
    try:
        result = database.posts.delete_one(filter)

        return "Post sucessfully deleted."

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)