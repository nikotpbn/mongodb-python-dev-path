from bson.objectid import ObjectId

import datetime

new_document = {
    "account_holder": "Addison Shelton",
    "account_id": "MD981234897",
    "account_type": "checking",
    "years_active": "5",
    "address": {
        "city": "Ridgewoord",
        "zip": "11385",
        "street": "Menahan St",
        "number": "1712",
    },
    "transfers_complete": [
        "TR987481928",
        "TR129387402",
        "TR007471992",
    ],
}

new_account = {
    "_id": ObjectId("6825f06998552c2e961fb3aa"),
    "account_holder": "Linus Trovalds",
    "account_id": "MD009122931",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.now(),
}

new_accounts = [
    {
        "_id": ObjectId("6825f1d49383506c57f8fddd"),
        "account_holder": "Ada Lovelace",
        "account_id": "MD898772658'",
        "account_type": "checking",
        "balance": 60218,
        "last_updated": datetime.datetime.now(),
    },
    {
        "_id": ObjectId("6825f1d49383506c57f8fdde"),
        "account_holder": "Muhammad ibn Musa al-Kwarizmi",
        "account_id": "MD887492889",
        "account_type": "savings",
        "balance": 267914296,
        "last_updated": datetime.datetime.now(),
    },
]
