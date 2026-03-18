import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Universal Data Analysis App")

# Sidebar
st.sidebar.header("Controls")

num_rows = st.sidebar.slider(
    "Select number of rows",
    min_value=10,
    max_value=200,
    value=50
)

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV safely
    data = pd.read_csv(uploaded_file, on_bad_lines='skip')

    # Clean column names
    data.columns = data.columns.astype(str).str.strip()

    # Fix duplicate column names
    new_cols = []
    seen = {}

    for col in data.columns:
        if col in seen:
            seen[col] += 1
            new_cols.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            new_cols.append(col)

    data.columns = new_cols  # ✅ Correct placement

    st.subheader("Raw Data")
    st.write(data.head())

    # Column selection
    st.subheader("Select Columns")

    columns = data.columns.tolist()

    date_col = st.selectbox("Select Date Column", columns)
    num_col1 = st.selectbox("Select First Numeric Column", columns)
    num_col2 = st.selectbox("Select Second Numeric Column", columns)

    # Convert date safely
    try:
        data[date_col] = pd.to_datetime(data[date_col])
    except:
        st.warning("Could not convert selected date column")

    # Ensure numeric columns
    try:
        data[num_col1] = pd.to_numeric(data[num_col1])
        data[num_col2] = pd.to_numeric(data[num_col2])
    except:
        st.error("Selected columns must be numeric")
        st.stop()

    # Filter data
    data = data[[date_col, num_col1, num_col2]].dropna()
    data = data.head(num_rows)

    st.subheader("Processed Data")
    st.write(data.head())

    # Metrics
    avg1 = data[num_col1].mean()
    avg2 = data[num_col2].mean()

    col1, col2 = st.columns(2)
    col1.metric(f"Average {num_col1}", int(avg1))
    col2.metric(f"Average {num_col2}", int(avg2))

    # Charts

    # Line chart
    fig, ax = plt.subplots()
    ax.plot(data[date_col], data[num_col1], label=num_col1)
    ax.plot(data[date_col], data[num_col2], label=num_col2)
    ax.set_title("Trend Analysis")
    ax.set_xlabel(date_col)
    ax.set_ylabel("Values")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)

    # Bar chart
    fig2, ax2 = plt.subplots()
    ax2.bar([num_col1, num_col2], [avg1, avg2])
    ax2.set_title("Average Comparison")
    ax2.grid(True)

    # Scatter plot
    fig3, ax3 = plt.subplots()
    ax3.scatter(data[num_col1], data[num_col2])
    ax3.set_title("Relationship Analysis")
    ax3.set_xlabel(num_col1)
    ax3.set_ylabel(num_col2)
    ax3.grid(True)

    # Chart selector
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

    # Download
    csv = data.to_csv(index=False)

    st.download_button(
        label="Download Processed Data",
        data=csv,
        file_name="processed_data.csv",
        mime="text/csv"
    )

else:
    st.warning("Please upload a CSV file")