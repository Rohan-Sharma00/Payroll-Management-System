from http import client
from typing import Collection
from urllib import response
from django import db
from django.db import connection
from pymongo import MongoClient

connection_string= "mongodb://127.0.0.1:27017/test"
client = MongoClient(connection_string)
db = client.get_database("test")

collection = db.get_collection("New")

document = {
    "name":"Bhavesh",
    "dept":"Science",
    "class":"Mca"
}

response = collection.insert_one(document)
last_inserted_id = response.inserted_id
print("Id is".format(last_inserted_id))