from pymongo import MongoClient
import certifi

from credentials import user, password

uri = f"mongodb+srv://{user}:{password}@cluster0.yvbp59j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)