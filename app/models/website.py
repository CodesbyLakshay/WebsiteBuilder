from app import mongo
from bson import ObjectId

class Website:
    @staticmethod
    def find_all():
        return mongo.db.websites.find()

    @staticmethod
    def find_by_id(id):
        return mongo.db.websites.find_one({'_id': ObjectId(id)})

    @staticmethod
    def insert(data):
        return mongo.db.websites.insert_one(data).inserted_id

    @staticmethod
    def update(id, data):
        mongo.db.websites.update_one({'_id': ObjectId(id)}, {'$set': data})

    @staticmethod
    def delete(id):
        mongo.db.websites.delete_one({'_id': ObjectId(id)})
