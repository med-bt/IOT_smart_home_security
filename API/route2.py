from fastapi import FastAPI
from bson import ObjectId
import numpy as np
from schema2 import list_deseri
from RAdatabase2 import collection
from fastapi import APIRouter,HTTPException
from baseclass import BaseClass
import RestApi
router =APIRouter()

@router.get("/")
async def get_iots():
    iots=list_deseri(collection.find())
    return iots

@router.post("/data")
def post(iot:BaseClass):
    collection.insert_one(dict(iot))

@router.post("/predict/")
def predict(item: BaseClass):
    try:
        features = np.array(item.features).reshape(1, -1)
        prediction = RestApi.model2.predict(features)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))