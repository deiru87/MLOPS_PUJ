from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

class Penguin(BaseModel):
    island: float = 1.0
    culmen_length_mm: float = 39.1
    culmen_depth_mm: float = 18.7
    flipper_length_mm: float = 181.0
    body_mass_g: float = 3750.0
    sex: int = 0
