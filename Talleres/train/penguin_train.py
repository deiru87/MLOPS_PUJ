from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import sqlalchemy as db
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
import pymysql

import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
from sklearn import metrics


def get_data(data):
    if data == 'penguins_data':

        engine = create_engine(
            "mysql+pymysql://" + os.environ["USER_DB"] + ":" + os.environ["PASS_DB"] + "@" + os.environ["IP_SERVER"] + "/" + os.environ["NAME_DB"])
        with engine.connect() as conn:
            query = 'SELECT species, island, culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g, sex FROM '+data
            if (db.inspect(conn).has_table('penguins_data')==True):
                print("TIENE TABLA")
                df_db = pd.read_sql_query(sql=text(query), con=conn)
            else:
                print("NO TIENE TABLA")
                df = pd.read_csv('data/penguins_size.csv')
                df.to_sql(con=engine, index_label='id', name='penguins_data', if_exists='replace')
                df_db = pd.read_sql_query(sql=text(query), con=conn)
        return df_db
    else:
        raise HTTPException(status_code=500, detail="Unkown dataset: "+data)




def train_model(data):
    df = get_data(data)
    df = df.dropna()
    df['species'].replace(['Adelie', 'Chinstrap', 'Gentoo'],
                        [0,1,2], inplace=True)
    df['island'].replace(['Torgersen', 'Biscoe', 'Dream'],
                        [0,1,2], inplace=True)
    df['sex'].replace(['MALE', 'FEMALE'],
                        [0,1], inplace=True)
    X = df.drop('species', axis=1)
    y = df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    expected_y = y_test
    predicted_y = model.predict(X_test)
    model_metrics = metrics.classification_report(expected_y, predicted_y, output_dict=True,zero_division=1)
    dump(model, "/train/model/" + data +'_model.joblib')
    return model_metrics
