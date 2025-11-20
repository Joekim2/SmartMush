import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train():
    # 1. Load Data
    try:
        df = pd.read_csv('mushroom_data.csv')
    except FileNotFoundError:
        print("❌ Error: 'mushroom_data.csv' not found. Run simulate_data.py first.")
        return

    X = df[['Temperature', 'Humidity', 'CO2_Level']]
    y = df['Growth_Class']

    # 2. Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Train Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4. Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # 5. Save Model
    joblib.dump(model, 'mushroom_ai_model.pkl')
    print("✅ Model saved as 'mushroom_ai_model.pkl'")

if __name__ == "__main__":
    train()