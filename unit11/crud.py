import pprint


def unit11(client):

    result = client.sample_training.zips.aggregate(
        [
            {"$match": {"state": "CA"}},
            {"$group": {"_id": "$city", "totalZips": {"$count": {}}}},
        ]
    )
    pprint.pp([x for x in result])

    result = client.sample_training.zips.aggregate(
        [
            { "$sort": { "pop": -1 } },
            { "$limit": 3 }
        ]
    )
    pprint.pp([x for x in result])

    result = client.sample_training.zips.aggregate(
        [{"$project": {"stage": 1, "zip": 1, "population": "$pop", "_id": 0}}]
    )
    pprint.pp([x for x in result])

    result = client.sample_training.zips.aggregate(
        [
            { "$set": {
                "pop_2022": { "$round": { "$multiply": [ 1.0031, "$pop"] } }
            } }
        ]
    )
    pprint.pp([x for x in result])

    result = client.sample_training.zips.aggregate(
        [
            { "$count": "total_zips" }
        ]
    )
    pprint.pp([x for x in result])