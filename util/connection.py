from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
def get_connection():
    try:
        client.admin.command('ping')
        # print("Pinged your deployment. You successfully connected to MongoDB!")

        return client

    except Exception as e:
        print(e)

def close_connection():
    client.close()