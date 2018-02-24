from pymongo import MongoClient

class PymongoClient():
    def __init__(self):
        client = MongoClient()
        client = MongoClient('mongodb://localhost:27017/')
        db = client['reddit_database']
        self.collection = db['daily_programmer_ideas']

    def get_collection(self):
        return self.collection
PymongoClient().get_collection().find_one({"url": str(response.url)})