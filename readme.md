# SmartMush - 🍄 Smart Mushroom Farm Monitoring System

The **Smart Mushroom Farm Monitoring System** is an AI-powered IoT project designed to monitor and optimize environmental conditions for mushroom cultivation.  
It uses simulated or real sensor data (temperature, humidity, and CO₂) to predict whether the farm environment is **optimal** or **suboptimal** for growth.  
The system can also be expanded to automatically control devices like fans, humidifiers, or heaters.

---

## 🚀 Features

- Real-time monitoring of temperature, humidity, and CO₂ levels  
- AI-based condition prediction (Optimal / Suboptimal)  
- Simple web dashboard using **Streamlit**  
- Optional hardware integration using **Arduino** or **Raspberry Pi**  
- Expandable to include automation and alert systems  

---

## 🧠 Tech Stack

- **Python** – Core logic, simulation, and machine learning  
- **scikit-learn** – AI model training and prediction  
- **pandas** – Data handling and CSV storage  
- **Streamlit** – Real-time dashboard visualization  
- **joblib** – Model saving and loading  
- *(Optional)* Arduino / Raspberry Pi for real sensor input  

---

## 📁 Project Structure

```
smart-mushroom-farm/
│
├── mushroom_data.csv              # Simulated dataset
├── simulate_data.py               # Script to generate fake sensor data
├── train_model.py                 # Trains the AI model
├── dashboard.py                   # Streamlit app for real-time monitoring
├── mushroom_ai_model.pkl          # Trained AI model (auto-generated)
└── README.md                      # Project documentation
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/SmartMush.git
cd SmartMush
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

*(Create a `requirements.txt` with the following:)*
```
pandas
scikit-learn
streamlit
joblib
```

### 3. Generate simulated sensor data
```bash
python simulate_data.py
```

### 4. Train the AI model
```bash
python train_model.py
```

### 5. Run the dashboard
```bash
streamlit run dashboard.py
```

---

## 📊 Dashboard Preview

The dashboard allows you to:
- Adjust temperature, humidity, and CO₂ levels with sliders  
- See instant AI predictions  
- Get visual feedback on farm conditions  

Example output:
```
Model Accuracy: 97.5%
✅ Conditions are ideal for mushroom growth!
```

---

## 🔧 Future Enhancements

- Integration with live IoT sensors (DHT11, MQ135)  
- Automated control system for fans and humidifiers  
- SMS or WhatsApp alerts for farm owners  
- Historical data visualization and analytics  


## 💡 Inspiration

This project was inspired by the need to bring **AI and IoT solutions** to small-scale agriculture, helping mushroom farmers monitor and maintain ideal growth conditions efficiently and sustainably.
