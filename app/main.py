from fastapi import FastAPI
from pydantic import BaseModel
# from app.models.model import predict_cost
# from app.models.model import __version__ as model_version

app=FastAPI()

class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_cost(payload.text)
    return {"language": language}