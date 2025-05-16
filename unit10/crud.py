import pprint
from bson.objectid import ObjectId

from .data.dataset import new_document, new_account, new_accounts

def metadata(cursor):
    result = [i for i in cursor]
    return { "num_docs": len(result), "data": result}


def unit10(client):

    db = client.bank
    accounts_collection = db.accounts

    # result = accounts_collection.insert_one(new_account)

    # document_id = result.inserted_id
    # print(f"_id of inserted document {document_id}")

    # result = accounts_collection.insert_many(new_accounts)
    # document_ids = result.inserted_ids
    # print("# of documents inserted: " + str(len(document_ids)))
    # print(f"_ids of inserted documents: {document_ids}")

    result = accounts_collection.find_one({"_id": ObjectId("6825f06998552c2e961fb3aa")})
    pprint.pp(result)

    cursor = accounts_collection.find({"balance": {"$gt": 4700}})
    pprint.pp(metadata(cursor))
