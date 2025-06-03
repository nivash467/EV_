import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("⚡ Electric Vehicle Adoption Tracker")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("e:\python assignment 3\ev_data.csv", parse_dates=["date"])

df = load_data()

# Line Plot: EV growth trend
st.subheader("EV Registration Growth Over Time")
fig_line = px.line(df, x="date", y="ev_sales", color="city", title="EV Growth Trend")
st.plotly_chart(fig_line)

# Bar Plot: Charging stations by city
st.subheader("Charging Stations by City")
stations_sum = df.groupby("city")["charging_stations"].max().reset_index()
fig_bar = px.bar(stations_sum, x="city", y="charging_stations", title="Stations by City")
st.plotly_chart(fig_bar)

# Heatmap: EV registrations by region
st.subheader("EV Registrations Heatmap (Region vs Date)")
pivot_df = df.pivot_table(values="ev_sales", index="region", columns="date", aggfunc="sum")
fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(pivot_df, cmap="YlGnBu", ax=ax)
st.pyplot(fig)
