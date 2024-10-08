from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import pandas as pd

# Initialize the FastAPI app
app = FastAPI()

# Load the pre-trained model
model = joblib.load('./Notebooks/credit_scoring_model.pkl')

# Define the input data schema using Pydantic
class CustomerData(BaseModel):
    recency: float
    frequency: int
    monetary: float
    seasonality: float

# Define the root endpoint
@app.get("/")
def root():
    return {"message": "Credit Scoring API is Running"}

# Define the prediction endpoint
@app.post("/predict")
def predict_credit_risk(data: CustomerData):
    # Extract data from the request body
    input_data = np.array([[data.recency, data.frequency, data.monetary, data.seasonality]])

    # Make prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0, 1]

    # Return the prediction and probability
    risk = "High Risk" if prediction == 1 else "Low Risk"
    return {"risk": risk, "default_probability": probability}

