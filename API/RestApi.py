import pickle
import joblib
from fastapi import FastAPI,Path
from pydantic import BaseModel
from route2 import router
from ml_model import model2
app=FastAPI()
app.include_router(router)
#model = joblib.load("model.pkl")
#model = pickle.load(open('model.pkl', 'rb'))
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://admin:test@cluster0.9lip2wo.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
