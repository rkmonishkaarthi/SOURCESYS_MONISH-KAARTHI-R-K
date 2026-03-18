import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Public Transport Analysis App")

st.sidebar.header("Controls")

num_rows = st.sidebar.slider(
    "Select number of rows",
    min_value=10,
    max_value=100,
    value=50
)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Dataset Validation
    required_columns = [
        "Date",
        "Subways: Total Estimated Ridership",
        "Buses: Total Estimated Ridership",
        "LIRR: Total Estimated Ridership",
        "Metro-North: Total Estimated Ridership"
    ]

    if not all(col in data.columns for col in required_columns):
        st.error("❌ Uploaded file does not have required columns")
        st.stop()

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
    data = data.head(num_rows)

    st.write("Cleaned Data")
    st.write(data.head())

    # Stats
    avg_subway = np.mean(data["Subways"])
    avg_bus = np.mean(data["Buses"])

    col1, col2 = st.columns(2)
    col1.metric("Average Subway", int(avg_subway))
    col2.metric("Average Bus", int(avg_bus))

    # Charts

    # Line Chart
    fig, ax = plt.subplots()
    ax.plot(data["Date"], data["Subways"], label="Subways")
    ax.plot(data["Date"], data["Buses"], label="Buses")
    ax.set_title("Public Transport Ridership Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Passengers")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)

    # Bar Chart
    transport = ["Subways", "Buses", "LIRR", "MetroNorth"]
    avg_values = [
        data["Subways"].mean(),
        data["Buses"].mean(),
        data["LIRR"].mean(),
        data["MetroNorth"].mean()
    ]

    fig2, ax2 = plt.subplots()
    ax2.bar(transport, avg_values)
    ax2.set_title("Average Transport Ridership")
    ax2.set_xlabel("Transport Type")
    ax2.set_ylabel("Average Passengers")
    ax2.grid(True)

    # Scatter Plot
    fig3, ax3 = plt.subplots()
    ax3.scatter(data["Buses"], data["Subways"])
    ax3.set_title("Bus vs Subway Ridership")
    ax3.set_xlabel("Bus Passengers")
    ax3.set_ylabel("Subway Passengers")
    ax3.grid(True)

    # Chart Selector
    st.subheader("Select Visualization")

    chart_option = st.selectbox(
        "Choose Chart",
        ["Line Chart", "Bar Chart", "Scatter Plot"]
    )

    if chart_option == "Line Chart":
        st.pyplot(fig)

    elif chart_option == "Bar Chart":
        st.pyplot(fig2)

    elif chart_option == "Scatter Plot":
        st.pyplot(fig3)

    csv = data.to_csv(index=False)

    st.download_button(
        label="Download Cleaned Data",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

else:
    st.warning("Please upload a CSV file")