from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
user = os.environ.get('MONGO_USER')
password = os.environ.get('MONGO_PASSWORD')

uri = f"mongodb+srv://{user}:{password}@cluster0.yvbp59j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
def get_connection():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        return client

    except Exception as e:
        print(e)