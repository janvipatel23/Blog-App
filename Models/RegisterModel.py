import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.CodeWizard
        self.Users = self.db.users

    def insert_user(self, data):
        hased = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.Users.insert({"username": data.username, "name": data.display_name, "password": hased, "email": data.email})
        print("data is", data)
