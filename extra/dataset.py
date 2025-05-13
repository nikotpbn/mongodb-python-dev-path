import datetime
from bson.objectid import ObjectId

podcasts = [
    {
        "_id": ObjectId("68237ae23934ecd422a6dddb"),
        "title": "Deletion Test",
        "platforms": ["Apple Podcasts", "Spotify"],
        "downloads": 8024,
        "uploaded": datetime.datetime(2022,7,2)
    },
    {
        "_id": ObjectId("68237ae23934ecd422a6dddc"),
        "title": "The DB Podcast",
        "platforms": ["Apple Podcasts", "Spotify"],
        "downloads": 6014,
        "uploaded": datetime.datetime(2020,4,28)
    },
    {
        "_id": ObjectId("68237ae23934ecd422a6dddd"),
        "title": "The DB Podcast",
        "platforms": ["Apple Podcasts", "Spotify"],
        "downloads": 6014,
        "uploaded": datetime.datetime(2020,4,28)
    },
    {
        "_id": ObjectId("68237ae23934ecd422a6ddde"),
        "title": "Syntax Errors",
        "subscribers": 1,
        "category": "crime",
        "description": "Missing comma? Straight to Jail."
    },
    {
        "_id": ObjectId("68237ae23934ecd422a6dddf"),
        "title": "The Unsolved Crimes Of Philiadelphia",
        "subscribers": 3,
        "category": "crime",
        "description": "It's not always Sunny in Philiadelphia."
    },
    {
        "_id": ObjectId("68237ae23934ecd422a6dde0"),
        "title": "Murder Podcast",
        "subscribers": 10,
        "category": "crime",
        "description": "Explaining cold-case murders"
    },

]

grades = [
    {
        "student_id": 546799,
        "scores": [{"type": "quizz", "score": 50}, {"type": "homework", "score": 70}],
        "class_id": 551,
    },
    {"student_id": 777777, "scores": [{"type": "quizz", "score": 72}], "class_id": 550},
    {"student_id": 223344, "scores": [{"type": "exam", "score": 45}], "class_id": 551},
]

post = {
    "title": "Coffee",
    "content": "Darkly colored, bitter, and slightly acidic, coffee has a stimulating effect on humans",
}

books = [
    {
        "title": "MongoDB in Action",
        "isbn": "1935182870",
        "pageCount": 0,
        "publishedDate": datetime.datetime(2011, 12, 12),
        "thumbnailUrl": "http://s3.amazonaws.com/AKIAJC5RLADLUMVROFDQ-book-thumb-images/banker.jpg",
        "shortDescription": "MongoDB in Action is a comprehensive guide to mongoDB",
        "longDescription": "MongoDB is a document-oriented database that's highly scalable and delivers very high-performance",
        "status": "TO BE CHANGED",
        "authors": ["Kyle Banker"],
        "categories": ["Next Generation Database"],
        "instock": False,
    },
    {
        "title": "A test document",
        "isbn": "0000000000",
        "pageCount": 0,
        "publishedDate": datetime.datetime(2011, 12, 13),
        "thumbnailUrl": "http://s3.amazonaws.com/AKIAJC5RLADLUMVROFDQ-book-thumb-images/banker.jpg",
        "shortDescription": "A dummy document for mongoDB",
        "longDescription": "An extra document to test MongoDB updateMany() in unit8 of Developer Path",
        "status": "TO BE CHANGED",
        "authors": ["Jonh Doe"],
        "categories": ["Next Generation Database"],
        "instock": False,
    },
]
