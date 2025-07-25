import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample location at KLCC
data = {
    "name": ["KLCC"],
    "latitude": [3.15687],
    "longitude": [101.71473],
    "address": ["Kuala Lumpur City Centre, 50088 Kuala Lumpur"]
}
df = pd.DataFrame(data)

st.set_page_config(page_title="Food Composting Locator", layout="wide")

st.title("Food Composting Locator demo")
st.write("Testing demo.")

# Center map view
map_center = [df["latitude"].mean(), df["longitude"].mean()]
m = folium.Map(location=map_center, zoom_start=15)

# Add marker
for _, row in df.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"<b>{row['name']}</b><br>{row['address']}",
        tooltip=row["name"],
        icon=folium.Icon(color="green", icon="map-marker", prefix="fa")
    ).add_to(m)

# Display map in Streamlit
st_folium(m, width=800, height=500)
