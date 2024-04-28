from fastapi import APIRouter
from pymongo import MongoClient

client=MongoClient("mongodb+srv://admin:test@cluster0.9lip2wo.mongodb.net/?retryWrites=true&w=majority")
db=client.iot_db
collection=db["iot_collection"]
