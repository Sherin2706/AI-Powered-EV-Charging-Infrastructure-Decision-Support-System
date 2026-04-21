import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from gtts import gTTS

# -------------------- LOAD DATA --------------------
df = pd.read_csv("detailed_ev_charging_stations.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Rename important columns (adjust if needed)
df.rename(columns={
    'usage_stats_(avg_users/day)': 'usage',
    'cost_(usd/kwh)': 'cost',
    'distance_to_city_(km)': 'distance',
    'charging_capacity_(kw)': 'capacity',
    'reviews_(rating)': 'rating'
}, inplace=True)

# -------------------- FEATURE ENGINEERING --------------------
df['availability_flag'] = df['availability'].apply(lambda x: 1 if x == '24/7' else 0)

def demand_level(x):
    if x > 80:
        return 'High'
    elif x > 50:
        return 'Medium'
    else:
        return 'Low'

df['demand_level'] = df['usage'].apply(demand_level)

# -------------------- RECOMMENDATION ENGINE --------------------
def recommend(row):
    if row['usage'] > 80 and row['distance'] > 10:
        return "Build new station"
    elif row['capacity'] < 40 and row['usage'] > 60:
        return "Increase capacity"
    elif row['availability_flag'] == 0:
        return "Make it 24/7"
    elif row['rating'] < 3:
        return "Improve service quality"
    else:
        return "System OK"

df['recommendation'] = df.apply(recommend, axis=1)

# -------------------- VOICE FUNCTION --------------------
def speak(text):
    tts = gTTS(text)
    file = "output.mp3"
    tts.save(file)
    return file

# -------------------- SIDEBAR FILTERS --------------------
st.sidebar.header("🔍 Filters")

demand_filter = st.sidebar.multiselect(
    "Demand Level",
    df['demand_level'].unique(),
    default=df['demand_level'].unique()
)

cost_range = st.sidebar.slider(
    "Cost Range",
    float(df['cost'].min()),
    float(df['cost'].max()),
    (float(df['cost'].min()), float(df['cost'].max()))
)

# Apply filters
filtered_df = df[
    (df['demand_level'].isin(demand_filter)) &
    (df['cost'] >= cost_range[0]) &
    (df['cost'] <= cost_range[1])
]

# -------------------- TITLE --------------------
st.title("⚡ EV Charging Decision Support Dashboard")

# -------------------- METRICS --------------------
col1, col2, col3 = st.columns(3)
col1.metric("Total Stations", len(filtered_df))
col2.metric("Avg Usage", round(filtered_df['usage'].mean(), 2))
col3.metric("Avg Rating", round(filtered_df['rating'].mean(), 2))

# -------------------- MAP --------------------
st.subheader("🗺️ Charging Stations Map")

m = folium.Map(
    location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()],
    zoom_start=4
)

for _, row in filtered_df.iterrows():
    color = "green" if row['demand_level']=="Low" else "orange" if row['demand_level']=="Medium" else "red"

    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color=color,
        fill=True,
        popup=f"""
        Usage: {row['usage']} <br>
        Cost: {row['cost']} <br>
        Recommendation: {row['recommendation']}
        """
    ).add_to(m)

st_folium(m, width=700)

# -------------------- RECOMMENDED LOCATIONS --------------------
st.subheader("📍 Recommended New Station Locations")

recommended = filtered_df[filtered_df['recommendation'] == "Build new station"]

if not recommended.empty:
    st.map(recommended[['latitude', 'longitude']])
else:
    st.info("No high-priority locations found")

# -------------------- TABLE --------------------
st.subheader("📊 Recommendations Table")

st.dataframe(filtered_df[['usage','distance','capacity','rating','recommendation']])

# -------------------- SCENARIO TESTING --------------------
st.sidebar.header("🧪 Test Scenario")

cost = st.sidebar.slider("Cost", 0.1, 0.5, 0.3)
distance = st.sidebar.slider("Distance", 0, 20, 10)
capacity = st.sidebar.slider("Capacity", 10, 100, 50)
rating = st.sidebar.slider("Rating", 1.0, 5.0, 4.0)

if st.sidebar.button("🔊 Get Recommendation + Voice"):
    
    if distance > 10:
        result = "High demand area detected. Build a new charging station."
    elif capacity < 40:
        result = "Increase charging capacity at this station."
    elif rating < 3:
        result = "Improve service quality for better user satisfaction."
    else:
        result = "System is operating efficiently."

    st.sidebar.success(result)

    audio_file = speak(result)
    st.audio(audio_file)