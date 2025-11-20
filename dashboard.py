import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests

# --- 1. CONFIGURATION & SETUP ---
st.set_page_config(
    page_title="SmartMush AI",
    page_icon="🍄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Load Assets
lottie_mushroom = load_lottieurl("https://lottie.host/5a609b25-150c-4858-9a65-16b38018ba22/2Q8s8F8F8F.json")

# --- 2. THEME ENGINE ---
# We place this at the top so it applies immediately
with st.sidebar:
    st.title("⚙️ Settings")
    # The Switch
    dark_mode = st.toggle("🌙 Dark Mode", value=True) 

# Define colors based on the switch
if dark_mode:
    theme_bg = "#0E1117"
    theme_text = "#FAFAFA"
    theme_card = "#262730"
    theme_plot = "plotly_dark"
    metric_text_color = "#FFFFFF"
else:
    theme_bg = "#FFFFFF"
    theme_text = "#000000"
    theme_card = "#F0F2F6"
    theme_plot = "plotly_white"
    metric_text_color = "#000000"

# Custom CSS Injection
st.markdown(f"""
    <style>
    /* Main Background */
    .stApp {{
        background-color: {theme_bg};
        color: {theme_text};
    }}
    
    /* Sidebar Background (Optional override) */
    [data-testid="stSidebar"] {{
        background-color: {theme_card};
    }}

    /* Metric Cards */
    .stMetric {{
        background-color: {theme_card};
        border-left: 5px solid #4CAF50;
        padding: 10px;
        border-radius: 5px;
        color: {metric_text_color} !important;
    }}
    
    /* Force text colors for headers */
    h1, h2, h3, p, span {{
        color: {theme_text} !important;
    }}
    
    /* Toast Styling */
    div[data-testid="stToast"] {{
        background-color: #4CAF50;
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOAD MODEL ---
try:
    model = joblib.load('mushroom_ai_model.pkl')
except FileNotFoundError:
    st.error("⚠️ Model missing! Please run `train_model.py` first.")
    st.stop()

# --- 4. SIDEBAR CONTROLS ---
with st.sidebar:
    st.divider()
    st.title("🎛 Control Panel")
    
    with st.container():
        st.write("Adjust environmental sensors:")
        temp = st.slider("Temperature (°C)", 10.0, 35.0, 22.0, 0.1)
        humidity = st.slider("Humidity (%)", 30.0, 100.0, 85.0, 0.1)
        co2 = st.slider("CO2 Level (ppm)", 300.0, 2000.0, 600.0, 10.0)

    st.divider()
    st.markdown("### 🤖 System Logs")
    st.code(f"Sensors Active...\nT={temp}°C | H={humidity}%", language="bash")

# --- 5. MAIN PREDICTION LOGIC ---
input_data = pd.DataFrame([[temp, humidity, co2]], columns=['Temperature', 'Humidity', 'CO2_Level'])
prediction = model.predict(input_data)[0]
proba = model.predict_proba(input_data)[0]
confidence = proba[prediction] * 100

# Dynamic Toast
if prediction == 1:
    st.toast('Conditions are OPTIMAL! 🍄', icon="✅")
else:
    st.toast('Warning: Conditions Suboptimal!', icon="⚠️")

# --- 6. DASHBOARD LAYOUT ---

col_header_1, col_header_2 = st.columns([3, 1])
with col_header_1:
    st.title("SmartMush: AI Farm Monitor")
    st.markdown("### Intelligent Environmental Analysis System")
    st.markdown("Dashboard monitoring real-time growth conditions for **Oyster Mushrooms**.")
with col_header_2:
    if lottie_mushroom:
        st_lottie(lottie_mushroom, height=150, key="mushroom_anim")
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/2909/2909937.png", width=100)

st.divider()

# Metrics Row
col1, col2, col3 = st.columns(3)

with col1:
    status_color = "normal" if prediction == 1 else "inverse"
    label_text = "OPTIMAL" if prediction == 1 else "SUBOPTIMAL"
    st.metric("Growth Status", label_text, delta="Stable" if prediction == 1 else "Needs Attention", delta_color=status_color)

with col2:
    # Gauge Chart with Theme Awareness
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = confidence,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "AI Confidence"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#4CAF50" if prediction == 1 else "#FF5252"},
            'steps': [{'range': [0, 50], 'color': "gray"},
                      {'range': [50, 100], 'color': "white" if dark_mode else "lightgray"}]
        }
    ))
    # Apply the theme logic
    fig_gauge.update_layout(
        height=150, 
        margin=dict(l=10,r=10,t=30,b=10),
        template=theme_plot, # SWITCHES PLOTLY THEME
        paper_bgcolor="rgba(0,0,0,0)", # Transparent background
        font={'color': theme_text}
    )
    st.plotly_chart(fig_gauge, use_container_width=True)

with col3:
    st.subheader("💡 AI Recommendation")
    if prediction == 1:
        st.success("System running perfectly.")
        if confidence > 90:
            st.balloons()
    else:
        if temp > 24: st.error("❄️ COOLING NEEDED: Temp is too high.")
        elif temp < 18: st.warning("🔥 HEATING NEEDED: Temp is too low.")
        if humidity < 80: st.info("💧 HUMIDIFIER: Increase moisture.")
        if co2 > 1000: st.warning("💨 VENTILATION: CO2 levels critical.")

st.divider()

# --- 7. INTERACTIVE ANALYSIS CHART ---
st.subheader("📊 3D Parameter Analysis")

# Dummy Data Generation
import numpy as np
np.random.seed(42)
demo_data = pd.DataFrame({
    'Temperature': np.random.uniform(10, 35, 100),
    'Humidity': np.random.uniform(30, 100, 100),
    'Status': np.random.choice(['Historical', 'Historical'], 100)
})

current_point = pd.DataFrame({
    'Temperature': [temp],
    'Humidity': [humidity],
    'Status': ['CURRENT READING']
})
chart_data = pd.concat([demo_data, current_point])

fig = px.scatter(
    chart_data, 
    x="Temperature", 
    y="Humidity", 
    color="Status",
    size="Temperature",
    color_discrete_map={'CURRENT READING': 'red', 'Historical': '#00B4D8'},
    title="Environmental Sweet Spot Analysis"
)

fig.add_shape(type="rect",
    x0=18, y0=80, x1=24, y1=100,
    line=dict(color="Green"),
    fillcolor="lightgreen",
    opacity=0.2,
    layer="below"
)

# Apply the theme logic here too
fig.update_layout(
    template=theme_plot, # SWITCHES PLOTLY THEME
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font={'color': theme_text},
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

st.caption("SmartMush System v1.0")