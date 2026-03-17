import streamlit as st

st.title("🎓 Student Information App")
st.header("Enter Student Details")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)
department = st.selectbox("Select your department",
                         ["CSE", "IT", "ECE", "EEE", "Mechanical"])
gender = st.radio("Select your gender", ["Male", "Female", "Other"])
skills = st.text_input("Enter your skills")
rating = st.slider("Rate your coding skills", 1, 10)

uploaded_image = st.file_uploader("Upload Student Image", type=["jpg", "png", "jpeg"])

if st.button("Submit"):

    if name == "":
        st.warning("Please enter your name!")
    else:
        st.success("Submitted Successfully!")

        if uploaded_image is not None:
            st.image(uploaded_image, caption="Student Image")

        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Department:", department)
        st.write("Gender:", gender)
        st.write("Skills:", skills)
        st.write("Rating:", rating)