from pymongo import MongoClient
from mongoengine import connect
from dotenv import dotenv_values


"""Settings"""
config = dotenv_values(".env")
username = config['MONGODB_LOGIN']
password = config['MONGODB_PASSWORD']

"""
Підключення за допомогою MongoClient
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.j1abi6t.mongodb.net/?retryWrites=true&w=majority")
db = client.vsm
"""

"""Підключення за допомогою ODM mongoengine"""
connect(host=f"mongodb+srv://{username}:{password}@cluster0.j1abi6t.mongodb.net/vsm?authSource=admin&ssl=true")
