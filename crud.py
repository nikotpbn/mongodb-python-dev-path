from connection import get_connection

client = get_connection()
database = client["blog"]
collection = database["posts"]

post = {
            'title': "Coffee",
            'content': "Darkly colored, bitter, and slightly acidic, coffee has a stimulating effect on humans"
        }

def create(payload):
    try:
        result = read({'title': payload['title']})
        if result:
            return "A post with this title already exists"

        result = collection.insert_one(payload)
        return "Post successfully created."

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def read(filter=None):
    try:
        result = collection.find_one(filter)
        # print(result.acknowledged)
        return result

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def update(filter):
    try:
        update_operation = { "$set" :
            { "title" : "A cup of Coffee",
             "url": "https://media.istockphoto.com/id/1152767411/pt/foto/cup-of-coffee-latte-isolated-on-white-background-with-clipping-path.jpg?s=1024x1024&w=is&k=20&c=qOJvxun-Uth21sKX1U7cgbZI6E440V19rZsimeFwKtw=" }
        }
        result = collection.update_one(filter, update_operation)

        return read({"title": "A cup of Coffee"})

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def delete(filter):
    try:
        result = collection.delete_one(filter)

        return "Post sucessfully deleted."

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

print(create(post))
print(read({'title': 'Coffee'}))
print(update({'title': 'Coffee'}))
print(delete({'title': "A cup of Coffee"}))