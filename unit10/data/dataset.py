from bson.objectid import ObjectId
from bson.decimal128 import Decimal128

import datetime

transactions = [
    {
        "_id": ObjectId("6825f06998552c2e961fb3aa"),
        "account_holder": "Coskim Demirbas",
        "account_id": "MDB574189300",
        "account_type": "checking",
        "balance": 4690.87,
        "transfers_complete": [
            "TR488315128",
            "TR401633822"
        ]
    },
    {
        "_id": ObjectId("6825f06998552c2e961fb3aa"),
        "account_holder": "Marcus Jorgensen",
        "account_id": "MD009122931",
        "account_type": "checking",
        "balance": 2522.14,
        "transfers_complete": [
            "TR488315128",
            "TR655897500"
        ]
    },
]

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
    {
        "_id": ObjectId("6826fd694315a5a3d5e42814"),
        "account_holder": "Kate Stone",
        "account_id": "MDB333829449",
        "account_type": "checking",
        "balance": Decimal128("4688"),
        "transfers_complete": [
            "TR854412948",
            "TR413308451",
            "TR328708274",
            "TR192714918",
            "TR263422717",
        ],
        "last_updated": datetime.datetime.now(),
    },
    {
        "account_id": "MDB156014571",
        "account_holder": "Adelen Værnes",
        "account_type": "savings",
        "balance": 1519.62,
        "transfers_complete": [
            "TR670287839",
            "TR679752211",
            "TR854525844",
            "TR762109284",
        ],
    },
    {
        "account_id": "MDB190468049",
        "account_holder": "Louis Lewis",
        "account_type": "savings",
        "balance": 4155.67,
        "transfers_complete": [
            "TR859060098",
            "TR729044189",
            "TR126484922",
            "TR617907396",
            "TR598541455",
        ],
    },
    {
        "account_id": "MDB870205338",
        "account_holder": "Juan Perez",
        "account_type": "checking",
        "balance": 1907.8,
        "transfers_complete": [
            "TR432759196",
            "TR797654953",
            "TR391563093",
            "TR464853424",
            "TR922604241",
        ],
    },
]
