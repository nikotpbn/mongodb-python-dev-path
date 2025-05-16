import pprint
from bson.objectid import ObjectId

from .data.dataset import new_document, new_account, new_accounts


def metadata(cursor):
    result = [i for i in cursor]
    return {"num_docs": len(result), "data": result}


def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=None,
):
    accounts_collection = session.client.bank.accounts
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    # Update sender
    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfer_complete": transfer_id},
        },
        session=session,
    )

    # Update receiver
    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfer_complete": transfer_id},
        },
        session=session,
    )

    transfers_collection.insert_one(transfer, session=session)

    print("Transaction successfull")

    return


def unit10(client):

    db = client.bank
    accounts_collection = db.accounts

    result = accounts_collection.insert_one(new_account)

    document_id = result.inserted_id
    print(f"_id of inserted document {document_id}")

    result = accounts_collection.insert_many(new_accounts)
    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

    result = accounts_collection.find_one({"_id": ObjectId("6825f06998552c2e961fb3aa")})
    pprint.pp(result)

    result = accounts_collection.find({"balance": {"$gt": 4700}})
    pprint.pp(metadata(result))

    result = accounts_collection.update_one(
        {"_id": ObjectId("6826fd694315a5a3d5e42814")}, {"$inc": {"balance": 100}}
    )
    print("Documents updated: " + str(result.modified_count))
    pprint.pp(result)

    result = accounts_collection.update_many(
        {"account_type": "savings"}, {"$set": {"minimum_balance": 100}}
    )
    print("Documents matched: " + str(result.matched_count))
    print("Documents modified: " + str(result.modified_count))
    pprint.pp(accounts_collection.find_one({"account_type": "savings"}))

    print("Searching for target document before delete:")
    pprint.pp(
        accounts_collection.find_one({"_id": ObjectId("6825f06998552c2e961fb3aa")})
    )
    result = accounts_collection.delete_one(
        {"_id": ObjectId("6825f06998552c2e961fb3aa")}
    )
    print("Searching for target document after delete:")
    pprint.pp(
        accounts_collection.find_one({"_id": ObjectId("6825f06998552c2e961fb3aa")})
    )
    print("documents deleted: " + str(result.deleted_count))

    print("Searching for target document before delete:")
    pprint.pp(accounts_collection.find_one({"balance": {"$lt": 2000}}))
    result = accounts_collection.delete_many({"balance": {"$lt": 2000}})
    print("Searching for target document after delete:")
    pprint.pp(accounts_collection.find_one({"balance": {"$lt": 2000}}))
    print("documents deleted: " + str(result.deleted_count))

    with client.start_session() as session:
        session.with_transaction(
            lambda session: callback(
                session,
                transfer_id="TR218721873",
                account_id_receiver="MDB343652528",
                account_id_sender="MDB574189300",
                transfer_amount=100,
            )
        )
