# 🍄 SmartMush: AI-Powered Farm Monitoring System

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-FF4B4B)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)

**SmartMush** is an intelligent IoT dashboard designed to optimize the growth of **Oyster Mushrooms**. It uses a Random Forest Machine Learning model to analyze environmental sensor data (Temperature, Humidity, CO₂) and provides real-time feedback to farmers.

---

## 🚀 Key Features

* **🧠 AI-Driven Predictions:** Instantly classifies growth conditions as *Optimal* or *Suboptimal*.
* **📊 Interactive Dashboard:** Built with Streamlit, featuring live Lottie animations and Plotly interactive charts.
* **🌗 Dark/Light Mode:** Fully functional theme toggle for day/night monitoring.
* **🐋 Dockerized:** Containerized application for consistent deployment across any device.
* **🧪 Robust Testing:** Integrated unit tests to ensure model reliability.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit (Python)
* **ML Engine:** Scikit-learn (Random Forest Classifier)
* **Visualization:** Plotly Interactive Charts
* **Deployment:** Docker
* **Data Handling:** Pandas & NumPy

---

## 📂 Project Structure

```text
SmartMush/
├── dashboard.py           # Main application (Streamlit)
├── train_model.py         # Script to train the AI model
├── simulate_data.py       # Generates synthetic training data
├── test.py                # Unit tests for the system
├── mushroom_ai_model.pkl  # Pre-trained AI model
├── Dockerfile             # Docker configuration
└── requirements.txt       # Python dependencies