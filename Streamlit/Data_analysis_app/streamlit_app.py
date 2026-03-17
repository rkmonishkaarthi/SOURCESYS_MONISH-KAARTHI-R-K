import streamlit as st
import pandas as pd
import numpy as np

st.title("Public Transport Analysis App")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())

    # Data cleaning
    data = data[[
        "Date",
        "Subways: Total Estimated Ridership",
        "Buses: Total Estimated Ridership",
        "LIRR: Total Estimated Ridership",
        "Metro-North: Total Estimated Ridership"
    ]]

    data.columns = ["Date", "Subways", "Buses", "LIRR", "MetroNorth"]

    data["Date"] = pd.to_datetime(data["Date"])
    data = data.dropna()
    data = data.head(50)

    st.write("Cleaned Data")
    st.write(data.head())

    # Stats
    avg_subway = np.mean(data["Subways"])
    avg_bus = np.mean(data["Buses"])

    col1, col2 = st.columns(2)
    col1.metric("Average Subway", int(avg_subway))
    col2.metric("Average Bus", int(avg_bus))

else:
    st.warning("Please upload a CSV file")