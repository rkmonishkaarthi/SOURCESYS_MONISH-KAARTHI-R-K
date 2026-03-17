import streamlit as st

st.title("Public Transport Analysis App")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully")