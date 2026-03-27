import streamlit as st
import joblib
import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("Insurance1.jpg")

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
}}
</style>
""", unsafe_allow_html=True)

model = joblib.load("model_columns.pkl")

st.title("Insurance Price Prediction App")

age = st.number_input("Age", 1, 100)
bmi = st.number_input("BMI", 10.0, 50.0)

sex = st.selectbox("Gender", ["male", "female"])
children = st.selectbox("Children", ["yes", "no"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Encoding
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0
children = 1 if children == "yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

if st.button("Predict Insurance Premium"):
    prediction = model.predict([[
        age,
        bmi,
        children,
        sex,
        smoker,
        region_northwest,
        region_southeast,
        region_southwest
    ]])
    
    st.success(f"Estimated Insurance Cost: ₹ {prediction[0]:,.2f}")