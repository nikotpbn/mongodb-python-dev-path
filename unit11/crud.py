import pprint


def unit11(client):

    result = client.sample_training.zips.aggregate(
        [
            {"$match": {"state": "CA"}},
            {"$group": {"_id": "$city", "totalZips": {"$count": {}}}},
        ]
    )


    pprint.pp([x for x in result])