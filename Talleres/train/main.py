from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import requests
import os
import numpy as np
import pandas as pd

import sqlalchemy as db
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from joblib import dump, load

import penguin_train
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

cvs_penguins = pd.read_csv('data/penguins_size.csv')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

        
@app.get('/train_model')
def train_model(model):
        if model == 'penguins_data':
            penguin_metrics = penguin_train.train_model('penguins_data')
            return penguin_metrics
        else:
            raise HTTPException(status_code=500, detail="Unkown dataset: "+model)
