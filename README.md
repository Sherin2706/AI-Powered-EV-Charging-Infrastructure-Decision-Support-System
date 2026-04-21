# ⚡ AI-Powered EV Charging Infrastructure Decision Support System

## 📌 Overview
With the rapid adoption of electric vehicles (EVs), efficient planning of charging infrastructure has become a critical challenge. This project presents a data-driven decision support system that analyzes EV charging station data to identify demand patterns, optimize infrastructure, and recommend optimal locations for new stations.

---

## 🎯 Objectives
- Analyze EV charging station usage patterns
- Identify high-demand and underutilized regions
- Recommend optimal locations for new charging stations
- Improve infrastructure efficiency and user experience

---

## 🚀 Features
- 📊 Exploratory Data Analysis (EDA)
- 🧠 Demand segmentation (Low / Medium / High)
- 🗺️ Geospatial visualization using interactive maps
- 📍 Recommendation engine for station placement and upgrades
- 🎛️ Interactive dashboard built with Streamlit
- 🔊 Voice-enabled recommendation output

---

## 🧰 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Folium (for maps)
- gTTS (for voice output)

---

## 📂 Dataset
- EV Charging Stations Dataset (Global)
- Includes location, usage, cost, capacity, availability, and more

> Note: Dataset may have limited entries for specific regions like India.

---

## 🧠 Approach

### 1. Data Preprocessing
- Cleaned and formatted dataset
- Handled data types and feature selection

### 2. Feature Engineering
- Created demand levels based on usage
- Derived availability flags

### 3. Exploratory Data Analysis
- Analyzed usage patterns, cost impact, and distance relationships

### 4. Recommendation System
- Built rule-based logic to:
  - Suggest new station locations
  - Recommend capacity upgrades
  - Improve availability and service quality

### 5. Dashboard Development
- Built interactive UI using Streamlit
- Integrated map-based visualization
- Enabled user-driven filtering and scenario testing

---

## 🗺️ Dashboard Components

### 🔹 Charging Stations Map
Displays all stations with demand-based color coding.

### 🔹 Recommended Locations Map
Highlights areas where new stations should be installed.

### 🔹 Insights Table
Shows station-level data with recommendations.

### 🔹 Scenario Testing
Allows users to input custom values and receive recommendations.

---

## 💡 Key Insights
- High-demand areas often lack sufficient infrastructure
- Distance from city impacts station usage
- Capacity constraints lead to overcrowding in some locations

---

## 📈 Business Impact
- Supports data-driven infrastructure planning
- Reduces cost of unnecessary investments
- Improves EV user experience
- Enables scalable EV ecosystem development

---

## 🧪 Limitations
- Dataset is partially synthetic and may lack strong predictive signals
- Limited regional coverage (e.g., India)

---

## 🔮 Future Improvements
- Integrate real-time data from IoT sensors
- Add traffic and population density data
- Improve ML-based demand prediction
- Deploy as a cloud-based application

---

## ▶️ How to Run

```bash
pip install streamlit folium streamlit-folium gtts pandas
streamlit run app.py


👤 Author

SHERIN.V

⭐ Acknowledgment

Dataset sourced from OpenChargeMap (public API)
