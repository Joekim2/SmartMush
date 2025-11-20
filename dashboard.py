import streamlit as st
import pandas as pd
import joblib
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="SmartMush Dashboard 🍄",
    page_icon="🍄",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Model Loading ---
MODEL_FILE = "mushroom_ai_model.pkl"

@st.cache_resource
def load_model(model_path):
    """Loads the trained model from disk."""
    if not os.path.exists(model_path):
        return None
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model(MODEL_FILE)

# --- Main Application ---
st.title("🍄 Smart Mushroom Farm Monitoring")

if model is None:
    st.error(
        f"**Model file not found!**\n\n"
        f"Please make sure the file `{MODEL_FILE}` is in the same directory. "
        f"You may need to run `train_model.py` first."
    )
else:
    st.markdown("""
    Adjust the sliders below to simulate the current conditions in your mushroom farm. 
    The AI will predict whether the environment is **optimal** or **suboptimal** for growth.
    """)

    # --- Sidebar for Input ---
    st.sidebar.header("Live Sensor Simulation")
    
    # Sliders for user input
    temp = st.sidebar.slider(
        "🌡️ Temperature (°C)", 
        min_value=10.0, 
        max_value=40.0, 
        value=22.5,  # Default optimal value
        step=0.5
    )
    
    humidity = st.sidebar.slider(
        "💧 Humidity (%)", 
        min_value=50.0, 
        max_value=100.0, 
        value=90.0,  # Default optimal value
        step=1.0
    )
    
    co2 = st.sidebar.slider(
        "💨 CO₂ Level (ppm)", 
        min_value=300.0, 
        max_value=2000.0, 
        value=600.0,  # Default optimal value
        step=25.0
    )

    # --- Prediction ---
    # Create a DataFrame from the inputs, matching the model's training format
    input_data = pd.DataFrame(
        [[temp, humidity, co2]],
        columns=['temperature', 'humidity', 'co2_level']
    )

    # Make prediction
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)

    # --- Display Results ---
    st.subheader("🤖 AI Prediction")
    
    # Get the confidence score
    confidence = prediction_proba.max() * 100

    if prediction == "Optimal":
        st.success(f"**✅ Optimal** (Confidence: {confidence:.2f}%)")
        st.markdown(
            "The current conditions are **ideal** for mushroom growth. "
            "Keep maintaining this environment!"
        )
    else:
        st.error(f"**❌ Suboptimal** (Confidence: {confidence:.2f}%)")
        st.markdown(
            "The current conditions are **not ideal**. "
            "One or more sensor values are outside the optimal range. "
            "Please check your farm's controls."
        )

    # Display the current inputs in a clean table
    st.subheader("Current Sensor Readings")
    st.dataframe(input_data.style.format({
        "temperature": "{:.1f} °C",
        "humidity": "{:.0f} %",
        "co2_level": "{:.0f} ppm"
    }))