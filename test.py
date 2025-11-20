import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
try:
    df = pd.read_csv("mushroom_data.csv")
except FileNotFoundError:
    print("Error: 'mushroom_data.csv' not found.")
    print("Please run 'simulate_data.py' first to generate the data.")
    exit()

print("Data loaded successfully.")

# --- Feature Engineering ---
# In this simple case, our features are the raw sensor data.
# The target is the 'condition' column.

# Define features (X) and target (y)
features = ['temperature', 'humidity', 'co2_level']
target = 'condition'

X = df[features]
y = df[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training model with {len(X_train)} samples...")

# --- Model Training ---
# We'll use a RandomForestClassifier, which is robust and works well.
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

print("Model trained.")

# --- Model Evaluation ---
# Predict on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Data: {accuracy * 100:.2f}%")

# --- Model Saving ---
# Save the trained model to a file
model_filename = "mushroom_ai_model.pkl"
joblib.dump(model, model_filename)

print(f"Model saved successfully as '{model_filename}'.")