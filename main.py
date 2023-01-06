from fastapi import FastAPI
from model.model import model
from model.model import predict_cost
from sklearn.preprocessing import MinMaxScaler
import pickle
import pandas as pd
import numpy as np

app=FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.post("/predictions/{predictions}")
def predict(response):
    answer=predict_cost(response,model)
    return {"answer": answer}