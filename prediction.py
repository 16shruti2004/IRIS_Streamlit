import joblib
import pandas as pd

# Load the trained model
model = joblib.load("rf_model.sav")

def predict (input_features):
    """Function to predict Iris species based on input features"""
    prediction = model.predict([input_features])
    return prediction[0]