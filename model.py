import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load the dataset
df = pd.read_csv("Iris.csv")
df.sample(frac = 1, random_state = 42)

# Prepare features and labels
X = df.iloc[:, 1:5]  # Sepal & Petal measurements
y = df["Class Label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model
joblib.dump(model, "rf_model.sav")
print("Model saved successfully!")

#iris_model.pkl