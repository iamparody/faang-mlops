from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
import os
from utils import load_model  


app = FastAPI()

# Load model once at startup
model = load_model("FAANG-Model")  


# Define expected input format
class StockFeatures(BaseModel):
    Prev_Close: float

@app.get("/")
def root():
    return {"message": "FAANG Forecast API is running!"}

@app.post("/predict")
def predict(features: StockFeatures):
    try:
        input_df = pd.DataFrame([features.dict()])
        prediction = model.predict(input_df)
        return {
            "input": features.dict(),
            "prediction": prediction[0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
