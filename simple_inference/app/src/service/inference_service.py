import requests
import os
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from joblib import load
from ..core.inference_core import InferenceCore
from ..dto.wine import Wine
from ..dto.house import House

app = FastAPI()
inference_core = InferenceCore()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/train_model")
async def train_model(data: str = 'wine'):
    inference_core.get_data(data)
    model_metrics = inference_core.train_model(data)
    return model_metrics


@app.post("/do_inference")
async def train_model(wine: Wine, house: House, model: str = 'wine'):
    if not os.path.isfile(inference_core.get_path() + '/model/' + model + '_model.joblib'):
        raise HTTPException(status_code=500, detail="Unkown model: " + model + " Try to train model first.")
    model_loaded = load(inference_core.get_path() + '/model/' + model + '_model.joblib')
    result_dict: List
    if model == 'wine':
        result_dict = [wine.dict()]
    else:
        result_dict = [house.dict()]

    return int(model_loaded.predict(pd.DataFrame(result_dict))[0])
