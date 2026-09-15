import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="World Weather Dashboard", layout="wide")

st.title("World Weather Dashboard")
st.write("Explore current weather data scraped from timeanddate.com using the filters below.")

with sqlite3.connect("weather.db") as connection:
    weather_data = pd.read_sql_query("SELECT * FROM weather", connection)

weather_data["temperature_value"] = weather_data["Temperature"].str.extract(r"(-?\d+)").astype(float)

available_cities = sorted(weather_data["City"].unique())
selected_cities = st.multiselect("Select cities", available_cities)

min_temperature = int(weather_data["temperature_value"].min())
max_temperature = int(weather_data["temperature_value"].max())
selected_temperature_range = st.slider(
    "Temperature range (\u00b0F)", min_temperature, max_temperature, (min_temperature, max_temperature)
)

filtered_weather_data = weather_data.copy()
if selected_cities:
    filtered_weather_data = filtered_weather_data[filtered_weather_data["City"].isin(selected_cities)]
filtered_weather_data = filtered_weather_data[
    (filtered_weather_data["temperature_value"] >= selected_temperature_range[0])
    & (filtered_weather_data["temperature_value"] <= selected_temperature_range[1])
]

bar_chart_figure = px.bar(
    filtered_weather_data,
    x="City",
    y="temperature_value",
    title="Temperature by City",
    labels={"City": "City", "temperature_value": "Temperature (\u00b0F)"},
)
st.plotly_chart(bar_chart_figure, use_container_width=True)

histogram_figure = px.histogram(
    filtered_weather_data,
    x="temperature_value",
    title="Distribution of Temperatures",
    labels={"temperature_value": "Temperature (\u00b0F)"},
)
st.plotly_chart(histogram_figure, use_container_width=True)

time_chart_figure = px.bar(
    filtered_weather_data,
    x="Time",
    y="temperature_value",
    color="City",
    barmode="group",
    title="Temperature by Local Time",
    labels={"Time": "Local Time", "temperature_value": "Temperature (\u00b0F)"},
)
st.plotly_chart(time_chart_figure, use_container_width=True)

st.dataframe(filtered_weather_data[["City", "Temperature", "Time"]], use_container_width=True)