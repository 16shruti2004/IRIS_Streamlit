# Iris Species Predictor 🌼

## Overview
This project aims to build a machine learning-based Iris flower species predictor using Python and Streamlit. 
It uses a trained Random Forest Classifier to classify Iris flowers into three species: Setosa, Versicolor, and Virginica 
based on their sepal and petal measurements.

## Dataset
- The project utilizes the Iris dataset, a well-known dataset in machine learning, containing 150 instances of Iris flowers with four feature measurements:- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)
- Class Label (Species name)
- The dataset is stored in data/iris.csv.

  ## Implementation Steps
  
  1. Model Development (model.py)
  - Load and preprocess the dataset.
  - Train a **Random Forest Classifier**.
  - Evaluate the model using accuracy metrics.
  - Save the trained model using `joblib`.
    
  2. Prediction Logic (`prediction.py`)
  - Load the trained model.
  - Implement a function that takes user input and returns the predicted species.
 
  3. Streamlit App (`app.py`)
  - Build a simple **user interface** using Streamlit.
  - Users input measurements through sliders.
  - Predictions are dynamically displayed.
 
    
## **Project Structure**
```
project_root/
│── data/
│   └── iris.csv  # Dataset
│── model/
│   └── iris_model.pkl  # Trained model
│── app.py  # Streamlit application
│── model.py  # Model training script
│── prediction.py  # Prediction function
│── README.md  # Project documentation
```

## **Deployment**
- Run the Streamlit app locally:
  ```bash
  streamlit run app.py
  ```
- Can be deployed online using **Streamlit Community Cloud**, **Heroku**, or **Docker**.

This project provides a hands-on way to implement **Machine Learning**, **Model Deployment**, and **Interactive Applications** using Streamlit. 
  


