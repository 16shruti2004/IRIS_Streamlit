import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title("Iris Flower Species Predictor 🌼")
st.markdown("Toy model to play to classify iris flowers into \
setosa, versicolor, virginica")

# User Inputs
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Prediction Button
if st.button("Predict"):
    input_data = [sepal_length, sepal_width, petal_length, petal_width]
    species = predict(input_data)
    st.success(f"Predicted Species: **{species}**")
