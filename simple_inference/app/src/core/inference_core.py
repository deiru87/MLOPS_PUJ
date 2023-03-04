from fastapi import HTTPException
import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from sklearn import preprocessing


class InferenceCore:
    url_wine = 'https://docs.google.com/uc?export=download&id=1ZsJWYHxcEdJQdb62diQf8o3fvXFawt1a'
    url_house_price = 'https://docs.google.com/uc?export=download&id=1WsTJN-u4YRrPKqJTp8h8iUSAdfJC8_qn'

    def __init__(self):
        pass

    def get_data(self, data: str = 'wine') -> None:
        if data == 'wine' or data == 'house_price':
            if not os.path.isfile(self.get_path() + data + '.csv'):
                url = self.url_wine if data == 'wine' else self.url_house_price
                r = requests.get(url, allow_redirects=True)
                open(self.get_path() + "/dataset/" + data + '.csv', 'wb').write(r.content)
        else:
            raise HTTPException(status_code=500, detail="Unkown dataset: " + data)

    def train_model(self, data: str = 'wine') -> any:
        if not os.path.isfile(self.get_path() + "/dataset/" + data + '.csv'):
            raise HTTPException(status_code=500, detail="Unkown dataset: " + data)
        df = pd.read_csv(self.get_path() + "/dataset/" + data + '.csv')
        df.columns = df.columns.str.replace(' ', '_')

        is_house = False

        if data == 'wine':
          X = df.drop('quality', axis=1)
          y = df['quality']
        else:
          X = df.drop(['date', 'price', 'street', 'city', 'statezip', 'country'], axis=1)
          y = df['price']
          is_house = True

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

        if is_house:
            label_encoder = preprocessing.LabelEncoder()
            y_train = label_encoder.fit_transform(y_train)
            y_test = label_encoder.fit_transform(y_test)

        model = SVC()
        model.fit(X_train, y_train)
        expected_y = y_test
        predicted_y = model.predict(X_test)
        model_metrics = metrics.classification_report(expected_y, predicted_y, output_dict=True, zero_division=1)
        dump(model, self.get_path() + '/model/' + data + '_model.joblib')

        return model_metrics

    @staticmethod
    def get_path() -> str:
        return '/app/app'
