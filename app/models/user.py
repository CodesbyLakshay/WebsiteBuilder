# app/models/user.py
from app import mongo
from bson import ObjectId

class User:
    @staticmethod
    def find_all():
        return mongo.db.users.find()

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def update_role(user_id, role):
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': {'role': role}})

    def save(self):
        mongo.db.users.insert_one({
            'email': self.email,
            'password': self.password,
            'role': self.role
        })

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role
