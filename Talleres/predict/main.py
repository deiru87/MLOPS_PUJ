from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
import penguin
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

app = FastAPI()

@app.post("/predict_model")
async def do_inference(penguin : penguin.Penguin, model:str='penguins_data'):
    if not os.path.isfile('/predict/model/' + model +'_model.joblib'):
        raise HTTPException(status_code=500, detail="Unkown model: "+ model+" Try to train model first.")
    model_loaded = load('/predict/model/' + model +'_model.joblib')
    return int(model_loaded.predict(pd.DataFrame([penguin.dict()]))[0])
