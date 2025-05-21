import pprint

def unit12(client):

    db = client.bank

    accounts_collection = db.accounts

    stage_one = { "$match": { "balance": { "$lt": 1000 } } }
    stage_two = { "$group": { "_id": "$account_type", "avg_balance": { "$avg": "$balance" } } }

    pipeline = [
        stage_one,
        stage_two
    ]

    results = accounts_collection.aggregate(pipeline)
    print()
    print("Average balance of checking and savings accounts with balances lower than a thousand dolalrs")

    pprint.pp([x for x in results])

    conversion_rate_usd_to_gbp = 1.03

    select_accounts = { "$match": { "account_type": "checking", "balance": { "$gt": 1500} } }

    organize_by_original_balance = { "$sort": { "balance": -1 } }

    return_specified_fields = {
        "$project": {
            "account_type": 1,
            "balance": 1,
            "gpb_balance": { "$divide": ["$balance", conversion_rate_usd_to_gbp] },
            "_id": 0,
        }
    }

    pipeline = [
        select_accounts,
        organize_by_original_balance,
        return_specified_fields
    ]

    results = accounts_collection.aggregate(pipeline)

    print("Account type, original balance and balance in GBP of checking accounts with original balance greater than $1,500,"
          "in order from highest original balance to lowest")

    pprint.pp([x for x in results])
